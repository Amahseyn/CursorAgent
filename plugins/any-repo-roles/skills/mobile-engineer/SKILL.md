---
name: mobile-engineer
description: Analyze any language and any repository type as a mobile engineer. Use when the user asks for this role or for an all-roles review.
---

# Mobile engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A permission requested before the feature that needs it.
- A path that assumes the network is always up.
- Platform-specific code with no equivalent on the other platform this repo supports.
- If this is not a mobile repo, say so and review the client surface it does have.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add SwiftUI to this Python package.
GOOD: This repo has no mobile target. Review the CLI session instead of inventing an app.
```
