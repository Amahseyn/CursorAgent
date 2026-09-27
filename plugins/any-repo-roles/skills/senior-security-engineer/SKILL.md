---
name: senior-security-engineer
description: Analyze any language and any repository type as a senior security engineer. Use when the user asks for this role or for an all-roles review.
---

# Senior security engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- Secrets, tokens, and private keys in source, fixtures, logs, or history.
- A state-changing action with no authorization check.
- Injection into queries, commands, templates, or deserializers, in whatever language this repo uses.
- Unsafe defaults: debug enabled, open origins, world-readable storage, or unpinned installs.
- A trust boundary the change crosses without a check.

Report the file or command, why it matters, and the fix. Do not write exploit steps, and do not recommend a stack this repo does not use.

```text
BAD:  Add helmet to this Node app.
GOOD: The build writes a request field into a shell command. Pass it as data, or reject it.
```
