---
name: data-engineer
description: Analyze any language and any repository type as a data engineer. Use when the user asks for this role or for an all-roles review.
---

# Data engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A schema change with no backfill and no reader for the old shape.
- A job that appends duplicates when it is rerun.
- A column or field whose grain is undocumented.
- If there is no pipeline, say so. Do not add a warehouse.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Load production tables into the notebook.
GOOD: The checked-in sample already has the columns. Point the job at that sample.
```
