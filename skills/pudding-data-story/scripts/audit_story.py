#!/usr/bin/env python3
"""Audit a visual-story project for common editorial and interaction omissions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".md",
    ".mjs",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
}

META_COPY = {
    "this visualization shows": "Replace production commentary with the finding.",
    "this chart shows": "State the finding, not the chart's existence.",
    "push the data": "Use a concrete action label.",
    "choose a lens": "Name the dimension or comparison.",
    "same group of particles": "Do not expose implementation metaphors to readers.",
    "这里展示": "直接陈述发现，不要复述设计要求。",
    "本图展示": "直接陈述发现，不要复述图表。",
    "推动数据": "把控件改成读者能理解的具体动作。",
    "观察镜头": "说清楚读者正在比较什么。",
    "同一组粒子": "不要向读者暴露实现隐喻。",
}

CHECKS = {
    "reduced motion": re.compile(r"prefers-reduced-motion", re.I),
    "accessible labels": re.compile(r"\baria-(?:label|labelledby|describedby)\b", re.I),
    "sticky scrolly": re.compile(r"position\s*:\s*sticky", re.I),
    "source or methods": re.compile(r"\b(source|sources|method|methodology)\b|来源|方法", re.I),
}

RUNE_PATTERN = re.compile(r"\$(?:state|derived)(?:\.(?:raw|by))?\s*\(", re.I)
PRERENDER_PATTERN = re.compile(r"export\s+const\s+prerender\s*=\s*true\b")


def collect_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() in TEXT_SUFFIXES else []
    return sorted(
        path
        for path in target.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and not any(part in {"node_modules", ".git", "dist", "build", ".next"} for part in path.parts)
    )


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def find_project_file(target: Path, name: str) -> Path | None:
    root = target if target.is_dir() else target.parent
    direct = root / name
    if direct.is_file():
        return direct
    return next(
        (
            path
            for path in root.rglob(name)
            if path.is_file()
            and not any(part in {"node_modules", ".git", "dist", "build", ".next"} for part in path.parts)
        ),
        None,
    )


def dependency_major(version: str) -> int | None:
    match = re.search(r"(?<!\d)(\d+)(?:\.\d+){0,2}", version)
    return int(match.group(1)) if match else None


def strict_stack_issues(target: Path, files: list[Path]) -> list[str]:
    issues: list[str] = []
    package_path = find_project_file(target, "package.json")

    if package_path is None:
        issues.append("package.json was not found.")
        dependencies: dict[str, str] = {}
    else:
        try:
            package = json.loads(read_text(package_path))
        except json.JSONDecodeError:
            issues.append(f"{package_path.name} is not valid JSON.")
            package = {}
        dependencies = {
            **package.get("dependencies", {}),
            **package.get("devDependencies", {}),
        }

    svelte_version = dependencies.get("svelte")
    if not svelte_version:
        issues.append("Svelte is not declared in package.json.")
    else:
        major = dependency_major(str(svelte_version))
        if major is None:
            issues.append(f"Could not verify the Svelte major version from {svelte_version!r}.")
        elif major < 5:
            issues.append(f"Svelte 5 or newer is required; found {svelte_version!r}.")

    if "@sveltejs/kit" not in dependencies:
        issues.append("@sveltejs/kit is not declared in package.json.")
    if "@sveltejs/adapter-static" not in dependencies:
        issues.append("@sveltejs/adapter-static is not declared in package.json.")

    config_path = next(
        (
            path
            for name in ("svelte.config.js", "svelte.config.mjs", "svelte.config.ts")
            if (path := find_project_file(target, name)) is not None
        ),
        None,
    )
    if config_path is None:
        issues.append("A SvelteKit svelte.config file was not found.")
    elif not re.search(r"@sveltejs/adapter-static|adapter\s*\(", read_text(config_path)):
        issues.append("svelte.config does not appear to configure adapter-static.")

    source_files = [path for path in files if path.suffix.lower() != ".md"]
    source_text = "\n".join(read_text(path) for path in source_files)

    if not PRERENDER_PATTERN.search(source_text):
        issues.append("No route-level `export const prerender = true` was found.")

    rune_state_files = [
        path
        for path in source_files
        if path.name.endswith((".svelte.js", ".svelte.ts", ".svelte.mjs"))
        and RUNE_PATTERN.search(read_text(path))
    ]
    if not rune_state_files:
        issues.append("No `.svelte.js` or `.svelte.ts` runes story-state module was found.")

    scrolly_files = [path for path in source_files if path.name.casefold() == "scrolly.svelte"]
    if not scrolly_files:
        issues.append("Scrolly.svelte was not found.")
    elif not any("IntersectionObserver" in read_text(path) for path in scrolly_files):
        issues.append("Scrolly.svelte does not appear to use IntersectionObserver.")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit a data-story source tree for meta-copy and basic experience requirements."
    )
    parser.add_argument("target", type=Path, help="Story file or project directory")
    parser.add_argument(
        "--strict-stack",
        action="store_true",
        help="Require the Svelte 5, SvelteKit static, runes-state, and sticky-scrolly baseline.",
    )
    args = parser.parse_args()

    target = args.target.expanduser().resolve()
    if not target.exists():
        print(f"ERROR: target does not exist: {target}", file=sys.stderr)
        return 2

    files = collect_files(target)
    if not files:
        print("ERROR: no supported text story files found", file=sys.stderr)
        return 2

    combined_parts: list[str] = []
    issues: list[str] = []

    for path in files:
        content = read_text(path)
        combined_parts.append(content)
        lowered = content.casefold()
        for phrase, advice in META_COPY.items():
            if phrase.casefold() in lowered:
                rel = path.relative_to(target) if target.is_dir() else path.name
                issues.append(f"META COPY [{rel}]: {phrase!r}. {advice}")

    combined = "\n".join(combined_parts)
    missing = [label for label, pattern in CHECKS.items() if not pattern.search(combined)]
    stack_issues = strict_stack_issues(target, files) if args.strict_stack else []

    print(f"Audited {len(files)} text file(s).")
    if issues:
        print("\nReader-copy issues:")
        for issue in issues:
            print(f"- {issue}")
    if missing:
        print("\nProject signals not found (review manually):")
        for label in missing:
            print(f"- {label}")
    if stack_issues:
        print("\nStrict Svelte 5 stack requirements not met:")
        for issue in stack_issues:
            print(f"- {issue}")

    if not issues and not missing and not stack_issues:
        print("PASS: no flagged meta-copy and all baseline project signals were found.")
        return 0

    print("\nREVIEW: automated signals are prompts for human QA, not proof of story quality.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
