---
name: powershell
description: Write and review PowerShell in any repository that already contains it. Use when the repo has PowerShell files or a module manifest.
---

# PowerShell

Use this only when the repository already contains PowerShell. Do not add it, and do not switch the file to another language.

Look for:

- An approved-verb violation when this module already uses approved verbs.
- `$ErrorActionPreference` changed for the whole session.
- A string command built for `Invoke-Expression`.
- A cmdlet style that does not match the `.psm1` already here.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Invoke-Expression on the argument.
GOOD: Call the cmdlet and set `-ErrorAction` on that call only.
```
