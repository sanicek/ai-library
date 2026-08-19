# Context7

Context7 supplies current, version-aware library documentation and code examples
through a remote MCP server.

## OpenCode Setup

Merge the `context7` entry from [`opencode.json`](opencode.json) into the `mcp`
object in the target workspace's OpenCode configuration. Restart OpenCode after
changing configuration.

The included configuration uses the public remote endpoint without credentials.
This is convenient for initial use but may have lower rate limits.

## Authentication

Context7 recommends authenticated use. Create an API key in the
[Context7 dashboard](https://context7.com/dashboard), export it before starting
OpenCode, and add a header to the copied server entry:

```json
{
  "headers": {
    "Authorization": "Bearer {env:CONTEXT7_API_KEY}"
  }
}
```

Do not put the API key itself in `opencode.json`. For an OAuth-managed setup,
use Context7's official `npx ctx7 setup --opencode` flow instead of manually
copying this example.

## Usage

Use Context7 for library, framework, SDK, API, CLI, and cloud-service questions
where current documentation matters. Resolve the library ID first unless an
exact Context7 ID such as `/vercel/next.js` is already known.

Requests and query context are sent to the Context7 service. Review its terms
before using it with sensitive or private information.

Sources:

- [Context7 OpenCode documentation](https://context7.com/docs/clients/opencode)
- [Context7 project](https://github.com/upstash/context7)
