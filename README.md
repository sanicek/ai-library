# AI Library

A personal library of reusable agents, skills, commands, instructions, and MCP
configuration examples for agentic workspaces.

Assets in this repository are starting points, not dependencies. Copy the parts
you need into a target repository, adapt them there, and treat the copied files
as owned by that repository. Backport generally useful lessons here as normal,
deliberate changes.

## Layout

| Path | Contents |
| --- | --- |
| `agents/` | OpenCode-compatible agents with reusable prompt bodies |
| `skills/` | Portable Agent Skills directories containing `SKILL.md` |
| `commands/opencode/` | OpenCode command definitions |
| `mcp/` | MCP server notes and OpenCode configuration examples |
| `instructions/` | Reusable guidance suitable for `AGENTS.md` or config instructions |
| `collections/` | Human-readable recommendations for assembling workspace setups |
| `scripts/validate.py` | Dependency-free local structural validation |

Directories may be absent until the library contains an asset of that kind.

## Catalog

### Agents

| Asset | Purpose |
| --- | --- |
| [`security-oracle`](agents/security-oracle.md) | Independent security, correctness, and architecture review |

The security oracle preserves its opinionated OpenAI model selection and grants
unrestricted Bash access for investigation. Its `edit: deny` setting does not
prevent shell commands from changing files. Review and restrict its permissions
before copying it into a workspace with different trust requirements.

### MCP Servers

| Asset | Purpose |
| --- | --- |
| [`context7`](mcp/context7/) | Current library and framework documentation |
| [`gh-grep`](mcp/gh-grep/) | Literal code search across public GitHub repositories |

## Using Assets

Copy assets manually. For example:

```sh
cp agents/code-reviewer.md /path/to/project/.opencode/agent/
cp -R skills/systematic-debugging /path/to/project/.opencode/skills/
```

Review an asset before using it. Paths, permissions, available tools, and project
conventions often need local adaptation.

MCP examples are complete JSON documents for reference and validation. Merge the
relevant `mcp` entry into the target project's `opencode.json`; do not replace an
existing project configuration wholesale. Environment variables are documented
beside each example, and secrets must remain outside this repository.

## Validation

Run the local validator after editing the library and before committing:

```sh
python3 scripts/validate.py
```

There is intentionally no hosted runner, Git hook, package manager setup, asset
installer, or update mechanism.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for asset formats and review criteria.
