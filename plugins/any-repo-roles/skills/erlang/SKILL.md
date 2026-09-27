---
name: erlang
description: Write and review Erlang in any repository that already contains it. Use when the repo has Erlang sources or an erlang.mk, rebar, or mix Erlang app.
---

# Erlang

Use this only when the repository already contains Erlang. Do not add it, and do not switch the file to another language.

Look for:

- A catch-all that turns a crash into `ok`.
- A process that is not in the supervision tree already defined.
- An OTP behavior implemented halfway when the module next to it uses the behavior.
- A build tool added beside rebar or erlang.mk, whichever is present.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Catch `_` and return ok.
GOOD: Let it crash into the supervisor this app already runs.
```
