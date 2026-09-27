---
name: vue
description: Write and review Vue in any repository that already contains it. Use when the repo has Vue single-file components.
---

# Vue

Use this only when the repository already contains Vue. Do not add it, and do not switch the file to another language.

Look for:

- An Options API block in a file whose neighbors use `<script setup>`, or the reverse.
- A state library added beside the store already in this app.
- A template ref used before the component has mounted, against the pattern next to it.
- A Vue major version that does not match package.json.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Mix Options API into a script-setup file and add Pinia beside the existing store.
GOOD: Keep `<script setup>` and the store this app already uses.
```
