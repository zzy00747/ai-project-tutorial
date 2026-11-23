# 附录 B　命令速查

> 用途：提供本教程最常用的最小命令集，而不是复制完整工具手册。统一核验日期：**2026-11-24**。CLI、斜杠命令和托管平台界面可能变化；实际执行前应以对应版本的官方文档和 `--help` 为准。

## B.1 Git：先看状态，再做小提交

```powershell
git status
git log --oneline --decorate -10
git diff --stat
git diff
git switch -c feat/example
git add PATH
git commit -m "feat: describe one change"
```

误操作排查与恢复：

```powershell
git diff --check
git show --stat HEAD
git restore --worktree -- PATH
git revert <COMMIT>
```

| 目的 | 命令 | 注意 |
|---|---|---|
| 查看未提交修改 | `git diff` | 默认不显示未跟踪文件内容 |
| 查看暂存区修改 | `git diff --staged` | 提交前重点审查 |
| 丢弃单文件工作区修改 | `git restore --worktree -- PATH` | 会覆盖未提交修改，先确认路径与 Diff |
| 用反向提交撤销已共享提交 | `git revert <COMMIT>` | 保留历史，通常比重写共享历史更适合协作 |
| 创建本地标签 | `git tag -a v1.0.0 -m "v1.0.0"` | 标签指向准确 commit；推送与发布按项目流程执行 |

官方来源：[Git Documentation](https://git-scm.com/docs)。

## B.2 Python 与项目运行

Windows PowerShell：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

macOS/Linux 创建与激活：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

需要避开 PATH 中其他工具时，显式使用虚拟环境解释器：

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

官方来源：[Python venv](https://docs.python.org/3/library/venv.html)、[pip](https://pip.pypa.io/en/stable/)、[Uvicorn](https://www.uvicorn.org/)。

## B.3 pytest：先确认收集，再看失败

```powershell
python -m pytest -q
python -m pytest --collect-only -q
python -m pytest tests/test_api.py -q
python -m pytest tests/test_api.py::test_create_subscription -q
python -m pytest -k "subscription" -q
python -m pytest --maxfail=1 -x
```

- `--collect-only`：只收集测试，排查“0 项运行”。
- `-k`：按表达式筛选名称匹配的测试。
- `-x`：首个失败后停止，适合集中处理根因；不把它当完整通过证据。
- 验收时重新运行完整测试集，不只运行刚修改的单测。

官方来源：[pytest Usage and Invocations](https://docs.pytest.org/en/stable/how-to/usage.html)。

## B.4 Ruff：让静态检查成为可执行反馈

```powershell
python -m ruff check .
python -m ruff check app tests
python -m ruff format --check .
python -m ruff check . --fix
```

`--fix` 会修改文件。先提交或保存基线，执行后查看：

```powershell
git diff --stat
git diff
python -m pytest -q
```

不要对 `.venv`、数据目录或整个磁盘运行自动修复。具体规则由项目配置决定，不在教程中假定所有默认规则始终相同。

官方来源：[Ruff](https://docs.astral.sh/ruff/)、[Ruff Configuration](https://docs.astral.sh/ruff/configuration/)。

## B.5 Spec Kit：把规格流程串起来

安装和初始化以当前 Quickstart 为准。官方 CLI 常见形式为：

```powershell
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify check
specify init <PROJECT_NAME>
```

在已集成的编码 Agent 中，核心阶段使用对应的 `speckit` 命令：

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.checklist
/speckit.tasks
/speckit.analyze
/speckit.implement
```

不是每个小修改都要机械执行全部命令。教程强调阶段产物：原则→规格→澄清→计划→任务→一致性检查→实现。安装参数、Agent 名称和可用命令可能变化，应先在当前环境运行 `specify --help`，不要混用旧教程中的无前缀斜杠命令。

官方来源：[github/spec-kit](https://github.com/github/spec-kit)、[Quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md)、[Agentic SDD 命令参考](https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md)。

## B.6 OpenSpec：围绕变更管理规格

```powershell
openspec init
openspec list
openspec show <CHANGE_ID>
openspec validate <CHANGE_ID> --strict
openspec archive <CHANGE_ID>
```

在编码 Agent 中，可用自然语言要求“创建 OpenSpec proposal”“应用指定 change”“归档已验收 change”。变更 ID 必须来自当前项目，不直接复制教程示例。不同版本的归档交互和校验参数可能不同，执行前查看：

```powershell
openspec --help
openspec archive --help
```

官方来源：[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)。

## B.7 Aider：仓库内小步修改与反馈

安装完成后，在项目根目录启动并显式加入相关文件：

```powershell
aider
aider README.md app/main.py tests/test_api.py
```

会话内常用命令：

```text
/diff
/test
/run <COMMAND>
/undo
/help
```

- `/diff`：查看 Aider 产生的修改。
- `/test`：运行项目配置的测试命令；先确认实际执行了什么。
- `/run`：运行命令并把输出用于后续协作。
- `/undo`：撤销 Aider 最近一次的 Git 提交，不等于恢复任意历史状态。

模型、认证和自动测试参数不在本附录写死。先备份或提交基线，再允许工具自动修改。

官方来源：[Aider Usage](https://aider.chat/docs/usage.html)、[Linting and Testing](https://aider.chat/docs/usage/lint-test.html)。

## B.8 OpenHands：用任务和验收条件驱动维护

OpenHands 的重点是任务工作流，而不是一条固定命令：

```text
输入：Issue、目标仓库、验收条件、允许范围
过程：研究与实现 → 开发 PR → 独立评审 → 测试 → 验收
输出：可审查的 PR、执行轨迹和验证结果
```

部署涉及仓库访问、令牌、运行环境和审批配置，应使用当前官方安装/部署文档；不要照搬旧版本的一体化 Docker 命令。旧 `All-Hands-AI/OpenHands` 已迁移到 `OpenHands/OpenHands`，代理核心还可能位于独立 SDK 仓库。

官方来源：[OpenHands](https://github.com/OpenHands/OpenHands)、[Software Factory](https://docs.openhands.dev/openhands/usage/use-cases/software-factory.md)。

## B.9 Renovate：依赖更新先形成可审查 PR

最小配置示例 `renovate.json`：

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "dependencyDashboard": true,
  "automerge": false,
  "schedule": ["before 9am on Monday"],
  "timezone": "Asia/Shanghai"
}
```

安装 Node.js 后，可用官方包中的校验器检查本地配置：

```powershell
npx --yes --package renovate renovate-config-validator
```

建议起步策略：

1. 开启 Dependency Dashboard，保留人工确认。
2. 小项目先关闭自动合并，观察更新质量。
3. CI 必须包含安装、测试和关键检查。
4. 失败时定位具体依赖和变更说明，不让 AI 同时升级整批包来“碰运气”。

官方来源：[Renovate Documentation](https://docs.renovatebot.com/)、[Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/)、[Configuration Validation](https://docs.renovatebot.com/config-validation/)。

## B.10 完成前最小检查序列

```powershell
git status
git diff --check
git diff --stat
python -m pytest -q
python -m ruff check .
```

通过标准：所有命令实际执行且成功；变更范围与任务一致；测试结果和 Diff 已写入 PR 或交接记录。如果项目包含前端、迁移或发布步骤，还应运行对应检查，不能用上述五条替代全部验收。
