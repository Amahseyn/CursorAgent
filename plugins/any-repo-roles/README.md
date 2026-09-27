# any-repo-roles

Review a repository in whatever languages and shape it actually has.

Detect the stack first. Then review as a named role, or as every role in this pack. A full review always includes senior security and product design. A role with nothing to inspect says so and stops, instead of inventing a web app, a mobile client, or a model.

Install steps are in [docs/how-to-use.md](../../docs/how-to-use.md). The default reads the code and calls only the matching role or language, then asks before adding or modifying a rule. Type `all` for every applicable role.

## Rule

| Rule | When it applies |
| --- | --- |
| `route-from-code` | Every chat. Reads the code and calls only the matching role or language |
| `detect-stack` | The agent is about to change or review code in any language |
| `when-they-say-all` | The user says all, everything, or asks for a full review |

## Roles

Security and trust: senior security, privacy, compliance.

Product and design: product designer, product manager, UX researcher, content designer, design systems, accessibility.

Engineering: senior software engineer, staff engineer, frontend, backend, mobile, data, machine learning, embedded, game, QA, performance, API design, database, localization.

Delivery: SRE, DevOps, platform, release, engineering manager, technical writer, support, customer success, data analyst, solutions architect.

## Languages

Each skill applies only when that language or ecosystem is already in the repo.

Languages: Python, TypeScript, JavaScript, Go, Rust, Java, Kotlin, Swift, C, C++, C#, Ruby, PHP, Scala, Elixir, Erlang, Dart, R, Lua, Haskell, OCaml, F#, Clojure, Zig, Perl, Julia, MATLAB, Fortran, Objective-C, Groovy, PowerShell, shell, SQL, HTML/CSS, Nix, GraphQL, Protocol Buffers, Terraform, CMake, Solidity.

Ecosystems: React, Vue, Svelte, Angular, Django, Rails, Spring, Laravel, Flutter, .NET.

## Git and workflows

Git: commit, branch, pull request, merge conflict, history.

Also: Docker, debugging, dependencies, configuration, logging, feature flags, background jobs, caching, monorepos, formatting, and error handling. Each one runs only when that workflow is already in the repo.
