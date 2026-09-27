# any-repo-roles

Review a repository in whatever languages and shape it actually has.

Detect the stack first. Then review as a named role, or as every role in this pack. A full review always includes senior security and product design. A role with nothing to inspect says so and stops, instead of inventing a web app, a mobile client, or a model.

Invoke `/analyze-as-role` for a full review, or one role, for example `/senior-security-engineer` or `/product-designer`. Invoke `/use-repo-language` to follow the language this repository already contains, for example `/python`, `/rust`, or `/react`.

## Rule

| Rule | When it applies |
| --- | --- |
| `detect-stack` | The agent is about to change or review code in any language |

## Roles

Security and trust: senior security, privacy, compliance.

Product and design: product designer, product manager, UX researcher, content designer, design systems, accessibility.

Engineering: senior software engineer, staff engineer, frontend, backend, mobile, data, machine learning, embedded, game, QA, performance, API design, database, localization.

Delivery: SRE, DevOps, platform, release, engineering manager, technical writer, support, customer success, data analyst, solutions architect.

## Languages

Each skill applies only when that language or ecosystem is already in the repo.

Languages: Python, TypeScript, JavaScript, Go, Rust, Java, Kotlin, Swift, C, C++, C#, Ruby, PHP, Scala, Elixir, Erlang, Dart, R, Lua, Haskell, OCaml, F#, Clojure, Zig, Perl, Julia, MATLAB, Fortran, Objective-C, Groovy, PowerShell, shell, SQL, HTML/CSS, Nix, GraphQL, Protocol Buffers, Terraform, CMake, Solidity.

Ecosystems: React, Vue, Svelte, Angular, Django, Rails, Spring, Laravel, Flutter, .NET.
