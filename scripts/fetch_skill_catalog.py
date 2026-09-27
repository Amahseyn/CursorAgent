#!/usr/bin/env python3
"""Download skill indexes used to see what this marketplace should not duplicate.

Writes names, summaries, and source URLs. It does not copy SKILL.md bodies.
"""

from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "catalog" / "skills.json"
TREE_URL = "https://api.github.com/repos/cursor/plugins/git/trees/HEAD?recursive=1"
MARKET_URL = "https://raw.githubusercontent.com/cursor/plugins/HEAD/.cursor-plugin/marketplace.json"
AWESOME_URL = "https://raw.githubusercontent.com/spencerpauly/awesome-cursor-skills/main/README.md"

BUILTIN = [
    ("automate", "Creates Cursor Automations from schedules, Slack, GitHub, and other triggers."),
    ("autopilot", "Keeps a pull request merge-ready by handling feedback, conflicts, and failing checks."),
    ("canvas", "Creates interactive React artifacts beside the chat."),
    ("create-hook", "Creates Cursor hooks and hooks.json entries."),
    ("create-rule", "Creates Cursor rules with the right scope."),
    ("create-skill", "Creates Agent Skills and SKILL.md files."),
    ("create-subagent", "Creates a custom subagent with a focused role."),
    ("cursor-blame", "Investigates AI-authored changes and the prompts behind them."),
    ("loop", "Runs a prompt or skill on an interval."),
    ("migrate-to-skills", "Converts eligible dynamic rules and slash commands into skills."),
    ("review", "Selects and runs a code-review agent."),
    ("review-bugbot", "Reviews changes for likely bugs with Bugbot."),
    ("review-security", "Reviews changes for security issues."),
    ("sdk", "Builds apps and automations on the Cursor SDK."),
    ("shell", "Runs the given text as a shell command."),
    ("split-to-prs", "Splits a large change into smaller pull requests."),
    ("statusline", "Configures the Cursor CLI status line."),
    ("update-cli-config", "Updates Cursor CLI settings in ~/.cursor/cli-config.json."),
    ("update-cursor-settings", "Finds and updates a Cursor or VS Code setting."),
]


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "CursorAgent-catalog"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode()


def awesome_skills(text: str) -> list[dict[str, str]]:
    collecting = False
    section = ""
    found: list[dict[str, str]] = []
    for line in text.splitlines():
        if line.startswith("## Plugins"):
            break
        if line.strip() == "## Skills":
            collecting = True
            continue
        if not collecting:
            continue
        if line.startswith("### "):
            section = line[4:].strip()
            continue
        match = re.match(r"- \[`?([^`\]]+)`?\]\(([^)]+)\) - (.+)$", line)
        if not match:
            continue
        link = match.group(2)
        if link.startswith(("http://", "https://")):
            url = link
        else:
            url = "https://github.com/spencerpauly/awesome-cursor-skills/blob/main/" + link.lstrip("./")
        found.append(
            {
                "name": match.group(1),
                "section": section,
                "summary": match.group(3).strip(),
                "url": url,
                "list": "https://github.com/spencerpauly/awesome-cursor-skills",
                "license": "CC0-1.0",
            }
        )
    return found


def cursor_plugins(tree: dict, marketplace: dict) -> list[dict[str, str]]:
    descriptions = {
        entry.get("name"): entry.get("description", "")
        for entry in marketplace.get("plugins", [])
        if isinstance(entry, dict)
    }
    skills: list[dict[str, str]] = []
    for item in tree.get("tree", []):
        path = item.get("path", "")
        if not path.endswith("/SKILL.md"):
            continue
        parts = path.split("/")
        if "skills" not in parts:
            continue
        skill_at = parts.index("skills")
        if skill_at + 1 >= len(parts) - 1:
            continue
        plugin = parts[0]
        skill = parts[skill_at + 1]
        skills.append(
            {
                "plugin": plugin,
                "pluginDescription": descriptions.get(plugin, ""),
                "name": skill,
                "path": path,
                "url": f"https://github.com/cursor/plugins/blob/HEAD/{path}",
            }
        )
    return skills


def main() -> None:
    marketplace = json.loads(fetch(MARKET_URL))
    tree = json.loads(fetch(TREE_URL))
    awesome = awesome_skills(fetch(AWESOME_URL))
    plugins = cursor_plugins(tree, marketplace)
    catalog = {
        "note": "Index only. Skill instructions stay in the upstream repository under that repository's license.",
        "sources": {
            "cursorDocs": "https://cursor.com/docs/skills",
            "cursorPlugins": "https://github.com/cursor/plugins",
            "awesomeCursorSkills": "https://github.com/spencerpauly/awesome-cursor-skills",
            "skillsDirectory": "https://skills.sh",
        },
        "builtin": [
            {"name": name, "invoke": f"/{name}", "summary": summary, "source": "https://cursor.com/docs/skills"}
            for name, summary in BUILTIN
        ],
        "cursorPlugins": plugins,
        "awesomeCursorSkills": awesome,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {OUT.relative_to(ROOT)} "
        f"({len(catalog['builtin'])} builtin, {len(plugins)} cursor plugins, {len(awesome)} awesome)"
    )


if __name__ == "__main__":
    main()
