---
name: compliance-reviewer
description: Analyze any language and any repository type as a compliance reviewer. Use when the user asks for this role or for an all-roles review.
---

# Compliance reviewer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A license, notice, or required header missing on new third-party code.
- An audit event the domain claims to record, with no write in this change.
- A control described in docs that the code does not enforce.
- Production data used in a sample, fixture, or test.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Copy the dataset into the repo so tests are realistic.
GOOD: Use the synthetic fixture that is already checked in. Do not add customer records.
```
