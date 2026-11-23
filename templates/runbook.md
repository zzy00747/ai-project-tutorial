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
