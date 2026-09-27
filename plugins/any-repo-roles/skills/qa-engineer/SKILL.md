---
name: qa-engineer
description: Analyze any language and any repository type as a qa engineer. Use when the user asks for this role or for an all-roles review.
---

# QA engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A behavior change with no test, or a test that cannot fail.
- A branch, flag, or error state the tests never enter.
- A check that depends on time, order, or the network with no control.
- Use the test tool this repo already has.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Snapshot the whole UI to prove a one-line fix.
GOOD: Add one test beside the existing cases that fails if the bug returns.
```
