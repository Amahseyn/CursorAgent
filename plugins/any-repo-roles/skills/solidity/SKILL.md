---
name: solidity
description: Write and review Solidity in any repository that already contains it. Use when the repo has Solidity files or a foundry, hardhat, or truffle config.
---

# Solidity

Use this only when the repository already contains Solidity. Do not add it, and do not switch the file to another language.

Look for:

- A compiler pragma wider than the version the config already pins.
- An external call before the state update the neighboring contract finishes first.
- A privileged function with no access check the other functions have.
- A new framework beside Foundry or Hardhat, whichever is already here.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Leave the pragma as `^0.4.0` and call out before updating state.
GOOD: Pin the compiler the foundry or hardhat config already pins, and update state before the external call.
```
