---
name: frontend-engineer
description: "Use when the user asks for this role or for an all-roles review."
disable-model-invocation: true
---

# Frontend engineer

## When to use

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

## When not to use

- The repository has no Frontend engineer surface. Say so in one line and stop.
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

- Client state that duplicates the server state this repo already stores.
- A request waterfall or a payload that ships data the view does not render.
- An interaction that loses input on refresh or error.
- If there is no UI, review the user-facing surface that does exist and say there is no frontend.

## How to apply each check

### 1. Client state that duplicates the server state this repo already stores.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 2. A request waterfall or a payload that ships data the view does not render.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 3. An interaction that loses input on refresh or error.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

### 4. If there is no UI, review the user-facing surface that does exist and say there is no frontend.

Search the file you opened and the two files closest to it. A hit is this exact situation, not a similar idea from another stack.
If it hits, quote the line and say which check it is. The change is the smallest edit that makes the GOOD example true in this repository.
If it misses, say what you opened and that this check does not apply. Do not pad the report.

## Report

Use this shape. One block per finding.

```text
Skill: frontend-engineer
File: <path>
Check: <the check that failed>
Evidence: <the line you read>
Change: <the edit, using a pattern already in this repo>
```

If nothing failed, the whole report is one line: which files you opened and that this skill found nothing.

## Examples

```text
BAD:  Add a React context for a Go CLI.
GOOD: There is no UI. Review the command's flags and stdout instead.
```

Walk the BAD line as if it were in the repository:

1. You open the file and see: Add a React context for a Go CLI.
2. You open the neighboring file and see the pattern the GOOD line names.
3. You change only the failing part so the result matches: There is no UI. Review the command's flags and stdout instead.
4. You do not reformat unrelated code and you do not add a new tool.

## Edge cases

- Several languages are present. Stay inside the files this skill owns.
- A generated file or a vendor directory contains the hit. Report it only if the repository edits that file by hand.
- The same hit is already described in `.cursor/rules/`. Propose modify, not a second rule.
- The user asked for a review only. Do not write a rule until they choose add or modify.

## Saving a rule

After the user accepts, write `.cursor/rules/frontend-engineer.mdc` in the project being reviewed, or update the file that already covers this concern.

```text
---
description: Frontend engineer in this repository follows the pattern already used next to the change
alwaysApply: false
---

# Frontend engineer

- State the one change.

BAD:  the line you found
GOOD: the line you will commit
```

Keep that rule under 50 lines. Leave `alwaysApply` false. Keep the description under 200 characters.

## Guidelines

- Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.
- A saved rule is one concern, under 50 lines, with `alwaysApply: false` and a description under 200 characters.
