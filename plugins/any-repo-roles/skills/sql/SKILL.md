---
name: sql
description: Write and review SQL in any repository that already contains it. Use when the repo has SQL files, a migration directory, or queries in the host language.
---

# SQL

Use this only when the repository already contains SQL. Do not add it, and do not switch the file to another language.

Look for:

- A value concatenated into a query.
- A dialect feature the migrations do not already use.
- A migration that rewrites data with no down path, when this repo's migrations have down paths.
- A second migration tool beside the one already in the repo.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Build the query with string format.
GOOD: Bind the parameter in the dialect the existing migration already uses.
```
