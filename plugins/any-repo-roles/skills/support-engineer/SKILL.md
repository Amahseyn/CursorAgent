---
name: support-engineer
description: Analyze any language and any repository type as a support engineer. Use when the user asks for this role or for an all-roles review.
---

# Support engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A failure the user cannot identify from the message, code, or log line.
- No request id, version, or input echo they can send you.
- A known bad state with no documented recovery.
- A debug step that requires a tool the user does not have.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Tell them to attach a core dump.
GOOD: Include the version and the error code this CLI already prints, and the one recovery step.
```
