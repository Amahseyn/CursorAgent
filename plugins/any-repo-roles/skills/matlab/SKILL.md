---
name: matlab
description: Write and review MATLAB in any repository that already contains it. Use when the repo has MATLAB files or a toolbox package.
---

# MATLAB

Use this only when the repository already contains MATLAB. Do not add it, and do not switch the file to another language.

Look for:

- A script that depends on the current folder when the function above takes a path.
- A toolbox function the repo does not already depend on.
- A loop the file next to it already writes as an array operation.
- A `.mat` file of real captured data added to the repo.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Save the lab recording into the repository.
GOOD: Take the path as an argument and use the toolbox the package already lists.
```
