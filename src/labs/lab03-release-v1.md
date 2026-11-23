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
