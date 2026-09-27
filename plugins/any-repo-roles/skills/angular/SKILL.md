---
name: angular
description: Write and review Angular in any repository that already contains it. Use when the repo has Angular modules or standalone components.
---

# Angular

Use this only when the repository already contains Angular. Do not add it, and do not switch the file to another language.

Look for:

- A new module style that fights standalone or NgModule, whichever this app uses.
- A subscribe with no teardown where the file above uses the `async` pipe or `takeUntilDestroyed`.
- A second UI library beside the one already imported.
- A version bump of Angular that was not asked for.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Subscribe in `ngOnInit` and never unsubscribe.
GOOD: Use the `async` pipe or the teardown the component next to this one uses.
```
