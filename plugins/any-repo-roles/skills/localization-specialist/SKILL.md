---
name: localization-specialist
description: Analyze any language and any repository type as a localization specialist. Use when the user asks for this role or for an all-roles review.
---

# Localization specialist

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A user-facing string concatenated from fragments that cannot be translated.
- A format that assumes one language's date, plural, or sort order.
- A string added outside the catalog this repo already uses for copy.
- If the repo is single-language on purpose, say so and still avoid building sentences in code.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Show 'You have ' + n + ' items'.
GOOD: Use the message catalog this repo already has, with a placeholder for the count.
```
