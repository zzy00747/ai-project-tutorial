# 《AI 项目实战》写作与集成契约

本文件用于保证多名作者写出的章节可以组合成同一套教程。

## 1. 教程定位

- 书名：**AI 项目实战：从零生成、验收到持续维护**。
- 读者：会使用电脑，但可能没有编程经验；或能生成 Demo、但不会交付和维护的人。
- 语言：简体中文；技术标识、命令、日志保留英文。
- 风格：实用、清楚、直接。先让读者完成任务，再解释必要原理。
- 核心立场：AI 可以承担实现，人负责意图、选择、验收与项目控制权。
- 不写工具宣传，不用“颠覆”“碾压”“零基础七天精通”等营销措辞。
- 不把 AI 的自我声明当验证结果；所有完成结论都应有命令、测试、Diff、截图或发布记录支撑。

## 2. 贯穿项目与版本

项目：**个人订阅与续费管理器（Subscription Tracker）**。

默认技术栈：Python 3.12+、FastAPI、SQLite、原生 HTML/CSS/JavaScript、pytest、Ruff、GitHub Actions。

版本路线：

| 版本 | 功能与阶段 |
|---|---|
| v0.0 | 第1章的一次性原型，仅用于观察失控风险 |
| v0.1 | 第7章：添加、查看订阅；打通界面→API→SQLite |
| v0.2 | 第8章：修改、删除、输入校验；小任务、小 Diff、小 PR |
| v1.0 | 第9—11章：测试、CSV 导出、CI、部署与发布 |
| v1.1 | 第12—14章：Bug 修复、搜索筛选、局部重构、旧项目接手 |
| v1.2 | 第15章：增加 billing_cycle 字段、数据库迁移、备份恢复 |
| v1.2.1 | 第16章：依赖维护、文档校正、运行观测与补丁发布 |

初始订阅字段：`id`、`name`、`amount`、`currency`、`renewal_date`、`note`、`created_at`。
第15章新增 `billing_cycle`，值限定为 `monthly`、`yearly`，默认 `monthly`。
金额示例优先使用“分”为单位的整数或在文中明确精度风险，不悄悄混用浮点与整数。
核心 API：`/api/subscriptions`；健康检查：`/health`。

## 3. 项目目录约定

```text
subscription-tracker/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ database.py
│  ├─ schemas.py
│  ├─ repository.py
│  ├─ routes.py
│  └─ static/
│     ├─ index.html
│     ├─ app.js
│     └─ styles.css
├─ tests/
│  ├─ test_api.py
│  └─ test_repository.py
├─ docs/
│  ├─ intent.md
│  ├─ acceptance.md
│  ├─ plan.md
│  ├─ tasks.md
│  ├─ decisions/
│  ├─ runbooks/
│  └─ handoff.md
├─ specs/
├─ scripts/
├─ .github/workflows/ci.yml
├─ AGENTS.md
├─ ARCHITECTURE.md
├─ requirements.txt
└─ README.md
```

## 4. 统一命令

优先使用跨平台命令；涉及终端时以 Windows PowerShell 为主，同时给 macOS/Linux 的必要差异。

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1             # Windows PowerShell
# source .venv/bin/activate             # macOS/Linux
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
python -m pytest -q
python -m ruff check .
```

Git 使用：

```powershell
git switch -c feat/example
git status
git diff --stat
git diff
git add PATH
git commit -m "feat: describe one change"
```

不要假定读者的全局 Python、Node.js 或 Docker 已安装；章节需要时应先说明。
不要编造测试通过数量、耗时、版本号、控制台输出或产品能力。
示例输出若只是结构演示，必须标注“示意”。

## 5. 每章固定结构

每章使用以下 12 个二级标题，允许在“操作步骤”内部增加三级标题：

```markdown
# 第 N 章　标题

> 本章成果：一句话。

## 1. 本章成果
## 2. 为什么需要它
## 3. 最少必备知识
## 4. 起始项目状态
## 5. 操作步骤与 AI 任务示例
## 6. AI 应生成的产物
## 7. 人工检查点
## 8. 验收命令与通过标准
## 9. 常见失败及恢复方法
## 10. 本章 Git 提交
## 11. 练习与扩展
## 12. 参考资料
```

写作要求：

- 正文目标为每章约 2500—4500 中文字，复杂章节可以更长，但不得用空泛概述凑篇幅。
- 第5节必须有可执行的 numbered steps、至少一个具体 AI 任务示例，以及必要代码或文件片段。
- AI 任务示例使用 `text` 代码块，包含：目标、上下文、范围、约束、验收、输出。
- 代码片段应尽可能完整；省略处用明确注释，不能用模糊的“这里省略所有实现”。
- 第7节告诉读者具体看什么，不只写“认真检查”。
- 第8节提供命令或可观察通过标准，不伪造结果。
- 第9节至少写 3 个“症状→原因→恢复动作”。
- 第10节给出建议分支、提交拆分和提交信息，不要求作者真的执行提交。
- 第12节列 2—5 个高相关一手来源；已在对话中核验的来源可直接引用，不确定的信息不写。
- 本章新增文件必须在正文中解释用途；不能让读者依赖不存在的配套网站或仓库。

## 6. 文件命名

```text
ch01-why-projects-fail.md
ch02-project-basics.md
ch03-git-safety.md
ch04-intent-and-acceptance.md
ch05-spec-driven-development.md
ch06-architecture-and-planning.md
ch07-vertical-slice.md
ch08-small-steps-and-prs.md
ch09-testing-and-debugging.md
ch10-context-engineering.md
ch11-ci-release-deploy.md
ch12-issue-driven-maintenance.md
ch13-change-and-refactoring.md
ch14-legacy-modernization.md
ch15-data-migration-recovery.md
ch16-long-term-maintenance.md
ch17-skill-engineering.md
ch18-subagents-and-automation.md
ch19-platforms-and-tool-migration.md
ch20-capstone.md
```

实验：

```text
lab01-disposable-prototype.md
lab02-project-blueprint.md
lab03-release-v1.md
lab04-evolution-v1-1.md
lab05-three-month-maintenance.md
```

## 7. 链接与版权

- 教程文件之间使用相对链接。
- 引用外部资料时写标题与 URL，不复制大段原文。
- 参考 GSE、ChiYu、Spec Kit、Vibe Coding Guide 等的结构和方法，正文案例与表述独立创作。
- 商业课程只参考公开大纲，不声称体验过付费内容。
- 对已归档或停止维护的项目明确标注，不安排读者安装其旧依赖。

## 8. 集成边界

- 每位作者只写分配给自己的文件，不修改 README、其他章节或共享模板。
- 章末暂时不写“上一章/下一章”，由主 Agent 统一生成。
- 不创建 Git 提交，不推送。
- 完成后返回：文件列表、字数概况、依赖的其他章节、需要主 Agent 统一处理的问题。
