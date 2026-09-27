---
name: typescript
description: Write and review TypeScript in any repository that already contains it. Use when the repo has TypeScript files or a tsconfig.
---

# TypeScript

Use this only when the repository already contains TypeScript. Do not add it, and do not switch the file to another language.

Look for:

- `any` where the surrounding code uses `unknown` and a narrowing check.
- A thrown string, or a catch that ignores the error type this repo already defined.
- A module syntax that does not match the `tsconfig` already in the repo.
- A compile target or strict flag weaker than the config that already passes.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Set `strict` to false so the file compiles.
GOOD: Type the catch as `unknown` and branch the way the neighboring file does.
```
