---
name: zig
description: Write and review Zig in any repository that already contains it. Use when the repo has Zig sources or a build.zig.
---

# Zig

Use this only when the repository already contains Zig. Do not add it, and do not switch the file to another language.

Look for:

- An allocator hidden inside a library function instead of passed in.
- An `undefined` or unchecked slice where the caller already passes a length.
- A build step that ignores the `build.zig` already in the repo.
- A panic on a path the library can return as an error.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Allocate with a global and panic on a short buffer.
GOOD: Take the allocator the caller already has, and return the error union the function above returns.
```
