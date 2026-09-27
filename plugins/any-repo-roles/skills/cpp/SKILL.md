---
name: cpp
description: Write and review C++ in any repository that already contains it. Use when the repo has C++ sources and a CMake or other C++ build.
---

# C++

Use this only when the repository already contains C++. Do not add it, and do not switch the file to another language.

Look for:

- A naked `new` or `delete` where the file next to it uses RAII.
- A standard version newer than the `CMAKE_CXX_STANDARD` already set.
- An exception or error-code policy that fights the one this library uses.
- A header that includes more than the includes beside it.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Set the standard to C++26 and manage the pointer by hand.
GOOD: Store the resource in the same RAII type the class above uses, on the standard CMake already sets.
```
