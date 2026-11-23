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
