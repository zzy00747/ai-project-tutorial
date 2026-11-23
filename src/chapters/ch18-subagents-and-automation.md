# 第 18 章　子 Agent、Hooks 与 Issue-to-PR 自动化

> 本章成果：用隔离的子任务、独立工作区和明确闸门，把一次订阅管理器修复变成可审查的 Issue-to-PR 流程。

## 1. 本章成果

你将完成一次半自动维护演练：从一个明确 Issue 出发，让规划、实现、验证和评审分别在不同上下文或不同工作区中进行，最后形成可人工合并的 PR。本章还会建立一个自主度阶梯，判断哪些动作可以由 AI 自动执行，哪些必须保留人工闸门。

完成后的产物包括：

```text
docs/issues/renewal-date-validation.md
docs/handoff/renewal-date-validation.md
docs/verification/renewal-date-validation.md
```

以及一个独立 Worktree 中的修复分支和评审记录。

## 2. 为什么需要它

多个 Agent 并不天然等于更快。拆分的第一个价值是**上下文隔离**：研究、实现、评审分别只保留自己需要的信息，避免一段长对话里既有旧需求、又有失败尝试、还有未验证结论。第二个价值是**职责分离**：实现者容易相信自己已经完成，独立评审者只看证据和 Diff，更容易发现问题。

但拆分也有成本：交接信息可能丢失，多个工作区可能修改冲突，自动化可能反复循环而无人叫停。因此不要从多 Agent 开始第一个项目。先具备小任务、测试、CI 和人工评审，再逐步引入自动化。

## 3. 最少必备知识

- **主 Agent**：掌握总体计划，负责拆任务、交接和整合，不亲自完成所有深度工作。
- **子 Agent**：在干净上下文中完成一个可独立验收的任务，只返回结论、证据和产物。
- **上下文压缩**：长会话接近限制时，把关键事实写入文件，再开新会话。
- **Git Worktree**：同一仓库在不同目录中检出不同分支，便于隔离并行修改。
- **Hook**：在特定工具事件前后自动执行检查；它提供快速反馈，但不能替代独立 CI。
- **自主度闸门**：每个级别明确谁能写文件、谁能运行命令、谁能合并。

## 4. 起始项目状态

从第 17 章后的项目开始，工作区应干净，核心检查通过：

```powershell
git status
python -m pytest -q
python -m ruff check .
```

本章的练习 Issue 使用：`renewal_date` 早于当前日期时没有明确校验。修复应让 API 拒绝无效日期，并保留清晰的 422 或项目既有错误格式。

## 5. 操作步骤与 AI 任务示例

### 第一步：把 Issue 写成可验收任务

创建 `docs/issues/renewal-date-validation.md`：

```markdown
# renewal_date 缺少过去日期校验

现象：通过 API 可以创建 renewal_date 早于今天的订阅。
验收：
- 请求返回项目既有的校验错误格式。
- 合法日期仍可创建。
- 增加回归测试。
- 不改变数据库字段。
```

### 第二步：让规划子 Agent 只读分析

```text
目标：分析 renewal_date 校验的影响范围，不修改代码。
上下文：Issue、AGENTS.md、app/schemas.py、app/repository.py、相关测试。
范围：只读；禁止写文件和运行会改变状态的命令。
约束：找出最小修改点；区分现有测试缺口和实现缺陷。
验收：列出影响文件、建议方案、回归测试和风险。
输出：简短规划报告。
```

规划完成后，把结果写入 `docs/handoff/renewal-date-validation.md`。交接文件必须包含目标、已完成分析、允许修改范围、禁止事项和验证命令。

### 第三步：创建独立 Worktree

```powershell
git switch main
git pull
git worktree add ../subscription-tracker-renewal-fix -b fix/renewal-date-validation
cd ../subscription-tracker-renewal-fix
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux 将激活命令替换为：

```bash
source .venv/bin/activate
```

每个 Worktree 应拥有自己的虚拟环境，避免不同分支的依赖互相污染。查看和清理由主目录执行：

```powershell
git worktree list
git worktree remove ../subscription-tracker-renewal-fix
```

### 第四步：实现子 Agent 在隔离目录中修复

```text
目标：修复 renewal_date 缺少过去日期校验的问题。
上下文：docs/handoff/renewal-date-validation.md、AGENTS.md、相关模块与测试。
范围：只允许修改 app/schemas.py、app/repository.py、tests/test_api.py。
约束：不修改数据库 schema；不重构无关代码；保留既有错误响应格式。
验收：新增非法过去日期和合法日期两个测试；pytest 与 Ruff 通过。
输出：修改文件列表、关键 Diff、真实命令结果。
```

实现结束后不要在同一会话中宣布验收，改为独立验证。

### 第五步：用 Hook 和 CI 形成两层反馈

Hook 与 CI 的职责不同。Hook 在本地尽早反馈，CI 在独立环境做最终门禁。具体配置格式取决于所用工具，以下只是**示意结构**：

```json
{
  "event": "before_commit",
  "command": "python -m pytest -q && python -m ruff check ."
}
```

CI 仍应运行：

```yaml
- run: python -m pip install -r requirements.txt
- run: python -m pytest -q
- run: python -m ruff check .
```

如果本地 Hook 被绕过，CI 必须仍能拦住问题。

### 第六步：独立评审子 Agent 只读检查

```text
目标：评审 fix/renewal-date-validation，不修改代码。
上下文：Issue、交接文件、git diff --stat、git diff、测试与 CI 结果。
范围：只读。
约束：不信任实现会话的自述；只根据 Diff、命令输出和测试判断。
验收：逐条检查 Issue 验收条件，并指出未覆盖风险。
输出：通过、请求修改或阻断，以及证据。
```

### 第七步：人工合并并记录自主度

人工最终确认 Diff、测试结果和发布影响，再合并 PR。将“哪些步骤自动、哪些步骤人工”写入维护记录，为后续提高自动化程度留下依据。

## 6. AI 应生成的产物

- 可验收 Issue 与交接文件；
- 规划报告，说明影响范围和禁止事项；
- Worktree 中的最小修复 Diff；
- 新增回归测试；
- 验证报告，包含 pytest、Ruff 和 `git diff --check` 的真实输出；
- 独立评审结论；
- PR 描述，说明根因、修改、风险和验证证据。

如果使用的是 OpenHands 或 GitHub Copilot coding agent 等具备 Issue-to-PR 能力的平台，最终仓库中仍应看到同样的产物：Issue、分支、代码 Diff、测试、评审和合并记录。工具可以代替手工操作，但不能代替证据。

## 7. 人工检查点

- 检查 Worktree 是否只包含本章分支，没有混入其他实验文件。
- 查看 `git diff --stat`：是否只改了预期文件。
- 确认实现、验证和评审没有共用同一段长对话。
- 检查交接文件是否足够让新会话继续，而不是只有“请参考上文”。
- 确认 Hook 只加速本地反馈，CI 仍是独立门禁。
- 若自动化反复失败，检查是否设置了最大尝试次数、超时和升级人工的条件。
- 合并前确认数据库没有被偷偷修改，尤其是迁移类任务。

## 8. 验收命令与通过标准

在修复 Worktree 中运行：

```powershell
git status
git diff --stat
git diff --check
python -m pytest -q
python -m ruff check .
python skills\verify-change\scripts\check_report.py docs\verification\renewal-date-validation.md
```

通过标准：

- 工作区除预期修复外没有其他变更；
- 非法过去日期被拒绝，合法日期仍可创建；
- pytest 与 Ruff 真实退出码为 0；
- 验证报告结构检查通过；
- 独立评审没有遗留阻断问题；
- Worktree 清理成功，主仓库不受影响。

不要以“子 Agent 说完成”作为通过证据。

## 9. 常见失败及恢复方法

1. **症状：两个并行任务修改同一文件后无法合并。** 原因：任务没有按文件和目录隔离。恢复：中止合并，重新划分任务边界，每个 Worktree 只负责一个可独立验收的变更。
2. **症状：新会话不知道之前为什么这样修改。** 原因：上下文压缩后关键事实没有落盘。恢复：补写 `docs/handoff/`，记录目标、约束、已完成分析和验证命令。
3. **症状：自动化循环反复修改同一个测试。** 原因：没有停止条件和失败预算。恢复：限制尝试次数，保存轨迹，升级人工；先修验收标准，再继续自动化。
4. **症状：本地 Hook 通过但 CI 失败。** 原因：环境或依赖不一致。恢复：以 CI 为准；检查虚拟环境、依赖锁定和测试数据。
5. **症状：平台拥有过宽的仓库或云资源权限。** 原因：为了省事授予全部权限。恢复：先在测试仓库运行，使用最小权限和只读评审，再逐步放开。

## 10. 本章 Git 提交

建议分支：

```text
fix/renewal-date-validation
```

提交可拆为：

```powershell
git add docs/issues docs/handoff
git commit -m "docs: add renewal date validation issue"
git add app tests
git commit -m "fix: reject renewal dates in the past"
git add docs/verification
git commit -m "docs: record verification evidence"
```

PR 合并后删除远程分支，再清理 Worktree。

## 11. 练习与扩展

- 给规划、实现、评审分别设置最大尝试次数，并记录第一次需要人工介入的原因。
- 将“只读研究”“可写实现”“只读评审”写成三个不同的任务模板，避免一个 Agent 同时承担所有角色。
- 比较串行流程与两个真正独立任务的 Worktree 流程；如果并行没有减少总时间或提高质量，就不要为了并行而并行。
- 在测试仓库中体验 OpenHands 或 Copilot coding agent 的 Issue-to-PR 流程，再回到本项目比较证据完整性。

## 12. 参考资料

- [OpenHands：Software Factory](https://docs.openhands.dev/openhands/usage/use-cases/software-factory.md)：Issue、开发 PR、评审、测试与合并的闭环示例。
- [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)：从任务到 PR 的官方能力与适用边界。
- [Git worktree](https://git-scm.com/docs/git-worktree)：多工作区隔离。
- [Anthropic：Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)：上下文隔离、压缩和子任务交接。
