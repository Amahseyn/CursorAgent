---
name: scala
description: Write and review Scala in any repository that already contains it. Use when the repo has Scala sources or an sbt or Mill build.
---

# Scala

Use this only when the repository already contains Scala. Do not add it, and do not switch the file to another language.

Look for:

- A `null` or thrown exception where this codebase uses `Option` or `Either`.
- A mutable collection where the neighboring code uses the immutable one.
- A build tool added beside sbt or Mill, whichever is already here.
- A Scala version that does not match `scalaVersion` in the build.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Throw a null and add a second build tool.
GOOD: Return `Either` the way the service next to this one does, on the Scala version the build already pins.
```
