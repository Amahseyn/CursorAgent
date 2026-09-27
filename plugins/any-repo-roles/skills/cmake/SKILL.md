---
name: cmake
description: Write and review CMake in any repository that already contains it. Use when the repo has CMakeLists or a toolchain file.
---

# CMake

Use this only when the repository already contains CMake. Do not add it, and do not switch the file to another language.

Look for:

- A glob of sources where the lists already name files.
- A minimum version lower than the `cmake_minimum_required` already set.
- A compiler flag that drops a warning the existing targets enable.
- A second build system beside CMake.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  File(GLOB) the sources and add a Makefile.
GOOD: Add the new file to the existing target, and keep the minimum version already declared.
```
