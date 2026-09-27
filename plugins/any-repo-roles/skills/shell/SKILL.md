---
name: shell
description: Write and review shell in any repository that already contains it. Use when the repo has shell scripts or a shebang.
---

# shell

Use this only when the repository already contains shell. Do not add it, and do not switch the file to another language.

Look for:

- An unquoted expansion.
- A bashism in a script whose shebang is `sh`.
- `set -euo pipefail` removed when the other scripts set it.
- A new shell beside the one the existing scripts already use.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Use a bash array in a `#!/bin/sh` script.
GOOD: Quote the expansion and keep the `sh` shebang the other scripts use.
```
