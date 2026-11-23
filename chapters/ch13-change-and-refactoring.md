# 第 13 章　需求演化与重构：修改系统，而不是重新生成系统

> 本章成果：在已有的 `v1.0`／`v1.1` 项目上，用规格变更、保护性测试和局部重构增加订阅搜索与筛选功能，而不是让 AI 重新生成整个项目。

## 1. 本章成果

完成本章后，你应该得到：

1. 一份搜索与筛选功能的变更规格。
2. 一组保护现有列表行为的测试。
3. 一个不改变外部行为的小型重构。
4. 一个支持 `q`、`currency` 和 `renewal_to` 的列表 API。
5. 一个最小可用的 Web 界面筛选表单。
6. 一条经验：需求变更应先改规格和测试，再改实现；重构与功能变更应使用不同提交，避免一次大 Diff 同时改变行为和结构。

## 2. 为什么需要它

AI 很容易把“增加搜索功能”理解成“重写整个列表模块”。项目变大以后，这种行为会带来三个问题：

1. 原有 API 契约可能被悄悄改变。
2. 既有页面、测试和文档可能失去对应实现。
3. 人工审查时无法判断哪些修改来自新需求，哪些修改来自 AI 的顺手重构。

维护阶段的关键不是“能不能让 AI 写出来”，而是能不能让修改保持局部、可解释、可回滚。规格变更、保护性测试和小 PR 就是把大风险拆成可检查的小步骤。

## 3. 最少必备知识

1. **变更规格（Spec Delta）**：只描述本次需求变化，而不是重写整份长期规格。
2. **保护性测试**：在改动前记录当前外部行为，使后续修改有回归依据。
3. **行为保持重构**：调整内部结构，但不改变 API、状态码、响应字段和排序。
4. **查询参数**：HTTP GET 请求中用于过滤结果的键值对。
5. **SQL 参数化查询**：把用户输入作为参数传给数据库，而不是拼接进 SQL 字符串。
6. **LIKE 通配符**：SQL 中 `%` 表示任意字符，`_` 表示单个字符；用户输入的 `%` 和 `_` 需要转义，否则搜索语义会出错。

## 4. 起始项目状态

从第 12 章 CSV 修复合并后的状态继续。确保工作区干净：

```powershell
git status
git switch main
python -m pytest -q
python -m ruff check .
```

创建功能分支：

```powershell
git switch -c feat/subscription-search-filter
```

本章的目标行为如下：

```text
GET /api/subscriptions
GET /api/subscriptions?q=VPN
GET /api/subscriptions?currency=USD
GET /api/subscriptions?renewal_to=2026-12-31
GET /api/subscriptions?q=VPN&currency=USD&renewal_to=2026-12-31
```

规则：

- 不带参数时，行为与现有列表接口完全一致。
- `q` 对 `name` 和 `note` 做不区分大小写的子串搜索。
- `q` 前后空白会被去除；空字符串视为不过滤。
- `currency` 会去除空白并转为大写后精确匹配。
- `renewal_to` 是 ISO 日期，表示 `renewal_date <= renewal_to`，包含当天。
- 多个条件同时存在时使用 AND。
- 没有匹配结果时返回 `200` 和空数组，不返回 `404`。
- 无效日期返回 FastAPI 默认的 `422`。
- 不新增分页、排序参数、权限或数据库字段。

## 5. 操作步骤与 AI 任务示例

### 5.1 先写变更规格

创建 `specs/changes/add-subscription-search.md`。它不是最终长期规格，而是这次变更的契约。

```markdown
# 变更规格：订阅搜索与筛选

## 动机

订阅数量增加后，用户需要快速找到特定名称、货币或续费日期范围内的记录。

## 当前行为

GET /api/subscriptions 返回全部订阅记录，排序和响应结构保持 v1.0 契约。

## 新行为

### 查询参数

| 参数 | 类型 | 必填 | 规则 |
|---|---|---|---|
| q | string | 否 | 去除空白；空值忽略；不区分大小写搜索 name 与 note |
| currency | string | 否 | 去除空白并转大写；精确匹配 |
| renewal_to | date | 否 | ISO 日期；renewal_date <= renewal_to；无效日期返回 422 |

### 验收场景

1. 不带参数时返回与改动前相同的记录集合和顺序。
2. `q=vpn` 能匹配名称或备注中包含 `VPN`、`vpn` 的记录。
3. `q=100%` 中的 `%` 按普通字符搜索，不作为 SQL 通配符。
4. `currency=usd` 与 `currency=USD` 行为一致。
5. `renewal_to=2026-12-05` 包含 2026-12-05 当天。
6. 多个参数同时存在时取交集。
7. 无结果返回 200 和空数组。

## 非目标

- 不增加分页。
- 不修改排序。
- 不增加高级表达式搜索。
- 不修改数据库 schema。
- 不改变创建、更新、删除和 CSV 导出接口。
```

实现合并后，再把上述稳定规则同步到正式规格 `specs/subscription-manager/spec.md`。不要把变更历史只留在聊天记录里。

### 5.2 增加保护性测试

在改实现前，先固定当前列表接口的外部契约。加入 `tests/test_api.py`：

```python
def test_list_without_filters_preserves_existing_contract(client):
    payloads = [
        {
            "name": "Cloud Storage",
            "amount": 990,
            "currency": "USD",
            "renewal_date": "2026-12-01",
            "note": "annual plan",
        },
        {
            "name": "VPN",
            "amount": 1299,
            "currency": "USD",
            "renewal_date": "2026-12-05",
            "note": "team plan",
        },
        {
            "name": "音乐会员",
            "amount": 1500,
            "currency": "CNY",
            "renewal_date": "2026-11-30",
            "note": "",
        },
    ]

    for payload in payloads:
        response = client.post("/api/subscriptions", json=payload)
        assert response.status_code in (200, 201)

    response = client.get("/api/subscriptions")
    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 3

    required_fields = {
        "id",
        "name",
        "amount",
        "currency",
        "renewal_date",
        "note",
        "created_at",
    }
    for item in body:
        assert required_fields.issubset(item)
```

如果你的现有接口返回包装对象，例如 `{"items": [...]}`，不要为了适配本章示例修改 API；应按当前真实契约调整测试。保护性测试的职责是记录现状，不是规定一个想象出来的接口。

运行：

```powershell
python -m pytest -q tests/test_api.py -k list
```

### 5.3 行为保持重构

如果当前查询逻辑散落在路由函数中，先做一次不增加功能的内部重构。目标只有一个：让后续搜索筛选逻辑进入 `app/repository.py`，而不是继续堆在路由层。

AI 任务示例：

```text
目标：在不改变外部行为的前提下，把 GET /api/subscriptions 的数据查询逻辑移动到 repository 层。

上下文：
- 项目：Subscription Tracker。
- 当前列表接口为 GET /api/subscriptions。
- tests/test_api.py 中已有 test_list_without_filters_preserves_existing_contract。
- 本次不新增 q、currency、renewal_to 参数。

范围：
1. app/routes.py。
2. app/repository.py。
3. 如确有必要，调整 tests/test_repository.py。

约束：
1. 不改变 URL、HTTP 方法、状态码、响应字段和排序。
2. 不修改数据库 schema。
3. 不新增业务功能。
4. 不升级依赖。
5. 保持 SQL 参数化。
6. 只重构当前列表查询路径。

验收：
1. python -m pytest -q 全部通过。
2. python -m ruff check . 通过。
3. git diff --stat 只显示与列表查询相关的文件。
4. 重构前后的 API 响应结构和排序一致。

输出：
1. 修改文件列表。
2. 行为是否保持不变的证据。
3. 任何无法确认的假设。
```

重构完成后运行：

```powershell
python -m pytest -q
git diff --stat
```

如果保护性测试失败，说明这次不是行为保持重构，应立即回退并缩小范围。

### 5.4 实现搜索筛选

新增或扩展 `app/repository.py` 中的查询函数。以下代码为示意，请结合当前数据库访问方式调整：

```python
def escape_like(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("%", "\\%")
        .replace("_", "\\_")
    )


def list_subscriptions(
    db,
    q: str | None = None,
    currency: str | None = None,
    renewal_to: str | None = None,
) -> list[dict]:
    sql = """
        SELECT id, name, amount, currency, renewal_date, note, created_at
        FROM subscriptions
    """
    conditions: list[str] = []
    params: list[str] = []

    if q:
        needle = f"%{escape_like(q.casefold())}%"
        conditions.append(
            "(lower(name) LIKE ? ESCAPE '\\' OR lower(note) LIKE ? ESCAPE '\\')"
        )
        params.extend([needle, needle])

    if currency:
        conditions.append("upper(currency) = ?")
        params.append(currency)

    if renewal_to:
        conditions.append("renewal_date <= ?")
        params.append(renewal_to)

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " ORDER BY renewal_date, id"

    rows = db.execute(sql, params).fetchall()
    return [dict(row) for row in rows]
```

路由层负责解析和规范化输入：

```python
from datetime import date


def normalize_optional_text(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = value.strip()
    return cleaned or None


@router.get("/api/subscriptions")
def list_subscriptions(
    q: str | None = None,
    currency: str | None = None,
    renewal_to: date | None = None,
):
    normalized_currency = normalize_optional_text(currency)
    if normalized_currency:
        normalized_currency = normalized_currency.upper()

    return repository.list_subscriptions(
        db=get_db(),
        q=normalize_optional_text(q),
        currency=normalized_currency,
        renewal_to=renewal_to.isoformat() if renewal_to else None,
    )
```

如果当前项目使用 FastAPI 依赖注入获取数据库连接，请保留原来的 `Depends(get_db)` 写法，不要为了示例引入新的全局连接方式。

### 5.5 为新行为补测试

至少覆盖以下场景：

```python
def test_search_matches_name_and_note_case_insensitively(client):
    ...

def test_like_wildcards_in_query_are_literal(client):
    ...

def test_currency_filter_is_case_insensitive(client):
    ...

def test_renewal_to_is_inclusive(client):
    ...

def test_combined_filters_use_and_semantics(client):
    ...

def test_no_match_returns_empty_list_not_404(client):
    ...
```

一个完整示例：

```python
def test_combined_filters_use_and_semantics(client):
    records = [
        {
            "name": "VPN Pro",
            "amount": 1299,
            "currency": "USD",
            "renewal_date": "2026-12-05",
            "note": "team",
        },
        {
            "name": "VPN Lite",
            "amount": 590,
            "currency": "CNY",
            "renewal_date": "2026-12-05",
            "note": "personal",
        },
        {
            "name": "Cloud VPN",
            "amount": 990,
            "currency": "USD",
            "renewal_date": "2027-01-10",
            "note": "backup",
        },
    ]
    for record in records:
        response = client.post("/api/subscriptions", json=record)
        assert response.status_code in (200, 201)

    response = client.get(
        "/api/subscriptions",
        params={
            "q": "vpn",
            "currency": "USD",
            "renewal_to": "2026-12-31",
        },
    )
    assert response.status_code == 200

    names = [item["name"] for item in response.json()]
    assert names == ["VPN Pro"]
```

### 5.6 最小前端集成

在 `app/static/index.html` 中加入筛选控件：

```html
<div class="filters">
  <label for="filter-q">搜索</label>
  <input id="filter-q" type="search" placeholder="名称或备注" />

  <label for="filter-currency">货币</label>
  <select id="filter-currency">
    <option value="">全部</option>
    <option value="USD">USD</option>
    <option value="CNY">CNY</option>
  </select>

  <label for="filter-renewal-to">续费日期不晚于</label>
  <input id="filter-renewal-to" type="date" />

  <button id="filter-reset" type="button">重置</button>
</div>
```

在 `app/static/app.js` 中只修改加载列表的 URL 构造，不要重写现有渲染函数：

```javascript
async function loadSubscriptions() {
  const params = new URLSearchParams();

  const q = document.getElementById("filter-q")?.value.trim();
  const currency = document.getElementById("filter-currency")?.value;
  const renewalTo = document.getElementById("filter-renewal-to")?.value;

  if (q) params.set("q", q);
  if (currency) params.set("currency", currency);
  if (renewalTo) params.set("renewal_to", renewalTo);

  const query = params.toString();
  const url = `/api/subscriptions${query ? `?${query}` : ""}`;

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  renderSubscriptions(await response.json());
}
```

为搜索框、货币选择和日期控件绑定重新加载事件。具体事件绑定应沿用当前 `app.js` 已有模式，不要为了一个筛选功能引入新的前端框架。

## 6. AI 应生成的产物

1. `specs/changes/add-subscription-search.md`。
2. 保护现有列表契约的测试。
3. 行为保持重构的小 Diff。
4. 搜索筛选 API 实现。
5. 新行为的单元或接口测试。
6. 最小前端筛选集成。
7. 合并后同步到正式规格的说明。

AI 不应该生成：

- 新的分页系统。
- 新的排序参数。
- 新的数据库字段。
- 全文搜索引擎。
- 与搜索无关的 UI 重构。
- 一次性覆盖 `app.js` 的大规模前端重写。

## 7. 人工检查点

1. **规格是否先于实现**：没有变更规格就直接写代码，后续无法判断 AI 是否私自扩大范围。
2. **保护性测试是否基于现状**：它应记录当前 API，而不是理想 API。
3. **重构提交是否没有功能变化**：查看 Diff，确认没有新增查询参数。
4. **SQL 是否参数化**：用户输入不能作为字符串拼进 SQL。
5. **LIKE 通配符是否转义**：搜索 `100%` 时，`%` 应当作普通字符。
6. **日期边界是否清楚**：`renewal_to` 包含当天，且测试覆盖当天记录。
7. **响应结构是否未变**：无结果仍应是 `200` 和空数组。
8. **前端是否只修改加载逻辑**：渲染、表单提交和现有事件不应被大面积重写。

## 8. 验收命令与通过标准

```powershell
python -m pytest -q
python -m pytest -q -k "list or search or filter"
python -m ruff check .
git diff --stat
git diff --check
```

启动应用并手工检查：

```powershell
python -m uvicorn app.main:app --reload
```

另一个 PowerShell 窗口：

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/api/subscriptions"
Invoke-RestMethod "http://127.0.0.1:8000/api/subscriptions?q=VPN"
Invoke-RestMethod "http://127.0.0.1:8000/api/subscriptions?currency=USD&renewal_to=2026-12-31"
```

通过标准：

1. 原有测试全部通过。
2. 搜索筛选测试全部通过。
3. Ruff 没有新增错误。
4. API 响应字段与 v1.0 保持一致。
5. 空结果返回空数组，不返回 404。
6. Diff 中没有无关文件。
7. 浏览器中筛选控件能正确刷新列表。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| 新测试通过，但页面无变化 | 前端仍调用旧 URL，或事件没有绑定 | 检查 `app.js` 中实际请求 URL 和浏览器开发者工具 Network 面板 |
| 搜索 `%` 返回所有记录 | LIKE 通配符未转义 | 使用 `escape_like()`，并补充 `q=100%` 的测试 |
| 日期筛选结果少一天 | 把 `renewal_to` 实现成 `<` 而非 `<=` | 对照规格修改 SQL，并增加当天边界测试 |
| 原列表顺序改变 | 重构时修改了 `ORDER BY` | 恢复保护性测试，要求 AI 只改结构不改排序 |
| AI 一次修改了创建、删除和导出接口 | 任务范围过宽 | 回退分支，重新拆成搜索 API、搜索测试和前端集成三个小任务 |
| 搜索对中文正常，对英文大小写不稳定 | 只做了 SQL `LIKE`，没有统一 `lower()` 或 `casefold()` | 在测试中加入大小写混合样本，再修正查询构造 |

## 10. 本章 Git 提交

建议分支：

```text
feat/subscription-search-filter
```

建议提交顺序：

```text
docs: add subscription search and filter change spec
test: protect existing subscription list contract
refactor: move subscription list query into repository
feat: add subscription search and filter API
test: cover search, currency and renewal date filters
feat: expose subscription filters in web UI
docs: sync search filter rules into canonical spec
```

如果团队要求每个提交都通过 CI，可以把失败的新行为测试与对应实现合并为一个 `feat:` 提交。关键原则是：重构提交不改行为，功能提交不夹带大规模无关重构。

## 11. 练习与扩展

1. 增加 `renewal_from` 参数，形成日期范围筛选。
2. 增加 `sort` 参数，但必须单独写规格、测试和 ADR。
3. 把当前筛选条件写入浏览器 URL，使列表结果可以被分享或刷新后恢复。
4. 为 `name`、`note` 和 `renewal_date` 增加数据库索引，并用测试记录查询语义不变。
5. 让一个全新 AI 会话只读取仓库和变更规格，然后复述本次功能的验收标准；如果它复述错误，说明规格还不够清楚。

## 12. 参考资料

1. GitHub Spec Kit：[Agentic SDD reference](https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md)
2. FastAPI 官方文档：[Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
3. Google Engineering Practices：[Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)
4. Fission-AI：[OpenSpec](https://github.com/Fission-AI/OpenSpec)
