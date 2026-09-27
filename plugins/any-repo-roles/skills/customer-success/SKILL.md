---
name: customer-success
description: Analyze any language and any repository type as a customer success. Use when the user asks for this role or for an all-roles review.
---

# Customer success

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A change that breaks a workflow an existing customer can already complete.
- A default that silently changes results a customer has saved.
- No note of who is affected and how they move to the new behavior.
- A success metric the product claims that this change makes worse, with no mention.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Remove the old export tonight.
GOOD: Keep the old export. Add the new one and name who should switch.
```
