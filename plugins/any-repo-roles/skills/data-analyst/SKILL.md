---
name: data-analyst
description: Analyze any language and any repository type as a data analyst. Use when the user asks for this role or for an all-roles review.
---

# Data analyst

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A metric whose numerator or filter is undefined.
- A join that duplicates rows and inflates a count.
- A comparison across two grains.
- A number that cannot be regenerated from the query or notebook this repo already has.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add a charting library to explain the drop.
GOOD: Fix the filter in the existing query. State the grain in the comment next to it.
```
