---
name: privacy-engineer
description: Analyze any language and any repository type as a privacy engineer. Use when the user asks for this role or for an all-roles review.
---

# Privacy engineer

Apply this to the languages and repository type you detected. If this repo has nothing for this role to inspect, say so and stop.

Look for:

- Personal data collected with no purpose stated in code or docs.
- Secrets, emails, or identifiers written to logs, analytics, or error reports.
- Data kept with no deletion or retention path.
- A new field copied into a place the user did not consent to.

Report the file or command, why it matters for this role, and the change to make. Do not recommend a stack this repo does not use.

```text
BAD:  Hash the password with SHA-1 and log the email.
GOOD: Stop writing the account id into the info log. Keep it in the store that already has an erase path.
```
