# AI 项目实战：从零生成、验收到持续维护

> 用一个真实项目，掌握需求、规格、编码、测试、部署、演化与 AI 工程化协作。

这不是一本“提示词大全”，也不是某个 AI 产品的操作手册。你要完成的是一个可导出、可测试、可发布、可回滚、可继续接手的软件项目。

## 你将学会什么

- 把模糊想法整理成意图、规格、验收场景和任务。
- 让 AI 小步完成实现，并通过 Diff、测试和 CI 检查结果。
- 用 Git 保留变更历史，在出错时恢复。
- 把项目规则、架构决策和故障经验沉淀为仓库资产。
- 修复 Bug、增加功能、接手旧项目，而不是推翻重写。
- 处理数据库迁移、备份恢复、依赖升级和文档漂移。
- 创建可复用 Skill，并逐步引入子 Agent 与 Issue-to-PR 自动化。

## 贯穿项目

教程使用“个人订阅与续费管理器”，默认技术栈为 Python、FastAPI、SQLite、原生 Web 前端、pytest、Ruff 和 GitHub Actions。

| 版本 | 你将完成的事情 |
|---|---|
| v0.0 | 生成一次性原型，观察需求模糊带来的失控 |
| v0.1 | 打通添加、查看订阅的完整流程 |
| v0.2 | 完成修改、删除、输入校验和小 PR |
| v1.0 | 补齐测试、CSV 导出、CI、部署与发布 |
| v1.1 | 修复 Bug、增加搜索筛选、局部重构、接手旧项目 |
| v1.2 | 完成数据库迁移、备份恢复与长期维护演练 |

## 推荐阅读路线

### 完整路线

按章节顺序阅读，并完成每章验收与五个实验。适合第一次独立完成软件项目的读者。

### 快速生成路线

第 1—9 章 → 第 11 章 → 实验三。适合想先做出并发布第一个版本的读者；之后仍需补读维护部分。

### 已有项目维护路线

第 2—3 章 → 第 9—10 章 → 第 12—16 章 → 实验四、五。适合已有代码仓库的读者。

### 工程自动化路线

先完成核心 16 章，再读第 17—19 章。不要从多 Agent 和自动化开始第一次项目实践。

## 第一部分：建立正确的 AI 开发方式

1. [AI 能生成代码，为什么项目仍然会失败](chapters/ch01-why-projects-fail.md)
2. [零基础必备：看懂项目、运行项目和阅读报错](chapters/ch02-project-basics.md)
3. [Git：AI 开发的安全带与时间机器](chapters/ch03-git-safety.md)

- [综合实验一：一次性原型与失控复盘](labs/lab01-disposable-prototype.md)

## 第二部分：从模糊想法到可实施规格

4. [从想法到意图：先决定不做什么](chapters/ch04-intent-and-acceptance.md)
5. [规格驱动开发：把需求写成可验证契约](chapters/ch05-spec-driven-development.md)
6. [最小架构、技术决策与任务拆分](chapters/ch06-architecture-and-planning.md)

- [综合实验二：不写代码，完成项目蓝图](labs/lab02-project-blueprint.md)

## 第三部分：AI 生成、验证与首次交付

7. [纵向打通：生成第一个真正可用的版本](chapters/ch07-vertical-slice.md)
8. [AI 实现闭环：小任务、小 Diff、小 PR](chapters/ch08-small-steps-and-prs.md)
9. [测试与调试：让“AI 说完成”变成可验证事实](chapters/ch09-testing-and-debugging.md)
10. [上下文工程：让 AI 在新会话中也能接手项目](chapters/ch10-context-engineering.md)
11. [CI、发布与部署：从本地能跑到别人能用](chapters/ch11-ci-release-deploy.md)

- [综合实验三：交付第一个正式版本](labs/lab03-release-v1.md)

## 第四部分：从会生成到能长期维护

12. [Issue 驱动维护：从问题报告到修复 PR](chapters/ch12-issue-driven-maintenance.md)
13. [需求演化与重构：修改系统，而不是重新生成系统](chapters/ch13-change-and-refactoring.md)
14. [接手旧项目：从陌生仓库到受控现代化](chapters/ch14-legacy-modernization.md)
15. [数据库迁移、备份与真正的故障恢复](chapters/ch15-data-migration-recovery.md)
16. [长期维护系统：依赖、安全、运行观测与文档漂移](chapters/ch16-long-term-maintenance.md)

- [综合实验四：完成一次完整的需求演化](labs/lab04-evolution-v1-1.md)
- [综合实验五：模拟项目上线三个月](labs/lab05-three-month-maintenance.md)

## 第五部分：把经验沉淀为可复用的 AI 工程能力

17. [Skill 工程：把有效协作流程变成项目资产](chapters/ch17-skill-engineering.md)
18. [子 Agent、Hooks 与 Issue-to-PR 自动化](chapters/ch18-subagents-and-automation.md)
19. [平台对照与工具迁移：不被某个产品绑定](chapters/ch19-platforms-and-tool-migration.md)
20. [结业项目：完成你自己的 AI 生成与维护闭环](chapters/ch20-capstone.md)

## 附录

- [附录 A：开发环境与故障速查](appendices/A-environment.md)
- [附录 B：工具命令对照](appendices/B-command-reference.md)
- [附录 C：失败案例库](appendices/C-failure-catalog.md)
- [附录 D：术语表](appendices/D-glossary.md)
- [附录 E：参考资料与来源索引](appendices/E-sources.md)

## 可复制模板

| 模板 | 用途 |
|---|---|
| [项目意图](blueprints/intent.md) | 明确用户、问题、范围、约束与成功标准 |
| [功能规格](blueprints/spec.md) | 记录行为、规则和验收场景 |
| [实施计划](blueprints/plan.md) | 记录技术方案、影响范围和验证策略 |
| [任务列表](blueprints/tasks.md) | 把计划拆成可独立验证的小任务 |
| [架构决策记录](blueprints/adr.md) | 保存技术选择的原因和后果 |
| [Issue](blueprints/issue.md) | 描述一个可交付的问题或需求 |
| [Bug 报告](blueprints/bug-report.md) | 保存复现、证据、影响与回归要求 |
| [PR 检查清单](blueprints/pr-checklist.md) | 审查 Diff、测试、兼容性和交付证据 |
| [发布检查清单](blueprints/release-checklist.md) | 检查构建、部署、回滚和发布记录 |
| [运行维护手册](blueprints/runbook.md) | 记录启动、观测、备份和故障处理 |
| [会话交接](blueprints/handoff.md) | 让新 AI 会话从项目事实继续工作 |
| [完成定义](blueprints/definition-of-done.md) | 统一“完成”所需的客观证据 |

## 每章如何使用

1. 先读“本章成果”和“起始项目状态”。
2. 按操作步骤完成任务，不要只复制 AI 的输出。
3. 在人工检查点阅读 Diff、文件和关键行为。
4. 执行验收命令，保存真实输出或截图。
5. 遇到失败时先按“症状—原因—恢复”处理。
6. 验收通过后，再按建议拆分 Git 提交。

## 教程的验收原则

- AI 说“完成”不是证据。
- 页面能打开不等于核心流程正确。
- 测试全绿还要检查测试是否真的断言了业务行为。
- 代码回滚不等于数据已经恢复。
- 平台快照不替代正式 Git 历史。
- 项目只有在干净环境可复现、后续变化可局部实现时，才算真正可交付、可维护。

## 写作与维护

章节结构、项目字段、命令和作者分工约定见 [写作与集成契约](writing-guide.md)。工具功能具有时效性，具体产品能力以官方最新文档为准；稳定的方法和验收原则不随工具界面变化而变化。
