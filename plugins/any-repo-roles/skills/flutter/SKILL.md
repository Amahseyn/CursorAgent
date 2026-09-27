---
name: flutter
description: Write and review Flutter in any repository that already contains it. Use when the repo has a Flutter app or package.
---

# Flutter

Use this only when the repository already contains Flutter. Do not add it, and do not switch the file to another language.

Look for:

- A `BuildContext` used across an async gap the analyzer already flags.
- A widget rebuilt from a `setState` that the file above handles with the existing state approach.
- A plugin the pubspec does not already allow for this SDK.
- Platform code changed with no Dart API the app already calls.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Use the context after the await.
GOOD: Check `mounted` the way the widget above does, and keep the pubspec SDK constraint.
```
