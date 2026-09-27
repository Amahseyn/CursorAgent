---
name: sre
description: Analyze any language and any repository type as a site reliability engineer. Use when the user asks for this role or for an all-roles review.
---

# Site reliability engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A new dependency or call with no timeout.
- A failure that does not log or exit in a way an operator can see.
- A change with no rollback if this repo already ships releases.
- Saturation: a queue, pool, or worker count with no limit.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add a Kubernetes cluster so this library can scale.
GOOD: Set a timeout on the call using the same helper the neighboring client uses.
```
