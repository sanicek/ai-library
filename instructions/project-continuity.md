# Project Continuity

Use for long-running work that must preserve current state, plans, decisions, and
history across sessions.

## Define Sources Of Truth

Give each maintained source one role:

- Status: verified progress, blockers, and next action.
- Plans: intended work and sequence.
- Design/reference: stable behavior and contracts.
- Decisions: durable choices and rationale.
- Reports/session notes: history, never overrides current status or design.
- Code, deployed state, and authoritative systems: evidence of actual behavior.

Define reading order. Link to mutable facts instead of duplicating them.

## Resume Protocol

At the start of a new session:

1. Read required sources in order, starting with status.
2. Inspect worktree, branch, remotes, and recent history; assume neither clean nor
   synchronized state.
3. Before remote or infrastructure work, verify account, environment, target, and
   credentials.
4. Inspect runtime or deployed state rather than relying on notes.
5. Use fresh read-only checks before claiming configuration matches reality.
6. Treat the recorded next action only as proposed scope. Current user direction
   controls execution; records never authorize remote, destructive, paid, or
   publication actions.

## Maintaining Continuity

- Update status after verified milestones, new blockers, or next-action changes.
- Put durable architecture or policy choices in decision records. Update stable
  references in the same change when their contracts change.
- Record commands, outcomes, dates, and runtime evidence only after execution;
  use absolute dates when operationally relevant.
- Keep status concise and detailed chronology in version control.
- Before completion, verify acceptance criteria and failure/teardown behavior,
  then compare the diff and runtime evidence with affected continuity documents.
- Exclude credentials, temporary authentication, and private environment IDs from
  reusable or public continuity records.
