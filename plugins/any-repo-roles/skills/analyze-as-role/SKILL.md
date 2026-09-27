---
name: analyze-as-role
description: "Use when the user asks for a review, says all or everything, or wants every applicable role."
---

# Analyze as a role

## When to use

Use this for a review. "all", "all roles", "everything", "full review", and "etc" mean every applicable role plus each language already present.

## Instructions

1. Detect languages from extensions, manifests, and tool configs. Name the repository type.
2. If they name roles or languages, review only those. If they give no scope, review senior security, product design, and the language that owns the files being discussed.
3. Open one sibling `SKILL.md` at a time and apply its Checks. Do not keep every skill in context.
4. Skip a role with nothing to inspect, and say why in one line. Do not invent a UI, service, or model.
5. Lead with findings more than one role would flag. Tie each finding to a file or command.

## Ask before writing rules

Do not write rules yet. List each proposal as add, modify, or skip.

- Add: a new `.cursor/rules/<concern>.mdc`.
- Modify: an existing file, and the change you would make.
- Skip a role that found nothing.

Wait for the answer. Write only what the user accepts.

## Worked pass

The user says "all" in a Go service that has HTTP handlers and a SQL migration.

1. Detect Go and SQL. The repository type is a service.
2. Open every role skill that has a surface, one at a time, plus `/go` and `/sql`. Skip game, embedded, and mobile in one line each because those files are not here.
3. Keep senior security and product design even when the user did not name them.
4. Lead with a finding both security and the API role would flag, with the file path.
5. Propose one rule per role that found something. Mark each add or modify. Wait.

## Guidelines

- An accepted rule uses `alwaysApply: false`, a description under 200 characters, and `globs` only for file types already in the project.
- Stay under 50 lines, with a BAD line and a GOOD line from this project.
- Do not write into `plugins/` unless they asked to publish a pack.

## Roles

- `/senior-security-engineer` — Senior security engineer
- `/privacy-engineer` — Privacy engineer
- `/compliance-reviewer` — Compliance reviewer
- `/product-designer` — Product designer
- `/product-manager` — Product manager
- `/ux-researcher` — UX researcher
- `/content-designer` — Content designer
- `/design-systems-designer` — Design systems designer
- `/accessibility-specialist` — Accessibility specialist
- `/senior-software-engineer` — Senior software engineer
- `/staff-engineer` — Staff engineer
- `/frontend-engineer` — Frontend engineer
- `/backend-engineer` — Backend engineer
- `/mobile-engineer` — Mobile engineer
- `/data-engineer` — Data engineer
- `/machine-learning-engineer` — Machine learning engineer
- `/embedded-engineer` — Embedded engineer
- `/game-engineer` — Game engineer
- `/qa-engineer` — QA engineer
- `/performance-engineer` — Performance engineer
- `/sre` — Site reliability engineer
- `/devops-engineer` — DevOps engineer
- `/platform-engineer` — Platform engineer
- `/release-engineer` — Release engineer
- `/database-administrator` — Database administrator
- `/api-designer` — API designer
- `/localization-specialist` — Localization specialist
- `/engineering-manager` — Engineering manager
- `/technical-writer` — Technical writer
- `/support-engineer` — Support engineer
- `/customer-success` — Customer success
- `/data-analyst` — Data analyst
- `/solutions-architect` — Solutions architect
