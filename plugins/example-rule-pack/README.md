# example-rule-pack

A worked example of a rule pack other Cursor users can install from this repository.

It is not a standard you must follow in your own projects. Copy `templates/rule-plugin` and add a new folder under `plugins/` when you want to publish rules for other people.

## Rules in this pack

| Rule | When it applies |
| --- | --- |
| `never-commit-secrets` | Agent pulls it in when the conversation is about secrets or commits |
| `typescript-error-handling` | A `.ts` or `.tsx` file is in context |

## Skill in this pack

| Skill | When it applies |
| --- | --- |
| `review-shared-rule` | Someone invokes `/review-shared-rule` |
