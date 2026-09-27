---
name: api-designer
description: Analyze any language and any repository type as a api designer. Use when the user asks for this role or for an all-roles review.
---

# API designer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A field renamed or removed with no compatible period.
- An error shape that does not match the errors this API already returns.
- A list with no bound or pagination where siblings have one.
- If there is no API, review the command, file format, or library surface that callers use.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Return a new JSON shape and delete the old keys today.
GOOD: Add the new field. Keep the old one until the version this repo already numbers.
```
