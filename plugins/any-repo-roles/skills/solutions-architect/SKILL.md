---
name: solutions-architect
description: Analyze any language and any repository type as a solutions architect. Use when the user asks for this role or for an all-roles review.
---

# Solutions architect

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- An integration added for a system this repo does not talk to.
- A new runtime when the current one already fits the constraint.
- A public boundary drawn in the wrong package.
- What this repository is not, stated so the change stays inside it.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Adopt the cloud stack from a different product.
GOOD: Call the queue this service already configures. Do not add a second one.
```
