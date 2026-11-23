# 功能规格（Spec）

> 把意图变成机器和人都能执行的契约：行为、规则、验收场景。
> 来源：`intent.md`。变更时新增版本行并注明原因。

- 功能名称：订阅管理核心
- 关联意图：`intent.md` v0.1
- 规格版本：v0.1（2026-XX-XX）

## 1. 用户故事

- US-1：作为用户，我想添加一条订阅，以便统一管理续费日期。
- US-2：作为用户，我想查看订阅列表和即将到期项，以便提前安排续费。
- US-3：作为用户，我想修改或删除订阅，以便数据与实际一致。

## 2. 验收场景（Given / When / Then）

### 场景 A：添加合法订阅

```gherkin
Given 订阅列表为空
When 我提交 {"name":"网盘会员","amount":1500,"currency":"CNY","renewal_date":"2026-12-01","note":""}
Then 返回 201，列表出现该记录，amount 显示为 15.00 元
```

### 场景 B：拒绝非法金额

```gherkin
Given 表单已打开
When 我提交 {"name":"网盘会员","amount":-5,"currency":"CNY","renewal_date":"2026-12-01"}
Then 返回 422，提示“金额必须为正整数（单位：分）”，列表无新增
```

### 场景 C：拒绝非法日期

```gherkin
Given 表单已打开
When 我提交 {"renewal_date":"2026-02-30"}
Then 返回 422，提示“日期格式无效”
```

### 场景 D：删除后不可再查

```gherkin
Given 已存在记录 id=1
When 我发送 DELETE /api/subscriptions/1
Then 返回 204；GET /api/subscriptions/1 返回 404
```

### 场景 E：到期提醒

```gherkin
Given 存在 renewal_date 在 7 天内的记录
When 我打开首页
Then 提醒区列出该记录，按 renewal_date 升序
```

## 3. 业务规则

- R1 金额以“分”为单位存储为正整数；展示时除以 100 保留两位。
- R2 `renewal_date` 使用 `YYYY-MM-DD`；早于当天 1 年以上的记录提交时警告确认。
- R3 删除为物理删除；不提供回收站（记录在非目标）。
- R4 到期提醒窗口默认 7 天，参数 `REMIND_DAYS` 可配置。

## 4. 边界条件

| 边界 | 期望行为 |
|---|---|
| name 超 100 字 | 422，提示长度上限 |
| 并发添加两条同名订阅 | 允许，id 不同 |
| 空列表 | 返回 200 + 空数组，页面显示“暂无订阅” |
| 系统日期晚于 renewal_date | 标记为“已过期”分组 |

## 5. 数据与 API 契约

- 表 `subscriptions`：`id INTEGER PK`、`name TEXT NOT NULL(≤100)`、`amount INTEGER NOT NULL CHECK(amount>0)`、`currency TEXT NOT NULL DEFAULT 'CNY'`、`renewal_date DATE NOT NULL`、`note TEXT DEFAULT ''`、`created_at TEXT NOT NULL DEFAULT (datetime('now'))`。
- `GET /api/subscriptions` → 200 列表，`?due_within=7` 过滤到期项。
- `POST /api/subscriptions` → 201 或 422（校验错误体含字段级 message）。
- `PUT /api/subscriptions/{id}` → 200 / 404 / 422。
- `DELETE /api/subscriptions/{id}` → 204 / 404。
- `GET /health` → 200 `{"status":"ok"}`。

## 6. 非功能要求

- 本地启动后接口 P95 < 200ms（10 条数据）。
- 任何 5xx 必须有对应日志行。
- UI 在 1280×720 与 375 宽度下可操作。

## 变更记录

| 版本 | 变更 | 原因 |
|---|---|---|
| v0.1 | 初版 | 对齐 intent v0.1 |

## 完成条件

- 每个用户故事至少 1 个验收场景；规则与场景一致；API 契约字段与数据表一致；AI 复述规格与原文无冲突。
