---
name: swift
description: Write and review Swift in any repository that already contains it. Use when the repo has Swift sources, a Package.swift, or an Xcode project.
---

# Swift

Use this only when the repository already contains Swift. Do not add it, and do not switch the file to another language.

Look for:

- A force unwrap on a value the file next to it treats as optional.
- A concurrency style (async, actor, or callback) that does not match this target.
- A second package manager beside Swift Package Manager or the Xcode project already present.
- A public API that skips the access level the rest of the module uses.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Force-unwrap the URL and add CocoaPods.
GOOD: Guard the optional the way the view model next to this one does.
```
