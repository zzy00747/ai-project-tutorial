# 会话交接文档（Handoff）

> 让一个新的 AI 会话（或同事）不读聊天记录就能继续干活。
> 原则：只写“当前事实”，不写过程叙事；信息以仓库为准，本文负责指路。

- 项目：subscription-tracker
- 目标版本：v1.2 → 准备 v1.2.1
- 更新人 / 日期：[名字] / 2026-XX-XX
- 预计交接时长：新会话读完本文 + 关键文件 ≤ 10 分钟

## 1. 项目是什么

个人订阅与续费管理器：本地运行，FastAPI + SQLite，管理订阅记录并提醒到期。
- 入口文档：`README.md`（运行）→ `AGENTS.md`（协作规则）→ `ARCHITECTURE.md`（结构）。
- 规格：`specs/`；决策：`docs/decisions/`；当前计划：`docs/plan.md`。

## 2. 当前状态

| 项 | 状态 |
|---|---|
| 分支 | `main`（HEAD: 4b7f9d1） |
| CI | 绿（最近一次 run #182） |
| 测试 | 38 passed |
| 版本 | v1.2 已发布；v1.2.1 进行中 |

## 3. 已完成（本迭代）

- billing_cycle 字段迁移（T1—T4）：迁移脚本 + 回归测试 + 备份演练，见 PR #31。
- CSV 导出特殊字符修复（ISSUE-014）：已合入并有回归测试。

## 4. 进行中 / 下一步

- [ ] T5（doing）：年付订阅的“按月折算展示”——方案已定（见 `docs/plan.md` 第 4 节），实现未开始。
- [ ] T6（todo）：Renovate 配置接入（参考 `ch16` 章节）。
- [ ] T7（todo）：更新 `docs/runbooks/operations.md` 的备份策略段落。

## 5. 已知问题与约束

- 年付记录的“下一次续费日”计算暂只支持整年，不支持自定义月数（记录在 spec 非目标）。
- 并发写 SQLite 未处理（ADR-0002 已接受该限制）。
- 不要直接修改 `docs/generated/` 下文件（机器生成，重跑脚本产出）。

## 6. 关键文件索引

| 要改什么 | 去哪 |
|---|---|
| API 行为 | `app/routes.py` + `specs/…/api.md` |
| 数据结构 | `app/database.py` + `app/schemas.py` + 迁移脚本 `scripts/migrations/` |
| 前端交互 | `app/static/app.js` |
| 协作规则 | `AGENTS.md` |
| 验收口径 | `docs/acceptance.md` + `templates/definition-of-done.md` |

## 7. 新会话第一步建议

1. 读本文 → 跑 `python -m pytest -q` 确认基线绿。
2. 领取第 4 节第一个未勾选项，先写验证方法再动代码。
3. 完成后更新本文的“已完成/进行中”。

## 完成条件

- 状态表与仓库实际一致（分支、CI、测试数）；下一步有明确验收方法；新会话按第 7 节可立即开工。
