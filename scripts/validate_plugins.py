#!/usr/bin/env python3
"""Check marketplace packs and shared Cursor rule files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".cursor-plugin" / "marketplace.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_RULE_LINES = 500
PREFERRED_RULE_LINES = 50
SKILL_KEYS = {
    "name",
    "description",
    "paths",
    "globs",
    "disable-model-invocation",
    "icon",
    "color",
}
SECRET_RE = re.compile(
    r"(AKIA[0-9A-Z]{16}|sk_live_[0-9A-Za-z]{8,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)
BAD_RE = re.compile(r"\bBAD\b")
GOOD_RE = re.compile(r"\bGOOD\b")

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    text = path.read_text(encoding="utf-8")
    if SECRET_RE.search(text):
        fail(f"{path.relative_to(ROOT)}: looks like it contains a secret")
    lines = text.splitlines()
    if len(lines) > MAX_RULE_LINES:
        fail(f"{path.relative_to(ROOT)}: {len(lines)} lines exceeds {MAX_RULE_LINES}")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)}: frontmatter is not closed")
        return None
    meta: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if ":" not in raw:
            fail(f"{path.relative_to(ROOT)}: bad frontmatter line: {raw}")
            continue
        key, value = raw.split(":", 1)
        meta[key.strip()] = value.strip().strip("'\"")
    return meta


def load_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
        return None
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)}: expected a JSON object")
        return None
    return data


def check_name(label: str, name: object) -> None:
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        fail(
            f"{label}: name must use lowercase letters, numbers, single hyphens, "
            f"or single periods, got {name!r}"
        )


def main() -> int:
    marketplace = load_json(MARKETPLACE)
    if marketplace is None:
        return report()

    check_name("marketplace", marketplace.get("name"))
    owner = marketplace.get("owner")
    if not isinstance(owner, dict) or not owner.get("name"):
        fail("marketplace: owner.name is required")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("marketplace: plugins must be a non-empty list")
        return report()

    seen: set[str] = set()
    for index, entry in enumerate(plugins):
        label = f"plugins[{index}]"
        if not isinstance(entry, dict):
            fail(f"{label}: expected an object")
            continue
        name = entry.get("name")
        check_name(label, name)
        if isinstance(name, str):
            if name in seen:
                fail(f"{label}: duplicate name {name}")
            seen.add(name)
        source = entry.get("source")
        if isinstance(source, dict):
            source = source.get("path")
        if not isinstance(source, str) or not source or source.startswith(("/", "..")) or ".." in Path(source).parts:
            fail(f"{label}: source must be a relative path inside the repo")
            continue
        plugin_dir = ROOT / source
        if not plugin_dir.is_dir():
            fail(f"{name}: source directory does not exist: {source}")
            continue
        if plugin_dir.resolve().parent.resolve() != (ROOT / "plugins").resolve():
            fail(f"{name}: source must be a direct child of plugins/")
        manifest_path = plugin_dir / ".cursor-plugin" / "plugin.json"
        manifest = load_json(manifest_path)
        if manifest is None:
            continue
        check_name(f"{source} plugin.json", manifest.get("name"))
        if manifest.get("name") != name:
            fail(f"{name}: plugin.json name {manifest.get('name')!r} does not match marketplace")
        if Path(source).name != name:
            fail(f"{name}: folder name {Path(source).name!r} does not match plugin name")
        if not manifest.get("description"):
            fail(f"{name}: plugin.json description is required")
        entry_description = entry.get("description")
        if isinstance(entry_description, str) and entry_description != manifest.get("description"):
            fail(f"{name}: marketplace description does not match plugin.json")

        rules_root = plugin_dir / "rules"
        rules = sorted(rules_root.rglob("*.mdc")) if rules_root.is_dir() else []
        stray = [
            path
            for path in (rules_root.rglob("*") if rules_root.is_dir() else [])
            if path.is_file() and path.suffix.lower() in {".md", ".markdown"}
        ]
        for path in stray:
            fail(f"{path.relative_to(ROOT)}: use .mdc so the rule has frontmatter")
        for rule in rules:
            text = rule.read_text(encoding="utf-8")
            line_count = len(text.splitlines())
            if PREFERRED_RULE_LINES < line_count <= MAX_RULE_LINES:
                warn(
                    f"{rule.relative_to(ROOT)}: {line_count} lines; prefer under "
                    f"{PREFERRED_RULE_LINES} (hard limit {MAX_RULE_LINES})"
                )
            meta = parse_frontmatter(rule)
            if meta is None:
                continue
            body = text.split("\n---\n", 1)[-1]
            if not BAD_RE.search(body) or not GOOD_RE.search(body):
                fail(f"{rule.relative_to(ROOT)}: include a BAD example and a GOOD example")
            always = meta.get("alwaysApply", "")
            if always not in {"true", "false"}:
                fail(f"{rule.relative_to(ROOT)}: alwaysApply must be true or false")
            description = meta.get("description", "")
            globs = meta.get("globs", "")
            manual = always == "false" and not description and not globs
            if not description and not manual:
                fail(f"{rule.relative_to(ROOT)}: description is required unless the rule is manual-only")
            unknown = set(meta) - {"description", "alwaysApply", "globs"}
            if unknown:
                fail(f"{rule.relative_to(ROOT)}: unknown frontmatter {sorted(unknown)}")
        skill_count = check_skills(plugin_dir)
        if not rules and skill_count == 0:
            fail(f"{name}: plugins need at least one rules/*.mdc file or skills/<name>/SKILL.md")

    return report()


def check_skills(plugin_dir: Path) -> int:
    skills_root = plugin_dir / "skills"
    if not skills_root.exists():
        return 0
    if not skills_root.is_dir():
        fail(f"{skills_root.relative_to(ROOT)}: skills must be a directory")
        return 0
    count = 0
    for path in sorted(skills_root.rglob("SKILL.md")):
        relative = path.relative_to(skills_root)
        label = path.relative_to(ROOT)
        if len(relative.parts) != 2:
            fail(f"{label}: put SKILL.md in skills/<name>/SKILL.md")
            continue
        folder = relative.parts[0]
        count += 1
        if not SKILL_NAME_RE.fullmatch(folder):
            fail(f"{label}: skill folder must be lowercase kebab-case")
        meta = parse_frontmatter(path)
        if meta is None:
            continue
        if meta.get("name") != folder:
            fail(f"{label}: name {meta.get('name')!r} does not match folder {folder}")
        if not meta.get("description"):
            fail(f"{label}: description is required")
        flag = meta.get("disable-model-invocation")
        if flag is not None and flag not in {"true", "false"}:
            fail(f"{label}: disable-model-invocation must be true or false")
        unknown = set(meta) - SKILL_KEYS
        if unknown:
            fail(f"{label}: unknown frontmatter {sorted(unknown)}")
    return count


def report() -> int:
    for item in warnings:
        print(f"warning: {item}")
    if errors:
        print(f"{len(errors)} problem(s):")
        for item in errors:
            print(f"- {item}")
        return 1
    print("plugin marketplace ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
