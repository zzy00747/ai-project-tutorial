# 第 8 章　AI 实现闭环：小任务、小 Diff、小 PR

> 本章成果：用“一个任务 → 一个 Diff → 一次评审 → 一个提交”的循环完成订阅的修改、删除和输入校验，形成 v0.2。

## 1. 本章成果

1. 你建立了一个可重复的 AI 实现闭环：任务包 → 生成 → Diff 审查 → 运行验证 → 提交。
2. 你能识别 AI 的三类越界：改无关文件、隐性新增功能、重命名既有接口。
3. 项目推进到 v0.2：修改、删除、输入校验三项功能各自独立提交。
4. 你知道什么时候应该停下来重新澄清需求，而不是继续让 AI 生成。

## 2. 为什么需要它

第 7 章打通了纵向切片，本章解决的是“持续开发”的质量问题。AI 一次生成的 Diff 越大，你能审的有效性越低——人面对 500 行 Diff 的真实审查质量趋近于零，只会在“能跑就行”处签字。小步循环的价值正在于此：每次生成控制在几十行内，每一行你都有余力真正读懂。同时，小提交让回滚精确到功能级（校验出问题只回滚校验，不动删除功能），也为第 11 章的 PR 与 CI 流程奠定粒度基础。“AI 说完成”不等于完成——本章把“完成”重新定义为：Diff 审查通过 + 验收命令真实通过。

## 3. 最少必备知识

- **任务包（task brief）**：给 AI 的一次生成指令，含目标/上下文/范围/约束/验收/输出六要素。
- **Diff 审查**：逐块阅读 `git diff`，重点看：范围外文件、签名变更、悄悄的行为变化。
- **无关修改**：AI 顺手做的格式化、重命名、依赖调整——不是 bug，但会污染提交。
- **隐性功能**：AI 为“帮到你”而自行添加的逻辑（如自动补默认值），改变契约且无测试。
- **自审 vs 人工评审**：AI 可以自查代码风格与明显 bug，但“需求是否被正确理解”必须人判断。
- **变更说明**：提交信息里写“为什么改”，Diff 已经写了“改了什么”。

## 4. 起始项目状态

v0.1：添加/查看订阅可用，`app/` 三层结构就位，基线提交与标签存在（第 3 章）。测试尚不完整（第 9 章补齐），本章的验证以运行验收命令为主。

## 5. 操作步骤与 AI 任务示例

### 步骤 1：为每个功能写任务包

先开分支：

```powershell
git switch -c feat/v0.2-crud
```

三个功能 = 三个任务包 = 三个提交。修改功能的任务包示例：

**给 AI 的任务示例（text 块）**：

```text
目标：为订阅记录实现修改功能（PUT /api/subscriptions/{id}）。
上下文：FastAPI 项目；现有代码见 app/routes.py、app/repository.py、app/schemas.py；规格见 specs/subscription-manager/spec.md（字段与校验规则以 spec 为准）。
范围：只允许修改上述三个文件中与本功能直接相关的部分；不得新增依赖；不得改动添加/查询功能。
约束：
  1. 复用 schemas.py 中既有校验（金额正整数、日期 YYYY-MM-DD）；
  2. id 不存在返回 404，校验失败返回 422（错误体含字段级 message）；
  3. 修改成功返回 200 与更新后的完整记录；
  4. 不修改 created_at。
验收：PUT 合法数据返回 200 且字段更新；非法金额返回 422；不存在的 id 返回 404。给出 curl 验证命令。
输出：修改后的完整文件内容 + 每处改动一句话说明。
```

### 步骤 2：生成并做 Diff 审查

```powershell
git diff --stat    # 先看文件数是否与任务范围一致
git diff           # 再逐块读内容
```

审查顺序：先 `--stat`（文件数对不对）→ 再读业务改动 → 最后扫一遍是否有“说不清目的”的改动。发现越界（如它顺手改了 `database.py`）：

```powershell
git restore app/database.py
```

### 步骤 3：运行验证

```powershell
# 启动
python -m uvicorn app.main:app --reload

# 修改成功
curl -X PUT http://127.0.0.1:8000/api/subscriptions/1 -H "Content-Type: application/json" -d "{\"name\":\"网盘会员\",\"amount\":2000,\"currency\":\"CNY\",\"renewal_date\":\"2026-12-15\",\"note\":\"升级版\"}"

# 非法金额 → 期望 422
curl -X PUT http://127.0.0.1:8000/api/subscriptions/1 -H "Content-Type: application/json" -d "{\"amount\":-5}"

# 不存在的 id → 期望 404
curl -X PUT http://127.0.0.1:8000/api/subscriptions/999 -H "Content-Type: application/json" -d "{\"amount\":100}"
```

三条命令的实际状态码与规格一致，功能才算完成。

### 步骤 4：提交（一个功能一条提交）

```powershell
git add app/routes.py app/repository.py app/schemas.py
git commit -m "feat: update subscription via PUT with validation"

# 删除功能重复步骤 1—4
git commit -m "feat: delete subscription via DELETE"

# 校验收紧重复步骤 1—4
git commit -m "feat: tighten input validation for subscription fields"
```

### 步骤 5：AI 自审与人工评审的组合

每个功能提交前，追加一个自审任务：

**给 AI 的任务示例（text 块）**：

```text
目标：对你刚生成的修改功能做自审。
范围：只检查 app/routes.py、app/repository.py、app/schemas.py 的当前改动。
检查项：
  1. 是否引入范围外改动；
  2. 是否改变既有函数签名或 JSON 契约；
  3. 错误分支是否返回规格要求的状态码；
  4. 是否存在与添加功能重复的逻辑（应复用）。
验收：输出问题清单（每条附文件与行号证据）；无问题则明确说“自审通过，无范围外改动”。
输出：Markdown 清单，不超过 300 字。
```

自审解决机械问题；**需求理解是否正确仍由你判断**——比如“修改时是否允许只传部分字段”，AI 无法替你决策，规格里写了什么就是什么。

### 步骤 6：合并回 main 并打标签

三个提交全部验收后：

```powershell
git switch main
git merge --no-ff feat/v0.2-crud
git tag -a v0.2 -m "subscriptions CRUD complete with validation"
```

## 6. AI 应生成的产物

每个任务包对应：1）范围内的文件修改；2）逐处改动说明；3）curl/pytest 形式的验证命令。三个功能完成后，你手里应有：三条独立提交、每条的 Diff 说明、每条的真实运行证据。

**AI 不应生成的**：依赖变更、数据库结构改动（本章规格未涉及）、前端大改版、对既有测试的删除。出现即恢复 + 收紧任务包。

## 7. 人工检查点

1. 三条提交的 Diff 是否互相独立？（只回滚校验不应影响修改功能——`git revert` 单条验证）
2. 每条 Diff 中是否有一行你说不出“为什么改它”？说不出就问 AI 或恢复。
3. 422 错误体的 message 是否字段级明确（能直接指导用户改输入）？
4. DELETE 后再 GET 是否 404？数据是否真从库中消失（查询 SQLite 文件确认）？
5. AI 自审清单里“无范围外改动”的声明，是否与 `git diff --stat` 一致？

## 8. 验收命令与通过标准

```powershell
git log --oneline        # 三条 feat 提交独立可见
git tag                  # v0.2 存在
python -m ruff check .   # 0 错误
# 三条 curl 命令状态码：200 / 422 / 404
```

通过标准：全部命令真实执行且结果符合规格；三条提交可独立 revert。

## 9. 常见失败及恢复方法

**症状 1：AI 每轮都把无关文件也改了。**
原因：任务包约束太弱（只说了“实现 X”）。
恢复：范围写死文件清单；每轮先 `git diff --stat` 核对文件数；越界即 `git restore <file>`。若持续出现，把范围约束前置为“输出前先列出你计划修改的文件，等确认后再写代码”。

**症状 2：修改功能把 created_at 也更新了。**
原因：AI 用“全量替换”实现 PUT。
恢复：任务包中显式写“不修改 created_at”；已生成的，在 repository 层排除该字段后重测；此坑记入失败案例库。

**症状 3：422 返回的是英文默认校验信息，用户无法理解。**
原因：未自定义 Pydantic 错误处理。
恢复：要求 AI 为字段校验错误加中文 message 映射；错误体结构写入 spec 后重测。

**症状 4：三个功能被 AI 合成了一次大生成，Diff 数百行。**
原因：你一次给了三个功能。
恢复：恢复全部改动（`git restore .`），严格按“一次一个任务包”重来。若已提交，`git reset --soft HEAD~1` 拆开重提（未共享时）。

**症状 5：AI 声称“验证通过”但 curl 实际 500。**
原因：它只检查了语法，未真正运行。
恢复：以你本机运行结果为准；把真实报错粘回给 AI 修复；牢记规则——运行验证永远由人触发、人看结果。

## 10. 本章 Git 提交

```text
分支：feat/v0.2-crud
feat: update subscription via PUT with validation
feat: delete subscription via DELETE
feat: tighten input validation for subscription fields
合并：git switch main && git merge --no-ff feat/v0.2-crud
标签：v0.2
```

## 11. 练习与扩展

1. 为“部分字段更新”（PATCH 语义）写任务包，体会与全量 PUT 的契约差异。
2. 故意给一个模糊任务包（“把校验做好一点”），观察 AI 的自由发挥，再对比严格任务包的产出差异。
3. 用 `git revert` 独立回滚三条提交之一，验证其余功能不受影响。
4. （进阶）把本章的任务包模板沉淀为项目里的 `docs/task-brief.md`，作为长期资产。

## 12. 参考资料

- Google 工程实践：小变更的价值（Small CLs）：https://google.github.io/eng-practices/review/developer/small-cls.html
- Anthropic：Effective context engineering for AI agents（任务上下文与最小信息原则）：https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- obra/superpowers 的 verification-before-completion 技能思想（完成前验证）：https://github.com/obra/superpowers
- ChiYu 铁人赛 Day 13（依蓝图自动建构 API，中文同型实践）：https://huangchiyu.com/ChiYu-Blog/posts/2025ithomeironmanday13/
