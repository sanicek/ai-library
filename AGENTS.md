# Repository Guidance

## Purpose

This repository contains reusable agentic assets. Consumers copy and adapt
individual assets; target repositories own their copies without synchronization.

## Working Rules

- Keep assets standalone, readable, manually copyable, and runtime-neutral where
  practical. Put runtime-specific assets under that runtime's directory.
- Do not add installers, management CLIs, lockfiles, generators, synchronization
  metadata, Git hooks, hosted CI, or dependencies used only for validation.
- Never commit credentials, tokens, private keys, or private project details.
- Use lowercase hyphen-separated names and preserve each runtime's native format.
- Add a new top-level asset category only when adding a real asset of that kind,
  then document its conventions in `README.md` and `CONTRIBUTING.md`.
- Keep `README.md` repository-wide; the filesystem is the asset catalog.
- Improve assets in place. Add variants only for materially different behavior
  or runtimes.

## Validation

After changing assets or conventions, run:

```sh
python3 scripts/validate.py
```

Before a user-requested commit, also inspect `git status --short` and the complete
intended diff, then stage only intended files. Never commit without an explicit
request. If validation cannot run, report why; do not claim success.

# Style

Be terse and information-dense. Omit filler, restatement, routine narration,
repeated context, and generic offers. Explain only useful non-obvious decisions,
tradeoffs, uncertainty, failures, or architecture.

Use targeted reads, avoid duplicated work, delegate suitable repetitive tasks,
make the smallest coherent change, and verify the narrowest relevant scope first.
Final responses normally state changes, caveats, and verification. Preserve exact
technical text and omit anything irrelevant to correctness or clarity.
