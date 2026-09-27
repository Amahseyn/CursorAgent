---
name: staff-engineer
description: Analyze any language and any repository type as a staff engineer. Use when the user asks for this role or for an all-roles review.
---

# Staff engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A boundary moved without a reason recorded in the change.
- A one-way migration, schema, or public API with no way back.
- Coupling that forces an unrelated package to release with this one.
- An operability gap: no log, metric, or exit code when this fails.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Import the service into the library so it can call the database.
GOOD: Keep the library pure. Pass the result in from the service that already owns the database.
```
