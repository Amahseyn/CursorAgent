---
name: lua
description: Write and review Lua in any repository that already contains it. Use when the repo has Lua files in a host such as a game, nginx, or an editor config.
---

# Lua

Use this only when the repository already contains Lua. Do not add it, and do not switch the file to another language.

Look for:

- A global where the module next to it uses `local`.
- A 0-based index on a Lua table.
- A library the host runtime in this repo does not already provide.
- A second Lua version than the host this config already targets.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add a LuaRocks dependency the editor build does not ship.
GOOD: Keep the logic local and 1-based, using only the APIs this host already calls.
```
