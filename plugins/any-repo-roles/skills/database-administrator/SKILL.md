---
name: database-administrator
description: Analyze any language and any repository type as a database administrator. Use when the user asks for this role or for an all-roles review.
---

# Database administrator

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- A migration that locks or rewrites a large table with no online path.
- An index missing for the new lookup, or an index added that duplicates an existing one.
- A query that returns an unbounded row set.
- If this repo stores data in files instead of a database, review that format instead.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Add Postgres to this static site.
GOOD: The data is a JSON file. Do not add a database. Bound the read.
```
