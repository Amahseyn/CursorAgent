---
name: ux-researcher
description: Analyze any language and any repository type as a ux researcher. Use when the user asks for this role or for an all-roles review.
---

# UX researcher

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A flow justified by 'users want' with no evidence in issues, research, or support notes.
- A critical path with no record of anyone having completed it.
- A group excluded by language, ability, device, or account type the product claims to serve.
- A question the change raises that this repo's research does not answer. Say what to ask, and do not invent the answer.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Users love this, so add three more steps.
GOOD: The issue thread shows people fail on the confirm step. Watch that step before adding a new one.
```
