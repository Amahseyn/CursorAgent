---
name: csharp
description: "Use when the repo has C# sources or a csproj."
disable-model-invocation: true
---

# C#

## When to use

Use this only when the repository already contains C#. Do not add it, and do not switch the file to another language.

## When not to use

- The repository has no C# surface. Say so in one line and stop.
- The user named a different skill. Do not apply this one beside it.
- The only way to comply would be to add a language, framework, or tool this repository does not already use.

## Instructions

1. Read the file that triggered this skill, then the nearest neighboring file that already does the job well.
2. Name the repository type and the language of the file you are reading.
3. Walk the checks in order. For each hit, record the path and the line. For each miss, record one sentence of evidence.
4. Compare the hit with the neighboring file before you invent a fix.
5. Report findings first, ordered by how many checks they fail.
6. If a finding should persist, propose add or modify. Wait. Write only what the user accepts.

## Checks

- A null forgiveness operator where nullable context is already on.
- A blocking `.Result` on a method whose neighbors are async.
- A second project style beside the SDK-style csproj already in the repo.
- A public API that skips the nullable annotations the assembly already emits.

## How to apply each check

### 1. A null forgiveness operator where nullable context is already on.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 2. A blocking `.Result` on a method whose neighbors are async.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 3. A second project style beside the SDK-style csproj already in the repo.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 4. A public API that skips the nullable annotations the assembly already emits.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

## Report

Use this shape. One block per finding.

```text
Skill: csharp
File: <path>
Check: <the check that failed>
Evidence: <the line you read>
Change: <the edit, using a pattern already in this repo>
```

If nothing failed, the whole report is one line: which files you opened and that this skill found nothing.

## Examples

```text
BAD:  Call `.Result` and add a packages.config.
GOOD: Await the task and keep the nullable annotations the csproj already enables.
```

Walk the BAD line as if it were in the repository:

1. You open the file and see: Call `.Result` and add a packages.config.
2. You open the neighboring file and see the pattern the GOOD line names.
3. You change only the failing part so the result matches: Await the task and keep the nullable annotations the csproj already enables.
4. You do not reformat unrelated code and you do not add a new tool.

## Edge cases

- Several languages are present. Stay inside the files this skill owns.
- A generated file or a vendor directory contains the hit. Report it only if the repository edits that file by hand.
- The same hit is already described in `.cursor/rules/`. Propose modify, not a second rule.
- The user asked for a review only. Do not write a rule until they choose add or modify.

## Saving a rule

After the user accepts, write `.cursor/rules/csharp.mdc` in the project being reviewed, or update the file that already covers this concern.

```text
---
description: C# in this repository follows the pattern already used next to the change
alwaysApply: false
---

# C#

- State the one change.

BAD:  the line you found
GOOD: the line you will commit
```

Keep that rule under 50 lines. Leave `alwaysApply` false. Keep the description under 200 characters.

## Guidelines

- Match the formatter, package layout, and test tool already in the repo.
- A saved rule is one concern, under 50 lines, with `alwaysApply: false` and a description under 200 characters.
