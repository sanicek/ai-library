# Contributing

## General Criteria

An asset should solve a recurring need, be understandable without private
context, and be safe to inspect and adapt before use. Keep changes focused and
avoid abstractions that make manual copying harder.

Use lowercase hyphen-separated names, such as `code-reviewer` or
`systematic-debugging`. Document prerequisites and runtime assumptions. Never
include real credentials or confidential project material.

## Agents

Store OpenCode-compatible agents as `agents/<name>.md`. Keep the prompt body as
runtime-neutral as practical while using native OpenCode frontmatter:

```markdown
---
description: Reviews changes for correctness and regressions.
mode: subagent
permission:
  edit: deny
---

Review the requested changes. Prioritize concrete findings...
```

Agents require `description` and a `mode` of `primary`, `subagent`, or `all`.

## Skills

Store each skill at `skills/<name>/SKILL.md`. Supporting files may live under
that skill's `references/`, `scripts/`, or `assets/` directories.

```markdown
---
name: example-skill
description: Use when a request matches the concrete triggers described here.
---

# Example Skill

Instructions for applying the skill...
```

The frontmatter name must match the directory name. Descriptions should explain
both what the skill does and when it applies.

## OpenCode Commands

Store commands as `commands/opencode/<name>.md`:

```markdown
---
description: Performs a specific repeatable workflow.
agent: build
---

Perform the workflow using this input: $ARGUMENTS
```

The Markdown body is the command template and must not be empty.

## MCP Configurations

Store each MCP example in `mcp/<name>/` with:

- `README.md` describing its purpose, prerequisites, required environment
  variables, and relevant security considerations.
- `opencode.json` containing a complete valid JSON example with `$schema` and an
  `mcp` object.

Use OpenCode environment interpolation such as `{env:GITHUB_TOKEN}` instead of
literal secrets. Consumers manually merge the desired server entry into their
project configuration.

## Instructions And Collections

Store reusable policy documents in `instructions/<name>.md`. Store curated,
human-readable workspace recipes in `collections/<name>.md`. Collections should
link to assets and explain why they work together; they are not manifests for an
installer.

## Local Validation

Run:

```sh
python3 scripts/validate.py
```

Fix validation failures before a requested commit. No hosted CI or Git hook is
used; closing the validation loop is part of the local agent workflow described
in `AGENTS.md`.
