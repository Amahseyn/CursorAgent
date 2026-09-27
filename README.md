# CursorAgent Rules

Cursor rules written by Cursor users, for other Cursor users to install.

A rule in this repository is not a note inside one project. It is a plugin. After you push this repo to GitHub, another person can add the marketplace in Cursor and install a pack. The rules then show up in Customize next to their other rules.

Cursor does not import loose `.mdc` files from a GitHub URL. The marketplace manifest at `.cursor-plugin/marketplace.json` is what makes a repository installable. Each pack lives in its own folder:

```text
plugins/your-pack/
  .cursor-plugin/plugin.json
  rules/your-rule.mdc
  skills/your-skill/SKILL.md
  README.md
```

## Install a pack

The GitHub repository has to be pushed first. This folder on your machine is not visible to other people until then.

1. In Cursor, open Customize.
2. Add this repository from GitHub (`https://github.com/Amahseyn/CursorAgent`). Cursor looks for `.cursor-plugin/marketplace.json`.
3. Install a plugin, for example `any-repo-roles` or `example-rule-pack`.

Team and Enterprise workspaces can add the same repository as a team marketplace. Installing a plugin is per user unless an admin assigns it.

`any-repo-roles` reviews any repository as senior security, product design, and the other roles that review a software change, in the language that repository already uses. `example-rule-pack` is only a format sample.

## Add a rule for other people

1. Copy `templates/rule-plugin` to `plugins/<kebab-name>/`.
2. Set `name` in `.cursor-plugin/plugin.json` to that same folder name.
3. Replace the sample rule. One concern per file. Stay under 50 lines. Include a bad example and a good example.
4. Add an entry to `.cursor-plugin/marketplace.json` with `"source": "plugins/<kebab-name>"`.
5. Run `python3 scripts/validate_plugins.py`.
6. Open a pull request. Contributions are MIT licensed.

Pick one apply mode in the frontmatter:

| You want | Frontmatter |
| --- | --- |
| Agent decides from the description | `alwaysApply: false`, a `description`, no `globs` |
| Only when certain files are open | `alwaysApply: false`, `globs`, and a `description` |
| Every chat in every project that installs the pack | `alwaysApply: true` |
| Only when someone @-mentions the rule | `alwaysApply: false`, and omit both `description` and `globs` |

Use `alwaysApply: true` only when the rule is safe in projects you have never seen.

Rules under `.cursor/rules/` apply while someone is editing *this* repository. They are not what other people install.

## Layout

| Path | Purpose |
| --- | --- |
| `.cursor-plugin/marketplace.json` | Lists every installable pack |
| `plugins/` | Packs other people can install. A pack can include `rules/*.mdc` and `skills/<name>/SKILL.md` |
| `templates/rule-plugin/` | Copy this to start a pack. It is not installable. |
| `.cursor/rules/` | Instructions for agents working in this repo |
| `catalog/skills.json` | Downloaded index of public Cursor skills. Names and source links only |
| `scripts/validate_plugins.py` | Checks names, manifests, rule frontmatter, and skills |
| `scripts/fetch_skill_catalog.py` | Refreshes `catalog/skills.json` from the public sources |

## License

MIT. See `LICENSE`. By opening a pull request you agree your rules may be used under that license.
