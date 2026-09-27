---
name: ocaml
description: Write and review OCaml in any repository that already contains it. Use when the repo has OCaml sources and a dune or opam file.
---

# OCaml

Use this only when the repository already contains OCaml. Do not add it, and do not switch the file to another language.

Look for:

- A partial match the compiler would warn on, silenced instead of handled.
- A mutable ref where the module next to it threads the value.
- A dependency missing from the dune or opam file that already builds this library.
- A build system added beside dune.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Silence the exhaustiveness warning.
GOOD: Handle the new variant in the match, and add the library to the existing dune file.
```
