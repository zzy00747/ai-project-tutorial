# 第 9 章　测试与调试：让“AI 说完成”变成可验证事实

> 本章成果：为订阅管理器建立 pytest 测试套件，掌握“先复现、再定位、修复带回归测试”的系统化调试循环，并植入一个 Bug 交给 AI 复现修复。

## 1. 本章成果

1. 项目拥有单元测试与接口测试，覆盖核心 API 的正常/边界/异常路径。
2. 你能判断一条测试是“真断言业务行为”还是“假绿”。
3. 你完成一次完整的调试循环：复现 → 缩小范围 → 定位根因 → 回归测试 → 修复。
4. Lint 与类型检查接入日常验证，形成独立的验证视角。

## 2. 为什么需要它

AI 生成的代码在“演示路径”上几乎总能工作，问题藏在边界与异常里：金额为负、日期非法、特殊字符、空列表。没有测试时，这些路径的回归是静默的——第 12 章将看到 CSV 特殊字符 Bug 就是这么进来的。测试的另一价值是给 AI 一个“客观裁判”：后续每次改动跑 `pytest -q`，红绿是机器判的，不由实现者（包括 AI）自己宣布。调试能力同样关键：AI 擅长修“被明确描述的问题”，而“从现象定位根因”的缩小范围过程需要人引导。本章教的正是这个引导方法。

## 3. 最少必备知识

- **测试金字塔（最小版）**：单元测试测函数（repository）；接口测试测 API（TestClient）；端到端测真实流程（手工/脚本）。本章聚焦前两层。
- **有效断言**：测试必须断言“业务结果”（状态码、字段值、列表顺序），而不是只断言“没抛异常”。
- **假绿**：测试通过但没验证任何东西——常见于 mock 掉了被测行为本身。
- **回归测试**：为每个修过的 Bug 写一条“防复活”用例；先红后绿。
- **AAA 结构**：Arrange（准备）→ Act（执行）→ Assert（断言）。
- **独立验证**：修复由 A 生成，验证视角应独立（不同会话/AI 角色/人工）。
- **Ruff**：风格与常见错误的静态检查，CI 门禁之一。

## 4. 起始项目状态

v0.2：CRUD 与校验可用，提交历史清晰。`tests/` 目录存在但几乎为空；依赖含 pytest 与 ruff（若未安装：`pip install pytest ruff` 并写入 requirements.txt）。

## 5. 操作步骤与 AI 任务示例

### 步骤 1：让 AI 生成测试初稿，你负责挑刺

**给 AI 的任务示例（text 块）**：

```text
目标：为 app/repository.py 的增删改查与 app/routes.py 的 API 编写 pytest 测试。
上下文：FastAPI + SQLite；规格见 specs/subscription-manager/spec.md（验收场景 A—E 与规则 R1—R4 为准）。
范围：只新增 tests/test_repository.py 与 tests/test_api.py；不修改应用代码。
约束：
  1. 数据库用临时文件或内存库，测试间互不影响；
  2. 每条测试 AAA 结构清晰，命名 test_<行为>_<条件>_<期望>；
  3. 覆盖：正常添加、非法金额 422、非法日期 422、删除后 404、到期过滤 due_within；
  4. 断言业务结果（状态码+字段值），禁止“只断言不抛异常”的假绿；
  5. 禁止 mock 掉被测的 repository 行为。
验收：python -m pytest -q 全绿；每条测试能对应到规格场景编号。
输出：两个完整测试文件 + 场景覆盖对照表。
```

拿到初稿后逐条抽查：把某条断言删掉测试还绿吗？绿=假绿，要求重写。

### 步骤 2：运行与修正

```powershell
python -m pytest -q
python -m pytest tests/test_api.py -q        # 只跑接口层
python -m pytest -q -k "invalid_amount"      # 按名过滤
```

常见修正点：测试没清库导致顺序依赖；日期用了“今天”导致次日运行结果变化（固定一个基准日期）；异步客户端用法错误。

### 步骤 3：植入 Bug——调试循环演练

在 `app/repository.py` 的查询函数里故意把排序字段写错（如按 `name` 排序而非 `renewal_date`），然后让另一个 AI 会话（不带你的记忆）来修：

**给新会话 AI 的任务示例（text 块）**：

```text
目标：诊断并修复“到期提醒列表顺序不对”的 Bug。
上下文：FastAPI + SQLite 项目；现象：GET /api/subscriptions?due_within=7 返回的顺序与 renewal_date 无关。
约束：
  1. 先复现：给出复现命令与最小数据集；
  2. 先写一条失败的回归测试（红），再修复实现让它变绿；
  3. 修复范围仅限 app/repository.py；不改 API 契约；不改无关文件；
  4. 不猜测原因，每一步结论给出证据（命令输出/代码行）。
验收：回归测试先红后绿；pytest 全绿；排序按 renewal_date 升序。
输出：诊断时间线 → 根因 → 修复 Diff → 验证命令与结果。
```

观察它是否真的先复现再改；跳过复现直接改的，打回重做。

### 步骤 4：边界与异常补测

按规格边界表补齐：空列表返回 `[]`、名称 100 字上限、`renewal_date` 早于当天 1 年的警告场景、`due_within=0`。每条都是 AI 初稿最爱漏的。

### 步骤 5：Lint 接入

```powershell
python -m ruff check .
python -m ruff check . --fix    # 自动修可修项
```

把 ruff 对未使用导入、未定义名的报错理解为“AI 生成代码的低级病灶探测器”——它比人工扫描快且不遗漏。

### 步骤 6：验证视角分离约定

写进 `AGENTS.md`（第 10 章正式成型，本章先落地规则）：**实现与验证不得由同一会话宣布完成。** 修复完成后，由新会话执行 `pytest -q` 与验收 curl，把输出贴回，才算关闭。

## 6. AI 应生成的产物

1. `tests/test_repository.py`、`tests/test_api.py`（含场景覆盖对照表）。
2. Bug 修复：回归测试（先红）+ 修复 Diff + 验证输出。
3. ruff 清零后的代码调整。

**人工检查物**：假绿抽查结果、边界补测清单、回归测试的“先红”证据（第一次运行输出）。

## 7. 人工检查点

1. 随机挑 2 条测试，删掉核心断言看是否仍绿——绿即假绿，重写。
2. 回归测试是否真的先红？（把修复回退，测试应失败）
3. 测试是否依赖执行顺序或“今天”这类漂移日期？
4. 修复 Diff 是否只有 repository？（越界即恢复）
5. ruff 报错是否被“忽略注释”压掉而不是真修？（`# noqa` 需逐个说理）

## 8. 验收命令与通过标准

```powershell
python -m pytest -q          # 全绿，数量 ≥ 15
python -m ruff check .       # 0 错误
curl http://127.0.0.1:8000/api/subscriptions?due_within=7   # 手工复核排序
```

通过标准：命令真实执行；你能指出任意一条测试对应规格的哪个场景；回归测试有先红证据。

## 9. 常见失败及恢复方法

**症状 1：测试单独跑绿、全量跑红。**
原因：测试间共享状态（同一 DB 文件/模块级变量）。
恢复：每条测试用 fixture 重建临时库；禁止模块级共享连接。要求 AI 修正后重跑全量。

**症状 2：AI 写的测试全是 happy path。**
原因：初稿任务未显式列边界。
恢复：按规格边界表逐条点名补测（空值/上限/非法格式/特殊字符），这些路径现在漏一条，将来就是一条线上 Bug。

**症状 3：AI 直接改测试让失败的实现变绿。**
原因：把“让测试通过”理解成目标本身。
恢复：先确认测试断言符合规格——测试对就改实现，测试错就改测试并说明规格依据；两者都不许静默对齐。

**症状 4：mock 泛滥导致假绿。**
原因：AI 习惯性把依赖 mock 掉。
恢复：约束“禁止 mock repository 层”；接口测试用真实临时库跑通；只有外部服务（如未来加的通知）才允许 mock。

**症状 5：日期相关测试今天跑绿明天跑红。**
原因：依赖系统当前日期。
恢复：测试内固定基准日期（freezegun 或注入 today 参数）；到期窗口计算参数化，便于测试注入。

## 10. 本章 Git 提交

```text
分支：feat/tests-and-debugging
test: add repository unit tests covering r1-r4 rules
test: add api tests for scenarios a-e
fix: order due reminders by renewal_date (regression test included)
chore: fix ruff findings across app package
合并回 main；如接近发布，可提前打 tag：v0.3-rc
```

## 11. 练习与扩展

1. 给一条现有测试故意注入“假绿”改法，再让你的 AI 会话审查找出它——训练审查能力。
2. 用 `pytest -q --tb=short` 体验失败输出的阅读技巧，把最长的一次失败输出交给 AI 解释根因。
3. （进阶）了解变异测试思想（mutmut），抽一个函数做小实验：变异存活说明测试有缺口。
4. 把本章的“验证视角分离”写进你的 `AGENTS.md` 草稿。

## 12. 参考资料

- pytest 官方文档：https://docs.pytest.org/
- Martin Fowler：TDD inside the agent loop（agent 循环中 TDD 的价值评估）：https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
- Ruff 官方文档：https://docs.astral.sh/ruff/
- obra/superpowers（TDD 与 systematic-debugging 技能实践）：https://github.com/obra/superpowers
- ChiYu 铁人赛 Day 15（Gemini CLI 辅助撰写 Pytest，中文同型实践）：https://huangchiyu.com/ChiYu-Blog/posts/2025ithomeironmanday15/
