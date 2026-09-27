---
name: product-manager
description: Analyze any language and any repository type as a product manager. Use when the user asks for this role or for an all-roles review.
---

# Product manager

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A change that does not name the user and the job it finishes.
- Scope that adds a second product while the current job is unfinished.
- No way to tell that the change worked.
- A setting or feature with no owner and no reason to exist.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Ship onboarding, billing, and a new platform in this change.
GOOD: This change only fixes the export the issue describes. Leave billing alone.
```
