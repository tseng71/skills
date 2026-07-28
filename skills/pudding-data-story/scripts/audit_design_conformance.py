#!/usr/bin/env python3
"""Validate completeness of design-contract conformance evidence."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


VALID_STATUSES = {"pass", "approved-deviation", "fail", "blocked"}
PASSING_STATUSES = {"pass", "approved-deviation"}
SCREENSHOT_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
REQUIREMENT_FIELDS = {
    "copy",
    "visual_entities",
    "encodings",
    "annotations",
    "controls",
    "motion",
    "reduced_motion",
}


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"file does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"top-level JSON value must be an object: {path}")
    return value


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def unique_ids(items: Any, label: str, issues: list[str]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    if not isinstance(items, list) or not items:
        issues.append(f"{label} must be a non-empty list.")
        return indexed
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            issues.append(f"{label}[{index}] must be an object.")
            continue
        item_id = item.get("id")
        if not nonempty_string(item_id):
            issues.append(f"{label}[{index}].id must be a non-empty string.")
            continue
        if item_id in indexed:
            issues.append(f"{label} contains duplicate id {item_id!r}.")
            continue
        indexed[item_id] = item
    return indexed


def resolve_project_reference(root: Path, value: Any) -> tuple[Path | None, str | None]:
    if not nonempty_string(value):
        return None, "reference must be a non-empty relative path."
    path_value = value.split("#", 1)[0]
    candidate = Path(path_value)
    if candidate.is_absolute():
        return None, "reference must be relative to the project root."
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        return None, "reference escapes the project root."
    if not resolved.is_file():
        return None, f"referenced file does not exist: {candidate}."
    return resolved, None


def validate_contract(contract: dict[str, Any], root: Path) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    list[str],
]:
    issues: list[str] = []
    if contract.get("schema_version") != 1:
        issues.append("contract.schema_version must equal 1.")
    if not nonempty_string(contract.get("design_version")):
        issues.append("contract.design_version must be a non-empty string.")
    sources = contract.get("design_sources")
    if not isinstance(sources, list) or not sources or not all(nonempty_string(value) for value in sources):
        issues.append("contract.design_sources must contain at least one non-empty path.")
    else:
        for source in sources:
            _, source_issue = resolve_project_reference(root, source)
            if source_issue:
                issues.append(f"contract.design_sources: {source_issue}")

    viewports = unique_ids(contract.get("viewports"), "contract.viewports", issues)
    for viewport_id, viewport in viewports.items():
        for dimension in ("width", "height"):
            value = viewport.get(dimension)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                issues.append(f"viewport {viewport_id!r} needs a positive integer {dimension}.")
        if not isinstance(viewport.get("reduced_motion"), bool):
            issues.append(f"viewport {viewport_id!r}.reduced_motion must be boolean.")

    scenes = unique_ids(contract.get("scenes"), "contract.scenes", issues)
    for scene_id, scene in scenes.items():
        for field in ("design_source", "route"):
            if not nonempty_string(scene.get(field)):
                issues.append(f"scene {scene_id!r}.{field} must be a non-empty string.")
        if nonempty_string(scene.get("design_source")):
            _, source_issue = resolve_project_reference(root, scene["design_source"])
            if source_issue:
                issues.append(f"scene {scene_id!r}.design_source: {source_issue}")

        trigger = scene.get("trigger")
        if not isinstance(trigger, dict) or not nonempty_string(trigger.get("kind")):
            issues.append(f"scene {scene_id!r}.trigger must contain a non-empty kind.")

        required_viewports = scene.get("required_viewports")
        if not isinstance(required_viewports, list) or not required_viewports:
            issues.append(f"scene {scene_id!r}.required_viewports must be a non-empty list.")
        else:
            for viewport_id in required_viewports:
                if viewport_id not in viewports:
                    issues.append(
                        f"scene {scene_id!r} references unknown viewport {viewport_id!r}."
                    )

        requirements = scene.get("requirements")
        if not isinstance(requirements, dict):
            issues.append(f"scene {scene_id!r}.requirements must be an object.")
        else:
            missing_fields = sorted(REQUIREMENT_FIELDS - requirements.keys())
            if missing_fields:
                issues.append(
                    f"scene {scene_id!r}.requirements is missing: {', '.join(missing_fields)}."
                )
            for field in ("copy", "visual_entities", "encodings", "annotations", "controls"):
                if field in requirements and not isinstance(requirements[field], list):
                    issues.append(f"scene {scene_id!r}.requirements.{field} must be a list.")
            for field in ("motion", "reduced_motion"):
                if field in requirements and not nonempty_string(requirements[field]):
                    issues.append(
                        f"scene {scene_id!r}.requirements.{field} must be a non-empty string."
                    )

        assertions = unique_ids(scene.get("assertions"), f"scene {scene_id!r}.assertions", issues)
        for assertion_id, assertion in assertions.items():
            if not nonempty_string(assertion.get("kind")):
                issues.append(
                    f"scene {scene_id!r} assertion {assertion_id!r}.kind must be non-empty."
                )

    return viewports, scenes, issues


def resolve_screenshot(root: Path, value: Any) -> tuple[Path | None, str | None]:
    if not nonempty_string(value):
        return None, "screenshot must be a non-empty relative path."
    candidate = Path(value)
    if candidate.is_absolute():
        return None, "screenshot path must be relative to the project root."
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        return None, "screenshot path escapes the project root."
    if resolved.suffix.casefold() not in SCREENSHOT_SUFFIXES:
        return None, f"screenshot must use one of {sorted(SCREENSHOT_SUFFIXES)}."
    if not resolved.is_file() or resolved.stat().st_size <= 0:
        return None, f"screenshot file is missing or empty: {candidate}."
    return resolved, None


def check_result_status(
    status: Any,
    approval_ref: Any,
    context: str,
    issues: list[str],
) -> None:
    if status not in VALID_STATUSES:
        issues.append(f"{context} has invalid status {status!r}.")
        return
    if status not in PASSING_STATUSES:
        issues.append(f"{context} is {status!r}.")
    if status == "approved-deviation" and not nonempty_string(approval_ref):
        issues.append(f"{context} needs a non-empty approval_ref.")


def validate_report(
    contract: dict[str, Any],
    report: dict[str, Any],
    root: Path,
    viewports: dict[str, dict[str, Any]],
    scenes: dict[str, dict[str, Any]],
) -> list[str]:
    issues: list[str] = []
    if report.get("schema_version") != 1:
        issues.append("report.schema_version must equal 1.")
    if report.get("design_version") != contract.get("design_version"):
        issues.append("report.design_version does not match the frozen contract.")
    for field in ("implementation_version", "target_url"):
        if not nonempty_string(report.get(field)):
            issues.append(f"report.{field} must be a non-empty string.")
    if not isinstance(report.get("iterations"), list):
        issues.append("report.iterations must be a list.")

    raw_results = report.get("results")
    if not isinstance(raw_results, list):
        issues.append("report.results must be a list.")
        raw_results = []

    results: dict[tuple[str, str], dict[str, Any]] = {}
    for index, result in enumerate(raw_results):
        if not isinstance(result, dict):
            issues.append(f"report.results[{index}] must be an object.")
            continue
        scene_id = result.get("scene_id")
        viewport_id = result.get("viewport_id")
        key = (scene_id, viewport_id)
        if scene_id not in scenes:
            issues.append(f"result {index} references unknown scene {scene_id!r}.")
            continue
        if viewport_id not in viewports:
            issues.append(f"result {index} references unknown viewport {viewport_id!r}.")
            continue
        if key in results:
            issues.append(f"duplicate result for scene/viewport {scene_id!r}/{viewport_id!r}.")
            continue
        results[key] = result

        _, screenshot_issue = resolve_screenshot(root, result.get("screenshot"))
        if screenshot_issue:
            issues.append(f"{scene_id}/{viewport_id}: {screenshot_issue}")

        raw_contracted_assertions = scenes[scene_id].get("assertions")
        if not isinstance(raw_contracted_assertions, list):
            raw_contracted_assertions = []
        contracted_assertions = {
            item["id"]: item
            for item in raw_contracted_assertions
            if isinstance(item, dict) and nonempty_string(item.get("id"))
        }
        result_assertions = result.get("assertions")
        if not isinstance(result_assertions, list):
            issues.append(f"{scene_id}/{viewport_id}.assertions must be a list.")
            result_assertions = []

        seen_assertions: set[str] = set()
        for assertion in result_assertions:
            if not isinstance(assertion, dict):
                issues.append(f"{scene_id}/{viewport_id} contains a non-object assertion result.")
                continue
            assertion_id = assertion.get("id")
            context = f"{scene_id}/{viewport_id} assertion {assertion_id!r}"
            if assertion_id not in contracted_assertions:
                issues.append(f"{context} is not in the contract.")
                continue
            if assertion_id in seen_assertions:
                issues.append(f"{context} appears more than once.")
                continue
            seen_assertions.add(assertion_id)
            if not nonempty_string(assertion.get("evidence")):
                issues.append(f"{context} needs non-empty evidence.")
            check_result_status(
                assertion.get("status"),
                assertion.get("approval_ref"),
                context,
                issues,
            )

        missing_assertions = sorted(contracted_assertions.keys() - seen_assertions)
        if missing_assertions:
            issues.append(
                f"{scene_id}/{viewport_id} is missing assertion results: "
                f"{', '.join(missing_assertions)}."
            )

        visual_review = result.get("visual_review")
        if not isinstance(visual_review, dict):
            issues.append(f"{scene_id}/{viewport_id}.visual_review must be an object.")
        else:
            context = f"{scene_id}/{viewport_id} visual review"
            if not nonempty_string(visual_review.get("evidence")):
                issues.append(f"{context} needs non-empty evidence.")
            check_result_status(
                visual_review.get("status"),
                visual_review.get("approval_ref"),
                context,
                issues,
            )

    expected = {
        (scene_id, viewport_id)
        for scene_id, scene in scenes.items()
        for viewport_id in (
            scene.get("required_viewports")
            if isinstance(scene.get("required_viewports"), list)
            else []
        )
        if viewport_id in viewports
    }
    missing_results = sorted(expected - results.keys())
    for scene_id, viewport_id in missing_results:
        issues.append(f"missing result for scene/viewport {scene_id!r}/{viewport_id!r}.")

    extra_results = sorted(results.keys() - expected)
    for scene_id, viewport_id in extra_results:
        issues.append(f"uncontracted result for scene/viewport {scene_id!r}/{viewport_id!r}.")

    summary = report.get("summary")
    if not isinstance(summary, dict):
        issues.append("report.summary must be an object.")
    else:
        if summary.get("status") != "pass":
            issues.append("report.summary.status must equal 'pass'.")
        if summary.get("unresolved") != 0:
            issues.append("report.summary.unresolved must equal 0.")
        if summary.get("blocked") != 0:
            issues.append("report.summary.blocked must equal 0.")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a Pudding story's frozen design contract and conformance evidence."
    )
    parser.add_argument("contract", type=Path, help="Path to design-contract.json")
    parser.add_argument("report", type=Path, help="Path to design-conformance.json")
    parser.add_argument(
        "--root",
        type=Path,
        required=True,
        help="Project root used to resolve screenshot paths",
    )
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: project root does not exist: {root}", file=sys.stderr)
        return 2

    try:
        contract = read_json(args.contract.expanduser().resolve())
        report = read_json(args.report.expanduser().resolve())
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    viewports, scenes, issues = validate_contract(contract, root)
    issues.extend(validate_report(contract, report, root, viewports, scenes))

    if issues:
        print("FAIL: design conformance evidence is incomplete or unresolved.")
        for issue in issues:
            print(f"- {issue}")
        return 1

    expected_count = sum(len(scene["required_viewports"]) for scene in scenes.values())
    print(
        "PASS: "
        f"{len(scenes)} scene(s), {expected_count} scene/viewport result(s), "
        "all assertions and visual reviews resolved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
