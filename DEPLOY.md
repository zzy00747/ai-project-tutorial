# Cloudflare Pages 部署说明

本仓库的站点产物已预构建在 `site/` 目录，纯静态 HTML，无任何构建依赖。

## 方式一：Cloudflare Pages（推荐）

1. GitHub 仓库 → 直接在 Cloudflare Dashboard 创建 Pages 项目并连接该仓库。
2. 构建设置：
   - **Framework preset**: `None`
   - **Build command**: 留空（或 `python scripts/build_site.py`，如需每次重新生成）
   - **Build output directory**: `site`
3. 保存后每次 push 自动部署。

## 方式二：只部署 site/ 目录

```powershell
npx wrangler pages deploy site --project-name ai-project-tutorial
```

## 方式三：GitHub Pages

仓库 Settings → Pages → Source 选 `Deploy from a branch`，分支选 `main`、目录选 `/site`（需先在 Settings → Actions 允许，或改用 GitHub Actions 部署）。

## 本地重新构建站点

```powershell
python -m pip install markdown pygments
python scripts/build_site.py     # 生成/刷新 site/
python -m http.server 8765 --directory site   # 本地预览 http://127.0.0.1:8765
```

## 站点功能

- 明暗主题（跟随系统 + 手动切换，localStorage 持久化）
- 全文搜索（`assets/search-index.json`，标题加权）
- 侧边栏分组导航 + 当前页高亮 + 上一页/下一页
- 代码块 Pygments 高亮（亮色 friendly / 暗色 monokai）+ 一键复制
- 响应式：≤900px 侧边栏变抽屉；打印样式隐藏导航
- 零 CDN 依赖，离线可打开
