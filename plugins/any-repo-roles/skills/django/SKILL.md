---
name: django
description: Write and review Django in any repository that already contains it. Use when the repo has a Django project or app.
---

# Django

Use this only when the repository already contains Django. Do not add it, and do not switch the file to another language.

Look for:

- A raw SQL string where the queryset API already expresses the query.
- A setting changed in production config for a local-only need.
- A model migration edited after it shipped, instead of a new migration.
- A second web framework beside Django.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Edit the applied migration and add Flask.
GOOD: Add a new migration and keep the queryset style the manager already uses.
```
