---
name: engineering-manager
description: Analyze any language and any repository type as a engineering manager. Use when the user asks for this role or for an all-roles review.
---

# Engineering manager

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A change so large that one review cannot check it.
- Ownership unclear: the code moves to a place no owner is named.
- On-call impact with no note of how failure looks.
- A date met by cutting the failure path.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Split nothing; land the rewrite and the feature together.
GOOD: Land the fix. Leave the rewrite in its own change so the owner can review it.
```
