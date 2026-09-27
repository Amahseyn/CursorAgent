---
name: performance-engineer
description: Analyze any language and any repository type as a performance engineer. Use when the user asks for this role or for an all-roles review.
---

# Performance engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A hot path that gains a query, copy, or remote call per item.
- A payload or asset larger than what the current view or command needs.
- A cache with no bound.
- A tuning change with no measurement in this repo's existing benchmark or profile.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Rewrite the service in Rust for speed.
GOOD: The loop queries once per row. Load the set the way the batch function above already does.
```
