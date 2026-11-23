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
