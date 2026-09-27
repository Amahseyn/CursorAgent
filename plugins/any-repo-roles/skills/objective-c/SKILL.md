---
name: objective-c
description: Write and review Objective-C in any repository that already contains it. Use when the repo has Objective-C sources in an Apple or GNUstep project.
---

# Objective-C

Use this only when the repository already contains Objective-C. Do not add it, and do not switch the file to another language.

Look for:

- A manual retain or release under ARC, which this project already uses.
- A nullability annotation missing on a header the module already annotates.
- A delegate property that is not weak, when the other delegates are weak.
- A Swift rewrite of an Objective-C file that was not asked for.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Rewrite the class in Swift and drop ARC.
GOOD: Keep the `.m` file. Mark the delegate weak and the header nullable, as the class beside it does.
```
