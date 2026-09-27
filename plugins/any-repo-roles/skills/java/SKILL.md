---
name: java
description: Write and review Java in any repository that already contains it. Use when the repo has Java sources or a Maven or Gradle build.
---

# Java

Use this only when the repository already contains Java. Do not add it, and do not switch the file to another language.

Look for:

- A checked exception swallowed, or a new runtime exception type the module does not use.
- A null return where the neighboring method uses the repo's existing optional style.
- A build file added beside the Maven or Gradle file that already builds this module.
- A language level older or newer than the `maven.compiler` or toolchain already set.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Introduce Kotlin for this one class.
GOOD: Throw the exception type the package already declares, and keep the Gradle build.
```
