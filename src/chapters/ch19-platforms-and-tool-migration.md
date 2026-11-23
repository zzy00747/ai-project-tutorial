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
