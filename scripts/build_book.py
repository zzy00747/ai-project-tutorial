#!/usr/bin/env python3
"""Build a single Markdown edition from the tutorial source files."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "AI-项目实战-完整教程.md"

ORDER = [
    "chapters/ch01-why-projects-fail.md",
    "labs/lab01-disposable-prototype.md",
    "chapters/ch02-project-basics.md",
    "chapters/ch03-git-safety.md",
    "chapters/ch04-intent-and-acceptance.md",
    "chapters/ch05-spec-driven-development.md",
    "chapters/ch06-architecture-and-planning.md",
    "labs/lab02-project-blueprint.md",
    "chapters/ch07-vertical-slice.md",
    "chapters/ch08-small-steps-and-prs.md",
    "chapters/ch09-testing-and-debugging.md",
    "chapters/ch10-context-engineering.md",
    "chapters/ch11-ci-release-deploy.md",
    "labs/lab03-release-v1.md",
    "chapters/ch12-issue-driven-maintenance.md",
    "chapters/ch13-change-and-refactoring.md",
    "chapters/ch14-legacy-modernization.md",
    "chapters/ch15-data-migration-recovery.md",
    "chapters/ch16-long-term-maintenance.md",
    "labs/lab04-evolution-v1-1.md",
    "labs/lab05-three-month-maintenance.md",
    "chapters/ch17-skill-engineering.md",
    "chapters/ch18-subagents-and-automation.md",
    "chapters/ch19-platforms-and-tool-migration.md",
    "chapters/ch20-capstone.md",
    "appendices/A-environment.md",
    "appendices/B-command-reference.md",
    "appendices/C-failure-catalog.md",
    "appendices/D-glossary.md",
    "appendices/E-sources.md",
]
TEMPLATES = [
    "intent.md", "spec.md", "plan.md", "tasks.md", "adr.md", "issue.md",
    "bug-report.md", "pr-checklist.md", "release-checklist.md", "runbook.md",
    "handoff.md", "definition-of-done.md",
]


def main() -> None:
    missing = [name for name in ORDER if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit("Missing files:\n" + "\n".join(missing))
    parts = [(ROOT / "README.md").read_text(encoding="utf-8").strip()]
    parts.extend((ROOT / name).read_text(encoding="utf-8").strip() for name in ORDER)
    parts.append("# 附录 F：可复制模板原文")
    parts.extend((ROOT / "templates" / name).read_text(encoding="utf-8").strip() for name in TEMPLATES)
    header = "<!-- 本文件由 scripts/build_book.py 生成，请修改源章节后重新构建。 -->\n\n"
    OUTPUT.write_text(header + "\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT.name}: {OUTPUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
