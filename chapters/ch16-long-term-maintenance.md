# 第 16 章　长期维护系统：依赖、安全、运行观测与文档漂移

> 本章成果：把一次性维护经验变成定期检查、小 PR、自动门禁和恢复演练，完成 v1.2.1 补丁维护闭环。

## 1. 本章成果

完成后，项目应拥有：

- Renovate 依赖更新配置和人工审查规则。
- 基于 `pip-audit` 的依赖安全检查步骤。
- 真实的 `/health` 检查和结构化请求日志。
- 从 FastAPI 路由自动生成 `docs/generated/routes.md`，并用 CI 发现文档漂移。
- 一个检查项目架构边界的小脚本。
- 周期性“维护垃圾回收”流程和自主度分级规则。
- 多个小 PR 合并后发布 v1.2.1。

本章的重点不是接入更多工具，而是让维护工作可重复、可验收、可交接。

## 2. 为什么需要它

项目上线后，需求变化只是维护的一部分。依赖会过期，安全公告会出现，文档会落后，代码会积累重复实现，服务也需要健康检查和日志。等到所有问题一起爆发再处理，通常只能大规模重写。

更有效的策略是把维护拆成小事件：依赖补丁、文档更新、架构违规清理、回归测试补充和备份演练各自形成小 PR。每个 PR 都应有测试或脚本证明，不能靠“看起来没问题”。OpenAI 把这类持续清理工作比喻为代码库的垃圾回收：定期扫描偏差并打开小的重构 PR，避免技术债复利增长。

## 3. 最少必备知识

- **补丁、次要和主版本升级**：风险依次提高，主版本必须人工评估变更日志和兼容性。
- **Dependency Dashboard**：Renovate 汇总待处理依赖更新的 Issue，避免逐个 PR 淹没维护者。
- **供应链风险**：一个包名或某个版本的代码可能在安装阶段执行，不能只看 README。
- **健康检查**：应用自身报告是否满足最低运行条件，例如数据库可查询。
- **文档漂移**：文档、生成文件和实际代码行为不一致。
- **架构约束**：把模块依赖规则写成可执行检查，而不是只写在 Markdown 中。

## 4. 起始项目状态

从完成第15章的 v1.2 项目开始，确认：

1. `data/subscriptions.db` 已包含 `billing_cycle`，且恢复演练记录存在。
2. `python -m pytest -q` 与 `python -m ruff check .` 当前能通过。
3. GitHub Actions 工作流 `.github/workflows/ci.yml` 已运行测试。
4. Git 工作区干净。

建立维护分支：

```powershell
git switch -c chore/maintenance-v1-2-1
git status
python -m pytest -q
python -m ruff check .
```

## 5. 操作步骤与 AI 任务示例

### 步骤 1：先执行只读维护扫描

把扫描任务交给 AI，但要求只读、分类和给证据，不立即修改：

```text
目标：为 Subscription Tracker 执行一次只读维护扫描。
上下文：v1.2；技术栈 Python/FastAPI/SQLite/pytest/Ruff/GitHub Actions；
核心路径 app/、tests/、scripts/、docs/、.github/workflows/。
范围：依赖更新与安全公告、失败或薄弱测试、重复代码、文档与路由漂移、
架构边界违规、备份/恢复手册缺口、日志与健康检查不足。
约束：本轮不得修改文件；不要凭猜测报告；每项必须给出文件路径、命令或代码证据，
并区分事实、建议和风险。
验收：输出按主题分组，每条含严重性、证据、影响、建议动作、预计范围。
输出：Markdown 维护报告草稿，保存到 docs/maintenance/YYYY-MM-DD-scan.md。
```

先获取当前事实：

```powershell
python -m pip list --outdated
python -m pytest -q
python -m ruff check .
```

记录真实输出，不要只保留 AI 的总结。

### 步骤 2：配置 Renovate

在仓库根目录新增 `renovate.json`：

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "dependencyDashboard": true,
  "dependencyDashboardApproval": true,
  "labels": ["dependencies"],
  "prConcurrentLimit": 2,
  "schedule": ["before 09:00 on Monday"],
  "timezone": "Asia/Shanghai",
  "packageRules": [
    {
      "matchManagers": ["pip_requirements"],
      "matchUpdateTypes": ["patch", "minor"],
      "groupName": "Python patch and minor dependencies"
    },
    {
      "matchManagers": ["pip_requirements"],
      "matchUpdateTypes": ["major"],
      "groupName": "Python major dependencies",
      "automerge": false
    }
  ]
}
```

教程中不开启自动合并。配置提交后，由仓库管理员选择 Renovate GitHub App 或自托管方式。配置生效前，仍可使用 `python -m pip list --outdated` 手动审查。

### 步骤 3：建立依赖安全审查流程

安装并运行 `pip-audit` 作为维护工具：

```powershell
python -m pip install pip-audit
python -m pip-audit -r requirements.txt
```

发现漏洞时的审查顺序：

1. 确认漏洞所在包、受影响版本和修复版本。
2. 检查项目是否真实调用了受影响功能。
3. 优先选择同一大版本内的修复版本。
4. 主版本升级必须阅读变更日志，并在分支中运行全部测试。
5. 若短期无法升级，在 `docs/maintenance/` 记录风险、临时缓解措施和复查日期。
6. 不在公开报告中直接粘贴敏感路径、密钥或内网地址。

### 步骤 4：补充健康检查和请求日志

新增 `app/health.py`：

```python
import os
import sqlite3
from pathlib import Path

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    database = Path(os.getenv("DATABASE_PATH", "data/subscriptions.db"))
    if not database.is_file():
        raise HTTPException(status_code=503, detail="database file is missing")
    try:
        connection = sqlite3.connect(
            f"file:{database.resolve().as_posix()}?mode=ro",
            uri=True,
            timeout=1,
        )
        connection.execute("SELECT 1").fetchone()
        connection.close()
    except sqlite3.Error:
        raise HTTPException(status_code=503, detail="database is unavailable")
    return {"status": "ok", "database": "connected"}
```

在 `app/main.py` 接入路由，并按项目现有导入风格调整：

```python
from app.health import router as health_router

app.include_router(health_router)
```

请求日志只记录方法、路径、状态码和耗时，避免查询参数、请求体和个人数据：

```python
import logging
import time

from fastapi import Request

logger = logging.getLogger("subscription_tracker")


@app.middleware("http")
async def log_request(request: Request, call_next):
    start = time.monotonic()
    response = await call_next(request)
    logger.info(
        "request method=%s path=%s status=%s duration_ms=%.1f",
        request.method,
        request.url.path,
        response.status_code,
        (time.monotonic() - start) * 1000,
    )
    return response
```

新增 `tests/test_health.py`，使用项目已有的 FastAPI 测试客户端：

```python
def test_health_reports_ok(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "connected"}
```

### 步骤 5：生成路由文档并检测漂移

新增 `scripts/export_routes.py`。它从真实应用对象导出路由，而不是让 AI 根据 README 猜接口：

```python
from pathlib import Path

from fastapi.routing import APIRoute

from app.main import app

OUTPUT = Path("docs/generated/routes.md")


def main() -> None:
    rows = []
    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue
        methods = sorted(route.methods - {"HEAD", "OPTIONS"})
        rows.append(f"| {route.path} | {', '.join(methods)} | {route.endpoint.__module__} |")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(
        [
            "# 自动生成的路由清单",
            "",
            "运行 `python scripts/export_routes.py` 更新，不要手工编辑。",
            "",
            "| 路径 | 方法 | 处理模块 |",
            "|---|---|---|",
            *rows,
            "",
        ]
    )
    OUTPUT.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
```

生成后检查文档是否与代码一致：

```powershell
python scripts/export_routes.py
git diff --exit-code -- docs/generated/routes.md
```

若命令返回差异，说明有人修改路由后没有重新生成文档；执行脚本并单独提交结果。

### 步骤 6：把架构边界写成可执行检查

新增 `scripts/check_architecture.py`，检查数据访问和底层模块不反向依赖上层：

```python
import ast
import sys
from pathlib import Path

FORBIDDEN_IMPORTS = {
    Path("app/repository.py"): {"fastapi", "app.routes"},
    Path("app/database.py"): {"fastapi", "app.routes", "app.repository"},
}


def imported_names(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def main() -> int:
    errors = []
    for path, forbidden in FORBIDDEN_IMPORTS.items():
        if not path.exists():
            continue
        for name in imported_names(path):
            if any(name == bad or name.startswith(bad + ".") for bad in forbidden):
                errors.append(f"{path}: forbidden import {name}")
    if errors:
        print("\n".join(errors))
        return 1
    print("architecture checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

运行：

```powershell
python scripts/check_architecture.py
```

发现违规时，移动依赖或调整职责；不要直接删除检查。若项目新增模块，把规则写入脚本和 `ARCHITECTURE.md`，使文字与检查一致。

### 步骤 7：把维护检查接入 CI

在现有 CI 工作流中增加以下步骤，命令应与本地一致：

```yaml
      - name: Check architecture boundaries
        run: python scripts/check_architecture.py
      - name: Regenerate route documentation
        run: python scripts/export_routes.py
      - name: Ensure generated documentation is committed
        run: git diff --exit-code -- docs/generated/routes.md
      - name: Audit Python dependencies
        run: |
          python -m pip install pip-audit
          python -m pip-audit -r requirements.txt
```

`pip-audit` 可能因新公告失败，这正是维护信号；不要为了让 CI 变绿而跳过检查。若漏洞不影响当前使用，记录风险与复查时间，再决定缓解方案。

### 步骤 8：建立每周垃圾回收流程

每周固定一次只读扫描，AI 输出问题清单，人挑选 2—3 个风险最高且范围最小的项目，再让 AI 分别生成小 PR。典型分类：

- 依赖补丁或安全修复
- 文档与生成清单更新
- 重复 helper 合并
- 缺失测试补充
- 架构违规修正
- 运行手册或备份演练更新

自主度从低到高分级：

| 级别 | AI 权限 | 人工职责 |
|---|---|---|
| L0 | 只读扫描和报告 | 审阅全部证据，决定后续动作 |
| L1 | 生成计划和 Diff，不修改文件 | 批准计划后授权实现 |
| L2 | 在隔离分支完成小任务 | 审查 Diff、运行测试并决定是否合并 |
| L3 | CI 失败后提交修复 PR | 检查失败原因、修复范围和回归证据 |
| L4 | 低风险补丁按明确策略自动提 PR | 设定策略、抽查日志，必要时人工合并 |
| L5 | 多环节自动执行 | 只适用于范围、权限、审计和回滚都已固化的任务 |

教程主线建议停在 L2—L3。涉及生产数据、密钥、发布和回滚的操作，必须保留人工审批。

### 步骤 9：发布 v1.2.1

当所有维护 PR 合并、CI 通过后：

```powershell
git switch main
git pull
python -m pytest -q
python -m ruff check .
python scripts/check_architecture.py
python -m pip-audit -r requirements.txt
```

随后按照第11章的发布流程打标签、更新发布说明，并记录每个 PR 解决的问题。补丁版本不应夹带未验收的新功能。

## 6. AI 应生成的产物

本章 AI 应输出：

- 只读维护扫描报告，含证据和风险分级。
- `renovate.json` 及其审查规则说明。
- 依赖安全审查记录。
- 健康检查、日志和测试代码。
- `scripts/export_routes.py`、`scripts/check_architecture.py` 与生成文档。
- CI 工作流更新。
- 每周维护流程和自主度政策。
- 发布 v1.2.1 前的检查清单。

不要把上述内容塞进一个“自动维护”大 Skill；先让每个检查可单独运行和验收。

## 7. 人工检查点

1. **依赖更新是否最小**：PR 只改依赖和相关测试，不夹带功能。
2. **安全公告是否相关**：区分“依赖有漏洞”和“项目调用路径受影响”。
3. **健康检查是否真的检测依赖**：`/health` 不能只返回固定 `ok`。
4. **日志是否安全**：没有密钥、完整查询参数、个人订阅数据或内网地址。
5. **生成文档是否由脚本产生**：人工编辑 `docs/generated/` 会让漂移检查失去意义。
6. **架构检查是否反映真实边界**：不能通过放宽规则或跳过脚本来通过 CI。
7. **维护 PR 是否可独立回滚**：每个 PR 有清晰范围和验收记录。

## 8. 验收命令与通过标准

```powershell
python -m pytest -q
python -m ruff check .
python scripts/check_architecture.py
python scripts/export_routes.py
git diff --exit-code -- docs/generated/routes.md
python -m pip-audit -r requirements.txt
python -m uvicorn app.main:app
```

另开 PowerShell：

```powershell
$health = Invoke-RestMethod http://127.0.0.1:8000/health
if ($health.status -ne "ok") { throw "health check failed" }
$health
```

通过标准：测试、Ruff、架构检查、文档一致性检查和安全审计都有真实结果；健康检查能访问数据库并返回 `ok`；CI 在干净检出中执行同一组检查；所有维护修改由小 PR 组成；发布说明列出变更、风险和回滚方式。

## 9. 常见失败及恢复方法

- **症状：Renovate 一次产生大量 PR。原因：没有分组、排期和并发限制。恢复动作：关闭噪声 PR，更新 `packageRules`、`schedule` 和 `prConcurrentLimit`，先处理补丁与安全公告。**
- **症状：`pip-audit` 持续失败但漏洞似乎无关。原因：存在受影响版本或传递依赖。恢复动作：确认调用路径，优先选择修复版本；无法升级时记录风险、缓解措施和复查日期。**
- **症状：数据库不可用但 `/health` 返回 `ok`。原因：健康检查没有真实查询数据库。恢复动作：加入文件存在性和 `SELECT 1` 检查，异常时返回 503，并补充失败路径测试。**
- **症状：CI 的文档一致性检查失败。原因：路由变化后未重新生成文档。恢复动作：运行导出脚本并提交 `docs/generated/routes.md`，不要手工改生成文件。**
- **症状：架构检查失败。原因：底层模块引入了上层依赖。恢复动作：调整模块职责或依赖方向；不要删除规则，除非 ADR 记录了边界变化。**
- **症状：AI 每周维护报告重复但问题没减少。原因：只扫描不关闭。恢复动作：限制每次最多处理 2—3 个事项，为每项指定 PR、验收证据和复查日期。**

## 10. 本章 Git 提交

建议按主题拆分 PR，而不是一个“维护大杂烩”：

```powershell
git add renovate.json docs/maintenance/
git commit -m "chore: add dependency maintenance policy"

git add app/health.py app/main.py tests/test_health.py
git commit -m "feat: add database-aware health check"

git add scripts/export_routes.py docs/generated/routes.md
git commit -m "docs: generate API route inventory"

git add scripts/check_architecture.py .github/workflows/ci.yml
git commit -m "ci: enforce architecture and generated docs"
```

实际执行前使用 `git diff --stat` 检查每个 PR 的影响范围。维护日志、扫描报告和发布说明应随对应 PR 或发布流程提交。

## 11. 练习与扩展

1. 模拟一次补丁升级失败：在分支中安装一个旧版本依赖，记录失败测试、根因和恢复步骤。
2. 故意在 `app/database.py` 中加入一个上层导入，观察架构检查如何阻止合并，然后修复违规。
3. 连续四周执行只读维护扫描，统计每类问题数量和平均关闭时间。
4. 为 `/health` 增加数据库文件缺失或不可读的失败测试，验证返回 503。
5. 把当前自主度政策写成 `docs/maintenance/autonomy.md`，明确哪些操作永远需要人工批准。
6. 选择一个真实依赖公告，完成影响分析、升级测试和发布记录。

## 12. 参考资料

- [Renovate：Configuration options](https://docs.renovatebot.com/configuration-options/)——分组、排期、审批和并发限制。
- [Renovate：Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/)——集中管理待处理更新。
- [pip-audit](https://github.com/pypa/pip-audit)——Python 依赖漏洞扫描。
- [FastAPI：Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)——请求日志中间件。
- [OpenAI：Harness Engineering](https://openai.com/zh-Hant/index/harness-engineering/)——持续清理代码库与工程反馈回路。
