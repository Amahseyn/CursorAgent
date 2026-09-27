---
name: nix
description: Write and review Nix in any repository that already contains it. Use when the repo has Nix files or a flake.
---

# Nix

Use this only when the repository already contains Nix. Do not add it, and do not switch the file to another language.

Look for:

- An unpinned channel when the flake already pins inputs.
- A second package manager wrapped around a build the flake already runs.
- An impurity (`builtins.currentTime`, an unlocked fetch) the other derivations avoid.
- A nixpkgs version that does not match the flake input.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Fetch master and call apt inside the derivation.
GOOD: Add the package to the flake input this repo already pins.
```
