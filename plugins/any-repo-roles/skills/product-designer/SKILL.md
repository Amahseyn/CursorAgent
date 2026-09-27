---
name: product-designer
description: Analyze any language and any repository type as a product designer. Use when the user asks for this role or for an all-roles review.
---

# Product designer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A task the user cannot finish, or a step with no next action.
- Missing empty, loading, error, and success states on the surface this repo actually has (screen, CLI, email, or API message).
- A destructive action with no preview or undo.
- Two labels for the same object, or a control whose name does not match what it does.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add a dashboard in React.
GOOD: The CLI exits 1 with no message. Print what failed and the one command that retries it.
```
