---
name: finish-rule-pack
description: Finish a shared Cursor rule pack in this repository. Use when adding a plugin under plugins/, editing marketplace.json, writing a rule or skill, or running scripts/validate_plugins.py.
---

# Finish a rule pack

Rules and skills for other people belong under `plugins/<name>/`. Files in `.cursor/rules/` apply only while editing this repository.

## Check the index first

Read `catalog/skills.json` before adding a skill. It lists Cursor's built-in skills, skills in `cursor/plugins`, and the Awesome Cursor Skills index. Point to an existing skill when it already covers the job. Do not copy an upstream `SKILL.md` into this repo.

Refresh that index with `python3 scripts/fetch_skill_catalog.py`.

## Add a pack

1. Copy `templates/rule-plugin` to `plugins/<kebab-name>/`.
2. Make the folder name, `plugin.json` `name`, and marketplace `name` match.
3. Use the same `description` in `plugin.json` and `.cursor-plugin/marketplace.json`.
4. Put one concern in each `rules/*.mdc` file. Stay under 50 lines. Include a BAD example and a GOOD example.
5. Add `skills/<name>/SKILL.md` only for an original workflow. The `name` field must match the folder.
6. Run `python3 scripts/validate_plugins.py` and fix every reported problem.
