# GitHub Grep

GitHub Grep exposes grep.app code search through MCP. It is useful for finding
literal implementation patterns and real-world examples across public GitHub
repositories.

## OpenCode Setup

Merge the `gh_grep` entry from [`opencode.json`](opencode.json) into the `mcp`
object in the target workspace's OpenCode configuration. Restart OpenCode after
changing configuration.

The underscore in `gh_grep` is intentional: it preserves the server name used
in OpenCode's official MCP documentation and produces stable tool names. The
library directory uses the repository's lowercase hyphen-separated convention.

No credential is required by this configuration.

## Usage

Search for literal code that would occur in source files, not conceptual
keywords. Narrow searches by language, repository, or path where possible.

Queries are sent to a remote service, and results come from publicly indexed
GitHub repositories. Do not include credentials, private source code, or other
sensitive information in queries.

Source: [OpenCode MCP server documentation](https://opencode.ai/docs/mcp-servers/)
