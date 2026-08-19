#!/usr/bin/env python3
"""Validate the repository's reusable agentic assets."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_FIELD = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
REQUIRED_ROOT_FILES = ("AGENTS.md", "README.md", "CONTRIBUTING.md", "LICENSE")
ASSET_ROOTS = ("agents", "skills", "commands", "mcp", "instructions", "collections")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|gho|ghu|ghs|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style token": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
}


class DuplicateJsonKey(ValueError):
    """Raised when a JSON object contains the same key more than once."""


def error(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def validate_name(errors: list[str], path: Path, name: str) -> None:
    if not NAME_PATTERN.fullmatch(name):
        error(errors, path, f"'{name}' must be lowercase hyphen-separated")


def parse_frontmatter(
    errors: list[str], path: Path
) -> tuple[dict[str, str], str] | None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        error(errors, path, "missing opening frontmatter delimiter")
        return None

    try:
        end = lines.index("---", 1)
    except ValueError:
        error(errors, path, "missing closing frontmatter delimiter")
        return None

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if line.startswith((" ", "\t")) or not line.strip():
            continue
        match = FRONTMATTER_FIELD.fullmatch(line)
        if match:
            fields[match.group(1)] = (match.group(2) or "").strip().strip("\"'")

    return fields, "\n".join(lines[end + 1 :]).strip()


def require_fields(
    errors: list[str], path: Path, fields: dict[str, str], required: tuple[str, ...]
) -> None:
    for field in required:
        if not fields.get(field):
            error(errors, path, f"frontmatter field '{field}' is required")


def validate_agents(errors: list[str]) -> None:
    directory = ROOT / "agents"
    if not directory.exists():
        return

    for path in sorted(directory.glob("*.md")):
        validate_name(errors, path, path.stem)
        parsed = parse_frontmatter(errors, path)
        if parsed is None:
            continue
        fields, body = parsed
        require_fields(errors, path, fields, ("description", "mode"))
        if fields.get("mode") not in {"primary", "subagent", "all"}:
            error(errors, path, "mode must be primary, subagent, or all")
        if not body:
            error(errors, path, "agent prompt body must not be empty")


def validate_skills(errors: list[str]) -> None:
    directory = ROOT / "skills"
    if not directory.exists():
        return

    for skill_dir in sorted(path for path in directory.iterdir() if path.is_dir()):
        validate_name(errors, skill_dir, skill_dir.name)
        path = skill_dir / "SKILL.md"
        if not path.is_file():
            error(errors, skill_dir, "missing SKILL.md")
            continue
        parsed = parse_frontmatter(errors, path)
        if parsed is None:
            continue
        fields, body = parsed
        require_fields(errors, path, fields, ("name", "description"))
        if fields.get("name") and fields["name"] != skill_dir.name:
            error(errors, path, "frontmatter name must match the skill directory")
        if not body:
            error(errors, path, "skill body must not be empty")


def validate_commands(errors: list[str]) -> None:
    directory = ROOT / "commands" / "opencode"
    if not directory.exists():
        return

    for path in sorted(directory.glob("*.md")):
        validate_name(errors, path, path.stem)
        parsed = parse_frontmatter(errors, path)
        if parsed is None:
            continue
        fields, body = parsed
        require_fields(errors, path, fields, ("description",))
        if not body:
            error(errors, path, "command template body must not be empty")


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonKey(f"duplicate key '{key}'")
        result[key] = value
    return result


def validate_mcp(errors: list[str]) -> None:
    directory = ROOT / "mcp"
    if not directory.exists():
        return

    for server_dir in sorted(path for path in directory.iterdir() if path.is_dir()):
        validate_name(errors, server_dir, server_dir.name)
        readme = server_dir / "README.md"
        config_path = server_dir / "opencode.json"
        if not readme.is_file():
            error(errors, server_dir, "missing README.md")
        if not config_path.is_file():
            error(errors, server_dir, "missing opencode.json")
            continue

        try:
            config = json.loads(
                config_path.read_text(encoding="utf-8"),
                object_pairs_hook=reject_duplicate_keys,
            )
        except (json.JSONDecodeError, DuplicateJsonKey) as exc:
            error(errors, config_path, f"invalid JSON: {exc}")
            continue

        if not isinstance(config, dict):
            error(errors, config_path, "configuration must be a JSON object")
            continue
        if config.get("$schema") != "https://opencode.ai/config.json":
            error(errors, config_path, "missing the OpenCode $schema declaration")
        servers = config.get("mcp")
        if not isinstance(servers, dict):
            error(errors, config_path, "mcp must be a JSON object")
            continue
        if server_dir.name not in servers:
            error(errors, config_path, "mcp must contain a server matching its directory name")


def validate_markdown_asset_names(errors: list[str]) -> None:
    for category in ("instructions", "collections"):
        directory = ROOT / category
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            validate_name(errors, path, path.stem)


def validate_secrets(errors: list[str]) -> None:
    for root_name in ASSET_ROOTS:
        directory = ROOT / root_name
        if not directory.exists():
            continue
        for path in sorted(item for item in directory.rglob("*") if item.is_file()):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(text):
                    error(errors, path, f"contains a value resembling a {label}")


def main() -> int:
    errors: list[str] = []
    for filename in REQUIRED_ROOT_FILES:
        path = ROOT / filename
        if not path.is_file():
            error(errors, path, "required repository file is missing")

    validate_agents(errors)
    validate_skills(errors)
    validate_commands(errors)
    validate_mcp(errors)
    validate_markdown_asset_names(errors)
    validate_secrets(errors)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for message in errors:
            print(f"- {message}", file=sys.stderr)
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
