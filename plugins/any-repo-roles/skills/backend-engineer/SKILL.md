---
name: backend-engineer
description: Analyze any language and any repository type as a backend engineer. Use when the user asks for this role or for an all-roles review.
---

# Backend engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A write that is not idempotent where retries are possible.
- A contract change with no version or compatible reader.
- A migration that drops or rewrites data with no backfill.
- If there is no service, review the persistence or file format this repo does have.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add a microservice in front of this library.
GOOD: The library writes a JSON file. Bump the format version and keep the old reader.
```
