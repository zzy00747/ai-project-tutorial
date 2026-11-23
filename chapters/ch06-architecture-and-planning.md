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
