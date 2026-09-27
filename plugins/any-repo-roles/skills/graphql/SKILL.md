---
name: graphql
description: Write and review GraphQL in any repository that already contains it. Use when the repo has GraphQL schemas or operations.
---

# GraphQL

Use this only when the repository already contains GraphQL. Do not add it, and do not switch the file to another language.

Look for:

- A field removed that existing operations in this repo still select.
- A list with no limit where the other fields paginate.
- A resolver error shape that does not match the errors this schema already returns.
- A second schema file that drifts from the one the server already loads.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Delete the field the client query still asks for.
GOOD: Deprecate the field and keep the selection the checked-in operation already uses.
```
