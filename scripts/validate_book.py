#!/usr/bin/env python3
"""Validate tutorial structure, required sections, links and fenced blocks."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
LABS = ROOT / "labs"
APPENDICES = ROOT / "appendices"
TEMPLATES = ROOT / "templates"

CHAPTER_FILES = [
    "ch01-why-projects-fail.md", "ch02-project-basics.md", "ch03-git-safety.md",
    "ch04-intent-and-acceptance.md", "ch05-spec-driven-development.md",
    "ch06-architecture-and-planning.md", "ch07-vertical-slice.md",
    "ch08-small-steps-and-prs.md", "ch09-testing-and-debugging.md",
    "ch10-context-engineering.md", "ch11-ci-release-deploy.md",
    "ch12-issue-driven-maintenance.md", "ch13-change-and-refactoring.md",
    "ch14-legacy-modernization.md", "ch15-data-migration-recovery.md",
    "ch16-long-term-maintenance.md", "ch17-skill-engineering.md",
    "ch18-subagents-and-automation.md", "ch19-platforms-and-tool-migration.md",
    "ch20-capstone.md",
]
LAB_FILES = [
    "lab01-disposable-prototype.md", "lab02-project-blueprint.md",
    "lab03-release-v1.md", "lab04-evolution-v1-1.md",
    "lab05-three-month-maintenance.md",
]
APPENDIX_FILES = ["A-environment.md", "B-command-reference.md", "C-failure-catalog.md", "D-glossary.md", "E-sources.md"]
TEMPLATE_FILES = [
    "intent.md", "spec.md", "plan.md", "tasks.md", "adr.md", "issue.md",
    "bug-report.md", "pr-checklist.md", "release-checklist.md", "runbook.md",
    "handoff.md", "definition-of-done.md",
]
REQUIRED_SECTIONS = [
    "## 1. 本章成果", "## 2. 为什么需要它", "## 3. 最少必备知识",
    "## 4. 起始项目状态", "## 5. 操作步骤与 AI 任务示例",
    "## 6. AI 应生成的产物", "## 7. 人工检查点",
    "## 8. 验收命令与通过标准", "## 9. 常见失败及恢复方法",
    "## 10. 本章 Git 提交", "## 11. 练习与扩展", "## 12. 参考资料",
]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def nonspace_length(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def check_links(path: Path, text: str) -> list[str]:
    problems: list[str] = []
    for raw in LINK_RE.findall(text):
        target = raw.strip().strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        target = unquote(target)
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            problems.append(f"{path.relative_to(ROOT)}: broken link {raw}")
    return problems


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    expected = (
        [(CHAPTERS / name) for name in CHAPTER_FILES]
        + [(LABS / name) for name in LAB_FILES]
        + [(APPENDICES / name) for name in APPENDIX_FILES]
        + [(TEMPLATES / name) for name in TEMPLATE_FILES]
        + [ROOT / "README.md", ROOT / "WRITING_GUIDE.md"]
    )
    for path in expected:
        if not path.is_file():
            errors.append(f"missing: {path.relative_to(ROOT)}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        if len(re.findall(r"^```", text, flags=re.MULTILINE)) % 2:
            errors.append(f"{path.relative_to(ROOT)}: unclosed fenced code block")
        errors.extend(check_links(path, text))
        if path.parent == CHAPTERS:
            for section in REQUIRED_SECTIONS:
                if section not in text:
                    errors.append(f"{path.relative_to(ROOT)}: missing section {section}")
            size = nonspace_length(text)
            if size < 1800:
                warnings.append(f"{path.relative_to(ROOT)}: short chapter ({size} nonspace chars)")
            if "AI 任务" not in text:
                errors.append(f"{path.relative_to(ROOT)}: no AI task example")
            # TODO 仅在作为未完成标记（行首占位）时告警；教学语境中的"写 TODO"提示不视为未完成
            unfinished = [m.group(0) for m in re.finditer(r"(?m)^\s*(?:[-*]\s*)?(?:\[[ ]\]\s*)?(TODO|TBD)\b(?!\(baseline-quirk\))|待补充|待完善", text)]
            if unfinished:
                warnings.append(f"{path.relative_to(ROOT)}: possible unfinished marker")

    chapter_chars = sum(nonspace_length((CHAPTERS / name).read_text(encoding="utf-8")) for name in CHAPTER_FILES if (CHAPTERS / name).is_file())
    print(f"Markdown files: {len(markdown_files)}")
    print(f"Chapters: {sum((CHAPTERS / name).is_file() for name in CHAPTER_FILES)}/20")
    print(f"Labs: {sum((LABS / name).is_file() for name in LAB_FILES)}/5")
    print(f"Chapter nonspace characters: {chapter_chars}")
    for item in warnings:
        print(f"WARN: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    print(f"Result: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
