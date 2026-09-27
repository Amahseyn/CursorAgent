---
name: python
description: Write and review Python in any repository that already contains it. Use when the repo has Python files, pyproject.toml, requirements.txt, or a Pipfile.
---

# Python

Use this only when the repository already contains Python. Do not add it, and do not switch the file to another language.

Look for:

- A bare `except` or an exception that drops the original error.
- A type the neighboring modules already annotate, left untyped on the new function.
- A path built with string concat instead of the path style this repo uses.
- A new installer or layout beside the one `pyproject.toml` or `requirements` already declares.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add a Node script to format the Python package.
GOOD: Raise the typed error the module next to this one uses, and pass the original as the cause.
```
