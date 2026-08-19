# Project Continuity

Use this policy for long-running work where future sessions must distinguish
current state, intended work, settled decisions, and historical context.

## Define Sources Of Truth

Assign one clear purpose to each maintained document or system:

- Status records verified progress, current blockers, and the next action.
- Plans describe intended future work and sequencing.
- Design or reference documents describe stable current behavior and contracts.
- Decision records preserve durable choices and rationale.
- Historical reports and session notes provide context but do not override current
  status or design.
- Source code, deployed state, and authoritative external systems remain the
  evidence for actual behavior.

Document the required reading order. Avoid duplicating the same mutable facts in
multiple places; link to the authoritative source instead.

## Resume Protocol

At the start of a new session:

1. Read the required sources in order, beginning with current status.
2. Inspect the worktree, branch, remotes, and recent history. Never assume the
   workspace is clean or synchronized.
3. Verify the active account, environment, target, and credentials before any
   remote or infrastructure operation.
4. Inspect relevant runtime or deployed state instead of relying only on notes.
5. Run fresh read-only verification or planning commands before claiming that
   configuration and reality match.
6. Treat the recorded next action as proposed scope. The current user's request
   controls what may execute, and recorded state never authorizes remote,
   destructive, paid, or publication actions.

## Maintaining Continuity

- Update status after a verified milestone, newly discovered blocker, or change
  to the next action.
- Record durable architecture or policy choices in the decision log, not only in
  status updates or conversation history.
- Update stable design references in the same change when their contracts change.
- Record commands, outcomes, dates, and runtime evidence only after execution.
- Use absolute dates when timing affects operations, releases, or incident history.
- Keep status concise; use version-control history for detailed change chronology.
- Do not mark work complete until its acceptance criteria and failure or teardown
  behavior have been verified.
- Before finishing, compare the actual diff and runtime evidence with all affected
  status, design, plan, and decision documents.
- Keep credentials, short-lived authentication material, and private environment
  identifiers out of continuity documentation intended for reuse or publication.
