# Contributing

Publish rules other Cursor users can install. One pack is one folder under `plugins/`. One rule file is one concern.

## Before you write

- The rule should change the agent's behavior in projects that are not this one.
- It should be specific enough to follow without guessing. "Write clean code" is not a rule.
- It must be safe to install in a stranger's repository. No private paths, hostnames, customer names, or credentials.
- Do not include exploit steps, malware, or other operational attack content.

## Add a pack

```bash
cp -R templates/rule-plugin plugins/my-pack
```

Then:

1. Rename the folder to lowercase kebab-case. The folder name, `plugin.json` `name`, and the marketplace `name` must match.
2. Write the description for a person choosing the pack in Customize.
3. Put the author name you want shown publicly in `author.name`.
4. Add the pack to `.cursor-plugin/marketplace.json`:

```json
{
  "name": "my-pack",
  "source": "./plugins/my-pack",
  "description": "Same description as plugin.json",
  "version": "0.1.0",
  "license": "MIT",
  "keywords": ["cursor-rules"],
  "category": "rules"
}
```

5. Validate:

```bash
python3 scripts/validate_plugins.py
```

## Rule file

Path: `plugins/<name>/rules/<concern>.mdc`

```markdown
---
description: When this rule is relevant, in one sentence
globs: "**/*.py"
alwaysApply: false
---

# Title

- Do this.
- Do not do that.

Include a fenced example with a BAD line and a GOOD line.
```

- Prefer under 50 lines. The hard limit is 500. The validator warns above 50 and fails above 500.
- Keep the `description` under 200 characters. Cursor uses that sentence to decide whether to load the file.
- Leave `alwaysApply` false unless every project that installs the pack must see the rule on every chat. The validator warns when it is true.
- Do not set `alwaysApply: true` together with `globs`. Cursor ignores `globs` in that case.
- A pack may auto-load two skills. Set `disable-model-invocation: true` on every other skill so they load only from `/skill-name` or when another skill opens the file.
- The marketplace `description` must match `plugin.json`.
- `description` is required unless the rule is manual-only (`alwaysApply: false` and no `globs`).
- `globs` is a quoted string. Separate patterns with commas: `"**/*.ts,**/*.tsx"`.
- `alwaysApply: true` ignores `globs` and `description`. Use it rarely.
- A plain `.md` file in `rules/` is not a Cursor rule for project use. This repo still rejects it so every shared rule has frontmatter.

## Skill file

Path: `plugins/<name>/skills/<skill>/SKILL.md`

- `name` in the frontmatter matches the folder.
- `description` says what the skill does and when to use it.
- Write the skill for this pack. `catalog/skills.json` lists skills that already exist elsewhere; do not copy those files.

## Review checklist

- [ ] Pack name is unique, kebab-case, and matches the folder.
- [ ] Marketplace entry `source` points at the pack folder.
- [ ] Marketplace `description` matches `plugin.json`.
- [ ] Each rule has one concern, a BAD example, and a GOOD example.
- [ ] `alwaysApply: true` is justified for unknown projects.
- [ ] No secrets, tokens, or private URLs.
- [ ] `python3 scripts/validate_plugins.py` passes.

## License

This repository is MIT. A pull request licenses your contribution under `LICENSE`.
