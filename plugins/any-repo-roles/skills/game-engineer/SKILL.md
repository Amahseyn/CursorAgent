---
name: game-engineer
description: Analyze any language and any repository type as a game engineer. Use when the user asks for this role or for an all-roles review.
---

# Game engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- Work on the frame path that allocates or waits on IO.
- Simulation that depends on frame time where the rest of the game is fixed-step.
- Content referenced by a path that the pipeline does not pack.
- If this is not a game, say so and stop.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add a web frontend to the simulation crate.
GOOD: The sim is fixed-step. Do not read wall-clock time inside the tick.
```
