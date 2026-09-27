---
name: julia
description: Write and review Julia in any repository that already contains it. Use when the repo has Julia sources or a Project.toml.
---

# Julia

Use this only when the repository already contains Julia. Do not add it, and do not switch the file to another language.

Look for:

- A type-unstable field on a hot struct the package already annotates.
- A package added to the global environment instead of Project.toml.
- A `cd` or write into a package function.
- A script layout that fights the `src/Name.jl` package already here.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Install the package into the global environment.
GOOD: Add it to Project.toml and keep the type annotation the struct above uses.
```
