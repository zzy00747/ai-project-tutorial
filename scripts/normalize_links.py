#!/usr/bin/env python3
"""Normalize internal links for MkDocs: .html targets back to .md.

MkDocs resolves links against source .md files and rewrites them to .html at build
time. Only links pointing at files that actually exist under src/ are rewritten;
external http(s) links and anchors are untouched.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"

LINK = re.compile(r"\]\(([^()\s#]+?)\.html((?:#[A-Za-z0-9_\-]*)?)\)")


def main() -> int:
    total = 0
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")

        def repl(m: re.Match) -> str:
            target, anchor = m.group(1), m.group(2)
            if target.startswith(("http://", "https://", "//")):
                return m.group(0)
            candidate = (path.parent / target).with_suffix(".md").resolve()
            if candidate.is_file():
                return f"]({target}.md{anchor})"
            return m.group(0)

        new, n = LINK.subn(repl, text)
        if n:
            path.write_text(new, encoding="utf-8")
            print(f"{path.relative_to(ROOT.parent)}: normalized {n} link(s)")
            total += n
    print(f"total normalized: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
