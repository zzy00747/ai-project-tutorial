# 第 10 章　上下文工程：让 AI 在新会话中也能接手项目

> 本章成果：为 Subscription Tracker 建立项目地图、AGENTS.md、交接记录和一条架构决策，使一个没有历史记忆的新 AI 会话能接手一个明确的小任务。

## 1. 本章成果

完成本章后，你的项目应该具备下面五项可交接资产：

1. `docs/project-map.md`：告诉 AI“当前代码在哪里、请求如何流动、测试放在哪里”。
2. `AGENTS.md`：告诉 AI 安装、运行、检查命令和项目边界。
3. `docs/handoff.md`：告诉下一个会话“当前做到哪里、下一步做什么、哪些证据已经存在”。
4. `docs/decisions/ADR-0002-agent-context-files.md`：记录为什么采用分层上下文文件，而不是不断堆长提示词。
5. 一次真实的新会话接手实验：新 AI 只读取指定文件，完成一个小任务，并由你独立验收。

本章的重点不是让 AI“记住更多”，而是让它**每次只拿到当前任务需要的高信号上下文**。

## 2. 为什么需要它

前面几章中，你和 AI 可能一直在同一个会话里工作。这个会话确实知道很多历史：你解释过需求、AI 修改过哪些文件、哪些命令失败过、哪些方案被否决。但会话历史有两个问题：

1. 它不可移植。换一个模型、工具、设备或同事，这些历史就消失了。
2. 它不是越多越好。长上下文会混入大量已经过时的工具输出、错误尝试和中间讨论，后续任务反而更容易抓错重点。

上下文工程要解决的是第二个问题：不是把所有资料塞给模型，而是决定**当前任务应该看到哪些资料、以什么顺序看到、哪些内容只放指针而不展开**。一个项目地图、一份短小的 AGENTS.md、一次明确交接，通常比复制整个仓库更有效。

`AGENTS.md` 的公开格式说明也强调，它是“README for agents”：面向代理的稳定入口，记录安装、测试、代码风格和项目约定，而不是把所有人类文档重复一遍。

## 3. 最少必备知识

开始本章前，理解下面几个概念即可：

- **上下文**：模型当前能看到的文件、命令输出、规格、历史和用户指令。
- **上下文腐化（context rot）**：上下文越长，模型越容易忽略或混淆其中真正重要的信息。
- **渐进披露**：入口文件只放稳定摘要和指针，细节资料按需读取。
- **项目地图**：用一页纸说明代码入口、数据流、职责边界和验证位置。
- **交接记录**：给下一个会话的任务包，而不是流水账。
- **ADR**：Architecture Decision Record，记录“为什么这样选”的短文档。

## 4. 起始项目状态

本章假设你已经完成第 9 章：项目有测试，CSV 导出功能可运行；如果 CSV 导出尚不存在，先完成第 9 章，不要在本章临时补功能。

建议从当前主分支创建文档分支：

```powershell
git switch -c docs/context-engineering
git status --short
```

开始前应确认下列命令在你的环境中可运行：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m ruff check .
python -m uvicorn app.main:app --reload
```

本章会新增或整理这些文件：

```text
AGENTS.md
docs/project-map.md
docs/handoff.md
docs/decisions/ADR-0002-agent-context-files.md
```

## 5. 操作步骤与 AI 任务示例

### 5.1 生成项目地图草案

先让 AI 根据当前仓库生成一份项目地图草案，但要求它只写当前真实存在的内容。

```text
目标：为 Subscription Tracker 生成 docs/project-map.md 草案。
上下文：只读取 README.md、ARCHITECTURE.md、docs/intent.md、docs/acceptance.md、specs/subscription-tracker/spec.md、app/main.py、app/routes.py、app/database.py、app/repository.py、app/schemas.py、tests/test_api.py、tests/test_repository.py。
范围：只创建或修改 docs/project-map.md。
约束：
1. 不得修改源代码、测试或规格。
2. 不得写入当前仓库中不存在的文件或功能。
3. 不超过 80 行。
4. 对不确定的内容写 TODO，不要猜测。
5. 使用文件路径说明职责，不复制大段代码。
验收：入口、请求路径、数据访问、测试、规格和文档指针均能与当前仓库对应。
输出：project-map.md 草案，以及需要人工确认的问题列表。
```

得到草案后，人工补充“为什么这样分层”，删除 AI 猜测的内容。下面是一个可以采用的完整示例：

```markdown
# Subscription Tracker Project Map

Last reviewed: <YYYY-MM-DD>

## 1. Entry points

- `app/main.py`: creates the FastAPI app, registers routes, mounts static files, and exposes `/health`.
- `python -m uvicorn app.main:app --reload`: local development command.

## 2. Request flow

`app/static/app.js`
→ `GET|POST|PUT|DELETE /api/subscriptions`
→ `app/routes.py`
→ `app/schemas.py`
→ `app/repository.py`
→ SQLite through `app/database.py`

## 3. Responsibilities

- `app/routes.py`: HTTP request handling, status codes, error responses.
- `app/schemas.py`: request/response field names, types, and validation rules.
- `app/repository.py`: subscription CRUD and CSV export data retrieval.
- `app/database.py`: SQLite connection and schema initialization.
- `app/static/`: browser UI; must not access the database directly.

## 4. Current data contract

Subscription fields: `id`, `name`, `amount`, `currency`, `renewal_date`, `note`, `created_at`.
`amount` is an integer in currency minor units, such as cents.
`renewal_date` uses `YYYY-MM-DD`.

## 5. Verification

- `python -m pytest -q`
- `python -m ruff check .`
- CSV export is exercised through `/api/subscriptions/export`.

## 6. Documents to read first

1. `docs/intent.md`
2. `docs/acceptance.md`
3. `specs/subscription-tracker/spec.md`
4. `ARCHITECTURE.md`
5. `docs/decisions/`
```

### 5.2 编写简洁的 AGENTS.md

`AGENTS.md` 是代理进入仓库时的稳定入口，但不应变成百科全书。它记录“每次都需要知道的内容”和“去哪里找详情”。下面是一个完整但简洁的示例：

```markdown
# AGENTS.md

## Project overview

Subscription Tracker is a local-first personal subscription and renewal manager. It uses Python 3.12+, FastAPI, SQLite, and plain HTML/CSS/JavaScript.

## Setup commands

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## Verification commands

Run these commands before reporting completion:

```powershell
python -m pytest -q
python -m ruff check .
```

Do not treat your own explanation as verification. Include the commands you actually ran and their result status.

## Core API contracts

- Health endpoint: `GET /health`
- Subscription collection: `/api/subscriptions`
- CSV export: `GET /api/subscriptions/export`
- Subscription fields: `id`, `name`, `amount`, `currency`, `renewal_date`, `note`, `created_at`
- `amount` must be an integer in currency minor units, not a floating-point currency value.
- `renewal_date` must use `YYYY-MM-DD`.

## Architecture boundaries

- `app/routes.py` adapts HTTP requests and responses.
- `app/schemas.py` validates API data contracts.
- `app/repository.py` owns database queries and result shaping.
- `app/database.py` owns SQLite connection and schema setup.
- `app/static/` contains browser assets and may only call the public API.
- `tests/` contains API and repository verification.

## Change rules

1. Complete one task at a time.
2. Read `docs/intent.md`, `docs/acceptance.md`, and the relevant specification before editing.
3. Do not modify unrelated files, dependencies, formatting, or documentation.
4. Do not add a dependency without an explicit task and an ADR.
5. Update tests when behavior changes.
6. Do not commit secrets, tokens, database files, or personal subscription data.
7. Preserve backward compatibility of existing API fields unless the task explicitly requests a migration.

## Document pointers

- `docs/project-map.md`: current code and data flow.
- `ARCHITECTURE.md`: module boundaries and constraints.
- `docs/handoff.md`: current state and next task.
- `docs/decisions/`: accepted and proposed architecture decisions.
- `docs/runbooks/`: operational procedures.
```

### 5.3 记录为什么这样设计上下文

新增 ADR，示例如下：

```markdown
# ADR-0002: Use layered project context instead of long prompts

- Status: Accepted
- Date: <YYYY-MM-DD>
- Decision owner: <your name>

## Context

Subscription Tracker is maintained through repeated AI sessions. Session history cannot be relied on as project memory, and copying large amounts of code into prompts increases noise and makes important constraints easier to miss.

## Options considered

1. Keep all instructions in one long prompt.
2. Keep documentation only in human-oriented README files.
3. Use a layered context system: short AGENTS.md, project map, specifications, ADRs, and handoff notes.

## Decision

Adopt option 3. AGENTS.md remains the stable entry point and command reference. Project-specific details stay in specs, docs, tests, and code. Each new task receives a handoff packet that lists only the files needed for that task.

## Consequences

- Benefits: context is portable across tools and sessions; important commands are discoverable; task-specific files can be loaded on demand.
- Costs: documents must be reviewed when architecture changes; stale pointers are possible.
- Mitigation: treat project-map.md and AGENTS.md as living files, and update them in the same PR that changes the related contract.

## Verification

A fresh AI session can complete a small documented task after reading only the pointer files and task-specific sources.
```

### 5.4 写交接记录，而不是流水账

交接记录应让下一个会话知道“从哪里继续”。下面是一个完整模板，所有尖括号都必须替换：

```markdown
# Handoff: CSV export test coverage review

- Updated: <YYYY-MM-DD HH:mm>
- Author: <your name or agent name>
- Base commit: <git-commit-sha>
- Branch: docs/context-engineering
- Environment: Windows PowerShell / Python 3.12 / Subscription Tracker

## Current verified state

- `python -m pytest -q`: <PASS|FAIL, command output summary>
- `python -m ruff check .`: <PASS|FAIL>
- CSV export route exercised by: <tests/test_api.py::test_name>
- Known limitations: <none or list>

## Next task

Check whether CSV export tests cover all of the following cases:

1. Chinese subscription name.
2. `note` containing a comma.
3. Empty `note`.
4. `amount` as an integer in minor units.

If a case is already covered, report the test file and test name. If a case is missing, add only the missing test to `tests/test_api.py`. Do not change implementation code in this task.

## Required context

Read these files first:

1. `AGENTS.md`
2. `docs/project-map.md`
3. `docs/acceptance.md`
4. `app/routes.py`
5. `tests/test_api.py`

## Constraints

- Modify at most `tests/test_api.py`.
- Do not refactor unrelated tests.
- Do not change the CSV endpoint or repository code.
- Run targeted tests, then full tests.

## Done definition

- Report each required case and whether it was already covered.
- Add missing tests without changing implementation.
- Provide commands run and result status.
- Leave the working tree with only expected test-file changes.
```

### 5.5 新会话接手实验

先确认工作树干净，再开始实验：

```powershell
git status --short
git diff --stat
```

打开一个**全新的 AI 会话**，不要粘贴之前的聊天记录。使用下面这个任务：

```text
请读取当前仓库中的 AGENTS.md、docs/project-map.md、docs/handoff.md、docs/acceptance.md、app/routes.py、tests/test_api.py。不要读取整个仓库。

任务：检查 GET /api/subscriptions/export 是否已经覆盖以下 CSV 场景：
1. 中文订阅名；
2. note 包含英文逗号；
3. note 为空；
4. amount 为整数分单位。

规则：
- 如果某个场景已有测试，只报告测试文件、测试函数和对应场景。
- 如果某个场景缺失，只修改 tests/test_api.py，补充缺失测试。
- 不修改实现代码、规格、AGENTS.md 或其他文档。
- 不重排无关代码。
- 运行 python -m pytest -q tests/test_api.py，再运行 python -m pytest -q。
- 最后报告修改文件、每个测试目的、命令结果和仍未解决的问题。
```

这个实验的关键不是 AI 能否写出测试，而是：**它是否没有依赖你的记忆，也能从仓库中的文档找到边界和验证方式。**

## 6. AI 应生成的产物

本章结束后，仓库中至少应出现或更新：

```text
AGENTS.md
docs/project-map.md
docs/handoff.md
docs/decisions/ADR-0002-agent-context-files.md
tests/test_api.py   # 仅在 CSV 测试确有缺口时由新会话修改
```

新会话还应返回一份文字报告，包含：

- 它实际读取了哪些文件；
- 四个 CSV 场景中哪些已有覆盖；
- 新增或修改的测试；
- 运行的命令；
- 是否遇到文档缺失、路径错误或命令失败。

## 7. 人工检查点

检查这些文件时，不要只看“有没有写”，而要检查它们是否真的能指导下一个会话：

- `AGENTS.md` 是否足够短？它应主要包含命令、边界和指针，而不是复制规格。
- 其中每一条命令是否都能在干净环境中运行？
- `docs/project-map.md` 是否只列出当前存在的文件？
- 是否存在 AI 猜测出来的模块、接口或“计划中的文件”？
- `docs/handoff.md` 是否还有未替换的 `<placeholder>`？
- 交接记录是否包含证据，而不是“已完成”“看起来没问题”这类空话？
- ADR 是否写了被否决的选项和代价，而不只是结论？
- 新会话是否询问了仓库里已经写明的问题？如果是，说明入口文档或指针不够清楚。
- 新会话是否修改了任务范围之外的文件？用 `git diff --stat` 检查。

## 8. 验收命令与通过标准

运行以下命令：

```powershell
git status --short
git diff --stat
git diff --check
python -m pytest -q
python -m ruff check .
```

通过标准：

1. 新增或修改文件只包含本章预期文档，以及确有必要的新增测试。
2. `git diff --check` 没有空白错误。
3. 测试命令没有失败项；具体数量以你的项目为准，不要照抄教程中的数字。
4. Ruff 没有未处理错误。
5. `AGENTS.md` 中的安装、运行、测试、检查命令均实际存在且可执行。
6. `docs/project-map.md` 中每个路径都能在仓库中找到。
7. `docs/handoff.md` 中没有残留尖括号占位符。
8. 新会话只读取指定文件即可完成或准确报告任务，不需要你重新解释项目背景。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| `AGENTS.md` 越来越长，AI 仍然漏掉关键约束 | 把规格、决策历史和全部代码说明塞进入口文件 | 将详情移回 `specs/`、`docs/decisions/` 和 `ARCHITECTURE.md`，`AGENTS.md` 只保留稳定命令、边界和指针 |
| 新会话反复询问项目结构或测试命令 | 项目地图缺少入口，或 AGENTS.md 没有给出验证命令 | 补充 `docs/project-map.md` 的请求流和验证命令，再重开一次会话验证 |
| 新会话修改了实现代码、规格或无关测试 | 交接任务范围不够明确 | 在 handoff 中写明“允许修改的文件”“禁止修改的文件”和“完成定义”，重新开始任务 |
| 文档声称已有功能，但代码中找不到 | AI 根据历史讨论猜测了项目状态 | 以当前代码和测试结果为准；删除不存在的内容，并把“不确定”明确写成 TODO |
| 长会话后半段 AI 开始重复错误建议 | 上下文混入大量过时工具输出和中间尝试 | 停止当前会话，写 handoff，开新会话，只带必要文件和任务约束 |
| 交接记录只有“完成了 CSV 功能” | 缺少证据，下一个会话无法判断当前状态 | 补充基线 commit、运行命令、结果状态、已知限制和下一步任务 |

## 10. 本章 Git 提交

建议分支：

```powershell
git switch -c docs/context-engineering
```

建议拆分：

```powershell
git add AGENTS.md docs/project-map.md
git commit -m "docs: add agent entry point and project map"

git add docs/decisions/ADR-0002-agent-context-files.md
git commit -m "docs: record layered agent context decision"

git add docs/handoff.md
git commit -m "docs: add fresh-session handoff packet"

git add tests/test_api.py
git commit -m "test: cover csv export edge cases"
```

最后一个提交只应出现在新会话确实补充了测试时。不要把文档整理、测试补充和实现变更混在同一个提交中。

## 11. 练习与扩展

1. **上下文预算实验**：分别让 AI“读取整个仓库”和“只读取项目地图指定的文件”完成同一个任务，比较修改范围、提问次数和最终结果。
2. **交接质量实验**：故意写一份缺少命令和证据的 handoff，观察新会话是否会猜测；再补全后重做。
3. **文档漂移检查**：写一个脚本，检查 `docs/project-map.md` 中列出的路径是否都存在。
4. **嵌套上下文**：如果以后加入独立前端目录，可尝试在该目录放置更具体的 `AGENTS.md`，并观察代理是否优先使用离被修改文件最近的说明。
5. **稳定规则检查化**：把“routes 不得直接写 SQL”“static 不得访问数据库”这类边界规则转化为测试或静态检查，而不是只依赖文档提醒。

## 12. 参考资料

- [Effective context engineering for AI agents - Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
- [AGENTS.md](https://agents.md/)
- [Architecture Decision Records - GitHub](https://github.com/joelparkerhenderson/architecture-decision-record)
- [Git diff documentation](https://git-scm.com/docs/git-diff)
