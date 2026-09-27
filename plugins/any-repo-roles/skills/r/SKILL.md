---
name: r
description: Write and review R in any repository that already contains it. Use when the repo has R files, a DESCRIPTION, or an renv lock.
---

# R

Use this only when the repository already contains R. Do not add it, and do not switch the file to another language.

Look for:

- A loop where the package next to it already vectorizes.
- A package loaded that renv or DESCRIPTION does not already record.
- A working-directory side effect in a function the package exports.
- A tidyverse rewrite of a base-R file, or the reverse, against the file's neighbors.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Call `setwd` inside the exported function.
GOOD: Take the path as an argument and use the same dplyr or base style the file above uses.
```
