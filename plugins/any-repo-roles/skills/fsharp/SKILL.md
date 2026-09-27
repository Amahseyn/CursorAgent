---
name: fsharp
description: Write and review F# in any repository that already contains it. Use when the repo has F# sources or an fsproj.
---

# F#

Use this only when the repository already contains F#. Do not add it, and do not switch the file to another language.

Look for:

- A `null` creeping into a file that otherwise uses `option`.
- An object hierarchy where the file next to it is a module of functions.
- A project file style that does not match the fsproj already here.
- A C# rewrite of an F# file that was not asked for.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Return null from the F# function.
GOOD: Return `option` and keep the function in the module the file above uses.
```
