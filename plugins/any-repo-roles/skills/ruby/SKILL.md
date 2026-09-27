---
name: ruby
description: Write and review Ruby in any repository that already contains it. Use when the repo has Ruby files, a Gemfile, or a gemspec.
---

# Ruby

Use this only when the repository already contains Ruby. Do not add it, and do not switch the file to another language.

Look for:

- `rescue Exception` or a rescue with an empty body.
- A gem added that the Gemfile and lockfile do not already agree on.
- A test helper other than the RSpec or Minitest layout already here.
- A frozen-string or magic-comment style that fights the file above.

Match the formatter, package layout, and test tool already in the repo.

```text
BAD:  Rescue Exception and print nothing.
GOOD: Rescue the error class the service already rescues, and keep the Gemfile.
```
