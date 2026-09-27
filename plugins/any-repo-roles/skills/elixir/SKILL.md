---
name: elixir
description: Write and review Elixir in any repository that already contains it. Use when the repo has Elixir files or a mix.exs.
---

# Elixir

Use this only when the repository already contains Elixir. Do not add it, and do not switch the file to another language.

Look for:

- A bang function whose caller does not expect a raise, where a non-bang exists.
- A process started outside the supervision tree this application already defines.
- A dependency the mix.exs and lock do not already share.
- A `with` or case style that fights the function above it.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Start a bare `GenServer` from the request.
GOOD: Add the child to the supervisor this application already starts.
```
