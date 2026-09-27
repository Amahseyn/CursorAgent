---
name: git-merge-conflict
description: "Use when the repo has conflict markers or a merge or rebase in progress."
disable-model-invocation: true
---

# Git merge conflict

## When to use

Use this only when the repository already has this workflow. Do not add a second tool for it.

## When not to use

- The repository has no Git merge conflict surface. Say so in one line and stop.
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

- Keeping both sides without reading what each side changed.
- Deleting a test or a migration to make the conflict disappear.
- Resolving by taking 'ours' or 'theirs' for the whole file when only a few lines clash.
- Continuing a rebase or merge that the user did not start.

## How to apply each check

### 1. Keeping both sides without reading what each side changed.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 2. Deleting a test or a migration to make the conflict disappear.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 3. Resolving by taking 'ours' or 'theirs' for the whole file when only a few lines clash.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 4. Continuing a rebase or merge that the user did not start.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

## Report

Use this shape. One block per finding.

```text
Skill: git-merge-conflict
File: <path>
Check: <the check that failed>
Evidence: <the line you read>
Change: <the edit, using a pattern already in this repo>
```

If nothing failed, the whole report is one line: which files you opened and that this skill found nothing.

## Examples

```text
BAD:  Delete the incoming tests so the file is clean.
GOOD: Keep both behaviors, and run the tests this repo already has.
```

Walk the BAD line as if it were in the repository:

1. You open the file and see: Delete the incoming tests so the file is clean.
2. You open the neighboring file and see the pattern the GOOD line names.
3. You change only the failing part so the result matches: Keep both behaviors, and run the tests this repo already has.
4. You do not reformat unrelated code and you do not add a new tool.

## Edge cases

- Several languages are present. Stay inside the files this skill owns.
- A generated file or a vendor directory contains the hit. Report it only if the repository edits that file by hand.
- The same hit is already described in `.cursor/rules/`. Propose modify, not a second rule.
- The user asked for a review only. Do not write a rule until they choose add or modify.

## Saving a rule

After the user accepts, write `.cursor/rules/git-merge-conflict.mdc` in the project being reviewed, or update the file that already covers this concern.

```text
---
description: Git merge conflict in this repository follows the pattern already used next to the change
alwaysApply: false
---

# Git merge conflict

- State the one change.

BAD:  the line you found
GOOD: the line you will commit
```

Keep that rule under 50 lines. Leave `alwaysApply` false. Keep the description under 200 characters.

## Guidelines

- Match the commands and templates already in the repo. Ask before adding or modifying a rule.
- A saved rule is one concern, under 50 lines, with `alwaysApply: false` and a description under 200 characters.
