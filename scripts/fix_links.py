#!/usr/bin/env python3
"""Fix markdown links whose closing parenthesis was stripped.

A broken link looks like:  [text](path.html   followed by space/CJK/pipe/etc.
We insert ')' right after the .html / .html#anchor target.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"

# target: something ending in .html or .html#anchor, NOT already followed by ')'
PATTERN = re.compile(r"\]\(([^()\s]*?\.html(?:#[A-Za-z0-9_\-]*)?)(?!\))(?=[\s|、，。；：！？])")


def fix_text(text: str) -> tuple[str, int]:
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        count += 1
        return "](" + m.group(1) + ")"

    return PATTERN.sub(repl, text), count


def main() -> int:
    total = 0
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        new, n = fix_text(text)
        if n:
            path.write_text(new, encoding="utf-8")
            print(f"{path.relative_to(ROOT.parent)}: fixed {n} link(s)")
            total += n
    print(f"total fixed: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
