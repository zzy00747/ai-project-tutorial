# 附录 A　开发环境与故障速查

> 目标：在 Windows 上跑通教程项目，并能处理 macOS/Linux 的必要差异。不要把“安装成功”当成“项目可运行”；最后用干净环境验收。

## A.1 准备清单

| 工具 | 用途 | 检查命令 |
|---|---|---|
| Git | 保存、比较和恢复变更 | `git --version` |
| Python 3.12+ | 运行 Subscription Tracker | `python --version` |
| 编辑器 | 阅读代码与文档，例如 VS Code | 在编辑器中打开项目根目录 |
| GitHub 账号 | PR、Actions、发布；仅本地练习时可暂不使用 | 不输出或提交账号令牌 |

建议使用不含空格的项目路径，例如：

```text
D:\projects\subscription-tracker
```

如果 `python` 指向非预期版本，Windows 可检查 `py -0p`，macOS/Linux 通常使用 `python3`。后续命令应始终使用当前虚拟环境中的 Python。

## A.2 Windows 主路径

在项目根目录打开 **PowerShell**：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
python -m ruff check .
python -m uvicorn app.main:app --reload
```

激活后，提示符通常出现 `(.venv)`。无论是否激活，都可以显式使用虚拟环境解释器：

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

如果 PowerShell 阻止激活脚本，优先使用上面的显式解释器方式；这不会修改本机执行策略。

打开另一个 PowerShell 窗口验证服务：

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

通过标准：命令成功返回健康检查响应；具体字段以项目实现为准，不预先编造输出。

## A.3 macOS/Linux 差异

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
python -m ruff check .
python -m uvicorn app.main:app --reload
```

另一个终端可执行：

```bash
curl --fail http://127.0.0.1:8000/health
```

| 事项 | Windows PowerShell | macOS/Linux |
|---|---|---|
| 创建虚拟环境 | `python -m venv .venv` | `python3 -m venv .venv` |
| 激活 | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| 显式解释器 | `.\.venv\Scripts\python.exe` | `./.venv/bin/python` |
| 查看环境变量 | `$env:NAME` | `printenv NAME` |
| 当前目录文件 | `Get-ChildItem` | `ls` |

Python、pytest、Ruff 和 Git 的主要命令保持一致；教程正文不把两套 shell 命令混在同一个代码块中。

## A.4 本地配置文件

`.gitignore` 至少应考虑：

```gitignore
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.env
*.db-wal
*.db-shm
```

数据库文件是否入库由项目决定：演示用空库可以入库，含个人数据的 SQLite 文件不应入库。`.env` 只保存本地配置，另外提供不含秘密的 `.env.example`。

最小 `.env.example` 结构：

```dotenv
APP_ENV=development
DATABASE_PATH=./data/subscriptions.db
```

具体变量名必须与项目代码一致；不要添加代码未读取的配置项。

## A.5 故障速查

| 症状 | 优先检查 | 恢复动作 |
|---|---|---|
| `'python' 不是内部或外部命令` | Python 是否安装、终端是否重开 | 安装 Python 后重开终端；Windows 尝试 `py --version` |
| Python 版本不符合要求 | `python --version`、`py -0p` | 用指定版本重新创建 `.venv`，不要混用全局包 |
| 虚拟环境激活被拒绝 | 是否只是脚本策略限制 | 使用 `.\.venv\Scripts\python.exe -m ...` |
| `No module named pip` | 当前解释器是否来自 `.venv` | 用当前 Python 执行 `python -m ensurepip --upgrade`，再检查环境 |
| 安装依赖超时或连接失败 | 网络、代理、镜像是否可达 | 保留完整错误；恢复网络后在同一虚拟环境重试，不随意安装替代包 |
| macOS/Linux 出现 `externally-managed-environment` | 是否向系统 Python 全局安装 | 创建并激活 `.venv`，所有依赖装入虚拟环境 |
| `uvicorn` 找不到 | 是否激活了创建项目时的环境 | 使用 `python -m uvicorn ...`；检查依赖是否装进当前环境 |
| `ModuleNotFoundError: app` | 当前目录是否为项目根目录、`app/__init__.py` 是否存在 | 回到含 `app/` 与 `requirements.txt` 的目录再运行 |
| 端口已被占用 | 另一个服务是否正在使用 8000 | 停止旧进程，或改用 `--port 8001` 并同步访问地址 |
| 浏览器无法连接 | 服务是否仍在运行、地址是否为 `127.0.0.1` | 查看启动日志；重新启动并检查 `/health` |
| 页面打开但 API 返回 404 | 路由路径是否为 `/api/subscriptions` | 对照实际路由和 API 文档，不让 AI 凭猜测修改 |
| pytest 收集到 0 项 | 是否在项目根目录、测试文件是否以 `test_` 开头 | 运行 `python -m pytest --collect-only -q`，修正命名或路径 |
| 测试导入失败 | 当前解释器、根目录、包结构 | 使用 `python -m pytest`，不要直接运行另一个环境的 `pytest` |
| Ruff 报错很多 | 是否包含虚拟环境或生成目录 | 检查配置和排除目录；只修复本项目代码，不格式化 `.venv` |
| `git` 提示不是仓库 | 当前目录是否含 `.git` | 进入正确项目根目录；未初始化时先确认目录再执行 `git init` |
| 干净克隆后启动失败 | 必要文件是否未提交、文档是否漏步骤 | 比较 `git status` 与文档，补充启动脚本或说明，再重新验证 |

## A.6 收集一份可定位的故障记录

向 AI 或其他协作者求助时，至少提供：

```text
操作系统：
项目版本或 commit：
当前目录：
使用的完整命令：
完整错误文本：
预期结果：
实际结果：
最近一次正常工作的版本：
已经尝试过的恢复动作：
```

不要只发“跑不起来”，也不要为了省事隐去关键错误行。令牌、密码和个人数据应脱敏。

## A.7 干净环境验收

在项目目录之外重新克隆到临时目录，使用新的虚拟环境：

```powershell
git clone <REPOSITORY_URL> subscription-tracker-clean
Set-Location subscription-tracker-clean
git switch --detach <RELEASE_TAG_OR_COMMIT>
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m ruff check .
```

通过标准：

- 不依赖原目录中的未提交文件。
- 安装、测试和静态检查可重复执行。
- README 中的启动步骤与实际项目一致。
- 服务启动后能访问 `/health`。
- 失败时保留命令和日志，修复文档或项目后从头复验。

## A.8 官方资料

- Python 虚拟环境：https://docs.python.org/3/library/venv.html
- pip 使用说明：https://pip.pypa.io/en/stable/
- Git 文档：https://git-scm.com/docs
- FastAPI 教程：https://fastapi.tiangolo.com/tutorial/
- pytest 使用说明：https://docs.pytest.org/en/stable/how-to/usage.html
- Ruff 使用说明：https://docs.astral.sh/ruff/
