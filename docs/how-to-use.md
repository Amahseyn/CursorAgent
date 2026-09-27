# How to use CursorAgent

Most people need one pack and one command. You do not clone this repository to use it.

## Review the project you have open

1. In Cursor, open **Customize** in the sidebar.
2. Choose **From GitHub Repository** and paste:

   `https://github.com/Amahseyn/CursorAgent`

3. Install **Any repo roles**. Leave **Example rule pack** uninstalled unless you are learning the file format.
4. Open the project you want reviewed. This marketplace repo is not that project.

You do not type a command to start. The default mode reads the code and calls only the role or language that matches, then asks before it adds or modifies a rule.

`all`, `everything`, and `full review` mean every role that has something to inspect in this project, plus the languages already here. The agent still asks whether to add, modify, or skip, and writes a file only after you answer.

A review that names no scope covers senior security, product design, and the language of the files you are discussing. Name a role, such as "product designer", to review as that role only.

## Commands

Type `/` and pick a name. You do not need to memorize the list.

| You want | Type |
| --- | --- |
| Default: read the code and pick the review | Already on. `/route-from-code` turns the same mode on for the whole chat |
| All roles, then ask about rules | `all` or `/analyze-as-role` |
| Only senior security | `/senior-security-engineer` |
| Only product design | `/product-designer` |
| The language already in the repo | `/use-repo-language` |
| One language, when that language is already there | `/python`, `/typescript`, `/go`, `/rust`, or another name from the pack |
| Git | `/git-commit`, `/git-branch`, `/git-pull-request`, `/git-merge-conflict`, `/git-history` |

One role or one language stays out of the chat until you type its name or the review opens that file. Installing the pack does not paste every skill into every message.

## If the command does nothing

- The pack is not installed. Repeat the Customize steps and install **Any repo roles**.
- You are chatting in the wrong window. Open the project you want reviewed, then type the command there.
- Cursor has an old copy. In Customize, refresh the marketplace, or reinstall **Any repo roles**.

Copying a `.mdc` file into your project does not install this pack. Cursor reads `.cursor-plugin/marketplace.json` from the GitHub repository.

## What you should see

**Any repo roles** reviews a repository as senior security, product design, and the other software roles, in the language that repository already uses.

**Example rule pack** is a format sample with two short rules. It is not a review of your product.

## A team

An admin on a Teams or Enterprise plan can share the same repository:

1. Open the Cursor dashboard → **Plugins**.
2. Under **Team Marketplaces**, choose **Import from Repo**.
3. Paste `https://github.com/Amahseyn/CursorAgent`.
4. Save. Developers then install **Any repo roles** from Customize, unless an admin marks it default-on or required.

The repository has to stay on GitHub. GitLab and a zip file are not a marketplace Cursor can import. A private GitHub repository needs the Cursor GitHub App installed on that organization.

## A checkout on your machine

Clone only when you are changing the packs.

```bash
git clone https://github.com/Amahseyn/CursorAgent.git
cd CursorAgent
python3 scripts/validate_plugins.py
```

To load a pack into your own Cursor from that checkout, copy the folder. A symlink that points outside `~/.cursor/plugins/local` is ignored.

```bash
mkdir -p ~/.cursor/plugins/local
rm -rf ~/.cursor/plugins/local/any-repo-roles
cp -R plugins/any-repo-roles ~/.cursor/plugins/local/any-repo-roles
```

Reload the window. After you edit a skill, copy the folder again.

## Add a rule without filling the context

A rule that loads on every chat costs space in every project that installs the pack. Write it so Cursor can leave it out.

| Situation | What to put in the rule |
| --- | --- |
| The agent can tell from the task | `alwaysApply: false` and a one-sentence `description` |
| Only some files matter | `alwaysApply: false`, `globs`, and a one-sentence `description` |
| Only when someone @-mentions it | `alwaysApply: false`, and omit `description` and `globs` |
| Every chat, in every installed project | `alwaysApply: true`, and only when the rule is safe there |

Also:

- One concern. Stay under 50 lines. Include a `BAD` line and a `GOOD` line.
- Keep the description under 200 characters. That sentence is what Cursor uses to decide whether to load the file.
- Do not set `alwaysApply: true` and `globs` together. Cursor ignores `globs` in that case, and the rule still loads every time.
- A pack may have two skills that load on their own. Set `disable-model-invocation: true` on every other skill. People can still type `/skill-name`.
- Do not copy a skill from another repository. `catalog/skills.json` lists ones that already exist.

The steps for a new pack are in [CONTRIBUTING.md](../CONTRIBUTING.md).
