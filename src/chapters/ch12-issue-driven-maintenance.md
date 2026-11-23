# 第 12 章　Issue 驱动维护：从问题报告到修复 PR

> 本章成果：把一个真实的 CSV 导出 Bug 从模糊反馈整理成高质量 Issue，先复现并写出回归测试，再用受控的 AI 修改完成小型修复 PR。

## 1. 本章成果

完成本章后，你应该得到：

1. 一份可复制、可验收的 Issue 文档。
2. 一个在修复前失败、修复后通过的回归测试。
3. 一个只修改 CSV 导出行为的小型 PR 或分支。
4. 一套“基线测试 → 失败测试 → 窄范围修改 → 重新验证 → Diff 审查”的 Aider 式闭环。
5. 一条经验：AI 说“已经修复”不能作为验收依据，可重复运行的测试和最小 Diff 才是依据。

本章不新增业务功能，只修复已有功能。项目从 `v1.0` 继续演化，而不是重新生成一个新项目。

## 2. 为什么需要它

项目发布以后，第一类维护工作通常不是大重构，而是处理具体问题：

- 用户导出的 CSV 在 Excel 或文本编辑器里错位。
- 某个包含逗号的订阅名称把一行拆成多列。
- 备注里的换行导致下一行记录被破坏。

如果直接把“CSV 导出有问题”丢给 AI，它可能修改导出路径、重写整个表格页面、升级依赖，甚至改变数据模型。维护阶段最重要的控制点是：

```text
问题是否可复现
→ 预期行为是否明确
→ 失败测试是否能证明问题
→ 修改范围是否足够小
→ 原有用例是否仍然通过
```

这正是 Issue 驱动维护的价值：先把模糊反馈变成项目资产，再让 AI 在一个受约束的范围内完成修改。

## 3. 最少必备知识

1. **Issue**：描述现象、复现步骤、预期结果、实际结果和验收标准的文档，不是情绪化投诉。
2. **回归测试**：专门证明某个 Bug 曾经存在、修复后不再复发的测试。
3. **最小可复现案例**：只保留触发问题所需的数据、输入和操作。
4. **Diff**：代码修改前后的差异，是人工审查 AI 工作的主要对象。
5. **CSV 转义**：字段中包含逗号、双引号或换行时，不能手工拼接文本，需要使用标准 CSV 序列化规则。

Python 的 `csv` 模块会自动处理字段转义。本章的问题就是导出实现绕过了它。

## 4. 起始项目状态

从 `v1.0` 的稳定状态开始。确保工作区干净，并且当前分支就是项目主线：

```powershell
git status
git log --oneline -5
git tag --list
git switch main
```

如果没有 `v1.0` 标签，使用第 11 章发布时记录的提交。创建修复分支：

```powershell
git switch -c fix/csv-special-characters
```

先运行基线检查：

```powershell
python -m pytest -q
python -m ruff check .
```

记录基线状态。如果主线原本就有失败测试，先处理主线问题，不要在 Bug 修复分支里顺手修改无关代码。

本章假设当前 CSV 导出接口为：

```text
GET /api/subscriptions/export
```

如果你的项目使用了不同路径，请替换为实际的导出接口，但不要把路径调整和功能修复合并到同一个 PR。

## 5. 操作步骤与 AI 任务示例

### 5.1 复现问题

在浏览器或终端中导出一份 CSV。PowerShell 示例：

```powershell
python -m uvicorn app.main:app --reload
```

服务启动后，在另一个终端执行：

```powershell
Invoke-WebRequest "http://127.0.0.1:8000/api/subscriptions/export" -OutFile subscriptions.csv
```

用文本编辑器打开 `subscriptions.csv`。如果某条记录的 `name` 或 `note` 包含 ASCII 逗号、双引号或换行，检查是否出现以下现象：

- 一条记录被拆成多行。
- 一行列数明显多于表头。
- 引号没有按 CSV 规则成对转义。
- 使用标准 CSV 解析器读取时字段内容发生变化。

### 5.2 编写高质量 Issue

在 `docs/runbooks/issue-001-csv-special-characters.md` 中记录问题。这个文件是项目维护证据，不是临时聊天记录。

```markdown
# Issue 001：CSV 导出未正确转义逗号、双引号和换行

- 影响版本：v1.0
- 影响接口：GET /api/subscriptions/export
- 严重程度：高，影响数据导出正确性
- 是否阻断使用：否，但导出数据不可信

## 复现数据

创建一条订阅记录：

- name：`VPN, "Team"`
- amount：`1299`
- currency：`USD`
- renewal_date：`2026-12-05`
- note：
  ```text
  first line
  second line, with "quote"
  ```

## 复现步骤

1. 启动应用。
2. 创建上述记录。
3. 访问 CSV 导出接口。
4. 使用标准 CSV 解析器读取导出内容。

## 预期结果

解析结果仍然只包含一条订阅记录，并且 `name` 与 `note` 的原始内容完整保留。

## 实际结果

字段中的逗号、双引号或换行破坏 CSV 行与列边界，标准解析器无法还原原始记录。

## 验收标准

1. 导出内容可以通过 `csv.DictReader` 正确解析。
2. 特殊字符字段往返后保持原值。
3. CSV 表头仍为 `id,name,amount,currency,renewal_date,note,created_at`。
4. 现有测试、Lint 和手工导出检查全部通过。
5. 修改范围限于 CSV 导出实现与对应测试。
```

### 5.3 先写失败测试

在 `tests/test_api.py` 中新增回归测试。不要先让 AI 修改实现，否则无法确认测试真的能发现问题。

```python
import csv
import io

CSV_HEADER = [
    "id",
    "name",
    "amount",
    "currency",
    "renewal_date",
    "note",
    "created_at",
]


def test_csv_export_preserves_special_characters(client):
    payload = {
        "name": 'VPN, "Team"',
        "amount": 1299,
        "currency": "USD",
        "renewal_date": "2026-12-05",
        "note": 'first line\nsecond line, with "quote"',
    }

    created_response = client.post("/api/subscriptions", json=payload)
    assert created_response.status_code in (200, 201)
    created = created_response.json()

    response = client.get("/api/subscriptions/export")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")

    reader = csv.DictReader(io.StringIO(response.text))
    assert reader.fieldnames == CSV_HEADER

    rows = [row for row in reader if row["id"] == str(created["id"])]
    assert len(rows) == 1

    row = rows[0]
    assert row["name"] == payload["name"]
    assert row["note"] == payload["note"]
    assert row["amount"] == str(payload["amount"])
    assert row["currency"] == payload["currency"]
    assert row["renewal_date"] == payload["renewal_date"]
    assert None not in row
```

运行：

```powershell
python -m pytest -q tests/test_api.py -k csv
```

这个测试必须先失败。如果它一开始就通过，说明测试没有复现真实问题，或者当前项目已经使用了标准 CSV 序列化。此时不要继续修改实现，先检查测试数据和导出路径。

### 5.4 给 AI 的窄范围任务

使用以下任务示例。重点是限定文件、禁止扩大范围，并要求 AI 报告假设。

```text
目标：修复 CSV 导出中逗号、双引号和换行破坏行与列边界的问题。

上下文：
- 项目：Subscription Tracker。
- 技术栈：Python 3.12+、FastAPI、SQLite、pytest、Ruff。
- 当前导出接口：GET /api/subscriptions/export。
- 订阅字段固定为 id、name、amount、currency、renewal_date、note、created_at。
- amount 使用整数分。
- tests/test_api.py 中已新增 test_csv_export_preserves_special_characters，当前应失败。

范围：
1. tests/test_api.py 中新增的回归测试。
2. 现有 CSV 导出实现所在文件。
3. 如果无法确定导出实现位置，先报告候选文件和函数，不要猜测修改。

约束：
1. 先运行 python -m pytest -q 获取基线。
2. 使用 Python csv 模块序列化，不手工拼接逗号。
3. 不修改数据库 schema、订阅字段、认证、部署配置或无关前端样式。
4. 不升级依赖。
5. 不改变导出 URL、响应状态码和 CSV 表头顺序。
6. 一次只完成 CSV 特殊字符修复。

验收：
1. python -m pytest -q tests/test_api.py -k csv 通过。
2. python -m pytest -q 全部通过。
3. python -m ruff check . 通过。
4. git diff 只包含 CSV 导出实现与回归测试相关修改。
5. 导出内容可以用 csv.DictReader 还原特殊字符字段。

输出：
1. 修改文件列表。
2. 关键 Diff 说明。
3. 实际运行的命令。
4. 无法确认的假设。
```

### 5.5 参考修复

以下代码为示意，实际函数名、路由对象和依赖注入方式应与当前项目保持一致。

```python
import csv
import io

from fastapi.responses import Response

CSV_FIELDNAMES = [
    "id",
    "name",
    "amount",
    "currency",
    "renewal_date",
    "note",
    "created_at",
]


def subscriptions_to_csv(subscriptions: list[dict]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=CSV_FIELDNAMES,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(subscriptions)
    return output.getvalue()


@router.get("/api/subscriptions/export")
def export_subscriptions():
    subscriptions = list_subscriptions()
    content = subscriptions_to_csv(subscriptions)
    return Response(
        content=content,
        media_type="text/csv; charset=utf-8",
        headers={
            "Content-Disposition": 'attachment; filename="subscriptions.csv"'
        },
    )
```

如果当前 `list_subscriptions()` 返回 Pydantic 对象或 ORM 对象，不要新写一套序列化逻辑；应复用现有 API 已经验证过的字段转换方式，把对象转换为包含上述七个键的字典后再交给 `csv.DictWriter`。

### 5.6 Aider 式 Git 与测试闭环

即使不使用 Aider，也建议按它的反馈方式组织工作：

1. 在干净分支上运行完整基线测试。
2. 只把相关文件交给 AI，例如 `app/routes.py` 和 `tests/test_api.py`。
3. 先得到失败测试，再得到实现修改。
4. 每次修改后立即运行测试。
5. 测试失败时，把完整错误输出交给同一个窄范围任务继续修复。
6. 测试通过后检查 Diff，而不是只看 AI 的总结。

如果你已经安装 Aider，可以使用类似命令：

```powershell
aider app/routes.py tests/test_api.py --test-cmd "python -m pytest -q" --auto-test
```

没有 Aider 时，用普通编码代理重复同样闭环即可。工具不是重点，重点是每次 AI 修改都经过测试和 Git 边界约束。

## 6. AI 应生成的产物

本章期望 AI 产出：

1. 修改文件列表，通常应只有导出实现文件和测试文件。
2. 使用 `csv.DictWriter` 或等价标准 CSV 序列化的实现。
3. 回归测试，且测试通过标准 CSV 解析器验证结果，而不是检查字符串里是否包含逗号。
4. 实际执行的命令清单。
5. 对不确定之处的明确说明，例如导出函数位置、现有响应头或对象序列化方式。

AI 不应该产出：

- 新页面或新组件。
- 数据库字段变更。
- 依赖升级。
- 与 CSV 无关的格式化修改。
- “我已经全面检查了项目”这类没有命令或测试支撑的结论。

## 7. 人工检查点

逐项检查：

1. **测试是否先失败过**：如果从未看到失败，不能证明它覆盖了 Bug。
2. **测试是否真的解析 CSV**：应使用 `csv.DictReader`，而不是人工数字段或查找子字符串。
3. **修改是否使用标准库**：`csv` 模块负责转义，手工 `replace('"', '""')` 容易漏掉换行和边界情况。
4. **表头是否未变**：字段顺序和名称是外部契约。
5. **响应类型是否未变**：仍应返回 CSV 文件和下载头。
6. **Diff 是否足够小**：运行 `git diff --stat`，确认没有顺带修改无关文件。
7. **是否存在隐藏格式化**：运行 `git diff --check`，检查尾随空格和冲突标记。
8. **假设是否被记录**：如果 AI 无法确定现有函数名，应报告而不是猜。

## 8. 验收命令与通过标准

```powershell
python -m pytest -q tests/test_api.py -k csv
python -m pytest -q
python -m ruff check .
git diff --stat
git diff --check
```

通过标准：

1. CSV 回归测试通过。
2. 完整测试套件通过。
3. Ruff 没有新增错误。
4. Diff 只包含 CSV 修复相关文件。
5. `git diff --check` 没有空白或冲突标记问题。

手工验收：

```powershell
Invoke-WebRequest "http://127.0.0.1:8000/api/subscriptions/export" -OutFile subscriptions-after-fix.csv
```

打开文件并确认包含逗号、引号和换行的记录不再破坏行列结构。不要在正文中写“测试全部通过，耗时 X 秒”之类未经实际运行的结果；你自己的命令输出才是验收证据。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| 新测试一开始就通过 | 测试没有覆盖特殊字符，或访问了错误导出路径 | 检查 payload、接口 URL 和响应内容；先确认手工导出仍能复现问题 |
| 测试失败，但错误是 `404` | 导出路由未注册，或被 `/api/subscriptions/{id}` 之类路径提前匹配 | 查看路由定义顺序和实际 URL；先恢复正确路由，再处理转义问题 |
| AI 修改了多个无关文件 | 任务范围太宽，或让 AI “顺便优化项目” | 放弃当前修改，重新从干净基线开始，只提供导出实现和测试文件 |
| CSV 在 Python 测试中通过，但 Excel 显示异常 | 编码、换行或 BOM 属于另一个问题 | 单独记录新 Issue；不要把它塞进当前转义修复 PR |
| 测试通过后手工导出仍异常 | 测试访问的实现与浏览器实际调用的接口不同 | 比较 URL、响应头和路由函数；必要时补充端到端测试 |

## 10. 本章 Git 提交

建议分支：

```text
fix/csv-special-characters
```

建议提交拆分：

```text
docs: add CSV special-character issue and acceptance criteria
fix: preserve CSV fields containing commas, quotes and newlines
```

第二个提交应同时包含回归测试和实现修复。这样可以避免主线出现“测试已知失败”的中间提交。如果团队约定允许失败测试先行，也可以拆成 `test:` 与 `fix:` 两个提交，但合并前应确保最终提交通过 CI。

提交前检查：

```powershell
git status
git diff --stat
git diff
```

不要使用 `git add .` 一次性提交所有文件，除非你确认工作区没有无关修改。

## 11. 练习与扩展

1. 增加 `note` 为空字符串和 `None` 两种情况的导出测试。
2. 增加包含全角逗号、中文引号和 Emoji 的记录，确认它们不被误当作分隔符。
3. 增加 CRLF 换行的备注，确认导出仍能正确解析。
4. 编写一个小型往返测试：创建记录 → 导出 CSV → 解析 CSV → 与 API 返回的原始记录比较。
5. 把本章 Issue 模板放入 `docs/runbooks/`，后续每个维护问题都先填写同样字段。

## 12. 参考资料

1. Python 官方文档：[csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
2. FastAPI 官方文档：[Testing](https://fastapi.tiangolo.com/tutorial/testing/)
3. Aider 官方文档：[Linting and Testing](https://aider.chat/docs/usage/lint-test.html)
4. GitHub Docs：[Get the best results from the Copilot coding agent](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results)
