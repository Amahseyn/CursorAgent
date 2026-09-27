---
name: frontend-engineer
description: Analyze any language and any repository type as a frontend engineer. Use when the user asks for this role or for an all-roles review.
---

# Frontend engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- Client state that duplicates the server state this repo already stores.
- A request waterfall or a payload that ships data the view does not render.
- An interaction that loses input on refresh or error.
- If there is no UI, review the user-facing surface that does exist and say there is no frontend.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add a React context for a Go CLI.
GOOD: There is no UI. Review the command's flags and stdout instead.
```
