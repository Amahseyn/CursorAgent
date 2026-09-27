# Agent instructions

This repository is a marketplace of Cursor rules. Other Cursor users install a pack from here. They do not clone this repo to receive the rules.

- Put rules for other people in `plugins/<name>/rules/*.mdc`.
- Put an original skill in `plugins/<name>/skills/<skill>/SKILL.md`. Do not copy an upstream skill file.
- Read `catalog/skills.json` before adding a skill. Refresh it with `python3 scripts/fetch_skill_catalog.py`.
- Register every pack in `.cursor-plugin/marketplace.json`.
- Keep each rule to one concern, under 50 lines, with a BAD example and a GOOD example. Leave `alwaysApply` false unless every installed project needs it on every chat.
- Let at most two skills in a pack load on their own. Set `disable-model-invocation: true` on the rest.
- Leave `.cursor/rules/` for instructions about working in this repository.
- Run `python3 scripts/validate_plugins.py` before finishing a pack.

Follow `CONTRIBUTING.md` when adding or changing a pack.
