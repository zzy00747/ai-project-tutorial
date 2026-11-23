# 第 11 章　CI、发布与部署：从本地能跑到别人能用

> 本章成果：把测试、代码检查、CSV 导出验收、发布记录和部署检查固化成可重复流程，得到 Subscription Tracker 的 v1.0 候选版本。

## 1. 本章成果

完成本章后，你应该拥有：

1. `.github/workflows/ci.yml`：在每次 push、pull request 和手动触发时运行安装、检查、测试与语法编译。
2. 一次**干净环境复现**：从远程仓库重新克隆，安装依赖，运行全部检查。
3. `.env.example`：记录非敏感运行配置，明确哪些内容不能提交。
4. `scripts/verify_csv_export.py`：独立验收 CSV 导出的响应类型、列名、中文、逗号和实际创建的数据行。
5. `docs/runbooks/deploy-v1.md`：部署前置条件、部署步骤、健康检查和冒烟检查。
6. `docs/runbooks/rollback-v1.md`：代码回滚、数据边界和失败后的恢复动作。
7. v1.0 发布说明模板：把“完成”变成可检查的证据。

本章不要求你一定拥有公网服务器。没有服务器时，可以完成本地发布候选版本和部署演练；**不要把本地运行结果写成生产部署成功**。

## 2. 为什么需要它

本地测试通过并不等于项目可交付。它至少可能隐藏四类问题：

1. **环境差异**：你本地缓存了依赖、环境变量或数据库文件，干净环境却缺少它们。
2. **配置漂移**：代码依赖某个未在仓库中说明的变量或默认路径。
3. **验收缺口**：页面能打开，不代表 CSV 的编码、列名、逗号转义和数据内容都正确。
4. **恢复缺口**：部署失败后，如果没有已知良好版本、健康检查和回滚步骤，就只能临时猜测。

CI 的价值是把验收命令绑定到具体 commit；发布流程的价值是把版本、配置、健康检查和回滚路径写下来。对 AI 生成的项目尤其如此：AI 可以写出看起来合理的代码，但“它说完成了”不能作为交付证据。

## 3. 最少必备知识

- **CI（Continuous Integration）**：自动执行安装、检查和测试，验证某个 commit 是否满足门禁。
- **Workflow / Job / Step**：GitHub Actions 中，workflow 是完整流程，job 是运行单元，step 是其中一条命令或动作。
- **Artifact**：构建、测试或发布产生的可保存文件。
- **Tag 与 Release**：tag 标记具体 commit，release 面向人提供版本说明和下载入口。
- **配置与密钥**：普通配置可以公开示例，密钥只能通过 Secret Manager 或平台 Secrets 注入。
- **健康检查（health check）**：判断进程和基础依赖是否响应。
- **冒烟检查（smoke test）**：验证一个最关键用户流程是否真的可用。
- **回滚**：恢复到已知良好版本；代码回滚不等于数据库恢复。

## 4. 起始项目状态

本章假设你已经完成第 9 章和第 10 章，当前项目应至少具备：

- `/health` 健康检查端点。
- `/api/subscriptions` 的增删改查。
- `GET /api/subscriptions/export` CSV 导出。
- 能覆盖核心行为和 CSV 导出的测试。
- `requirements.txt` 中包含运行、测试和 Ruff 所需依赖。
- 上下文文档 `AGENTS.md`、`docs/project-map.md`、`docs/handoff.md` 已存在。

创建发布分支：

```powershell
git switch -c ci/release-v1
git status --short
python -m pytest -q
python -m ruff check .
```

如果这些命令失败，先修复，不要开始发布流程。

## 5. 操作步骤与 AI 任务示例

### 5.1 确认本地合同

先在本地启动应用：

```powershell
python -m uvicorn app.main:app --reload
```

在另一个终端检查健康端点：

```powershell
curl.exe --fail --show-error --silent http://127.0.0.1:8000/health
```

macOS/Linux：

```bash
curl --fail --show-error --silent http://127.0.0.1:8000/health
```

记录实际状态码和响应体。健康检查通过只说明服务基础可用，不能代替 CSV 导出和 UI 流程验收。

### 5.2 添加 GitHub Actions CI

让 AI 生成初稿时，必须限定范围和命令：

```text
目标：为 Subscription Tracker 创建 GitHub Actions CI。
上下文：只读取 README.md、AGENTS.md、requirements.txt、pytest 配置（如有）、tests/ 目录结构。
范围：只新增 .github/workflows/ci.yml，不修改业务代码、测试或依赖。
约束：
1. 使用 Python 3.12。
2. 在 push 到 main、pull request 到 main 和 workflow_dispatch 时运行。
3. 设置 permissions: contents: read。
4. 步骤依次执行：checkout、setup-python、安装 requirements.txt、ruff check、pytest、compileall app。
5. 不部署，不使用 secrets，不发布 Release。
6. 不添加 badge、缓存策略以外的花哨配置。
7. 本地命令必须与 CI 命令一致。
验收：YAML 可被 GitHub Actions 解析，任一检查失败时 workflow 失败。
输出：完整 workflow 文件、每步目的、可能导致本地与 CI 结果不一致的因素。
```

人工审查后，可采用这个完整 workflow：

```yaml
name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  verify:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r requirements.txt

      - name: Lint with Ruff
        run: python -m ruff check .

      - name: Run tests
        run: python -m pytest -q

      - name: Compile application package
        run: python -m compileall -q app
```

说明：

- `actions/checkout@v4` 和 `actions/setup-python@v5` 使用主版本标签，便于教学阅读。生产项目可进一步固定到完整 commit SHA，以降低供应链风险。
- `permissions: contents: read` 遵循最小权限原则；当前 CI 不需要写仓库。
- `workflow_dispatch` 允许你在没有新提交时手动复跑。
- `compileall` 不能代替测试，它只检查 Python 文件能否编译。

### 5.3 干净环境复现

本地通过不等于干净环境通过。把项目推送到远程后，从一个新目录克隆：

```powershell
cd ..
git clone <YOUR_REPO_URL> subscription-tracker-clean
cd subscription-tracker-clean
git switch <CI_BRANCH_OR_TAG>
python -m venv .venv
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ruff check .
python -m pytest -q
python -m compileall -q app
```

每条命令都必须返回成功状态。若失败，优先检查：

- 依赖是否漏写进 `requirements.txt`；
- 测试是否依赖你本地已有数据库或缓存文件；
- 是否读取了未提交的 `.env`；
- Python 小版本是否与 CI 不同；
- 代码是否依赖 Windows 路径分隔符。

### 5.4 配置与密钥

新增 `.env.example`，只写非敏感示例：

```dotenv
# Copy this file to .env for local development only.
# Do not commit .env or any real credential.
APP_ENV=development
DATABASE_PATH=data/subscriptions.db
LOG_LEVEL=INFO

# Deployment placeholders. Real values belong in your secret manager.
# DEPLOY_HOST=
# DEPLOY_USER=
# DEPLOY_TOKEN=
```

如果你的代码目前还没有集中读取这些变量，不要在发布说明中声称“已支持环境变量配置”。可以先完成这个受控 AI 任务：

```text
目标：为 Subscription Tracker 增加集中运行时配置。
上下文：读取 AGENTS.md、docs/project-map.md、app/database.py、app/main.py、tests/。
范围：新增 app/config.py，并让 SQLite 数据库路径通过配置读取。
约束：
1. 保留公开 API 不变。
2. 不引入新依赖。
3. 测试必须使用临时数据库，不得读写 data/subscriptions.db。
4. 不提交 .env。
5. 默认值保持当前本地开发行为不变。
6. 只修改实现配置所需的最小文件。
验收：python -m pytest -q 与 python -m ruff check . 通过；设置 DATABASE_PATH 后，应用使用指定路径。
输出：变更文件列表、配置字段说明、需要人工确认的风险。
```

一个最小配置示例：

```python
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_env: str
    database_path: str
    log_level: str


def load_settings() -> Settings:
    return Settings(
        app_env=os.getenv("APP_ENV", "development"),
        database_path=os.getenv("DATABASE_PATH", "data/subscriptions.db"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
```

密钥规则：

- `.env` 必须被 `.gitignore` 忽略。
- 真实密钥不进入源码、CI YAML、日志、发布说明和截图。
- GitHub Actions 中通过 Secrets 注入，不把 secret 打印到日志。
- 当前 CI 只做检查和测试，不需要部署密钥；不要为了“看起来高级”提前添加部署权限。

### 5.5 验收 CSV 导出

CSV 很容易出现三类问题：响应类型错误、UTF-8 BOM 或编码错误、含逗号字段没有正确引用。下面脚本会创建一个带中文和逗号的测试订阅，导出 CSV，找到该行，验证列名和内容，最后删除测试数据。

新增 `scripts/verify_csv_export.py`：

```python
#!/usr/bin/env python3
"""Verify CSV export against a disposable local Subscription Tracker instance.

Usage:
    python scripts/verify_csv_export.py [BASE_URL]

The default base URL is http://127.0.0.1:8000. This script creates one test
subscription, exports CSV, verifies the created row, and then deletes the test
subscription. Do not run it against production data unless you have an approved
temporary database and understand that it performs a DELETE request.
"""

from __future__ import annotations

import csv
import io
import json
import sys
import urllib.error
import urllib.request
import uuid

DEFAULT_BASE_URL = "http://127.0.0.1:8000"
EXPECTED_COLUMNS = [
    "id",
    "name",
    "amount",
    "currency",
    "renewal_date",
    "note",
    "created_at",
]


def request_json(url: str, method: str = "GET", payload: dict | None = None):
    data = None
    headers = {"Accept": "application/json"}

    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            body = response.read()
            parsed = json.loads(body.decode("utf-8")) if body else None
            return response.status, parsed
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def fetch_csv(url: str):
    request = urllib.request.Request(url, headers={"Accept": "text/csv"}, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            return response.status, response.headers.get_content_type(), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, "", exc.read()


def delete_quietly(url: str) -> None:
    request = urllib.request.Request(url, method="DELETE")
    try:
        urllib.request.urlopen(request, timeout=10)
    except urllib.error.HTTPError:
        # Cleanup is best-effort; the verification result remains authoritative.
        pass
    except urllib.error.URLError:
        pass


def main() -> int:
    base_url = (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_BASE_URL).rstrip("/")
    marker = f"CSV验收-{uuid.uuid4().hex[:8]}"

    payload = {
        "name": marker,
        "amount": 1299,
        "currency": "CNY",
        "renewal_date": "2027-01-15",
        "note": "含,逗号与中文",
    }

    status, created = request_json(f"{base_url}/api/subscriptions", "POST", payload)
    if status not in (200, 201) or not isinstance(created, dict):
        print(f"FAIL: POST /api/subscriptions returned {status}: {created}")
        return 1

    record_id = created.get("id")
    if record_id is None:
        print(f"FAIL: created subscription response has no id field: {created}")
        return 1

    try:
        status, content_type, body = fetch_csv(f"{base_url}/api/subscriptions/export")
        if status != 200:
            print(f"FAIL: CSV export returned HTTP {status}: {body!r}")
            return 1

        if content_type != "text/csv":
            print(f"FAIL: expected Content-Type text/csv, got {content_type!r}")
            return 1

        text = body.decode("utf-8-sig")
        rows = list(csv.DictReader(io.StringIO(text)))
        if not rows:
            print("FAIL: CSV export contains no data rows")
            return 1

        missing_columns = [column for column in EXPECTED_COLUMNS if column not in rows[0]]
        if missing_columns:
            print(f"FAIL: CSV is missing columns: {missing_columns}")
            return 1

        matched = [row for row in rows if str(row.get("id")) == str(record_id)]
        if len(matched) != 1:
            print(f"FAIL: expected exactly one exported row for id {record_id}, found {len(matched)}")
            return 1

        row = matched[0]
        checks = {
            "name": row.get("name") == marker,
            "amount": row.get("amount") == "1299",
            "currency": row.get("currency") == "CNY",
            "renewal_date": row.get("renewal_date") == "2027-01-15",
            "note": row.get("note") == "含,逗号与中文",
            "created_at_present": bool(row.get("created_at")),
        }
        failed_checks = [key for key, ok in checks.items() if not ok]
        if failed_checks:
            print(f"FAIL: CSV row mismatch: {failed_checks}; row={row}")
            return 1

        print(f"CSV export OK: id={record_id}, marker={marker}, rows={len(rows)}")
        return 0
    finally:
        delete_quietly(f"{base_url}/api/subscriptions/{record_id}")


if __name__ == "__main__":
    raise SystemExit(main())
```

运行方式：

```powershell
python -m uvicorn app.main:app --reload
```

在另一个终端：

```powershell
python scripts/verify_csv_export.py
echo $LASTEXITCODE
```

macOS/Linux：

```bash
python scripts/verify_csv_export.py
echo $?
```

通过标准是脚本退出码为 `0`，并输出以 `CSV export OK` 开头的实际结果。若路由、列名、编码或逗号处理不符合预期，脚本会明确失败。

### 5.6 创建发布候选版本

CI 通过后，再创建 tag。不要先打 tag、后补测试。

```powershell
git status --short
git switch main
git pull --ff-only
git merge --no-ff ci/release-v1
python -m pytest -q
python -m ruff check .
```

打开 GitHub Actions，确认对应 commit 的 workflow 已通过。然后：

```powershell
git tag -a v1.0.0 -m "Release Subscription Tracker v1.0.0"
git push origin v1.0.0
```

发布说明可以使用这个模板：

```markdown
# Subscription Tracker v1.0.0

- Release commit: <git-commit-sha>
- CI run: <workflow-run-url>
- Clean environment verification: <date, operator, result>
- CSV export verification: <command and actual result>
- Deployment target: <none|staging|production>
- Health check URL: <health-url or none>

## Included

- Core subscription CRUD
- CSV export
- Automated CI checks
- Deployment and rollback runbooks

## Known limitations

- <list actual limitations; write none only after checking>

## Rollback plan

- See docs/runbooks/rollback-v1.md
```

所有尖括号必须替换为真实链接、命令输出摘要或明确写 `none`。不要为了美观编造 CI 地址。

### 5.7 部署、健康检查与冒烟检查

下面是一个可调整的 Linux 服务器部署模板。它不会自动适配所有托管平台；`REPO_URL`、路径、服务名、反向代理和证书都需要按你的环境修改。

`docs/runbooks/deploy-v1.md` 示例：

```markdown
# Subscription Tracker v1.0 deployment runbook

## Preconditions

- CI for the exact release tag is green.
- Target host has Python 3.12 and required OS packages.
- Deployment user can read the repository and manage the service.
- Existing production data, if any, has a current backup.
- HTTPS reverse proxy and firewall rules are configured separately.

## Variables

```bash
export REPO_URL="<your-git-repo-url>"
export APP_USER="<deployment-user>"
export APP_HOST="<server-host>"
export APP_DIR="/srv/subscription-tracker"
export RELEASE_TAG="v1.0.0"
export SERVICE_NAME="subscription-tracker"
export HEALTH_URL="https://<your-domain>/health"
```

## Deploy exact release

```bash
ssh "$APP_USER@$APP_HOST"
set -euo pipefail

mkdir -p "$APP_DIR/releases"
cd "$APP_DIR"

git clone --branch "$RELEASE_TAG" --depth 1 "$REPO_URL" "releases/$RELEASE_TAG"
ln -sfn "$APP_DIR/releases/$RELEASE_TAG" "$APP_DIR/current"

cd "$APP_DIR/current"
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ruff check .
.venv/bin/python -m pytest -q
```

## Service unit template

```ini
[Unit]
Description=Subscription Tracker
After=network.target

[Service]
Type=simple
User=appuser
WorkingDirectory=/srv/subscription-tracker/current
EnvironmentFile=/srv/subscription-tracker/shared/app.env
ExecStart=/srv/subscription-tracker/current/.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
```

## Restart and health check

```bash
sudo systemctl restart "$SERVICE_NAME"
curl --fail --show-error --silent "$HEALTH_URL"
```

## Smoke check

1. Open the deployed URL in a browser.
2. Create one clearly named smoke-test subscription.
3. List subscriptions and confirm the record appears.
4. Export CSV and confirm the smoke-test record is present.
5. Delete the smoke-test record.
6. Record who performed the check, when, and the actual result.

## Deployment evidence

- Release tag:
- Deployed commit:
- CI run:
- Health check result:
- Smoke check result:
- Operator:
- Timestamp:
```

如果还没有服务器，可以在本地完成同等演练：用干净 clone、独立虚拟环境、独立数据目录、`uvicorn` 进程、健康检查和 CSV 脚本验收。证据中必须写 `local deployment rehearsal`，不能写成 production。

### 5.8 回滚流程

`docs/runbooks/rollback-v1.md` 示例：

```markdown
# Subscription Tracker rollback runbook

## When to roll back

- Health endpoint does not return success after deployment.
- Core create/list/export flow fails.
- A required configuration or dependency is missing.
- Automated checks fail on the deployed release.

## Code rollback

```bash
export APP_DIR="/srv/subscription-tracker"
export SERVICE_NAME="subscription-tracker"
export PREVIOUS_RELEASE="<last-known-good-tag>"

ln -sfn "$APP_DIR/releases/$PREVIOUS_RELEASE" "$APP_DIR/current"
sudo systemctl restart "$SERVICE_NAME"
curl --fail --show-error --silent "$HEALTH_URL"
```

## First-release failure

If v1.0 is the first deployed version and no previous release exists, do not invent a rollback target. Stop or disable the public service, restore the prior infrastructure state, and record the failure evidence.

## Database boundary

A code rollback does not reverse database records or schema migrations. Before rolling back:

1. Identify whether the failed release changed the database schema.
2. If it did not, code rollback may be sufficient.
3. If it did, restore from an approved backup or apply a forward-fix migration.
4. Never overwrite production data without a backup and an explicit recovery decision.

## Evidence

- Failed release:
- Reason:
- Rollback target or action:
- Health check result:
- Data impact:
- Operator:
- Timestamp:
```

v1.0 如果只引入 CSV 导出和 CI，通常没有数据库 schema 迁移；但你仍应根据实际代码确认这一点，不能照抄本章结论。

## 6. AI 应生成的产物

本章可让 AI 生成以下文件初稿：

```text
.github/workflows/ci.yml
.env.example
scripts/verify_csv_export.py
docs/runbooks/deploy-v1.md
docs/runbooks/rollback-v1.md
docs/runbooks/release-v1.0.0.md
```

AI 还应返回：

- workflow 每个步骤的目的；
- 本地检查与 CI 检查是否一致；
- CSV 验收覆盖了哪些场景；
- 配置项中哪些是非敏感、哪些必须作为 Secret；
- 部署与回滚中需要人工确认的环境差异；
- 未验证项清单。

## 7. 人工检查点

发布前逐项检查：

- CI YAML 是否只运行检查，不偷偷部署或写仓库？
- `permissions` 是否保持 `contents: read`？
- CI 命令是否与本地命令一致？
- `requirements.txt` 是否包含测试、Ruff 和运行所需依赖？
- 干净 clone 是否没有依赖你本地的 `.env`、缓存或 SQLite 文件？
- CSV 脚本是否验证 Content-Type、列名、中文、逗号、实际创建行和清理删除？
- `.env.example` 是否没有真实密钥？
- `.env`、数据库文件和验收产物是否被 `.gitignore` 忽略？
- Release tag 是否指向 CI 通过的那个 commit？
- 健康检查是否只证明服务响应，而不是证明业务流程可用？
- 部署证据是否区分本地演练、staging 和 production？
- 回滚目标是否真实存在，并且数据库兼容性已确认？

## 8. 验收命令与通过标准

本地验收：

```powershell
git status --short
python -m ruff check .
python -m pytest -q
python scripts/verify_csv_export.py
echo $LASTEXITCODE
curl.exe --fail --show-error --silent http://127.0.0.1:8000/health
```

干净环境验收：

```powershell
cd subscription-tracker-clean
python -m ruff check .
python -m pytest -q
python -m compileall -q app
```

发布一致性验收：

```powershell
git rev-parse HEAD
git rev-list -n 1 v1.0.0
git tag --list "v1.0.0"
```

通过标准：

1. 所有命令退出码为 `0`。
2. GitHub Actions 对应 commit 或 tag 的 workflow 已通过。
3. 干净 clone 能完成依赖安装和全部检查。
4. CSV 脚本输出 `CSV export OK`，且退出码为 `0`。
5. 健康检查返回预期 JSON 或状态码，实际内容以你的 `/health` 实现为准。
6. `git rev-parse HEAD` 与 `git rev-list -n 1 v1.0.0` 指向同一 commit。
7. 发布说明中每个尖括号均已替换为真实证据或明确写 `none`。
8. 如果执行了部署，记录环境、健康检查和冒烟结果；如果没有执行，明确写 `not deployed`。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| 本地测试通过，CI 安装依赖失败 | 依赖只装在本地环境，没写入 `requirements.txt` | 在干净虚拟环境中复现，补齐依赖，重新运行 CI |
| 干净 clone 测试失败，本地却通过 | 测试依赖未提交的 `.env`、本地 SQLite 或缓存文件 | 删除未跟踪依赖，改测试使用临时数据库或 fixture，重新验证 |
| CSV 脚本返回 404 | 导出路径、方法或路由注册与规格不一致 | 检查 `app/routes.py` 和规格中的路径，统一为一个公开端点，不要保留多个别名 |
| CSV 中中文乱码或逗号破坏列 | 编码、BOM 或 CSV quoting 处理错误 | 使用 UTF-8，必要时写 `utf-8-sig` 供 Excel 读取；让 Python `csv` 模块处理引号，不要手工拼字符串 |
| 健康检查通过，但 UI 或导出失败 | `/health` 只检查进程，未覆盖数据库和业务流程 | 增加冒烟检查，至少验证创建、列表和导出一条测试记录 |
| Workflow 日志泄露 Secret | 将 secret 直接 echo、写入环境示例或放进代码 | 立即轮换密钥，从历史和工作流中删除，改用平台 Secrets 并检查日志权限 |
| 部署后服务无法访问 | 端口、反向代理、防火墙、路径权限或进程用户不匹配 | 查看服务状态和应用日志，先在本机 `127.0.0.1` 验证，再检查代理和防火墙 |
| 回滚后仍运行新版本 | symlink 未切换、服务未重启或缓存的旧进程仍存在 | 检查 `current` 指向、服务状态、进程启动时间和健康检查结果 |

## 10. 本章 Git 提交

建议分支：

```powershell
git switch -c ci/release-v1
```

建议拆分：

```powershell
git add .github/workflows/ci.yml
git commit -m "ci: add lint test and compile checks"

git add scripts/verify_csv_export.py
git commit -m "test: verify csv export contract independently"

git add .env.example
git commit -m "chore: document runtime configuration placeholders"

git add docs/runbooks/deploy-v1.md docs/runbooks/rollback-v1.md
git commit -m "docs: add v1 deployment and rollback runbooks"
```

只有 CI 通过且干净环境复现成功后，才创建 `v1.0.0` tag。不要把未验证的发布说明、临时数据库或验收 CSV 一起提交。

## 11. 练习与扩展

1. **制造一次 CI 红灯**：在临时分支让一个测试失败，观察 workflow 如何阻止合并，再恢复。
2. **漏依赖实验**：从 `requirements.txt` 删除一个测试依赖，验证干净 clone 能否发现问题。
3. **增强 CSV 验收**：增加空字符串、超长 note、重复订阅名和非法日期等测试场景。
4. **发布产物**：使用 `git archive` 或 Actions artifact 生成源代码包，并记录校验和。
5. **受控部署**：为 GitHub Actions 添加带 manual approval 的 deployment environment，但保持当前教程主流程不自动部署。
6. **供应链加固**：把 `actions/checkout` 和 `actions/setup-python` 固定到完整 commit SHA，并记录升级流程。

## 12. 参考资料

- [About continuous integration - GitHub Docs](https://docs.github.com/en/actions/get-started/continuous-integration)
- [Workflow syntax for GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [Using secrets in GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Managing releases in a repository - GitHub Docs](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
