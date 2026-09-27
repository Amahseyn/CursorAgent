---
name: javascript
description: Write and review JavaScript in any repository that already contains it. Use when the repo has JavaScript files and no request to migrate them.
---

# JavaScript

Use this only when the repository already contains JavaScript. Do not add it, and do not switch the file to another language.

Look for:

- A silent conversion of this package to TypeScript.
- A module style (`import` or `require`) that fights the package.json `type` field.
- A callback or promise style that does not match the file next to this one.
- A lint rule disabled instead of the pattern the existing eslint config asks for.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Rename the file to `.ts` and add a tsconfig.
GOOD: Keep the CommonJS export this package.json already declares.
```
