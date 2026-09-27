---
name: kotlin
description: Write and review Kotlin in any repository that already contains it. Use when the repo has Kotlin sources or a Kotlin build plugin.
---

# Kotlin

Use this only when the repository already contains Kotlin. Do not add it, and do not switch the file to another language.

Look for:

- A platform type left unchecked where the file next to it null-checks.
- A blocking call inside a coroutine the module already marks suspend.
- A Java-only rewrite of a Kotlin file, or a new Kotlin file in a Java-only module.
- A coroutine library the Gradle build does not already depend on.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add `!!` on the platform type.
GOOD: Return a nullable and handle it the way the caller in this module does.
```
