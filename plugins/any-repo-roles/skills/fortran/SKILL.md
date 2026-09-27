---
name: fortran
description: Write and review Fortran in any repository that already contains it. Use when the repo has Fortran sources and a build that compiles them.
---

# Fortran

Use this only when the repository already contains Fortran. Do not add it, and do not switch the file to another language.

Look for:

- An implicit variable the module does not already allow.
- A common block added where the file above uses a module.
- A compiler standard newer than the flags already in the build.
- An array assumed-size where the interface already passes bounds.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Turn implicit typing back on.
GOOD: Use the module and the standard flag the Makefile already passes.
```
