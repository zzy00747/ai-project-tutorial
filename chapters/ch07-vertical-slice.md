# 第 7 章　纵向打通：生成第一个真正可用的版本

> 本章成果：让读者完成 Subscription Tracker 的第一个可用纵向切片，从浏览器表单到 FastAPI 接口再到 SQLite 数据表，保存并查看一条订阅记录。

## 1. 本章成果

完成本章后，项目应当具备：

- 一个可启动的 FastAPI 应用，并暴露 `/health` 健康检查。
- 一个 SQLite 数据表，能够持久保存订阅记录。
- 两个核心 API：
  - `GET /api/subscriptions`：列出全部订阅。
  - `POST /api/subscriptions`：创建一条订阅。
- 一个最小网页：填写表单、提交数据、显示已有订阅。
- 一条端到端证据：浏览器刷新后，刚才创建的订阅仍然存在。

对应版本为 **v0.1**。它不追求漂亮界面，也不实现修改、删除、导入导出、提醒或用户登录。本章只证明一件事：

> 用户操作、HTTP 请求、后端校验、数据持久化和页面展示能够真正连通。

如果这条“纵向切片”不成立，后续所有功能都只是叠在不可靠地基上的演示。

## 2. 为什么需要它

很多 AI 生成的项目看起来一次性完成了很多页面和模块，但存在一个共同问题：每一块都可以局部运行，整体却无法可靠串起来。典型表现包括：

- 页面能显示，但数据没有真正写入数据库。
- API 能返回固定示例数据，但没有经过校验。
- 后端能创建数据，但刷新页面后前端看不到。
- 项目能运行，却没有人知道启动命令、数据库位置或失败原因。
- AI 一次生成大量文件，读者无法判断哪些代码与当前需求有关。

纵向切片的目的，是先用最小功能打通真实路径：

```text
浏览器表单
→ fetch 请求
→ FastAPI 路由
→ Pydantic 校验
→ SQLite 写入
→ GET 查询
→ 前端渲染
```

这条链路一旦可运行、可检查，后续增加修改、删除、搜索、测试和部署时，才有稳定的反馈边界。

## 3. 最少必备知识

不需要先系统学完 Python、HTTP 或数据库，但要理解本章使用的几个概念：

- **HTTP 请求与响应**：浏览器通过 `GET` 获取数据，通过 `POST` 提交数据。
- **JSON**：前后端交换的数据格式，例如 `{"name": "Music", "amount": 1500}`。
- **API 路由**：后端暴露的固定地址，例如 `/api/subscriptions`。
- **数据库表**：SQLite 中的 `subscriptions` 表负责持久保存记录。
- **静态文件**：`index.html`、`app.js` 和 `styles.css` 由 FastAPI 提供给浏览器。
- **金额单位**：为了避免浮点误差，本项目 `amount` 字段统一使用**分**为单位的正整数。`1500` 表示 `15.00` 元。

如果某个概念暂时不清楚，可以先照步骤完成任务，再回到本节和报错信息建立理解。

## 4. 起始项目状态

开始本章前，应当已经完成意图、规格、架构和任务拆分，仓库中至少存在这些内容：

```text
subscription-tracker/
├─ docs/
│  ├─ intent.md
│  ├─ acceptance.md
│  ├─ plan.md
│  └─ tasks.md
├─ specs/
├─ AGENTS.md
├─ ARCHITECTURE.md
├─ README.md
└─ requirements.txt
```

`requirements.txt` 可以先写入：

```text
fastapi
pydantic
uvicorn[standard]
pytest
httpx
ruff
```

然后创建并激活虚拟环境：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS 或 Linux 使用：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

本章结束时，项目将扩展为：

```text
subscription-tracker/
├─ app/
│  ├─ __init__.py
│  ├─ database.py
│  ├─ main.py
│  ├─ repository.py
│  ├─ routes.py
│  ├─ schemas.py
│  └─ static/
│     ├─ app.js
│     ├─ index.html
│     └─ styles.css
└─ requirements.txt
```

`tests/` 暂不在本章创建，后续测试章节会加入。

## 5. 操作步骤与 AI 任务示例

### 5.1 定义本章的唯一任务

不要把“生成整个项目”直接交给 AI。当前任务只有一条：

> 实现一个可以添加并查看订阅记录的纵向切片。

建议把它写入 `docs/tasks.md`：

```markdown
### T-07 纵向切片：添加并查看订阅

目标：用户可以通过网页添加一条订阅，并在刷新后看到这条订阅。

范围：
- `GET /api/subscriptions`
- `POST /api/subscriptions`
- `/health`
- 最小表单和列表

不做：
- 修改、删除、搜索、导出
- 用户登录和提醒
- 数据库迁移工具
- 额外前端框架

完成标准：
- 新记录能保存到 SQLite。
- 页面刷新后仍显示该记录。
- 非法金额返回 422。
- 服务日志没有未处理异常。
```

### 5.2 给 AI 的任务示例

可以直接使用下面这个任务，也可以换成自己的编码 Agent：

```text
目标：
为 Subscription Tracker 实现 v0.1 纵向切片，让浏览器表单可以通过 FastAPI 将一条订阅记录保存到 SQLite，并能列出全部记录。

上下文：
- 当前仓库已有 docs/、specs/、AGENTS.md、ARCHITECTURE.md 和 requirements.txt。
- Python 版本为 3.12+。
- 后端使用 FastAPI，数据访问使用 Python 标准库 sqlite3，不引入 ORM。
- 前端只使用原生 HTML、CSS 和 JavaScript。
- 数据库文件路径通过环境变量 DATABASE_PATH 配置，默认为项目根目录下的 subscriptions.db。
- 订阅字段为 id、name、amount、currency、renewal_date、note、created_at。
- amount 必须是以分为单位的正整数。
- renewal_date 使用 ISO 日期格式 YYYY-MM-DD。

范围：
只能创建或修改以下文件：
- requirements.txt
- app/__init__.py
- app/database.py
- app/schemas.py
- app/repository.py
- app/routes.py
- app/main.py
- app/static/index.html
- app/static/app.js
- app/static/styles.css

约束：
- 不创建测试文件。
- 不实现修改、删除、搜索、导入导出、提醒或认证。
- 不引入数据库迁移工具、ORM、前端框架、Tailwind、Node.js 构建流程或其他新依赖。
- SQL 必须使用参数绑定，禁止把用户输入拼接进 SQL 字符串。
- Pydantic 模型必须拒绝空名称、非正整数金额和错误的货币代码。
- created_at 由后端生成 UTC ISO 时间，不能接受客户端传入。
- 前端渲染订阅时必须使用 textContent 或 createElement，不能使用 innerHTML 拼接用户数据。
- /health 必须在静态文件挂载之前注册，避免被根路径静态服务遮蔽。
- 所有 API 路径使用 /api/subscriptions。

验收：
1. 运行 python -m uvicorn app.main:app --reload 后，访问 http://127.0.0.1:8000 可以看到表单。
2. 提交 name=Music、amount=1500、currency=CNY、renewal_date=2026-12-01 后，页面列表显示该记录。
3. 刷新页面，记录仍然存在。
4. GET /health 返回 {"status":"ok"}。
5. POST amount=0 返回 422。
6. python -m ruff check . 通过。
7. 服务日志中没有未处理异常。

输出：
- 按文件列出完整修改内容。
- 不要输出与任务无关的文档。
- 如果某个验收条件无法满足，先说明阻塞原因，不要伪造完成。
```

### 5.3 创建数据访问层

新建空文件 `app/__init__.py`，然后创建 `app/database.py`：

```python
import os
import sqlite3
from collections.abc import Iterator
from pathlib import Path


def connect(database_path: str | Path | None = None) -> sqlite3.Connection:
    """打开一个 SQLite 连接。

    默认路径来自环境变量 DATABASE_PATH；测试时可以直接传入临时数据库路径。
    """
    path = Path(database_path or os.getenv("DATABASE_PATH", "subscriptions.db"))
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(database_path: str | Path | None = None) -> None:
    """创建订阅表。"""
    connection = connect(database_path)
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                amount INTEGER NOT NULL CHECK (amount > 0),
                currency TEXT NOT NULL DEFAULT 'CNY',
                renewal_date TEXT NOT NULL,
                note TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


def get_db() -> Iterator[sqlite3.Connection]:
    """FastAPI 依赖项：为一次请求提供数据库连接，并在请求结束后关闭。"""
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()
```

这里有两个关键点：

1. `connect()` 每次读取 `DATABASE_PATH`，因此测试和生产可以使用不同数据库。
2. `get_db()` 的 `finally` 分支负责关闭连接，避免请求结束后连接泄漏。

### 5.4 定义请求与响应模型

创建 `app/schemas.py`：

```python
from datetime import date, datetime

from pydantic import BaseModel, Field, field_validator


class SubscriptionBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    amount: int = Field(gt=0, description="金额，单位为分")
    currency: str = Field(min_length=3, max_length=3)
    renewal_date: date
    note: str = Field(default="", max_length=500)

    @field_validator("name", "currency", "note", mode="before")
    @classmethod
    def strip_text(cls, value: object) -> object:
        if isinstance(value, str):
            return value.strip()
        return value

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value:
            raise ValueError("name cannot be empty")
        return value

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str) -> str:
        normalized = value.upper()
        if not normalized.isascii():
            raise ValueError("currency must be an ASCII code")
        return normalized


class SubscriptionCreate(SubscriptionBase):
    """创建订阅时客户端可以提供的字段。"""


class Subscription(SubscriptionBase):
    """返回给客户端的完整订阅记录。"""

    id: int
    created_at: datetime
```

这些模型承担第一道校验：

- `name` 去除首尾空格后不能为空。
- `amount` 必须是大于 `0` 的整数。
- `currency` 统一转为大写，例如 `cny` 会变成 `CNY`。
- `renewal_date` 必须能解析为日期。
- `id` 和 `created_at` 只能由后端产生，客户端无法通过 `SubscriptionCreate` 伪造。

### 5.5 实现仓库层

创建 `app/repository.py`：

```python
import sqlite3
from datetime import datetime, timezone

from .schemas import SubscriptionCreate


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_subscription(connection: sqlite3.Connection, subscription_id: int) -> dict | None:
    row = connection.execute(
        "SELECT * FROM subscriptions WHERE id = ?",
        (subscription_id,),
    ).fetchone()
    return dict(row) if row is not None else None


def list_subscriptions(connection: sqlite3.Connection) -> list[dict]:
    rows = connection.execute(
        "SELECT * FROM subscriptions ORDER BY renewal_date, id"
    ).fetchall()
    return [dict(row) for row in rows]


def create_subscription(
    connection: sqlite3.Connection,
    payload: SubscriptionCreate,
) -> dict:
    data = payload.model_dump(mode="json")
    data["created_at"] = _now_utc()

    with connection:
        cursor = connection.execute(
            """
            INSERT INTO subscriptions (
                name, amount, currency, renewal_date, note, created_at
            ) VALUES (
                :name, :amount, :currency, :renewal_date, :note, :created_at
            )
            """,
            data,
        )

    created = get_subscription(connection, int(cursor.lastrowid))
    if created is None:
        raise RuntimeError("subscription was created but could not be read back")
    return created
```

注意：

- `payload.model_dump(mode="json")` 会把 `date` 转成 ISO 字符串，适合直接存入 SQLite。
- `with connection:` 表示 SQL 成功时提交，异常时回滚。
- `get_subscription()` 在本章只被创建逻辑复用，但它也为后续按 ID 查询打好基础。

### 5.6 暴露 API

创建 `app/routes.py`：

```python
import sqlite3

from fastapi import APIRouter, Depends, status

from . import repository
from .database import get_db
from .schemas import Subscription, SubscriptionCreate

router = APIRouter(prefix="/api/subscriptions", tags=["subscriptions"])


@router.get("", response_model=list[Subscription])
def list_subscriptions_route(
    connection: sqlite3.Connection = Depends(get_db),
) -> list[dict]:
    return repository.list_subscriptions(connection)


@router.post(
    "",
    response_model=Subscription,
    status_code=status.HTTP_201_CREATED,
)
def create_subscription_route(
    payload: SubscriptionCreate,
    connection: sqlite3.Connection = Depends(get_db),
) -> dict:
    return repository.create_subscription(connection, payload)
```

两个路由都使用空路径 `""`，配合前缀后实际地址是 `/api/subscriptions`。

### 5.7 创建应用入口

创建 `app/main.py`：

```python
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import init_db
from .routes import router

STATIC_DIR = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Subscription Tracker",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(router)
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
```

`/health` 必须先注册，再挂载根路径静态文件，否则访问 `/health` 时可能被静态文件处理器拦截。

### 5.8 创建最小前端

创建 `app/static/index.html`：

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>个人订阅管理器</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <main>
      <h1>个人订阅管理器</h1>
      <p id="status" role="status"></p>

      <form id="subscription-form">
        <label>
          名称
          <input id="name" name="name" maxlength="100" required />
        </label>

        <label>
          金额（分）
          <input id="amount" name="amount" type="number" min="1" step="1" required />
        </label>

        <label>
          货币
          <input id="currency" name="currency" value="CNY" maxlength="3" required />
        </label>

        <label>
          续费日期
          <input id="renewal_date" name="renewal_date" type="date" required />
        </label>

        <label>
          备注
          <input id="note" name="note" maxlength="500" />
        </label>

        <button type="submit">添加订阅</button>
      </form>

      <section>
        <h2>现有订阅</h2>
        <ul id="subscription-list"></ul>
      </section>
    </main>

    <script src="app.js"></script>
  </body>
</html>
```

创建 `app/static/app.js`：

```javascript
const form = document.getElementById("subscription-form");
const list = document.getElementById("subscription-list");
const statusElement = document.getElementById("status");
const apiUrl = "/api/subscriptions";

async function request(url, options = {}) {
  const response = await fetch(url, options);

  if (!response.ok) {
    let message = `${response.status} ${response.statusText}`;
    try {
      const body = await response.json();
      if (body.detail !== undefined) {
        message = JSON.stringify(body.detail);
      }
    } catch {
      // 响应不是 JSON 时，保留默认 HTTP 状态信息。
    }
    throw new Error(message);
  }

  return response.status === 204 ? null : response.json();
}

function render(subscriptions) {
  list.replaceChildren();

  for (const item of subscriptions) {
    const entry = document.createElement("li");
    let text = `${item.name}：${item.amount} ${item.currency}，${item.renewal_date}`;
    if (item.note) {
      text += `（${item.note}）`;
    }
    entry.textContent = text;
    list.appendChild(entry);
  }
}

function showMessage(message, isError = false) {
  statusElement.textContent = message;
  statusElement.className = isError ? "error" : "";
}

async function refresh() {
  const subscriptions = await request(apiUrl);
  render(subscriptions);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const amount = Number(form.amount.value);
  if (!Number.isInteger(amount) || amount <= 0) {
    showMessage("金额必须是正整数，单位为分", true);
    return;
  }

  const payload = {
    name: form.name.value.trim(),
    amount,
    currency: form.currency.value.trim().toUpperCase(),
    renewal_date: form.renewal_date.value,
    note: form.note.value.trim(),
  };

  try {
    await request(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    form.reset();
    form.currency.value = "CNY";
    showMessage("订阅已添加");
    await refresh();
  } catch (error) {
    showMessage(error.message, true);
  }
});

refresh().catch((error) => showMessage(error.message, true));
```

创建 `app/static/styles.css`，先保证基本可读即可：

```css
body {
  font-family: system-ui, sans-serif;
  margin: 2rem auto;
  max-width: 42rem;
  padding: 0 1rem;
}

form {
  display: grid;
  gap: 0.75rem;
}

label {
  display: grid;
  gap: 0.25rem;
}

#status.error {
  color: #b00020;
}
```

### 5.9 启动并验证

在项目根目录运行：

```powershell
python -m uvicorn app.main:app --reload
```

浏览器访问：

```text
http://127.0.0.1:8000
```

填写：

- 名称：`Music`
- 金额（分）：`1500`
- 货币：`CNY`
- 续费日期：未来某个日期
- 备注：`vertical slice`

提交后，列表应显示这条记录；刷新页面，记录仍然存在。

也可以用 PowerShell 直接验证 API：

```powershell
$body = @{
  name = "Music"
  amount = 1500
  currency = "CNY"
  renewal_date = "2026-12-01"
  note = "created by api"
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/subscriptions" -ContentType "application/json" -Body $body
Invoke-RestMethod "http://127.0.0.1:8000/api/subscriptions"
```

### 5.10 更新任务状态

验证通过后，把 `docs/tasks.md` 中的 `T-07` 标记为完成，并记录：

- 实际创建的文件。
- 手工验收结果。
- 未覆盖的后续风险，例如“尚无自动测试”。

不要让任务状态只停留在 AI 会话里。

## 6. AI 应生成的产物

合格的 AI 输出应当包含这些文件，且不扩展无关功能：

```text
app/__init__.py
app/database.py
app/schemas.py
app/repository.py
app/routes.py
app/main.py
app/static/index.html
app/static/app.js
app/static/styles.css
```

同时应当能够解释：

- 数据表包含哪些字段。
- `POST /api/subscriptions` 如何校验金额、名称、货币和日期。
- `created_at` 为什么由后端生成。
- 前端提交后为什么需要重新调用 `GET /api/subscriptions`。
- 数据库文件默认保存在哪里。
- 如何通过 `DATABASE_PATH` 切换数据库位置。

如果 AI 额外生成了 ORM、迁移系统、登录认证、React 前端、Docker、CI 或“未来可能用到”的模块，应当要求它撤回并重新限定范围。

## 7. 人工检查点

逐条检查以下内容，不要只看页面是否能打开：

- [ ] `requirements.txt` 只包含本章需要的依赖，没有额外框架。
- [ ] SQL 全部使用参数绑定，没有出现 f-string 或字符串拼接。
- [ ] `amount` 的类型是 `int`，不是 `float`，且要求大于 `0`。
- [ ] `created_at` 由后端生成，客户端不能提交该字段。
- [ ] `SubscriptionCreate` 不包含 `id` 和 `created_at`。
- [ ] `/health` 在静态文件挂载之前注册。
- [ ] API 前缀是 `/api/subscriptions`，没有散落在 `main.py` 里的重复路由。
- [ ] 数据库连接在 `get_db()` 的 `finally` 中关闭。
- [ ] 前端使用 `textContent` 或 `createElement` 渲染用户输入，没有 `innerHTML`。
- [ ] 提交成功后调用 `form.reset()` 和 `refresh()`。
- [ ] 提交失败时错误显示在 `#status`，而不是只在浏览器控制台里出现。
- [ ] 刷新页面后数据仍然存在，说明写入的是 SQLite，不是 JavaScript 内存变量。

特别要检查 AI 是否“顺手”做了这些事：

- 添加登录、权限或提醒。
- 改成 SQLAlchemy、Tortoise、Prisma、Redis 或其他数据层。
- 创建额外前端框架或构建工具。
- 修改 `docs/`、`specs/` 或架构文档却未在输出中说明。
- 返回 `200` 而不是 `201` 后，又悄悄修改验收标准。

## 8. 验收命令与通过标准

在项目根目录依次运行：

```powershell
python -m compileall app
python -m ruff check .
python -m uvicorn app.main:app --reload
```

保持服务运行，另开一个终端检查健康状态：

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/health"
```

通过标准：

- `compileall` 没有语法错误。
- `ruff check .` 退出码为 `0`。
- `/health` 返回包含 `status` 为 `ok` 的 JSON。
- `POST` 一条合法订阅后返回包含 `id` 和 `created_at` 的对象。
- `GET /api/subscriptions` 能返回刚才创建的记录。
- 浏览器刷新页面后记录仍然存在。
- 服务日志中没有未处理异常。

再检查非法金额：

```powershell
curl.exe -i -X POST "http://127.0.0.1:8000/api/subscriptions" -H "Content-Type: application/json" -d "{\"name\":\"Invalid\",\"amount\":0,\"currency\":\"CNY\",\"renewal_date\":\"2026-12-01\",\"note\":\"\"}"
```

通过标准：

- HTTP 状态码为 `422`。
- 响应中包含与 `amount` 有关的校验错误。
- `GET /api/subscriptions` 没有新增 `Invalid` 记录。

如果使用 macOS 或 Linux，可直接使用 `curl` 代替 `curl.exe`。

## 9. 常见失败及恢复方法

### 失败 1：启动时提示 `ModuleNotFoundError: No module named 'app'`

**症状**：

```text
ModuleNotFoundError: No module named 'app'
```

**原因**：通常是在 `app/` 目录内部启动，或者虚拟环境未激活，导致 Python 找不到项目根目录下的 `app` 包。

**恢复动作**：

1. 回到 `subscription-tracker/` 项目根目录。
2. 确认当前目录能看到 `app/` 和 `requirements.txt`。
3. 激活虚拟环境并重新安装依赖。
4. 使用完整模块路径启动：

```powershell
python -m uvicorn app.main:app --reload
```

### 失败 2：页面能打开，但提交后返回 `404` 或 `405`

**症状**：

浏览器状态区显示：

```text
404 Not Found
```

或：

```text
405 Method Not Allowed
```

**原因**：常见原因包括路由前缀不一致、静态文件挂载顺序错误，或前端请求了错误地址。

**恢复动作**：

1. 检查 `app/routes.py` 的前缀是否为 `/api/subscriptions`。
2. 检查两个路由路径是否都是空字符串 `""`。
3. 检查 `app/static/app.js` 中的 `apiUrl` 是否为 `/api/subscriptions`。
4. 检查 `app/main.py` 中是否先 `include_router(router)`，再 `app.mount("/")`。
5. 重启服务后重新提交。

### 失败 3：API 返回 `500 Internal Server Error`，日志提示 `no such table: subscriptions`

**症状**：

```text
sqlite3.OperationalError: no such table: subscriptions
```

**原因**：数据库表没有初始化。可能是 `lifespan` 没有执行、`init_db()` 没有被调用，或者服务实际连接的数据库不是预期文件。

**恢复动作**：

1. 确认 `app/main.py` 使用了 `lifespan=lifespan`。
2. 确认 `lifespan()` 中调用了 `init_db()`。
3. 删除默认测试数据库文件，重新启动服务：

```powershell
Remove-Item subscriptions.db -ErrorAction SilentlyContinue
python -m uvicorn app.main:app --reload
```

4. 如果设置了 `DATABASE_PATH`，检查它指向的位置是否可写。

### 失败 4：提交表单时返回 `422`，但不知道哪个字段错误

**症状**：

状态区显示一大段 JSON，例如包含 `loc`、`msg` 和 `type`。

**原因**：FastAPI 使用 Pydantic 返回详细校验错误。前端当前直接把 `detail` 序列化显示，因此信息较原始。

**恢复动作**：

1. 先看响应中的 `loc`，它指出错误字段。
2. 常见修复：
   - `amount` 必须是正整数，单位为分。
   - `renewal_date` 必须是 `YYYY-MM-DD`。
   - `currency` 去除空格后必须正好三个字符。
   - `name` 去除空格后不能为空。
3. 暂时可以让 AI 优化错误展示，但不要在本章扩大到复杂前端状态管理。

### 失败 5：浏览器刷新后记录消失

**症状**：

添加后立即能看到记录，刷新页面后列表为空。

**原因**：数据只保存在前端 JavaScript 变量中，或后端没有真正提交 SQLite 事务。

**恢复动作**：

1. 检查 `repository.create_subscription()` 是否使用 `with connection:`。
2. 确认项目根目录生成了 `subscriptions.db`。
3. 用 `GET /api/subscriptions` 直接查询，而不是只看页面。
4. 如果 API 返回为空，说明写入没有成功；如果 API 有数据但页面为空，说明前端刷新或渲染逻辑有问题。

## 10. 本章 Git 提交

建议从一个新分支开始：

```powershell
git switch -c feat/vertical-slice
```

可以按职责拆成四次提交：

```powershell
git add requirements.txt
git commit -m "chore: add subscription tracker runtime dependencies"

git add app/__init__.py app/database.py app/schemas.py app/repository.py
git commit -m "feat: persist subscriptions with sqlite"

git add app/routes.py app/main.py
git commit -m "feat: expose subscription api and health endpoint"

git add app/static
git commit -m "feat: add minimal subscription web form"
```

提交前检查差异范围：

```powershell
git status
git diff --stat
git diff
```

如果 Diff 中出现了任务范围外的文件，先恢复它们，再提交：

```powershell
git restore PATH
```

## 11. 练习与扩展

完成主线后，可以选择一个练习，但每次仍然只做一个小变更：

1. 在列表中显示换算后的元金额，例如 `1500 分 = 15.00 CNY`。
2. 当列表为空时，显示“暂无订阅”。
3. 给 `note` 增加前端长度提示，并阻止超过 `500` 个字符。
4. 将 `renewal_date` 的默认值设置为下个月同一天。
5. 在页面中按续费日期排序，并与后端排序结果比较。
6. 把手工验收步骤整理到 `docs/runbooks/vertical-slice.md`。

不要在本章扩展以下功能：

- 修改和删除订阅。
- 搜索、筛选和统计。
- CSV 导入导出。
- 用户认证。
- 自动提醒。
- 数据库迁移工具。

这些功能应当在后续章节以独立任务出现。

## 12. 参考资料

- FastAPI：Static Files，https://fastapi.tiangolo.com/tutorial/static-files/
- FastAPI：Dependencies，https://fastapi.tiangolo.com/tutorial/dependencies/
- Python 标准库：sqlite3，https://docs.python.org/3/library/sqlite3.html
- Pydantic：Validators，https://docs.pydantic.dev/latest/concepts/validators/
- MDN：Using Fetch，https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
