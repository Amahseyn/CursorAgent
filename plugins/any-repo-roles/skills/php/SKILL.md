---
name: php
description: Write and review PHP in any repository that already contains it. Use when the repo has PHP files or a composer.json.
---

# PHP

Use this only when the repository already contains PHP. Do not add it, and do not switch the file to another language.

Look for:

- A SQL or shell string built by concatenation.
- A type or property style older than the PHP version composer.json requires.
- A framework bootstrap in a library that has no framework.
- An autoload path outside the PSR layout composer.json already maps.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Interpolate the request into the SQL.
GOOD: Bind the parameter with the database API this project already uses, on the PHP version composer requires.
```
