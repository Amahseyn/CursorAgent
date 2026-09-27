---
name: terraform
description: Write and review Terraform in any repository that already contains it. Use when the repo has Terraform or OpenTofu files.
---

# Terraform

Use this only when the repository already contains Terraform. Do not add it, and do not switch the file to another language.

Look for:

- A resource the state layout does not already manage, added in a one-off folder.
- A provider version floating when the lock file pins providers.
- A secret written in a `.tf` file.
- An apply step suggested as the edit. Change the configuration the modules already use.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Put the API token in the `.tf` file and apply production.
GOOD: Pass the token through the variable the module already declares. Leave apply to the human.
```
