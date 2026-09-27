---
name: rust
description: Write and review Rust in any repository that already contains it. Use when the repo has Rust files, Cargo.toml, or a workspace member.
---

# Rust

Use this only when the repository already contains Rust. Do not add it, and do not switch the file to another language.

Look for:

- `unwrap` or `expect` in a library path whose crate already returns `Result`.
- A clone that hides a borrow the function could take.
- An edition, crate, or feature the workspace Cargo.toml does not already allow.
- Unsafe with no invariant stated next to the block.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add `.unwrap()` so the example compiles.
GOOD: Return the `Result` and use `?` the way the function above does.
```
