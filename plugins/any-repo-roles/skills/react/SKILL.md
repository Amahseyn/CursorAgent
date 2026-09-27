---
name: react
description: Write and review React in any repository that already contains it. Use when the repo has React components in this repository.
---

# React

Use this only when the repository already contains React. Do not add it, and do not switch the file to another language.

Look for:

- A new state store beside the one this app already uses.
- An effect that copies props into state.
- A UI library added for one control the repo already has.
- A class component in a file whose neighbors are functions, or the reverse.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Install a second component library for one button.
GOOD: Use the button and the state style the component next to this one uses.
```
