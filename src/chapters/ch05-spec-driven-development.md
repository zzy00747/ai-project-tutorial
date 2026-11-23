# 第 5 章　规格驱动开发：把需求写成可验证契约

> 本章成果：把第 4 章的意图和验收标准，转化为可追踪、可测试、可供 AI 实现的行为规格与 API 契约。

## 1. 本章成果

完成本章后，项目中应新增以下文件：

```text
specs/subscription-manager/spec.md
specs/subscription-manager/api.md
specs/subscription-manager/scenarios.md
docs/spec-traceability.md
```

这些文件共同构成第一版规格：

- `spec.md`：定义系统必须满足的行为、数据规则、状态码和阶段范围。
- `api.md`：定义核心 HTTP 接口、请求示例、响应示例和错误契约。
- `scenarios.md`：把关键行为写成可转成测试的 Given/When/Then 场景。
- `spec-traceability.md`：记录 Intent、Acceptance、Spec 和后续任务之间的对应关系。

本章仍然不生成应用代码。规格完成并通过审查后，第 6 章才开始设计架构和任务。

## 2. 为什么需要它

Intent 说明“为什么做”，Spec 说明“系统应表现出什么行为”。没有 Spec 时，AI 每一轮都可能重新猜测边界条件：空名称是否允许？金额是元还是分？删除不存在的记录返回什么？列表按什么排序？这些猜测会分散到代码、测试和文档中，后期很难统一。

规格驱动开发（Spec-Driven Development，SDD）的价值，是在实现前形成一份人和 AI 都能审查的契约。它不是为了增加仪式感，而是解决三个问题：

1. **可验收**：每条需求都能变成测试或明确的手工检查。
2. **可追踪**：代码和任务可以回链到具体需求。
3. **可演化**：后续改需求时，先改 Spec，再改代码，而不是直接在聊天记录里临时决定。

### Spec Kit 与 OpenSpec 的主辅关系

本教程把**仓库内的 Markdown 规格文件作为唯一事实源**。工具可以辅助生成和组织这些文件，但不能替代人工审查。

[github/spec-kit](https://github.com/github/spec-kit) 适合作为主参考流程。它把开发拆成若干阶段，例如建立项目原则、编写规格、澄清歧义、制定计划、拆分任务、分析一致性并实现。初学者可以借用它的阶段意识，但不必一开始就执行全部命令。

[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) 更轻量，适合作为辅助对照，尤其适合后续“提出变更、审查差异、归档决定”的演化场景。它强调用变更提案管理规格，而不是把所有讨论都堆在一份大文档里。

教程中的使用原则是：

| 工具 | 在教程中的角色 | 使用方式 |
|---|---|---|
| 手写 Markdown 规格 | 主线 | `specs/subscription-manager/` 下的文件是最终事实源 |
| Spec Kit | 主流程参考 | 借用阶段划分和澄清思路；工具输出必须经过人工审查后纳入仓库规格 |
| OpenSpec | 轻量变更辅助 | 后续需求变更时作为对照方法，不与 Spec Kit 同时管理同一份规格状态 |

不要在一个项目里同时初始化两套流程并各自生成规格文件。否则会出现两份“看起来都对”的规格，AI 和新读者都不知道该相信哪一份。具体安装命令会随版本变化，本教程不在正文堆砌命令；需要时以官方 README 和当前版本为准。

## 3. 最少必备知识

- **需求 ID**：例如 `SUB-001`，用于让测试、任务和代码引用同一条行为。
- **MUST / SHOULD / MAY**：分别表示必须满足、建议满足和可选行为。第一版应谨慎使用 SHOULD 和 MAY。
- **正常路径与异常路径**：成功创建是一条路径；无效输入、记录不存在、数据库不可写是另一些路径。
- **API 契约**：路径、方法、请求字段、响应字段、状态码和错误格式。
- **验收场景**：用 Given/When/Then 描述前置条件、操作和可观察结果。
- **规格追踪**：Intent → Acceptance → Spec → Task → Test 的对应关系。
- **Spec Delta**：后续只描述规格变化的部分，而不是每次重写整份文档。

## 4. 起始项目状态

确认第 4 章文档已经提交：

```powershell
git status
git switch -c docs/specification
```

当前项目应至少有：

```text
docs/intent.md
docs/acceptance.md
README.md
AGENTS.md
```

如果还没有 `specs/` 目录，本章会创建它。不要在本章创建 `app/`、`tests/` 或数据库文件。

## 5. 操作步骤与 AI 任务示例

### 5.1 从验收标准反推规格

规格不是重新写一遍愿望，而是把每条 Acceptance 转成系统行为。使用以下 AI 任务：

```text
目标：基于现有 Intent 和 Acceptance，为 Subscription Tracker 编写第一版行为规格与 API 契约。

上下文：
- 请阅读 `docs/intent.md`、`docs/acceptance.md`。
- 项目是本地单用户应用，使用 Python 3.12+、FastAPI、SQLite 和原生前端。
- 初始字段为 id、name、amount、currency、renewal_date、note、created_at。
- 金额使用“分”为单位的正整数。
- 核心 API 是 `/api/subscriptions`，健康检查是 `/health`。
- v0.1 只做添加、查看和持久化；v0.2 做修改、删除和完整校验；v1.0 做 CSV 导出、测试、CI 和发布。

范围：
- 只生成规格、API 契约、验收场景和追踪表。
- 不生成 Python 代码、前端代码、测试代码或 CI 配置。
- 不设计登录、提醒、邮箱抓取、汇率换算或多用户功能。

约束：
- 每条行为需求必须有唯一 ID。
- 每条需求必须标明所属版本阶段。
- 每个字段必须写清类型、是否必填、默认值和边界。
- 每个 API 必须写清方法、路径、成功状态码、失败状态码和示例。
- 不要复制 Intent 原文来充数；Spec 必须描述可测试行为。

验收：
- AC-01 到 AC-08 都能追踪到至少一条 Spec 需求。
- 正常、无效输入、记录不存在和持久化场景均有明确预期。
- API 示例中的字段名、类型和阶段范围保持一致。

输出：
1. `specs/subscription-manager/spec.md`
2. `specs/subscription-manager/api.md`
3. `specs/subscription-manager/scenarios.md`
4. `docs/spec-traceability.md`
5. 规格中仍存在、需要我决定的开放问题清单
```

### 5.2 编写 `specs/subscription-manager/spec.md`

以下示例可直接作为起点。它刻意不规定函数名、类名和目录结构，只规定外部可验证行为。

````markdown
# Subscription Tracker Specification

## 1. 范围

本规格覆盖本地单用户订阅管理器的 v0.1、v0.2 和 v1.0 行为。登录、权限、自动提醒、邮箱抓取、汇率换算、支付集成和多设备同步不在范围内。

## 2. 数据规则

| 字段 | 类型 | 必填 | 规则 |
|---|---|---|---|
| `id` | integer | 服务端生成 | 数据库主键，创建后不可由客户端指定或修改 |
| `name` | string | 是 | 去除首尾空白后长度为 1—80 |
| `amount` | integer | 是 | 以“分”为单位，必须大于 0；`1200` 表示 12.00 |
| `currency` | string | 是 | 只能是 `CNY` 或 `USD` |
| `renewal_date` | string | 是 | ISO 8601 日期，格式 `YYYY-MM-DD`，必须是有效日期 |
| `note` | string | 否 | 最长 500 字符；缺省为空字符串 |
| `created_at` | string | 服务端生成 | UTC ISO 8601 时间戳，创建后不可修改 |

## 3. 行为需求

### SUB-001　创建订阅（v0.1）

系统 MUST 允许用户提交一条有效订阅记录。创建成功后，系统 MUST 返回包含服务端生成 `id` 和 `created_at` 的完整记录。

### SUB-002　查看订阅列表（v0.1）

系统 MUST 返回所有订阅记录。列表 MUST 按 `renewal_date` 升序排序；日期相同时按 `id` 升序排序。

### SUB-003　持久化（v0.1）

成功创建的订阅 MUST 保存在 SQLite 数据库中。应用停止并重新启动后，数据 MUST 仍然存在且字段值不变。

### SUB-004　输入校验（v0.2）

系统 MUST 拒绝无效输入，包括：空名称、超长名称、非正整数金额、不支持的货币、无效日期、超长备注。校验失败时 MUST NOT 写入数据库。

### SUB-005　更新订阅（v0.2）

系统 MUST 允许根据 `id` 更新 `name`、`amount`、`currency`、`renewal_date` 和 `note`。更新成功后，后续查询 MUST 返回新值。`id` 和 `created_at` MUST NOT 被客户端修改。

### SUB-006　删除订阅（v0.2）

系统 MUST 允许根据 `id` 删除订阅。删除成功后，该记录 MUST NOT 出现在列表或 CSV 导出中。删除不存在的记录 MUST 返回 404。

### SUB-007　CSV 导出（v1.0）

系统 MUST 提供 UTF-8 CSV 导出。导出内容 MUST 包含当前所有订阅，字段顺序固定为：

```text
id,name,amount,currency,renewal_date,note,created_at
```

CSV 中的 `amount` 仍为分单位整数。包含逗号、引号或换行的字段 MUST 按 CSV 规则正确转义。

### OPS-001　健康检查（v0.1）

系统 MUST 提供 `GET /health`。服务可正常处理请求时，MUST 返回 HTTP 200 和 JSON 对象 `{"status": "ok"}`。

## 4. 非功能需求

- NFR-001：项目 MUST 能从干净 Git 工作副本安装依赖并启动。
- NFR-002：核心行为 MUST 能由自动化测试覆盖。
- NFR-003：应用 MUST NOT 依赖外部付费服务、邮箱账号或支付平台。
- NFR-004：错误信息 SHOULD 指出字段和原因，但 MUST NOT 泄露数据库文件路径、密钥或完整堆栈给普通页面用户。
- NFR-005：文档与规格 MUST 与已发布版本保持可追踪关系。

## 5. 开放问题

- OQ-001：CSV 是否需要包含可读金额列？当前决定：只导出 `amount` 分单位整数，避免两种金额来源。
- OQ-002：是否允许过去日期？当前决定：允许，因为用户可能补录历史订阅。
- OQ-003：是否提供分页？当前决定：v1.0 不提供分页，数据量为个人本地使用规模。
````

### 5.3 编写 `specs/subscription-manager/api.md`

API 契约应稳定到足以支撑测试，但不必提前绑定框架内部错误对象的每个字段。

````markdown
# Subscription Tracker API

## 基础约定

- Base URL：`http://127.0.0.1:8000`
- 请求与响应默认使用 `application/json; charset=utf-8`。
- CSV 导出使用 `text/csv; charset=utf-8`。
- 所有时间戳使用 UTC ISO 8601。
- `id` 和 `created_at` 由服务端生成，客户端不得指定。

## 1. 健康检查

```http
GET /health
```

成功响应：

```json
{
  "status": "ok"
}
```

## 2. 创建订阅

```http
POST /api/subscriptions
```

请求示例：

```json
{
  "name": "Example Cloud",
  "amount": 1200,
  "currency": "CNY",
  "renewal_date": "2027-01-15",
  "note": "个人存储空间"
}
```

成功响应：`201 Created`

```json
{
  "id": 1,
  "name": "Example Cloud",
  "amount": 1200,
  "currency": "CNY",
  "renewal_date": "2027-01-15",
  "note": "个人存储空间",
  "created_at": "2026-11-24T00:00:00Z"
}
```

失败响应：`422 Unprocessable Entity`

当请求体缺少字段或字段不满足数据规则时，响应 MUST 标识出错字段和原因。具体 JSON 结构可沿用框架默认校验格式，但必须由测试固定，避免后续随机变化。

## 3. 查看订阅列表

```http
GET /api/subscriptions
```

成功响应：`200 OK`

```json
[
  {
    "id": 1,
    "name": "Example Cloud",
    "amount": 1200,
    "currency": "CNY",
    "renewal_date": "2027-01-15",
    "note": "个人存储空间",
    "created_at": "2026-11-24T00:00:00Z"
  },
  {
    "id": 2,
    "name": "Domain Renewal",
    "amount": 8800,
    "currency": "CNY",
    "renewal_date": "2027-03-01",
    "note": "",
    "created_at": "2026-11-24T00:05:00Z"
  }
]
```

排序规则：`renewal_date` 升序；相同日期按 `id` 升序。

## 4. 更新订阅

```http
PUT /api/subscriptions/{id}
```

请求示例：

```json
{
  "name": "Example Cloud Pro",
  "amount": 2400,
  "currency": "CNY",
  "renewal_date": "2027-01-15",
  "note": "已升级存储空间"
}
```

成功响应：`200 OK`，返回更新后的完整记录。  
记录不存在：`404 Not Found`

```json
{
  "detail": "Subscription not found"
}
```

## 5. 删除订阅

```http
DELETE /api/subscriptions/{id}
```

成功响应：`204 No Content`  
记录不存在：`404 Not Found`

## 6. CSV 导出

```http
GET /api/subscriptions/export.csv
```

成功响应：`200 OK`

响应头应包含：

```http
Content-Type: text/csv; charset=utf-8
```

响应体示例：

```csv
id,name,amount,currency,renewal_date,note,created_at
1,Example Cloud,1200,CNY,2027-01-15,个人存储空间,2026-11-24T00:00:00Z
2,"Domain, Renewal",8800,CNY,2027-03-01,,2026-11-24T00:05:00Z
```
````

### 5.4 编写 `specs/subscription-manager/scenarios.md`

````markdown
# Subscription Tracker Scenarios

## SC-001　创建有效订阅

Given 应用已启动且数据库中没有订阅  
When 提交 `name="Example Cloud"`、`amount=1200`、`currency="CNY"`、`renewal_date="2027-01-15"`  
Then 创建请求返回 201  
And 返回记录包含服务端生成的 `id` 和 `created_at`  
And 列表请求返回 1 条记录

## SC-002　拒绝无效金额

Given 用户正在创建订阅  
When `amount=0` 或 `amount=-100` 或 `amount=12.5`  
Then 请求返回 422  
And 数据库中的订阅数量不变

## SC-003　拒绝无效货币和日期

Given 用户正在创建订阅  
When `currency="RMB"` 或 `renewal_date="2027-13-40"`  
Then 请求返回 422  
And 错误信息标识对应字段  
And 数据库中的订阅数量不变

## SC-004　列表排序

Given 数据库中存在续费日期分别为 `2027-03-01`、`2027-01-15`、`2027-01-15` 的三条订阅  
When 请求订阅列表  
Then 返回顺序按日期升序排列  
And 日期相同的两条记录按 `id` 升序排列

## SC-005　更新不存在的订阅

Given 数据库中不存在 `id=999` 的订阅  
When 对 `/api/subscriptions/999` 发起更新请求  
Then 返回 404  
And 数据库内容不变

## SC-006　删除后不再导出

Given 数据库中存在两条订阅  
When 删除其中一条并请求 CSV 导出  
Then CSV 只包含剩余一条数据记录  
And 表头字段顺序保持不变

## SC-007　重启后数据保留

Given 已成功创建一条订阅  
When 停止应用、重新启动应用并请求列表  
Then 该订阅仍存在  
And `id`、`amount`、`currency`、`renewal_date` 和 `created_at` 均未变化
````

### 5.5 建立追踪表

新建 `docs/spec-traceability.md`：

````markdown
# Spec Traceability

| Intent | Acceptance | Spec | Scenario | 计划任务 | 测试 |
|---|---|---|---|---|---|
| G1 记录订阅 | AC-01、AC-02、AC-04 | SUB-001、SUB-003、SUB-004 | SC-001、SC-002、SC-003、SC-007 | 第 6 章拆分 | 待补 |
| G2 查看列表 | AC-03 | SUB-002 | SC-004 | 第 6 章拆分 | 待补 |
| G3 修改或删除 | AC-05、AC-06 | SUB-005、SUB-006 | SC-005、SC-006 | 第 6 章拆分 | 待补 |
| G4 导出 CSV | AC-07 | SUB-007 | SC-006 | 第 6 章拆分 | 待补 |
| G5 可维护交付 | AC-08 | NFR-001、NFR-002、OPS-001 | 待补 | 第 6 章拆分 | 待补 |
````

“计划任务”和“测试”两列在第 6 章和第 9 章逐步填写。规格阶段允许它们为空，但不允许 Intent 或 Acceptance 找不到对应 Spec。

### 5.6 独立澄清审查

开启新的 AI 会话，执行只读审查：

```text
目标：检查 Subscription Tracker 规格是否存在歧义、矛盾或不可测试内容。

上下文：
- 请阅读 `docs/intent.md`、`docs/acceptance.md`、`specs/subscription-manager/spec.md`、`specs/subscription-manager/api.md`、`specs/subscription-manager/scenarios.md` 和 `docs/spec-traceability.md`。
- 项目是本地单用户应用，不包含登录、提醒、邮箱抓取、汇率换算和支付功能。

范围：
- 只审查规格，不修改文件，不生成实现代码。
- 重点检查字段规则、状态码、排序、持久化、CSV、错误处理和追踪表。

约束：
- 每条问题必须引用文件和需求 ID。
- 区分 blocker、major、minor。
- 不要建议扩大 v1.0 范围。

验收：
- 找出无法转成测试的描述。
- 找出 API 与 Spec 不一致之处。
- 找出 Acceptance 未覆盖或重复覆盖的情况。

输出：
1. 问题清单；
2. 每条问题的最小修改建议；
3. 是否可以进入架构与规划阶段的结论。
```

## 6. AI 应生成的产物

合理产物：

- 行为规格；
- API 契约；
- Given/When/Then 场景；
- 追踪表；
- 开放问题和独立审查报告。

不合理产物：

- Python 路由、数据库模型或 Pydantic Schema 代码；
- 前端 HTML/CSS/JavaScript；
- pytest 测试代码；
- CI 配置；
- 具体函数名、类名和目录设计。

如果 AI 顺手写出了实现代码，应把它移到第 7 章之后，或放入临时草稿，不要提交到规格分支。

## 7. 人工检查点

1. **追踪是否闭合？**  
   从每个 `Gx` 找到 `AC-xx`，再找到 `SUB-xxx` 或 `OPS-xxx`。任何断链都要补规格或删目标。
2. **字段规则是否唯一？**  
   `amount` 全篇必须都是分单位整数；`currency` 全篇只能是 `CNY` 和 `USD`；`renewal_date` 全篇必须是 `YYYY-MM-DD`。
3. **状态码是否一致？**  
   创建成功是 201，更新成功是 200，删除成功是 204，不存在是 404，校验失败是 422。不要在同一接口中混用 200 和 201。
4. **阶段是否明确？**  
   v0.1 不应包含完整校验、更新、删除和 CSV 导出。规格可以提前写清楚，但任务计划必须分阶段实现。
5. **异常路径是否足够？**  
   至少检查空名称、0 或负金额、非整数金额、不支持货币、无效日期、更新不存在记录和删除不存在记录。
6. **是否过度设计？**  
   分页、缓存、软删除、国际化、权限、报表和消息队列都不应出现在第一版规格中，除非 Intent 明确要求。

## 8. 验收命令与通过标准

运行：

```powershell
git status --short
git diff --check
git diff --name-only
```

通过标准：

- 新增文件只包含规格、API、场景、追踪表和本章说明允许的文档。
- `spec-traceability.md` 中每个 Intent 都有至少一条 Spec。
- AC-01 到 AC-08 都能对应到 Spec 或明确标记为后续阶段。
- API 示例字段与数据规则表完全一致。
- 每个正常路径至少有一个异常路径。
- 没有生成应用代码、测试代码或 CI 配置。

本章的“通过”不是 AI 说规格完整，而是追踪表闭合且人工确认字段、状态码和阶段没有冲突。

## 9. 常见失败及恢复方法

| 症状 | 原因 | 恢复动作 |
|---|---|---|
| Spec 写满“高效、稳定、安全、易用”，但无法测试 | 把质量愿望当成行为需求 | 删除主观描述，改写成具体输入、操作、状态码和数据变化 |
| API 中出现 `price`，Spec 中却叫 `amount` | 工具或 AI 在不同段落自行改名 | 以数据规则表为准，全文统一字段名，并用追踪表检查所有示例 |
| Spec 同时规定类名、函数名、目录和数据库表结构 | 把第 6 章架构决策提前写入行为契约 | 将实现细节移到架构草稿；Spec 只保留外部行为和必要约束 |
| Spec Kit、OpenSpec 和手写规格同时存在三份文档 | 多工具并行管理同一状态 | 选择仓库内 `specs/subscription-manager/` 作为唯一事实源，其他工具输出仅作为审查草稿 |
| 只写成功创建，不写无效输入和 404 | 忽略异常路径 | 按字段逐个补校验场景，并为更新/删除补记录不存在场景 |
| 后续代码改了行为，但规格没有更新 | 把规格当一次性文档 | 先提交 Spec Delta，再修改代码；追踪表中记录变更原因 |

如果规格文件已经混乱，不要逐行修补。可以恢复到本章起点后重做：

```powershell
git switch docs/intent-and-acceptance
git switch -c docs/specification-retry
```

## 10. 本章 Git 提交

建议分支：

```text
docs/specification
```

建议提交拆分：

```powershell
git add specs/subscription-manager/spec.md
git commit -m "docs: add subscription behavior specification"

git add specs/subscription-manager/api.md
git commit -m "docs: define subscription API contract"

git add specs/subscription-manager/scenarios.md
git commit -m "docs: add acceptance scenarios"

git add docs/spec-traceability.md
git commit -m "docs: trace intent and acceptance to spec"
```

每次提交前查看：

```powershell
git diff --staged --stat
git diff --staged
```

如果发现应用代码混入暂存区，使用：

```powershell
git restore --staged PATH
```

## 11. 练习与扩展

1. **新增货币**：把 `currency` 扩展为支持 `EUR`，写一份只包含变更内容的 Spec Delta，不要重写整份规格。
2. **增加分页**：为列表 API 设计 `limit` 和 `offset`，并说明默认值、最大值、越界行为和排序稳定性。
3. **补充搜索规格**：为 v1.1 的搜索筛选功能写规格，但不实现代码。
4. **工具对照**：阅读 Spec Kit 的阶段说明和 OpenSpec 的变更说明，用 200 字写出两者分别适合什么项目阶段。
5. **反向追踪**：从 `SC-006` 反查它覆盖了哪些 Acceptance、Spec 和 Intent；如果查不到，说明追踪表有断链。

## 12. 参考资料

- [github/spec-kit](https://github.com/github/spec-kit)
- [Spec Kit agentic SDD reference](https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md)
- [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [需求和架构（GSE 2026 第 6 讲）](https://jyywiki.cn/GSE/2026/lect6.md)
