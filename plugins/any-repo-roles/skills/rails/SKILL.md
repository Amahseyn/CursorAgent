---
name: rails
description: Write and review Rails in any repository that already contains it. Use when the repo has a Rails application.
---

# Rails

Use this only when the repository already contains Rails. Do not add it, and do not switch the file to another language.

Look for:

- A skipped strong parameter on a new attribute.
- A callback that hides a write the service object next to it makes explicit.
- A gem that duplicates one the Gemfile already has.
- A migration that changes a shipped migration instead of adding one.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Permit all keys and edit the old migration.
GOOD: Permit the new attribute and add a migration, the way the model above does.
```
