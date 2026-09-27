---
name: svelte
description: Write and review Svelte in any repository that already contains it. Use when the repo has Svelte components.
---

# Svelte

Use this only when the repository already contains Svelte. Do not add it, and do not switch the file to another language.

Look for:

- A store added beside the rune or store style this app already uses.
- A DOM write in a component whose neighbors bind state.
- A SvelteKit route in a library that is not SvelteKit.
- A major version that does not match package.json.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add SvelteKit routes inside this component library.
GOOD: Keep the component. Use the same `$state` or store the component above uses.
```
