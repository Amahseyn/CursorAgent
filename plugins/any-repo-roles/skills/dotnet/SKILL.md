---
name: dotnet
description: Write and review .NET in any repository that already contains it. Use when the repo has a .NET solution or project.
---

# .NET

Use this only when the repository already contains .NET. Do not add it, and do not switch the file to another language.

Look for:

- A package version that fights `Directory.Packages.props` or the csproj already here.
- A new exe or class library in a folder the solution does not include.
- A nullable or implicit-usings setting that fights the Directory.Build.props already set.
- A second target framework beside the ones the project already multi-targets, unless the change is that target.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add a packages.config and a new target framework on one project.
GOOD: Add the PackageReference the way the csproj next to it does, and include the project in the solution.
```
