---
name: technical-writer
description: Analyze any language and any repository type as a technical writer. Use when the user asks for this role or for an all-roles review.
---

# Technical writer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A command in the docs that does not match the command in the repo.
- A setup step that skips the failure the tool actually prints.
- A new flag or file with no mention where this repo keeps its docs.
- Docs that describe a stack this repository does not contain.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Document the Docker flow for a repo that has no Dockerfile.
GOOD: Update the existing guide so the command matches the script in this repo.
```
