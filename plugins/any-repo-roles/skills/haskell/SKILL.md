---
name: haskell
description: Write and review Haskell in any repository that already contains it. Use when the repo has Haskell sources and a cabal or stack file.
---

# Haskell

Use this only when the repository already contains Haskell. Do not add it, and do not switch the file to another language.

Look for:

- Partial functions (`head`, `fromJust`) where the module uses `Maybe`.
- An effect style (IO, a transformer, or polysemy-style) the module does not already use.
- A GHC extension the cabal file does not already enable.
- A second build tool beside cabal or stack, whichever is here.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Call `fromJust` and add Stack beside Cabal.
GOOD: Return `Maybe` and keep the extensions the cabal file already lists.
```
