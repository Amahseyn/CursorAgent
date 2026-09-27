---
name: dart
description: Write and review Dart in any repository that already contains it. Use when the repo has Dart files or a pubspec.yaml.
---

# Dart

Use this only when the repository already contains Dart. Do not add it, and do not switch the file to another language.

Look for:

- A null assertion where the neighboring code uses null-safe flow.
- Flutter widgets added to a Dart package that has no Flutter dependency.
- A package version that fights the pubspec SDK constraint.
- An async gap that uses the value after a `BuildContext` check the file already warns about, when this is Flutter.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add Flutter to this pure Dart library.
GOOD: Keep it a Dart package. Handle the nullable the way the function above does.
```
