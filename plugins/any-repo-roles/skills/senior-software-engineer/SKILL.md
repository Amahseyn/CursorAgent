---
name: senior-software-engineer
description: Analyze any language and any repository type as a senior software engineer. Use when the user asks for this role or for an all-roles review.
---

# Senior software engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A behavior change with no failure path.
- An edge case the surrounding code already handles and this change ignores.
- A wide edit where a local one would do.
- A new abstraction used once.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Refactor the whole module while fixing the null.
GOOD: Guard the null the same way the caller above already does.
```
