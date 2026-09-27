---
name: route-from-code
description: "Use when reading or changing code in the open project. This mode is the default."
icon: git-branch
color: cyan
---

# Route from the code

## When to use

This is the default mode. Use it on every task in a project that installs this pack.

## Instructions

1. Read the tree, manifests, and the files in the change before you name a skill.
2. Open only the matches below, one `SKILL.md` at a time.
3. Say which skill you will open and the file that triggered it. Do not open the rest.
4. List proposed rules as add or modify, then ask. Wait. Write only what the user accepts under `.cursor/rules/` in the project being reviewed.

## Routing

| What you read | Open |
| --- | --- |
| Secrets, auth, or permissions | `/senior-security-engineer` |
| Personal data in logs or storage | `/privacy-engineer` |
| Screens, CLI output, or error states | `/product-designer` |
| User-facing copy | `/content-designer` |
| Tests or untested branches | `/qa-engineer` |
| CI, Docker, or deploy scripts | `/devops-engineer` |
| Timeouts, health, or rollback | `/sre` |
| SQL or migrations | `/database-administrator` and `/sql` |
| HTTP or RPC contracts | `/api-designer` |
| A language manifest or source file | that language's skill, such as `/python` or `/rust` |
| A commit or commit message | `/git-commit` |
| A branch or worktree | `/git-branch` |
| A pull request | `/git-pull-request` |
| Conflict markers | `/git-merge-conflict` |
| Log, blame, revert, or undo | `/git-history` |
| A Dockerfile or Compose file | `/docker` |
| A bug or stack trace | `/debugging` |
| A lockfile or dependency bump | `/dependencies` |
| Config or `.env` | `/configuration` |
| Log calls | `/logging` |
| A feature flag | `/feature-flags` |
| A queue, worker, or cron | `/background-jobs` |
| A cache | `/caching` |
| Several packages in one repo | `/monorepo` |
| A formatter or linter config | `/formatting` |
| A catch or returned error | `/error-handling` |

## Worked pass

The user says "look at this change" and the diff touches `src/app.py` plus `Dockerfile`.

1. Read both files and the manifest. The repository is a Python service.
2. Open `/python` because `src/app.py` is Python. Open `/docker` because a Dockerfile is in the change. Leave `/rust`, `/product-designer`, and the other skills closed.
3. Apply each opened skill's checks. Quote the line that failed.
4. Propose:
   - Add `.cursor/rules/python.mdc` if that concern is not saved yet.
   - Modify `.cursor/rules/docker.mdc` if a Docker rule already exists.
5. Stop. Wait for add, modify, or skip. Write only the accepted file.

## Guidelines

- Open one skill at a time. Do not load the rest into context.
- Do not write a rule until the user chooses add, modify, or skip.
- A saved rule stays under 50 lines with `alwaysApply: false`.
