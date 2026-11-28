# 综合实验五：模拟项目上线三个月

> 实验成果：在不推翻项目的前提下，随机处理六个真实维护事件，形成可审计的三个月维护记录，并发布一个经过验证的补丁版本。

本实验假设你已经完成 [第12章](../chapters/ch12-issue-driven-maintenance.md)、[第13章](../chapters/ch13-change-and-refactoring.md)、[第15章](../chapters/ch15-data-migration-recovery.md) 和 [第16章](../chapters/ch16-long-term-maintenance.md)。项目当前版本应为 v1.2，`subscriptions` 表已包含 `billing_cycle`。

## 1. 实验目标

证明项目不仅能生成，还能在上线后应对：

- 用户缺陷和功能变化。
- 依赖补丁、安全公告和升级失败。
- 数据库备份、恢复与代码回滚。
- 文档、生成清单和架构规则漂移。
- 运行日志、健康检查与故障定位。
- 新 AI 会话或新维护者接手。

最终交付物不是“AI 说维护完成”，而是命令、Diff、测试、PR、备份文件、健康检查和复盘记录。

## 2. 开始前的项目基线

在项目根目录执行：

```powershell
git status
python -m pytest -q
python -m ruff check .
python scripts/check_architecture.py
python scripts/export_routes.py
git diff --exit-code -- docs/generated/routes.md
python -m pip-audit -r requirements.txt
python -m pip list --outdated
```

把真实输出保存到：

```text
docs/maintenance/lab05/baseline.md
```

如果任何基线检查失败，先修复原问题并开始新的基线。不要把旧失败混入随机维护事件。

建议从干净状态创建实验记录目录：

```powershell
New-Item -ItemType Directory -Force docs/maintenance/lab05
```

## 3. 随机事件卡

事件池如下。每张卡都模拟一种上线后可能出现的维护压力。

| 编号 | 事件 | 必须留下的证据 |
|---|---|---|
| M01 | 用户报告 CSV 导出或列表页漏掉 `billing_cycle` | Issue、回归测试、修复 Diff、API 或导出结果 |
| M02 | Renovate 或 `pip list --outdated` 发现补丁升级，但 CI 失败 | 失败日志、根因、修复 PR 或暂缓记录 |
| M03 | `pip-audit` 报告一个依赖漏洞 | 漏洞编号或输出、影响分析、升级/缓解决定 |
| M04 | 需要验证迁移后备份仍可恢复 | 备份文件、恢复命令、恢复后查询结果 |
| M05 | README 或生成路由文档与实际 API 不一致 | 文档 Diff、导出脚本运行结果、CI 检查 |
| M06 | `app/repository.py` 或 `app/database.py` 出现禁止的上层依赖 | 架构检查失败输出、修复 Diff、重新通过记录 |
| M07 | 数据库不可用时 `/health` 未返回故障，或日志无法定位请求 | 健康检查测试、日志样本说明、修复 Diff |
| M08 | 两个模块出现重复 helper 或重复校验逻辑 | 重复位置、合并 Diff、测试结果 |
| M09 | 用户要求按币种筛选订阅 | Spec Delta、验收场景、功能测试、PR |
| M10 | 迁移或 API 的非法 `billing_cycle` 缺少测试 | 新增测试、失败前后证据 |
| M11 | 模拟一次补丁发布后发现启动失败，需要回滚 | 发布记录、回滚命令、回滚后健康检查 |
| M12 | 一个全新 AI 会话必须接手项目并完成一个小任务 | 交接文档、AI 任务说明、Diff 和验收记录 |

在 PowerShell 中随机抽取六张卡：

```powershell
$cards = @("M01","M02","M03","M04","M05","M06","M07","M08","M09","M10","M11","M12")
$draw = Get-Random -InputObject $cards -Count 6
$draw
```

如果团队需要复现同一组事件，可指定种子：

```powershell
$draw = Get-Random -InputObject $cards -Count 6 -SetSeed 20261124
$draw
```

把实际抽到的编号写入 `docs/maintenance/lab05/event-draw.md`，不要预填结果。

## 4. 三个月节奏

六张卡分成三个月，每月两张：

| 月份 | 重点 | 处理卡片 |
|---|---|---|
| 第 1 个月 | 稳定基线，处理缺陷和文档/架构漂移 | 抽到的第 1—2 张 |
| 第 2 个月 | 依赖、安全、观测和恢复能力 | 抽到的第 3—4 张 |
| 第 3 个月 | 小功能演化、发布和交接 | 抽到的第 5—6 张 |

如果随机结果使某个月负担过重，可以调整月份顺序，但必须在日志中说明原因。

每月按以下循环处理每张卡：

1. 把事件写成 Issue 或 Bug Report，使用 [Issue 模板](../blueprints/issue.md) 和 [Bug 报告模板](../blueprints/bug-report.md)。
2. 判断是否需要修改规格；功能变化必须先更新 Spec Delta。
3. 建立单独分支，例如 `fix/m01-csv-billing-cycle`。
4. 先写能暴露问题的测试或检查，再让 AI 修复。
5. 让 AI 输出计划、影响文件和 Diff，不直接接受“已完成”。
6. 运行相关测试、全量测试、Ruff 和架构检查。
7. 按 [PR 检查清单](../blueprints/pr-checklist.md) 人工审查。
8. 合并后更新 [运行维护手册](../blueprints/runbook.md) 或相关文档。
9. 在维护日志记录实际命令、证据、风险和耗时。

每月结束时，若已有合并且验证的维护 PR，可按第11章和第16章流程发布补丁版本。不要为了凑版本号发布未验收内容。

## 5. AI 协作规则

允许使用 AI，但必须遵守：

- 每张卡先让 AI 做只读分析，再授权修改。
- 每次任务都提供当前项目状态、范围、约束和验收标准。
- AI 的完成声明必须附命令、测试结果、Diff 或文件路径。
- 不让 AI 自评分数；评分由你根据客观证据完成。
- 不让 AI 直接修改 `main`、删除数据库或覆盖备份。
- 涉及恢复、发布和依赖安全时，人工保留最终批准。

一个标准任务示例：

```text
目标：处理事件卡 M05，修复生成路由文档与实际 API 不一致的问题。
上下文：项目为 Subscription Tracker v1.2；已有 scripts/export_routes.py、
docs/generated/routes.md 和 CI 文档一致性检查。
范围：只允许修改生成文档、导出脚本、相关测试和必要说明。
约束：先运行导出脚本并给出真实差异；不得手工编辑 docs/generated/routes.md；
不得改变现有 API 行为；不得删除 CI 检查。
验收：git diff --exit-code -- docs/generated/routes.md 通过；相关测试通过；
维护日志记录命令和证据。
输出：差异摘要、修改文件、执行命令、真实结果和剩余风险。
```

## 6. 维护日志

每张卡写一份记录，保存到 `docs/maintenance/lab05/`，例如 `month-1-M05.md`：

```markdown
# 事件卡 M05：文档与实际 API 不一致

- 日期：YYYY-MM-DD
- 触发方式：随机事件卡 / 用户报告 / CI 失败
- 基线命令与结果：
- 问题复现：
- 规格或文档变更：
- 分支与 PR：
- AI 任务与主要回答摘要：
- 人工审查结论：
- 执行命令：
- 真实证据：
- 风险与回滚方式：
- 实际耗时：
- 后续复查事项：
```

“真实证据”应粘贴命令的关键输出、测试名称、PR 链接、文件路径或恢复核验结果。不要粘贴密钥、个人订阅数据或内网地址。

## 7. 评分表

总分 100 分。评分时逐项写证据位置；没有证据的项不得分。

| 项目 | 分值 | 满分标准 |
|---|---:|---|
| 基线与事件抽取 | 5 | 保存真实基线输出，记录随机抽取结果和月份安排 |
| 六个事件完成度 | 30 | 每张卡 5 分：有 Issue、计划、实现、证据和复查事项 |
| 测试与 CI | 15 | 新增或修复行为均有测试；全量测试和 Ruff 通过；CI 或等价命令有真实结果 |
| 依赖与安全 | 10 | 至少处理一次过期依赖或安全公告，记录影响分析、升级/缓解决定和复查日期 |
| 备份与恢复 | 10 | 至少完成一次备份、恢复和核验；说明代码回滚、数据恢复和前向修复的边界 |
| 文档、架构与观测 | 10 | 文档/生成清单一致；架构检查通过；健康检查或日志能支持定位问题 |
| 交接与复盘 | 10 | 新 AI 会话能凭仓库和交接文档完成一个小任务；复盘写出三类问题和后续动作 |
| 过程纪律 | 10 | 小 PR、独立分支、人工审查、无未记录修改、无伪造证据 |

### 评分等级

| 总分 | 结论 |
|---|---|
| 90—100 | 可以独立承担个人项目长期维护 |
| 75—89 | 基本合格，需补齐证据不足的项目 |
| 60—74 | 重新完成薄弱事件卡，并补写维护日志 |
| 0—59 | 回到第12—16章，先完成每章验收再做实验 |

### 强制不合格条件

出现以下任一情况，本实验不通过：

- 伪造命令输出、测试结果或发布记录。
- 没有备份/恢复证据，却声称可以回滚。
- 所有修改直接提交到 `main`，没有审查记录。
- 六张卡少于四张完成。
- AI 的“完成”声明被当作唯一证据。

## 8. 最终复盘

完成六张卡后，写 `docs/maintenance/lab05/retrospective.md`，至少回答：

1. 哪类事件最容易演变成大 PR？为什么？
2. 哪些检查应该固化为脚本或 CI，而不是提醒 AI 注意？
3. 哪些文档必须人工维护，哪些应由脚本生成？
4. 当前项目适合哪一级 AI 自主度？哪些操作必须人工批准？
5. 下一个三个月应优先处理哪三类维护债？
6. 如果新维护者只读仓库，能否接手？缺什么？

复盘应引用具体事件卡、命令和文件路径，不写“整体还不错”这类无证据结论。

## 9. 最终提交物

```text
docs/maintenance/lab05/
├─ baseline.md
├─ event-draw.md
├─ month-1-*.md
├─ month-2-*.md
├─ month-3-*.md
├─ retrospective.md
└─ score.md
```

同时保留：

- 六个事件对应的分支或 PR 记录。
- 新增/修改的测试、脚本、文档和配置。
- 一次补丁版本发布或明确的“暂不发布”决定。
- 恢复演练产生的备份文件和核验记录。

## 10. 与其他章节的关系

- 缺陷和 Issue 流程见 [第12章](../chapters/ch12-issue-driven-maintenance.md)。
- 功能变化与重构见 [第13章](../chapters/ch13-change-and-refactoring.md)。
- 旧项目分析和基线建立见 [第14章](../chapters/ch14-legacy-modernization.md)。
- 数据库迁移、备份和恢复见 [第15章](../chapters/ch15-data-migration-recovery.md)。
- Renovate、安全审计、健康检查、文档漂移和自主度分级见 [第16章](../chapters/ch16-long-term-maintenance.md)。
- 完成定义参考 [完成定义模板](../blueprints/definition-of-done.md) 和 [会话交接模板](../blueprints/handoff.md)。

这个实验的目标不是让项目“看起来被维护过”，而是证明：三个月后，项目仍能通过客观检查被理解、修改、验证、发布和恢复。
