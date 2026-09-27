---
name: c
description: Write and review C in any repository that already contains it. Use when the repo has C sources and a Makefile, meson, or compiler flags.
---

# C

Use this only when the repository already contains C. Do not add it, and do not switch the file to another language.

Look for:

- An unbounded copy into a fixed buffer.
- An allocation with no free on the path that already owns that pointer.
- A warning flag removed that the existing build turns on.
- A new libc assumption the Makefile does not already compile with.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Use `strcpy` into the stack buffer.
GOOD: Bound the copy and check the length the way the neighboring function does.
```
