---
name: review-shared-rule
description: Review a Cursor rule that other people will install. Use when a shared rule pack is being written or edited.
disable-model-invocation: true
---

# Review a shared rule

1. Keep the rule to one concern.
2. Prefer under 50 lines.
3. Include a BAD example and a GOOD example.
4. Leave out private paths, hostnames, customer names, and credentials.
5. Set `alwaysApply: true` only when the rule is safe in a project you have never seen.

```text
BAD:  alwaysApply: true on a rule that names one company's paths
GOOD: alwaysApply: false with a description the agent can match
```
