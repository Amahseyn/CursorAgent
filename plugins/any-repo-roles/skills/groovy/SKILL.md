---
name: groovy
description: Write and review Groovy in any repository that already contains it. Use when the repo has Groovy sources or a Gradle build that uses Groovy.
---

# Groovy

Use this only when the repository already contains Groovy. Do not add it, and do not switch the file to another language.

Look for:

- A dynamic call where the file next to it is `@CompileStatic`.
- A Gradle task written in a new Kotlin DSL file when the build is Groovy, or the reverse.
- A dependency version that fights the version catalog already in the build.
- A Java rewrite that was not asked for.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add a second build.gradle.kts beside the Groovy build.
GOOD: Keep the Groovy build. Use the version catalog the other tasks already use.
```
