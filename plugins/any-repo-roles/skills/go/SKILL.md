---
name: go
description: Write and review Go in any repository that already contains it. Use when the repo has Go files or a go.mod.
---

# Go

Use this only when the repository already contains Go. Do not add it, and do not switch the file to another language.

Look for:

- An error string that drops the wrapped error, or a panic used as control flow.
- A `context.Context` missing on a call whose neighbors take one.
- An export or package name that breaks the layout `go.mod` already uses.
- A formatter or helper other than `gofmt` when the repo has no other formatter.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add a Java-style exception hierarchy.
GOOD: Return `fmt.Errorf("...: %w", err)` the way the caller above already wraps errors.
```
