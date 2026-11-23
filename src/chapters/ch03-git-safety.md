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
