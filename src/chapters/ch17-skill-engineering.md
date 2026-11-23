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
