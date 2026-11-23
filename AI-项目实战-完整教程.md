<!-- 本文件由 scripts/build_book.py 生成，请修改源章节后重新构建。 -->

# AI 项目实战：从零生成、验收到持续维护

> 用一个真实项目，掌握需求、规格、编码、测试、部署、演化与 AI 工程化协作。

这不是一本“提示词大全”，也不是某个 AI 产品的操作手册。你要完成的是一个可导出、可测试、可发布、可回滚、可继续接手的软件项目。

## 你将学会什么

- 把模糊想法整理成意图、规格、验收场景和任务。
- 让 AI 小步完成实现，并通过 Diff、测试和 CI 检查结果。
- 用 Git 保留变更历史，在出错时恢复。
- 把项目规则、架构决策和故障经验沉淀为仓库资产。
- 修复 Bug、增加功能、接手旧项目，而不是推翻重写。
- 处理数据库迁移、备份恢复、依赖升级和文档漂移。
- 创建可复用 Skill，并逐步引入子 Agent 与 Issue-to-PR 自动化。

## 贯穿项目

教程使用“个人订阅与续费管理器”，默认技术栈为 Python、FastAPI、SQLite、原生 Web 前端、pytest、Ruff 和 GitHub Actions。

| 版本 | 你将完成的事情 |
|---|---|
| v0.0 | 生成一次性原型，观察需求模糊带来的失控 |
| v0.1 | 打通添加、查看订阅的完整流程 |
| v0.2 | 完成修改、删除、输入校验和小 PR |
| v1.0 | 补齐测试、CSV 导出、CI、部署与发布 |
| v1.1 | 修复 Bug、增加搜索筛选、局部重构、接手旧项目 |
| v1.2 | 完成数据库迁移、备份恢复与长期维护演练 |

## 推荐阅读路线

### 完整路线

按章节顺序阅读，并完成每章验收与五个实验。适合第一次独立完成软件项目的读者。

### 快速生成路线

第 1—9 章 → 第 11 章 → 实验三。适合想先做出并发布第一个版本的读者；之后仍需补读维护部分。

### 已有项目维护路线

第 2—3 章 → 第 9—10 章 → 第 12—16 章 → 实验四、五。适合已有代码仓库的读者。

### 工程自动化路线

先完成核心 16 章，再读第 17—19 章。不要从多 Agent 和自动化开始第一次项目实践。

## 第一部分：建立正确的 AI 开发方式

1. [AI 能生成代码，为什么项目仍然会失败](chapters/ch01-why-projects-fail.md)
2. [零基础必备：看懂项目、运行项目和阅读报错](chapters/ch02-project-basics.md)
3. [Git：AI 开发的安全带与时间机器](chapters/ch03-git-safety.md)

- [综合实验一：一次性原型与失控复盘](labs/lab01-disposable-prototype.md)

## 第二部分：从模糊想法到可实施规格

4. [从想法到意图：先决定不做什么](chapters/ch04-intent-and-acceptance.md)
5. [规格驱动开发：把需求写成可验证契约](chapters/ch05-spec-driven-development.md)
6. [最小架构、技术决策与任务拆分](chapters/ch06-architecture-and-planning.md)

- [综合实验二：不写代码，完成项目蓝图](labs/lab02-project-blueprint.md)

## 第三部分：AI 生成、验证与首次交付

7. [纵向打通：生成第一个真正可用的版本](chapters/ch07-vertical-slice.md)
8. [AI 实现闭环：小任务、小 Diff、小 PR](chapters/ch08-small-steps-and-prs.md)
9. [测试与调试：让“AI 说完成”变成可验证事实](chapters/ch09-testing-and-debugging.md)
10. [上下文工程：让 AI 在新会话中也能接手项目](chapters/ch10-context-engineering.md)
11. [CI、发布与部署：从本地能跑到别人能用](chapters/ch11-ci-release-deploy.md)

- [综合实验三：交付第一个正式版本](labs/lab03-release-v1.md)

## 第四部分：从会生成到能长期维护

12. [Issue 驱动维护：从问题报告到修复 PR](chapters/ch12-issue-driven-maintenance.md)
13. [需求演化与重构：修改系统，而不是重新生成系统](chapters/ch13-change-and-refactoring.md)
14. [接手旧项目：从陌生仓库到受控现代化](chapters/ch14-legacy-modernization.md)
15. [数据库迁移、备份与真正的故障恢复](chapters/ch15-data-migration-recovery.md)
16. [长期维护系统：依赖、安全、运行观测与文档漂移](chapters/ch16-long-term-maintenance.md)

- [综合实验四：完成一次完整的需求演化](labs/lab04-evolution-v1-1.md)
- [综合实验五：模拟项目上线三个月](labs/lab05-three-month-maintenance.md)

## 第五部分：把经验沉淀为可复用的 AI 工程能力

17. [Skill 工程：把有效协作流程变成项目资产](chapters/ch17-skill-engineering.md)
18. [子 Agent、Hooks 与 Issue-to-PR 自动化](chapters/ch18-subagents-and-automation.md)
19. [平台对照与工具迁移：不被某个产品绑定](chapters/ch19-platforms-and-tool-migration.md)
20. [结业项目：完成你自己的 AI 生成与维护闭环](chapters/ch20-capstone.md)

## 附录

- [附录 A：开发环境与故障速查](appendices/A-environment.md)
- [附录 B：工具命令对照](appendices/B-command-reference.md)
- [附录 C：失败案例库](appendices/C-failure-catalog.md)
- [附录 D：术语表](appendices/D-glossary.md)
- [附录 E：参考资料与来源索引](appendices/E-sources.md)

## 可复制模板

| 模板 | 用途 |
|---|---|
| [项目意图](templates/intent.md) | 明确用户、问题、范围、约束与成功标准 |
| [功能规格](templates/spec.md) | 记录行为、规则和验收场景 |
| [实施计划](templates/plan.md) | 记录技术方案、影响范围和验证策略 |
| [任务列表](templates/tasks.md) | 把计划拆成可独立验证的小任务 |
| [架构决策记录](templates/adr.md) | 保存技术选择的原因和后果 |
| [Issue](templates/issue.md) | 描述一个可交付的问题或需求 |
| [Bug 报告](templates/bug-report.md) | 保存复现、证据、影响与回归要求 |
| [PR 检查清单](templates/pr-checklist.md) | 审查 Diff、测试、兼容性和交付证据 |
| [发布检查清单](templates/release-checklist.md) | 检查构建、部署、回滚和发布记录 |
| [运行维护手册](templates/runbook.md) | 记录启动、观测、备份和故障处理 |
| [会话交接](templates/handoff.md) | 让新 AI 会话从项目事实继续工作 |
| [完成定义](templates/definition-of-done.md) | 统一“完成”所需的客观证据 |

## 每章如何使用

1. 先读“本章成果”和“起始项目状态”。
2. 按操作步骤完成任务，不要只复制 AI 的输出。
3. 在人工检查点阅读 Diff、文件和关键行为。
4. 执行验收命令，保存真实输出或截图。
5. 遇到失败时先按“症状—原因—恢复”处理。
6. 验收通过后，再按建议拆分 Git 提交。

## 教程的验收原则

- AI 说“完成”不是证据。
- 页面能打开不等于核心流程正确。
- 测试全绿还要检查测试是否真的断言了业务行为。
- 代码回滚不等于数据已经恢复。
- 平台快照不替代正式 Git 历史。
- 项目只有在干净环境可复现、后续变化可局部实现时，才算真正可交付、可维护。

## 写作与维护

章节结构、项目字段、命令和作者分工约定见 [写作与集成契约](WRITING_GUIDE.md)。工具功能具有时效性，具体产品能力以官方最新文档为准；稳定的方法和验收原则不随工具界面变化而变化。

---

# 第 1 章　AI 能生成代码，为什么项目仍然会失败

> 本章成果：亲手生成一个订阅管理器的一次性原型，记录它为什么不能作为正式项目，并建立“AI 负责实现、人负责验收”的基本工作习惯。

## 1. 本章成果

完成本章后，你会得到一个标记为 `v0.0` 的临时原型，以及一份属于你自己的项目问题清单。

具体产出包括：

- 一个单文件 HTML 原型 `index.html`
- 一份人工观察记录 `observations.md`
- 至少三个可复述的问题，例如需求误解、状态丢失、金额处理不清、缺少测试、修改范围失控
- 一个明确结论：这个原型只能用于学习，不应直接继续扩展成正式项目

本章不追求“功能越多越好”。相反，我们故意让 AI 快速生成一个看起来能跑的页面，然后观察它缺少哪些东西。后面所有章节会逐步补齐这些缺口：需求与规格、架构、测试、Git、上下文、发布和维护。

## 2. 为什么需要它

很多 AI 编程教程从“安装工具”或“写提示词”开始，但真正拉开差距的不是生成能力，而是能否持续修改和验收。AI 已经可以很快产出页面、接口和数据库代码；项目失败通常发生在后续阶段：需求变化时不知道改哪里，代码越来越多时不敢改，出错时无法复现，上线后没有日志、备份和回滚。

一次性原型实验有三个作用：

1. **让你亲身体验 Demo 与产品的区别。** 页面能打开，不等于需求完整；AI 说“已完成”，不等于用户可以安全使用。
2. **建立证据意识。** 后续每章都会要求你留下命令输出、测试结果、Diff 或运行记录，而不是接受模型的自然语言承诺。
3. **避免过早依赖某个工具。** 本章只需要浏览器、文本编辑器和任意能写代码的 AI。Python、Git、测试和部署会按学习顺序逐步加入。

[生成式软件工程课程](https://jyywiki.cn/GSE/2026/)在第一讲中就强调，成功演示并不等于需求实现；[ChiYu 的《左手蓝图，右手魔法》系列](https://huangchiyu.com/ChiYu-Blog/series/2025ithomeironman/)也用“只想要脚踏车，却得到航空母舰”描述无约束 Vibe Coding 的失控。本章会把这种失控变成一次可控的观察实验。

## 3. 最少必备知识

- **HTML、CSS、JavaScript 的分工：** HTML 是内容结构，CSS 是外观，JavaScript 负责交互。本章原型不会建立真正的前后端分离系统。
- **浏览器本地文件：** 双击或通过命令打开的 `index.html` 只运行在当前浏览器中，不等于部署到服务器。
- **浏览器控制台：** 通常按 `F12` 或 `Ctrl+Shift+I` 打开，用于查看 JavaScript 错误。
- **内存数据与持久化数据：** 数据如果只保存在页面 JavaScript 变量中，刷新后通常会消失；如果写入 `localStorage`，同一浏览器可能保留，但仍不是数据库。
- **需求、验收、回归：** 需求说明要做什么，验收说明如何证明做到了，回归确保修复或新增功能没有破坏旧行为。
- **一次性原型：** 目标是验证想法和暴露问题，不是长期维护对象。

如果你不理解某个术语，不必立刻查全部资料。本章只需要能打开文件、点击页面、阅读错误并记录现象。

## 4. 起始项目状态

本章从一个空目录开始，不依赖任何配套仓库、模板或在线环境。

建议目录：

```text
subscription-tracker-prototype/
```

完成本章后，目录至少应包含：

```text
subscription-tracker-prototype/
├─ index.html
└─ observations.md
```

你可以自行增加：

```text
subscription-tracker-prototype/
├─ index-before-edit.html
└─ evidence/
   ├─ 01-initial.png
   ├─ 02-add-record.png
   └─ 03-console-error.png
```

安全边界：

- 不要输入真实银行卡、账号密码、手机号或个人订阅数据。
- 不要连接真实支付、邮件、短信或云服务。
- 不要把本章原型部署给真实用户。

本章故意不创建正式项目目录 `subscription-tracker/`。那个目录会在后续章节中建立，避免一次性实验污染正式项目历史。

## 5. 操作步骤与 AI 任务示例

### 5.1 创建实验目录

在 PowerShell、Terminal 或其他终端中执行：

```powershell
mkdir subscription-tracker-prototype
cd subscription-tracker-prototype
```

Windows、macOS 和 Linux 的这条命令基本相同。进入目录后，再创建空白文件：

```text
index.html
observations.md
```

也可以先让 AI 生成内容，再由你保存为这两个文件。

### 5.2 使用第一个 AI 任务生成一次性原型

将以下内容发送给你使用的 AI 编码工具。这个提示词刻意限制范围和输出形式，避免 AI 引入框架、后端或真实外部服务。

```text
目标：
创建一个用于教学观察的一次性订阅管理器 HTML 原型。

上下文：
这是教程第 1 章的 v0.0 实验，读者可能没有编程经验。它只用于暴露 AI 生成项目的常见问题，不用于真实交付。

范围：
只允许创建一个自包含的 index.html，内部可包含 HTML、CSS 和 JavaScript。
实现以下功能：
1. 展示一个订阅列表。
2. 初始提供两条示例数据。
3. 用户可添加一条新订阅。
4. 每条记录包含 name、amount_cents、renewal_date、note 四个字段。
5. amount_cents 使用整数“分”表示金额，页面显示时可转换为元，但内部计算和存储保持整数。

约束：
- 不使用 React、Vue、构建工具、后端、数据库或任何外部库。
- 不请求外部 URL，不加载远程字体、图片或脚本。
- 不保存真实个人数据，不使用支付、短信、邮件或认证。
- 不要求持久化；刷新后新增数据消失是可接受结果，但必须在说明中写明当前状态保存方式。
- 代码应能在现代浏览器中直接打开运行。

验收：
1. 打开 index.html 后能看到示例订阅。
2. 填写 name="测试网盘"、amount_cents=9900、renewal_date="2027-01-01"、note="教学示例" 后可以新增一条记录。
3. amount_cents 为 0、负数或非整数时应被拒绝，并显示可理解的错误。
4. 控制台没有阻塞页面使用的 JavaScript 错误。
5. 明确说明数据是否会在刷新后保留。

输出：
1. 完整 index.html。
2. 不超过 15 行的实现说明。
3. 不超过 10 条已知限制。
不要输出安装步骤、部署建议或后续扩展计划。
```

如果 AI 返回多个文件、框架项目或要求安装依赖，不要继续扩展。把最后一段约束重新发给它，要求“只输出完整单文件 `index.html`”。

### 5.3 保存并打开原型

把 AI 输出保存为 `index.html`，确保文件编码为 UTF-8。

打开方式：

```powershell
# Windows PowerShell
Invoke-Item index.html
```

```bash
# macOS
open index.html
```

```bash
# Linux，根据桌面环境选择其中一种
xdg-open index.html
```

也可以直接在文件管理器中双击。打开后按 `F12` 或 `Ctrl+Shift+I` 查看控制台。

### 5.4 执行第一轮人工验收

逐项测试并记录实际结果：

1. 页面是否显示两条示例订阅？
2. 添加 `测试网盘 / 9900 / 2027-01-01 / 教学示例` 是否成功？
3. 金额显示是否正确？`9900` 分应显示为 `99.00` 元或等价格式。
4. 输入 `-1`、`0`、`99.5`、空名称时，页面是否阻止无效数据？
5. 刷新页面后，新增记录是否仍然存在？
6. 控制台是否出现 JavaScript 错误？

在 `observations.md` 中使用如下表格：

```markdown
| 测试 | 预期 | 实际 | 证据 | 判断 |
|---|---|---|---|---|
| 初始列表 | 显示两条示例 | 待填写 | 截图或控制台输出 | 通过/失败/范围外 |
| 新增有效记录 | 列表增加一条 | 待填写 | 截图 | 通过/失败 |
| 金额显示 | 9900 分显示为 99.00 元 | 待填写 | 截图 | 通过/失败 |
| 无效金额 | 拒绝并提示 | 待填写 | 截图 | 通过/失败 |
| 刷新后状态 | 记录当前保存方式 | 待填写 | 截图 | 说明 |
| 控制台错误 | 无阻塞错误 | 待填写 | 错误文本 | 通过/失败 |
```

### 5.5 观察一次需求变更

需求变更是项目维护的常态。我们先制造一次很小的变更，观察 AI 是否只改必要范围。

先备份当前文件：

```powershell
# Windows PowerShell
Copy-Item index.html index-before-edit.html
```

```bash
# macOS/Linux
cp index.html index-before-edit.html
```

发送第二个 AI 任务：

```text
目标：
在现有 index.html 中增加“编辑已存在订阅”的功能。

上下文：
当前文件是一个教学用一次性原型，数据保存在浏览器页面状态中，不是正式产品。

范围：
只允许修改现有 index.html。
只能增加编辑 name、amount_cents、renewal_date、note 的能力。
不要修改现有视觉风格，不要新增页面、文件或外部依赖。

约束：
- 编辑前必须保留原值。
- 取消编辑后不得留下重复记录或破坏现有列表。
- 仍然使用整数 amount_cents。
- 不引入 React、Vue、构建工具、后端、数据库或外部库。

验收：
1. 可以选择任意一条记录进入编辑状态。
2. 修改并保存后，列表只显示更新后的结果，不产生重复项。
3. 取消编辑后列表保持不变。
4. 原有新增和无效输入校验仍然可用。
5. 说明本次修改涉及哪些 HTML、CSS 或 JavaScript 区域。

输出：
1. 完整更新后的 index.html。
2. 不超过 10 条变更说明。
3. 不超过 5 条新增风险。
```

保存新版本，重复上一轮测试，并额外验证：

- 是否能选择一条记录进入编辑状态？
- 保存后是否只更新该记录？
- 取消后是否保持原样？
- 原来的新增和校验是否仍然可用？

### 5.6 记录问题并丢弃原型

在 `observations.md` 中至少写下三类问题：

```markdown
## 这个原型不能作为正式项目的原因

1. 需求方面：……
2. 数据方面：……
3. 质量方面：……
4. 维护方面：……
5. 交付方面：……
```

你可以写：

- 没有规格，AI 只能猜测用户真实意图。
- 数据只在浏览器中，不能多设备使用，也没有备份。
- 没有测试，任何修改都可能破坏旧功能。
- 没有 Git，AI 大范围修改后无法可靠回退。
- 没有部署、日志和监控，不能判断线上问题。

这些正是后续章节要解决的问题。完成记录后，不要继续向这个原型添加功能。它是 `v0.0`，已经完成教学使命。

### 5.7 配套实验

如果你希望执行更完整的步骤、自检表和常见失败处理，可以继续完成[实验 1：一次性原型](../labs/lab01-disposable-prototype.md)。

## 6. AI 应生成的产物

第一个任务完成后，AI 应提供：

- 完整单文件 `index.html`
- 简短实现说明
- 已知限制

第二个任务完成后，AI 应提供：

- 更新后的完整 `index.html`
- 变更说明
- 新增风险

以下内容必须由你完成，不能直接让 AI 替代：

- `observations.md`
- 每项测试的实际结果
- 控制台错误原文
- 是否通过验收的最终判断

如果 AI 在输出中声称“已通过全部测试”，你仍应把这句话视为待验证声明。只有浏览器中的实际行为、控制台信息和你的记录才是证据。

## 7. 人工检查点

打开 `index.html` 的源代码，重点检查：

1. **外部依赖**
   ```powershell
   # Windows PowerShell
   Select-String -Path index.html -Pattern "https?://"
   ```

   ```bash
   # macOS/Linux
   grep -nE "https?://" index.html
   ```

   如果搜到外部 URL，逐个判断它是否违反了“不请求外部资源”的约束。

2. **危险或可疑代码**
   ```powershell
   Select-String -Path index.html -Pattern "eval\(|document\.write|innerHTML"
   ```

   ```bash
   grep -nE "eval\(|document\.write|innerHTML" index.html
   ```

   出现这些模式不一定是致命错误，但你需要理解它们的用途。若无法解释，就不要继续扩展该文件。

3. **金额处理**
   查找 `amount_cents`、`parseInt`、`Number`、`parseFloat` 等关键字，确认内部是否真的使用整数，而不是先转成浮点数再四舍五入。

4. **状态保存方式**
   查找 `localStorage`、`sessionStorage` 或 JavaScript 变量。记录刷新后数据为什么会保留或消失。

5. **第二次修改范围**
   对比 `index-before-edit.html` 与新 `index.html`。此时你还没有学习 Git Diff，因此可以先观察：
   - 文件大小是否变化异常
   - 页面结构是否被重写
   - 原有功能是否仍能使用
   - AI 的变更说明是否与实际测试一致

6. **AI 自述与证据是否一致**
   如果 AI 说“已保留原功能”，你必须重新测试新增和校验；如果 AI 说“不会丢失数据”，你必须刷新页面验证。

## 8. 验收命令与通过标准

执行以下检查：

```powershell
# Windows PowerShell
Get-ChildItem
Get-Item index.html
Get-Item observations.md
Select-String -Path index.html -Pattern "https?://"
```

```bash
# macOS/Linux
ls -l
test -f index.html && echo "index.html exists"
test -f observations.md && echo "observations.md exists"
grep -nE "https?://" index.html
```

本章通过标准：

1. `index.html` 和 `observations.md` 都存在于实验目录中。
2. 浏览器能打开原型，并记录初始页面状态。
3. 你完成了至少六项第一轮测试，并记录实际结果。
4. 你完成了一次“编辑功能”需求变更，并记录至少一个新增问题或风险。
5. `observations.md` 至少写出三个原型不能直接进入正式项目的原因。
6. 你没有把 AI 的“已完成”声明直接当作验收结果。

不要要求原型没有 Bug。本章的通过标准不是完美，而是你能准确说出它哪里不完整、为什么不可交付，以及下一步应该补什么。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| AI 输出 React、Node.js、多个文件或安装步骤 | 原始需求中“完整”“项目”等词触发过度设计 | 停止安装；重发约束，要求“只输出完整单文件 `index.html`，不使用框架和外部依赖” |
| 浏览器打开后空白 | HTML 未保存完整、文件编码错误、JavaScript 初始化异常 | 打开控制台复制错误；从 AI 最近一次完整输出重新保存；必要时要求它只修复报错，不新增功能 |
| 点击“添加”没有反应 | 按钮 ID 与 JavaScript 不匹配、事件未绑定、脚本报错中断 | 记录控制台错误和按钮 HTML；要求 AI 只修复事件绑定；若无法定位，恢复 `index-before-edit.html` 后重新描述问题 |
| 中文显示乱码 | 文件不是 UTF-8，或缺少 `<meta charset="utf-8">` | 用支持 UTF-8 的编辑器重新保存；检查 HTML 头部 charset；不要让 AI 重写整个页面 |
| 刷新后新增数据消失 | 数据只保存在 JavaScript 内存中，或原型未实现持久化 | 这不是必须立即修复的 Bug，而是设计边界。记录当前保存方式，并说明正式项目需要数据库和迁移策略 |
| 第二次需求变更后原功能失效 | AI 重写了无关代码，或没有保留旧行为基线 | 恢复 `index-before-edit.html`；将变更拆得更小；重新发送只包含编辑功能的范围约束 |

恢复时遵循一个原则：**先回到最后一个已知可运行状态，再缩小任务。** 不要在一个已经混乱的文件上继续叠加新功能。

## 10. 本章 Git 提交

第 3 章才会正式学习 Git，因此本章不要求你已经安装或初始化仓库。

如果你希望保留这个一次性原型作为学习记录，可在第 3 章之后执行：

```powershell
git init
git switch -c exp/disposable-prototype
git add index.html observations.md
git commit -m "test: record disposable prototype limitations"
git tag v0.0
```

说明：

- `exp/disposable-prototype` 表示这是实验分支，不应继续作为正式项目主线。
- `v0.0` 只是本教程的版本约定，不代表存在一个可下载的现成标签。
- 不必提交 `index-before-edit.html`，除非你想保留需求变更前后的人工对照。
- 不要把本章原型推送到公开仓库，尤其当其中包含你临时记录的个人测试数据时。

## 11. 练习与扩展

1. **换一个问题领域重做实验。** 把订阅管理器换成“读书笔记”或“家庭物品清单”，仍然只允许单文件 HTML。观察 AI 是否犯同类错误。
2. **只允许 AI 提问，不允许写代码。** 把你的模糊想法发给 AI，要求它最多提出 10 个澄清问题。整理哪些问题真正影响实现。
3. **列出五个隐藏假设。** 例如“金额单位是元还是分”“续费日期是否包含时区”“删除是否需要确认”“数据是否多设备同步”。
4. **比较两种修改策略。** 第一次要求“增加完整编辑功能”，第二次要求“只增加编辑备注字段”，记录修改范围和失败风险差异。
5. **写一段 200 字复盘。** 说明如果直接把这个原型交给朋友使用，最可能在哪一天、因为什么问题失败。

## 12. 参考资料

- [生成式软件工程（2026 秋季学期）](https://jyywiki.cn/GSE/2026/)
- [GSE 2026 第一讲：欢迎来到未来](https://jyywiki.cn/GSE/2026/lect1.md)
- [ChiYu：2025 iThome 鐵人賽《左手蓝图，右手魔法》系列](https://huangchiyu.com/ChiYu-Blog/series/2025ithomeironman/)

---

# 实验 1：一次性原型——生成、观察、修改、丢弃

> 实验目标：用最快速度让 AI 生成一个订阅管理器原型，再通过人工测试和一次需求变更，证明“页面能跑”不等于“项目可交付”。

本实验对应 `v0.0`，只用于观察 AI 生成项目的常见缺口。它不是正式项目，不建议继续扩展、部署或交给真实用户使用。

## 1. 实验准备

### 1.1 需要的工具

- 一个现代浏览器
- 一个支持 UTF-8 的文本编辑器
- 任意能够生成或修改 HTML/CSS/JavaScript 的 AI 工具
- Windows PowerShell、macOS Terminal 或 Linux Shell

本实验不要求：

- Python
- Node.js
- Git
- 数据库
- 云服务账号
- 真实部署

### 1.2 安全边界

- 不使用真实姓名、手机号、银行卡、密码或个人订阅账号。
- 不连接支付、邮件、短信、云存储或第三方 API。
- 所有示例数据都应明确可识别为教学数据，例如 `测试网盘`、`示例音乐会员`。
- 实验目录应独立于后续正式项目目录，避免把临时原型混入项目历史。

### 1.3 创建目录

```powershell
mkdir subscription-tracker-prototype
cd subscription-tracker-prototype
mkdir evidence
```

创建以下空文件：

```text
index.html
observations.md
```

最终至少得到：

```text
subscription-tracker-prototype/
├─ evidence/
├─ index.html
└─ observations.md
```

## 2. 实验任务

本实验分为四个阶段：

1. 生成最小原型
2. 人工验收
3. 增加一次小需求变更
4. 记录不可交付原因并丢弃原型

每个阶段都必须留下证据，而不是只记录“AI 说完成了”。

## 3. 阶段一：生成最小原型

### 3.1 初始提示词

将以下内容完整发送给 AI：

```text
目标：
创建一个用于教学观察的一次性订阅管理器 HTML 原型。

上下文：
读者可能没有编程经验。这是 v0.0 实验，只用于暴露 AI 生成项目的问题，不用于真实交付。

范围：
只允许创建一个自包含的 index.html，内部可包含 HTML、CSS 和 JavaScript。
实现：
1. 展示订阅列表。
2. 初始提供两条示例数据。
3. 用户可以添加一条新订阅。
4. 字段为 name、amount_cents、renewal_date、note。
5. amount_cents 使用整数“分”表示金额；页面显示可转换为元，但内部保存和校验保持整数。
6. 无效输入包括空 name、amount_cents 小于等于 0、amount_cents 非整数、renewal_date 为空。

约束：
- 不使用 React、Vue、构建工具、后端、数据库或任何外部库。
- 不请求外部 URL，不加载远程字体、图片或脚本。
- 不保存真实个人数据，不接入支付、短信、邮件或认证。
- 不要求刷新后保留数据；若使用 localStorage，必须明确说明。
- 代码应能在现代浏览器中直接打开运行。

验收：
1. 打开 index.html 后能看到两条示例订阅。
2. 添加 name="测试网盘"、amount_cents=9900、renewal_date="2027-01-01"、note="教学示例" 后列表新增一条记录。
3. amount_cents=9900 应显示为 99.00 元或等价格式。
4. 输入 -1、0、99.5 或空名称时应被拒绝，并显示用户可理解的错误。
5. 控制台没有阻塞页面使用的 JavaScript 错误。
6. 说明数据刷新后是否保留，以及当前使用什么方式保存。

输出：
1. 完整 index.html。
2. 不超过 15 行实现说明。
3. 不超过 10 条已知限制。
不要输出安装步骤、部署建议或后续扩展计划。
```

### 3.2 保存结果

将 AI 输出保存为 `index.html`，确保编码为 UTF-8。

如果 AI 返回多个文件、框架项目或安装命令，发送以下纠正提示：

```text
你超出了范围。请只输出完整单文件 index.html。
不要使用 React、Vue、构建工具、后端、数据库、外部库或安装步骤。
保留原始功能，不新增功能。
```

### 3.3 打开原型

```powershell
# Windows PowerShell
Invoke-Item index.html
```

```bash
# macOS
open index.html
```

```bash
# Linux
xdg-open index.html
```

打开浏览器控制台，通常使用 `F12` 或 `Ctrl+Shift+I`。

## 4. 阶段二：人工验收

### 4.1 功能测试表

在 `observations.md` 中建立以下表格，并逐项填写：

```markdown
| 编号 | 测试 | 操作 | 预期 | 实际 | 证据 | 结果 |
|---|---|---|---|---|---|---|
| T1 | 初始列表 | 打开 index.html | 显示两条示例订阅 | 待填写 | evidence/01-initial.png | 通过/失败 |
| T2 | 新增有效记录 | 添加“测试网盘 / 9900 / 2027-01-01 / 教学示例” | 列表新增一条记录 | 待填写 | evidence/02-add-record.png | 通过/失败 |
| T3 | 金额显示 | 查看 9900 分 | 显示 99.00 元或等价格式 | 待填写 | evidence/03-amount.png | 通过/失败 |
| T4 | 空名称 | name 留空并提交 | 拒绝并提示 | 待填写 | evidence/04-empty-name.png | 通过/失败 |
| T5 | 非法金额 | 分别输入 -1、0、99.5 | 拒绝并提示 | 待填写 | evidence/05-invalid-amount.png | 通过/失败 |
| T6 | 空日期 | renewal_date 留空 | 拒绝并提示 | 待填写 | evidence/06-empty-date.png | 通过/失败 |
| T7 | 刷新状态 | 添加记录后刷新页面 | 记录实际保存方式 | 待填写 | evidence/07-refresh.png | 说明 |
| T8 | 控制台错误 | 执行 T1—T7 后查看控制台 | 无阻塞错误 | 待填写 | evidence/08-console.png | 通过/失败 |
```

截图不是强制要求。如果你不方便截图，可以保存控制台错误文本、页面显示内容的文字描述，以及你输入的具体测试数据。

### 4.2 代码检查

检查是否存在外部资源：

```powershell
# Windows PowerShell
Select-String -Path index.html -Pattern "https?://"
```

```bash
# macOS/Linux
grep -nE "https?://" index.html
```

检查是否存在需要解释的危险模式：

```powershell
Select-String -Path index.html -Pattern "eval\(|document\.write|innerHTML"
```

```bash
grep -nE "eval\(|document\.write|innerHTML" index.html
```

检查金额字段：

```powershell
Select-String -Path index.html -Pattern "amount_cents|parseInt|Number\(|parseFloat"
```

```bash
grep -nE "amount_cents|parseInt|Number\(|parseFloat" index.html
```

在 `observations.md` 中记录：

- 是否发现外部 URL
- 是否发现 `localStorage` 或 `sessionStorage`
- 金额是否真的按整数处理
- 是否存在你无法解释的 JavaScript 代码

### 4.3 至少记录三个问题

```markdown
## v0.0 原型的主要问题

1. 需求问题：……
2. 数据问题：……
3. 质量问题：……
4. 维护问题：……
5. 交付问题：……
```

至少完成三条。每条应包含“现象、影响、后续哪一章解决”。

例如：

```markdown
刷新后新增记录消失。
影响：用户无法长期保存订阅，不能用于真实场景。
后续：第 7 章引入 SQLite，第 15 章学习数据迁移与备份恢复。
```

## 5. 阶段三：一次小需求变更

### 5.1 备份当前版本

```powershell
# Windows PowerShell
Copy-Item index.html index-before-edit.html
```

```bash
# macOS/Linux
cp index.html index-before-edit.html
```

### 5.2 变更提示词

```text
目标：
在现有 index.html 中增加“编辑已存在订阅”的功能。

上下文：
当前文件是教学用一次性原型，数据保存在浏览器页面状态中，不是正式产品。

范围：
只允许修改现有 index.html。
只能增加编辑 name、amount_cents、renewal_date、note 的能力。
不要修改现有视觉风格，不要新增页面、文件或外部依赖。

约束：
- 编辑前必须保留原值。
- 取消编辑后不得留下重复记录或破坏现有列表。
- 仍然使用整数 amount_cents。
- 不引入 React、Vue、构建工具、后端、数据库或外部库。
- 不要重写与编辑功能无关的代码。

验收：
1. 可以选择任意一条记录进入编辑状态。
2. 修改并保存后，列表只显示更新后的结果，不产生重复项。
3. 取消编辑后列表保持不变。
4. 原有新增和无效输入校验仍然可用。
5. 说明本次修改涉及哪些 HTML、CSS 或 JavaScript 区域。

输出：
1. 完整更新后的 index.html。
2. 不超过 10 条变更说明。
3. 不超过 5 条新增风险。
```

### 5.3 变更后的补充测试

在 `observations.md` 中追加：

```markdown
| 编号 | 测试 | 操作 | 预期 | 实际 | 证据 | 结果 |
|---|---|---|---|---|---|---|
| E1 | 进入编辑 | 点击任意记录的编辑入口 | 表单显示原值 | 待填写 | evidence/edit-01.png | 通过/失败 |
| E2 | 保存修改 | 修改 note 后保存 | 只更新该记录 | 待填写 | evidence/edit-02.png | 通过/失败 |
| E3 | 取消编辑 | 修改字段后取消 | 列表恢复原状 | 待填写 | evidence/edit-03.png | 通过/失败 |
| E4 | 重复项检查 | 连续编辑同一条记录两次 | 不产生重复记录 | 待填写 | evidence/edit-04.png | 通过/失败 |
| E5 | 原有新增功能 | 再次添加一条新记录 | 仍可新增 | 待填写 | evidence/edit-05.png | 通过/失败 |
| E6 | 原有校验 | 输入非法金额 | 仍被拒绝 | 待填写 | evidence/edit-06.png | 通过/失败 |
```

### 5.4 判断修改是否失控

记录以下问题：

- AI 是否修改了与编辑无关的页面结构？
- 原有示例数据是否消失或改变？
- 是否新增了外部依赖？
- 变更说明是否与你的测试结果一致？
- 你是否还能解释当前 `index.html` 的主要结构？

如果最后一项答案为“不能”，这就是一个重要的维护风险信号。

## 6. 阶段四：丢弃与复盘

### 6.1 写出最终结论

在 `observations.md` 末尾补充：

```markdown
## 为什么这个原型不能继续扩展

- 没有规格和验收标准，后续需求会继续靠猜测。
- 没有数据库，真实数据无法可靠保存。
- 没有测试，任何修改都可能破坏旧功能。
- 没有 Git，AI 大范围修改后无法可靠回退。
- 没有部署、日志、备份和回滚流程。
```

根据你自己的实验结果修改上述条目，不要机械复制。

### 6.2 停止继续加功能

不要继续让 AI 添加登录、支付、提醒、云同步或美观样式。这个实验的重点不是做出一个“看起来完整”的页面，而是证明缺少工程闭环时，生成速度越快，后续维护风险越大。

### 6.3 可选保留

如果你想保留实验记录，等第 3 章学习 Git 后再创建本地仓库并提交：

```powershell
git init
git switch -c exp/disposable-prototype
git add index.html observations.md
git commit -m "test: record disposable prototype limitations"
git tag v0.0
```

不要推送到公开仓库，尤其当 `observations.md` 中包含你的临时测试信息时。

## 7. 自检表

完成实验前逐项确认：

- [ ] 已创建独立的 `subscription-tracker-prototype/` 目录。
- [ ] `index.html` 能在浏览器中打开。
- [ ] 已完成 T1—T8 八项初始测试。
- [ ] 已记录控制台错误或“无阻塞错误”的实际观察。
- [ ] 已检查外部 URL、存储方式和金额字段。
- [ ] 已备份 `index-before-edit.html`。
- [ ] 已完成 E1—E6 六项编辑功能测试。
- [ ] 已记录至少三个不可交付原因。
- [ ] 已区分 AI 的自述与你的实际观察。
- [ ] 已停止继续扩展原型。

## 8. 常见失败与恢复

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| AI 生成了 React、Node.js 或多文件项目 | “完整项目”“企业级”等词触发过度设计 | 不安装依赖；重发范围约束，要求只输出单文件 `index.html` |
| 页面打开后完全空白 | HTML 保存不完整、UTF-8 编码错误、脚本初始化失败 | 打开控制台复制第一条错误；重新保存 AI 的完整输出；要求只修复该错误，不新增功能 |
| 添加按钮无响应 | 按钮 ID 与 JavaScript 选择器不匹配，或事件监听器未绑定 | 记录按钮 HTML 和控制台错误；要求 AI 只修复事件绑定；无法定位时恢复备份文件 |
| 金额显示为 `NaN`、`99` 或 `9900 元` | 输入未转换为整数，或显示逻辑混淆“分”和“元” | 检查 `amount_cents` 相关代码；要求 AI 内部保持整数、仅显示时除以 100，并补充无效输入校验 |
| 刷新后记录消失 | 数据只保存在 JavaScript 内存中 | 在观察记录中写明这是设计边界；正式项目需要数据库、迁移和备份，不在 v0.0 修复 |
| 编辑功能导致记录重复 | 保存时新增了一条记录，而不是更新原记录 | 恢复 `index-before-edit.html`；要求 AI 只实现“根据记录标识更新原对象”，不改变新增逻辑 |
| 第二次修改后无法解释代码 | AI 重写了无关区域，上下文和范围失控 | 停止继续修改；恢复备份；把需求拆得更小，并在后续章节引入 Git Diff、测试和规格 |
| 中文字符变成乱码 | 文件未以 UTF-8 保存，或缺少 charset 声明 | 使用 UTF-8 重新保存；检查 `<meta charset="utf-8">`；不要让 AI 重写整个页面 |

## 9. 实验通过标准

你不需要做出一个完美原型。满足以下条件即可视为通过：

1. 生成了可打开的单文件 HTML 原型。
2. 完成了至少八项初始人工测试。
3. 完成了一次编辑功能需求变更。
4. 记录了至少三个不能继续扩展的原因。
5. 能区分“AI 声称完成”和“浏览器实际验证”。
6. 主动停止了对 `v0.0` 原型的继续开发。

完成本实验后，你已经得到了后续教程最重要的经验：**AI 可以迅速生成表面可用的结果，但真正的项目需要规格、测试、版本控制、上下文、发布和维护共同约束。**

---

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

---

# 第 3 章　Git：AI 开发的安全带与时间机器

> 本章成果：建立项目 Git 基线，完成一次“AI 改坏 → 比较差异 → 恢复 → 重新修改”的完整演练，掌握让 AI 改代码时永远可回退的工作方式。

## 1. 本章成果

1. 项目拥有 Git 仓库、`.gitignore` 和一条清晰的提交历史。
2. 你能读懂 `git status`、`git diff`、`git log --oneline` 的输出。
3. 你完成过一次文件恢复与一次版本回滚，并知道两者差别。
4. 你形成了肌肉记忆：**让 AI 动手前先提交，AI 动完先看 Diff。**

## 2. 为什么需要它

AI 改代码有两个特点：改得快、改得多。没有版本控制的 AI 协作，就像没有刹车的高速驾驶——你以为自己在“快速迭代”，实际上是在赌每次生成都不出问题。常见事故包括：AI 顺手改坏了另一个模块、删掉了你没注意的文件、或把十几个无关改动混在一次修改里。Git 解决的不是“AI 会不会犯错”，而是“犯错之后代价有多大”。有基线时，回滚是一条命令的事；没有基线时，你可能要手工找回几个小时前的状态。此外，后续章节的分支、PR、CI、回滚演练，全部建立在 Git 之上。

## 3. 最少必备知识

- **仓库（repository）**：Git 管理的目录，`.git/` 隐藏文件夹记录全部历史。
- **工作区 / 暂存区 / 提交**：你编辑的是工作区；`git add` 把改动放进暂存区；`git commit` 把暂存区固化成一条历史。
- **提交（commit）**：一次快照＋说明。好提交=单一目的＋可读信息。
- **Diff**：两个版本之间的差异。`git diff` 看未暂存改动，`git diff --staged` 看待提交改动。
- **分支（branch）**：独立的开发线。`main` 保持稳定，功能在 `feat/xxx` 分支上做。
- **HEAD**：当前所在提交。
- **恢复 vs 回滚**：恢复（restore/checkout）针对文件，回滚（revert/reset）针对提交历史。
- **`.gitignore`**：声明不入库的文件（虚拟环境、数据库、日志、密钥）。

## 4. 起始项目状态

沿用第 2 章可运行的项目目录（订阅管理器起始骨架或第 1 章的 v0.0 原型均可）。本章开始前：

- Python 环境可用，`python --version` 正常。
- Git 已安装：`git --version` 正常；首次使用需配置身份：

```powershell
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

此时项目还没有 Git 仓库（或历史混乱），正是建立基线的时机。

## 5. 操作步骤与 AI 任务示例

### 步骤 1：初始化仓库与忽略规则

在项目根目录：

```powershell
git init
git status
```

创建 `.gitignore`（Windows 为主，兼顾 macOS/Linux）：

```text
.venv/
__pycache__/
*.pyc
data/
backups/
logs/
.env
.DS_Store
Thumbs.db
```

说明：`data/`（SQLite 数据文件）与 `logs/` 属于运行产物，不入库；`.env` 存密钥，永不入库。

### 步骤 2：建立第一次提交（基线）

```powershell
git add .gitignore README.md
git commit -m "chore: init repo with gitignore"
git add .
git status          # 确认没有意外文件（如 .venv）被暂存
git commit -m "feat: initial subscription tracker skeleton"
git log --oneline
```

你应看到两条历史。这就是**基线**：之后任何 AI 改动，都有一个“已知良好”的退路。

### 步骤 3：学习读 Diff

先自己改动一处（例如在 `README.md` 末尾加一行），然后：

```powershell
git diff
git diff --stat
```

读懂输出里的 `-`/`+` 行。这是后面审查 AI 改动的基本功：**AI 声称只改了 A，你用 Diff 验证它是否只改了 A。**

### 步骤 4：功能分支

```powershell
git switch -c feat/due-reminder
```

原则：`main` 只接收验证过的提交；实验性改动在分支上进行，失败就丢弃分支，`main` 不受影响。

### 步骤 5：AI 任务——一次受控的失败演练

这是本章核心练习。先提交当前干净状态，然后故意让 AI 改坏代码。

**给 AI 的任务示例（text 块）**：

```text
目标：为订阅列表 API 添加“按 renewal_date 排序”功能。
上下文：FastAPI 项目，订阅路由在 app/routes.py，数据访问在 app/repository.py。
范围：只允许修改 app/repository.py 和 app/routes.py；不得改其他文件；不得重命名现有函数。
约束：金额字段处理逻辑不得变动；返回 JSON 结构保持不变。
验收：GET /api/subscriptions?sort=asc 返回按 renewal_date 升序的列表；不传 sort 时行为与现在一致。
输出：直接给出修改后的完整文件内容，并说明每个函数的改动点。
```

AI 返回后，**先不要**直接运行：

```powershell
git diff --stat     # AI 声称的改动范围
git diff            # 实际改动内容
```

逐行核对：它是否碰了范围外的文件？是否悄悄重命名了函数？是否把“排序”写成了“过滤”？

### 步骤 6：改坏 → 比较 → 恢复 → 重新修改

假设 Diff 审查发现 AI 同时改了 `schemas.py`（范围外），且排序逻辑错误：

```powershell
# 只恢复被越权改动的文件
git restore app/schemas.py
# 若整个改动都不要了
git restore app/repository.py app/routes.py
```

恢复后，把明确的反馈给 AI，重新生成；每轮生成后重复步骤 5 的 Diff 审查。这个循环（生成→审查→恢复→再生成）就是“安全带”的全部用法。

### 步骤 7：提交与撤销提交

验收通过后：

```powershell
git add app/repository.py app/routes.py
git commit -m "feat: sort subscriptions by renewal_date"
```

若提交后发现信息写错或漏文件（尚未推送时）：

```powershell
git commit --amend -m "feat: sort subscriptions by renewal_date"
```

若要撤销一条已提交但未共享的提交，保留历史用 revert：

```powershell
git revert <commit-hash>
```

### 步骤 8：标签与版本标记

```powershell
git tag -a v0.1-baseline -m "working baseline before AI refactor"
git tag            # 查看标签
```

标签用于标记“可靠锚点”，如发布版（v1.0）、演练前基线。回滚时可以精确回到某个锚点。

## 6. AI 应生成的产物

本章 AI 的产出被刻意限定为代码改动，而非文档。你应该得到：

1. 只涉及声明范围内文件的修改。
2. 一段对改动点的自然语言说明（函数级别）。
3. （可选）针对新排序行为的 pytest 用例建议。

**AI 不应生成的东西**：范围外文件的改动、依赖变更、对既有函数签名的重命名。一旦出现，回到步骤 6 恢复后重新下任务。这份“预期产出清单”本身就是你审查 AI 的依据。

## 7. 人工检查点

1. `git log --oneline`：历史是否清晰，每条是否单一目的？
2. `git diff --stat`：改动文件数与 AI 声称是否一致？
3. 逐行读 Diff：有没有“看起来合理但你说不清为什么”的改动？说不清就问 AI，或直接恢复。
4. `.gitignore` 生效：`git status` 里不应出现 `.venv/`、`data/`。
5. 分支实验：在分支上随意改坏文件，`git switch main` 后确认 `main` 干净无损。

## 8. 验收命令与通过标准

```powershell
git log --oneline          # ≥3 条历史，含基线与功能提交
git status                 # 工作区干净（除未跟踪的运行产物）
git tag                    # 至少 1 个标注锚点
git restore --staged . && git restore .   # 演练后可随时清空工作区
```

通过标准：执行上述命令无报错；你能口头回答“恢复文件和回滚提交分别用什么命令、影响什么范围”。

## 9. 常见失败及恢复方法

**症状 1：`git add .` 把 `.venv/`、`data/` 全暂存了。**
原因：`.gitignore` 缺失或规则拼写错误。
恢复：`git restore --staged .` 清空暂存区；修正 `.gitignore` 后重新 add。若已提交，`git rm -r --cached .venv` 并提交一条 `.gitignore` 修正。

**症状 2：AI 改了范围外文件，Diff 混乱看不清。**
原因：任务约束不严或 AI 自作主张扩大范围。
恢复：`git restore .` 整体恢复后，把任务改写为更硬的范围约束（“只允许修改这两个文件，逐文件列出改动”），重新生成；每轮用 `git diff --stat` 先看文件数再读内容。

**症状 3：误用 `git reset --hard` 丢了未提交的修改。**
原因：reset --hard 会抹掉工作区改动。
恢复：未提交且被抹掉的改动 Git 原生不保；可尝试 `git fsck --lost-found` 找悬空对象（不保证成功）。预防：习惯用 `git stash`（临时收起）代替 reset --hard。

**症状 4：提交信息写错但已提交。**
原因：手误或信息无法反映改动。
恢复：未推送时 `git commit --amend -m "正确信息"`；已推送共享时不改历史，追加一条 `docs: correct commit message intent` 说明性提交。

**症状 5：分支上实验失败，想把整个分支扔掉。**
原因：实验性改动污染了分支。
恢复：`git switch main` 后 `git branch -D feat/xxx` 强删分支即可，`main` 不受影响。

## 10. 本章 Git 提交

建议分支与提交拆分（保持每条单一目的）：

```text
分支：main 直接操作（本章为基线建设）
chore: init repo with gitignore
feat: initial subscription tracker skeleton
docs: add note on ai collaboration baseline   （可选）
tag：v0.1-baseline
```

若在演练中产生可保留的排序功能，则在 `feat/due-reminder` 分支提交并合并：

```text
feat: sort subscriptions by renewal_date
```

## 11. 练习与扩展

1. 用 `git stash` 替代一次“恢复”操作，体会两者的差异。
2. 故意制造一次合并冲突（两个分支改同一行），手工解决并提交。
3. 给项目添加 `git status -s` + `git log --graph --oneline` 的日常检查习惯。
4. （进阶）了解 `git bisect`：当 AI 引入的 Bug 来源不明时，用二分法定位是哪条提交开始出问题。

## 12. 参考资料

- Pro Git（官方书，中文版免费）：https://git-scm.com/book/zh/v2
- Git 官方文档（restore/revert/reset）：https://git-scm.com/docs
- GitHub Docs：关于 Pull Request：https://docs.github.com/pull-requests
- ChiYu 铁人赛 Day 4（Git 与 GitHub 入门，中文）：https://huangchiyu.com/ChiYu-Blog/posts/2025ithomeironmanday4/

---

# 第 4 章　从想法到意图：先决定不做什么

> 本章成果：把“做一个订阅管理器”的一句话愿望，整理成可审查的意图文档、验收标准和范围边界。

## 1. 本章成果

完成本章后，项目中应新增两份文档：

```text
docs/intent.md
docs/acceptance.md
```

`docs/intent.md` 回答：

- 这个项目解决谁的什么问题？
- 第一版必须做到什么程度？
- 哪些问题明确不做？
- 有哪些假设、约束和风险？

`docs/acceptance.md` 回答：

- 怎样才算完成？
- 每个目标如何被观察、测试或手工验证？
- 哪些验收条件属于 `v0.1`、`v0.2`，哪些属于 `v1.0`？

本章不生成任何应用代码。目标是先建立人和 AI 共同遵守的决策边界，再进入第 5 章的规格设计。

## 2. 为什么需要它

AI 非常擅长把模糊需求迅速扩大成大量代码。只输入“做一个订阅管理网站，功能越完整越好”，很容易得到一个包含登录、支付接口、后台管理、消息通知甚至容器配置的项目。表面上代码很多，实际上真正需要的“记录金额、保存续费日期、下次还能继续维护”反而没有被验证。

Intent 不是需求规格，也不是实施计划，而是项目的第一层决策：

| 层级 | 回答的问题 | 本章位置 |
|---|---|---|
| Intent | 为什么做，做到什么程度，不做什么 | `docs/intent.md` |
| Spec | 系统应表现出哪些可验证行为 | 第 5 章 |
| Plan | 采用什么架构，怎样拆成任务 | 第 6 章 |
| Implementation | 代码、测试、CI 和发布产物 | 第 7—11 章 |

先写 Intent 的价值，是把“人的判断”固化成项目资产。之后 AI 生成规格、任务或代码时，都可以引用这些判断，而不是每次都从一句自然语言重新猜测。

## 3. 最少必备知识

- **目标**：项目要带来的可观察价值。
- **非目标**：第一版明确不处理的问题。写非目标不是减少价值，而是防止范围无限扩大。
- **假设**：当前未被验证、但会影响设计的判断。
- **约束**：技术、运行环境、法律、数据或成本方面的限制。
- **验收标准**：可被测试或人工检查的行为结果，而不是“界面美观”“代码整洁”这类主观评价。
- **完成定义**：一个版本除了功能本身，还需要哪些测试、文档、Git 记录和运行证据。

本章只需要使用 Markdown 文件和 Git，不要求掌握 Python、FastAPI 或数据库。

## 4. 起始项目状态

开始本章前，项目应已经完成第 3 章的 Git 基线：

```powershell
git status
git log --oneline -5
```

确认工作区没有未提交修改。新建文档分支：

```powershell
git switch -c docs/intent-and-acceptance
```

如果项目中还没有 `docs/` 目录，本章会创建它。暂时不需要创建 `app/`、`tests/` 或数据库文件。

## 5. 操作步骤与 AI 任务示例

### 5.1 先写十行原始想法

新建临时记录，不必讲究格式：

```text
我想做一个个人订阅管理器。
问题：视频会员、云服务、域名和工具的续费时间分散在邮件、浏览器收藏和支付记录里。
目标：在一个本地网页里记录订阅名称、金额、货币、下次续费日期和备注。
第一版只要自己用，不需要账号系统。
希望能看到所有订阅按续费日期排序，之后能编辑和删除。
后续希望能导出 CSV，用于备份和整理。
```

### 5.2 让 AI 只提问，不设计

使用下面的 AI 任务示例。重点是让 AI 暴露缺失信息，而不是立即给出技术栈。

```text
目标：帮我把 Subscription Tracker 的原始想法整理成 Intent 和验收标准。

上下文：
- 这是一个本地、单用户的个人订阅与续费管理器。
- 默认技术栈后续会讨论，本章只产出文档。
- 初始字段包括 name、amount、currency、renewal_date、note。
- 项目需要支持从 v0.1 到 v1.0 的渐进开发。

范围：
- 只讨论产品意图、用户价值、范围、非目标、假设、约束和风险。
- 只设计可观察验收标准。
- 不生成应用代码、数据库 Schema、API 设计或前端界面。

约束：
- 不要建议登录、支付、邮件抓取、自动提醒或多用户功能。
- 金额必须明确精度策略。
- 每条目标至少对应一条可验证结果。
- 输出使用简体中文 Markdown。

验收：
- Intent 覆盖背景、用户、目标、非目标、假设、约束、风险和版本范围。
- Acceptance 中每条标准都有明确操作、预期结果和所属版本。
- 不出现无法验证的主观描述。

输出：
1. 最多 8 个需要我确认的问题；
2. `docs/intent.md` 草稿；
3. `docs/acceptance.md` 草稿；
4. Intent 条目到验收条件的追踪表。
```

### 5.3 回答关键问题

AI 至少应该问到下面几类问题，你可以直接采用这些回答：

1. **是否允许多个用户使用？**  
   不。第一版是本地单用户，不设计账号、角色和权限。
2. **金额如何表示？**  
   使用“分”为单位的正整数，例如 `1200` 表示 12.00 元；不混用浮点数。
3. **货币支持哪些？**  
   第一版支持 `CNY` 和 `USD` 两种 ISO 4217 代码，不做汇率换算。
4. **续费日期是自动提醒日期还是人工记录？**  
   是用户手工记录的下次续费日期，不连接邮箱、日历或支付平台。
5. **删除是否需要撤销？**  
   第一版删除后立即生效，不设计回收站；数据安全依靠 Git、数据库备份和 CSV 导出。
6. **列表如何排序？**  
   按 `renewal_date` 升序，相同日期按 `id` 升序。

### 5.4 编写 `docs/intent.md`

下面是可直接复制并在自己项目中修改的示例：

```markdown
# Intent: 个人订阅与续费管理器

## 背景

个人订阅通常分散在邮件、浏览器收藏、支付记录和不同网站后台中。续费日期、金额和用途缺少统一记录，容易出现重复订阅、忘记取消或无法统计年度支出的问题。

## 用户

单人本地用户。用户会使用浏览器，能完成基本文件操作；不要求具备后端开发经验。

## 要解决的问题

1. 订阅信息分散，难以统一查看。
2. 金额、货币和续费日期缺少可靠记录。
3. 项目上线后仍需要持续修改、测试和维护。

## 产品目标

- G1：在一个本地网页中记录订阅。
- G2：查看按下次续费日期排序的订阅列表。
- G3：修改或删除已有订阅。
- G4：导出 CSV，用于备份和外部整理。
- G5：应用重启后数据仍然保留。

## 非目标

- N1：不做多用户、登录、注册和权限管理。
- N2：不自动抓取邮箱、日历、银行或支付平台数据。
- N3：不发送续费提醒邮件、短信或浏览器通知。
- N4：不做汇率换算和财务报表。
- N5：第一版不做移动端原生应用。

## 关键业务概念

- 订阅：一条需要定期付费的记录。
- 金额：以“分”为单位的正整数，避免浮点精度误差。
- 货币：ISO 4217 代码，第一版支持 `CNY` 和 `USD`。
- 续费日期：用户手工填写的下次续费日期，格式为 `YYYY-MM-DD`。
- 备注：可选说明，最多 500 个字符。

## 版本范围

- v0.1：添加、查看订阅，打通界面、API 和 SQLite。
- v0.2：修改、删除订阅，完成输入校验。
- v1.0：CSV 导出、测试、CI、部署和发布。

## 假设

- A1：数据保存在本机，单个 SQLite 文件足以满足第一版。
- A2：用户能接受手工输入续费日期。
- A3：浏览器访问 `http://127.0.0.1:8000` 是主要使用方式。

## 约束

- C1：默认技术栈为 Python 3.12+、FastAPI、SQLite、原生 HTML/CSS/JavaScript。
- C2：所有 API 以 `/api/subscriptions` 为核心入口，健康检查使用 `/health`。
- C3：文档、代码和测试保存在同一个 Git 仓库中。
- C4：不引入需要额外账号、密钥或付费服务的外部平台。

## 风险

- R1：金额如果用浮点数表示，可能出现精度误差。
- R2：需求容易扩展成自动提醒或多用户系统。
- R3：AI 可能为了“完整”生成大量与验收无关的模块。
- R4：文档如果与后续代码不同步，会变成误导性上下文。
```

### 5.5 编写 `docs/acceptance.md`

验收标准应描述外部可观察结果，而不是规定内部实现。例如“使用 FastAPI”是约束，“页面刷新后记录仍然存在”是验收。

````markdown
# Acceptance: 个人订阅与续费管理器

## 通用规则

- 每条验收标准都必须能被自动化测试或明确的手工步骤验证。
- 状态使用：未开始、进行中、已通过、已失败。
- 版本阶段使用：v0.1、v0.2、v1.0。

## 验收场景

### AC-01　添加有效订阅（v0.1）

Given 应用已启动，且当前没有任何订阅记录  
When 用户填写名称、金额、货币、续费日期和可选备注并提交  
Then 页面显示成功状态，列表中出现该订阅，并显示服务端生成的标识与创建时间

示例输入：

```json
{
  "name": "Example Cloud",
  "amount": 1200,
  "currency": "CNY",
  "renewal_date": "2027-01-15",
  "note": "个人存储空间"
}
```

### AC-02　拒绝无效输入（v0.2）

Given 用户正在创建或编辑订阅  
When 名称为空，金额为 0、负数或非整数，货币不是 `CNY`/`USD`，或续费日期不是有效日期  
Then 系统拒绝保存，给出可理解的错误原因，原有数据保持不变

### AC-03　按续费日期查看列表（v0.1）

Given 数据库中存在多条订阅记录  
When 用户打开订阅列表  
Then 记录按 `renewal_date` 升序显示；日期相同时按 `id` 升序显示

### AC-04　重启后保留数据（v0.1）

Given 已成功创建一条订阅  
When 停止并重新启动应用  
Then 该订阅仍然出现在列表中，字段值没有变化

### AC-05　修改订阅（v0.2）

Given 列表中存在一条订阅  
When 用户修改名称、金额、货币、续费日期或备注并保存  
Then 列表和后续查询均显示新值，未修改的记录不受影响

### AC-06　删除订阅（v0.2）

Given 列表中存在一条订阅  
When 用户确认删除该订阅  
Then 该记录从列表和后续导出结果中消失，其他记录保持不变

### AC-07　导出 CSV（v1.0）

Given 数据库中存在至少两条订阅记录  
When 用户请求 CSV 导出  
Then 得到一个 UTF-8 CSV 文件，每行包含一条订阅，字段顺序固定且可读

### AC-08　项目可重复验证（v1.0）

Given 一个干净的 Git 工作副本  
When 按 README 安装依赖、启动应用并运行测试  
Then 应用能够启动，测试全部通过，且核心验收场景可以被自动检查

## 追踪表

| Intent | Acceptance | 状态 |
|---|---|---|
| G1 记录订阅 | AC-01、AC-02、AC-04 | 未开始 |
| G2 查看列表 | AC-03 | 未开始 |
| G3 修改或删除 | AC-05、AC-06 | 未开始 |
| G4 导出 CSV | AC-07 | 未开始 |
| G5 可维护交付 | AC-08 | 未开始 |
````

### 5.6 让另一个 AI 会话独立审查

不要在生成文档的同一个会话里让 AI 评价“自己刚才写得很好”。开启新会话，只给它文档路径和审查任务：

```text
目标：审查 Subscription Tracker 的 Intent 和 Acceptance 是否足以支撑后续规格与实现。

上下文：
- 请阅读 `docs/intent.md` 和 `docs/acceptance.md`。
- 本项目是本地单用户应用，第一版不做登录、提醒、邮件抓取和汇率换算。

范围：
- 只审查文档一致性、可验证性和范围控制。
- 不修改文件，不生成代码，不提出新功能。

约束：
- 每条问题必须引用具体条目 ID 或标题。
- 按 blocker、major、minor 分级。
- 对无法验证的验收标准，给出可观察的改写建议。

验收：
- 找出 Intent 与 Acceptance 之间未覆盖或互相矛盾的地方。
- 判断金额、货币、日期和删除规则是否足够明确。
- 检查是否混入了第 5 章规格或第 6 章架构才需要决定的实现细节。

输出：
1. 问题清单；
2. 每个问题的修改建议；
3. 是否可以进入规格阶段的结论。
```

## 6. AI 应生成的产物

本章合理的 AI 产物包括：

- `docs/intent.md` 草稿；
- `docs/acceptance.md` 草稿；
- 最多 8 个澄清问题；
- Intent 到 Acceptance 的追踪表；
- 独立审查报告。

本章不应当生成：

- `app/` 下的 Python 代码；
- 数据库迁移脚本；
- 前端页面；
- CI 配置；
- 具体 API JSON Schema。

如果 AI 生成了上述内容，说明任务范围失控。保留有用文字，但不要提交无关代码。

## 7. 人工检查点

逐项检查：

1. **目标是否能对应验收？**  
   每个 `Gx` 至少出现在追踪表中一次；找不到验收条件的目标要么删除，要么补充可观察结果。
2. **非目标是否真的挡住范围？**  
   检查有没有出现登录、邮箱、自动提醒、支付、汇率、多设备同步等内容。
3. **金额规则是否唯一？**  
   全篇只能有一种表示方式。本项目采用“分为单位的正整数”，不能一会儿写 `12.00`，一会儿写 `1200` 且没有说明换算关系。
4. **验收是否可失败？**  
   “页面易用”无法失败；“无效日期提交后不保存记录，并显示错误原因”可以失败。
5. **阶段是否清楚？**  
   AC 条目必须标明 v0.1、v0.2 或 v1.0，避免第 7 章把全部功能一次塞进 Walking Skeleton。
6. **是否过早绑定实现？**  
   Intent 可以写默认技术栈作为项目约束，但不应规定函数名、类名、目录结构或具体库版本。

## 8. 验收命令与通过标准

运行：

```powershell
git status --short
git diff --check
git diff --name-only
```

通过标准：

- `git status --short` 只显示本章预期新增或修改的文档。
- `git diff --check` 没有报告行尾空格等基础格式问题。
- `docs/intent.md` 至少包含背景、用户、目标、非目标、假设、约束、风险和版本范围。
- `docs/acceptance.md` 至少包含 AC-01 到 AC-08，以及 Intent 到 Acceptance 的追踪表。
- 每条目标都能在追踪表中找到至少一条验收标准。
- 仓库中没有本章新增的应用源代码。

不要伪造命令输出。若工具尚未安装测试环境，本章的通过标准以文件内容和 Git 差异为准。

## 9. 常见失败及恢复方法

| 症状 | 原因 | 恢复动作 |
|---|---|---|
| AI 返回完整项目目录、Python 代码和 Dockerfile | 提示词只说“做项目”，没有限制“只产出文档” | 删除未提交的代码文件，重发只允许生成 `docs/intent.md` 和 `docs/acceptance.md` 的任务 |
| 需求不断增加邮箱抓取、自动提醒、多用户和支付对接 | 缺少非目标和范围边界 | 把新增内容移入“未来想法”，补写 N1—N5，并将当前版本目标收敛到 v0.1—v1.0 |
| 验收标准写成“界面美观、性能良好、代码健壮” | 把主观评价当作可验证结果 | 改写成具体操作和预期结果，例如“提交无效日期后列表记录数量不变，并显示错误原因” |
| 金额同时出现 `12.00`、`1200` 和 `decimal` | 没有固定业务精度规则 | 在 Intent 中明确“amount 为分单位正整数”，全文统一示例，并删除冲突表述 |
| 审查 AI 说“文档很好”，但没有引用任何条目 | 审查任务缺少输出约束，或上下文仍带着生成过程 | 开新会话，只提供文件内容和审查任务，要求输出 blocker/major/minor 与条目引用 |

如果文档已被错误内容污染，可以恢复分支起点：

```powershell
git status
git restore docs/intent.md docs/acceptance.md
```

只有在确认不需要保留当前修改时才执行恢复；必要时先复制一份草稿到项目外部。

## 10. 本章 Git 提交

建议分支：

```text
docs/intent-and-acceptance
```

建议提交拆分：

```powershell
git add docs/intent.md
git commit -m "docs: add subscription tracker intent"

git add docs/acceptance.md
git commit -m "docs: add measurable acceptance criteria"

git add docs/intent.md docs/acceptance.md
git commit -m "docs: trace goals to acceptance scenarios"
```

提交前检查：

```powershell
git diff --staged --stat
git diff --staged
```

不要把第 5 章的 API 规格或第 6 章的架构文件提前混入本分支。

## 11. 练习与扩展

1. **换领域练习**：把“订阅管理器”替换成“读书笔记管理器”，保留同样的 Intent 结构，检查非目标是否仍然有效。
2. **反向分析**：打开第 1 章的一次性原型，为它补写 Intent 和 Acceptance，找出它当初为什么会扩大范围。
3. **失败设计**：故意删除所有非目标，再让 AI 重新提出功能建议，记录范围膨胀的具体表现。
4. **团队练习**：两人分别独立写 Intent，再比较目标和验收差异；不要先讨论答案。
5. **进入规格前的小测验**：随机选择一条 Acceptance，回答“它将在哪个版本、用什么测试或手工步骤验证”。

## 12. 参考资料

- [欢迎来到未来（GSE 2026 第 1 讲）](https://jyywiki.cn/GSE/2026/lect1.md)
- [Lab1：个人数字助手（GSE 2026）](https://jyywiki.cn/GSE/2026/lab1.md)
- [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)
- [Beyond Vibe Coding: From Coder to AI-Era Developer](https://beyond.addy.ie/)
- [To vibe or not to vibe（Martin Fowler）](https://martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html)

---

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

---

# 第 6 章　最小架构、技术决策与任务拆分

> 本章成果：为订阅管理器写出 `ARCHITECTURE.md`、第一份 ADR、实施计划和任务列表——一份能直接指导 AI 编码的完整蓝图。

## 1. 本章成果

1. 你能画出项目的模块边界和数据流向，并固化为 `ARCHITECTURE.md`。
2. 你用 ADR 记录了至少一个技术选择及其理由。
3. 你把规格拆成了带验证方法的任务清单。
4. 你理解纵向切片（Walking Skeleton）：先打通一条最细的完整链路，而不是横向铺满每层。

## 2. 为什么需要它

规格回答“做什么”，架构与计划回答“怎么做、按什么顺序做”。没有这一层，AI 会用自己的默认品味替你做几十个隐含决策：目录结构、分层方式、错误处理风格——每个决策单看都合理，合起来却常常互相冲突。写出最小架构的本质，是把**你**的决策显式化，把**AI 的自由度**收窄到实现细节上。同时，任务拆分质量直接决定后续 AI 协作质量：任务越大，Diff 越大，人工审查越不可行；任务越小，每一步都可独立验证、可独立提交。

## 3. 最少必备知识

- **模块边界**：职责的分界线。边界清晰的系统，一次需求变化只需要改少数模块。
- **依赖方向**：谁引用谁。单向依赖（routes → repository → database）比双向纠缠好维护。
- **ADR（架构决策记录）**：轻量文档，记录“当时为什么这么选”，防止三个月后忘记或无谓返工。
- **纵向切片 / Walking Skeleton**：先实现一条端到端的最小功能路径（界面→API→数据库→界面），验证整体结构，再逐个功能横向加宽。
- **技术选型的约束链**：需求约束选型，而不是选型反过来重塑需求。
- **任务的可验证性**：每个任务必须能说出“怎么算完成、用什么命令验证”。

## 4. 起始项目状态

已完成：意图（`docs/intent.md`）、规格（`specs/subscription-manager/`）。项目还没有代码骨架。本章产出的计划与架构，是第 7 章编码的直接输入。

## 5. 操作步骤与 AI 任务示例

### 步骤 1：确定最小架构

订阅管理器的三层结构（保持刻意简单，拒绝过早引入框架）：

```text
界面层  app/static/          原生 HTML/JS，只做展示与表单
接口层  app/routes.py        参数校验、响应组装（不写 SQL）
数据层  app/repository.py    SQL 与行映射（不写业务规则）
公共    app/schemas.py       Pydantic 模型，字段唯一权威定义
        app/database.py      连接与建表
```

依赖方向单向：`routes → repository → database`；`schemas` 被引用但不反向依赖任何层。画在纸上或用 Mermaid 均可——先自己画，再让 AI 复核，而不是让 AI 从零发明。

### 步骤 2：AI 任务——架构评审

**给 AI 的任务示例（text 块）**：

```text
目标：评审我给出的最小架构是否足以支撑规格中的全部场景。
上下文：规格见 specs/subscription-manager/spec.md（你先读取）；架构描述如下——
  routes.py 只做校验与响应；repository.py 只做 SQL 与行映射；
  schemas.py 为字段唯一权威定义；database.py 负责连接与建表；
  依赖方向 routes → repository → database，单向。
范围：只评审架构，不写实现代码。
约束：如指出问题，必须同时给出最小修改方案；不允许建议引入新框架或新依赖，除非指出规格中明确需要而当前架构无法满足的能力。
验收：输出“结论 + 问题清单（每条附证据与修改建议）”；若无问题，明确说“无阻塞问题”。
输出：Markdown，不超过 600 字。
```

注意这个任务的克制设计：限定“只评审不写码”、禁止随手引依赖、要求结论可核对。这正是本章教你的思维方式。

### 步骤 3：写 ARCHITECTURE.md

在仓库根目录创建（内容以你评审后的架构为准）：

```markdown
# ARCHITECTURE

订阅管理器为单体三层架构：静态前端 + FastAPI 接口层 + SQLite 数据层。

## 模块与依赖方向

routes → repository → database；schemas 被引用，不反向依赖。
（附模块图：界面 → routes → repository → database）

## 边界规则

- routes.py 不出现 SQL；repository.py 不出现业务规则；两者通过 schemas 传递数据。
- 业务规则（校验、到期计算）集中在 schemas/repository；界面只展示。
- docs/generated/ 为机器产物，禁止手改。

## 禁止事项

- 不引入前端构建链；不加 ORM（当前规模用 sqlite3 原生）；不做微服务拆分。
```

### 步骤 4：写第一份 ADR

以“数据存储选 SQLite 还是 Postgres”为例，使用 `templates/adr.md` 模板填写。核心是**候选方案表**与**负面后果**：SQLite 的缺点（并发写弱、不适合多机）要如实写，并给出“何时重估”条件（如用户数 > 10 或需要跨机共享时重新评估）。再补一条 ADR-0002：“金额以整数分存储”——记录避免浮点误差的理由。

### 步骤 5：AI 任务——从规格生成任务清单初稿

**给 AI 的任务示例（text 块）**：

```text
目标：依据 specs/subscription-manager/spec.md 生成任务清单初稿。
范围：只输出任务表，不写代码。
约束：
  1. 每个任务工作量 ≤ 半天，且能独立验证；
  2. 第一个任务必须是“最小纵向切片”（界面→API→数据库打通一条记录的添加与展示）；
  3. 每个任务必须包含验证方法（命令或手工步骤）；
  4. 任务间依赖显式列出；
  5. 使用 templates/tasks.md 的表格列（ID/任务/依赖/状态/验证方法/完成条件）。
验收：任务并集覆盖规格全部验收场景 A—E，无遗漏；无“实现全部功能”这类不可验证的大任务。
输出：Markdown 表格 + 一段“覆盖性自检”说明。
```

### 步骤 6：人工修剪任务清单

AI 的初稿常见问题：任务粒度不均、漏掉“冒烟验证”类任务、把前后端改动塞进一个任务。逐条修剪，直到每个任务满足三个标准：**单一目的、独立可验证、半天内可完成**。修剪后的清单存入 `docs/tasks.md`。

### 步骤 7：确定实施顺序

按纵向切片原则排布：T1 骨架与 `/health` → T2 建表 → T3 添加订阅（界面→API→库）→ T4 查看列表 → 后续才是修改/删除/校验/导出。**先把“添加并查看”这一条最细的链路跑通，是第 7 章的全部内容。**

## 6. AI 应生成的产物

1. 架构评审结论（问题清单或“无阻塞”）。
2. 任务清单初稿（Markdown 表格）＋覆盖性自检。
3. （可选）Mermaid 架构图初稿，供你修订后收录。

**人工产物**（AI 不代劳）：`ARCHITECTURE.md` 最终版、`ADR-0001`、`ADR-0002`、修剪后的 `docs/plan.md` 与 `docs/tasks.md`。架构与决策是人的责任域，AI 只做评审与草稿。

## 7. 人工检查点

1. 依赖方向是否单向？在 `ARCHITECTURE.md` 里能否一眼看出“谁引用谁”。
2. 每条 ADR 是否包含**负面后果**？只有优点的 ADR 是无效的。
3. 任务清单是否覆盖规格场景 A—E？拿规格逐场景对照。
4. 每个任务的“验证方法”是否真的可执行（命令能否直接粘贴运行）？
5. 有没有为“不做的事”立字据？（禁止事项 + 非目标双重确认）

## 8. 验收命令与通过标准

```powershell
# 文件存在且非空
Get-ChildItem ARCHITECTURE.md, docs/plan.md, docs/tasks.md, docs/decisions/ADR-0001.md

# 内容抽检：禁止事项、依赖方向、任务验证方法均存在
Select-String -Path ARCHITECTURE.md -Pattern "依赖方向|禁止"
Select-String -Path docs/tasks.md -Pattern "验证方法"
```

通过标准：文件齐备；任务表无空“验证方法”；ADR 含候选方案与重估条件；你能对第三人讲清“为什么选 SQLite、什么情况下换”。

## 9. 常见失败及恢复方法

**症状 1：AI 生成的架构建议引入了重框架（Django、微服务、K8s）。**
原因：模型默认倾向“完整方案”，未受规模约束。
恢复：在任务中显式声明“禁止引入新依赖/框架，当前规模为单人本地工具”；对已有产出，只采纳其中符合最小原则的部分，其余丢弃。

**症状 2：任务清单里有“实现全部后端”这类巨石任务。**
原因：AI 未按半天粒度拆分。
恢复：把巨石任务按“可独立验证的最小行为”二次拆分；每拆出一个，问自己“这条怎么验证？”答不出就继续拆。

**症状 3：任务覆盖遗漏（如场景 E 到期提醒没任务）。**
原因：AI 按印象生成而非对照规格。
恢复：把验收场景编号逐条映射到任务 ID（补一列“对应场景”），缺口立现；该映射保留在 `docs/tasks.md` 头部。

**症状 4：ADR 只写结论不写理由。**
原因：把 ADR 当表单填。
恢复：自问三个问题——“当时还有哪些选项？”“为什么放弃它们？”“什么情况发生时应该重新评估？”答全再定稿。

**症状 5：ARCHITECTURE.md 与后续代码漂移。**
原因：文档一次性生成，无人维护。
恢复：在本章就写上“改动架构必须同步改本文档”的规则进 `AGENTS.md`；第 10 章会给出文档漂移检查的固定动作。

## 10. 本章 Git 提交

```text
分支：docs/architecture
docs: add architecture and boundary rules          （ARCHITECTURE.md）
docs: record adr-0001 storage and adr-0002 money   （docs/decisions/）
docs: add implementation plan and task breakdown   （docs/plan.md, docs/tasks.md）
```

三个提交对应三种用途不同的文档；合并回 `main` 后，这份蓝图就是第 7 章的起点。

## 11. 练习与扩展

1. 为“前端不引入构建链”再写一条 ADR，练习把负面后果写具体。
2. 把你的任务清单交给另一个 AI 会话做“覆盖性挑战”，让它专找漏掉的场景。
3. （进阶）阅读 Spec Kit 的 `/speckit.plan` 设计，对比本章手工做法的差异：https://github.com/github/spec-kit
4. 用同一方法为你的下一个真实项目做一次蓝图，体会哪些格子仍然填不出来。

## 12. 参考资料

- Spec Kit（规格驱动的官方流程，本章任务拆分思想与之同源）：https://github.com/github/spec-kit
- OpenSpec（轻量替代，写清 change 的 propose/verify/archive）：https://github.com/Fission-AI/OpenSpec
- ADR 常见格式（Michael Nygard 原始形态）：https://github.com/joelparkerhenderson/architecture-decision-record
- The Pragmatic Engineer 关于 Walking Skeleton 的讨论与引用：httpsmartfowler 之外的通俗介绍可先读：https://en.wikipedia.org/wiki/Walking_skeleton
- Vibe Coding Guide（中文，工作流章节与本章计划/任务思想一致）：https://github.com/Lling0000/Vibe_coding_guide

---

# 综合实验二：不写代码，完成项目蓝图

> 实验成果：在不写一行实现代码的前提下，完成订阅管理器的意图、规格、架构、ADR、计划、任务清单，并通过三轮评审。

## 实验目标

证明一个结论：**代码之前的工作决定项目成败的八成。** 本实验全部产出是文档，全部评审是“能否指导编码”。

## 前置条件

- 已完成第 4—6 章阅读；`templates/` 下模板可用。
- 两个独立的 AI 会话（A：协作撰写；B：只做评审，不共享 A 的对话记忆）。

## 产出清单

| 产物 | 来源模板 | 存放位置 |
|---|---|---|
| 项目意图 | `templates/intent.md` | `docs/intent.md` |
| 功能规格 | `templates/spec.md` | `specs/subscription-manager/spec.md` |
| 架构说明 | 第 6 章步骤 3 | `ARCHITECTURE.md` |
| 两条 ADR | `templates/adr.md` | `docs/decisions/` |
| 实施计划 | `templates/plan.md` | `docs/plan.md` |
| 任务清单 | `templates/tasks.md` | `docs/tasks.md` |

## 步骤

### 第一轮：用会话 A 起草（60 分钟）

按 intent → spec → 架构 → ADR → plan → tasks 的顺序填写模板。每份文档完成即存盘，不追求完美，追求“格子填满、每条可验证”。AI 只做起草与追问（让它列出你没回答的问题），**决策由你做**。

### 第二轮：用会话 B 交叉评审（30 分钟）

把 6 份文档交给会话 B，评审指令：

**给会话 B 的任务示例（text 块）**：

```text
目标：评审一份“未写代码的项目蓝图”，判断它是否足以指导编码。
材料：意图/规格/架构/ADR/计划/任务清单共 6 份（随附）。
评审视角：
  1. 一致性：任务清单是否覆盖规格全部场景？规格与意图是否冲突？
  2. 可验证性：每个成功标准与任务是否有可执行验证方法？
  3. 规模约束：是否存在不必要的复杂度（重框架、过早优化）？
  4. 盲区：有没有“没人能回答”的含糊表述？
约束：只评审不重写；每条意见给出证据（引用原文）；区分“阻塞级”与“建议级”。
验收：输出问题清单（≤10 条，按严重度排序）；结尾给“可进入编码 / 需修改后再审”的明确结论。
```

### 第三轮：修复与终审（30 分钟）

会话 A 逐条处理阻塞级问题（建议级自行取舍），然后回答三个终审问题：

1. 把任务清单交给一个**从没读过本教程**的新 AI 会话，它能直接开工吗？
2. 拿规格场景 E（到期提醒）追问：“第一个实现它的任务叫什么、怎么验证？”能秒答吗？
3. 有没有任何一条文档依赖“我们俩聊过的其他内容”？（蓝图必须自包含）

### 第四轮：归档与提交

```powershell
git switch -c docs/blueprint
git add docs/ specs/ ARCHITECTURE.md
git commit -m "docs: project blueprint v0.1 (intent, spec, architecture, plan, tasks)"
git switch main && git merge --no-ff docs/blueprint
git tag -a v0-blueprint -m "blueprint reviewed and frozen"
```

## 自检表

| # | 检查项 | 通过标准 |
|---|---|---|
| 1 | 非目标清单存在且与目标无冲突 | 每条非目标可追溯到“为什么不做的理由” |
| 2 | 每条验收场景有 Given/When/Then | 场景可直接翻译成 pytest |
| 3 | 数据表字段与 API 契约一致 | 字段名/类型逐一对得上 |
| 4 | 架构依赖方向单向 | 图上看不出双向箭头 |
| 5 | 每条 ADR 有负面后果与重估条件 | 只写优点的 ADR 视为未完成 |
| 6 | 任务 ≤ 半天且含验证方法 | 无“实现全部功能”式巨石任务 |
| 7 | 任务并集覆盖场景 A—E | 对照表无空缺 |
| 8 | 蓝图自包含 | 新会话仅凭仓库即可开工 |
| 9 | 会话 B 结论为“可进入编码” | 阻塞级问题数为 0 |
| 10 | 版本标签已打 | `git tag` 可见 v0-blueprint |

## 常见失败与恢复

**失败 1：直接让 AI“帮我规划整个项目”，产出华丽但空洞。**
恢复：回到模板逐格填；AI 的角色是追问与起草，不是代答。空泛段落整段删除重写。

**失败 2：会话 B 一味奉承“很好，可以开始”。**
恢复：评审指令加“必须找出至少 3 个问题，否则视为评审无效”；或换更苛刻的措辞重发。

**失败 3：蓝图越写越大，陷入过度设计。**
恢复：对照“禁止事项/非目标”砍掉；凡是“将来可能需要”的一律进待办池不进本版。

**失败 4：任务清单与规格场景对不上号。**
恢复：在 tasks.md 头部建“场景↔任务”映射列，缺口强制补任务或改规格（改规格需升版本号）。

**失败 5：文档间术语不一致（“记录/条目/订阅”混用）。**
恢复：统一术语表（`appendices/D-glossary.md`），全局替换后重审。

## 完成标准

- 6 份产出齐备且入库；自检表 10/10 通过；会话 B 结论“可进入编码”；标签 `v0-blueprint` 已存在。

## 下一步

进入第 7 章：拿着这份蓝图开始纵向切片编码。

---

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

---

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

---

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

---

# 第 10 章　上下文工程：让 AI 在新会话中也能接手项目

> 本章成果：为 Subscription Tracker 建立项目地图、AGENTS.md、交接记录和一条架构决策，使一个没有历史记忆的新 AI 会话能接手一个明确的小任务。

## 1. 本章成果

完成本章后，你的项目应该具备下面五项可交接资产：

1. `docs/project-map.md`：告诉 AI“当前代码在哪里、请求如何流动、测试放在哪里”。
2. `AGENTS.md`：告诉 AI 安装、运行、检查命令和项目边界。
3. `docs/handoff.md`：告诉下一个会话“当前做到哪里、下一步做什么、哪些证据已经存在”。
4. `docs/decisions/ADR-0002-agent-context-files.md`：记录为什么采用分层上下文文件，而不是不断堆长提示词。
5. 一次真实的新会话接手实验：新 AI 只读取指定文件，完成一个小任务，并由你独立验收。

本章的重点不是让 AI“记住更多”，而是让它**每次只拿到当前任务需要的高信号上下文**。

## 2. 为什么需要它

前面几章中，你和 AI 可能一直在同一个会话里工作。这个会话确实知道很多历史：你解释过需求、AI 修改过哪些文件、哪些命令失败过、哪些方案被否决。但会话历史有两个问题：

1. 它不可移植。换一个模型、工具、设备或同事，这些历史就消失了。
2. 它不是越多越好。长上下文会混入大量已经过时的工具输出、错误尝试和中间讨论，后续任务反而更容易抓错重点。

上下文工程要解决的是第二个问题：不是把所有资料塞给模型，而是决定**当前任务应该看到哪些资料、以什么顺序看到、哪些内容只放指针而不展开**。一个项目地图、一份短小的 AGENTS.md、一次明确交接，通常比复制整个仓库更有效。

`AGENTS.md` 的公开格式说明也强调，它是“README for agents”：面向代理的稳定入口，记录安装、测试、代码风格和项目约定，而不是把所有人类文档重复一遍。

## 3. 最少必备知识

开始本章前，理解下面几个概念即可：

- **上下文**：模型当前能看到的文件、命令输出、规格、历史和用户指令。
- **上下文腐化（context rot）**：上下文越长，模型越容易忽略或混淆其中真正重要的信息。
- **渐进披露**：入口文件只放稳定摘要和指针，细节资料按需读取。
- **项目地图**：用一页纸说明代码入口、数据流、职责边界和验证位置。
- **交接记录**：给下一个会话的任务包，而不是流水账。
- **ADR**：Architecture Decision Record，记录“为什么这样选”的短文档。

## 4. 起始项目状态

本章假设你已经完成第 9 章：项目有测试，CSV 导出功能可运行；如果 CSV 导出尚不存在，先完成第 9 章，不要在本章临时补功能。

建议从当前主分支创建文档分支：

```powershell
git switch -c docs/context-engineering
git status --short
```

开始前应确认下列命令在你的环境中可运行：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m ruff check .
python -m uvicorn app.main:app --reload
```

本章会新增或整理这些文件：

```text
AGENTS.md
docs/project-map.md
docs/handoff.md
docs/decisions/ADR-0002-agent-context-files.md
```

## 5. 操作步骤与 AI 任务示例

### 5.1 生成项目地图草案

先让 AI 根据当前仓库生成一份项目地图草案，但要求它只写当前真实存在的内容。

```text
目标：为 Subscription Tracker 生成 docs/project-map.md 草案。
上下文：只读取 README.md、ARCHITECTURE.md、docs/intent.md、docs/acceptance.md、specs/subscription-tracker/spec.md、app/main.py、app/routes.py、app/database.py、app/repository.py、app/schemas.py、tests/test_api.py、tests/test_repository.py。
范围：只创建或修改 docs/project-map.md。
约束：
1. 不得修改源代码、测试或规格。
2. 不得写入当前仓库中不存在的文件或功能。
3. 不超过 80 行。
4. 对不确定的内容写 TODO，不要猜测。
5. 使用文件路径说明职责，不复制大段代码。
验收：入口、请求路径、数据访问、测试、规格和文档指针均能与当前仓库对应。
输出：project-map.md 草案，以及需要人工确认的问题列表。
```

得到草案后，人工补充“为什么这样分层”，删除 AI 猜测的内容。下面是一个可以采用的完整示例：

```markdown
# Subscription Tracker Project Map

Last reviewed: <YYYY-MM-DD>

## 1. Entry points

- `app/main.py`: creates the FastAPI app, registers routes, mounts static files, and exposes `/health`.
- `python -m uvicorn app.main:app --reload`: local development command.

## 2. Request flow

`app/static/app.js`
→ `GET|POST|PUT|DELETE /api/subscriptions`
→ `app/routes.py`
→ `app/schemas.py`
→ `app/repository.py`
→ SQLite through `app/database.py`

## 3. Responsibilities

- `app/routes.py`: HTTP request handling, status codes, error responses.
- `app/schemas.py`: request/response field names, types, and validation rules.
- `app/repository.py`: subscription CRUD and CSV export data retrieval.
- `app/database.py`: SQLite connection and schema initialization.
- `app/static/`: browser UI; must not access the database directly.

## 4. Current data contract

Subscription fields: `id`, `name`, `amount`, `currency`, `renewal_date`, `note`, `created_at`.
`amount` is an integer in currency minor units, such as cents.
`renewal_date` uses `YYYY-MM-DD`.

## 5. Verification

- `python -m pytest -q`
- `python -m ruff check .`
- CSV export is exercised through `/api/subscriptions/export`.

## 6. Documents to read first

1. `docs/intent.md`
2. `docs/acceptance.md`
3. `specs/subscription-tracker/spec.md`
4. `ARCHITECTURE.md`
5. `docs/decisions/`
```

### 5.2 编写简洁的 AGENTS.md

`AGENTS.md` 是代理进入仓库时的稳定入口，但不应变成百科全书。它记录“每次都需要知道的内容”和“去哪里找详情”。下面是一个完整但简洁的示例：

```markdown
# AGENTS.md

## Project overview

Subscription Tracker is a local-first personal subscription and renewal manager. It uses Python 3.12+, FastAPI, SQLite, and plain HTML/CSS/JavaScript.

## Setup commands

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## Verification commands

Run these commands before reporting completion:

```powershell
python -m pytest -q
python -m ruff check .
```

Do not treat your own explanation as verification. Include the commands you actually ran and their result status.

## Core API contracts

- Health endpoint: `GET /health`
- Subscription collection: `/api/subscriptions`
- CSV export: `GET /api/subscriptions/export`
- Subscription fields: `id`, `name`, `amount`, `currency`, `renewal_date`, `note`, `created_at`
- `amount` must be an integer in currency minor units, not a floating-point currency value.
- `renewal_date` must use `YYYY-MM-DD`.

## Architecture boundaries

- `app/routes.py` adapts HTTP requests and responses.
- `app/schemas.py` validates API data contracts.
- `app/repository.py` owns database queries and result shaping.
- `app/database.py` owns SQLite connection and schema setup.
- `app/static/` contains browser assets and may only call the public API.
- `tests/` contains API and repository verification.

## Change rules

1. Complete one task at a time.
2. Read `docs/intent.md`, `docs/acceptance.md`, and the relevant specification before editing.
3. Do not modify unrelated files, dependencies, formatting, or documentation.
4. Do not add a dependency without an explicit task and an ADR.
5. Update tests when behavior changes.
6. Do not commit secrets, tokens, database files, or personal subscription data.
7. Preserve backward compatibility of existing API fields unless the task explicitly requests a migration.

## Document pointers

- `docs/project-map.md`: current code and data flow.
- `ARCHITECTURE.md`: module boundaries and constraints.
- `docs/handoff.md`: current state and next task.
- `docs/decisions/`: accepted and proposed architecture decisions.
- `docs/runbooks/`: operational procedures.
```

### 5.3 记录为什么这样设计上下文

新增 ADR，示例如下：

```markdown
# ADR-0002: Use layered project context instead of long prompts

- Status: Accepted
- Date: <YYYY-MM-DD>
- Decision owner: <your name>

## Context

Subscription Tracker is maintained through repeated AI sessions. Session history cannot be relied on as project memory, and copying large amounts of code into prompts increases noise and makes important constraints easier to miss.

## Options considered

1. Keep all instructions in one long prompt.
2. Keep documentation only in human-oriented README files.
3. Use a layered context system: short AGENTS.md, project map, specifications, ADRs, and handoff notes.

## Decision

Adopt option 3. AGENTS.md remains the stable entry point and command reference. Project-specific details stay in specs, docs, tests, and code. Each new task receives a handoff packet that lists only the files needed for that task.

## Consequences

- Benefits: context is portable across tools and sessions; important commands are discoverable; task-specific files can be loaded on demand.
- Costs: documents must be reviewed when architecture changes; stale pointers are possible.
- Mitigation: treat project-map.md and AGENTS.md as living files, and update them in the same PR that changes the related contract.

## Verification

A fresh AI session can complete a small documented task after reading only the pointer files and task-specific sources.
```

### 5.4 写交接记录，而不是流水账

交接记录应让下一个会话知道“从哪里继续”。下面是一个完整模板，所有尖括号都必须替换：

```markdown
# Handoff: CSV export test coverage review

- Updated: <YYYY-MM-DD HH:mm>
- Author: <your name or agent name>
- Base commit: <git-commit-sha>
- Branch: docs/context-engineering
- Environment: Windows PowerShell / Python 3.12 / Subscription Tracker

## Current verified state

- `python -m pytest -q`: <PASS|FAIL, command output summary>
- `python -m ruff check .`: <PASS|FAIL>
- CSV export route exercised by: <tests/test_api.py::test_name>
- Known limitations: <none or list>

## Next task

Check whether CSV export tests cover all of the following cases:

1. Chinese subscription name.
2. `note` containing a comma.
3. Empty `note`.
4. `amount` as an integer in minor units.

If a case is already covered, report the test file and test name. If a case is missing, add only the missing test to `tests/test_api.py`. Do not change implementation code in this task.

## Required context

Read these files first:

1. `AGENTS.md`
2. `docs/project-map.md`
3. `docs/acceptance.md`
4. `app/routes.py`
5. `tests/test_api.py`

## Constraints

- Modify at most `tests/test_api.py`.
- Do not refactor unrelated tests.
- Do not change the CSV endpoint or repository code.
- Run targeted tests, then full tests.

## Done definition

- Report each required case and whether it was already covered.
- Add missing tests without changing implementation.
- Provide commands run and result status.
- Leave the working tree with only expected test-file changes.
```

### 5.5 新会话接手实验

先确认工作树干净，再开始实验：

```powershell
git status --short
git diff --stat
```

打开一个**全新的 AI 会话**，不要粘贴之前的聊天记录。使用下面这个任务：

```text
请读取当前仓库中的 AGENTS.md、docs/project-map.md、docs/handoff.md、docs/acceptance.md、app/routes.py、tests/test_api.py。不要读取整个仓库。

任务：检查 GET /api/subscriptions/export 是否已经覆盖以下 CSV 场景：
1. 中文订阅名；
2. note 包含英文逗号；
3. note 为空；
4. amount 为整数分单位。

规则：
- 如果某个场景已有测试，只报告测试文件、测试函数和对应场景。
- 如果某个场景缺失，只修改 tests/test_api.py，补充缺失测试。
- 不修改实现代码、规格、AGENTS.md 或其他文档。
- 不重排无关代码。
- 运行 python -m pytest -q tests/test_api.py，再运行 python -m pytest -q。
- 最后报告修改文件、每个测试目的、命令结果和仍未解决的问题。
```

这个实验的关键不是 AI 能否写出测试，而是：**它是否没有依赖你的记忆，也能从仓库中的文档找到边界和验证方式。**

## 6. AI 应生成的产物

本章结束后，仓库中至少应出现或更新：

```text
AGENTS.md
docs/project-map.md
docs/handoff.md
docs/decisions/ADR-0002-agent-context-files.md
tests/test_api.py   # 仅在 CSV 测试确有缺口时由新会话修改
```

新会话还应返回一份文字报告，包含：

- 它实际读取了哪些文件；
- 四个 CSV 场景中哪些已有覆盖；
- 新增或修改的测试；
- 运行的命令；
- 是否遇到文档缺失、路径错误或命令失败。

## 7. 人工检查点

检查这些文件时，不要只看“有没有写”，而要检查它们是否真的能指导下一个会话：

- `AGENTS.md` 是否足够短？它应主要包含命令、边界和指针，而不是复制规格。
- 其中每一条命令是否都能在干净环境中运行？
- `docs/project-map.md` 是否只列出当前存在的文件？
- 是否存在 AI 猜测出来的模块、接口或“计划中的文件”？
- `docs/handoff.md` 是否还有未替换的 `<placeholder>`？
- 交接记录是否包含证据，而不是“已完成”“看起来没问题”这类空话？
- ADR 是否写了被否决的选项和代价，而不只是结论？
- 新会话是否询问了仓库里已经写明的问题？如果是，说明入口文档或指针不够清楚。
- 新会话是否修改了任务范围之外的文件？用 `git diff --stat` 检查。

## 8. 验收命令与通过标准

运行以下命令：

```powershell
git status --short
git diff --stat
git diff --check
python -m pytest -q
python -m ruff check .
```

通过标准：

1. 新增或修改文件只包含本章预期文档，以及确有必要的新增测试。
2. `git diff --check` 没有空白错误。
3. 测试命令没有失败项；具体数量以你的项目为准，不要照抄教程中的数字。
4. Ruff 没有未处理错误。
5. `AGENTS.md` 中的安装、运行、测试、检查命令均实际存在且可执行。
6. `docs/project-map.md` 中每个路径都能在仓库中找到。
7. `docs/handoff.md` 中没有残留尖括号占位符。
8. 新会话只读取指定文件即可完成或准确报告任务，不需要你重新解释项目背景。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| `AGENTS.md` 越来越长，AI 仍然漏掉关键约束 | 把规格、决策历史和全部代码说明塞进入口文件 | 将详情移回 `specs/`、`docs/decisions/` 和 `ARCHITECTURE.md`，`AGENTS.md` 只保留稳定命令、边界和指针 |
| 新会话反复询问项目结构或测试命令 | 项目地图缺少入口，或 AGENTS.md 没有给出验证命令 | 补充 `docs/project-map.md` 的请求流和验证命令，再重开一次会话验证 |
| 新会话修改了实现代码、规格或无关测试 | 交接任务范围不够明确 | 在 handoff 中写明“允许修改的文件”“禁止修改的文件”和“完成定义”，重新开始任务 |
| 文档声称已有功能，但代码中找不到 | AI 根据历史讨论猜测了项目状态 | 以当前代码和测试结果为准；删除不存在的内容，并把“不确定”明确写成 TODO |
| 长会话后半段 AI 开始重复错误建议 | 上下文混入大量过时工具输出和中间尝试 | 停止当前会话，写 handoff，开新会话，只带必要文件和任务约束 |
| 交接记录只有“完成了 CSV 功能” | 缺少证据，下一个会话无法判断当前状态 | 补充基线 commit、运行命令、结果状态、已知限制和下一步任务 |

## 10. 本章 Git 提交

建议分支：

```powershell
git switch -c docs/context-engineering
```

建议拆分：

```powershell
git add AGENTS.md docs/project-map.md
git commit -m "docs: add agent entry point and project map"

git add docs/decisions/ADR-0002-agent-context-files.md
git commit -m "docs: record layered agent context decision"

git add docs/handoff.md
git commit -m "docs: add fresh-session handoff packet"

git add tests/test_api.py
git commit -m "test: cover csv export edge cases"
```

最后一个提交只应出现在新会话确实补充了测试时。不要把文档整理、测试补充和实现变更混在同一个提交中。

## 11. 练习与扩展

1. **上下文预算实验**：分别让 AI“读取整个仓库”和“只读取项目地图指定的文件”完成同一个任务，比较修改范围、提问次数和最终结果。
2. **交接质量实验**：故意写一份缺少命令和证据的 handoff，观察新会话是否会猜测；再补全后重做。
3. **文档漂移检查**：写一个脚本，检查 `docs/project-map.md` 中列出的路径是否都存在。
4. **嵌套上下文**：如果以后加入独立前端目录，可尝试在该目录放置更具体的 `AGENTS.md`，并观察代理是否优先使用离被修改文件最近的说明。
5. **稳定规则检查化**：把“routes 不得直接写 SQL”“static 不得访问数据库”这类边界规则转化为测试或静态检查，而不是只依赖文档提醒。

## 12. 参考资料

- [Effective context engineering for AI agents - Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
- [AGENTS.md](https://agents.md/)
- [Architecture Decision Records - GitHub](https://github.com/joelparkerhenderson/architecture-decision-record)
- [Git diff documentation](https://git-scm.com/docs/git-diff)

---

# 第 11 章　CI、发布与部署：从本地能跑到别人能用

> 本章成果：把测试、代码检查、CSV 导出验收、发布记录和部署检查固化成可重复流程，得到 Subscription Tracker 的 v1.0 候选版本。

## 1. 本章成果

完成本章后，你应该拥有：

1. `.github/workflows/ci.yml`：在每次 push、pull request 和手动触发时运行安装、检查、测试与语法编译。
2. 一次**干净环境复现**：从远程仓库重新克隆，安装依赖，运行全部检查。
3. `.env.example`：记录非敏感运行配置，明确哪些内容不能提交。
4. `scripts/verify_csv_export.py`：独立验收 CSV 导出的响应类型、列名、中文、逗号和实际创建的数据行。
5. `docs/runbooks/deploy-v1.md`：部署前置条件、部署步骤、健康检查和冒烟检查。
6. `docs/runbooks/rollback-v1.md`：代码回滚、数据边界和失败后的恢复动作。
7. v1.0 发布说明模板：把“完成”变成可检查的证据。

本章不要求你一定拥有公网服务器。没有服务器时，可以完成本地发布候选版本和部署演练；**不要把本地运行结果写成生产部署成功**。

## 2. 为什么需要它

本地测试通过并不等于项目可交付。它至少可能隐藏四类问题：

1. **环境差异**：你本地缓存了依赖、环境变量或数据库文件，干净环境却缺少它们。
2. **配置漂移**：代码依赖某个未在仓库中说明的变量或默认路径。
3. **验收缺口**：页面能打开，不代表 CSV 的编码、列名、逗号转义和数据内容都正确。
4. **恢复缺口**：部署失败后，如果没有已知良好版本、健康检查和回滚步骤，就只能临时猜测。

CI 的价值是把验收命令绑定到具体 commit；发布流程的价值是把版本、配置、健康检查和回滚路径写下来。对 AI 生成的项目尤其如此：AI 可以写出看起来合理的代码，但“它说完成了”不能作为交付证据。

## 3. 最少必备知识

- **CI（Continuous Integration）**：自动执行安装、检查和测试，验证某个 commit 是否满足门禁。
- **Workflow / Job / Step**：GitHub Actions 中，workflow 是完整流程，job 是运行单元，step 是其中一条命令或动作。
- **Artifact**：构建、测试或发布产生的可保存文件。
- **Tag 与 Release**：tag 标记具体 commit，release 面向人提供版本说明和下载入口。
- **配置与密钥**：普通配置可以公开示例，密钥只能通过 Secret Manager 或平台 Secrets 注入。
- **健康检查（health check）**：判断进程和基础依赖是否响应。
- **冒烟检查（smoke test）**：验证一个最关键用户流程是否真的可用。
- **回滚**：恢复到已知良好版本；代码回滚不等于数据库恢复。

## 4. 起始项目状态

本章假设你已经完成第 9 章和第 10 章，当前项目应至少具备：

- `/health` 健康检查端点。
- `/api/subscriptions` 的增删改查。
- `GET /api/subscriptions/export` CSV 导出。
- 能覆盖核心行为和 CSV 导出的测试。
- `requirements.txt` 中包含运行、测试和 Ruff 所需依赖。
- 上下文文档 `AGENTS.md`、`docs/project-map.md`、`docs/handoff.md` 已存在。

创建发布分支：

```powershell
git switch -c ci/release-v1
git status --short
python -m pytest -q
python -m ruff check .
```

如果这些命令失败，先修复，不要开始发布流程。

## 5. 操作步骤与 AI 任务示例

### 5.1 确认本地合同

先在本地启动应用：

```powershell
python -m uvicorn app.main:app --reload
```

在另一个终端检查健康端点：

```powershell
curl.exe --fail --show-error --silent http://127.0.0.1:8000/health
```

macOS/Linux：

```bash
curl --fail --show-error --silent http://127.0.0.1:8000/health
```

记录实际状态码和响应体。健康检查通过只说明服务基础可用，不能代替 CSV 导出和 UI 流程验收。

### 5.2 添加 GitHub Actions CI

让 AI 生成初稿时，必须限定范围和命令：

```text
目标：为 Subscription Tracker 创建 GitHub Actions CI。
上下文：只读取 README.md、AGENTS.md、requirements.txt、pytest 配置（如有）、tests/ 目录结构。
范围：只新增 .github/workflows/ci.yml，不修改业务代码、测试或依赖。
约束：
1. 使用 Python 3.12。
2. 在 push 到 main、pull request 到 main 和 workflow_dispatch 时运行。
3. 设置 permissions: contents: read。
4. 步骤依次执行：checkout、setup-python、安装 requirements.txt、ruff check、pytest、compileall app。
5. 不部署，不使用 secrets，不发布 Release。
6. 不添加 badge、缓存策略以外的花哨配置。
7. 本地命令必须与 CI 命令一致。
验收：YAML 可被 GitHub Actions 解析，任一检查失败时 workflow 失败。
输出：完整 workflow 文件、每步目的、可能导致本地与 CI 结果不一致的因素。
```

人工审查后，可采用这个完整 workflow：

```yaml
name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  verify:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r requirements.txt

      - name: Lint with Ruff
        run: python -m ruff check .

      - name: Run tests
        run: python -m pytest -q

      - name: Compile application package
        run: python -m compileall -q app
```

说明：

- `actions/checkout@v4` 和 `actions/setup-python@v5` 使用主版本标签，便于教学阅读。生产项目可进一步固定到完整 commit SHA，以降低供应链风险。
- `permissions: contents: read` 遵循最小权限原则；当前 CI 不需要写仓库。
- `workflow_dispatch` 允许你在没有新提交时手动复跑。
- `compileall` 不能代替测试，它只检查 Python 文件能否编译。

### 5.3 干净环境复现

本地通过不等于干净环境通过。把项目推送到远程后，从一个新目录克隆：

```powershell
cd ..
git clone <YOUR_REPO_URL> subscription-tracker-clean
cd subscription-tracker-clean
git switch <CI_BRANCH_OR_TAG>
python -m venv .venv
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ruff check .
python -m pytest -q
python -m compileall -q app
```

每条命令都必须返回成功状态。若失败，优先检查：

- 依赖是否漏写进 `requirements.txt`；
- 测试是否依赖你本地已有数据库或缓存文件；
- 是否读取了未提交的 `.env`；
- Python 小版本是否与 CI 不同；
- 代码是否依赖 Windows 路径分隔符。

### 5.4 配置与密钥

新增 `.env.example`，只写非敏感示例：

```dotenv
# Copy this file to .env for local development only.
# Do not commit .env or any real credential.
APP_ENV=development
DATABASE_PATH=data/subscriptions.db
LOG_LEVEL=INFO

# Deployment placeholders. Real values belong in your secret manager.
# DEPLOY_HOST=
# DEPLOY_USER=
# DEPLOY_TOKEN=
```

如果你的代码目前还没有集中读取这些变量，不要在发布说明中声称“已支持环境变量配置”。可以先完成这个受控 AI 任务：

```text
目标：为 Subscription Tracker 增加集中运行时配置。
上下文：读取 AGENTS.md、docs/project-map.md、app/database.py、app/main.py、tests/。
范围：新增 app/config.py，并让 SQLite 数据库路径通过配置读取。
约束：
1. 保留公开 API 不变。
2. 不引入新依赖。
3. 测试必须使用临时数据库，不得读写 data/subscriptions.db。
4. 不提交 .env。
5. 默认值保持当前本地开发行为不变。
6. 只修改实现配置所需的最小文件。
验收：python -m pytest -q 与 python -m ruff check . 通过；设置 DATABASE_PATH 后，应用使用指定路径。
输出：变更文件列表、配置字段说明、需要人工确认的风险。
```

一个最小配置示例：

```python
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_env: str
    database_path: str
    log_level: str


def load_settings() -> Settings:
    return Settings(
        app_env=os.getenv("APP_ENV", "development"),
        database_path=os.getenv("DATABASE_PATH", "data/subscriptions.db"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
```

密钥规则：

- `.env` 必须被 `.gitignore` 忽略。
- 真实密钥不进入源码、CI YAML、日志、发布说明和截图。
- GitHub Actions 中通过 Secrets 注入，不把 secret 打印到日志。
- 当前 CI 只做检查和测试，不需要部署密钥；不要为了“看起来高级”提前添加部署权限。

### 5.5 验收 CSV 导出

CSV 很容易出现三类问题：响应类型错误、UTF-8 BOM 或编码错误、含逗号字段没有正确引用。下面脚本会创建一个带中文和逗号的测试订阅，导出 CSV，找到该行，验证列名和内容，最后删除测试数据。

新增 `scripts/verify_csv_export.py`：

```python
#!/usr/bin/env python3
"""Verify CSV export against a disposable local Subscription Tracker instance.

Usage:
    python scripts/verify_csv_export.py [BASE_URL]

The default base URL is http://127.0.0.1:8000. This script creates one test
subscription, exports CSV, verifies the created row, and then deletes the test
subscription. Do not run it against production data unless you have an approved
temporary database and understand that it performs a DELETE request.
"""

from __future__ import annotations

import csv
import io
import json
import sys
import urllib.error
import urllib.request
import uuid

DEFAULT_BASE_URL = "http://127.0.0.1:8000"
EXPECTED_COLUMNS = [
    "id",
    "name",
    "amount",
    "currency",
    "renewal_date",
    "note",
    "created_at",
]


def request_json(url: str, method: str = "GET", payload: dict | None = None):
    data = None
    headers = {"Accept": "application/json"}

    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json; charset=utf-8"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            body = response.read()
            parsed = json.loads(body.decode("utf-8")) if body else None
            return response.status, parsed
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def fetch_csv(url: str):
    request = urllib.request.Request(url, headers={"Accept": "text/csv"}, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            return response.status, response.headers.get_content_type(), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, "", exc.read()


def delete_quietly(url: str) -> None:
    request = urllib.request.Request(url, method="DELETE")
    try:
        urllib.request.urlopen(request, timeout=10)
    except urllib.error.HTTPError:
        # Cleanup is best-effort; the verification result remains authoritative.
        pass
    except urllib.error.URLError:
        pass


def main() -> int:
    base_url = (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_BASE_URL).rstrip("/")
    marker = f"CSV验收-{uuid.uuid4().hex[:8]}"

    payload = {
        "name": marker,
        "amount": 1299,
        "currency": "CNY",
        "renewal_date": "2027-01-15",
        "note": "含,逗号与中文",
    }

    status, created = request_json(f"{base_url}/api/subscriptions", "POST", payload)
    if status not in (200, 201) or not isinstance(created, dict):
        print(f"FAIL: POST /api/subscriptions returned {status}: {created}")
        return 1

    record_id = created.get("id")
    if record_id is None:
        print(f"FAIL: created subscription response has no id field: {created}")
        return 1

    try:
        status, content_type, body = fetch_csv(f"{base_url}/api/subscriptions/export")
        if status != 200:
            print(f"FAIL: CSV export returned HTTP {status}: {body!r}")
            return 1

        if content_type != "text/csv":
            print(f"FAIL: expected Content-Type text/csv, got {content_type!r}")
            return 1

        text = body.decode("utf-8-sig")
        rows = list(csv.DictReader(io.StringIO(text)))
        if not rows:
            print("FAIL: CSV export contains no data rows")
            return 1

        missing_columns = [column for column in EXPECTED_COLUMNS if column not in rows[0]]
        if missing_columns:
            print(f"FAIL: CSV is missing columns: {missing_columns}")
            return 1

        matched = [row for row in rows if str(row.get("id")) == str(record_id)]
        if len(matched) != 1:
            print(f"FAIL: expected exactly one exported row for id {record_id}, found {len(matched)}")
            return 1

        row = matched[0]
        checks = {
            "name": row.get("name") == marker,
            "amount": row.get("amount") == "1299",
            "currency": row.get("currency") == "CNY",
            "renewal_date": row.get("renewal_date") == "2027-01-15",
            "note": row.get("note") == "含,逗号与中文",
            "created_at_present": bool(row.get("created_at")),
        }
        failed_checks = [key for key, ok in checks.items() if not ok]
        if failed_checks:
            print(f"FAIL: CSV row mismatch: {failed_checks}; row={row}")
            return 1

        print(f"CSV export OK: id={record_id}, marker={marker}, rows={len(rows)}")
        return 0
    finally:
        delete_quietly(f"{base_url}/api/subscriptions/{record_id}")


if __name__ == "__main__":
    raise SystemExit(main())
```

运行方式：

```powershell
python -m uvicorn app.main:app --reload
```

在另一个终端：

```powershell
python scripts/verify_csv_export.py
echo $LASTEXITCODE
```

macOS/Linux：

```bash
python scripts/verify_csv_export.py
echo $?
```

通过标准是脚本退出码为 `0`，并输出以 `CSV export OK` 开头的实际结果。若路由、列名、编码或逗号处理不符合预期，脚本会明确失败。

### 5.6 创建发布候选版本

CI 通过后，再创建 tag。不要先打 tag、后补测试。

```powershell
git status --short
git switch main
git pull --ff-only
git merge --no-ff ci/release-v1
python -m pytest -q
python -m ruff check .
```

打开 GitHub Actions，确认对应 commit 的 workflow 已通过。然后：

```powershell
git tag -a v1.0.0 -m "Release Subscription Tracker v1.0.0"
git push origin v1.0.0
```

发布说明可以使用这个模板：

```markdown
# Subscription Tracker v1.0.0

- Release commit: <git-commit-sha>
- CI run: <workflow-run-url>
- Clean environment verification: <date, operator, result>
- CSV export verification: <command and actual result>
- Deployment target: <none|staging|production>
- Health check URL: <health-url or none>

## Included

- Core subscription CRUD
- CSV export
- Automated CI checks
- Deployment and rollback runbooks

## Known limitations

- <list actual limitations; write none only after checking>

## Rollback plan

- See docs/runbooks/rollback-v1.md
```

所有尖括号必须替换为真实链接、命令输出摘要或明确写 `none`。不要为了美观编造 CI 地址。

### 5.7 部署、健康检查与冒烟检查

下面是一个可调整的 Linux 服务器部署模板。它不会自动适配所有托管平台；`REPO_URL`、路径、服务名、反向代理和证书都需要按你的环境修改。

`docs/runbooks/deploy-v1.md` 示例：

```markdown
# Subscription Tracker v1.0 deployment runbook

## Preconditions

- CI for the exact release tag is green.
- Target host has Python 3.12 and required OS packages.
- Deployment user can read the repository and manage the service.
- Existing production data, if any, has a current backup.
- HTTPS reverse proxy and firewall rules are configured separately.

## Variables

```bash
export REPO_URL="<your-git-repo-url>"
export APP_USER="<deployment-user>"
export APP_HOST="<server-host>"
export APP_DIR="/srv/subscription-tracker"
export RELEASE_TAG="v1.0.0"
export SERVICE_NAME="subscription-tracker"
export HEALTH_URL="https://<your-domain>/health"
```

## Deploy exact release

```bash
ssh "$APP_USER@$APP_HOST"
set -euo pipefail

mkdir -p "$APP_DIR/releases"
cd "$APP_DIR"

git clone --branch "$RELEASE_TAG" --depth 1 "$REPO_URL" "releases/$RELEASE_TAG"
ln -sfn "$APP_DIR/releases/$RELEASE_TAG" "$APP_DIR/current"

cd "$APP_DIR/current"
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ruff check .
.venv/bin/python -m pytest -q
```

## Service unit template

```ini
[Unit]
Description=Subscription Tracker
After=network.target

[Service]
Type=simple
User=appuser
WorkingDirectory=/srv/subscription-tracker/current
EnvironmentFile=/srv/subscription-tracker/shared/app.env
ExecStart=/srv/subscription-tracker/current/.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
```

## Restart and health check

```bash
sudo systemctl restart "$SERVICE_NAME"
curl --fail --show-error --silent "$HEALTH_URL"
```

## Smoke check

1. Open the deployed URL in a browser.
2. Create one clearly named smoke-test subscription.
3. List subscriptions and confirm the record appears.
4. Export CSV and confirm the smoke-test record is present.
5. Delete the smoke-test record.
6. Record who performed the check, when, and the actual result.

## Deployment evidence

- Release tag:
- Deployed commit:
- CI run:
- Health check result:
- Smoke check result:
- Operator:
- Timestamp:
```

如果还没有服务器，可以在本地完成同等演练：用干净 clone、独立虚拟环境、独立数据目录、`uvicorn` 进程、健康检查和 CSV 脚本验收。证据中必须写 `local deployment rehearsal`，不能写成 production。

### 5.8 回滚流程

`docs/runbooks/rollback-v1.md` 示例：

```markdown
# Subscription Tracker rollback runbook

## When to roll back

- Health endpoint does not return success after deployment.
- Core create/list/export flow fails.
- A required configuration or dependency is missing.
- Automated checks fail on the deployed release.

## Code rollback

```bash
export APP_DIR="/srv/subscription-tracker"
export SERVICE_NAME="subscription-tracker"
export PREVIOUS_RELEASE="<last-known-good-tag>"

ln -sfn "$APP_DIR/releases/$PREVIOUS_RELEASE" "$APP_DIR/current"
sudo systemctl restart "$SERVICE_NAME"
curl --fail --show-error --silent "$HEALTH_URL"
```

## First-release failure

If v1.0 is the first deployed version and no previous release exists, do not invent a rollback target. Stop or disable the public service, restore the prior infrastructure state, and record the failure evidence.

## Database boundary

A code rollback does not reverse database records or schema migrations. Before rolling back:

1. Identify whether the failed release changed the database schema.
2. If it did not, code rollback may be sufficient.
3. If it did, restore from an approved backup or apply a forward-fix migration.
4. Never overwrite production data without a backup and an explicit recovery decision.

## Evidence

- Failed release:
- Reason:
- Rollback target or action:
- Health check result:
- Data impact:
- Operator:
- Timestamp:
```

v1.0 如果只引入 CSV 导出和 CI，通常没有数据库 schema 迁移；但你仍应根据实际代码确认这一点，不能照抄本章结论。

## 6. AI 应生成的产物

本章可让 AI 生成以下文件初稿：

```text
.github/workflows/ci.yml
.env.example
scripts/verify_csv_export.py
docs/runbooks/deploy-v1.md
docs/runbooks/rollback-v1.md
docs/runbooks/release-v1.0.0.md
```

AI 还应返回：

- workflow 每个步骤的目的；
- 本地检查与 CI 检查是否一致；
- CSV 验收覆盖了哪些场景；
- 配置项中哪些是非敏感、哪些必须作为 Secret；
- 部署与回滚中需要人工确认的环境差异；
- 未验证项清单。

## 7. 人工检查点

发布前逐项检查：

- CI YAML 是否只运行检查，不偷偷部署或写仓库？
- `permissions` 是否保持 `contents: read`？
- CI 命令是否与本地命令一致？
- `requirements.txt` 是否包含测试、Ruff 和运行所需依赖？
- 干净 clone 是否没有依赖你本地的 `.env`、缓存或 SQLite 文件？
- CSV 脚本是否验证 Content-Type、列名、中文、逗号、实际创建行和清理删除？
- `.env.example` 是否没有真实密钥？
- `.env`、数据库文件和验收产物是否被 `.gitignore` 忽略？
- Release tag 是否指向 CI 通过的那个 commit？
- 健康检查是否只证明服务响应，而不是证明业务流程可用？
- 部署证据是否区分本地演练、staging 和 production？
- 回滚目标是否真实存在，并且数据库兼容性已确认？

## 8. 验收命令与通过标准

本地验收：

```powershell
git status --short
python -m ruff check .
python -m pytest -q
python scripts/verify_csv_export.py
echo $LASTEXITCODE
curl.exe --fail --show-error --silent http://127.0.0.1:8000/health
```

干净环境验收：

```powershell
cd subscription-tracker-clean
python -m ruff check .
python -m pytest -q
python -m compileall -q app
```

发布一致性验收：

```powershell
git rev-parse HEAD
git rev-list -n 1 v1.0.0
git tag --list "v1.0.0"
```

通过标准：

1. 所有命令退出码为 `0`。
2. GitHub Actions 对应 commit 或 tag 的 workflow 已通过。
3. 干净 clone 能完成依赖安装和全部检查。
4. CSV 脚本输出 `CSV export OK`，且退出码为 `0`。
5. 健康检查返回预期 JSON 或状态码，实际内容以你的 `/health` 实现为准。
6. `git rev-parse HEAD` 与 `git rev-list -n 1 v1.0.0` 指向同一 commit。
7. 发布说明中每个尖括号均已替换为真实证据或明确写 `none`。
8. 如果执行了部署，记录环境、健康检查和冒烟结果；如果没有执行，明确写 `not deployed`。

## 9. 常见失败及恢复方法

| 症状 | 可能原因 | 恢复动作 |
|---|---|---|
| 本地测试通过，CI 安装依赖失败 | 依赖只装在本地环境，没写入 `requirements.txt` | 在干净虚拟环境中复现，补齐依赖，重新运行 CI |
| 干净 clone 测试失败，本地却通过 | 测试依赖未提交的 `.env`、本地 SQLite 或缓存文件 | 删除未跟踪依赖，改测试使用临时数据库或 fixture，重新验证 |
| CSV 脚本返回 404 | 导出路径、方法或路由注册与规格不一致 | 检查 `app/routes.py` 和规格中的路径，统一为一个公开端点，不要保留多个别名 |
| CSV 中中文乱码或逗号破坏列 | 编码、BOM 或 CSV quoting 处理错误 | 使用 UTF-8，必要时写 `utf-8-sig` 供 Excel 读取；让 Python `csv` 模块处理引号，不要手工拼字符串 |
| 健康检查通过，但 UI 或导出失败 | `/health` 只检查进程，未覆盖数据库和业务流程 | 增加冒烟检查，至少验证创建、列表和导出一条测试记录 |
| Workflow 日志泄露 Secret | 将 secret 直接 echo、写入环境示例或放进代码 | 立即轮换密钥，从历史和工作流中删除，改用平台 Secrets 并检查日志权限 |
| 部署后服务无法访问 | 端口、反向代理、防火墙、路径权限或进程用户不匹配 | 查看服务状态和应用日志，先在本机 `127.0.0.1` 验证，再检查代理和防火墙 |
| 回滚后仍运行新版本 | symlink 未切换、服务未重启或缓存的旧进程仍存在 | 检查 `current` 指向、服务状态、进程启动时间和健康检查结果 |

## 10. 本章 Git 提交

建议分支：

```powershell
git switch -c ci/release-v1
```

建议拆分：

```powershell
git add .github/workflows/ci.yml
git commit -m "ci: add lint test and compile checks"

git add scripts/verify_csv_export.py
git commit -m "test: verify csv export contract independently"

git add .env.example
git commit -m "chore: document runtime configuration placeholders"

git add docs/runbooks/deploy-v1.md docs/runbooks/rollback-v1.md
git commit -m "docs: add v1 deployment and rollback runbooks"
```

只有 CI 通过且干净环境复现成功后，才创建 `v1.0.0` tag。不要把未验证的发布说明、临时数据库或验收 CSV 一起提交。

## 11. 练习与扩展

1. **制造一次 CI 红灯**：在临时分支让一个测试失败，观察 workflow 如何阻止合并，再恢复。
2. **漏依赖实验**：从 `requirements.txt` 删除一个测试依赖，验证干净 clone 能否发现问题。
3. **增强 CSV 验收**：增加空字符串、超长 note、重复订阅名和非法日期等测试场景。
4. **发布产物**：使用 `git archive` 或 Actions artifact 生成源代码包，并记录校验和。
5. **受控部署**：为 GitHub Actions 添加带 manual approval 的 deployment environment，但保持当前教程主流程不自动部署。
6. **供应链加固**：把 `actions/checkout` 和 `actions/setup-python` 固定到完整 commit SHA，并记录升级流程。

## 12. 参考资料

- [About continuous integration - GitHub Docs](https://docs.github.com/en/actions/get-started/continuous-integration)
- [Workflow syntax for GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [Using secrets in GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Managing releases in a repository - GitHub Docs](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)

---

# 综合实验三：交付第一个正式版本 v1.0

> 实验成果：把 v0.x 的项目推到 v1.0——干净环境可安装、CI 全绿、CSV 导出可用、有标签有发布记录、回滚方案纸面可执行。

## 实验目标

跨越“本地能跑”与“别人能用”之间的鸿沟。交付不是“在我机器上没问题”，而是：干净环境可复现、检查自动化、失败可回滚、过程有证据。

## 前置条件

- 第 7—11 章完成；本地测试全绿；GitHub 仓库已建立。
- 一个全新目录用于“干净环境复现”（或另一台机器/容器）。

## 交付定义（对照 templates/definition-of-done.md）

| 维度 | v1.0 要求 |
|---|---|
| 功能 | 订阅 CRUD、到期提醒、CSV 导出全部可用 |
| 质量 | pytest 全绿；ruff 0 错误；CI 门禁通过 |
| 复现 | 新目录 clone → install → run 一条路径无人工补丁 |
| 证据 | 验收命令输出、CI run 链接、导出文件抽查截图 |
| 回滚 | 回滚到上一标签的命令与责任人已写明 |

## 步骤

### 步骤 1：补齐 CSV 导出与验收

若尚未实现，按规格 R 系列规则完成导出（标准库 `csv` 模块，含特殊字符处理——第 12 章将回来验证它的质量）。验收：

```powershell
python -m pytest -q
# 页面点击导出 → 用 Excel/文本编辑器打开 → 列数与表头一致
```

### 步骤 2：固化 CI

确认 `.github/workflows/ci.yml` 包含（与第 11 章一致）：

```yaml
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m ruff check .
      - run: python -m pytest -q
```

推送后确认 Actions 页面全绿，**记下 run 链接作为发布证据**。

### 步骤 3：干净环境复现

```powershell
cd ..\clean-test
git clone <你的仓库地址>
cd clean-test\subscription-tracker   # 视仓库结构
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app       # 不带 --reload，模拟真实启动
curl http://127.0.0.1:8000/health
```

任何需要“手工补一步”的地方（漏写的依赖、未入库的静态文件）都是发布阻塞项，修完重走。

### 步骤 4：执行发布检查清单

打开 `templates/release-checklist.md` 逐项执行。重点三件：

1. **标签**：`git tag -a v1.0 -m "first deliverable release"`。
2. **发布说明**：写清“包含什么/不包含什么/已知问题”。
3. **回滚方案**：写明回滚命令（`git switch --detach v0.2` + 重新部署步骤）与执行时机。

### 步骤 5：发布与记录

```powershell
git push origin main --tags
```

在 GitHub Release（或 `docs/releases/v1.0.md`）归档：变更摘要、CI run 链接、验收证据、已知问题。

## 故障恢复预案（演练其中一项）

| 场景 | 恢复动作 |
|---|---|
| 干净环境安装失败 | 按“症状→原因→恢复”定位（常见：依赖漏写、Python 版本不符）；修复后重走步骤 3 |
| CI 红 | 只允许修红不允许跳过；`pytest -q` 本地复现 → 修复 → 重推 |
| 发布后发现核心流程坏 | 先执行回滚方案（回到上一标签），再排查；**先恢复服务，再找根因** |
| 导出文件乱码 | 确认 UTF-8 BOM 处理；此问题若涉及已导出数据，重新导出并 diff |

## 自检表

| # | 检查项 | 证据 |
|---|---|---|
| 1 | 干净目录完整走通安装→启动→健康检查 | 命令输出 |
| 2 | pytest 全绿（附数量） | CI/本地输出 |
| 3 | ruff 0 错误 | CI/本地输出 |
| 4 | CSV 导出可打开、列正确 | 截图/文件抽查 |
| 5 | CI run 全绿链接 | URL |
| 6 | 标签 v1.0 存在且指向正确提交 | `git tag -n` |
| 7 | 发布说明含已知问题 | 文档链接 |
| 8 | 回滚方案纸面可执行（命令逐条写明） | 发布记录 |
| 9 | 回滚演练（至少 dry-run 一次） | 命令记录 |
| 10 | 证据归档位置明确 | docs/releases/ |

## 常见失败与恢复

**失败 1：CI 绿但本地红（或反之）。**
原因：环境差异（Python 版本、依赖锁定）。
恢复：CI 与本地统一 Python 3.12；requirements.txt 完全锁定；以 CI 环境为准复现本地差异。

**失败 2：干净环境少文件（静态资源没入库）。**
原因：`.gitignore` 过度或 add 遗漏。
恢复：补入库 + 提交 `.gitignore` 修正说明；复现实验重新来一遍，不允许“那次是特例”。

**失败 3：急着发版跳过回滚预案。**
恢复：把回滚预案作为发布前置门禁（checklist 第 5 节），不写不发。真正出事时你会感谢它。

**失败 4：把“发布”当成一次 commit 而非一套流程。**
恢复：回看本实验步骤——标签、说明、证据、回滚缺一不可；下次提前一天做 checklist。

## 完成标准

自检表 10/10；`v1.0` 标签已推送；发布记录可追溯；回滚演练有记录。

## 下一步

v1.0 之后的第一次需求变更与 Bug 修复（第 12—13 章）将从这里出发——这正是“维护”的起点。

---

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

---

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

---

# 第 14 章　接手旧项目：从陌生仓库到受控现代化

> 本章成果：接手一个无说明、无测试、结构混乱的订阅管理器旧版本，建立基线与项目地图，完成第一阶段受控现代化 PR。

## 1. 本章成果

1. 你掌握陌生仓库的标准进入流程：地图 → 运行 → 测试基线 → 风险清单。
2. 你能区分“文档说的”与“代码实际做的”，并以实际行为为准建立事实基线。
3. 你完成第一阶段现代化：一次只动一个模块，每阶段独立提交并验证。
4. 你知道何时应该停止修补、重新评估架构。

## 2. 为什么需要它

“从零生成”只是教程故事的一半；现实中大量工作是接手——自己三个月前的项目、同事留下的仓库、AI 之前生成的失控原型。旧项目的危险不在“旧”，而在**未知**：不知道哪些行为是刻意的、哪些是偶然的、改一处会不会连锁崩塌。没有基线就动手的现代化，本质是把未知风险直接引入稳定行为。本章流程的价值在于：先花少量时间建立“现在是什么样”的客观事实，让后续每一步修改都有对照物。这与第 12—13 章一脉相承——维护的通用纪律是“先理解、再保护、后修改”。

## 3. 最少必备知识

- **项目地图**：入口、依赖、数据流、外部接触面的简明描述（一页以内）。
- **行为基线**：当前系统对一组输入的实际响应记录（含测试与手工快照）。
- **保护性测试**：为既有行为补写的测试，目的不是验证正确性，而是“钉住现状”，让重构可检测。
- **架构测试**：用代码固化依赖方向约束（如“repository 不得 import routes”），违反即 CI 红。
- **Strangler 式迁移**：新逻辑逐步包住旧逻辑，而不是一次性替换。
- **现代化 vs 重写**：现代化保持外部行为不变；重写是新项目，需要新蓝图。

## 4. 起始项目状态

本章使用一个特制的“旧版”起点：`legacy/` 目录提供一份订阅管理器的混乱版本——无 README、依赖未锁定、SQL 拼接在路由里、无任何测试、变量名随意、有一个“看起来能跑”的入口脚本。**若你在重建该起点**：故意保留这些病灶；若没有现成起点，用你自己早期的某个项目（或让 AI 生成一份“故意混乱”版本）。

## 5. 操作步骤与 AI 任务示例

### 步骤 1：建立 Git 基线与隔离

```powershell
cd legacy\subscription-tracker-old
git init
git add -A
git commit -m "chore: import legacy code as-is, no fixes yet"
git tag legacy-intake
```

**一条修复都不做就提交**——这是现代化的第一原则：先原样入库，让之后每一步都有 diff 对照。

### 步骤 2：让 AI 生成项目地图初稿

**给 AI 的任务示例（text 块）**：

```text
目标：为这个陌生仓库生成项目地图。
范围：只读代码与目录结构，不修改任何文件。
地图必须包含：
  1. 入口（启动命令、入口文件、路由注册方式）；
  2. 目录结构（每个顶层目录/文件一句话职责）；
  3. 数据流（一次“添加订阅”请求从入口到存储的完整路径）；
  4. 外部依赖清单（框架/库/环境变量/文件）；
  5. 风险观察（你注意到的坏味道，只列不改）。
约束：区分“从代码确认的事实”与“你的推测”，推测必须标注 [推测]；
  引用结论时给出文件与行号。
验收：按地图中的入口命令应能启动服务（若失败，报告失败现象作为事实）。
输出：Markdown 地图，不超过 800 字。
```

### 步骤 3：人工验证地图（不信 AI，信运行）

按 AI 给出的入口命令实际启动；对地图中标注 [推测] 的条目逐个用运行或读码证实/证伪。地图修正后存为 `docs/repo-map.md`。

### 步骤 4：建立运行基线

对核心行为做快照记录（旧代码无论多丑，先记录它**实际**做什么）：

```powershell
# 逐条执行并记录响应原文（存 docs/behavior-baseline.md）
curl http://127.0.0.1:8000/api/subscriptions
curl -X POST http://127.0.0.1:8000/api/subscriptions -H "Content-Type: application/json" -d "{\"name\":\"基线样本\",\"amount\":100,\"currency\":\"CNY\",\"renewal_date\":\"2026-12-01\"}"
curl -X DELETE http://127.0.0.1:8000/api/subscriptions/1
```

注意记录“怪行为”——比如旧代码可能对负金额静默接受。**基线的意义是钉住现状（包括怪行为），修复怪行为是后续显式决策，不是顺手改。**

### 步骤 5：AI 任务——保护性测试

**给 AI 的任务示例（text 块）**：

```text
目标：为既有行为编写保护性测试，钉住当前基线。
上下文：docs/behavior-baseline.md 记录了实际响应（包括怪行为）；代码在 app/ 下。
范围：只新增 tests/；不修改应用代码。
约束：
  1. 测试断言“现状”而非“理想”——基线里负金额被接受，测试就断言它被接受，并加注释 TODO(baseline-quirk)；
  2. 每条测试注明对应基线条目；
  3. 覆盖：列表查询、添加、删除、以及基线中全部怪行为；
  4. 运行结果必须与基线一致（pytest 全绿）。
验收：python -m pytest -q 全绿；绿的含义是“现状被钉住”。
输出：完整测试文件 + 与基线的覆盖对照。
```

这一步最容易出错的地方：AI 会忍不住“顺手修好”怪行为再写理想测试——打回，保护性测试期修行为等于自毁基线。

### 步骤 6：依赖与静态检查基线

```powershell
pip freeze > docs/requirements-snapshot.txt   # 事实快照（旧依赖原样）
python -m ruff check . --statistics          # 只统计，不修复
```

把 ruff 统计与依赖快照存档。它们回答“这个仓库病得多重”，为现代化排序提供依据。

### 步骤 7：现代化计划与第一阶段

制定分阶段计划（写入 `docs/modernization-plan.md`），每阶段满足：单一模块、行为不变、可独立验证。第一阶段典型选择：**把 SQL 从路由层抽到 repository 层**（结构改善，外部行为零变化）。

**给 AI 的任务示例（text 块）**：

```text
目标：第一阶段现代化——将路由层内联 SQL 抽取到 repository 层。
范围：app/routes.py、新建 app/repository.py；不得改 API 契约、不改任何行为、不改其他文件。
约束：
  1. 保护性测试必须全绿（它们是行为的裁判）；
  2. 纯机械搬迁 + 最小命名统一，不优化逻辑，不修怪行为；
  3. 每完成一个函数迁移列出前后对照；
  4. 迁移完成后 ruff check 对新代码 0 错误（旧病灶本次不处理）。
验收：pytest 全绿；curl 基线命令响应与 docs/behavior-baseline.md 逐条一致（diff 响应原文）。
输出：修改后文件 + 迁移对照表 + 验证输出。
```

### 步骤 8：分阶段提交

```powershell
git add app/repository.py app/routes.py
git commit -m "refactor: extract sql from routes into repository (behavior preserved)"
```

每个阶段一条提交；保护性测试全绿 + 基线 diff 为空是合并前提。

## 6. AI 应生成的产物

1. 项目地图初稿（含事实/推测区分）。
2. 保护性测试套件（含怪行为 TODO 标注）。
3. 第一阶段迁移 Diff + 前后对照表。

**人工产物**：修正后的 `docs/repo-map.md`、`docs/behavior-baseline.md`、`docs/modernization-plan.md`、ruff 统计快照。判断“先改哪个”是人的决策，AI 提供证据。

## 7. 人工检查点

1. 地图中的每条 [推测] 是否已验证或降级为“待验证”？
2. 基线里的怪行为是否被如实记录（而不是被“顺手修好”）？
3. 保护性测试里 TODO(baseline-quirk) 的条目，是否都能对应到基线原文？
4. 第一阶段 Diff 是否真的“行为不变”？（基线命令逐条 diff 响应）
5. modernization-plan 的每阶段是否满足“单模块 + 行为不变 + 可独立验证”？

## 8. 验收命令与通过标准

```powershell
python -m pytest -q              # 保护性测试全绿
curl <基线命令三条>               # 响应与基线一致
git log --oneline                # intake 原样提交与迁移提交分开可见
git tag                          # legacy-intake 存在
```

通过标准：全部命令真实执行；你能指着任一怪行为说出“现在为什么还留着、计划哪阶段处理”。

## 9. 常见失败及恢复方法

**症状 1：AI 拿到旧代码就开始“全面重写”。**
原因：把接手当成新项目。
恢复：任务约束写死“禁止重写，只允许机械搬迁”；重写需求请回到第 4—6 章流程另立新项目，两者不可混。

**症状 2：保护性测试阶段顺手修了怪行为。**
原因：AI（和人）对丑代码有天然修正欲。
恢复：恢复该改动（`git restore`），重申“怪行为在本阶段是契约”；修复怪行为排入 modernization-plan 的显式阶段，走规格变更。

**症状 3：迁移后某条基线响应变了。**
原因：搬迁中引入行为变化（常在默认值/异常路径）。
恢复：立即回滚该文件（`git restore`），缩小迁移粒度（一次一个函数）重来；基线 diff 为空是唯一合并标准。

**症状 4：依赖快照里有无法安装的老包。**
原因：旧环境与当前 Python 版本不兼容。
恢复：在单独虚拟环境中固定 Python 版本运行旧代码；把“依赖现代化”设为独立阶段（对应第 16 章流程），不要混入结构迁移。

**症状 5：AI 声称“测试全绿”但从未运行。**
原因：无执行环境或跳过验证。
恢复：你亲自运行 pytest 并贴回输出；坚持第 9 章的“验证视角分离”约定。

## 10. 本章 Git 提交

```text
分支：modernize/legacy-intake
chore: import legacy code as-is, no fixes yet        （tag: legacy-intake）
docs: add repo map and behavior baseline
test: pin current behavior with protective tests
refactor: extract sql from routes into repository (behavior preserved)
chore: record dependency snapshot and ruff statistics
```

## 11. 练习与扩展

1. 对基线中的怪行为各写一条“修复任务”，走第 13 章的规格变更流程（体验“接手→修复”全链路）。
2. 为“repository 不得 import routes”写一条架构测试（custom import 检查或 pytest 收集期断言），接入 CI。
3. （进阶）尝试 Strangler 式迁移：让新旧实现并行、开关切换、逐步删旧码，体会与一次性搬迁的差异。
4. 把本章流程提炼为你的“接手新仓库 SOP”个人清单。

## 12. 参考资料

- UI5 Agentic Development Tutorial 的遗留项目现代化步骤（本章模式的同型示范）：https://github.com/ui5/tutorials/blob/main/packages/agentic/steps/04/README.md
- Michael Feathers《Working Effectively with Legacy Code》核心思想：先有测试再改代码（接变更点概念）
- Martin Fowler：StranglerFigApplication：https://martinfowler.com/bliki/StranglerFigApplication.html
- humanlayer：复杂代码库中让 agent 真正解决问题的实践：https://github.com/humanlayer/humanlayer
- ChiYu 铁人赛 Day 31（旧代码模块化重构，中文同型实践）：https://huangchiyu.com/ChiYu-Blog/posts/2025ithomeironmanday31/

---

# 第 15 章　数据库迁移、备份与真正的故障恢复

> 本章成果：为订阅管理器增加 `billing_cycle`，用可重复执行的 SQLite 迁移保留旧数据，并实际完成一次备份、恢复和回滚边界演练。

## 1. 本章成果

完成后，项目将从 v1.1 演进到 v1.2，具备以下能力：

- 订阅记录支持 `monthly` 和 `yearly` 两种计费周期，旧记录自动使用 `monthly`。
- 有一份可审查、可在数据库副本上重跑的迁移脚本。
- 能在迁移前生成一致性备份，并把备份恢复成另一个数据库文件进行核验。
- 能解释代码回滚、数据库迁移和数据恢复为什么是三件事。
- 留下迁移测试、恢复手册和一份真实演练记录。

本章使用 Python 标准库 `sqlite3`，不引入新的数据库框架。

## 2. 为什么需要它

新增一个字段看似只是修改 API，实际上会同时改变代码、数据库结构和已有数据。只让 AI 修改模型，旧数据库可能因缺少字段而报错；直接删除数据库重建，则会丢失用户数据。

备份也不等于具备恢复能力。从未恢复过的备份，只说明文件存在，不说明它可用。恢复旧备份还会删除备份之后产生的合法新数据，因此“回到旧版本”不是一个无代价动作。

本章选择**加字段、保留数据、先副本演练**的方式，让变化保持小而可逆。金额继续使用整数分，不因本次迁移改变既有精度约定。

## 3. 最少必备知识

- **Schema**：表包含哪些列，以及类型、默认值和约束。
- **迁移（Migration）**：把数据库从一种 Schema 状态变为另一种状态的受控过程。
- **备份与恢复**：备份生成一致的数据库副本；恢复用副本替换或重建目标数据库。
- **事务**：一组操作要么全部提交，要么全部回滚。SQLite 的 `BEGIN IMMEDIATE` 会在事务开始时取得写锁，适合短迁移。
- **`PRAGMA user_version`**：SQLite 内置的用户 Schema 版本号。本章将 v1.2 的数据库标记为 `1`，它不是应用发布版本号。
- **RPO**：能容忍丢失多少最近数据。本章先不追求自动计算，只需在恢复记录中明确备份时间与其后可能丢失的写入。

## 4. 起始项目状态

从已完成第 12—14 章的 v1.1 项目开始，确认：

1. `data/subscriptions.db` 是实际使用的数据库；若你的配置不同，后续命令统一替换为真实路径。
2. `subscriptions` 表已有 `id`、`name`、`amount`、`currency`、`renewal_date`、`note`、`created_at`。
3. `python -m pytest -q` 和 `python -m ruff check .` 可以作为修改前基线。
4. Git 工作区没有无关修改，数据库文件不会被提交到 Git。

先建立分支并检查现状：

```powershell
git switch -c feat/billing-cycle-migration
git status
python -m pytest -q
python -m ruff check .
```

若基线已经失败，先记录并修复原问题，不要把旧失败混入本次迁移。

## 5. 操作步骤与 AI 任务示例

### 步骤 1：先写变更契约

在 `specs/` 中补充以下规则：新字段名为 `billing_cycle`；仅允许 `monthly`、`yearly`；缺省为 `monthly`；迁移不能删除或重写既有记录；API 必须拒绝其他值。新增字段还应进入创建、编辑、列表和详情流程。

给 AI 的任务应限制实现范围：

```text
目标：为 Subscription Tracker 增加 billing_cycle，并完成 SQLite 数据迁移。
上下文：当前为 v1.1；金额 amount 使用整数分；实际表为 subscriptions；
初始字段见 WRITING_GUIDE.md；核心 API 为 /api/subscriptions。
范围：schemas.py、repository.py、必要的前端表单、迁移脚本、迁移测试和恢复手册。
约束：只允许 monthly/yearly；旧记录默认 monthly；不得删除数据库重建；
不得改变 amount 类型；迁移必须可重复执行；先给计划和影响文件，再修改。
验收：旧行保留且为 monthly；可新增 yearly；非法值被拒绝；重复迁移不新增列；
原有测试与新增测试均执行；恢复脚本可在副本上验证。
输出：变更摘要、逐文件 Diff、执行的命令和真实结果、未完成项与回滚建议。
```

### 步骤 2：在任何迁移前制作一致性备份

新增 `scripts/db_backup.py`。它使用 SQLite 在线备份 API，而不是在数据库仍被写入时直接复制文件：

```python
import argparse
import sqlite3
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--backup", type=Path, required=True)
    args = parser.parse_args()
    database = args.database.resolve()
    backup = args.backup.resolve()
    if not database.is_file():
        parser.error(f"database not found: {database}")
    if backup.exists():
        parser.error(f"refusing to overwrite: {backup}")
    backup.parent.mkdir(parents=True, exist_ok=True)

    source = sqlite3.connect(f"file:{database.as_posix()}?mode=ro", uri=True)
    target = sqlite3.connect(backup)
    try:
        source.backup(target)
        result = target.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError(f"backup integrity_check failed: {result}")
    finally:
        target.close()
        source.close()
    print(f"backup created: {backup}")


if __name__ == "__main__":
    main()
```

备份文件名应包含时间和用途，例如 `backups/before-billing-cycle-2026-11-24.db`。日期使用实际操作日期；脚本拒绝覆盖已有备份。备份文件与数据库一样可能含个人数据，不提交到公开仓库。

### 步骤 3：编写可重复执行的迁移脚本

新增 `scripts/migrate_001_add_billing_cycle.py`：

```python
import argparse
import sqlite3
from pathlib import Path


def column_names(connection: sqlite3.Connection) -> set[str]:
    return {
        row[1]
        for row in connection.execute("PRAGMA table_info(subscriptions)")
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, required=True)
    args = parser.parse_args()
    database = args.database.resolve()
    if not database.is_file():
        parser.error(f"database not found: {database}")

    connection = sqlite3.connect(database, timeout=5)
    try:
        connection.execute("BEGIN IMMEDIATE")
        version = connection.execute("PRAGMA user_version").fetchone()[0]
        if version > 1:
            raise RuntimeError(f"unsupported schema version: {version}")
        if "billing_cycle" not in column_names(connection):
            connection.execute(
                """
                ALTER TABLE subscriptions
                ADD COLUMN billing_cycle TEXT NOT NULL DEFAULT 'monthly'
                CHECK (billing_cycle IN ('monthly', 'yearly'))
                """
            )
        connection.execute("PRAGMA user_version = 1")
        result = connection.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError(f"integrity_check failed: {result}")
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
    print(f"schema version 1 ready: {database}")


if __name__ == "__main__":
    main()
```

`ALTER TABLE ... ADD COLUMN` 让旧行获得默认值，`CHECK` 在数据库层拦截非法值。重复执行时先检查列，因此不会再次添加同名列。幂等不等于可以跳过备份：脚本未来的修改、操作失误和数据问题仍可能产生损失。

### 步骤 4：让应用读写新字段

检查并修改实际实现，而不是只改文档：

- `app/schemas.py`：用 `Literal["monthly", "yearly"]` 或等价校验限制输入，创建模型默认 `monthly`。
- `app/repository.py`：查询列、插入和更新参数都包含 `billing_cycle`，保持参数化 SQL。
- `app/routes.py`：确认响应模型不会把新字段过滤掉。
- `app/static/`：创建和编辑表单提供两个明确选项，列表显示当前周期。
- `tests/`：覆盖旧行迁移、新建 `yearly`、非法输入、重复迁移和原有 API 行为。

迁移测试可在临时目录创建旧 Schema，再用 `subprocess.run` 调用脚本。至少包含以下核心断言，不要使用没有业务断言的空测试：

```python
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "migrate_001_add_billing_cycle.py"


def test_migration_preserves_old_rows_and_rejects_bad_cycle(tmp_path: Path) -> None:
    database = tmp_path / "old.db"
    connection = sqlite3.connect(database)
    connection.execute(
        """
        CREATE TABLE subscriptions (
            id INTEGER PRIMARY KEY, name TEXT NOT NULL, amount INTEGER NOT NULL,
            currency TEXT NOT NULL, renewal_date TEXT NOT NULL,
            note TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL
        )
        """
    )
    connection.execute(
        "INSERT INTO subscriptions VALUES (1, 'Music', 1000, 'CNY', '2027-01-01', '', '2026-01-01T00:00:00Z')"
    )
    connection.commit()
    connection.close()

    for _ in range(2):
        subprocess.run([sys.executable, str(SCRIPT), "--database", str(database)], check=True)

    connection = sqlite3.connect(database)
    try:
        row = connection.execute(
            "SELECT name, amount, billing_cycle FROM subscriptions WHERE id = 1"
        ).fetchone()
        assert row == ("Music", 1000, "monthly")
        assert connection.execute("PRAGMA user_version").fetchone()[0] == 1
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO subscriptions (name, amount, currency, renewal_date, billing_cycle, created_at) VALUES ('Bad', 100, 'CNY', '2027-01-01', 'weekly', '2026-01-01T00:00:00Z')"
            )
    finally:
        connection.close()
```

### 步骤 5：先迁移副本，再处理真实数据库

```powershell
New-Item -ItemType Directory -Force data, backups
Copy-Item data/subscriptions.db data/migration-test.db -Force
python scripts/migrate_001_add_billing_cycle.py --database data/migration-test.db
python -m pytest -q
```

核对副本的行数、旧值和新字段后，停止开发服务器，备份真实数据库，再执行迁移：

```powershell
python scripts/db_backup.py --database data/subscriptions.db --backup backups/before-billing-cycle.db
python scripts/migrate_001_add_billing_cycle.py --database data/subscriptions.db
```

若 `backups/before-billing-cycle.db` 已存在，换一个带实际时间的新文件名，不覆盖旧备份。

### 步骤 6：实现并执行恢复演练

新增 `scripts/db_restore.py`。恢复前先验证备份，并在目标目录生成临时文件；只有验证通过才替换目标：

```python
import argparse
import os
import shutil
import sqlite3
from pathlib import Path


def check(database: Path) -> None:
    connection = sqlite3.connect(f"file:{database.as_posix()}?mode=ro", uri=True)
    try:
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise RuntimeError("integrity_check failed")
        table = connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'subscriptions'"
        ).fetchone()
        if table is None:
            raise RuntimeError("subscriptions table is missing")
    finally:
        connection.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backup", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--confirm-offline", action="store_true")
    args = parser.parse_args()
    if not args.confirm_offline:
        parser.error("stop the application and repeat with --confirm-offline")
    backup = args.backup.resolve()
    target = args.target.resolve()
    if not backup.is_file():
        parser.error(f"backup not found: {backup}")
    check(backup)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.name + ".restoring")
    if temporary.exists():
        parser.error(f"temporary file exists: {temporary}")
    try:
        shutil.copyfile(backup, temporary)
        check(temporary)
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(f"restored: {target}")


if __name__ == "__main__":
    main()
```

第一次演练不要覆盖真实数据库，恢复到一个新文件：

```powershell
python scripts/db_restore.py --backup backups/before-billing-cycle.db --target data/restored-test.db --confirm-offline
python -c "import sqlite3; c=sqlite3.connect('data/restored-test.db'); print(c.execute('SELECT COUNT(*) FROM subscriptions').fetchone()[0]); c.close()"
```

比较恢复文件与备份的行数、关键记录和 Schema。随后把实际备份位置、停止服务命令、恢复命令、核验人和数据丢失窗口写入 `docs/runbooks/database-recovery.md`。

### 步骤 7：演练三种不同的“回滚”

1. **代码回滚**：本次是向后兼容的加列，旧代码不知道新列，但插入仍有数据库默认值。验证旧代码能否读取迁移后的数据库，可以回滚代码而保留新 Schema。
2. **数据恢复**：若恢复迁移前备份，迁移后新增和修改的数据会丢失。先导出或保存当前数据库供核对，不直接覆盖唯一副本。
3. **前向修复**：若数据已经混合、旧备份太旧，通常应在当前状态上修复，而不是强行回到过去。记录选择理由和影响范围。

### 步骤 8：完成端到端验收

启动应用，分别创建月付和年付订阅，编辑其中一条，重新启动后再次检查。最后运行全部测试、Ruff 和 `/health`，保存真实输出作为 v1.2 的验收证据。

## 6. AI 应生成的产物

本章结束时，仓库至少应新增或更新：

- `scripts/db_backup.py`：一致性备份与完整性检查。
- `scripts/migrate_001_add_billing_cycle.py`：加列、约束和 Schema 版本。
- `scripts/db_restore.py`：离线恢复与恢复前校验。
- `tests/test_migration.py`：旧数据保留、非法值和重复执行测试。
- `docs/runbooks/database-recovery.md`：责任人、命令、备份位置和恢复记录。
- 规格、API、前端和数据库访问代码中的 `billing_cycle` 支持。

AI 还应给出实际 Diff 和执行记录。“应该可以”“理论上不会丢数据”不算完成证据。

## 7. 人工检查点

1. **看约束**：数据库和 API 都只允许两个值，默认值确实是 `monthly`。
2. **看旧数据**：比较迁移前后主键、名称、金额、日期和备注，不只比较行数。
3. **看事务**：异常路径有 rollback，脚本不会把空文件当合法旧库。
4. **看备份**：备份文件非空、未被覆盖、未进入 Git，且通过 `integrity_check`。
5. **看恢复**：恢复演练使用了备份而不是原库，应用停止后才替换真实目标。
6. **看回滚假设**：明确哪些旧代码兼容新 Schema，哪些情况需要数据恢复或前向修复。

## 8. 验收命令与通过标准

```powershell
python -m pytest -q
python -m ruff check .
python scripts/migrate_001_add_billing_cycle.py --database data/migration-test.db
python scripts/db_restore.py --backup backups/before-billing-cycle.db --target data/restored-test-2.db --confirm-offline
python -m uvicorn app.main:app
```

另开 PowerShell：

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

通过标准：重复迁移没有重复列错误；旧记录仍为 `monthly`；年付记录可创建；非法周期被 API 和数据库拒绝；恢复文件能打开且关键记录与备份一致；应用健康检查正常；所有结果来自你实际执行的命令。

## 9. 常见失败及恢复方法

- **症状：`duplicate column name`。原因：重复执行了不带列检查的简单 SQL。恢复动作：不要删列；使用本章脚本检查现状，确认 `user_version` 与数据后再继续。**
- **症状：`database is locked`。原因：仍有服务或测试持有写事务。恢复动作：停止写入进程并结束悬挂事务；不要删除 `-wal` 或 `-shm` 文件来“解锁”。**
- **症状：恢复后缺少最近订阅。原因：备份早于这些写入。恢复动作：保留当前库供对账，评估备份时间窗，必要时从当前库导出新增记录后合并。**
- **症状：API 返回 422 但数据库有合法值。原因：Pydantic 模型、前端选项或响应模型未同步。恢复动作：沿请求→Schema→Repository→数据库逐层定位，不放宽数据库约束来掩盖问题。**
- **症状：旧版本代码无法处理迁移后数据库。原因：变更并非向后兼容。恢复动作：停止服务，按恢复手册选择代码修复或数据恢复；先保留故障现场，不反复尝试不同迁移。**

## 10. 本章 Git 提交

建议分支：`feat/billing-cycle-migration`。数据库和备份不提交，代码按可审查单元拆分：

```powershell
git add specs/ app/ tests/test_migration.py
git commit -m "feat: add billing cycle to subscriptions"
git add scripts/db_backup.py scripts/migrate_001_add_billing_cycle.py scripts/db_restore.py
git commit -m "feat: add SQLite migration and recovery tools"
git add docs/runbooks/database-recovery.md
git commit -m "docs: record database recovery drill"
```

实际暂存前运行 `git diff --stat` 和 `git diff`，不要把演练数据库加入提交。全部检查通过后，再将合并后的版本标记为 v1.2。

## 11. 练习与扩展

1. 在临时数据库插入多行旧数据，迁移后逐行比较导出结果，而非只检查行数。
2. 分别在启用和未启用 WAL 的测试数据库上演练备份，记录操作差异。
3. 为迁移测试增加“列已存在但 `user_version` 仍为 0”的场景，讨论应自动修复还是人工介入。
4. 设计下一次新增字段时保持旧代码兼容的规则，并把规则加入 ADR。
5. 将恢复演练加入每月维护日程，记录备份时间、恢复目标和实际发现的问题。

## 12. 参考资料

- [SQLite：ALTER TABLE](https://sqlite.org/lang_altertable.html)——加列语法与限制。
- [Python：sqlite3 Connection.backup](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.backup)——一致性备份 API。
- [SQLite：PRAGMA integrity_check](https://sqlite.org/pragma.html#pragma_integrity_check)——数据库完整性检查。
- [SQLite：Transaction](https://sqlite.org/lang_transaction.html)——事务与 `BEGIN IMMEDIATE` 行为。

---

# 第 16 章　长期维护系统：依赖、安全、运行观测与文档漂移

> 本章成果：把一次性维护经验变成定期检查、小 PR、自动门禁和恢复演练，完成 v1.2.1 补丁维护闭环。

## 1. 本章成果

完成后，项目应拥有：

- Renovate 依赖更新配置和人工审查规则。
- 基于 `pip-audit` 的依赖安全检查步骤。
- 真实的 `/health` 检查和结构化请求日志。
- 从 FastAPI 路由自动生成 `docs/generated/routes.md`，并用 CI 发现文档漂移。
- 一个检查项目架构边界的小脚本。
- 周期性“维护垃圾回收”流程和自主度分级规则。
- 多个小 PR 合并后发布 v1.2.1。

本章的重点不是接入更多工具，而是让维护工作可重复、可验收、可交接。

## 2. 为什么需要它

项目上线后，需求变化只是维护的一部分。依赖会过期，安全公告会出现，文档会落后，代码会积累重复实现，服务也需要健康检查和日志。等到所有问题一起爆发再处理，通常只能大规模重写。

更有效的策略是把维护拆成小事件：依赖补丁、文档更新、架构违规清理、回归测试补充和备份演练各自形成小 PR。每个 PR 都应有测试或脚本证明，不能靠“看起来没问题”。OpenAI 把这类持续清理工作比喻为代码库的垃圾回收：定期扫描偏差并打开小的重构 PR，避免技术债复利增长。

## 3. 最少必备知识

- **补丁、次要和主版本升级**：风险依次提高，主版本必须人工评估变更日志和兼容性。
- **Dependency Dashboard**：Renovate 汇总待处理依赖更新的 Issue，避免逐个 PR 淹没维护者。
- **供应链风险**：一个包名或某个版本的代码可能在安装阶段执行，不能只看 README。
- **健康检查**：应用自身报告是否满足最低运行条件，例如数据库可查询。
- **文档漂移**：文档、生成文件和实际代码行为不一致。
- **架构约束**：把模块依赖规则写成可执行检查，而不是只写在 Markdown 中。

## 4. 起始项目状态

从完成第15章的 v1.2 项目开始，确认：

1. `data/subscriptions.db` 已包含 `billing_cycle`，且恢复演练记录存在。
2. `python -m pytest -q` 与 `python -m ruff check .` 当前能通过。
3. GitHub Actions 工作流 `.github/workflows/ci.yml` 已运行测试。
4. Git 工作区干净。

建立维护分支：

```powershell
git switch -c chore/maintenance-v1-2-1
git status
python -m pytest -q
python -m ruff check .
```

## 5. 操作步骤与 AI 任务示例

### 步骤 1：先执行只读维护扫描

把扫描任务交给 AI，但要求只读、分类和给证据，不立即修改：

```text
目标：为 Subscription Tracker 执行一次只读维护扫描。
上下文：v1.2；技术栈 Python/FastAPI/SQLite/pytest/Ruff/GitHub Actions；
核心路径 app/、tests/、scripts/、docs/、.github/workflows/。
范围：依赖更新与安全公告、失败或薄弱测试、重复代码、文档与路由漂移、
架构边界违规、备份/恢复手册缺口、日志与健康检查不足。
约束：本轮不得修改文件；不要凭猜测报告；每项必须给出文件路径、命令或代码证据，
并区分事实、建议和风险。
验收：输出按主题分组，每条含严重性、证据、影响、建议动作、预计范围。
输出：Markdown 维护报告草稿，保存到 docs/maintenance/YYYY-MM-DD-scan.md。
```

先获取当前事实：

```powershell
python -m pip list --outdated
python -m pytest -q
python -m ruff check .
```

记录真实输出，不要只保留 AI 的总结。

### 步骤 2：配置 Renovate

在仓库根目录新增 `renovate.json`：

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "dependencyDashboard": true,
  "dependencyDashboardApproval": true,
  "labels": ["dependencies"],
  "prConcurrentLimit": 2,
  "schedule": ["before 09:00 on Monday"],
  "timezone": "Asia/Shanghai",
  "packageRules": [
    {
      "matchManagers": ["pip_requirements"],
      "matchUpdateTypes": ["patch", "minor"],
      "groupName": "Python patch and minor dependencies"
    },
    {
      "matchManagers": ["pip_requirements"],
      "matchUpdateTypes": ["major"],
      "groupName": "Python major dependencies",
      "automerge": false
    }
  ]
}
```

教程中不开启自动合并。配置提交后，由仓库管理员选择 Renovate GitHub App 或自托管方式。配置生效前，仍可使用 `python -m pip list --outdated` 手动审查。

### 步骤 3：建立依赖安全审查流程

安装并运行 `pip-audit` 作为维护工具：

```powershell
python -m pip install pip-audit
python -m pip-audit -r requirements.txt
```

发现漏洞时的审查顺序：

1. 确认漏洞所在包、受影响版本和修复版本。
2. 检查项目是否真实调用了受影响功能。
3. 优先选择同一大版本内的修复版本。
4. 主版本升级必须阅读变更日志，并在分支中运行全部测试。
5. 若短期无法升级，在 `docs/maintenance/` 记录风险、临时缓解措施和复查日期。
6. 不在公开报告中直接粘贴敏感路径、密钥或内网地址。

### 步骤 4：补充健康检查和请求日志

新增 `app/health.py`：

```python
import os
import sqlite3
from pathlib import Path

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    database = Path(os.getenv("DATABASE_PATH", "data/subscriptions.db"))
    if not database.is_file():
        raise HTTPException(status_code=503, detail="database file is missing")
    try:
        connection = sqlite3.connect(
            f"file:{database.resolve().as_posix()}?mode=ro",
            uri=True,
            timeout=1,
        )
        connection.execute("SELECT 1").fetchone()
        connection.close()
    except sqlite3.Error:
        raise HTTPException(status_code=503, detail="database is unavailable")
    return {"status": "ok", "database": "connected"}
```

在 `app/main.py` 接入路由，并按项目现有导入风格调整：

```python
from app.health import router as health_router

app.include_router(health_router)
```

请求日志只记录方法、路径、状态码和耗时，避免查询参数、请求体和个人数据：

```python
import logging
import time

from fastapi import Request

logger = logging.getLogger("subscription_tracker")


@app.middleware("http")
async def log_request(request: Request, call_next):
    start = time.monotonic()
    response = await call_next(request)
    logger.info(
        "request method=%s path=%s status=%s duration_ms=%.1f",
        request.method,
        request.url.path,
        response.status_code,
        (time.monotonic() - start) * 1000,
    )
    return response
```

新增 `tests/test_health.py`，使用项目已有的 FastAPI 测试客户端：

```python
def test_health_reports_ok(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "connected"}
```

### 步骤 5：生成路由文档并检测漂移

新增 `scripts/export_routes.py`。它从真实应用对象导出路由，而不是让 AI 根据 README 猜接口：

```python
from pathlib import Path

from fastapi.routing import APIRoute

from app.main import app

OUTPUT = Path("docs/generated/routes.md")


def main() -> None:
    rows = []
    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue
        methods = sorted(route.methods - {"HEAD", "OPTIONS"})
        rows.append(f"| {route.path} | {', '.join(methods)} | {route.endpoint.__module__} |")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    content = "\n".join(
        [
            "# 自动生成的路由清单",
            "",
            "运行 `python scripts/export_routes.py` 更新，不要手工编辑。",
            "",
            "| 路径 | 方法 | 处理模块 |",
            "|---|---|---|",
            *rows,
            "",
        ]
    )
    OUTPUT.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
```

生成后检查文档是否与代码一致：

```powershell
python scripts/export_routes.py
git diff --exit-code -- docs/generated/routes.md
```

若命令返回差异，说明有人修改路由后没有重新生成文档；执行脚本并单独提交结果。

### 步骤 6：把架构边界写成可执行检查

新增 `scripts/check_architecture.py`，检查数据访问和底层模块不反向依赖上层：

```python
import ast
import sys
from pathlib import Path

FORBIDDEN_IMPORTS = {
    Path("app/repository.py"): {"fastapi", "app.routes"},
    Path("app/database.py"): {"fastapi", "app.routes", "app.repository"},
}


def imported_names(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def main() -> int:
    errors = []
    for path, forbidden in FORBIDDEN_IMPORTS.items():
        if not path.exists():
            continue
        for name in imported_names(path):
            if any(name == bad or name.startswith(bad + ".") for bad in forbidden):
                errors.append(f"{path}: forbidden import {name}")
    if errors:
        print("\n".join(errors))
        return 1
    print("architecture checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

运行：

```powershell
python scripts/check_architecture.py
```

发现违规时，移动依赖或调整职责；不要直接删除检查。若项目新增模块，把规则写入脚本和 `ARCHITECTURE.md`，使文字与检查一致。

### 步骤 7：把维护检查接入 CI

在现有 CI 工作流中增加以下步骤，命令应与本地一致：

```yaml
      - name: Check architecture boundaries
        run: python scripts/check_architecture.py
      - name: Regenerate route documentation
        run: python scripts/export_routes.py
      - name: Ensure generated documentation is committed
        run: git diff --exit-code -- docs/generated/routes.md
      - name: Audit Python dependencies
        run: |
          python -m pip install pip-audit
          python -m pip-audit -r requirements.txt
```

`pip-audit` 可能因新公告失败，这正是维护信号；不要为了让 CI 变绿而跳过检查。若漏洞不影响当前使用，记录风险与复查时间，再决定缓解方案。

### 步骤 8：建立每周垃圾回收流程

每周固定一次只读扫描，AI 输出问题清单，人挑选 2—3 个风险最高且范围最小的项目，再让 AI 分别生成小 PR。典型分类：

- 依赖补丁或安全修复
- 文档与生成清单更新
- 重复 helper 合并
- 缺失测试补充
- 架构违规修正
- 运行手册或备份演练更新

自主度从低到高分级：

| 级别 | AI 权限 | 人工职责 |
|---|---|---|
| L0 | 只读扫描和报告 | 审阅全部证据，决定后续动作 |
| L1 | 生成计划和 Diff，不修改文件 | 批准计划后授权实现 |
| L2 | 在隔离分支完成小任务 | 审查 Diff、运行测试并决定是否合并 |
| L3 | CI 失败后提交修复 PR | 检查失败原因、修复范围和回归证据 |
| L4 | 低风险补丁按明确策略自动提 PR | 设定策略、抽查日志，必要时人工合并 |
| L5 | 多环节自动执行 | 只适用于范围、权限、审计和回滚都已固化的任务 |

教程主线建议停在 L2—L3。涉及生产数据、密钥、发布和回滚的操作，必须保留人工审批。

### 步骤 9：发布 v1.2.1

当所有维护 PR 合并、CI 通过后：

```powershell
git switch main
git pull
python -m pytest -q
python -m ruff check .
python scripts/check_architecture.py
python -m pip-audit -r requirements.txt
```

随后按照第11章的发布流程打标签、更新发布说明，并记录每个 PR 解决的问题。补丁版本不应夹带未验收的新功能。

## 6. AI 应生成的产物

本章 AI 应输出：

- 只读维护扫描报告，含证据和风险分级。
- `renovate.json` 及其审查规则说明。
- 依赖安全审查记录。
- 健康检查、日志和测试代码。
- `scripts/export_routes.py`、`scripts/check_architecture.py` 与生成文档。
- CI 工作流更新。
- 每周维护流程和自主度政策。
- 发布 v1.2.1 前的检查清单。

不要把上述内容塞进一个“自动维护”大 Skill；先让每个检查可单独运行和验收。

## 7. 人工检查点

1. **依赖更新是否最小**：PR 只改依赖和相关测试，不夹带功能。
2. **安全公告是否相关**：区分“依赖有漏洞”和“项目调用路径受影响”。
3. **健康检查是否真的检测依赖**：`/health` 不能只返回固定 `ok`。
4. **日志是否安全**：没有密钥、完整查询参数、个人订阅数据或内网地址。
5. **生成文档是否由脚本产生**：人工编辑 `docs/generated/` 会让漂移检查失去意义。
6. **架构检查是否反映真实边界**：不能通过放宽规则或跳过脚本来通过 CI。
7. **维护 PR 是否可独立回滚**：每个 PR 有清晰范围和验收记录。

## 8. 验收命令与通过标准

```powershell
python -m pytest -q
python -m ruff check .
python scripts/check_architecture.py
python scripts/export_routes.py
git diff --exit-code -- docs/generated/routes.md
python -m pip-audit -r requirements.txt
python -m uvicorn app.main:app
```

另开 PowerShell：

```powershell
$health = Invoke-RestMethod http://127.0.0.1:8000/health
if ($health.status -ne "ok") { throw "health check failed" }
$health
```

通过标准：测试、Ruff、架构检查、文档一致性检查和安全审计都有真实结果；健康检查能访问数据库并返回 `ok`；CI 在干净检出中执行同一组检查；所有维护修改由小 PR 组成；发布说明列出变更、风险和回滚方式。

## 9. 常见失败及恢复方法

- **症状：Renovate 一次产生大量 PR。原因：没有分组、排期和并发限制。恢复动作：关闭噪声 PR，更新 `packageRules`、`schedule` 和 `prConcurrentLimit`，先处理补丁与安全公告。**
- **症状：`pip-audit` 持续失败但漏洞似乎无关。原因：存在受影响版本或传递依赖。恢复动作：确认调用路径，优先选择修复版本；无法升级时记录风险、缓解措施和复查日期。**
- **症状：数据库不可用但 `/health` 返回 `ok`。原因：健康检查没有真实查询数据库。恢复动作：加入文件存在性和 `SELECT 1` 检查，异常时返回 503，并补充失败路径测试。**
- **症状：CI 的文档一致性检查失败。原因：路由变化后未重新生成文档。恢复动作：运行导出脚本并提交 `docs/generated/routes.md`，不要手工改生成文件。**
- **症状：架构检查失败。原因：底层模块引入了上层依赖。恢复动作：调整模块职责或依赖方向；不要删除规则，除非 ADR 记录了边界变化。**
- **症状：AI 每周维护报告重复但问题没减少。原因：只扫描不关闭。恢复动作：限制每次最多处理 2—3 个事项，为每项指定 PR、验收证据和复查日期。**

## 10. 本章 Git 提交

建议按主题拆分 PR，而不是一个“维护大杂烩”：

```powershell
git add renovate.json docs/maintenance/
git commit -m "chore: add dependency maintenance policy"

git add app/health.py app/main.py tests/test_health.py
git commit -m "feat: add database-aware health check"

git add scripts/export_routes.py docs/generated/routes.md
git commit -m "docs: generate API route inventory"

git add scripts/check_architecture.py .github/workflows/ci.yml
git commit -m "ci: enforce architecture and generated docs"
```

实际执行前使用 `git diff --stat` 检查每个 PR 的影响范围。维护日志、扫描报告和发布说明应随对应 PR 或发布流程提交。

## 11. 练习与扩展

1. 模拟一次补丁升级失败：在分支中安装一个旧版本依赖，记录失败测试、根因和恢复步骤。
2. 故意在 `app/database.py` 中加入一个上层导入，观察架构检查如何阻止合并，然后修复违规。
3. 连续四周执行只读维护扫描，统计每类问题数量和平均关闭时间。
4. 为 `/health` 增加数据库文件缺失或不可读的失败测试，验证返回 503。
5. 把当前自主度政策写成 `docs/maintenance/autonomy.md`，明确哪些操作永远需要人工批准。
6. 选择一个真实依赖公告，完成影响分析、升级测试和发布记录。

## 12. 参考资料

- [Renovate：Configuration options](https://docs.renovatebot.com/configuration-options/)——分组、排期、审批和并发限制。
- [Renovate：Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/)——集中管理待处理更新。
- [pip-audit](https://github.com/pypa/pip-audit)——Python 依赖漏洞扫描。
- [FastAPI：Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)——请求日志中间件。
- [OpenAI：Harness Engineering](https://openai.com/zh-Hant/index/harness-engineering/)——持续清理代码库与工程反馈回路。

---

# 综合实验四：完成一次完整的需求演化（v1.1）

> 实验成果：从一条 Issue 出发，完成规格变更、影响分析、新功能、回归测试、局部重构、数据库迁移、发布的全链路，项目演进到 v1.1。

## 实验目标

验证核心主张：**演化中的项目不需要推翻重来，而是按规格→计划→实现→验证→发布的既有循环小步推进。** 本实验是前 16 章方法的综合应用，也是结业项目（第 20 章）的彩排。

## 演化剧本（按顺序执行）

```text
ISSUE-021 用户报告：导出 CSV 的特殊字符列错位（Bug）
  → ISSUE-022 新需求：按名称搜索与按状态筛选订阅（Feature）
     → 重构：臃肿的 routes.py 拆分（Refactor）
        → 数据：为筛选新增 status 字段（Migration）
           → 发布 v1.1（Release）
```

四类工作交叉进行，正是真实维护的日常节奏。

## 第一幕：Bug 修复（ISSUE-021）

### 步骤

1. 用 `templates/issue.md` + `templates/bug-report.md` 写规范报告（含复现与证据）。
2. **先写回归测试（红）**：名称含 `,`、`"`、换行三种样本的导出断言。
3. 让 AI 会话修复（根因：导出未用 csv 模块转义），范围仅限导出代码。
4. 修复后回归测试变绿；`pytest -q` 全绿；`docs/behavior-baseline.md` 更新导出行为条目。
5. 用 `templates/pr-checklist.md` 审查后合并（fix 提交）。

### 关键纪律

- 修复 PR 中回归测试先于实现提交（先红后绿的证据要留存）。
- 不顺手修其他怪行为——它们各有各的 Issue。

## 第二幕：新功能（ISSUE-022 搜索与筛选）

### 步骤

1. **改规格先行**：`specs/` 中新增搜索/筛选验收场景（Given/When/Then），spec 版本升为 v0.2 并记录变更原因。
2. 用 `templates/plan.md` 写变更计划：影响 routes/repository/schemas/前端；验证策略；回滚思路。
3. 拆任务入 `docs/tasks.md`（每条 ≤ 半天、可独立验证）。
4. 逐任务走第 8 章闭环：任务包 → Diff 审查 → 运行验证 → 独立提交。
5. 前端交互补一条接口测试与手工验收（搜索“云盘”只返回匹配项）。

### 关键纪律

- 功能提交（feat）与修复提交（fix）分开；规格版本号随行为变化递增。
- AI 声称搜索可用 ≠ 可用——用 curl + 真实数据验证。

## 第三幕：局部重构

### 步骤

1. 识别目标：v1.1 迭代中 routes.py 超过既有单文件约定（参照第 14 章 ruff 统计确认臃肿事实）。
2. **确认保护网**：当前 pytest 全绿（这是重构合法性的唯一依据）。
3. 拆分方向：按资源拆 `routes/subscriptions.py`、抽取公共校验依赖；纯机械搬迁，零行为变化。
4. 每拆一步：pytest 全绿 + 手工冒烟（添加→搜索→删除）→ 独立提交。
5. 提交信息用 `refactor:` 前缀，与功能/修复提交明确区分。

### 关键纪律

- 重构 PR 不含任何行为变化——reviewer 检查点就是“diff 里找不到语义变化”。
- 若保护网不绿，先修复再重构，禁止带病重构。

## 第四幕：数据库迁移（status 字段）

### 步骤

1. 备份：`python scripts/backup_db.py`，并对备份执行 `PRAGMA integrity_check`。
2. 写迁移脚本 `scripts/migrations/002_add_status.py`：`ALTER TABLE subscriptions ADD COLUMN status TEXT NOT NULL DEFAULT 'active'`；脚本必须幂等（重复执行不报错）。
3. 测试库演练迁移一次；旧数据读取冒烟（迁移前 10 条记录全部可读且 status='active'）。
4. 应用迁移 + 新功能按 status 筛选的验收场景补测。
5. 记录回滚边界（写入发布说明）：**代码可 revert，已 ALTER 的列不可自动消失**——数据回滚 = 从备份还原，有数据丢失窗口。

### 关键纪律

- 迁移前备份是硬性前置（第 15 章详述边界）。
- 迁移脚本独立提交（`migration:` 前缀），不与功能提交混合。

## 第五幕：发布 v1.1

1. 走 `templates/release-checklist.md` 全流程（干净环境、CI、迁移演练、回滚方案）。
2. 发布说明必须包含：四幕变更摘要、status 字段的回滚边界声明、已知问题。
3. `git tag -a v1.1 && git push --tags`。

## 自检表

| # | 检查项 | 通过标准 |
|---|---|---|
| 1 | Bug 有规范 Issue + 回归测试先红后绿 | 证据留存 |
| 2 | 新功能先改规格后编码 | spec 版本递增记录 |
| 3 | 任务拆分与验证方法完整 | tasks.md 无空验证列 |
| 4 | feat/fix/refactor/migration 提交分离 | `git log --oneline` 可辨 |
| 5 | 重构零行为变化 | 冒烟 + pytest 全绿证据 |
| 6 | 迁移前备份 + integrity_check 通过 | 备份路径记录 |
| 7 | 迁移幂等 | 重复执行不报错 |
| 8 | 回滚边界（代码/数据）写入发布说明 | 文档可见 |
| 9 | 干净环境复现 v1.1 | clone→install→test→run |
| 10 | CI 全绿 + 标签 v1.1 | run 链接 + `git tag` |

## 常见失败与恢复

**失败 1：修 Bug 时顺手重构导出模块。**
恢复：revert 重来；fix 提交里只允许根因修复。重构单独立项走第三幕流程。

**失败 2：新功能没改规格直接编码。**
恢复：停下补规格；对照验收场景逐条补测；把“先规格后代码”写进 `AGENTS.md`。

**失败 3：迁移直接在正式库执行，无备份。**
恢复：立即停止；若有备份按第 15 章恢复步骤还原；把备份步骤写入 CI 前置脚本或发布 checklist 硬性项。

**失败 4：重构 PR 里混入了“顺便优化搜索”。**
恢复：`git reset` 拆分提交；语义变化移回第二幕的任务流。

**失败 5：AI 把幂等迁移写成“每次都加列”。**
恢复：脚本加存在性检查（`PRAGMA table_info`）；测试库重复执行两次验证不报错；此坑记入失败案例库。

## 完成标准

自检表 10/10；`v1.1` 标签存在；四幕的提交历史类型清晰可辨；发布说明含回滚边界。

## 下一步

第 15—16 章将把本实验第四幕的迁移经验扩展成完整的备份恢复体系与长期维护机制；实验五则把时间快进三个月。

---

# 综合实验五：模拟项目上线三个月

> 实验成果：在不推翻项目的前提下，随机处理六个真实维护事件，形成可审计的三个月维护记录，并发布一个经过验证的补丁版本。

本实验假设你已经完成 [第12章](../chapters/ch12-issue-driven-maintenance.md)、[第13章](../chapters/ch13-change-and-refactoring.md)、[第15章](../chapters/ch15-data-migration-recovery.md) 和 [第16章](../chapters/ch16-long-term-maintenance.md)。项目当前版本应为 v1.2，`subscriptions` 表已包含 `billing_cycle`。

## 1. 实验目标

证明项目不仅能生成，还能在上线后应对：

- 用户缺陷和功能变化。
- 依赖补丁、安全公告和升级失败。
- 数据库备份、恢复与代码回滚。
- 文档、生成清单和架构规则漂移。
- 运行日志、健康检查与故障定位。
- 新 AI 会话或新维护者接手。

最终交付物不是“AI 说维护完成”，而是命令、Diff、测试、PR、备份文件、健康检查和复盘记录。

## 2. 开始前的项目基线

在项目根目录执行：

```powershell
git status
python -m pytest -q
python -m ruff check .
python scripts/check_architecture.py
python scripts/export_routes.py
git diff --exit-code -- docs/generated/routes.md
python -m pip-audit -r requirements.txt
python -m pip list --outdated
```

把真实输出保存到：

```text
docs/maintenance/lab05/baseline.md
```

如果任何基线检查失败，先修复原问题并开始新的基线。不要把旧失败混入随机维护事件。

建议从干净状态创建实验记录目录：

```powershell
New-Item -ItemType Directory -Force docs/maintenance/lab05
```

## 3. 随机事件卡

事件池如下。每张卡都模拟一种上线后可能出现的维护压力。

| 编号 | 事件 | 必须留下的证据 |
|---|---|---|
| M01 | 用户报告 CSV 导出或列表页漏掉 `billing_cycle` | Issue、回归测试、修复 Diff、API 或导出结果 |
| M02 | Renovate 或 `pip list --outdated` 发现补丁升级，但 CI 失败 | 失败日志、根因、修复 PR 或暂缓记录 |
| M03 | `pip-audit` 报告一个依赖漏洞 | 漏洞编号或输出、影响分析、升级/缓解决定 |
| M04 | 需要验证迁移后备份仍可恢复 | 备份文件、恢复命令、恢复后查询结果 |
| M05 | README 或生成路由文档与实际 API 不一致 | 文档 Diff、导出脚本运行结果、CI 检查 |
| M06 | `app/repository.py` 或 `app/database.py` 出现禁止的上层依赖 | 架构检查失败输出、修复 Diff、重新通过记录 |
| M07 | 数据库不可用时 `/health` 未返回故障，或日志无法定位请求 | 健康检查测试、日志样本说明、修复 Diff |
| M08 | 两个模块出现重复 helper 或重复校验逻辑 | 重复位置、合并 Diff、测试结果 |
| M09 | 用户要求按币种筛选订阅 | Spec Delta、验收场景、功能测试、PR |
| M10 | 迁移或 API 的非法 `billing_cycle` 缺少测试 | 新增测试、失败前后证据 |
| M11 | 模拟一次补丁发布后发现启动失败，需要回滚 | 发布记录、回滚命令、回滚后健康检查 |
| M12 | 一个全新 AI 会话必须接手项目并完成一个小任务 | 交接文档、AI 任务说明、Diff 和验收记录 |

在 PowerShell 中随机抽取六张卡：

```powershell
$cards = @("M01","M02","M03","M04","M05","M06","M07","M08","M09","M10","M11","M12")
$draw = Get-Random -InputObject $cards -Count 6
$draw
```

如果团队需要复现同一组事件，可指定种子：

```powershell
$draw = Get-Random -InputObject $cards -Count 6 -SetSeed 20261124
$draw
```

把实际抽到的编号写入 `docs/maintenance/lab05/event-draw.md`，不要预填结果。

## 4. 三个月节奏

六张卡分成三个月，每月两张：

| 月份 | 重点 | 处理卡片 |
|---|---|---|
| 第 1 个月 | 稳定基线，处理缺陷和文档/架构漂移 | 抽到的第 1—2 张 |
| 第 2 个月 | 依赖、安全、观测和恢复能力 | 抽到的第 3—4 张 |
| 第 3 个月 | 小功能演化、发布和交接 | 抽到的第 5—6 张 |

如果随机结果使某个月负担过重，可以调整月份顺序，但必须在日志中说明原因。

每月按以下循环处理每张卡：

1. 把事件写成 Issue 或 Bug Report，使用 [Issue 模板](../templates/issue.md) 和 [Bug 报告模板](../templates/bug-report.md)。
2. 判断是否需要修改规格；功能变化必须先更新 Spec Delta。
3. 建立单独分支，例如 `fix/m01-csv-billing-cycle`。
4. 先写能暴露问题的测试或检查，再让 AI 修复。
5. 让 AI 输出计划、影响文件和 Diff，不直接接受“已完成”。
6. 运行相关测试、全量测试、Ruff 和架构检查。
7. 按 [PR 检查清单](../templates/pr-checklist.md) 人工审查。
8. 合并后更新 [运行维护手册](../templates/runbook.md) 或相关文档。
9. 在维护日志记录实际命令、证据、风险和耗时。

每月结束时，若已有合并且验证的维护 PR，可按第11章和第16章流程发布补丁版本。不要为了凑版本号发布未验收内容。

## 5. AI 协作规则

允许使用 AI，但必须遵守：

- 每张卡先让 AI 做只读分析，再授权修改。
- 每次任务都提供当前项目状态、范围、约束和验收标准。
- AI 的完成声明必须附命令、测试结果、Diff 或文件路径。
- 不让 AI 自评分数；评分由你根据客观证据完成。
- 不让 AI 直接修改 `main`、删除数据库或覆盖备份。
- 涉及恢复、发布和依赖安全时，人工保留最终批准。

一个标准任务示例：

```text
目标：处理事件卡 M05，修复生成路由文档与实际 API 不一致的问题。
上下文：项目为 Subscription Tracker v1.2；已有 scripts/export_routes.py、
docs/generated/routes.md 和 CI 文档一致性检查。
范围：只允许修改生成文档、导出脚本、相关测试和必要说明。
约束：先运行导出脚本并给出真实差异；不得手工编辑 docs/generated/routes.md；
不得改变现有 API 行为；不得删除 CI 检查。
验收：git diff --exit-code -- docs/generated/routes.md 通过；相关测试通过；
维护日志记录命令和证据。
输出：差异摘要、修改文件、执行命令、真实结果和剩余风险。
```

## 6. 维护日志

每张卡写一份记录，保存到 `docs/maintenance/lab05/`，例如 `month-1-M05.md`：

```markdown
# 事件卡 M05：文档与实际 API 不一致

- 日期：YYYY-MM-DD
- 触发方式：随机事件卡 / 用户报告 / CI 失败
- 基线命令与结果：
- 问题复现：
- 规格或文档变更：
- 分支与 PR：
- AI 任务与主要回答摘要：
- 人工审查结论：
- 执行命令：
- 真实证据：
- 风险与回滚方式：
- 实际耗时：
- 后续复查事项：
```

“真实证据”应粘贴命令的关键输出、测试名称、PR 链接、文件路径或恢复核验结果。不要粘贴密钥、个人订阅数据或内网地址。

## 7. 评分表

总分 100 分。评分时逐项写证据位置；没有证据的项不得分。

| 项目 | 分值 | 满分标准 |
|---|---:|---|
| 基线与事件抽取 | 5 | 保存真实基线输出，记录随机抽取结果和月份安排 |
| 六个事件完成度 | 30 | 每张卡 5 分：有 Issue、计划、实现、证据和复查事项 |
| 测试与 CI | 15 | 新增或修复行为均有测试；全量测试和 Ruff 通过；CI 或等价命令有真实结果 |
| 依赖与安全 | 10 | 至少处理一次过期依赖或安全公告，记录影响分析、升级/缓解决定和复查日期 |
| 备份与恢复 | 10 | 至少完成一次备份、恢复和核验；说明代码回滚、数据恢复和前向修复的边界 |
| 文档、架构与观测 | 10 | 文档/生成清单一致；架构检查通过；健康检查或日志能支持定位问题 |
| 交接与复盘 | 10 | 新 AI 会话能凭仓库和交接文档完成一个小任务；复盘写出三类问题和后续动作 |
| 过程纪律 | 10 | 小 PR、独立分支、人工审查、无未记录修改、无伪造证据 |

### 评分等级

| 总分 | 结论 |
|---|---|
| 90—100 | 可以独立承担个人项目长期维护 |
| 75—89 | 基本合格，需补齐证据不足的项目 |
| 60—74 | 重新完成薄弱事件卡，并补写维护日志 |
| 0—59 | 回到第12—16章，先完成每章验收再做实验 |

### 强制不合格条件

出现以下任一情况，本实验不通过：

- 伪造命令输出、测试结果或发布记录。
- 没有备份/恢复证据，却声称可以回滚。
- 所有修改直接提交到 `main`，没有审查记录。
- 六张卡少于四张完成。
- AI 的“完成”声明被当作唯一证据。

## 8. 最终复盘

完成六张卡后，写 `docs/maintenance/lab05/retrospective.md`，至少回答：

1. 哪类事件最容易演变成大 PR？为什么？
2. 哪些检查应该固化为脚本或 CI，而不是提醒 AI 注意？
3. 哪些文档必须人工维护，哪些应由脚本生成？
4. 当前项目适合哪一级 AI 自主度？哪些操作必须人工批准？
5. 下一个三个月应优先处理哪三类维护债？
6. 如果新维护者只读仓库，能否接手？缺什么？

复盘应引用具体事件卡、命令和文件路径，不写“整体还不错”这类无证据结论。

## 9. 最终提交物

```text
docs/maintenance/lab05/
├─ baseline.md
├─ event-draw.md
├─ month-1-*.md
├─ month-2-*.md
├─ month-3-*.md
├─ retrospective.md
└─ score.md
```

同时保留：

- 六个事件对应的分支或 PR 记录。
- 新增/修改的测试、脚本、文档和配置。
- 一次补丁版本发布或明确的“暂不发布”决定。
- 恢复演练产生的备份文件和核验记录。

## 10. 与其他章节的关系

- 缺陷和 Issue 流程见 [第12章](../chapters/ch12-issue-driven-maintenance.md)。
- 功能变化与重构见 [第13章](../chapters/ch13-change-and-refactoring.md)。
- 旧项目分析和基线建立见 [第14章](../chapters/ch14-legacy-modernization.md)。
- 数据库迁移、备份和恢复见 [第15章](../chapters/ch15-data-migration-recovery.md)。
- Renovate、安全审计、健康检查、文档漂移和自主度分级见 [第16章](../chapters/ch16-long-term-maintenance.md)。
- 完成定义参考 [完成定义模板](../templates/definition-of-done.md) 和 [会话交接模板](../templates/handoff.md)。

这个实验的目标不是让项目“看起来被维护过”，而是证明：三个月后，项目仍能通过客观检查被理解、修改、验证、发布和恢复。

---

# 第 17 章　Skill 工程：把有效协作流程变成项目资产

> 本章成果：为订阅管理器创建一个可版本化、可测试的小型验证 Skill，并用真实任务判断它是否值得保留。

## 1. 本章成果

前面的章节已经反复执行“读验收条件→检查 Diff→运行测试→记录结果”。本章把这套流程整理为 `verify-change` Skill。完成后，你将得到：

```text
skills/verify-change/
├─ SKILL.md
├─ references/checks.md
├─ scripts/check_report.py
└─ evals/evals.json
```

`skills/` 是仓库内的源目录，用来审阅和版本管理；不同 Agent 的自动发现目录并不相同，实际安装或链接位置以所用工具的文档为准。即使暂时没有自动加载，这个目录仍是可共享的项目资产。

## 2. 为什么需要它

聊天记录里的好提示词很难复用：下一次可能漏掉测试，也可能把“页面能打开”写成“交付完成”。Skill 适合保存**重复发生、步骤相对稳定、产出可以检查**的流程。

但 Skill 不是项目的全部规则。五种载体各有职责：

| 载体 | 保存什么 | 何时生效 | 典型例子 |
|---|---|---|---|
| `AGENTS.md` | 全项目长期约定和入口 | Agent 工作时 | 安装命令、目录边界、提交要求 |
| Skill | 某类任务的操作流程 | 任务匹配时加载 | 验证一次变更、处理一个 Issue |
| Script | 确定性计算与检查 | 被命令调用时 | 检查报告结构、生成项目地图 |
| Hook | 某事件前后的自动动作 | 工具事件发生时 | 写文件后运行格式化 |
| CI | 独立的交付质量门禁 | 推送或 PR 时 | 安装依赖、测试、Ruff、构建 |

原则是：**需要判断的流程交给 Skill，需要每次都遵守的入口写进 AGENTS.md，能够确定执行的事情交给脚本、Hook 或 CI。** 不要把同一个规则在五处各写一份；保留一个事实来源，其余位置只放链接。

## 3. 最少必备知识

一个 Skill 通常有三层信息：

1. **元数据**：`name` 与 `description` 经常处于可见状态，主要决定何时触发。
2. **SKILL.md 正文**：匹配后加载，写操作顺序、输入输出和停止条件。
3. **随附资源**：`references/` 保存按需读取的说明，`scripts/` 保存可执行程序，`assets/` 保存输出需要的模板。

这叫渐进披露。它的目的不是追求文件数量，而是避免每次任务都加载所有知识。正文若不断膨胀，应把某个专题移入引用文件，并明确“何时读取它”。

还要区分两类评测：**触发评测**回答“该用时是否用了、不该用时是否误用”；**执行评测**回答“触发后是否真正完成了任务”。只测其中一类，会漏掉另一半问题。

## 4. 起始项目状态

本章从第 16 章后的 `v1.2.1` 开始。项目应当已有：

- `AGENTS.md`、`ARCHITECTURE.md` 和有效的验收文档；
- 可运行的 `python -m pytest -q` 与 `python -m ruff check .`；
- 第 13 章的搜索筛选功能及其测试；
- 一个干净的 Git 工作区。

先建立基线：

```powershell
git status
python -m pytest -q
python -m ruff check .
```

如果基线失败，先回到第 9 章处理，不要把原有问题伪装成 Skill 的评测失败。

## 5. 操作步骤与 AI 任务示例

### 第一步：写出单一用途和输入输出契约

本例只负责“验证一次已经完成的变更”，不负责实现功能，也不自动合并 PR。输入是任务、验收条件和当前 Diff；输出是一份验证报告。先把这个边界写在一页纸内，再创建文件。

### 第二步：创建 SKILL.md

```markdown
---
name: verify-change
description: Verify a completed code change against its acceptance criteria, inspect its diff, run project checks, and produce an evidence report. Use whenever the user asks whether a change, bug fix, or PR is ready, even if they only say "帮我验收一下".
---

# Verify a change

1. Read the task, acceptance criteria, AGENTS.md, and references/checks.md.
2. Inspect `git status`, `git diff --stat`, and `git diff`. Report unrelated changes.
3. Run the relevant commands from references/checks.md. Record real exit codes and important output.
4. Create the requested report under `docs/verification/` with these sections: `验收命令`, `实际结果`, `遗留风险`.
5. Run `python skills/verify-change/scripts/check_report.py REPORT_PATH` to check report completeness.
6. State readiness only from observed evidence. If a command fails, mark verification failed and leave implementation to a separate task.
```

正文使用命令式步骤，并解释验收条件来自项目而非模型想象。不要在这里塞入所有 API 知识。

### 第三步：添加按需引用

`references/checks.md` 保存本项目特定的检查：

```markdown
# Subscription Tracker checks

Run for every behavior change:
- `python -m pytest -q`
- `python -m ruff check .`
- `git diff --check`

For API changes, also exercise `/api/subscriptions` and `/health` against the running app.
Do not treat a report-structure check as proof that tests passed.
```

### 第四步：添加确定性脚本

`scripts/check_report.py` 只检查报告是否具备必要证据栏位：

```python
import sys
from pathlib import Path

REQUIRED = ("## 验收命令", "## 实际结果", "## 遗留风险")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_report.py REPORT_PATH")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"missing report: {path}")
        return 1
    text = path.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED if heading not in text]
    if missing:
        print("missing sections: " + ", ".join(missing))
        return 1
    print("report structure: OK; test results still require review")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

这个脚本有意不判断“测试是否通过”；退出码和输出才是行为证据。

### 第五步：准备执行评测

`evals/evals.json` 使用同一项目、同一提交上的真实任务：

```json
{
  "skill_name": "verify-change",
  "evals": [
    {
      "id": 1,
      "prompt": "检查搜索筛选变更是否可交付，并保存验证报告。",
      "expected_output": "报告包含验收条件、真实命令结果和遗留风险。",
      "files": [],
      "expectations": [
        "读取验收条件并检查 Diff",
        "实际运行 pytest 与 Ruff",
        "报告没有把结构检查当作测试通过"
      ]
    },
    {
      "id": 2,
      "prompt": "这个改动里有一项测试失败，请验收并给出结论。",
      "expected_output": "明确验收失败，保留失败证据，不擅自改实现。",
      "files": [],
      "expectations": ["结论为未通过", "记录失败命令", "没有修改业务代码"]
    }
  ]
}
```

分别在“加载 Skill”和“不加载 Skill”的新会话执行同一提示，保存报告和真实命令结果，再按 expectations 评分。触发测试另备正例与近似的负例，例如“只解释 pytest 的 `-q` 参数，不操作仓库”不应触发。

### 第六步：让 AI 协助修订，而不是代评自己

```text
目标：改进 verify-change Skill。
上下文：SKILL.md、checks.md、evals.json，以及两组同任务评测产物。
范围：只修改 skills/verify-change/。
约束：保留只读验证边界；减少重复指令；不得根据一次成功就宣称普遍有效。
验收：每个修改都对应一个观察到的失败；补充误触发或漏触发用例。
输出：变更 Diff、失败模式表、下一轮评测计划。
```

## 6. AI 应生成的产物

AI 最终应交付四类东西：Skill 源文件、检查脚本、评测用例、评测结果表。结果表至少记录任务、是否触发、期望是否满足、实际证据、耗时或资源消耗（工具能提供时才记录）。

验证报告本身可以采用：

```markdown
# 搜索筛选变更验证
## 验收命令
## 实际结果
## 遗留风险
```

“实际结果”必须写真实退出码、失败摘要和报告路径；不知道的项目写“未验证”，不能补成“通过”。

## 7. 人工检查点

- 看 `description` 是否同时说明“做什么”和“何时使用”，有没有过宽到所有编码任务都触发。
- 看 Skill 是否仍只做验证；若它开始实现功能、部署和合并，应拆分。
- 看引用文件是否确实按需读取，正文是否又复制了一遍。
- 抽查一条命令输出与报告是否一致。
- 比较加载与未加载 Skill 的结果：若两者一样好，这个 Skill 可能没有价值；若只是更长而没有提高正确性，也不应保留。
- 检查负例是否足够接近真实场景，而不是用完全无关的问题充当“误触发测试”。

## 8. 验收命令与通过标准

创建一份实际报告后执行：

```powershell
python skills\verify-change\scripts\check_report.py docs\verification\search-filter.md
python -m pytest -q
python -m ruff check .
git diff --check
```

macOS/Linux 将报告脚本路径中的反斜杠换为正斜杠。通过标准是：报告结构检查成功；测试与 Ruff 的真实退出码均为 0；Diff 没有空白错误；触发正例能使用 Skill、近似负例不会误用；执行评测中的每条 expectation 都有可定位证据。评测若出现波动，重复运行并保留差异，不用一次结果下结论。

## 9. 常见失败及恢复方法

1. **症状：所有编码请求都触发。** 原因：描述只写“处理项目变更”。恢复：限定为“已完成变更的验收与证据报告”，加入实现、解释概念等负例。
2. **症状：报告结构合格，但测试其实失败。** 原因：把脚本结果当成质量结论。恢复：查看原始退出码，将验证标记失败；脚本只负责结构。
3. **症状：SKILL.md 越来越长。** 原因：所有场景都堆进正文。恢复：按场景拆入 `references/`，正文保留选择规则与共同步骤。
4. **症状：加载 Skill 后仍漏跑检查。** 原因：命令只存在于聊天或文档中。恢复：在 `checks.md` 保留唯一命令清单，并加入对应 expectation。
5. **症状：新 Skill 与 AGENTS.md 冲突。** 原因：同一规则多处漂移。恢复：确定事实来源，另一处改为链接后重新评测。

## 10. 本章 Git 提交

建议使用 `feat/verify-change-skill` 分支，拆成两次提交：

```powershell
git switch -c feat/verify-change-skill
git add skills/verify-change
git commit -m "feat: add change verification skill"
git add skills/verify-change/evals docs/verification
git commit -m "test: evaluate change verification skill"
```

若验证报告含有真实项目临时数据，只提交去敏后的样例，不提交数据库、日志或凭据。

## 11. 练习与扩展

- 为基础练习增加三个“应该触发”和三个“近似但不应触发”的提示，观察误判。
- 把 `plan-small-change` 写成第二个 Skill，要求输出影响范围、任务和验证计划，不修改代码。
- 比较两个版本时保持任务和起始提交一致；不要同时更换模型、Skill 和项目数据。
- 若某项检查每次都必须执行且不需要判断，将它移入 CI，而不是继续扩充 Skill。

## 12. 参考资料

- [Agent Skills Specification](https://agentskills.io/specification)：Skill 的通用结构与字段。
- [Anthropic Skills：skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)：草稿、测试、评测和迭代方法。
- [Anthropic：Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)：最小高信号上下文与渐进披露。
- [AGENTS.md](https://agents.md/)：跨工具项目入口及项目约定。

---

# 第 18 章　子 Agent、Hooks 与 Issue-to-PR 自动化

> 本章成果：用隔离的子任务、独立工作区和明确闸门，把一次订阅管理器修复变成可审查的 Issue-to-PR 流程。

## 1. 本章成果

你将完成一次半自动维护演练：从一个明确 Issue 出发，让规划、实现、验证和评审分别在不同上下文或不同工作区中进行，最后形成可人工合并的 PR。本章还会建立一个自主度阶梯，判断哪些动作可以由 AI 自动执行，哪些必须保留人工闸门。

完成后的产物包括：

```text
docs/issues/renewal-date-validation.md
docs/handoff/renewal-date-validation.md
docs/verification/renewal-date-validation.md
```

以及一个独立 Worktree 中的修复分支和评审记录。

## 2. 为什么需要它

多个 Agent 并不天然等于更快。拆分的第一个价值是**上下文隔离**：研究、实现、评审分别只保留自己需要的信息，避免一段长对话里既有旧需求、又有失败尝试、还有未验证结论。第二个价值是**职责分离**：实现者容易相信自己已经完成，独立评审者只看证据和 Diff，更容易发现问题。

但拆分也有成本：交接信息可能丢失，多个工作区可能修改冲突，自动化可能反复循环而无人叫停。因此不要从多 Agent 开始第一个项目。先具备小任务、测试、CI 和人工评审，再逐步引入自动化。

## 3. 最少必备知识

- **主 Agent**：掌握总体计划，负责拆任务、交接和整合，不亲自完成所有深度工作。
- **子 Agent**：在干净上下文中完成一个可独立验收的任务，只返回结论、证据和产物。
- **上下文压缩**：长会话接近限制时，把关键事实写入文件，再开新会话。
- **Git Worktree**：同一仓库在不同目录中检出不同分支，便于隔离并行修改。
- **Hook**：在特定工具事件前后自动执行检查；它提供快速反馈，但不能替代独立 CI。
- **自主度闸门**：每个级别明确谁能写文件、谁能运行命令、谁能合并。

## 4. 起始项目状态

从第 17 章后的项目开始，工作区应干净，核心检查通过：

```powershell
git status
python -m pytest -q
python -m ruff check .
```

本章的练习 Issue 使用：`renewal_date` 早于当前日期时没有明确校验。修复应让 API 拒绝无效日期，并保留清晰的 422 或项目既有错误格式。

## 5. 操作步骤与 AI 任务示例

### 第一步：把 Issue 写成可验收任务

创建 `docs/issues/renewal-date-validation.md`：

```markdown
# renewal_date 缺少过去日期校验

现象：通过 API 可以创建 renewal_date 早于今天的订阅。
验收：
- 请求返回项目既有的校验错误格式。
- 合法日期仍可创建。
- 增加回归测试。
- 不改变数据库字段。
```

### 第二步：让规划子 Agent 只读分析

```text
目标：分析 renewal_date 校验的影响范围，不修改代码。
上下文：Issue、AGENTS.md、app/schemas.py、app/repository.py、相关测试。
范围：只读；禁止写文件和运行会改变状态的命令。
约束：找出最小修改点；区分现有测试缺口和实现缺陷。
验收：列出影响文件、建议方案、回归测试和风险。
输出：简短规划报告。
```

规划完成后，把结果写入 `docs/handoff/renewal-date-validation.md`。交接文件必须包含目标、已完成分析、允许修改范围、禁止事项和验证命令。

### 第三步：创建独立 Worktree

```powershell
git switch main
git pull
git worktree add ../subscription-tracker-renewal-fix -b fix/renewal-date-validation
cd ../subscription-tracker-renewal-fix
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux 将激活命令替换为：

```bash
source .venv/bin/activate
```

每个 Worktree 应拥有自己的虚拟环境，避免不同分支的依赖互相污染。查看和清理由主目录执行：

```powershell
git worktree list
git worktree remove ../subscription-tracker-renewal-fix
```

### 第四步：实现子 Agent 在隔离目录中修复

```text
目标：修复 renewal_date 缺少过去日期校验的问题。
上下文：docs/handoff/renewal-date-validation.md、AGENTS.md、相关模块与测试。
范围：只允许修改 app/schemas.py、app/repository.py、tests/test_api.py。
约束：不修改数据库 schema；不重构无关代码；保留既有错误响应格式。
验收：新增非法过去日期和合法日期两个测试；pytest 与 Ruff 通过。
输出：修改文件列表、关键 Diff、真实命令结果。
```

实现结束后不要在同一会话中宣布验收，改为独立验证。

### 第五步：用 Hook 和 CI 形成两层反馈

Hook 与 CI 的职责不同。Hook 在本地尽早反馈，CI 在独立环境做最终门禁。具体配置格式取决于所用工具，以下只是**示意结构**：

```json
{
  "event": "before_commit",
  "command": "python -m pytest -q && python -m ruff check ."
}
```

CI 仍应运行：

```yaml
- run: python -m pip install -r requirements.txt
- run: python -m pytest -q
- run: python -m ruff check .
```

如果本地 Hook 被绕过，CI 必须仍能拦住问题。

### 第六步：独立评审子 Agent 只读检查

```text
目标：评审 fix/renewal-date-validation，不修改代码。
上下文：Issue、交接文件、git diff --stat、git diff、测试与 CI 结果。
范围：只读。
约束：不信任实现会话的自述；只根据 Diff、命令输出和测试判断。
验收：逐条检查 Issue 验收条件，并指出未覆盖风险。
输出：通过、请求修改或阻断，以及证据。
```

### 第七步：人工合并并记录自主度

人工最终确认 Diff、测试结果和发布影响，再合并 PR。将“哪些步骤自动、哪些步骤人工”写入维护记录，为后续提高自动化程度留下依据。

## 6. AI 应生成的产物

- 可验收 Issue 与交接文件；
- 规划报告，说明影响范围和禁止事项；
- Worktree 中的最小修复 Diff；
- 新增回归测试；
- 验证报告，包含 pytest、Ruff 和 `git diff --check` 的真实输出；
- 独立评审结论；
- PR 描述，说明根因、修改、风险和验证证据。

如果使用的是 OpenHands 或 GitHub Copilot coding agent 等具备 Issue-to-PR 能力的平台，最终仓库中仍应看到同样的产物：Issue、分支、代码 Diff、测试、评审和合并记录。工具可以代替手工操作，但不能代替证据。

## 7. 人工检查点

- 检查 Worktree 是否只包含本章分支，没有混入其他实验文件。
- 查看 `git diff --stat`：是否只改了预期文件。
- 确认实现、验证和评审没有共用同一段长对话。
- 检查交接文件是否足够让新会话继续，而不是只有“请参考上文”。
- 确认 Hook 只加速本地反馈，CI 仍是独立门禁。
- 若自动化反复失败，检查是否设置了最大尝试次数、超时和升级人工的条件。
- 合并前确认数据库没有被偷偷修改，尤其是迁移类任务。

## 8. 验收命令与通过标准

在修复 Worktree 中运行：

```powershell
git status
git diff --stat
git diff --check
python -m pytest -q
python -m ruff check .
python skills\verify-change\scripts\check_report.py docs\verification\renewal-date-validation.md
```

通过标准：

- 工作区除预期修复外没有其他变更；
- 非法过去日期被拒绝，合法日期仍可创建；
- pytest 与 Ruff 真实退出码为 0；
- 验证报告结构检查通过；
- 独立评审没有遗留阻断问题；
- Worktree 清理成功，主仓库不受影响。

不要以“子 Agent 说完成”作为通过证据。

## 9. 常见失败及恢复方法

1. **症状：两个并行任务修改同一文件后无法合并。** 原因：任务没有按文件和目录隔离。恢复：中止合并，重新划分任务边界，每个 Worktree 只负责一个可独立验收的变更。
2. **症状：新会话不知道之前为什么这样修改。** 原因：上下文压缩后关键事实没有落盘。恢复：补写 `docs/handoff/`，记录目标、约束、已完成分析和验证命令。
3. **症状：自动化循环反复修改同一个测试。** 原因：没有停止条件和失败预算。恢复：限制尝试次数，保存轨迹，升级人工；先修验收标准，再继续自动化。
4. **症状：本地 Hook 通过但 CI 失败。** 原因：环境或依赖不一致。恢复：以 CI 为准；检查虚拟环境、依赖锁定和测试数据。
5. **症状：平台拥有过宽的仓库或云资源权限。** 原因：为了省事授予全部权限。恢复：先在测试仓库运行，使用最小权限和只读评审，再逐步放开。

## 10. 本章 Git 提交

建议分支：

```text
fix/renewal-date-validation
```

提交可拆为：

```powershell
git add docs/issues docs/handoff
git commit -m "docs: add renewal date validation issue"
git add app tests
git commit -m "fix: reject renewal dates in the past"
git add docs/verification
git commit -m "docs: record verification evidence"
```

PR 合并后删除远程分支，再清理 Worktree。

## 11. 练习与扩展

- 给规划、实现、评审分别设置最大尝试次数，并记录第一次需要人工介入的原因。
- 将“只读研究”“可写实现”“只读评审”写成三个不同的任务模板，避免一个 Agent 同时承担所有角色。
- 比较串行流程与两个真正独立任务的 Worktree 流程；如果并行没有减少总时间或提高质量，就不要为了并行而并行。
- 在测试仓库中体验 OpenHands 或 Copilot coding agent 的 Issue-to-PR 流程，再回到本项目比较证据完整性。

## 12. 参考资料

- [OpenHands：Software Factory](https://docs.openhands.dev/openhands/usage/use-cases/software-factory.md)：Issue、开发 PR、评审、测试与合并的闭环示例。
- [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)：从任务到 PR 的官方能力与适用边界。
- [Git worktree](https://git-scm.com/docs/git-worktree)：多工作区隔离。
- [Anthropic：Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)：上下文隔离、压缩和子任务交接。

---

# 第 19 章　平台对照与工具迁移：不被某个产品绑定

> 本章成果：建立一套平台边界检查方法，并证明订阅管理器可以从仓库导出、独立运行和继续维护。

## 1. 本章成果

本章不要求你购买或长期使用某个 AI 建站平台。你将完成两件事：

1. 使用官方文档比较 Replit Agent、Lovable、Bolt.new、v0 和 GitHub Copilot coding agent 的能力边界，重点判断“快照是否等于 Git”“预览是否等于测试”“代码回滚是否等于数据恢复”“项目能否完整导出”。
2. 把当前订阅管理器导出到一个全新目录，在干净环境中安装、测试并启动，证明项目不依赖任何特定聊天会话。

完成后新增：

```text
docs/runbooks/platform-boundaries.md
docs/runbooks/export-and-migration.md
```

## 2. 为什么需要它

托管平台可以显著降低第一次上线的门槛：不需要提前配置服务器、数据库和发布流程。但它们也会隐藏一些长期维护所必需的事实：代码在哪里、配置在哪里、数据库由谁备份、版本历史如何与 Git 对应、回滚会恢复什么。

教程的主线始终是“可导出源码＋可迁移流程”。平台适合作为对照组，帮助理解正式 Git、测试和发布为什么仍然重要。一旦项目离开平台后无法安装、无法测试或无法恢复数据，前面的自动化程度越高，风险反而越大。

## 3. 最少必备知识

- **平台快照**：保存某一时刻的代码、配置或对话状态，恢复方式由平台定义。
- **Git 历史**：提交、分支、标签和 Diff，可被任何 Git 工具检查与迁移。
- **预览**：人工或浏览器自动检查页面行为。
- **系统测试**：可重复执行并留下退出码、断言和日志的验证。
- **代码回滚**：恢复程序版本。
- **数据恢复**：恢复数据库记录、迁移状态和备份点。
- **导出**：获得源码、依赖清单、配置说明和数据访问方式，并能离开原平台运行。

## 4. 起始项目状态

从第 18 章后的项目开始，工作区干净，CI 或本地检查通过。确认仓库具备可迁移所需的最小资产：

```powershell
git status
python -m pytest -q
python -m ruff check .
```

如果项目曾经连接过任何平台，先记录其数据库位置、密钥名称和发布地址；不要在本章直接粘贴真实密钥。

## 5. 操作步骤与 AI 任务示例

### 第一步：阅读官方能力，而不是宣传页

针对每个平台，只记录能由官方文档核验的信息：生成方式、计划或审批、测试、历史与恢复、Git/导出、部署和维护边界。产品能力会变化，记录访问日期。

### 第二步：填写平台边界表

创建 `docs/runbooks/platform-boundaries.md`，建议表格如下：

```markdown
# 平台边界检查

| 平台 | 生成与迭代 | 历史/恢复 | 测试证据 | Git/导出 | 主要边界 | 官方文档核验日期 |
|---|---|---|---|---|---|---|
```

按官方文档可确认的典型结论示例：

| 平台 | 可借鉴的维护问题 |
|---|---|
| [Replit Agent](https://docs.repl.it/learn/build-with-agent) | 自动浏览器测试并非每次都执行；[检查点](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks)可能包含配置或数据状态，但应确认它与 Git 的关系 |
| [Lovable](https://docs.lovable.dev/features/plan-mode) | 计划可编辑并批准；恢复旧版本不一定撤销之后的数据库记录或迁移 |
| [Bolt.new](https://support.bolt.new/building) | 可查看代码和终端；实时预览不等于完整测试 |
| [v0](https://v0.app/docs/agentic-features) | 版本支持 Diff 与恢复，并可与 GitHub、CI 衔接；手工修改是否进入平台版本需要核验 |
| [Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) | 适合已有仓库的 Issue→分支→测试→PR；部署依赖仓库自身 CI/CD |

不要在表中写“它一定会自动测试”“数据一定能恢复”等未经文档确认的句子。

### 第三步：导出当前项目并证明可迁移

在项目根目录生成一个不含 Git 历史的源码包：

```powershell
git archive --format=zip --output=..\subscription-tracker-export.zip HEAD
```

解压并测试：

```powershell
Expand-Archive ..\subscription-tracker-export.zip -DestinationPath ..\subscription-tracker-export
cd ..\subscription-tracker-export
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m ruff check .
python -m uvicorn app.main:app --reload
```

macOS/Linux 解压可使用：

```bash
unzip ../subscription-tracker-export.zip -d ../subscription-tracker-export
```

并改用 `source .venv/bin/activate`。

如果项目包含数据库文件，另写恢复说明；导出的源码包不应混入个人订阅数据、密钥或生产数据库。

### 第四步：可选执行一次真实平台对照

若你有某个平台的可用账号，建议选 Replit 或 Lovable 做一次小型对照：

1. 使用同一份 `docs/intent.md` 创建一个最小 CRUD 应用。
2. 记录它的计划、生成、预览和发布步骤。
3. 修改一条数据后恢复旧版本，观察代码与数据是否都回滚。
4. 导出或同步到 GitHub。
5. 在本地干净目录安装并运行测试。

没有账号时，跳过这一步；只用文档完成边界分析，并明确写“未实测”。

### 第五步：整理迁移清单

创建 `docs/runbooks/export-and-migration.md`：

```markdown
# 导出与迁移清单
1. 源码、依赖清单和启动命令。
2. 环境变量名称、用途及占位示例。
3. 数据库类型、迁移历史和备份位置。
4. 发布地址、健康检查和日志入口。
5. 平台专有服务及替代方案。
6. 已知不可导出部分。
```

AI 任务示例：

```text
目标：基于仓库和官方文档生成平台边界与迁移检查清单，不登录第三方平台。
上下文：docs/runbooks、README、AGENTS.md、requirements.txt、CI 配置。
范围：只创建两份 Markdown Runbook。
约束：只写能核验的事实；未实测项目标注“未实测”；不记录真实密钥。
验收：表格覆盖生成、历史、测试、导出、数据恢复和部署；迁移清单能指导干净环境运行。
输出：两份文档和建议补充的资料。
```

## 6. AI 应生成的产物

- `docs/runbooks/platform-boundaries.md`，每项能力附官方链接和核验日期。
- `docs/runbooks/export-and-migration.md`，覆盖源码、依赖、配置、数据、发布和不可导出风险。
- 一份干净目录导出验证记录，至少包含安装、pytest、Ruff 和启动检查。
- 若进行了平台实测，另存操作时间、版本、观察结果和截图或 URL；未实测则明确说明。

## 7. 人工检查点

- 表格中的“测试证据”是否区分了自动测试、浏览器预览和人工验收。
- “历史/恢复”是否区分了平台快照、Git 提交和数据库备份。
- 导出包是否真的不包含 `.venv/`、数据库文件、日志和密钥。
- 迁移清单是否列出平台专有认证、数据库、函数或托管服务。
- 所有未实测的能力是否标注清楚，没有把文档能力写成你的项目已经完成。
- 干净目录是否能独立安装运行，而不是依赖原项目缓存。

## 8. 验收命令与通过标准

```powershell
git status
python -m pytest -q
python -m ruff check .
git archive --format=zip --output=..\subscription-tracker-export.zip HEAD
```

进入导出目录后再次执行：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m ruff check .
python -m uvicorn app.main:app --reload
```

通过标准：原仓库与导出目录都能安装依赖；两个目录的 pytest 与 Ruff 退出码均为 0；应用可以启动并通过 `/health`；平台边界表覆盖五个平台；迁移清单没有遗漏环境变量、数据库和发布配置；未实测内容已明确标注。

## 9. 常见失败及恢复方法

1. **症状：平台预览正常，导出后无法启动。** 原因：环境变量、密钥或托管服务未随源码导出。恢复：补齐 `example.env`、README 启动说明和依赖清单；无法替代的服务写入迁移风险。
2. **症状：恢复旧版本后，新数据仍然存在。** 原因：代码快照没有回滚数据库。恢复：使用数据库备份恢复，或编写前向修复迁移；把“代码回滚≠数据回滚”写入 Runbook。
3. **症状：平台与 GitHub 双向同步后出现冲突。** 原因：两边都被修改且没有唯一事实来源。恢复：先备份当前代码，选择 Git 为主仓库，平台只发布或只读同步。
4. **症状：官方界面与教程记录不一致。** 原因：产品更新。恢复：按当前文档重新核验，记录访问日期；保留稳定的验收问题清单，而不是截图流程。
5. **症状：导出测试通过，但生产无法访问。** 原因：只验证了本地启动，没有验证部署配置、网络、端口和健康检查。恢复：按第 11 章重新执行发布检查。

## 10. 本章 Git 提交

建议分支：

```text
docs/platform-boundaries
```

提交拆分：

```powershell
git add docs/runbooks/platform-boundaries.md
git commit -m "docs: compare ai platform maintenance boundaries"
git add docs/runbooks/export-and-migration.md
git commit -m "docs: add export and migration runbook"
```

导出包、临时解压目录和任何数据库文件不要提交。

## 11. 练习与扩展

- 选两个平台执行同一个最小 CRUD 任务，比较需求澄清、历史恢复、导出和测试证据。
- 为订阅管理器增加 `example.env` 和启动脚本，使干净环境迁移少一个手工步骤。
- 估算从某个托管平台迁回本地或普通云主机的工作量，分别列出代码、数据、认证、发布和监控。
- 把“平台能力核验日期”纳入第 16 章的文档漂移扫描。

## 12. 参考资料

- [Replit Agent](https://docs.repl.it/learn/build-with-agent)、[App Testing](https://docs.replit.com/features/agent/app-testing)、[Checkpoints and rollbacks](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks)
- [Lovable Plan mode](https://docs.lovable.dev/features/plan-mode)、[History](https://docs.lovable.dev/features/projects/history)、[GitHub sync](https://docs.lovable.dev/integrations/github)
- [Bolt.new Build](https://support.bolt.new/building)、[Version history and GitHub](https://support.bolt.new/reference/version-history-github)
- [v0 Agent features](https://v0.app/docs/agentic-features)、[Versions](https://v0.app/docs/versions)、[GitHub](https://v0.app/docs/github)
- [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)

---

# 第 20 章　结业项目：完成你自己的 AI 生成与维护闭环

> 本章成果：独立选择一个小项目，在 30 天内完成生成、发布、维护演练和最终复盘，并用证据包证明它可交付、可恢复、可继续接手。

## 1. 本章成果

结业项目不是再做一个更大的订阅管理器，而是证明你能把前面的方法迁移到自己的问题上。最终需要提交：

1. 一个可运行、可测试、可发布的真实项目；
2. 完整 Git 历史、版本标签和发布记录；
3. 意图、规格、架构、任务、验证和维护文档；
4. 至少一个自定义 Skill、Hook 或自动化检查；
5. 一份 30 天维护日志和最终复盘。

评审不看代码行数，而看：需求是否清楚、变更是否受控、测试是否真的能发现问题、故障能否恢复、后续维护者能否接手。

## 2. 为什么需要它

教程里的示例项目已经替读者排除了许多现实噪音：字段清楚、依赖简单、故障是预埋的。真实项目则会带来模糊需求、外部服务、数据隐私、时间不足和不断变化的工具。

结业项目的目标是完成一次小规模但完整的闭环：

```text
选择问题
→ 定义范围
→ 写出规格
→ 小步实现
→ 独立验证
→ 发布
→ 处理变化
→ 恢复故障
→ 复盘
```

如果只完成“生成和上线”，项目仍可能在下一次需求变化时失控。维护演练才能证明你掌握的是工程闭环，而不是一次性生成技巧。

## 3. 最少必备知识

- 如何把模糊想法缩小为明确范围、非目标和验收条件；
- 如何创建规格、计划和可独立验证的小任务；
- 如何使用 Git 分支、Diff、标签和回滚；
- 如何运行测试、静态检查和独立验证；
- 如何保存上下文交接文件，让新 AI 会话继续工作；
- 如何处理 Bug、新功能、迁移、依赖更新和文档漂移；
- 如何评价自动化是否真的减少了返工。

如果你还没有完成核心章节，不要直接从结业项目开始。先完成一个小项目的生成与维护，再选择自己的题目。

## 4. 起始项目状态

从空仓库开始，不要复制订阅管理器的业务代码。可以复用教程中的模板、Skill、CI 结构和验收原则。

```powershell
mkdir capstone-project
cd capstone-project
git init
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux 使用：

```bash
mkdir capstone-project
cd capstone-project
git init
python3 -m venv .venv
source .venv/bin/activate
```

默认建议使用 Python、FastAPI、SQLite、pytest、Ruff 和 GitHub Actions；也可以选择另一种栈，但必须在 `AGENTS.md` 中写清等价的安装、运行、测试、检查和发布命令。

项目选择标准：

- 一个核心实体或一个小工作流；
- 不超过 5 个核心操作；
- 本地可运行、可测试；
- 不依赖付费第三方服务作为唯一路径；
- 数据可以导出和恢复；
- 你自己会在 30 天内真的使用它。

合格例子：阅读记录与复习提醒、家庭库存管理、个人运动日志、小型账单分类器、学习笔记检索工具。  
不合格例子：完整社交平台、支付系统、多租户 SaaS、需要大量真实用户数据的项目。

## 5. 操作步骤与 AI 任务示例

### 第一步：用 AI 缩小范围，但不让它替你选择目标

```text
目标：把我的结业项目想法缩小到 30 天可完成、可维护的范围。
上下文：我的可用时间、已有技能、必须解决的问题、候选功能。
范围：只输出意图、范围、非目标和风险，不生成代码。
约束：一个核心实体；最多 5 个核心操作；本地可运行；第一版不引入付费外部服务。
验收：每个核心操作都有用户场景和可检查的验收条件。
输出：capstone-intent.md 草案。
```

把最终决定权保留在自己手里。AI 可以提出范围，但你要选择真正会使用和验收的问题。

### 第二步：建立里程碑计划

| 里程碑 | 建议时间 | 必须完成 | 退出条件 |
|---|---|---|---|
| M0 项目启动 | 第 1—2 天 | 仓库、环境、意图、非目标 | 干净环境能运行空项目或起始命令 |
| M1 蓝图 | 第 3—5 天 | 规格、架构、ADR、任务拆分 | 每条需求有验收方法，第一任务可独立验证 |
| M2 v0.1 | 第 6—9 天 | 最小纵向切片 | 核心流程端到端可用 |
| M3 v1.0 | 第 10—16 天 | 测试、CI、发布、部署或可分发包 | 干净环境安装、测试、发布并记录回滚方式 |
| M4 维护循环 | 第 17—24 天 | Bug、新功能、迁移或依赖事件 | 每类事件都有 Issue、验证和 PR |
| M5 30 天复盘 | 第 25—30 天 | 恢复演练、文档校正、最终发布、复盘 | 新 AI 会话能凭仓库继续一个任务 |

AI 规划任务示例：

```text
目标：把 M1 蓝图拆成可执行任务。
上下文：capstone-intent.md、规格、架构、我的每日可用时间。
范围：只修改 docs/plan.md 和 docs/tasks.md。
约束：每个任务可独立验证；单个任务预计不超过一次工作会话；标注依赖和风险。
验收：第一个任务能直接开始，不需要额外隐藏假设。
输出：任务列表、依赖图和完成定义。
```

### 第三步：按小 Diff 实现，不要一次性生成整个项目

每个任务使用固定任务包：

```text
目标：
上下文文件：
允许修改范围：
禁止事项：
验收命令：
输出要求：
```

实现后必须查看：

```powershell
git status
git diff --stat
git diff
```

只有当修改范围、测试和验收一致时才提交。

### 第四步：建立独立验证与发布

至少准备这些命令或等价命令：

```powershell
python -m pytest -q
python -m ruff check .
git diff --check
```

发布前完成：

- 干净目录安装；
- 核心用户流程人工验收；
- CI 通过；
- 版本标签；
- 发布说明；
- 回滚方式；
- 配置和密钥占位说明。

### 第五步：执行 30 天维护演练

从第 17 天开始，至少完成六类事件：

| 事件 | 要求 |
|---|---|
| Bug 修复 | 先写失败回归测试，再修复 |
| 新功能 | 先更新规格和验收条件，再实现 |
| 数据或配置迁移 | 有备份、迁移脚本、验证和恢复方案 |
| 依赖/安全维护 | 升级一个依赖或处理一次静态安全警告 |
| 文档漂移 | 找出文档与实际行为不一致处并修正 |
| 上下文交接 | 新 AI 会话只凭仓库完成一个小任务 |

建议节奏：

```text
第 17—18 天：整理维护待办，建立事件卡片
第 19—21 天：完成一个 Bug 修复
第 22—24 天：完成一个新功能或小重构
第 25—26 天：执行迁移、备份和恢复演练
第 27—28 天：处理依赖、安全和文档漂移
第 29—30 天：发布补丁版本并复盘
```

维护记录放入 `docs/maintenance-log.md`，每条包括日期、事件、根因、验证命令、证据链接和后续风险。

### 第六步：创建至少一个项目资产

从以下任选一项，必须真正被使用过：

- 一个验证或规划 Skill；
- 一个提交前检查 Hook；
- 一个生成项目地图或健康报告的脚本；
- 一个 CI 质量门禁；
- 一份新会话交接模板。

资产不在多，而在下次维护时确实减少了遗漏。

### 第七步：完成最终复盘

```text
目标：基于 Git 历史、验证报告和维护日志复盘结业项目。
上下文：docs/intent.md、specs/、docs/verification/、docs/maintenance-log.md、git log --stat。
范围：只创建 docs/retrospective.md。
约束：用证据支持结论；区分事实、判断和未完成事项。
验收：列出最有效的流程、最大返工来源、下一位维护者注意事项。
输出：复盘报告和未来 30 天维护计划。
```

## 6. AI 应生成的产物

AI 在不同阶段应分别生成或协助整理：

```text
docs/intent.md
docs/acceptance.md
specs/
ARCHITECTURE.md
docs/decisions/
docs/plan.md
docs/tasks.md
AGENTS.md
docs/handoff/
docs/verification/
docs/maintenance-log.md
docs/retrospective.md
.github/workflows/ci.yml
skills/ 或 scripts/
```

最终证据包建议包含：

- 仓库 URL 或本地路径；
- 版本标签与发布说明；
- CI 运行记录；
- 测试与静态检查输出；
- 至少一次 Bug、功能、迁移和恢复记录；
- 新 AI 会话交接任务的结果；
- 自定义 Skill、Hook 或脚本；
- 复盘报告。

## 7. 人工检查点

- 项目是否仍然是你最初想解决的问题，而不是被 AI 扩大成无关系统。
- 每个里程碑是否有退出证据，而不是“看起来差不多了”。
- Diff 是否足够小，能在合理时间内读完关键修改。
- 测试是否断言业务行为，而不只是调用函数或检查页面存在。
- 发布是否能在干净环境复现。
- 回滚是否真的演练过，尤其是数据和配置。
- 新 AI 会话是否只凭仓库就能继续，而不需要你重述聊天历史。
- 维护日志是否记录失败和未完成事项，而不是只记成功。

## 8. 验收命令与通过标准

基础命令：

```powershell
git status
git log --oneline --decorate
python -m pytest -q
python -m ruff check .
git diff --check
```

如果使用其他技术栈，换成 `AGENTS.md` 中登记的等价命令。干净环境复现：

```powershell
git archive --format=zip --output=..\capstone-export.zip HEAD
Expand-Archive ..\capstone-export.zip -DestinationPath ..\capstone-export
cd ..\capstone-export
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload
```

### 评审量规（满分 100）

| 维度 | 分值 | 通过证据 |
|---|---:|---|
| 意图与范围 | 10 | 用户、问题、非目标、成功标准清楚；范围没有失控 |
| 规格与验收 | 15 | 每条核心需求有场景和可检查验收条件 |
| 架构与上下文 | 10 | 架构、ADR、AGENTS.md 与实际代码一致 |
| 任务拆分与 Git | 10 | 小 Diff、清晰提交、标签和可审查 PR/分支 |
| 测试与调试 | 15 | 单元/集成测试覆盖正常与异常；至少一次先回归后修复 |
| 发布与回滚 | 15 | 干净环境可安装运行；发布、健康检查和回滚有记录 |
| 维护演练 | 15 | 完成 Bug、功能、迁移、依赖、文档和交接六类事件 |
| 自动化资产 | 5 | 至少一个 Skill、Hook、脚本或 CI 门禁被实际使用 |
| 证据与复盘 | 5 | 维护日志、验证记录和复盘基于真实证据 |

评分建议：

- **90—100**：可以公开作为作品集项目；
- **70—89**：通过结业，但需要列出剩余维护债务；
- **50—69**：完成生成，但维护闭环不足，需补做事件；
- **低于 50**：建议缩小范围后重做 M1—M3。

通过标准不是“AI 完成了所有任务”，而是证据能支持每个维度的分数。

## 9. 常见失败及恢复方法

1. **症状：第一周就选了过大的题目。** 原因：把“能想到”当成“能交付”。恢复：砍到一个核心实体和五个操作，把其余功能写入非目标。
2. **症状：代码很多，但没有测试，后期不敢改。** 原因：测试被推迟到项目末尾。恢复：停止新功能，为当前核心流程补保护性测试，再继续。
3. **症状：一个 PR 修改几十个文件。** 原因：任务没有拆分或 AI 顺手重构。恢复：要求 AI 只保留一个任务的最小 Diff，其余变更另开分支。
4. **症状：发布后发现问题却无法回到稳定版本。** 原因：只有代码回滚，没有数据和配置恢复方案。恢复：补做备份与恢复演练，把步骤写入 Runbook。
5. **症状：新 AI 会话重复犯同样错误。** 原因：经验留在聊天记录中。恢复：更新 AGENTS.md、Skill、Hook 或 CI，并重新运行相关检查。
6. **症状：30 天维护只有成功记录。** 原因：复盘变成展示。恢复：补录失败、未解决问题和下一步计划；没有失败记录通常说明事件太简单。

## 10. 本章 Git 提交

建议按里程碑分支和标签：

```text
milestone/m1-blueprint
milestone/m2-vertical-slice
milestone/m3-release
milestone/m4-maintenance
```

版本标签：

```text
v0.1
v1.0
v1.1
v1.1.1
```

示例提交：

```powershell
git switch -c milestone/m3-release
git add .github/workflows/ci.yml docs/release-checklist.md
git commit -m "ci: add release quality gates"
git tag v1.0
```

不要把虚拟环境、数据库文件、日志、密钥或导出包提交进仓库。

## 11. 练习与扩展

- 把项目发布为公开仓库，并补充面向陌生维护者的 README。
- 邀请另一个人或一个全新 AI 会话，只凭仓库完成一个小任务，记录交接缺口。
- 用两种不同编码 Agent 完成同一个维护事件，比较 Diff、测试证据和返工次数。
- 再运行 30 天维护，观察技术债是被持续偿还还是重新累积。
- 把复盘中的稳定经验整理成第二版 Skill，但不要把所有偶然经验都写成强制规则。

## 12. 参考资料

- [生成式软件工程（2026 秋季学期）](https://jyywiki.cn/GSE/2026/)：项目化教学、实验与长期演化的课程组织方式。
- [OpenAI：Harness Engineering](https://openai.com/zh-Hant/index/harness-engineering/)：把原则编码进仓库并持续清理残留问题的维护思路。
- [Anthropic：Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)：上下文隔离、压缩和交接。
- [AGENTS.md](https://agents.md/)：跨工具项目入口与约定。
- [Google Engineering Practices：Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)：小变更与可审查提交。

---

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

---

# 附录 B　命令速查

> 用途：提供本教程最常用的最小命令集，而不是复制完整工具手册。统一核验日期：**2026-11-24**。CLI、斜杠命令和托管平台界面可能变化；实际执行前应以对应版本的官方文档和 `--help` 为准。

## B.1 Git：先看状态，再做小提交

```powershell
git status
git log --oneline --decorate -10
git diff --stat
git diff
git switch -c feat/example
git add PATH
git commit -m "feat: describe one change"
```

误操作排查与恢复：

```powershell
git diff --check
git show --stat HEAD
git restore --worktree -- PATH
git revert <COMMIT>
```

| 目的 | 命令 | 注意 |
|---|---|---|
| 查看未提交修改 | `git diff` | 默认不显示未跟踪文件内容 |
| 查看暂存区修改 | `git diff --staged` | 提交前重点审查 |
| 丢弃单文件工作区修改 | `git restore --worktree -- PATH` | 会覆盖未提交修改，先确认路径与 Diff |
| 用反向提交撤销已共享提交 | `git revert <COMMIT>` | 保留历史，通常比重写共享历史更适合协作 |
| 创建本地标签 | `git tag -a v1.0.0 -m "v1.0.0"` | 标签指向准确 commit；推送与发布按项目流程执行 |

官方来源：[Git Documentation](https://git-scm.com/docs)。

## B.2 Python 与项目运行

Windows PowerShell：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

macOS/Linux 创建与激活：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

需要避开 PATH 中其他工具时，显式使用虚拟环境解释器：

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

官方来源：[Python venv](https://docs.python.org/3/library/venv.html)、[pip](https://pip.pypa.io/en/stable/)、[Uvicorn](https://www.uvicorn.org/)。

## B.3 pytest：先确认收集，再看失败

```powershell
python -m pytest -q
python -m pytest --collect-only -q
python -m pytest tests/test_api.py -q
python -m pytest tests/test_api.py::test_create_subscription -q
python -m pytest -k "subscription" -q
python -m pytest --maxfail=1 -x
```

- `--collect-only`：只收集测试，排查“0 项运行”。
- `-k`：按表达式筛选名称匹配的测试。
- `-x`：首个失败后停止，适合集中处理根因；不把它当完整通过证据。
- 验收时重新运行完整测试集，不只运行刚修改的单测。

官方来源：[pytest Usage and Invocations](https://docs.pytest.org/en/stable/how-to/usage.html)。

## B.4 Ruff：让静态检查成为可执行反馈

```powershell
python -m ruff check .
python -m ruff check app tests
python -m ruff format --check .
python -m ruff check . --fix
```

`--fix` 会修改文件。先提交或保存基线，执行后查看：

```powershell
git diff --stat
git diff
python -m pytest -q
```

不要对 `.venv`、数据目录或整个磁盘运行自动修复。具体规则由项目配置决定，不在教程中假定所有默认规则始终相同。

官方来源：[Ruff](https://docs.astral.sh/ruff/)、[Ruff Configuration](https://docs.astral.sh/ruff/configuration/)。

## B.5 Spec Kit：把规格流程串起来

安装和初始化以当前 Quickstart 为准。官方 CLI 常见形式为：

```powershell
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify check
specify init <PROJECT_NAME>
```

在已集成的编码 Agent 中，核心阶段使用对应的 `speckit` 命令：

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.checklist
/speckit.tasks
/speckit.analyze
/speckit.implement
```

不是每个小修改都要机械执行全部命令。教程强调阶段产物：原则→规格→澄清→计划→任务→一致性检查→实现。安装参数、Agent 名称和可用命令可能变化，应先在当前环境运行 `specify --help`，不要混用旧教程中的无前缀斜杠命令。

官方来源：[github/spec-kit](https://github.com/github/spec-kit)、[Quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md)、[Agentic SDD 命令参考](https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md)。

## B.6 OpenSpec：围绕变更管理规格

```powershell
openspec init
openspec list
openspec show <CHANGE_ID>
openspec validate <CHANGE_ID> --strict
openspec archive <CHANGE_ID>
```

在编码 Agent 中，可用自然语言要求“创建 OpenSpec proposal”“应用指定 change”“归档已验收 change”。变更 ID 必须来自当前项目，不直接复制教程示例。不同版本的归档交互和校验参数可能不同，执行前查看：

```powershell
openspec --help
openspec archive --help
```

官方来源：[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)。

## B.7 Aider：仓库内小步修改与反馈

安装完成后，在项目根目录启动并显式加入相关文件：

```powershell
aider
aider README.md app/main.py tests/test_api.py
```

会话内常用命令：

```text
/diff
/test
/run <COMMAND>
/undo
/help
```

- `/diff`：查看 Aider 产生的修改。
- `/test`：运行项目配置的测试命令；先确认实际执行了什么。
- `/run`：运行命令并把输出用于后续协作。
- `/undo`：撤销 Aider 最近一次的 Git 提交，不等于恢复任意历史状态。

模型、认证和自动测试参数不在本附录写死。先备份或提交基线，再允许工具自动修改。

官方来源：[Aider Usage](https://aider.chat/docs/usage.html)、[Linting and Testing](https://aider.chat/docs/usage/lint-test.html)。

## B.8 OpenHands：用任务和验收条件驱动维护

OpenHands 的重点是任务工作流，而不是一条固定命令：

```text
输入：Issue、目标仓库、验收条件、允许范围
过程：研究与实现 → 开发 PR → 独立评审 → 测试 → 验收
输出：可审查的 PR、执行轨迹和验证结果
```

部署涉及仓库访问、令牌、运行环境和审批配置，应使用当前官方安装/部署文档；不要照搬旧版本的一体化 Docker 命令。旧 `All-Hands-AI/OpenHands` 已迁移到 `OpenHands/OpenHands`，代理核心还可能位于独立 SDK 仓库。

官方来源：[OpenHands](https://github.com/OpenHands/OpenHands)、[Software Factory](https://docs.openhands.dev/openhands/usage/use-cases/software-factory.md)。

## B.9 Renovate：依赖更新先形成可审查 PR

最小配置示例 `renovate.json`：

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "dependencyDashboard": true,
  "automerge": false,
  "schedule": ["before 9am on Monday"],
  "timezone": "Asia/Shanghai"
}
```

安装 Node.js 后，可用官方包中的校验器检查本地配置：

```powershell
npx --yes --package renovate renovate-config-validator
```

建议起步策略：

1. 开启 Dependency Dashboard，保留人工确认。
2. 小项目先关闭自动合并，观察更新质量。
3. CI 必须包含安装、测试和关键检查。
4. 失败时定位具体依赖和变更说明，不让 AI 同时升级整批包来“碰运气”。

官方来源：[Renovate Documentation](https://docs.renovatebot.com/)、[Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/)、[Configuration Validation](https://docs.renovatebot.com/config-validation/)。

## B.10 完成前最小检查序列

```powershell
git status
git diff --check
git diff --stat
python -m pytest -q
python -m ruff check .
```

通过标准：所有命令实际执行且成功；变更范围与任务一致；测试结果和 Diff 已写入 PR 或交接记录。如果项目包含前端、迁移或发布步骤，还应运行对应检查，不能用上述五条替代全部验收。

---

# 附录 C　故障与恢复目录

> 目标：遇到 AI 开发问题时，先判断症状、确认证据，再选择最小恢复动作。不要根据 AI 的自我声明判断问题已解决；恢复后必须重新运行验收命令。

每条记录固定检查五项：

```text
症状：看到了什么
根因：为什么会发生
证据：用什么命令、文件或日志证明
恢复：怎样回到可继续工作的状态
预防：怎样让下次更容易被发现或避免
```

## C.1 规格与任务失控

### C.1.1 简单需求生成了复杂项目

- **症状**：请求一个简单订阅记录页面，结果出现多个框架、数据库、认证、前端构建和大量陌生目录。
- **根因**：任务没有非目标、规模限制和技术约束；“做得完整一点”被 AI 理解为扩大技术栈。
- **证据**：`git diff --stat`；新增依赖列表；目录树与规格中的范围对照。
- **恢复**：保留当前分支，回到上一个基线标签或提交；先补充 `intent.md`、`spec.md` 与非目标，再重新实现最小纵向切片。
- **预防**：任务包明确“只允许修改的文件、禁止新增的依赖、完成标准”；每个功能先问“最小可验收版本是什么”。

### C.1.2 规格看起来完整，却无法验收

- **症状**：需求写了很多，但不知道怎样证明功能完成。
- **根因**：只有抽象描述，没有输入、输出、边界和验收场景。
- **证据**：逐条检查需求是否对应测试、命令或可观察行为；找不到对应项就是缺口。
- **恢复**：把无法验收的需求降级为开放问题；为核心场景补充 Given/When/Then。
- **预防**：使用 [spec.md](../templates/spec.md) 和 [definition-of-done.md](../templates/definition-of-done.md)，规格完成前不进入实现。

### C.1.3 一个 PR 同时改功能、重构和格式

- **症状**：Diff 很大，审查者无法判断哪些变化与需求有关。
- **根因**：没有任务边界；让 AI“顺便优化”了整个项目。
- **证据**：`git diff --stat`、`git diff`，以及 PR 描述与关联 Issue/Spec 的对照。
- **恢复**：关闭或拆分该 PR；把功能变更、重构和格式化分别提交。
- **预防**：一个任务一个 PR；[pr-checklist.md](../templates/pr-checklist.md) 中写明变更类型和不应触碰的目录。

## C.2 运行与验证失败

### C.2.1 AI 声明完成，但项目无法运行

- **症状**：AI 回答“已完成并通过测试”，实际启动失败或页面异常。
- **根因**：实现结果没有经过独立验证；测试缺失、命令错误或环境不同。
- **证据**：在干净终端执行安装、测试、启动和 `/health`，保留完整命令与输出。
- **恢复**：回到最近可运行提交；把真实错误提供给 AI，先复现再修复，不接受“应该可以了”的说法。
- **预防**：完成前执行固定检查序列；验收记录中保存命令、版本和结果。

### C.2.2 本地能跑，干净克隆跑不起来

- **症状**：原目录正常，新克隆缺少文件、配置或数据目录。
- **根因**：依赖了未提交文件、本机全局工具或隐藏状态。
- **证据**：`git status`、`git ls-files`；在临时目录重新克隆并安装。
- **恢复**：补齐项目必需文件或文档说明；重新执行干净环境验收。
- **预防**：CI 使用干净检出；`.env` 不入库，但必须有 `.env.example`。

### C.2.3 依赖安装失败或版本不稳定

- **症状**：同一份代码在另一台机器或 CI 中安装、启动失败。
- **根因**：依赖未固定、平台差异、网络受限或隐式系统依赖。
- **证据**：`requirements.txt` 或锁文件；完整安装错误；Python 与操作系统版本。
- **恢复**：在最近可安装版本上缩小范围，一次只调整一个依赖；必要时恢复锁文件。
- **预防**：记录 Python 版本；CI 从干净环境安装；依赖更新使用小 PR 和测试门禁。

### C.2.4 测试全绿但行为仍然错误

- **症状**：pytest 通过，实际添加订阅、查询或导出结果不正确。
- **根因**：测试没有覆盖验收场景、断言太弱，或 mock 掉了真实行为。
- **证据**：`--collect-only` 确认实际收集范围；读取断言；用 API 或界面执行验收场景。
- **恢复**：先写一个能失败的验收测试，再修改实现，直到真实行为正确。
- **预防**：测试必须引用规格或验收编号；关键流程至少有一个端到端或 API 测试。

### C.2.5 只运行了与修改无关的测试

- **症状**：修改了数据库逻辑，却只跑前端或某个无关单测。
- **根因**：没有把“受影响范围”映射到测试命令。
- **证据**：PR 中的 Diff 与测试日志、收集列表对照。
- **恢复**：根据文件和调用关系补跑对应测试，再运行完整测试集。
- **预防**：任务包中写明必须执行的测试命令；CI 阻止只靠局部测试合并。

## C.3 上下文与协作失败

### C.3.1 新会话忘记项目约定

- **症状**：上一次已经纠正过的命名、目录或数据格式，新会话又改错。
- **根因**：约定只存在于聊天记录，没有写入项目或上下文入口。
- **证据**：检查 `AGENTS.md`、`ARCHITECTURE.md`、ADR 与任务说明；对比两次会话的 Diff。
- **恢复**：把稳定约定写入项目文档；当前任务用交接摘要重新开始，不要继续污染旧上下文。
- **预防**：每次纠正后问“该写入哪个文件、测试或检查？”；长期规则不能只留在对话里。

### C.3.2 上下文太长导致越改越偏

- **症状**：会话后期重复实现、忘记先前决定或开始修改无关文件。
- **根因**：无关历史、工具输出和大文件占据注意力；没有压缩或交接。
- **证据**：新会话只提供仓库和当前任务，观察结果是否改善。
- **恢复**：保存交接文档，清理无关上下文，从最近绿色提交开始新的窄任务。
- **预防**：使用 [handoff.md](../templates/handoff.md)；长资料放 `references/` 或磁盘，按需读取。

### C.3.3 AI 在修复循环中制造新问题

- **症状**：每次修复都让另一个测试失败，提交越来越多但状态不稳定。
- **根因**：没有稳定复现、根因假设和回退点。
- **证据**：提交历史和测试输出显示“修 A 坏 B”的循环。
- **恢复**：回到最后一个绿色提交；先写最小复现，限制只能修改必要文件。
- **预防**：设置尝试次数上限；连续失败后改为人分析根因，而不是继续盲目生成补丁。

### C.3.4 并行 Agent 或分支互相覆盖

- **症状**：两个任务修改同一文件，最后集成时出现冲突或功能被覆盖。
- **根因**：任务范围重叠，没有文件所有权和隔离策略。
- **证据**：各分支的 `git diff --stat`、冲突文件和测试失败记录。
- **恢复**：选择一个主分支，按行为逐项合入并重新测试；不要一次性自动解决所有冲突。
- **预防**：按可独立验证的模块拆分；必要时使用 Git worktree 或串行执行。

## C.4 发布、数据与维护失败

### C.4.1 代码回滚后数据库不兼容

- **症状**：应用恢复到旧版本，但启动或查询因新 schema 失败。
- **根因**：代码回滚与数据库状态没有一起考虑。
- **证据**：当前 commit、迁移记录、数据库 schema、备份文件及其验证结果。
- **恢复**：优先使用兼容性备份；否则编写向前修复迁移，不要在未备份的数据上试错。
- **预防**：迁移前备份；保留“旧代码能否读取新 schema”的兼容策略；发布与数据回滚分别演练。

### C.4.2 平台快照恢复后用户数据没有恢复

- **症状**：在托管平台恢复了版本，代码回到旧状态，但新增数据仍然存在或状态不一致。
- **根因**：平台检查点主要恢复代码、配置或特定数据库快照，不等同于业务数据事务回滚。
- **证据**：平台版本记录、数据库导出/恢复前后的数据对比、操作日志。
- **恢复**：按数据影响编写补偿操作或恢复经过验证的备份；先在副本上演练。
- **预防**：在正式迁移或危险变更前导出并验证备份；记录哪些状态受平台快照保护、哪些不受保护。

### C.4.3 本地正常，部署环境失败

- **症状**：本地 `/health` 正常，部署后启动失败、路径错误或接口异常。
- **根因**：环境变量、工作目录、依赖、端口、数据库路径或密钥配置不同。
- **证据**：同一 commit 在本地和部署环境的日志；配置项清单；启动命令。
- **恢复**：恢复到上一个可用发布；只修改部署配置或兼容性代码，不混入新功能。
- **预防**：发布前在干净环境验证；健康检查和关键流程作为部署后必查项。

### C.4.4 文档、命令与实际项目漂移

- **症状**：README 或 Runbook 中的命令失败，目录和 API 说明与代码不一致。
- **根因**：功能演化后没有同步文档，也没有文档检查。
- **证据**：逐条执行文档命令；比较文档与当前路由、脚本和配置。
- **恢复**：先修复文档中阻塞启动、测试和发布的路径，再安排完整校对。
- **预防**：区分“人写为什么”和“脚本生成现状”；CI 至少检查链接、关键命令或生成文档是否过期。

### C.4.5 依赖批量更新后服务异常

- **症状**：一次升级多个包后测试或运行行为变化。
- **根因**：更新范围过大，无法定位不兼容变更。
- **证据**：更新 PR 的版本变化、CI 日志和失败测试。
- **恢复**：关闭或回滚该 PR；一次只升级一个包，重新验证。
- **预防**：使用 Dependency Dashboard、分组和排期；高风险包必须人工审批；自动合并前至少有可靠测试。

### C.4.6 旧 Bug 再次出现

- **症状**：曾经修复的问题在新功能后复现。
- **根因**：修复没有留下回归测试，或测试未覆盖真实调用路径。
- **证据**：历史 Issue/PR、当前复现步骤、缺失的测试名称。
- **恢复**：先添加能稳定失败的回归测试，再重新修复。
- **预防**：每个 Bug 修复必须关联 Issue、测试和验收证据；重构前先建立行为基线。

## C.5 通用故障记录模板

```markdown
## 故障记录：[简短标题]

- 发现时间与环境：
- 项目版本或 commit：
- 症状：
- 影响范围：
- 复现步骤：
- 关键日志或命令输出：
- 初步根因：
- 已执行的恢复动作：
- 验证证据：
- 遗留风险：
- 预防措施：
- 相关 Issue/PR/Runbook：
```

记录时脱敏令牌、密码、个人数据和生产主机信息。若同一类故障重复出现，应把规则转化为测试、Lint、架构检查或 CI 门禁，而不是只写进文档。

---

# 附录 D　术语表

> 目标：用尽量少的概念解释 AI 项目从生成到维护的关键术语。遇到新工具时，先判断它属于哪一层，而不是机械记住产品名。

## D.1 AI 协作与上下文

| 术语 | 解释 |
|---|---|
| AI 编码代理 | 能读取项目、调用工具、修改文件、运行命令并根据结果继续工作的 AI 系统 |
| 聊天式 AI | 以对话为主，通常不直接管理仓库、运行测试或验证交付结果 |
| Prompt | 当前任务中给模型的指令、上下文和约束 |
| Context | 模型本次决策能看到的全部信息，包括指令、文件、工具结果和历史 |
| Context window | 一次推理可容纳的上下文范围；超出后旧信息会被截断、压缩或丢弃 |
| Context engineering | 决定“何时给模型哪些高价值信息”的工程实践 |
| Context rot | 上下文过长或噪声过多导致模型检索与推理质量下降 |
| Token | 模型处理文本的基本单位；中文、代码和标点并不一定是一个字对应一个 token |
| Tool | Agent 可调用的外部能力，例如读文件、搜索、运行命令或访问 API |
| MCP | Model Context Protocol，一种连接模型与外部工具和数据源的协议 |
| Skill | 可复用的任务说明、脚本和参考资料，用来封装重复流程 |
| Subagent | 在独立上下文中处理专项任务的子 Agent，主 Agent 只接收摘要或结果 |
| Hook | 在特定事件前后自动执行的脚本或检查，例如提交前、工具调用后 |
| Harness | 模型之外支撑其可靠工作的工程环境，包括上下文、工具、测试、权限和反馈回路 |
| Human-in-the-loop | 在计划、实现、审查、合并或发布中保留人工判断节点 |
| Autonomy level | Agent 可独立行动的程度，从只读建议到自动提交和发布逐级上升 |
| Worktree | 同一 Git 仓库的多个工作目录，用于隔离并行修改 |
| Sandbox | 限制命令、文件和网络权限的执行环境，用来降低误操作风险 |
| Just-in-time retrieval | 先保存文件路径、查询或链接，需要时再读取内容，而不是一次性塞入全部资料 |

## D.2 需求、规格与计划

| 术语 | 解释 |
|---|---|
| Intent | 用户的真实问题、目标和限制，比具体功能更早确定 |
| Mini-PRD | 简短产品需求说明，用于快速澄清目标、范围、非目标和验收 |
| Spec | 可审查、可验证的功能规格，包括行为、规则、数据和验收场景 |
| SDD | Spec-Driven Development，先形成规格和计划，再进入实现 |
| Spec Kit | GitHub 提供的规格驱动开发工具包，串联 constitution、specify、plan、tasks 等阶段 |
| OpenSpec | 围绕变更提案、规格更新和归档组织的轻量 SDD 工具 |
| Constitution | 项目长期遵守的原则、质量标准和工程约束 |
| Acceptance criteria | 判断一项需求是否完成的可观察条件 |
| Scenario | 用具体输入、操作和预期结果描述一个验收场景 |
| Non-goal | 当前版本明确不做的事情，用来防止范围膨胀 |
| NFR | 非功能需求，例如性能、安全、兼容性、可维护性和可用性 |
| MVP | 能解决核心问题的最小可用产品，不是功能残缺的 Demo |
| Vertical slice | 打通一个完整业务流程所需的最小纵向实现 |
| Walking skeleton | 先建立从入口到存储的最小可运行骨架，再逐步增强 |
| Definition of Done | 一项工作被视为完成前必须满足的全部证据和检查 |
| ADR | Architectural Decision Record，记录重要技术决策的原因、选项和后果 |
| Scope creep | 需求或实现在没有重新评审的情况下不断扩大 |
| Task packet | 交给 AI 的单个任务说明，包括目标、上下文、范围、约束、验收和输出 |

## D.3 版本、评审与发布

| 术语 | 解释 |
|---|---|
| Commit | 一次保存的项目状态，应聚焦一个可理解的变更 |
| Atomic commit | 只完成一个 logically complete change 的提交，便于审查、测试和回滚 |
| Diff | 两个版本之间的差异，是人工审查 AI 修改的核心证据 |
| Branch | 与主线隔离的开发线 |
| PR | Pull Request，用于提交、审查、测试和合并一组变更 |
| Code review | 对 Diff、测试、文档和风险的人工或工具审查 |
| CI | Continuous Integration，在提交或 PR 上自动运行构建、测试和检查 |
| CD | Continuous Delivery/Deployment，把通过验证的版本交付或部署到目标环境 |
| Quality gate | 必须通过才允许继续的检查，例如测试、Lint、安全扫描或架构规则 |
| Tag | 指向特定 commit 的标记，常用于发布版本 |
| Release | 一次正式交付的版本及其说明、产物和验证证据 |
| Rollback | 恢复到之前可用状态，可能涉及代码、配置、数据或部署 |
| Revert | Git 中通过反向提交撤销历史变更的方式，保留原历史 |
| Clean checkout | 不包含本地未提交状态的全新检出环境，用于复现交付结果 |

## D.4 测试与质量

| 术语 | 解释 |
|---|---|
| Unit test | 验证函数、类或小模块在受控输入下行为的测试 |
| Integration test | 验证多个模块、数据库或外部接口协同工作的测试 |
| End-to-end test | 从用户入口到最终结果验证完整业务流程的测试 |
| Regression test | 防止已修复问题再次出现的测试 |
| Characterization test | 为现有行为建立基线的测试，常用于重构前保护系统 |
| TDD | 先写失败测试，再实现功能，最后重构的开发方式 |
| Assertion | 测试中对实际结果与预期结果的明确比较 |
| Mock | 用替身隔离外部依赖；过度 mock 可能让测试通过但真实行为错误 |
| Test oracle | 判断结果是否正确的依据，例如规格、验收场景或历史行为 |
| Test gap | 重要行为、路径或边界缺少有效测试的状态 |
| Coverage | 测试覆盖代码或分支的程度；高覆盖率不等于高质量验收 |
| Lint | 通过规则检查代码风格、可疑写法和简单错误 |
| Static analysis | 不运行程序，通过代码结构发现潜在问题的分析方法 |
| Architecture test | 把依赖方向、模块边界等架构规则变成可执行检查 |
| Mutation testing | 故意修改代码，检验测试是否真的能发现错误 |
| Golden master | 用既有输出作为基准，比较后续实现是否保持行为一致 |

## D.5 维护、数据与运维

| 术语 | 解释 |
|---|---|
| Refactoring | 在不改变外部行为的前提下改善代码结构 |
| Technical debt | 为了短期速度积累、后续需要额外偿还的设计或实现问题 |
| Cognitive debt | 团队对系统理解不足，导致难以判断修改影响和承担后果 |
| Repo map | 项目目录、模块、入口、依赖和关键文件形成的导航图 |
| Documentation drift | 文档与实际代码、命令或架构逐渐不一致 |
| Generated docs | 由脚本从代码或配置生成的现状文档，应注明来源和再生成方式 |
| Dependency | 项目依赖的外部库、服务或工具 |
| Version pinning | 固定依赖版本，以提高构建可重复性 |
| Lockfile | 记录完整依赖解析结果的文件，用于复现安装环境 |
| Supply chain risk | 依赖来源、包名、构建或发布环节被篡改或引入风险的问题 |
| Renovate | 自动创建依赖更新 PR，并提供 Dashboard、分组和审批策略 |
| Schema migration | 数据库结构或数据的受控变更 |
| Forward fix | 不回滚数据，而是通过新的兼容修复继续向前恢复 |
| Backup | 可恢复的数据副本，必须经过验证才算可靠 |
| Restore drill | 定期演练恢复流程，确认备份、权限和步骤仍然有效 |
| Observability | 通过日志、指标、追踪和告警理解系统运行状态 |
| Health check | 判断服务是否启动并具备基本可用性的检查接口 |
| Structured log | 带字段、级别、时间和请求标识的日志，便于定位问题 |
| Alert | 达到阈值或异常模式时通知维护者的机制 |
| Runbook | 标准操作步骤，例如启动、发布、备份、恢复和常见故障处理 |
| Incident | 影响可用性、数据、安全或用户结果的事件 |
| Postmortem | 事件后的原因、影响、时间线和预防改进记录 |
| Residue cleanup | 定期清理 AI 或快速迭代留下的重复代码、无用配置和过期文档 |
| Small PR | 小范围、可审查、可回滚的变更，是长期维护自动化的基础 |

## D.6 教程中的项目术语

| 术语 | 解释 |
|---|---|
| Subscription Tracker | 本教程贯穿使用的个人订阅与续费管理器 |
| `intent.md` | 项目意图、用户、目标、非目标和验收信号 |
| `spec.md` | 当前功能或变更的可验证规格 |
| `plan.md` | 一次变更的实施计划、影响范围、风险和验证方式 |
| `tasks.md` | 计划拆分后的可执行任务及状态 |
| `handoff.md` | 会话、人员或 Agent 之间交接当前状态和下一步 |
| `/health` | 教程项目的健康检查端点 |
| `/api/subscriptions` | 教程项目的核心订阅数据 API |
| `billing_cycle` | 第 15 章数据迁移中新增的续费周期字段 |

---

# 附录 E　资料来源与核验说明

> 统一核验日期：**2026-11-24**。  
> 本附录只整理本教程设计过程中实际检索或读取的一手课程、官方文档、仓库与公开教程。商业课程只记录公开大纲，不表示已经购买、体验或评价其内部内容。仓库状态、命令和平台能力可能变化，使用前应重新核对官方版本。

## E.1 本地输入资料

| 资料 | 用途 |
|---|---|
| `AI-项目生成与维护-GitHub资料地图.md` | 提供规格层、上下文层、生成编排和维护闭环的初步分类 |
| `AI-项目生成与维护-非GitHub平台资料地图.md` | 补充厂商工程报告、论文、社区反例和组织视角 |

这两份文件由用户在任务中提供，本教程只借鉴其分类和判断原则，不复制其中可能过期的工具推荐。

## E.2 课程与系统化教程

| 来源 | 类型 | 主要借鉴内容 |
|---|---|---|
| [生成式软件工程（2026 秋）](https://jyywiki.cn/GSE/2026/) | 大学课程主页 | 18 讲与实验的节奏；工程判断、Agent Native 开发、软件演化与质量保障的结构 |
| [GSE Lab1：个人数字助手](https://jyywiki.cn/GSE/2026/lab1.md) | 课程实验 | 开放实验、持续改进、把有效流程沉淀为脚本或技能 |
| [GSE 第1讲](https://jyywiki.cn/GSE/2026/lect1.md) | 课程讲义 | 以验收成果而非代码量评价学习；局部修改与独立验证 |
| [GSE 第10讲：软件的演化](https://jyywiki.cn/GSE/2026/lect10.md) | 课程讲义 | RFC/ADR、原子提交、PR、分层验收和回归测试 |
| [左手蓝图，右手魔法：2025 iThome 铁人赛系列](https://huangchiyu.com/ChiYu-Blog/series/2025ithomeironman/) | 32 篇中文免费系列 | 零基础贯穿项目；文档先行；Git、Flask、API、CI、Pytest、前端与重构 |
| [AI 时代的 Clean Code：30 天系列](https://huangchiyu.com/ChiYu-Blog/series/ithome-2026-ai-clean-code/) | 中文系列 | 可读性、测试证据、架构边界、故意制造失败与 Agent Skill 沉淀 |
| [文件驱动 AI 开发（图书公开目录）](https://www.mybookone.com.hk/page/detail_w/2117513186437857282/9786264146340.html) | 图书资料页 | 文件驱动开发、贯穿项目、TDD、交付维运与持续维护定位 |
| [Vibe Coding 2.0：从 DDD 到 SDD](https://huangchiyu.com/ChiYu-Blog/posts/vibe-coding-2-0-sdd/) | 作者文章 | 文档约定与强制规格之间的层次差异 |
| [Vibe Coding Guide](https://github.com/Lling0000/Vibe_coding_guide) | 中文开放教程仓库 | Spec、上下文、Worktree、Skill、CI、Diff Review 与交接流程 |
| [Vibe Coding Guide 在线版](https://lling0000.github.io/Vibe_coding_guide/) | 在线教程网站 | 19 章与 36 天学习路径的组织方式 |
| [AI 编程全流程：从需求到上线](https://www.tahou.com/article/212321858624960517) | 中文实操长文 | 零基础从想法到上线、服务器、HTTPS、分支迭代与基础运维 |
| [AI 赋能软件开发实践手册](https://github.com/havvk/awesome-ai-development) | 中文开放手册 | 需求、生成、重构、审查、测试、部署脚本和生产排错场景 |
| [AI Fundamentals](https://aifundamentals.dev/) | 英文付费课程主页 | 工具无关的上下文、指令、验证回路、技术债与跨项目复用 |
| [AI Fundamentals 示例仓库](https://github.com/AvdLee/AI-Fundamentals-Course) | 开源练习项目 | starter/final 状态与课程练习分离 |
| [Beyond Vibe Coding](https://beyond.addy.ie/) | 英文电子书/免费站点 | 从原型到工程化；mini-PRD、逐改测试、TDD、检查点与技术债 |
| [The AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) | Anthropic 实践指南 | 六阶段输入物、人工审批、沙箱、部署/回滚和事故回到需求 |
| [UI5 Agentic Development Tutorial](https://github.com/UI5/tutorials/tree/main/packages/agentic) | 官方技术教程 | 创建、增强、迁移与遗留项目现代化的分步实验 |
| [UI5 Step 4: Modernize a Legacy OpenUI5 Project](https://github.com/ui5/tutorials/blob/main/packages/agentic/steps/04/README.md) | 教程步骤 | Linter、Skills、分阶段提交和验证门禁 |
| [Agentic AI Applications with Claude Code](https://github.com/tertiarycourses/TGS-2025052468-Agentic-AI-Applications-with-Claude-Code) | 公开课程仓库 | 一个主题、一个 Lab、一个实践任务，最后进入测试、安全和部署 |
| [Vibe Coding 零基础入门到实战应用](http://yun.itheima.com/course/1100.html) | 商业课程公开介绍 | SDD、实战项目、测试、部署、迭代优化与 Skill/Subagent 的课程定位 |
| [The Claude Code Bootcamp](https://zerotomastery.io/courses/claude-code-bootcamp/) | 商业课程公开介绍 | 从想法到 Spec、上下文、质量审计、测试和部署的课程结构 |
| [AI-Assisted Programming 中文资料页](https://www.gotop.com.tw/book/BookDetails.aspx?bn=A791) | 图书资料页 | 需求、规划、编码、调试、测试、部署与工具全景 |
| [Generative AI for Software Development](https://www.deeplearning.ai/specializations/generative-ai-for-software-development/) | 在线课程公开大纲 | 代码生成、调试、测试、依赖与文档的分模块教学 |
| [AI-Powered Software Development Certification](https://www.coursera.org/specializations/ai-powered-software-development-certification) | 在线课程公开大纲 | 需求、生成、迁移、测试、部署、支持和维护的阶段划分 |

## E.3 规格驱动与工作流工具

| 来源 | 类型 | 主要借鉴内容 |
|---|---|---|
| [github/spec-kit](https://github.com/github/spec-kit) | 官方仓库 | constitution、specify、clarify、plan、tasks、analyze、implement 的阶段产物 |
| [Spec Kit Quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) | 官方文档 | 初始化与阶段命令的使用入口 |
| [Spec Kit Agentic SDD 参考](https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md) | 官方文档 | 当前 `/speckit.*` 命令及质量门禁 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 官方仓库 | 轻量规格变更、proposal、validate 与 archive 流程 |
| [Agent Skills Specification](https://agentskills.io/specification) | 官方规范 | `SKILL.md` 元数据、正文、scripts/references/assets 的组织方式 |
| [anthropics/skills](https://github.com/anthropics/skills) | 官方示例仓库 | 真实 Skill 目录结构和可复用模板 |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | 官方 Skill | 创建、评测和迭代 Skill 的方法 |
| [obra/superpowers](https://github.com/obra/superpowers) | 开源 Skill 集合 | TDD、系统化调试、代码评审和完成前验证的技能边界 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 官方社区资源合集 | Agents、Instructions、Skills、Hooks、Workflows 的职责区分 |
| [create-specification](https://github.com/github/awesome-copilot/tree/main/skills/create-specification) | 社区 Skill | 规格文档最小结构 |
| [create-implementation-plan](https://github.com/github/awesome-copilot/tree/main/skills/create-implementation-plan) | 社区 Skill | 实施计划与任务拆分 |
| [acquire-codebase-knowledge](https://github.com/github/awesome-copilot/tree/main/skills/acquire-codebase-knowledge) | 社区 Skill | 扫描仓库、生成结构和风险文档 |
| [test-gap-audit](https://github.com/github/awesome-copilot/tree/main/skills/test-gap-audit) | 社区 Skill | 只读识别测试缺口与弱断言 |
| [create-agentsmd](https://github.com/github/awesome-copilot/tree/main/skills/create-agentsmd) | 社区 Skill | 从仓库生成 AGENTS.md 的参考流程 |
| [AGENTS.md](https://agents.md/) | 开放格式 | README 与 Agent 入口文件的分工；多工具兼容 |

社区贡献的 Skill 不等于官方保证。使用前检查许可证、脚本副作用和适用版本。

## E.4 工程实践与研究资料

| 来源 | 类型 | 主要借鉴内容 |
|---|---|---|
| [Harness 工程：在智慧体优先的世界中善用 Codex](https://openai.com/zh-Hant/index/harness-engineering/) | OpenAI 工程文章 | 黄金原则编码、残留物清理、背景重构 PR 和长期维护 |
| [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Anthropic 研究文章 | 最小高信号上下文、渐进披露、压缩、笔记和子 Agent |
| [Exploring Generative AI](https://martinfowler.com/articles/exploring-gen-ai.html) | 持续更新文章系列 | SDD、上下文工程、TDD、Harness、质量与遗留项目实践 |
| [Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | 文章 | 不同 SDD 工具的思路比较 |
| [TDD inside the agent loop](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html) | 文章 | Agent 循环中的 TDD 是否真正改善质量 |
| [Google Engineering Practices: Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) | 官方工程实践 | 小变更、清晰说明、审查和回滚 |
| [GitHub Actions: Continuous integration](https://docs.github.com/en/actions/get-started/continuous-integration) | 官方文档 | 把本地验收命令固化为 CI |
| [Renovate Documentation](https://docs.renovatebot.com/) | 官方文档 | 依赖更新策略、分组和验证 |
| [Renovate Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/) | 官方文档 | 集中查看和审批更新 |

## E.5 代码生成与维护项目案例

| 来源 | 类型/状态 | 教程用途 |
|---|---|---|
| [OpenHands](https://github.com/OpenHands/OpenHands) | 活跃仓库；旧路径已迁移 | Issue→PR、评审、测试和 Software Factory 闭环案例 |
| [OpenHands Software Factory](https://docs.openhands.dev/openhands/usage/use-cases/software-factory.md) | 官方文档 | 维护自动化与人工验收流程 |
| [software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) | 官方 SDK 仓库 | 当前代理核心与部署架构可能分离 |
| [Aider](https://github.com/Aider-AI/aider) | 活跃仓库 | Repo Map、Git 提交、Lint/Test 与存量维护 |
| [Aider Linting and Testing](https://aider.chat/docs/usage/lint-test.html) | 官方文档 | `/test`、`--auto-test`、`/run` 与失败修复 |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 活跃仓库 | 多角色 SOP：PRD、设计、任务、代码与增量开发 |
| [MetaGPT Incremental Development](https://docs.deepwisdom.ai/main/en/guide/in_depth_guides/incremental_development.html) | 官方文档 | 对既有生成项目追加需求和修 Bug |
| [Cline](https://github.com/cline/cline) | 活跃仓库 | IDE 人在回路、Diff、检查点、终端反馈和权限审批 |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | 研究/基准型项目；官方推荐后继项目 | GitHub Issue 到 Patch 的仓库修复流程 |
| [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) | 后继轻量项目 | 新实操案例优先参考 |
| [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) | 已归档 | Prompt 到代码库和项目演进史；不作为现行实操环境 |
| [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) | README 声明停止维护 | 早期多角色开发流程与供应链风险案例；静态阅读 |

## E.6 平台化开发案例

| 来源 | 主要核验能力 | 教程用途 |
|---|---|---|
| [Replit: Build with Agent](https://docs.repl.it/learn/build-with-agent) | 规划、生成、调试和继续迭代 | 快速展示零基础闭环 |
| [Replit: App Testing](https://docs.replit.com/features/agent/app-testing) | 浏览器操作、测试数据和自动修复 | 区分平台测试与正式测试体系 |
| [Replit: Checkpoints and Rollbacks](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks) | 代码、对话、配置和数据库状态恢复 | 讲解快照能力与边界 |
| [Lovable: Plan Mode](https://docs.lovable.dev/features/plan-mode) | 先检查和澄清，再批准计划 | 需求确认与人工审批 |
| [Lovable: Version History](https://docs.lovable.dev/features/projects/history) | 版本历史与恢复 | 代码回滚与数据回滚的区别 |
| [Lovable: GitHub Integration](https://docs.lovable.dev/integrations/github) | GitHub 同步 | 平台项目如何进入正式 Git 流程 |
| [Bolt: Building](https://support.bolt.new/building) | Plan Mode、Prompt 增强和项目构建 | 提示词与项目变化的直观对照 |
| [Bolt: Code View](https://support.bolt.new/building/code-view) | 源码、预览和终端 | 让初学者查看报错并小步修复 |
| [Bolt: Version History and GitHub](https://support.bolt.new/reference/version-history-github) | 历史、恢复和 GitHub 连接 | 版本恢复与代码托管边界 |
| [v0: Agentic Features](https://v0.app/docs/agentic-features) | 沙箱、浏览器、终端、测试和修复 | 平台 Agent 能力演示 |
| [v0: Versions](https://v0.app/docs/versions) | Diff 与恢复 | 平台版本和 Git 历史的关系 |
| [v0: GitHub](https://v0.app/docs/github) | 分支、预览、PR、CI | 从生成平台进入工程审查 |
| [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) | Issue、分支、测试、PR 和评审响应 | 存量项目维护案例 |
| [Copilot coding agent 最佳实践](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results) | 明确任务、验收条件和小范围变更 | Issue 写作和人工审查教学 |
| [Devin: Testing and Recordings](https://docs.devin.ai/work-with-devin/testing-and-recordings) | 端到端测试计划和录像 | 高级代理的验证证据与局限 |
| [Devin: Playbooks](https://docs.devin.ai/product-guides/creating-playbooks) | 可复用维护流程 | 与 Skill/Runbook 的对照 |
| [Base44: App Editor](https://docs.base44.com/Getting-Started/app-editor-overview) | Discuss/Build、预览、测试、发布与监控 | 托管式闭环案例 |
| [Base44: Developer Architecture](https://docs.base44.com/developers/app-code/overview/introduction) | 托管后端、GitHub 同步与架构边界 | 平台黑盒与迁移风险 |

## E.7 使用这些资料的原则

1. **先判断层次**：每个工具属于规格、上下文、执行、验证、发布还是维护层。
2. **先做项目，再讲工具**：所有工具都要服务 Subscription Tracker 的某个验收结果。
3. **区分稳定原理与时效命令**：原理写入正文，具体命令记录版本和核验日期。
4. **不复制受版权保护的长内容**：只引用标题、URL 和独立总结。
5. **不推荐已归档或停止维护的项目作为现行实操环境**：它们只作为案例或历史材料。
6. **平台不能替代可迁移能力**：读者最终要能导出代码、运行测试、查看 Git 历史并完成维护。

---

# 附录 F：可复制模板原文

---

# 项目意图（Intent）

> 一页说清楚：为谁解决什么问题、做到什么程度算成功、明确不做什么。
> 填写时机：项目开始前；重大需求变化时更新版本号。
> 填写原则：每条都可以被争论和验证；写不出来的格子先用 `TODO` 占位并列入待澄清。

- 状态：草稿 / 已确认
- 版本：v0.1（2026-XX-XX）
- 负责人：[你的名字]

## 1. 用户与问题

| 项 | 内容 |
|---|---|
| 目标用户 | 例如：有多项订阅服务（视频、云盘、软件会员）的个人用户 |
| 核心问题 | 例如：续费日期分散在不同平台，容易忘记、被自动扣款 |
| 用户现状 | 例如：用备忘录或表格手动记录，经常漏记 |
| 不解决的场景 | 例如：企业级多部门费用管理、自动代付 |

## 2. 目标与非目标

**目标（本版本要做到）**

1. 能添加、查看、修改、删除订阅记录。
2. 能看到即将到期（7 天内）的订阅提醒列表。
3. 数据保存在本地，可导出为 CSV。

**非目标（本版本明确不做）**

1. 不做多人协作与账号体系。
2. 不做自动扣款或支付对接。
3. 不做移动 App。

## 3. 成功标准（可验证）

| 编号 | 标准 | 验证方法 |
|---|---|---|
| S1 | 添加一条订阅后，重启程序数据仍在 | 手动重启＋页面复查 |
| S2 | 金额、日期非法输入被拒绝并给出提示 | 用非法值实测 |
| S3 | 导出的 CSV 能被 Excel 打开且字段完整 | 打开导出文件核对 |

## 4. 假设与约束

| 类型 | 内容 |
|---|---|
| 假设 | 用户设备可信，不需要强加密存储 |
| 技术约束 | Python + FastAPI + SQLite，单人本地运行 |
| 时间约束 | 首个可用版本 1 周内完成 |

## 5. MVP 边界

- 包含：订阅 CRUD、到期提醒列表、CSV 导出。
- 不包含：提醒推送、多币种换算、历史账单统计（记入待办池）。

## 6. 待澄清问题

- [ ] 金额是否需要支持小数？精度如何处理？（倾向：整数分存储）
- [ ] “即将到期”的天数是否可配置？

## 完成条件

- 每个格子已填写或标入待澄清；目标与非目标无冲突；成功标准全部有验证方法；已向至少一位潜在用户口述确认。

---

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

---

# 实施计划（Plan）

> 说明这个变更怎么做：方案、影响范围、验证策略、回滚思路。
> 粒度：一次计划对应一次可发布的变更（一个版本或一个功能包）。

- 变更名称：订阅管理核心 v0.1
- 关联规格：`spec.md` v0.1
- 计划版本：v0.1（2026-XX-XX）

## 1. 技术方案

| 决策点 | 选择 | 理由 | 关联 ADR |
|---|---|---|---|
| Web 框架 | FastAPI | 自带校验与文档，适合小型 API | ADR-0001 |
| 存储 | SQLite 单文件 | 零部署成本，够用 | ADR-0002 |
| 前端 | 原生 HTML/JS | 无构建链，降低复杂度 | ADR-0003 |
| 金额 | 整数分 | 避免浮点误差 | ADR-0004 |

## 2. 影响范围

- 新增：`app/`（main、database、schemas、repository、routes）、`app/static/`、`tests/`。
- 修改：无（首个功能包）。
- 不触碰：无既有生产数据。

## 3. 模块与接口

```text
routes.py      只做参数校验与响应
repository.py  只做 SQL 与行映射
schemas.py     Pydantic 模型，唯一字段定义处
database.py    连接与建表
main.py        装配 + 静态文件挂载 + /health
```

依赖方向：routes → repository → database；schemas 被引用但不反向依赖。

## 4. 验证策略

| 层 | 验证方法 | 通过标准 |
|---|---|---|
| 单元 | pytest 测 repository 增删改查与校验 | 全部通过 |
| 接口 | pytest + TestClient 走 5 个验收场景 | 全部通过 |
| 手工 | 启动服务，页面完成添加/查看/修改/删除 | 无异常、数据持久 |
| 静态 | `ruff check .` | 0 错误 |

## 5. 任务拆分

见 `tasks.md`。原则：每任务 ≤ 半天、可独立验证、一个任务一个提交。

## 6. 风险与回滚

| 风险 | 应对 |
|---|---|
| 日期时区问题 | 统一本地日期字符串存储，比较用字符串排序（ISO 格式） |
| 并发写 SQLite | 单人使用场景，接受；记录 ADR 备忘 |
| 回滚 | 首版无迁移；直接 `git revert` 提交组即可 |

## 7. 完成定义

- `tasks.md` 全部勾选；CI 绿；5 个验收场景有证据；`README.md` 更新启动说明。

## 完成条件

- 方案与规格对应无缺口；影响范围明确列出“不触碰”内容；每个风险有应对；回滚步骤可执行。

---

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

---

# 架构决策记录（ADR-XXXX：标题）

> 一条 ADR 记录一个“当时为什么这么选”。写得短，重点在理由与后果。
> 状态：提议 / 已接受 / 已废弃（被 ADR-YYYY 取代）。

- 编号：ADR-0001
- 日期：2026-XX-XX
- 状态：已接受
- 关联：plan.md、spec.md

## 背景

（两三句：遇到什么约束或问题，必须做选择。）

示例：项目需要一个本地运行的 HTTP API，要求零配置启动、自带请求校验和接口文档，团队只有 1 人、无运维预算。

## 候选方案

| 方案 | 优点 | 缺点 |
|---|---|---|
| A. FastAPI | 校验/文档/异步内置；学习曲线平缓 | 需要安装依赖，冷启动略慢 |
| B. Flask | 极简生态成熟 | 校验和文档要自己拼装 |
| C. Django | 全家桶 | 对单人小项目过重 |

## 决策

选择 A。核心理由：Pydantic 校验直接落地 spec 的字段规则，OpenAPI 文档可作为 AI 的上下文来源。

## 后果

**正面**

- 字段校验错误自动返回 422 结构化信息。
- 接口文档可机器读取，便于后续维护会话快速对齐。

**负面 / 风险**

- 绑定 Python 生态；若未来换语言需重写（记录于“何时重估”条件）。

## 何时重估

出现以下任一情况重新评估：并发用户 > 10；需要跨机器共享数据；需要强事务一致性。

## 完成条件

- 背景、决策、后果齐备；负面后果如实记录；重估条件可观察。

---

# Issue：[类型] 一句话描述问题或需求

> 类型：`bug` / `feature` / `chore` / `question`
> 好的 Issue 让不看历史的人也能判断：发生了什么、期望什么、怎么算修好。

- 编号：ISSUE-014
- 类型：bug
- 状态：open / in-progress / resolved
- 报告人 / 日期：[名字] / 2026-XX-XX
- 影响版本：v1.1（commit 3f9c2ab）

## 问题描述

（两三句：谁在什么操作下遇到了什么，实际与预期的差异。）

示例：在订阅名称包含英文逗号时，导出的 CSV 列错位，Excel 打开后金额列跑到备注列。

## 复现步骤

1. 启动服务（`python -m uvicorn app.main:app`）。
2. 添加订阅，名称填 `云盘,高级版`。
3. 点击“导出 CSV”。
4. 用 Excel 打开 `subscriptions.csv`。

## 预期结果

名称字段以整列呈现，共 8 列，与表头一致。

## 实际结果

该行被拆为 9 列，后续字段整体右移一位（见附件截图/文件）。

## 证据

- 命令与输出：
  ```text
  python -m pytest tests/test_export.py -q
  # 输出：1 failed, 1 passed（失败用例：test_export_quotes_comma）
  ```
- 数据样本：`name = 云盘,高级版` 的导出行原文。

## 影响范围

- 影响所有名称含 `,`、`"`、换行 的导出记录；不影响列表页与数据库数据。

## 验收标准（怎么算解决）

1. 新增回归测试：名称含逗号/引号/换行时导出列数正确。
2. 既有数据导出与导入往返一致。
3. `pytest -q` 全绿，CI 通过。

## 关联

- 模板：`bug-report.md`（更详细的诊断记录）
- 修复 PR：[待填]

---

# Bug 报告与诊断记录

> 比 Issue 更深一层：记录诊断过程，让“怎么找到根因”可复盘。
> 与 `issue.md` 配合使用：Issue 对外沟通，本文件对内排障。

- Bug 编号：BUG-2026-014
- 关联 Issue：ISSUE-014
- 严重级：高 / 中 / 低（判定：数据错乱=高；展示异常=中；提示不友好=低）
- 记录人 / 日期：[名字] / 2026-XX-XX

## 1. 环境

| 项 | 值 |
|---|---|
| 版本 / 提交 | v1.1 / commit 3f9c2ab |
| OS / Python | Windows 11 / 3.12.4 |
| 数据库状态 | 12 条记录，3 条名称含特殊字符 |

## 2. 复现信息

- 最小复现：名称为 `a,b` 的一条记录 → 导出 → Excel 打开。
- 复现率：3/3。
- 首次出现：引入导出功能（commit 8d1e40b）之后。

## 3. 证据

```text
# 导出行原文（截取）
云盘,高级版,1500,CNY,2026-12-01,...

# 期望（名称被引号包裹）
"云盘,高级版",1500,CNY,2026-12-01,...
```

日志：无 5xx，属纯输出格式错误。

## 4. 诊断过程（时间线）

1. 假设 1：Excel 编码问题 → 用文本编辑器打开，列同样错位 → 排除。
2. 假设 2：写库时字段错位 → 查询数据库，行数据正确 → 排除。
3. 假设 3：导出未做 CSV 转义 → 查看 `scripts/export.py`，直接 `join(',')` → **确认**。

## 5. 根因

导出实现手动拼接字符串，未使用 csv 模块的 QUOTE 处理，含 `,`/`"`/换行的字段破坏列结构。

## 6. 修复方案

- 改用标准库 `csv.writer` 写出。
- 新增回归测试：名称含 `,`、`"`、`\n` 三种样本的导出断言。
- 导入侧同样改用 `csv.reader`，并补往返一致性测试。

## 7. 影响与回归要求

- 已导出的历史 CSV 文件需人工核对；修复后重新导出并 diff。
- 回归测试必须在修复 PR 中先于实现提交（红→绿）。

## 8. 复盘要点（写进失败案例库）

- 根因类别：格式处理 / 边界数据。
- 教训：AI 生成的导出代码在“正常数据”下测试全绿，边界字符必须显式入测。
- 预防：导出/导入类功能一律走标准库并带特殊字符用例。

## 完成条件

- 诊断时间线完整；根因有证据；回归测试与修复对应；复盘条目已同步失败案例库。

---

# PR 检查清单

> 提交或审查 PR 时逐项勾选。任何一项不满足，PR 不进入合并。
> 原则：小 Diff、单一目的、证据链接。

- PR 标题：feat: 修复 CSV 导出特殊字符列错位
- 关联 Issue：ISSUE-014
- 作者 / 评审人：[名字] / [名字]
- Diff 规模：3 文件，+45 −12

## A. 范围

- [ ] Diff 只包含本 Issue 相关改动（无顺手重构、无无关格式化）。
- [ ] 每个文件改动都能说清目的。
- [ ] 如包含重构，已与功能改动拆分为独立提交/PR。

## B. 代码质量

- [ ] 命名与既有风格一致；无魔法数字（常量已具名）。
- [ ] 无重复实现（已检索是否已有同功能函数）。
- [ ] 错误路径有处理（4xx/异常分支不是静默吞掉）。

## C. 测试

- [ ] 新增/修改行为有对应测试（先红后绿）。
- [ ] 边界与异常用例覆盖（空值、特殊字符、最大长度）。
- [ ] `python -m pytest -q` 全绿；`python -m ruff check .` 0 错误。
- [ ] 测试断言业务行为，而非只断言“不抛异常”。

## D. 兼容与数据

- [ ] API 变更向后兼容；若破坏性变更已注明并更新 spec 版本。
- [ ] 涉及数据库时：有迁移脚本 + 迁移前后备份说明。
- [ ] 依赖变更已写入 requirements.txt 并说明原因。

## E. 文档与上下文

- [ ] `AGENTS.md` / `ARCHITECTURE.md` / spec 若受影响已同步更新。
- [ ] README 的启动/使用说明仍然正确。
- [ ] 新增文件在正文中说明用途。

## F. 证据

- [ ] 验收命令输出已贴入 PR 描述（或附截图）。
- [ ] Issue 验收标准逐条对应勾选。
- [ ] 已在新会话/干净目录复验核心流程。

## G. 提交拆分

- [ ] 提交按“一个目的一条”拆分，信息用 `feat:/fix:/test:/docs:` 前缀。
- [ ] 无 `WIP`、无注释掉的大段死代码。

## 完成条件

- 以上全部勾选；评审人对照清单抽查通过；合并方式（merge/squash）已按仓库约定执行。

---

# 发布检查清单（Release）

> 每次对外发版执行一次。目标：发布的每个版本都可复现、可验证、可回滚。
> 版本号遵循语义化：破坏性变更升主版本，新功能升次版本，修复升修订。

- 版本：v1.2.1
- 类型：patch（依赖维护 + 文档校正）
- 发布人 / 日期：[名字] / 2026-XX-XX
- 基线提交：[main 分支 HEAD SHA]

## 1. 预发布检查

- [ ] 全部目标 Issue/PR 已合并，`main` 无未合入的必要修复。
- [ ] CI 在基线提交全绿（lint + test）。
- [ ] 版本号已按变更类型确定并写入 `RELEASE_NOTES` 草稿。
- [ ] 数据库迁移（如有）已在测试库演练一次。

## 2. 构建与产物

- [ ] 干净目录 `git clone` → 按零基础步骤安装成功（无全局残留依赖）。
- [ ] `python -m pytest -q` 在干净环境全绿。
- [ ] 启动脚本/命令验证通过，`/health` 返回 200。
- [ ] 产物（如导出模板、文档包）已生成并抽查。

## 3. 数据与迁移

- [ ] 迁移前备份已执行并验证可打开（SQLite：`.backup` 生成文件 + `PRAGMA integrity_check`）。
- [ ] 迁移脚本幂等（重复执行不重复加列）。
- [ ] 迁移后冒烟：旧数据可读、新字段默认值正确。

## 4. 部署

- [ ] 部署目标与配置（环境变量、端口、密钥来源）核对无误。
- [ ] 部署后健康检查通过，核心流程手工走通一条（添加→查看→删除）。
- [ ] 日志能看到本次启动记录。

## 5. 回滚方案（发布前必须先想好）

- [ ] 代码回滚：回滚到上一版本标签的具体命令已写明（`git switch --detach v1.2.0` + 重新部署）。
- [ ] 数据回滚：迁移是否可逆；不可逆时，恢复方式为“从备份还原”并写明步骤与数据丢失窗口。
- [ ] 责任人与执行时机已约定。

## 6. 发布动作

- [ ] 打标签并推送：`git tag -a vX.Y.Z -m "..."`。
- [ ] GitHub Release / 内部公告发布，附 CHANGELOG 与已知问题。
- [ ] `RELEASE_NOTES` 归档进仓库 `docs/releases/`。

## 7. 发布后观察

- [ ] 24h 内检查：错误日志、健康检查、关键功能抽查。
- [ ] 问题处理预案：发现 P0 时先回滚再排查。

## 完成条件

- 全部勾选且证据可追溯；回滚方案“纸上可执行”；发布记录与标签指向一致。

---

# 运行维护手册（Runbook）

> 给“三个月后的你”或接手人：怎么把它跑起来、坏了先看哪里、怎么备份恢复。
> 位置：`docs/runbooks/operations.md`；重大变化时更新版本。

- 适用版本：v1.2.x
- 更新人 / 日期：[名字] / 2026-XX-XX

## 1. 启动与停止

```powershell
# 启动（开发）
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
# 健康检查
curl http://127.0.0.1:8000/health   # 期望 {"status":"ok"}
```

- 停止：直接结束进程（本地单机，无优雅停机需求）；重启后数据持久于 `data/app.db`。

## 2. 常用命令

| 目的 | 命令 |
|---|---|
| 跑测试 | `python -m pytest -q` |
| 静态检查 | `python -m ruff check .` |
| 导出 CSV | 页面点击“导出”，或 `python -m app.tools.export` |
| 备份数据库 | `python scripts/backup_db.py`（内部调用 SQLite `.backup`） |
| 校验备份 | `python -c "import sqlite3;s=sqlite3.connect('backups/latest.db');print(s.execute('PRAGMA integrity_check').fetchone())"` |

## 3. 日志与观测

- 应用日志：控制台输出 + `logs/app.log`（RotatingFileHandler，5MB×3）。
- 看什么：启动 banner、5xx 堆栈、慢请求（>1s）。
- 无外部监控；判断存活的最低标准：`/health` 200。

## 4. 备份与恢复

- 策略：每次发版前 + 每周一自动备份到 `backups/YYYYMMDD/`。
- 恢复步骤（数据错误/迁移失败时）：
  1. 停止服务。
  2. `copy backups\YYYYMMDD\app.db data\app.db`（先改名旧库为 `app.db.bad`）。
  3. 启动服务 → `/health` → 抽查最近一条订阅记录。

## 5. 常见故障处理

| 症状 | 先查 | 处理 |
|---|---|---|
| 端口被占用 | `netstat -ano \| findstr 8000` | 结束占用进程或换 `--port 8001` |
| 启动报 ModuleNotFoundError | 虚拟环境是否激活 | 重新 Activate 再安装依赖 |
| 页面能开但接口 500 | `logs/app.log` 最后堆栈 | 按堆栈定位；无法定位则回滚到上一版本 |
| 数据库 locked | 是否两个进程同写 | 关闭多余进程；单人使用不应出现，出现则提 Issue |

## 6. 升级与迁移

- 升级前：执行第 4 节备份；对照 `docs/releases/` 的迁移说明。
- 迁移失败：执行“恢复步骤”；迁移脚本问题记录为 Issue，不手工改库。

## 7. 责任与联系

- 维护人：[名字]；升级窗口：周末；紧急联系：[方式]。

## 完成条件

- 新人按本文档 15 分钟内可完成“启动→健康检查→备份→恢复演练”四件事；故障表覆盖最近 3 个月实际故障。

---

# 会话交接文档（Handoff）

> 让一个新的 AI 会话（或同事）不读聊天记录就能继续干活。
> 原则：只写“当前事实”，不写过程叙事；信息以仓库为准，本文负责指路。

- 项目：subscription-tracker
- 目标版本：v1.2 → 准备 v1.2.1
- 更新人 / 日期：[名字] / 2026-XX-XX
- 预计交接时长：新会话读完本文 + 关键文件 ≤ 10 分钟

## 1. 项目是什么

个人订阅与续费管理器：本地运行，FastAPI + SQLite，管理订阅记录并提醒到期。
- 入口文档：`README.md`（运行）→ `AGENTS.md`（协作规则）→ `ARCHITECTURE.md`（结构）。
- 规格：`specs/`；决策：`docs/decisions/`；当前计划：`docs/plan.md`。

## 2. 当前状态

| 项 | 状态 |
|---|---|
| 分支 | `main`（HEAD: 4b7f9d1） |
| CI | 绿（最近一次 run #182） |
| 测试 | 38 passed |
| 版本 | v1.2 已发布；v1.2.1 进行中 |

## 3. 已完成（本迭代）

- billing_cycle 字段迁移（T1—T4）：迁移脚本 + 回归测试 + 备份演练，见 PR #31。
- CSV 导出特殊字符修复（ISSUE-014）：已合入并有回归测试。

## 4. 进行中 / 下一步

- [ ] T5（doing）：年付订阅的“按月折算展示”——方案已定（见 `docs/plan.md` 第 4 节），实现未开始。
- [ ] T6（todo）：Renovate 配置接入（参考 `ch16` 章节）。
- [ ] T7（todo）：更新 `docs/runbooks/operations.md` 的备份策略段落。

## 5. 已知问题与约束

- 年付记录的“下一次续费日”计算暂只支持整年，不支持自定义月数（记录在 spec 非目标）。
- 并发写 SQLite 未处理（ADR-0002 已接受该限制）。
- 不要直接修改 `docs/generated/` 下文件（机器生成，重跑脚本产出）。

## 6. 关键文件索引

| 要改什么 | 去哪 |
|---|---|
| API 行为 | `app/routes.py` + `specs/…/api.md` |
| 数据结构 | `app/database.py` + `app/schemas.py` + 迁移脚本 `scripts/migrations/` |
| 前端交互 | `app/static/app.js` |
| 协作规则 | `AGENTS.md` |
| 验收口径 | `docs/acceptance.md` + `templates/definition-of-done.md` |

## 7. 新会话第一步建议

1. 读本文 → 跑 `python -m pytest -q` 确认基线绿。
2. 领取第 4 节第一个未勾选项，先写验证方法再动代码。
3. 完成后更新本文的“已完成/进行中”。

## 完成条件

- 状态表与仓库实际一致（分支、CI、测试数）；下一步有明确验收方法；新会话按第 7 节可立即开工。

---

# 完成定义（Definition of Done）

> 团队与 AI 共同的“什么算做完”。任何任务、PR、版本宣称完成前逐项对照。
> 用法：贴在 `AGENTS.md` 末尾或 PR 模板；AI 宣称完成时引用本清单逐条核验。

- 适用范围：subscription-tracker 全部开发与维护工作
- 版本：v1.0（2026-XX-XX）

## 1. 代码

- [ ] 改动范围与任务描述一致，无无关文件。
- [ ] 遵循 `ARCHITECTURE.md` 依赖方向（routes → repository → database）。
- [ ] 新增依赖有理由记录（ADR 或 PR 描述）。
- [ ] `python -m ruff check .` 0 错误。

## 2. 测试（实现者不自行宣布通过）

- [ ] 新行为有测试；修复必有回归测试（先红后绿）。
- [ ] 边界用例覆盖：空值、特殊字符、上限、非法日期。
- [ ] `python -m pytest -q` 全绿（附输出）。
- [ ] 抽查至少 1 条测试确为“断言业务行为”。

## 3. 文档

- [ ] 行为变化已同步：spec 版本行、`AGENTS.md`、`ARCHITECTURE.md`（如涉及）。
- [ ] 用户可见变化已更新 README。
- [ ] 机器生成文档未手改，已重跑生成脚本。

## 4. 数据与兼容

- [ ] 涉及表结构：有迁移脚本 + 迁移前备份 + 幂等性验证。
- [ ] API 变更向后兼容；破坏性变更已升主版本并更新调用方。
- [ ] 旧数据读写验证通过（至少一条真实历史记录）。

## 5. 交付证据

- [ ] 验收命令输出或截图已留存（PR 描述或 `docs/evidence/`）。
- [ ] 对应任务/Issue 的验收标准逐条勾选。
- [ ] 干净目录复验通过（clone → install → test → run）。

## 6. 维护性

- [ ] Git 提交拆分合理，信息符合 `feat:/fix:/test:/docs:` 约定。
- [ ] `tasks.md` 状态与验证证据已更新。
- [ ] 若产生新踩坑经验：已追加到 `appendices/C-failure-catalog.md` 对应类别或新建条目。

## 7. 发布（仅版本级任务）

- [ ] `release-checklist.md` 全绿；标签与发布说明一致；回滚方案可执行。

## 特殊说明

- “AI 说已完成”“本地看起来没问题”“截图能打开”均**不**满足本清单。
- 无法满足某项时，任务状态只能标 `blocked` 并写明原因，不得标 `done`。
