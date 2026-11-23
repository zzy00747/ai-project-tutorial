# 部署说明

站点由 **Material for MkDocs**（27.6k★，Python）构建，产物输出到 `site/`。

## 本地构建与预览

```powershell
python -m pip install mkdocs-material mkdocs-minify-plugin
mkdocs serve            # http://127.0.0.1:8000 实时预览
mkdocs build --strict   # 产物在 site/
```

## 方式一：Cloudflare Pages（推荐）

1. Cloudflare Dashboard → Pages → 连接本仓库。
2. 构建设置：
   - **Framework preset**: `None`（或 MkDocs，若列表可选）
   - **Build command**: `pip install mkdocs-material mkdocs-minify-plugin && mkdocs build`
   - **Build output directory**: `site`
   - Python 版本需 ≥ 3.9（环境变量 `PYTHON_VERSION=3.13`）
3. 保存后每次 push 自动部署。

## 方式二：GitHub Pages

仓库已含 `.github/workflows/docs.yml`：push 到 main 自动构建并发布到 GitHub Pages（需在 Settings → Pages → Source 选 **GitHub Actions**）。

## 方式三：只部署 site/ 目录

```powershell
npx wrangler pages deploy site --project-name ai-project-tutorial
```

## 站点能力（Material 主题内置）

- 明暗主题切换（跟随系统 + 手动，持久化）
- 全文搜索（中文分词优化 + 搜索建议/高亮/分享）
- 侧边栏分组导航 + 当前页高亮 + 章节内嵌 TOC（toc.integrate）
- 代码块一键复制 + Pygments 高亮 + 行号锚点
- 回到顶部、页脚上下篇、Instant loading、页眉编辑/查看源码按钮
- 响应式移动端适配、打印样式、无障碍焦点
