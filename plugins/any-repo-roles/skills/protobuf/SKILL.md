---
name: protobuf
description: Write and review Protocol Buffers in any repository that already contains it. Use when the repo has proto files or a codegen config.
---

# Protocol Buffers

Use this only when the repository already contains Protocol Buffers. Do not add it, and do not switch the file to another language.

Look for:

- A field number reused or a field renamed in place.
- A required-style break of an existing message.
- A codegen plugin the repo does not already run.
- A JSON mapping that fights the options the proto already sets.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Reuse field number 3 for the new type.
GOOD: Add a new field number and keep the generator the Makefile already runs.
```
