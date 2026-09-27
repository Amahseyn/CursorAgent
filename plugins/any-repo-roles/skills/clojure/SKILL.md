---
name: clojure
description: Write and review Clojure in any repository that already contains it. Use when the repo has Clojure sources and a deps.edn, project.clj, or shadow-cljs config.
---

# Clojure

Use this only when the repository already contains Clojure. Do not add it, and do not switch the file to another language.

Look for:

- A `nil` return where the namespace uses a map of known keys.
- A side effect in a function whose neighbors are pure.
- A build tool added beside the deps file already here.
- A Java interop call where a Clojure function in the repo already wraps it.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Add Leiningen beside deps.edn for one namespace.
GOOD: Use the wrapper this repo already has, and keep deps.edn.
```
