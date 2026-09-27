---
name: embedded-engineer
description: Analyze any language and any repository type as a embedded engineer. Use when the user asks for this role or for an all-roles review.
---

# Embedded engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- Unbounded allocation or recursion on a target with a fixed memory budget.
- A hardware register or pin used with no comment tying it to the board this repo documents.
- An interrupt path that shares state without the protection the rest of the firmware uses.
- If this is not embedded, say so and stop.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Pull in an operating system scheduler for this firmware loop.
GOOD: Keep the loop. Bound the buffer the same way the existing driver does.
```
