# 第 15 章　数据库迁移、备份与真正的故障恢复

> 本章成果：为订阅管理器增加 `billing_cycle`，用可重复执行的 SQLite 迁移保留旧数据，并实际完成一次备份、恢复和回滚边界演练。

## 1. 本章成果

完成后，项目将从 v1.1 演进到 v1.2，具备以下能力：

- 订阅记录支持 `monthly` 和 `yearly` 两种计费周期，旧记录自动使用 `monthly`。
- 有一份可审查、可在数据库副本上重跑的迁移脚本。
- 能在迁移前生成一致性备份，并把备份恢复成另一个数据库文件进行核验。
- 能解释代码回滚、数据库迁移和数据恢复为什么是三件事。
- 留下迁移测试、恢复手册和一份真实演练记录。

本章使用 Python 标准库 `sqlite3`，不引入新的数据库框架。

## 2. 为什么需要它

新增一个字段看似只是修改 API，实际上会同时改变代码、数据库结构和已有数据。只让 AI 修改模型，旧数据库可能因缺少字段而报错；直接删除数据库重建，则会丢失用户数据。

备份也不等于具备恢复能力。从未恢复过的备份，只说明文件存在，不说明它可用。恢复旧备份还会删除备份之后产生的合法新数据，因此“回到旧版本”不是一个无代价动作。

本章选择**加字段、保留数据、先副本演练**的方式，让变化保持小而可逆。金额继续使用整数分，不因本次迁移改变既有精度约定。

## 3. 最少必备知识

- **Schema**：表包含哪些列，以及类型、默认值和约束。
- **迁移（Migration）**：把数据库从一种 Schema 状态变为另一种状态的受控过程。
- **备份与恢复**：备份生成一致的数据库副本；恢复用副本替换或重建目标数据库。
- **事务**：一组操作要么全部提交，要么全部回滚。SQLite 的 `BEGIN IMMEDIATE` 会在事务开始时取得写锁，适合短迁移。
- **`PRAGMA user_version`**：SQLite 内置的用户 Schema 版本号。本章将 v1.2 的数据库标记为 `1`，它不是应用发布版本号。
- **RPO**：能容忍丢失多少最近数据。本章先不追求自动计算，只需在恢复记录中明确备份时间与其后可能丢失的写入。

## 4. 起始项目状态

从已完成第 12—14 章的 v1.1 项目开始，确认：

1. `data/subscriptions.db` 是实际使用的数据库；若你的配置不同，后续命令统一替换为真实路径。
2. `subscriptions` 表已有 `id`、`name`、`amount`、`currency`、`renewal_date`、`note`、`created_at`。
3. `python -m pytest -q` 和 `python -m ruff check .` 可以作为修改前基线。
4. Git 工作区没有无关修改，数据库文件不会被提交到 Git。

先建立分支并检查现状：

```powershell
git switch -c feat/billing-cycle-migration
git status
python -m pytest -q
python -m ruff check .
```

若基线已经失败，先记录并修复原问题，不要把旧失败混入本次迁移。

## 5. 操作步骤与 AI 任务示例

### 步骤 1：先写变更契约

在 `specs/` 中补充以下规则：新字段名为 `billing_cycle`；仅允许 `monthly`、`yearly`；缺省为 `monthly`；迁移不能删除或重写既有记录；API 必须拒绝其他值。新增字段还应进入创建、编辑、列表和详情流程。

给 AI 的任务应限制实现范围：

```text
目标：为 Subscription Tracker 增加 billing_cycle，并完成 SQLite 数据迁移。
上下文：当前为 v1.1；金额 amount 使用整数分；实际表为 subscriptions；
初始字段见 WRITING_GUIDE.md；核心 API 为 /api/subscriptions。
范围：schemas.py、repository.py、必要的前端表单、迁移脚本、迁移测试和恢复手册。
约束：只允许 monthly/yearly；旧记录默认 monthly；不得删除数据库重建；
不得改变 amount 类型；迁移必须可重复执行；先给计划和影响文件，再修改。
验收：旧行保留且为 monthly；可新增 yearly；非法值被拒绝；重复迁移不新增列；
原有测试与新增测试均执行；恢复脚本可在副本上验证。
输出：变更摘要、逐文件 Diff、执行的命令和真实结果、未完成项与回滚建议。
```

### 步骤 2：在任何迁移前制作一致性备份

新增 `scripts/db_backup.py`。它使用 SQLite 在线备份 API，而不是在数据库仍被写入时直接复制文件：

```python
import argparse
import sqlite3
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--backup", type=Path, required=True)
    args = parser.parse_args()
    database = args.database.resolve()
    backup = args.backup.resolve()
    if not database.is_file():
        parser.error(f"database not found: {database}")
    if backup.exists():
        parser.error(f"refusing to overwrite: {backup}")
    backup.parent.mkdir(parents=True, exist_ok=True)

    source = sqlite3.connect(f"file:{database.as_posix()}?mode=ro", uri=True)
    target = sqlite3.connect(backup)
    try:
        source.backup(target)
        result = target.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError(f"backup integrity_check failed: {result}")
    finally:
        target.close()
        source.close()
    print(f"backup created: {backup}")


if __name__ == "__main__":
    main()
```

备份文件名应包含时间和用途，例如 `backups/before-billing-cycle-2026-11-24.db`。日期使用实际操作日期；脚本拒绝覆盖已有备份。备份文件与数据库一样可能含个人数据，不提交到公开仓库。

### 步骤 3：编写可重复执行的迁移脚本

新增 `scripts/migrate_001_add_billing_cycle.py`：

```python
import argparse
import sqlite3
from pathlib import Path


def column_names(connection: sqlite3.Connection) -> set[str]:
    return {
        row[1]
        for row in connection.execute("PRAGMA table_info(subscriptions)")
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, required=True)
    args = parser.parse_args()
    database = args.database.resolve()
    if not database.is_file():
        parser.error(f"database not found: {database}")

    connection = sqlite3.connect(database, timeout=5)
    try:
        connection.execute("BEGIN IMMEDIATE")
        version = connection.execute("PRAGMA user_version").fetchone()[0]
        if version > 1:
            raise RuntimeError(f"unsupported schema version: {version}")
        if "billing_cycle" not in column_names(connection):
            connection.execute(
                """
                ALTER TABLE subscriptions
                ADD COLUMN billing_cycle TEXT NOT NULL DEFAULT 'monthly'
                CHECK (billing_cycle IN ('monthly', 'yearly'))
                """
            )
        connection.execute("PRAGMA user_version = 1")
        result = connection.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError(f"integrity_check failed: {result}")
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
    print(f"schema version 1 ready: {database}")


if __name__ == "__main__":
    main()
```

`ALTER TABLE ... ADD COLUMN` 让旧行获得默认值，`CHECK` 在数据库层拦截非法值。重复执行时先检查列，因此不会再次添加同名列。幂等不等于可以跳过备份：脚本未来的修改、操作失误和数据问题仍可能产生损失。

### 步骤 4：让应用读写新字段

检查并修改实际实现，而不是只改文档：

- `app/schemas.py`：用 `Literal["monthly", "yearly"]` 或等价校验限制输入，创建模型默认 `monthly`。
- `app/repository.py`：查询列、插入和更新参数都包含 `billing_cycle`，保持参数化 SQL。
- `app/routes.py`：确认响应模型不会把新字段过滤掉。
- `app/static/`：创建和编辑表单提供两个明确选项，列表显示当前周期。
- `tests/`：覆盖旧行迁移、新建 `yearly`、非法输入、重复迁移和原有 API 行为。

迁移测试可在临时目录创建旧 Schema，再用 `subprocess.run` 调用脚本。至少包含以下核心断言，不要使用没有业务断言的空测试：

```python
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "migrate_001_add_billing_cycle.py"


def test_migration_preserves_old_rows_and_rejects_bad_cycle(tmp_path: Path) -> None:
    database = tmp_path / "old.db"
    connection = sqlite3.connect(database)
    connection.execute(
        """
        CREATE TABLE subscriptions (
            id INTEGER PRIMARY KEY, name TEXT NOT NULL, amount INTEGER NOT NULL,
            currency TEXT NOT NULL, renewal_date TEXT NOT NULL,
            note TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL
        )
        """
    )
    connection.execute(
        "INSERT INTO subscriptions VALUES (1, 'Music', 1000, 'CNY', '2027-01-01', '', '2026-01-01T00:00:00Z')"
    )
    connection.commit()
    connection.close()

    for _ in range(2):
        subprocess.run([sys.executable, str(SCRIPT), "--database", str(database)], check=True)

    connection = sqlite3.connect(database)
    try:
        row = connection.execute(
            "SELECT name, amount, billing_cycle FROM subscriptions WHERE id = 1"
        ).fetchone()
        assert row == ("Music", 1000, "monthly")
        assert connection.execute("PRAGMA user_version").fetchone()[0] == 1
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO subscriptions (name, amount, currency, renewal_date, billing_cycle, created_at) VALUES ('Bad', 100, 'CNY', '2027-01-01', 'weekly', '2026-01-01T00:00:00Z')"
            )
    finally:
        connection.close()
```

### 步骤 5：先迁移副本，再处理真实数据库

```powershell
New-Item -ItemType Directory -Force data, backups
Copy-Item data/subscriptions.db data/migration-test.db -Force
python scripts/migrate_001_add_billing_cycle.py --database data/migration-test.db
python -m pytest -q
```

核对副本的行数、旧值和新字段后，停止开发服务器，备份真实数据库，再执行迁移：

```powershell
python scripts/db_backup.py --database data/subscriptions.db --backup backups/before-billing-cycle.db
python scripts/migrate_001_add_billing_cycle.py --database data/subscriptions.db
```

若 `backups/before-billing-cycle.db` 已存在，换一个带实际时间的新文件名，不覆盖旧备份。

### 步骤 6：实现并执行恢复演练

新增 `scripts/db_restore.py`。恢复前先验证备份，并在目标目录生成临时文件；只有验证通过才替换目标：

```python
import argparse
import os
import shutil
import sqlite3
from pathlib import Path


def check(database: Path) -> None:
    connection = sqlite3.connect(f"file:{database.as_posix()}?mode=ro", uri=True)
    try:
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise RuntimeError("integrity_check failed")
        table = connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'subscriptions'"
        ).fetchone()
        if table is None:
            raise RuntimeError("subscriptions table is missing")
    finally:
        connection.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backup", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--confirm-offline", action="store_true")
    args = parser.parse_args()
    if not args.confirm_offline:
        parser.error("stop the application and repeat with --confirm-offline")
    backup = args.backup.resolve()
    target = args.target.resolve()
    if not backup.is_file():
        parser.error(f"backup not found: {backup}")
    check(backup)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.name + ".restoring")
    if temporary.exists():
        parser.error(f"temporary file exists: {temporary}")
    try:
        shutil.copyfile(backup, temporary)
        check(temporary)
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(f"restored: {target}")


if __name__ == "__main__":
    main()
```

第一次演练不要覆盖真实数据库，恢复到一个新文件：

```powershell
python scripts/db_restore.py --backup backups/before-billing-cycle.db --target data/restored-test.db --confirm-offline
python -c "import sqlite3; c=sqlite3.connect('data/restored-test.db'); print(c.execute('SELECT COUNT(*) FROM subscriptions').fetchone()[0]); c.close()"
```

比较恢复文件与备份的行数、关键记录和 Schema。随后把实际备份位置、停止服务命令、恢复命令、核验人和数据丢失窗口写入 `docs/runbooks/database-recovery.md`。

### 步骤 7：演练三种不同的“回滚”

1. **代码回滚**：本次是向后兼容的加列，旧代码不知道新列，但插入仍有数据库默认值。验证旧代码能否读取迁移后的数据库，可以回滚代码而保留新 Schema。
2. **数据恢复**：若恢复迁移前备份，迁移后新增和修改的数据会丢失。先导出或保存当前数据库供核对，不直接覆盖唯一副本。
3. **前向修复**：若数据已经混合、旧备份太旧，通常应在当前状态上修复，而不是强行回到过去。记录选择理由和影响范围。

### 步骤 8：完成端到端验收

启动应用，分别创建月付和年付订阅，编辑其中一条，重新启动后再次检查。最后运行全部测试、Ruff 和 `/health`，保存真实输出作为 v1.2 的验收证据。

## 6. AI 应生成的产物

本章结束时，仓库至少应新增或更新：

- `scripts/db_backup.py`：一致性备份与完整性检查。
- `scripts/migrate_001_add_billing_cycle.py`：加列、约束和 Schema 版本。
- `scripts/db_restore.py`：离线恢复与恢复前校验。
- `tests/test_migration.py`：旧数据保留、非法值和重复执行测试。
- `docs/runbooks/database-recovery.md`：责任人、命令、备份位置和恢复记录。
- 规格、API、前端和数据库访问代码中的 `billing_cycle` 支持。

AI 还应给出实际 Diff 和执行记录。“应该可以”“理论上不会丢数据”不算完成证据。

## 7. 人工检查点

1. **看约束**：数据库和 API 都只允许两个值，默认值确实是 `monthly`。
2. **看旧数据**：比较迁移前后主键、名称、金额、日期和备注，不只比较行数。
3. **看事务**：异常路径有 rollback，脚本不会把空文件当合法旧库。
4. **看备份**：备份文件非空、未被覆盖、未进入 Git，且通过 `integrity_check`。
5. **看恢复**：恢复演练使用了备份而不是原库，应用停止后才替换真实目标。
6. **看回滚假设**：明确哪些旧代码兼容新 Schema，哪些情况需要数据恢复或前向修复。

## 8. 验收命令与通过标准

```powershell
python -m pytest -q
python -m ruff check .
python scripts/migrate_001_add_billing_cycle.py --database data/migration-test.db
python scripts/db_restore.py --backup backups/before-billing-cycle.db --target data/restored-test-2.db --confirm-offline
python -m uvicorn app.main:app
```

另开 PowerShell：

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

通过标准：重复迁移没有重复列错误；旧记录仍为 `monthly`；年付记录可创建；非法周期被 API 和数据库拒绝；恢复文件能打开且关键记录与备份一致；应用健康检查正常；所有结果来自你实际执行的命令。

## 9. 常见失败及恢复方法

- **症状：`duplicate column name`。原因：重复执行了不带列检查的简单 SQL。恢复动作：不要删列；使用本章脚本检查现状，确认 `user_version` 与数据后再继续。**
- **症状：`database is locked`。原因：仍有服务或测试持有写事务。恢复动作：停止写入进程并结束悬挂事务；不要删除 `-wal` 或 `-shm` 文件来“解锁”。**
- **症状：恢复后缺少最近订阅。原因：备份早于这些写入。恢复动作：保留当前库供对账，评估备份时间窗，必要时从当前库导出新增记录后合并。**
- **症状：API 返回 422 但数据库有合法值。原因：Pydantic 模型、前端选项或响应模型未同步。恢复动作：沿请求→Schema→Repository→数据库逐层定位，不放宽数据库约束来掩盖问题。**
- **症状：旧版本代码无法处理迁移后数据库。原因：变更并非向后兼容。恢复动作：停止服务，按恢复手册选择代码修复或数据恢复；先保留故障现场，不反复尝试不同迁移。**

## 10. 本章 Git 提交

建议分支：`feat/billing-cycle-migration`。数据库和备份不提交，代码按可审查单元拆分：

```powershell
git add specs/ app/ tests/test_migration.py
git commit -m "feat: add billing cycle to subscriptions"
git add scripts/db_backup.py scripts/migrate_001_add_billing_cycle.py scripts/db_restore.py
git commit -m "feat: add SQLite migration and recovery tools"
git add docs/runbooks/database-recovery.md
git commit -m "docs: record database recovery drill"
```

实际暂存前运行 `git diff --stat` 和 `git diff`，不要把演练数据库加入提交。全部检查通过后，再将合并后的版本标记为 v1.2。

## 11. 练习与扩展

1. 在临时数据库插入多行旧数据，迁移后逐行比较导出结果，而非只检查行数。
2. 分别在启用和未启用 WAL 的测试数据库上演练备份，记录操作差异。
3. 为迁移测试增加“列已存在但 `user_version` 仍为 0”的场景，讨论应自动修复还是人工介入。
4. 设计下一次新增字段时保持旧代码兼容的规则，并把规则加入 ADR。
5. 将恢复演练加入每月维护日程，记录备份时间、恢复目标和实际发现的问题。

## 12. 参考资料

- [SQLite：ALTER TABLE](https://sqlite.org/lang_altertable.html)——加列语法与限制。
- [Python：sqlite3 Connection.backup](https://docs.python.org/3/library/sqlite3.html#sqlite3).Connection.backup)——一致性备份 API。
- [SQLite：PRAGMA integrity_check](https://sqlite.org/pragma.html#pragma_integrity_chec)k)——数据库完整性检查。
- [SQLite：Transaction](https://sqlite.org/lang_transaction.html)——事务与 `BEGIN IMMEDIATE` 行为。
