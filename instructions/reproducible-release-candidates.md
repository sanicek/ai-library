# Reproducible Release Candidates

Use when published installable artifacts must contain the exact tested bytes.

## Classify The Change

- Release changes that affect shipped output, runtime behavior, compatibility,
  dependencies, or artifact-generating tools. Classify by artifact behavior, not
  file type or label.
- Documentation, process, tests, and internal tools need no release when shipped
  output is provably unchanged.
- For release-bearing changes, select a version and update release records in the
  same pull request. Follow repository versioning; do not assume SemVer.

## Build The Candidate

- Build once from a clean, identified commit using the canonical packaging entry
  point and pinned dependencies.
- Record source revision, dependency and tool versions, build options, and platform
  details needed to reproduce it.
- Calculate a strong checksum such as SHA-256. Never silently replace accepted
  version bytes.

## Validate The Exact Artifact

- Validate archive structure, metadata, and contents; install or deploy it without
  rebuilding; run practical automated checks against the installed candidate.
- Run only the smallest representative manual smoke test establishing the release
  contract unless broader coverage is requested.
- Record checksum and results. Any byte change voids acceptance.
- Do not merge before required acceptance; use a draft pull request when needed.

## Merge And Publication

- Reproduce after merge in a fresh clone/worktree when possible. Otherwise use
  only non-destructive fetch and fast-forward on a clean default branch. Stop on
  dirtiness or divergence; never reset, clean, or implicitly stash.
- The rebuilt checksum must match the accepted candidate. A mismatch voids
  acceptance; investigate and repeat full-artifact validation before publication.
- Publish only the accepted artifact, checksum, and required release/provenance
  records. Immediately before upload, checksum the exact supplied file and stop
  unless it matches. Verify and record any immutable destination digest.
- Treat hosting-service snapshots as source archives, not automatically supported
  installable packages.
- Require current user authorization and repository policy for tags, releases,
  deployments, marketplace uploads, and publication; ask if either is unclear.
- Report revision, artifact identity, checksum, validation, and publication result.
