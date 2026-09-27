---
name: perl
description: Write and review Perl in any repository that already contains it. Use when the repo has Perl files or a cpanfile.
---

# Perl

Use this only when the repository already contains Perl. Do not add it, and do not switch the file to another language.

Look for:

- A file with `strict` and `warnings` removed when the others enable them.
- A module version the cpanfile does not already pin.
- A regular expression that interpolates a value.
- A second test harness beside the `t/` layout already here.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Turn off strict so the global works.
GOOD: Declare the lexical and keep `strict` and `warnings`, as the module above does.
```
