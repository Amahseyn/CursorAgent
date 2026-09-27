---
name: devops-engineer
description: Analyze any language and any repository type as a devops engineer. Use when the user asks for this role or for an all-roles review.
---

# DevOps engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A pipeline step that is not reproducible, or a tool version that is floating.
- A secret printed in CI logs or stored in the workflow file.
- An environment difference between the check and the release build.
- If there is no pipeline, say what command a local check would run, using tools already in the repo.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add a cloud account in the workflow yaml.
GOOD: Pin the image tag the other job already pins. Read the token from the environment.
```
