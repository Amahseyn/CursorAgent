---
name: senior-security-engineer
description: "Use when the user asks for this role or for an all-roles review."
disable-model-invocation: true
---

# Senior security engineer

## When to use

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

## When not to use

- The repository has no Senior security engineer surface. Say so in one line and stop.
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

- Secrets, tokens, and private keys in source, fixtures, logs, or history.
- A state-changing action with no authorization check.
- Injection into queries, commands, templates, or deserializers, in whatever language this repo uses.
- Unsafe defaults: debug enabled, open origins, world-readable storage, or unpinned installs.
- A trust boundary the change crosses without a check.

## How to apply each check

### 1. Secrets, tokens, and private keys in source, fixtures, logs, or history.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 2. A state-changing action with no authorization check.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 3. Injection into queries, commands, templates, or deserializers, in whatever language this repo uses.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 4. Unsafe defaults: debug enabled, open origins, world-readable storage, or unpinned installs.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 5. A trust boundary the change crosses without a check.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

## Report

Use this shape. One block per finding.

```text
Skill: senior-security-engineer
File: <path>
Check: <the check that failed>
Evidence: <the line you read>
Change: <the edit, using a pattern already in this repo>
```

If nothing failed, the whole report is one line: which files you opened and that this skill found nothing.

## Examples

```text
BAD:  Add helmet to this Node app.
GOOD: The build writes a request field into a shell command. Pass it as data, or reject it.
```

Walk the BAD line as if it were in the repository:

1. You open the file and see: Add helmet to this Node app.
2. You open the neighboring file and see the pattern the GOOD line names.
3. You change only the failing part so the result matches: The build writes a request field into a shell command. Pass it as data, or reject it.
4. You do not reformat unrelated code and you do not add a new tool.

## Edge cases

- Several languages are present. Stay inside the files this skill owns.
- A generated file or a vendor directory contains the hit. Report it only if the repository edits that file by hand.
- The same hit is already described in `.cursor/rules/`. Propose modify, not a second rule.
- The user asked for a review only. Do not write a rule until they choose add or modify.

## Saving a rule

After the user accepts, write `.cursor/rules/senior-security-engineer.mdc` in the project being reviewed, or update the file that already covers this concern.

```text
---
description: Senior security engineer in this repository follows the pattern already used next to the change
alwaysApply: false
---

# Senior security engineer

- State the one change.

BAD:  the line you found
GOOD: the line you will commit
```

Keep that rule under 50 lines. Leave `alwaysApply` false. Keep the description under 200 characters.

## Guidelines

- Report the file or command, why it matters, and the fix. Do not write exploit steps, and do not recommend a stack this repo does not use.
- A saved rule is one concern, under 50 lines, with `alwaysApply: false` and a description under 200 characters.
