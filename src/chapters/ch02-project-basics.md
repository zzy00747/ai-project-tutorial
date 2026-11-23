# 第 2 章　零基础必备：看懂项目、运行项目和阅读报错

> 本章成果：在本地建立 Subscription Tracker 的最小运行环境，启动一个 FastAPI 健康检查接口，并学会把报错整理成 AI 能有效处理的问题报告。

## 1. 本章成果

完成本章后，你应拥有一个可以本地运行的最小项目骨架：

```text
subscription-tracker/
├─ app/
│  ├─ __init__.py
│  └─ main.py
├─ docs/
│  └─ environment-check.md
├─ requirements.txt
└─ .venv/
```

你将完成以下事情：

- 检查或安装 Python
- 创建项目专属虚拟环境 `.venv`
- 安装 FastAPI 和 Uvicorn
- 启动本地服务
- 访问 `/health` 并看到 JSON 响应
- 故意制造一次错误，让 AI 协助诊断
- 把环境状态和报错处理过程记录到 `docs/environment-check.md`

本章的 `/health` 不是订阅管理器的业务功能，只是环境冒烟检查。它证明“这个项目能在你的电脑上启动”，后续章节会在此基础上加入数据库、页面、测试和订阅记录。

## 2. 为什么需要它

AI 编程教程里最常见的挫折不是模型不会写代码，而是读者无法判断代码为什么跑不起来。依赖装错位置、Python 版本不一致、端口被占用、虚拟环境没有激活、路径里有特殊字符，都会让看似正确的代码失败。

如果你不能区分下面几类问题，就很难有效使用 AI：

- **环境问题：** Python、依赖、虚拟环境、端口、权限。
- **代码问题：** 导入错误、语法错误、接口路径不存在、业务逻辑错误。
- **运行问题：** 服务没有启动、浏览器访问了错误 URL、请求参数不符合接口约定。
- **验收问题：** 程序启动了，但没有证据证明它满足需求。

本章会建立一个很小的可运行基线。后面每当你让 AI 修改项目，都应该先确认“修改前能运行，修改后也能运行”。没有这个基线，AI 的每次输出都会变成无法判断真假的猜测。

## 3. 最少必备知识

- **终端：** 输入命令的窗口。Windows 可用 PowerShell，macOS/Linux 可用 Terminal。
- **当前目录：** 命令默认作用于终端所在目录。多数错误来自“在错误目录执行命令”。
- **Python 解释器：** 运行 Python 程序的程序。不同项目可以使用不同解释器。
- **虚拟环境 `.venv`：** 项目专属的依赖目录，避免不同项目的包互相污染。
- **包与模块：** `pip install fastapi` 安装包；Python 代码通过 `import fastapi` 使用模块。
- **HTTP 请求与响应：** 浏览器或命令访问 URL，服务器返回状态码和 JSON 等数据。
- **端口：** 本地服务通过端口区分，例如 `127.0.0.1:8000`。
- **堆栈跟踪：** Python 报错中从上到下的调用过程，通常最后几行包含真正关键的错误类型和位置。

你不需要一开始理解 FastAPI 的全部机制。本章只要求你能创建文件、安装依赖、启动服务，并准确描述看到的现象。

## 4. 起始项目状态

本章从空目录开始，不依赖第 1 章的一次性原型，也不依赖任何配套仓库。

如果你已经完成第 1 章，请把正式项目创建在另一个目录：

```text
subscription-tracker/
```

不要继续使用：

```text
subscription-tracker-prototype/
```

本章完成后，项目应包含：

```text
subscription-tracker/
├─ app/
│  ├─ __init__.py
│  └─ main.py
├─ docs/
│  └─ environment-check.md
└─ requirements.txt
```

`.venv/` 会在创建虚拟环境后出现。它是依赖目录，不应该手动编辑，也不应该作为项目成果逐行阅读。

## 5. 操作步骤与 AI 任务示例

### 5.1 检查 Python

Windows PowerShell：

```powershell
python --version
```

如果提示找不到 `python`，尝试：

```powershell
py --version
py -3 --version
```

macOS/Linux：

```bash
python3 --version
```

本教程默认 Python 3.12 或更新版本。如果版本过低或未安装，请从 Python 官方站点安装适合你操作系统的版本。安装后关闭并重新打开终端，再次检查版本。

### 5.2 创建项目目录

```powershell
mkdir subscription-tracker
cd subscription-tracker
mkdir app
mkdir docs
```

Windows、macOS 和 Linux 的上述命令基本一致。

### 5.3 创建并激活虚拟环境

Windows PowerShell：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

激活成功后，PowerShell 提示符前通常会出现 `(.venv)`。这只是视觉提示，后续仍会用命令验证实际解释器路径。

如果 Windows 拒绝执行激活脚本，不要立刻修改系统安全策略。可以改用虚拟环境中的 Python 可执行文件：

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

### 5.4 创建依赖文件

在项目根目录创建 `requirements.txt`，写入：

```text
fastapi
uvicorn[standard]
```

本章暂时不固定版本号，避免教程写作时的版本很快过期。后续章节会介绍锁文件和依赖升级策略。

安装依赖：

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

macOS/Linux 中，如果 `python` 指向系统 Python，请使用：

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 5.5 创建最小应用

创建空文件：

```text
app/__init__.py
```

它的作用是让 Python 将 `app` 视为包。文件可以为空。

创建 `app/main.py`：

```python
from fastapi import FastAPI

app = FastAPI(title="Subscription Tracker")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
```

这段代码只做三件事：

1. 创建 FastAPI 应用。
2. 注册 `/health` 路由。
3. 返回一个 JSON 对象。

不要在此阶段添加订阅模型、数据库、页面或认证。项目越小，报错越容易定位。

### 5.6 启动服务

在项目根目录执行：

```powershell
python -m uvicorn app.main:app --reload
```

macOS/Linux 中如需明确使用 Python 3：

```bash
python3 -m uvicorn app.main:app --reload
```

服务启动后，不要关闭这个终端窗口。它会持续运行，直到你按 `Ctrl+C` 停止。

### 5.7 验证健康检查

打开浏览器访问：

```text
http://127.0.0.1:8000/health
```

也可以使用命令验证。

Windows PowerShell：

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

macOS/Linux：

```bash
curl -i http://127.0.0.1:8000/health
```

你应该能看到包含 `"status": "ok"` 的 JSON 响应。具体格式可能因浏览器或命令不同而略有差异。

如果你访问：

```text
http://127.0.0.1:8000/
```

看到 404 是正常的，因为本章只定义了 `/health`，没有定义根路径。

### 5.8 制造并诊断一次真实报错

为了练习阅读错误，我们故意修改 `app/main.py`，把导入名称写错：

```python
from fastapi import FastAPI
from app.missing_module import helper  # 故意制造 ModuleNotFoundError

app = FastAPI(title="Subscription Tracker")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
```

重新启动：

```powershell
python -m uvicorn app.main:app --reload
```

终端应出现包含 `ModuleNotFoundError` 的堆栈跟踪。复制完整错误，不要只复制最后一行。

使用以下 AI 任务模板：

```text
目标：
诊断一个 Python/FastAPI 项目启动失败的原因，并给出最小修复方案。

上下文：
这是教程 Subscription Tracker 的环境冒烟检查。项目使用 Python 虚拟环境、FastAPI 和 Uvicorn。当前只应有一个 /health 接口。

范围：
只分析启动失败原因。
只允许建议修改 app/main.py 或依赖安装方式。
不要建议新增业务功能、数据库、前端页面或部署配置。

必须提供的信息：
1. 操作系统和终端类型：[填写]
2. Python 命令：[填写]
3. Python 版本输出：[填写]
4. 当前目录：[填写]
5. 虚拟环境是否激活：[填写]
6. 实际执行命令：[填写]
7. 完整错误输出：
[粘贴完整 traceback]

约束：
- 先解释错误发生在哪里，再给修复步骤。
- 不确定时列出需要补充的信息，不要猜测。
- 不要建议安装与错误无关的全局包。
- 不要修改 .venv 内部文件。
- 修复后应能通过启动命令和 /health 请求验证。
- 不要把“应该已经修复”当作结论，必须给出验证命令。

验收：
1. 指出错误类型和直接原因。
2. 给出最小修复步骤。
3. 给出修复后的验证命令。
4. 说明如何避免同类错误。

输出：
1. 错误解释。
2. 最小修复步骤。
3. 验证命令。
4. 需要我补充的信息（如有）。
```

根据 AI 的解释，删除故意加入的错误导入，恢复原来的 `app/main.py`，再次启动并访问 `/health`。

### 5.9 创建环境检查记录

创建 `docs/environment-check.md`，记录你的实际环境：

```markdown
# 环境检查记录

## 基本信息

- 操作系统：
- 终端：
- Python 命令：
- Python 版本：
- 虚拟环境路径：
- 项目目录：

## 已执行命令

1. 
2. 
3. 

## 验证结果

- `/health` 是否返回 JSON：
- 根路径 `/` 是否返回 404：
- `python -m pip check` 是否通过：
- 是否仍有未解决报错：

## 本次学到的报错类型

- 错误类型：
- 直接原因：
- 修复方式：
- 下次如何避免：
```

这个文件不是装饰品。后续当你更换电脑、重新安装依赖或让 AI 在新会话中接手项目时，它可以帮助快速恢复上下文。

## 6. AI 应生成的产物

本章中，AI 可以协助生成或检查：

- `requirements.txt` 的初始内容
- `app/main.py` 的最小健康检查代码
- 报错解释和最小修复步骤
- `docs/environment-check.md` 的模板

但以下内容必须由你验证并填写：

- Python 版本
- 虚拟环境实际路径
- 依赖安装是否成功
- `/health` 是否真的返回 JSON
- 控制台或终端中的完整错误
- 修复后是否重新启动成功

如果 AI 直接给出一个看似正确的修复，你仍应执行：

```powershell
python -m uvicorn app.main:app --reload
```

并重新访问 `/health`。只有实际运行结果才能证明环境恢复。

## 7. 人工检查点

请逐项检查，而不是只看页面是否打开。

1. **确认当前 Python 来自虚拟环境**

   ```powershell
   python -c "import sys; print(sys.executable)"
   ```

   macOS/Linux：

   ```bash
   python3 -c "import sys; print(sys.executable)"
   ```

   输出路径应位于当前项目的 `.venv` 目录内。

2. **确认依赖安装在当前环境中**

   ```powershell
   python -m pip show fastapi
   python -m pip show uvicorn
   ```

   检查输出中的 `Location` 是否指向 `.venv`。

3. **确认依赖关系没有明显冲突**

   ```powershell
   python -m pip check
   ```

4. **确认启动目录正确**

   启动命令必须在包含 `app/` 和 `requirements.txt` 的项目根目录执行。如果当前目录错误，Python 可能找不到 `app.main:app`。

5. **确认访问的是正确地址**

   本章有效地址是：

   ```text
   http://127.0.0.1:8000/health
   ```

   不是：

   ```text
   http://127.0.0.1:8000/
   ```

6. **确认报错记录完整**

   一份有效报错记录应包含：
   - 操作系统和终端
   - 当前目录
   - Python 版本
   - 实际执行命令
   - 完整 traceback
   - 你已经尝试过的修复
   - 修复后的新结果

7. **确认没有把 AI 解释当成验证**

   AI 可以说“原因是 ModuleNotFoundError”，但你仍要通过重新启动和访问 `/health` 证明问题消失。

## 8. 验收命令与通过标准

在项目根目录执行：

```powershell
python --version
python -c "import sys; print(sys.executable)"
python -m pip check
python -c "import fastapi, uvicorn; print('imports ok')"
python -m uvicorn app.main:app --reload
```

服务启动后，在另一个终端执行：

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

macOS/Linux 可使用：

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
python3 -m pip check
python3 -c "import fastapi, uvicorn; print('imports ok')"
python3 -m uvicorn app.main:app --reload
```

另一个终端：

```bash
curl -i http://127.0.0.1:8000/health
```

通过标准：

1. Python 版本满足教程要求。
2. `sys.executable` 指向当前项目 `.venv` 内的解释器。
3. `python -m pip check` 没有报告依赖冲突。
4. `import fastapi, uvicorn` 成功。
5. Uvicorn 能启动且没有阻塞性 traceback。
6. `/health` 返回包含 `"status": "ok"` 的 JSON。
7. 根路径 `/` 返回 404，并且你能解释这是预期行为。
8. `docs/environment-check.md` 已记录实际命令、结果和一次报错处理过程。

不要伪造输出。如果你暂时无法解决某个错误，也应如实记录当前状态；未解决的环境问题会影响后续所有章节。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| `python` 不是内部或外部命令 | 未安装 Python，或未加入 PATH | Windows 尝试 `py --version`；macOS/Linux 尝试 `python3 --version`；必要时重新安装并重启终端 |
| 激活 `.venv` 时被 PowerShell 阻止 | 当前执行策略禁止运行脚本 | 不修改全局策略；改用 `.venv\Scripts\python.exe -m ...` 直接调用虚拟环境解释器 |
| `ModuleNotFoundError: No module named 'fastapi'` | 依赖安装到了全局 Python，或虚拟环境未激活 | 运行 `python -c "import sys; print(sys.executable)"` 确认解释器；在 `.venv` 中重新执行 `python -m pip install -r requirements.txt` |
| `ModuleNotFoundError: No module named 'app'` 或 `app.main:app` 找不到 | 启动目录不是项目根目录，或缺少 `app/__init__.py` | 回到包含 `app/` 和 `requirements.txt` 的目录；确认 `app/__init__.py` 存在 |
| 端口 8000 已被占用 | 上一次服务未停止，或其他程序使用该端口 | 在原终端按 `Ctrl+C` 停止服务；仍冲突时改用 `--port 8001`，并同步修改验证 URL |
| 访问根路径出现 404 | 当前只注册了 `/health`，没有根路由 | 这是预期结果；访问 `http://127.0.0.1:8000/health`，不要为了消除 404 提前添加业务页面 |
| JSON 中文显示异常或文件乱码 | 文件未以 UTF-8 保存，或终端编码不同 | 用 UTF-8 重新保存 `app/main.py`；本章响应只包含英文 `ok`，可先排除业务中文问题 |
| 修改代码后服务没有变化 | `--reload` 未生效、保存失败或启动了旧目录 | 确认文件已保存；停止服务后在项目根目录重新启动；检查当前目录和 `sys.executable` |

处理环境错误时，优先按以下顺序排查：

```text
当前目录
→ Python 解释器
→ 虚拟环境
→ 依赖安装位置
→ 启动命令
→ 访问 URL
→ 代码本身
```

## 10. 本章 Git 提交

第 3 章会正式初始化 Git。你可以先记住本章的建议提交边界。

建议分支：

```text
chore/project-environment
```

建议提交文件：

```text
requirements.txt
app/__init__.py
app/main.py
docs/environment-check.md
```

不应提交：

```text
.venv/
__pycache__/
*.py[cod]
```

建议提交信息：

```text
chore: add FastAPI health smoke check
```

如果后续你在同一分支修复环境问题，可以追加：

```text
docs: record environment troubleshooting results
```

不要把所有调试过程压成一个“update”提交。环境、依赖、代码和文档最好分开，后续回顾时才能知道每类变更解决了什么问题。

## 11. 练习与扩展

1. **换端口启动。** 使用 `--port 8001` 启动服务，并验证 `http://127.0.0.1:8001/health`。
2. **制造导入错误。** 删除 `app/__init__.py` 后重新启动，记录错误；恢复文件并确认服务正常。
3. **制造路由错误。** 临时把 `@app.get("/health")` 改成 `@app.get("/healthz")`，观察旧 URL 的 404 与新 URL 的成功响应。
4. **生成依赖快照。** 执行 `python -m pip freeze > requirements-lock.txt`，但不要覆盖 `requirements.txt`。思考锁文件与依赖声明文件的区别。
5. **训练报错提问。** 把你遇到过的任意错误整理成第 5.8 节的 AI 任务模板，检查 AI 是否能在不看到完整上下文时给出可靠建议。
6. **关闭网络后重试。** 依赖已安装时，断网启动 `/health` 是否仍可运行？记录结果，并解释本地服务与外部 API 的区别。

## 12. 参考资料

- [Python 官方文档：venv — 创建虚拟环境](https://docs.python.org/zh-cn/3/library/venv.html)
- [FastAPI 官方教程](https://fastapi.tiangolo.com/tutorial/)
- [Uvicorn 官方文档](https://www.uvicorn.org/)
- [Python 官方文档：traceback 模块](https://docs.python.org/zh-cn/3/library/traceback.html)
