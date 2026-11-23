# 附录 D　术语表

> 目标：用尽量少的概念解释 AI 项目从生成到维护的关键术语。遇到新工具时，先判断它属于哪一层，而不是机械记住产品名。

## D.1 AI 协作与上下文

| 术语 | 解释 |
|---|---|
| AI 编码代理 | 能读取项目、调用工具、修改文件、运行命令并根据结果继续工作的 AI 系统 |
| 聊天式 AI | 以对话为主，通常不直接管理仓库、运行测试或验证交付结果 |
| Prompt | 当前任务中给模型的指令、上下文和约束 |
| Context | 模型本次决策能看到的全部信息，包括指令、文件、工具结果和历史 |
| Context window | 一次推理可容纳的上下文范围；超出后旧信息会被截断、压缩或丢弃 |
| Context engineering | 决定“何时给模型哪些高价值信息”的工程实践 |
| Context rot | 上下文过长或噪声过多导致模型检索与推理质量下降 |
| Token | 模型处理文本的基本单位；中文、代码和标点并不一定是一个字对应一个 token |
| Tool | Agent 可调用的外部能力，例如读文件、搜索、运行命令或访问 API |
| MCP | Model Context Protocol，一种连接模型与外部工具和数据源的协议 |
| Skill | 可复用的任务说明、脚本和参考资料，用来封装重复流程 |
| Subagent | 在独立上下文中处理专项任务的子 Agent，主 Agent 只接收摘要或结果 |
| Hook | 在特定事件前后自动执行的脚本或检查，例如提交前、工具调用后 |
| Harness | 模型之外支撑其可靠工作的工程环境，包括上下文、工具、测试、权限和反馈回路 |
| Human-in-the-loop | 在计划、实现、审查、合并或发布中保留人工判断节点 |
| Autonomy level | Agent 可独立行动的程度，从只读建议到自动提交和发布逐级上升 |
| Worktree | 同一 Git 仓库的多个工作目录，用于隔离并行修改 |
| Sandbox | 限制命令、文件和网络权限的执行环境，用来降低误操作风险 |
| Just-in-time retrieval | 先保存文件路径、查询或链接，需要时再读取内容，而不是一次性塞入全部资料 |

## D.2 需求、规格与计划

| 术语 | 解释 |
|---|---|
| Intent | 用户的真实问题、目标和限制，比具体功能更早确定 |
| Mini-PRD | 简短产品需求说明，用于快速澄清目标、范围、非目标和验收 |
| Spec | 可审查、可验证的功能规格，包括行为、规则、数据和验收场景 |
| SDD | Spec-Driven Development，先形成规格和计划，再进入实现 |
| Spec Kit | GitHub 提供的规格驱动开发工具包，串联 constitution、specify、plan、tasks 等阶段 |
| OpenSpec | 围绕变更提案、规格更新和归档组织的轻量 SDD 工具 |
| Constitution | 项目长期遵守的原则、质量标准和工程约束 |
| Acceptance criteria | 判断一项需求是否完成的可观察条件 |
| Scenario | 用具体输入、操作和预期结果描述一个验收场景 |
| Non-goal | 当前版本明确不做的事情，用来防止范围膨胀 |
| NFR | 非功能需求，例如性能、安全、兼容性、可维护性和可用性 |
| MVP | 能解决核心问题的最小可用产品，不是功能残缺的 Demo |
| Vertical slice | 打通一个完整业务流程所需的最小纵向实现 |
| Walking skeleton | 先建立从入口到存储的最小可运行骨架，再逐步增强 |
| Definition of Done | 一项工作被视为完成前必须满足的全部证据和检查 |
| ADR | Architectural Decision Record，记录重要技术决策的原因、选项和后果 |
| Scope creep | 需求或实现在没有重新评审的情况下不断扩大 |
| Task packet | 交给 AI 的单个任务说明，包括目标、上下文、范围、约束、验收和输出 |

## D.3 版本、评审与发布

| 术语 | 解释 |
|---|---|
| Commit | 一次保存的项目状态，应聚焦一个可理解的变更 |
| Atomic commit | 只完成一个 logically complete change 的提交，便于审查、测试和回滚 |
| Diff | 两个版本之间的差异，是人工审查 AI 修改的核心证据 |
| Branch | 与主线隔离的开发线 |
| PR | Pull Request，用于提交、审查、测试和合并一组变更 |
| Code review | 对 Diff、测试、文档和风险的人工或工具审查 |
| CI | Continuous Integration，在提交或 PR 上自动运行构建、测试和检查 |
| CD | Continuous Delivery/Deployment，把通过验证的版本交付或部署到目标环境 |
| Quality gate | 必须通过才允许继续的检查，例如测试、Lint、安全扫描或架构规则 |
| Tag | 指向特定 commit 的标记，常用于发布版本 |
| Release | 一次正式交付的版本及其说明、产物和验证证据 |
| Rollback | 恢复到之前可用状态，可能涉及代码、配置、数据或部署 |
| Revert | Git 中通过反向提交撤销历史变更的方式，保留原历史 |
| Clean checkout | 不包含本地未提交状态的全新检出环境，用于复现交付结果 |

## D.4 测试与质量

| 术语 | 解释 |
|---|---|
| Unit test | 验证函数、类或小模块在受控输入下行为的测试 |
| Integration test | 验证多个模块、数据库或外部接口协同工作的测试 |
| End-to-end test | 从用户入口到最终结果验证完整业务流程的测试 |
| Regression test | 防止已修复问题再次出现的测试 |
| Characterization test | 为现有行为建立基线的测试，常用于重构前保护系统 |
| TDD | 先写失败测试，再实现功能，最后重构的开发方式 |
| Assertion | 测试中对实际结果与预期结果的明确比较 |
| Mock | 用替身隔离外部依赖；过度 mock 可能让测试通过但真实行为错误 |
| Test oracle | 判断结果是否正确的依据，例如规格、验收场景或历史行为 |
| Test gap | 重要行为、路径或边界缺少有效测试的状态 |
| Coverage | 测试覆盖代码或分支的程度；高覆盖率不等于高质量验收 |
| Lint | 通过规则检查代码风格、可疑写法和简单错误 |
| Static analysis | 不运行程序，通过代码结构发现潜在问题的分析方法 |
| Architecture test | 把依赖方向、模块边界等架构规则变成可执行检查 |
| Mutation testing | 故意修改代码，检验测试是否真的能发现错误 |
| Golden master | 用既有输出作为基准，比较后续实现是否保持行为一致 |

## D.5 维护、数据与运维

| 术语 | 解释 |
|---|---|
| Refactoring | 在不改变外部行为的前提下改善代码结构 |
| Technical debt | 为了短期速度积累、后续需要额外偿还的设计或实现问题 |
| Cognitive debt | 团队对系统理解不足，导致难以判断修改影响和承担后果 |
| Repo map | 项目目录、模块、入口、依赖和关键文件形成的导航图 |
| Documentation drift | 文档与实际代码、命令或架构逐渐不一致 |
| Generated docs | 由脚本从代码或配置生成的现状文档，应注明来源和再生成方式 |
| Dependency | 项目依赖的外部库、服务或工具 |
| Version pinning | 固定依赖版本，以提高构建可重复性 |
| Lockfile | 记录完整依赖解析结果的文件，用于复现安装环境 |
| Supply chain risk | 依赖来源、包名、构建或发布环节被篡改或引入风险的问题 |
| Renovate | 自动创建依赖更新 PR，并提供 Dashboard、分组和审批策略 |
| Schema migration | 数据库结构或数据的受控变更 |
| Forward fix | 不回滚数据，而是通过新的兼容修复继续向前恢复 |
| Backup | 可恢复的数据副本，必须经过验证才算可靠 |
| Restore drill | 定期演练恢复流程，确认备份、权限和步骤仍然有效 |
| Observability | 通过日志、指标、追踪和告警理解系统运行状态 |
| Health check | 判断服务是否启动并具备基本可用性的检查接口 |
| Structured log | 带字段、级别、时间和请求标识的日志，便于定位问题 |
| Alert | 达到阈值或异常模式时通知维护者的机制 |
| Runbook | 标准操作步骤，例如启动、发布、备份、恢复和常见故障处理 |
| Incident | 影响可用性、数据、安全或用户结果的事件 |
| Postmortem | 事件后的原因、影响、时间线和预防改进记录 |
| Residue cleanup | 定期清理 AI 或快速迭代留下的重复代码、无用配置和过期文档 |
| Small PR | 小范围、可审查、可回滚的变更，是长期维护自动化的基础 |

## D.6 教程中的项目术语

| 术语 | 解释 |
|---|---|
| Subscription Tracker | 本教程贯穿使用的个人订阅与续费管理器 |
| `intent.md` | 项目意图、用户、目标、非目标和验收信号 |
| `spec.md` | 当前功能或变更的可验证规格 |
| `plan.md` | 一次变更的实施计划、影响范围、风险和验证方式 |
| `tasks.md` | 计划拆分后的可执行任务及状态 |
| `handoff.md` | 会话、人员或 Agent 之间交接当前状态和下一步 |
| `/health` | 教程项目的健康检查端点 |
| `/api/subscriptions` | 教程项目的核心订阅数据 API |
| `billing_cycle` | 第 15 章数据迁移中新增的续费周期字段 |
