---
name: spring
description: Write and review Spring in any repository that already contains it. Use when the repo has a Spring application.
---

# Spring

Use this only when the repository already contains Spring. Do not add it, and do not switch the file to another language.

Look for:

- A `new` of a bean the context already provides.
- A transaction boundary that does not match the annotation style on the class above.
- A second configuration style beside Java config or the XML this app already uses.
- A Spring Boot version that does not match the parent pom or Gradle plugin.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Construct the repository with `new` and add a second framework.
GOOD: Inject the bean and keep the transaction annotation the service above uses.
```
