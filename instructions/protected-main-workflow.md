# Protected Main Workflow

Use this policy when all repository changes must reach the default branch through
reviewed pull requests.

This policy describes mechanics; it grants no authority to change Git history or
remote state. A request to edit files does not authorize committing, pushing,
opening or updating a pull request, merging, or deleting branches. Require a
current, unambiguous user instruction covering each externally visible or
destructive action before performing it.

## Starting Work

- Treat the default branch as protected. Do not commit or push directly to it.
- Before creating a branch, inspect the worktree, current branch, remotes, and
  recent history. Do not discard or absorb unrelated changes.
- Start from the current remote default branch unless the user explicitly chooses
  another base.
- Name the branch according to repository convention. When no convention exists,
  use a short lowercase hyphen-separated description with an appropriate change
  prefix.

## Preparing The Change

- Keep the branch focused on one coherent purpose.
- Run validation appropriate to the actual change. Do not claim broader coverage
  than the commands provide.
- Inspect the complete intended diff and recent history before committing.
- Stage only intended files and follow the repository's commit-message policy.
- Never skip hooks, checks, or validation merely to produce a commit.

## Opening And Updating The Pull Request

- Push the feature branch and open a pull request against the intended base.
- Summarize the behavior and rationale, not just the files changed.
- Record the validation commands and their results. State unavailable or skipped
  checks explicitly.
- Review every commit and the complete base-to-head diff before presenting the
  pull request as ready.
- If review requests changes, reuse the same branch and pull request. Make the
  focused amendment, validate it, commit it, and push it.
- Keep the pull request description accurate as scope or validation changes.

## Merging

- Do not merge without explicit user authorization.
- Immediately before merging, confirm the pull request is open, targets the
  intended base, is mergeable, and has the required reviews or checks.
- Use the repository-selected merge, squash, or rebase strategy. Do not impose a
  different history policy from this reusable instruction.
- After merging, synchronize the local default branch and verify the merged
  state with non-destructive fetch and fast-forward operations. If the worktree
  is dirty or the branch has diverged, stop instead of resetting, cleaning,
  implicitly stashing, or discarding work.
- Delete local or remote branches only when the current user authorizes cleanup
  and repository policy permits that branch to be deleted.
- Report the pull request URL, resulting commit, validation evidence, and final
  worktree state.
