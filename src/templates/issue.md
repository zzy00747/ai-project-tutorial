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
