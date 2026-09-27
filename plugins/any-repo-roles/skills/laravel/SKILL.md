---
name: laravel
description: Write and review Laravel in any repository that already contains it. Use when the repo has a Laravel application.
---

# Laravel

Use this only when the repository already contains Laravel. Do not add it, and do not switch the file to another language.

Look for:

- A raw query where the eloquent model already has the relation.
- A secret in `.env` committed, or a config read with `env()` outside config files.
- A controller that skips the form request the neighboring controller uses.
- A Laravel major version that does not match composer.json.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Call `env()` in the controller and commit `.env`.
GOOD: Read the config key and validate with a form request, as the controller next to this one does.
```
