---
name: accessibility-specialist
description: Analyze any language and any repository type as a accessibility specialist. Use when the user asks for this role or for an all-roles review.
---

# Accessibility specialist

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A control with no accessible name in the UI, CLI help, or API error.
- Keyboard or focus order that skips the action, or a screen that traps focus.
- Meaning carried only by color.
- A time limit, motion, or audio path with no alternative the codebase already allows.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  The div onclick is fine because it looks like a button.
GOOD: Use the button component this repo already has, with its name set from the visible label.
```
