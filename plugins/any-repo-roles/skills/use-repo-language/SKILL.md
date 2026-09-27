---
name: use-repo-language
description: "Use when the open project has a known language or framework and that skill should be opened."
disable-model-invocation: true
---

# Use the repo language

## When to use

Use this when the default route has already named a language that is present in the project.

## Instructions

1. Detect languages from extensions, manifests, and tool configs.
2. Open `../<name>/SKILL.md` for each language that is actually present. Those files are not already in context.
3. Skip a language the repository does not contain. Do not add it.
4. In a mixed repo, follow the language that owns the file you are changing.

## Worked pass

The repository has `go.mod`, `*.go` files, and a `package.json` only inside `web/`.

1. Open `/go` for a change under the module root.
2. Open `/javascript` or `/typescript` only when the file you are changing is under `web/`.
3. Do not open `/python` or `/rust`. Do not add those languages.
4. Apply the opened skill's checks, then ask before you add or modify a rule.

## Languages

- `/python` — Python
- `/typescript` — TypeScript
- `/javascript` — JavaScript
- `/go` — Go
- `/rust` — Rust
- `/java` — Java
- `/kotlin` — Kotlin
- `/swift` — Swift
- `/c` — C
- `/cpp` — C++
- `/csharp` — C#
- `/ruby` — Ruby
- `/php` — PHP
- `/scala` — Scala
- `/elixir` — Elixir
- `/erlang` — Erlang
- `/dart` — Dart
- `/sql` — SQL
- `/shell` — shell
- `/html-css` — HTML and CSS
- `/r` — R
- `/lua` — Lua
- `/haskell` — Haskell
- `/ocaml` — OCaml
- `/fsharp` — F#
- `/clojure` — Clojure
- `/zig` — Zig
- `/perl` — Perl
- `/julia` — Julia
- `/powershell` — PowerShell
- `/objective-c` — Objective-C
- `/solidity` — Solidity
- `/groovy` — Groovy
- `/fortran` — Fortran
- `/matlab` — MATLAB
- `/nix` — Nix
- `/graphql` — GraphQL
- `/protobuf` — Protocol Buffers
- `/terraform` — Terraform
- `/cmake` — CMake
- `/react` — React
- `/vue` — Vue
- `/svelte` — Svelte
- `/angular` — Angular
- `/django` — Django
- `/rails` — Rails
- `/spring` — Spring
- `/flutter` — Flutter
- `/dotnet` — .NET
- `/laravel` — Laravel
