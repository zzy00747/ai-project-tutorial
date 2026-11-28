# 任务列表（Tasks）

> 把计划拆成可独立验证的小任务。一个任务 = 一个提交；全部完成 = 计划完成。
> 状态：`todo` / `doing` / `done` / `blocked`。

- 关联计划：`plan.md` v0.1
- 更新时间：2026-XX-XX

## 使用规则

1. 每个任务必须写“如何验证”，没有验证方法的任务先拆细再排期。
2. 一次只做一个 `doing`；`blocked` 必须写明阻塞原因和求助对象。
3. 完成任务时把验证证据（命令输出/截图/测试名）链接到提交信息或 PR。

## 任务

| ID | 任务 | 依赖 | 状态 | 验证方法 | 完成条件 |
|---|---|---|---|---|---|
| T1 | 初始化项目骨架与 requirements | - | todo | `python -m uvicorn app.main:app` 返回 404 但进程不崩 | 目录结构与 GUIDE 一致 |
| T2 | database.py：连接与建表 | T1 | todo | pytest 建表冒烟测试通过 | 表结构与 spec 第5节一致 |
| T3 | schemas.py：Pydantic 模型与校验 | T1 | todo | 非法金额/日期单测通过 | 覆盖 R1/R2/边界表 |
| T4 | repository.py：CRUD 实现 | T2,T3 | todo | repository 单测通过 | 方法与 spec API 一一对应 |
| T5 | routes.py：5 个 API 端点 | T4 | todo | TestClient 场景 A—D 通过 | 状态码符合契约 |
| T6 | /health 端点 | T1 | todo | `curl /health` 返回 ok | 200 + JSON |
| T7 | 前端列表 + 添加表单 | T5 | todo | 手工操作场景 A | 数据入库且页面可见 |
| T8 | 修改/删除交互 | T7 | todo | 手工场景 D | 操作后列表刷新 |
| T9 | 到期提醒区 | T7 | todo | 手工场景 E | 7 天内记录按期升序 |
| T10 | CSV 导出 | T5 | todo | 导出文件 Excel 可开 | 字段完整、乱码处理正确 |
| T11 | ruff + pytest 接入 CI | T3 | todo | GitHub Actions 绿 | 工作流跑 lint+test |
| T12 | README 启动说明 | T11 | todo | 新目录按 README 可跑通 | 无遗漏命令 |

## 阻塞与风险登记

| 任务 | 阻塞/风险 | 处理 |
|---|---|---|
| T7 | AI 生成的 JS 与后端字段名不一致 | 提交前人工对照 spec 第5节 |

## 完成条件

- 所有任务为 `done` 且有证据；无 `blocked` 遗留；任务实际拆分与 plan 影响范围一致。
