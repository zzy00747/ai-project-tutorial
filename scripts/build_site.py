#!/usr/bin/env python3
"""Build a polished static docs site from Markdown sources (no Node/Rust).

Usage: python scripts/build_site.py
Output: site/ (pure static, deploy to Cloudflare Pages directly)
"""
from __future__ import annotations

import html as html_mod
import json
import re
import shutil
import sys
from html.parser import HTMLParser
from pathlib import Path

import markdown
from pygments import highlight as pyg_highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
OUT = ROOT / "site"
ASSETS = OUT / "assets"

# (source rel path, group label)
PAGES: list[tuple[str, str]] = [
    ("index.md", "开始"),
    ("chapters/ch01-why-projects-fail.md", "第一部分 · 建立正确的 AI 开发方式"),
    ("labs/lab01-disposable-prototype.md", "第一部分 · 建立正确的 AI 开发方式"),
    ("chapters/ch02-project-basics.md", "第一部分 · 建立正确的 AI 开发方式"),
    ("chapters/ch03-git-safety.md", "第一部分 · 建立正确的 AI 开发方式"),
    ("chapters/ch04-intent-and-acceptance.md", "第二部分 · 从想法到可实施规格"),
    ("chapters/ch05-spec-driven-development.md", "第二部分 · 从想法到可实施规格"),
    ("chapters/ch06-architecture-and-planning.md", "第二部分 · 从想法到可实施规格"),
    ("labs/lab02-project-blueprint.md", "第二部分 · 从想法到可实施规格"),
    ("chapters/ch07-vertical-slice.md", "第三部分 · AI 生成、验证与首次交付"),
    ("chapters/ch08-small-steps-and-prs.md", "第三部分 · AI 生成、验证与首次交付"),
    ("chapters/ch09-testing-and-debugging.md", "第三部分 · AI 生成、验证与首次交付"),
    ("chapters/ch10-context-engineering.md", "第三部分 · AI 生成、验证与首次交付"),
    ("chapters/ch11-ci-release-deploy.md", "第三部分 · AI 生成、验证与首次交付"),
    ("labs/lab03-release-v1.md", "第三部分 · AI 生成、验证与首次交付"),
    ("chapters/ch12-issue-driven-maintenance.md", "第四部分 · 从会生成到能长期维护"),
    ("chapters/ch13-change-and-refactoring.md", "第四部分 · 从会生成到能长期维护"),
    ("chapters/ch14-legacy-modernization.md", "第四部分 · 从会生成到能长期维护"),
    ("chapters/ch15-data-migration-recovery.md", "第四部分 · 从会生成到能长期维护"),
    ("chapters/ch16-long-term-maintenance.md", "第四部分 · 从会生成到能长期维护"),
    ("labs/lab04-evolution-v1-1.md", "第四部分 · 从会生成到能长期维护"),
    ("labs/lab05-three-month-maintenance.md", "第四部分 · 从会生成到能长期维护"),
    ("chapters/ch17-skill-engineering.md", "第五部分 · 沉淀为可复用的 AI 工程能力"),
    ("chapters/ch18-subagents-and-automation.md", "第五部分 · 沉淀为可复用的 AI 工程能力"),
    ("chapters/ch19-platforms-and-tool-migration.md", "第五部分 · 沉淀为可复用的 AI 工程能力"),
    ("chapters/ch20-capstone.md", "第五部分 · 沉淀为可复用的 AI 工程能力"),
    ("appendices/A-environment.md", "附录"),
    ("appendices/B-command-reference.md", "附录"),
    ("appendices/C-failure-catalog.md", "附录"),
    ("appendices/D-glossary.md", "附录"),
    ("appendices/E-sources.md", "附录"),
    ("templates-intro.md", "可复制模板"),
    ("templates/intent.md", "可复制模板"),
    ("templates/spec.md", "可复制模板"),
    ("templates/plan.md", "可复制模板"),
    ("templates/tasks.md", "可复制模板"),
    ("templates/adr.md", "可复制模板"),
    ("templates/issue.md", "可复制模板"),
    ("templates/bug-report.md", "可复制模板"),
    ("templates/pr-checklist.md", "可复制模板"),
    ("templates/release-checklist.md", "可复制模板"),
    ("templates/runbook.md", "可复制模板"),
    ("templates/handoff.md", "可复制模板"),
    ("templates/definition-of-done.md", "可复制模板"),
]

SITE_NAME = "AI 项目实战"
SITE_SUBTITLE = "从零生成、验收到持续维护"

MD = markdown.Markdown(
    extensions=["extra", "toc", "sane_lists", "codehilite"],
    extension_configs={"codehilite": {"guess_lang": False, "css_class": "hl"}},
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        if tag in ("script", "style"):
            self._skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style") and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip_depth and data.strip():
            self.parts.append(data.strip())


def plain_text(html: str, limit: int = 6000) -> str:
    parser = TextExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass
    text = " ".join(parser.parts)
    text = re.sub(r"\s+", " ", text)
    return text[:limit]


def md_link_to_html(text: str) -> str:
    """Rewrite internal .md hrefs in already-rendered HTML to .html (anchors kept)."""
    def href_repl(m: re.Match) -> str:
        target = m.group(1)
        new = re.sub(r"\.md(?=(#[A-Za-z0-9_\-]+)?$)", ".html", target)
        return f'href="{new}"'

    return re.sub(r'href="([^"]+\.md(?:#[A-Za-z0-9_\-]+)?)"', href_repl, text)


def highlight_code(html: str) -> str:
    """Wrap pygments codehilite output with copy button; highlight bare pre blocks."""
    def wrap(match: re.Match) -> str:
        return (
            '<div class="code-wrap">'
            '<button class="copy-btn" type="button">复制</button>'
            + match.group(0)
            + "</div>"
        )

    html = re.sub(r'<div class="hl">.*?</div>', wrap, html, flags=re.DOTALL)
    html = re.sub(r"<pre><code>", '<pre><code class="hl">', html)
    html = re.sub(
        r"<pre><code[^>]*>.*?</pre>",
        wrap,
        html,
        flags=re.DOTALL,
    )
    return html


def convert(src_path: Path) -> str:
    text = src_path.read_text(encoding="utf-8")
    MD.reset()
    body = MD.convert(text)
    body = md_link_to_html(body)
    body = highlight_code(body)
    return body


def first_heading(html: str, fallback: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1))
        return html_mod.unescape(title).strip() or fallback
    return fallback


CSS = """\
:root{--bg:#faf9f7;--surface:#fff;--sidebar:#f3f2ee;--text:#1f2328;--text-2:#57606a;--border:#e4e2dc;--accent:#4f46e5;--accent-2:#7c3aed;--radius:10px;--shadow:0 1px 3px rgb(0 0 0/.08);--font-sans:-apple-system,"Segoe UI","Microsoft YaHei","PingFang SC","Noto Sans SC",sans-serif;--font-mono:"Cascadia Code",Consolas,"JetBrains Mono",monospace}
[data-theme="dark"]{--bg:#101014;--surface:#18181f;--sidebar:#14141a;--text:#e6e6ea;--text-2:#9a9aa5;--border:#2a2a33;--accent:#818cf8;--accent-2:#a78bfa;--shadow:0 1px 3px rgb(0 0 0/.4)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.8 var(--font-sans)}
a{color:var(--accent);text-decoration:none;transition:.15s ease}a:hover{text-decoration:underline;text-underline-offset:3px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:14px;padding:10px 20px;background:color-mix(in srgb,var(--bg) 80%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--border)}
.topbar .brand{font-weight:700;font-size:1.05rem;color:var(--text);white-space:nowrap}
.topbar .brand small{color:var(--text-2);font-weight:400;margin-left:8px}
.topbar .spacer{flex:1}
.searchbox{position:relative;width:min(320px,40vw)}
.searchbox input{width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:999px;background:var(--surface);color:var(--text);font:inherit}
.searchbox input:focus{border-color:var(--accent);outline:none;box-shadow:0 0 0 3px color-mix(in srgb,var(--accent) 25%,transparent)}
.search-results{position:absolute;top:110%;left:0;right:0;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);max-height:340px;overflow:auto;display:none}
.search-results a{display:block;padding:8px 14px;color:var(--text);border-bottom:1px solid var(--border)}
.search-results a:last-child{border-bottom:0}
.search-results a b{color:var(--accent)}
.search-results a small{display:block;color:var(--text-2);font-size:.82rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.search-empty{padding:10px 14px;color:var(--text-2);font-size:.9rem}
.theme-btn{border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:999px;padding:6px 12px;cursor:pointer;font:inherit}
.theme-btn:hover{border-color:var(--accent)}
.layout{display:grid;grid-template-columns:280px minmax(0,1fr);gap:0;align-items:start}
.sidebar{position:sticky;top:57px;height:calc(100vh - 57px);overflow:auto;padding:18px 14px 40px;background:var(--sidebar);border-right:1px solid var(--border)}
.sidebar .group{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-2);margin:18px 10px 6px;font-weight:600}
.sidebar a{display:block;padding:6px 10px;border-radius:8px;color:var(--text);font-size:.92rem;line-height:1.5;border-left:3px solid transparent;margin:1px 0}
.sidebar a:hover{background:color-mix(in srgb,var(--accent) 8%,transparent);text-decoration:none}
.sidebar a.active{border-left-color:var(--accent);background:color-mix(in srgb,var(--accent) 12%,transparent);font-weight:600}
.content{padding:36px 32px 80px;min-width:0}
article{max-width:76ch;margin:0 auto;animation:fadein .3s ease}
@keyframes fadein{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
article h1{font-size:1.9rem;line-height:1.35;margin:0 0 .8em}
article h2{font-size:1.4rem;margin:2em 0 .6em;padding-bottom:.3em;border-bottom:1px solid var(--border)}
article h3{font-size:1.15rem;margin:1.6em 0 .5em}
article h4{font-size:1rem;margin:1.4em 0 .4em}
article p{text-align:justify;margin:.9em 0}
article ul,article ol{padding-left:1.6em;margin:.8em 0}
article li{margin:.35em 0}
article blockquote{margin:1.2em 0;padding:.8em 1.1em;background:var(--surface);border-left:3px solid var(--accent);border-radius:var(--radius);color:var(--text-2)}
article blockquote p{margin:.3em 0;text-align:left}
article hr{border:0;border-top:1px solid var(--border);margin:2em 0}
article img{max-width:100%;border-radius:var(--radius)}
code{font-family:var(--font-mono);font-size:.9em;background:color-mix(in srgb,var(--accent) 10%,transparent);padding:.15em .4em;border-radius:5px}
pre{position:relative;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1em 1.1em;overflow:auto;font-size:.88rem;line-height:1.6;margin:1.1em 0}
pre code{background:none;padding:0}
.code-wrap{position:relative;margin:1.1em 0}
.code-wrap pre{margin:0}
.copy-btn{position:absolute;top:8px;right:8px;z-index:2;border:1px solid var(--border);background:var(--bg);color:var(--text-2);border-radius:6px;padding:3px 9px;font-size:.75rem;cursor:pointer;opacity:0;transition:.15s ease;font-family:var(--font-sans)}
.code-wrap:hover .copy-btn{opacity:1}
.copy-btn:hover{color:var(--accent);border-color:var(--accent)}
.copy-btn.copied{color:#16a34a;border-color:#16a34a;opacity:1}
.tbl-wrap{overflow:auto;margin:1.2em 0}
article table{border-collapse:collapse;width:100%;font-size:.92rem;background:var(--surface);border-radius:var(--radius)}
article th{background:var(--sidebar);font-weight:600;text-align:left}
article th,article td{border:1px solid var(--border);padding:.5em .75em}
article tbody tr:nth-child(even){background:color-mix(in srgb,var(--sidebar) 55%,transparent)}
.pagenav{display:flex;justify-content:space-between;gap:12px;margin-top:3em;padding-top:1.2em;border-top:1px solid var(--border)}
.pagenav a{padding:10px 14px;border:1px solid var(--border);border-radius:var(--radius);background:var(--surface);max-width:46%}
.pagenav a small{display:block;color:var(--text-2);font-size:.78rem}
.pagenav a.next{text-align:right;margin-left:auto}
footer{padding:26px 20px;color:var(--text-2);font-size:.85rem;text-align:center;border-top:1px solid var(--border)}
.hamburger{display:none;border:1px solid var(--border);background:var(--surface);border-radius:8px;padding:6px 10px;cursor:pointer;font:inherit;color:var(--text)}
@media (max-width:900px){
.layout{display:block}
.sidebar{position:fixed;left:0;top:0;bottom:0;z-index:40;width:280px;transform:translateX(-100%);transition:transform .2s ease;height:100vh;border-right:1px solid var(--border)}
.sidebar.open{transform:none;box-shadow:0 0 40px rgb(0 0 0/.25)}
.hamburger{display:inline-block}
.content{padding:24px 18px 60px}
.searchbox{width:min(200px,38vw)}
}
@media print{.topbar,.sidebar,.pagenav,.copy-btn{display:none!important}.layout{display:block}.content{padding:0}.article,article{max-width:none}}
.hl{background:transparent}
:root:not([data-theme="dark"]) .hl{""" + HtmlFormatter(style="friendly").get_style_defs(".hl") + """}
[data-theme="dark"] .hl{""" + HtmlFormatter(style="monokai").get_style_defs(".hl") + """}
"""

THEME_INIT = """\
(function(){try{var t=localStorage.getItem('theme');if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';document.documentElement.dataset.theme=t;}catch(e){document.documentElement.dataset.theme='light';}})();
"""

APP_JS = """\
(function(){
  var btn=document.querySelector('.theme-btn');
  if(btn){btn.addEventListener('click',function(){
    var cur=document.documentElement.dataset.theme==='dark'?'light':'dark';
    document.documentElement.dataset.theme=cur;try{localStorage.setItem('theme',cur);}catch(e){}
  });}
  var ham=document.querySelector('.hamburger'),sb=document.querySelector('.sidebar');
  if(ham&&sb){ham.addEventListener('click',function(){sb.classList.toggle('open');});}
  document.addEventListener('click',function(e){
    if(sb&&sb.classList.contains('open')&&!sb.contains(e.target)&&e.target!==ham&&!ham.contains(e.target))sb.classList.remove('open');
  });
  document.querySelectorAll('.copy-btn').forEach(function(b){
    b.addEventListener('click',function(){
      var code=b.parentElement.querySelector('pre');
      if(!code)return;
      var t=code.innerText;
      (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){
        b.textContent='已复制';b.classList.add('copied');
        setTimeout(function(){b.textContent='复制';b.classList.remove('copied');},1600);
      },function(){b.textContent='请手动复制';setTimeout(function(){b.textContent='复制';},1600);});
    });
  });
  // search
  var box=document.querySelector('.searchbox input'),panel=document.querySelector('.search-results');
  if(!box||!panel)return;var index=[];
  fetch((document.baseURI.replace(/[^/]*$/,''))+'assets/search-index.json').then(function(r){return r.json();}).then(function(d){index=d;}).catch(function(){});
  function render(q){
    if(!q){panel.style.display='none';panel.innerHTML='';return;}
    var ql=q.toLowerCase(),out=[];
    for(var i=0;i<index.length&&out.length<10;i++){
      var it=index[i],score=0;
      if(it.t.toLowerCase().indexOf(ql)>=0)score+=3;
      if(it.c.toLowerCase().indexOf(ql)>=0)score+=1;
      if(score)out.push({t:it.t,u:it.u,c:it.c,s:score});
    }
    out.sort(function(a,b){return b.s-a.s;});
    panel.innerHTML=out.length?out.map(function(o){
      var pos=o.c.toLowerCase().indexOf(ql);
      var snip=pos>=0?o.c.slice(Math.max(0,pos-40),pos+80):o.c.slice(0,120);
      return '<a href="'+o.u+'"><b>'+o.t+'</b><small>…'+snip+'…</small></a>';
    }).join(''):'<div class="search-empty">没有找到相关内容</div>';
    panel.style.display='block';
  }
  box.addEventListener('input',function(){render(box.value.trim());});
  box.addEventListener('focus',function(){if(box.value.trim())render(box.value.trim());});
  document.addEventListener('click',function(e){
    if(!panel.contains(e.target)&&e.target!==box)panel.style.display='none';
  });
})();
"""


def out_rel(src_rel: str) -> str:
    return src_rel[:-3] + ".html"


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    ASSETS.mkdir(parents=True)

    pages = []
    for src_rel, group in PAGES:
        src_path = SRC / src_rel
        if not src_path.is_file():
            print(f"skip missing: {src_rel}")
            continue
        pages.append((src_rel, group, src_path))

    converted: dict[str, str] = {}
    for src_rel, _, src_path in pages:
        body = convert(src_path)
        converted[src_rel] = body

    groups: list[tuple[str, list[tuple[str, str, str]]]] = []
    for src_rel, group, _ in pages:
        if groups and groups[-1][0] == group:
            groups[-1][1].append((src_rel, out_rel(src_rel), first_heading(converted[src_rel], src_rel)))
        else:
            groups.append((group, [(src_rel, out_rel(src_rel), first_heading(converted[src_rel], src_rel))]))

    nav_html_parts = []
    for group, items in groups:
        nav_html_parts.append(f'<div class="group">{html_mod.escape(group)}</div>')
        for _, href, title in items:
            nav_html_parts.append(f'<a href="{href}" data-nav="{href}">{html_mod.escape(title)}</a>')
    nav_html = "\n".join(nav_html_parts)

    index = []
    for src_rel, _, _ in pages:
        index.append({"t": first_heading(converted[src_rel], src_rel), "u": out_rel(src_rel), "c": plain_text(converted[src_rel])})
    (ASSETS / "search-index.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")

    total = len(pages)
    for i, (src_rel, _, src_path) in enumerate(pages):
        rel = out_rel(src_rel)
        body = converted[src_rel]
        title = first_heading(body, SITE_NAME)
        prev = pages[i - 1] if i > 0 else None
        nxt = pages[i + 1] if i < total - 1 else None

        pagenav = '<nav class="pagenav">'
        if prev:
            pagenav += f'<a href="{out_rel(prev[0])}"><small>← 上一篇</small>{html_mod.escape(first_heading(converted[prev[0]], prev[0]))}</a>'
        if nxt:
            pagenav += f'<a class="next" href="{out_rel(nxt[0])}"><small>下一篇 →</small>{html_mod.escape(first_heading(converted[nxt[0]], nxt[0]))}</a>'
        pagenav += "</nav>"

        page = f"""<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(title)} · {SITE_NAME}</title>
<script>{THEME_INIT}</script>
<style>{CSS}</style>
</head>
<body>
<header class="topbar">
<button class="hamburger" aria-label="打开目录">☰</button>
<a class="brand" href="index.html">{SITE_NAME}<small>{SITE_SUBTITLE}</small></a>
<div class="spacer"></div>
<div class="searchbox">
<input type="search" placeholder="搜索教程内容…" aria-label="搜索">
<div class="search-results"></div>
</div>
<button class="theme-btn" aria-label="切换主题">🌓</button>
</header>
<div class="layout">
<nav class="sidebar" aria-label="目录">{nav_html}</nav>
<main class="content"><article>{body}</article>{pagenav}</main>
</div>
<footer>{SITE_NAME} · {SITE_SUBTITLE} · 由纯静态 HTML 生成，可部署到 Cloudflare Pages / GitHub Pages</footer>
<script src="assets/app.js"></script>
</body>
</html>"""
        out_path = OUT / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page, encoding="utf-8")

    (ASSETS / "app.js").write_text(APP_JS, encoding="utf-8")
    print(f"built {total} pages -> {OUT}")


if __name__ == "__main__":
    sys.exit(build())
