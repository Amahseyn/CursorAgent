# CursorAgent Rules

Install a pack in Cursor, then type one command in the project you want reviewed.

The full steps, team install, and the context rules are in [docs/how-to-use.md](docs/how-to-use.md).

## Use it

1. Open **Customize** → **From GitHub Repository**.
2. Paste `https://github.com/Amahseyn/CursorAgent`.
3. Install **Any repo roles**.
4. Open your project and work as usual.

Cloning this repository does not turn the pack on. Cursor installs it from `.cursor-plugin/marketplace.json`.

The default reads the code and calls only the matching role or language, then asks before it adds or modifies a rule. Type `all` when you want every applicable role. Other commands stay out of the chat until you ask for them.

## Add a pack

1. Copy `templates/rule-plugin` to `plugins/<kebab-name>/`.
2. Set `name` in `plugins/<kebab-name>/.cursor-plugin/plugin.json` to that folder name. `displayName` is the label in Customize.
3. One `.mdc` per concern, under 50 lines, with a `BAD` line and a `GOOD` line. Leave `alwaysApply` false unless every installed project must see the rule on every chat.
4. Add `"source": "./plugins/<kebab-name>"` to `.cursor-plugin/marketplace.json`, with the same `description` as `plugin.json`.
5. A pack may auto-load two skills. Set `disable-model-invocation: true` on the rest.
6. Run `python3 scripts/validate_plugins.py`.

Details are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Layout

| Path | Purpose |
| --- | --- |
| `docs/how-to-use.md` | How to install and use a pack |
| `.cursor-plugin/marketplace.json` | Lists every installable pack |
| `plugins/` | Packs other people install |
| `templates/rule-plugin/` | Copy this to start a pack. It is not installable. |
| `scripts/validate_plugins.py` | Checks manifests, frontmatter, and context limits |

## License

MIT. See `LICENSE`. By opening a pull request you agree your rules may be used under that license.
