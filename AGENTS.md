# Repository Guidance

## Purpose

This repository is a curated library of reusable agentic assets. Consumers copy
individual assets into another workspace and adapt them there. A copied asset is
owned by its target repository; this library does not track or update vendored
copies.

## Working Rules

- Keep assets standalone, readable, and easy to copy manually.
- Keep prompt bodies runtime-neutral where practical.
- Put runtime-specific assets in a directory named for that runtime.
- Do not add installers, management CLIs, lockfiles, generators, synchronization
  metadata, Git hooks, or hosted CI configuration.
- Do not introduce a dependency solely for repository validation.
- Never commit credentials, tokens, private keys, or private project details.
- Use lowercase hyphen-separated names for assets and directories.
- Preserve the native format expected by the target runtime.
- Add a new top-level asset category only when adding a real asset of that kind,
  and document its conventions in `README.md` and `CONTRIBUTING.md`.
- Prefer improving an asset in place over creating a nearly identical variant.
  Create a variant when its behavior or target runtime materially differs.

## Validation

Run the local validator after changing assets or repository conventions:

```sh
python3 scripts/validate.py
```

Before making a user-requested commit:

1. Run `python3 scripts/validate.py`.
2. Inspect `git status --short` and the complete intended diff.
3. Stage only the intended files.
4. Do not commit unless the user explicitly requested a commit.

If validation cannot run, state why rather than claiming the change is valid.
