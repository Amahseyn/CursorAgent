---
name: platform-engineer
description: Analyze any language and any repository type as a platform engineer. Use when the user asks for this role or for an all-roles review.
---

# Platform engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A team-wide default changed with no migration note.
- A paved path bypassed by a one-off script.
- A golden template that no longer matches the service this change copies.
- If this repo is not a platform, review only the shared tooling it does contain.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Give this service its own deploy system.
GOOD: Call the deploy script the template in this repo already documents.
```
