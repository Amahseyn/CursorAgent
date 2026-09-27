---
name: csharp
description: Write and review C# in any repository that already contains it. Use when the repo has C# sources or a csproj.
---

# C#

Use this only when the repository already contains C#. Do not add it, and do not switch the file to another language.

Look for:

- A null forgiveness operator where nullable context is already on.
- A blocking `.Result` on a method whose neighbors are async.
- A second project style beside the SDK-style csproj already in the repo.
- A public API that skips the nullable annotations the assembly already emits.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Call `.Result` and add a packages.config.
GOOD: Await the task and keep the nullable annotations the csproj already enables.
```
