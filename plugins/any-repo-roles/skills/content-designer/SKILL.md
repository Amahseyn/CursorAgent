---
name: content-designer
description: Analyze any language and any repository type as a content designer. Use when the user asks for this role or for an all-roles review.
---

# Content designer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- An error that names an internal type, code, or stack and not what the person should do.
- Two terms for one object in this repo's UI, CLI, or docs.
- A label that is a verb on one control and a noun on the same action elsewhere.
- Placeholder text that is the only instruction.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Alert the string 'Error: null'.
GOOD: Replace it with the action that failed and the one next step, in the words this product already uses.
```
