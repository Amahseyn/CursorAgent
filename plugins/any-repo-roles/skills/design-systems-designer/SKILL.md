---
name: design-systems-designer
description: Analyze any language and any repository type as a design systems designer. Use when the user asks for this role or for an all-roles review.
---

# Design systems designer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A one-off color, space, or type value where this repo already has a token or component.
- A control missing the states the existing components implement.
- A new pattern that duplicates a component already in the repo.
- If this repo has no design system, say so. Do not invent one in the same change.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Create a new button style beside the existing Button.
GOOD: Use the Button this repo already ships, including its disabled state.
```
