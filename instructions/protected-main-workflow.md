# Protected Main Workflow

Use when all changes reach the default branch through reviewed pull requests.

This policy grants no authority. Editing does not authorize commits, pushes, pull
request creation or updates, merges, or branch deletion. Each requires current,
unambiguous user authorization covering that action and scope.

## Starting Work

- Never commit or push directly to the protected default branch.
- Before branching, inspect worktree, branch, remotes, and recent history; neither
  discard nor absorb unrelated changes.
- Base work on the current remote default branch unless the user chooses another.
- Follow repository branch naming, or use a short lowercase hyphenated name.

## Preparing The Change

- Keep one coherent purpose. Run relevant validation without overstating coverage.
- Before an authorized commit, inspect the complete intended diff and recent
  history, stage only intended files, follow message policy, and never skip hooks
  or checks.

## Opening And Updating The Pull Request

- When authorized, push the branch and open or update its pull request against the
  intended base.
- Describe behavior and rationale, validation commands/results, and unavailable
  or skipped checks.
- Before declaring readiness, review every commit and the complete base-to-head
  diff.
- Address review on the same branch and pull request with focused, validated,
  separately authorized commits and pushes. Keep its description current.

## Merging

- Merge only when explicitly authorized, after confirming the pull request is
  open, correctly based, mergeable, and all required reviews and checks passed.
- Use repository-selected merge strategy; impose no history policy.
- After merge, synchronize the local default branch and verify merged state using
  only non-destructive fetch and fast-forward operations. Stop on dirtiness or
  divergence; never reset, clean, implicitly stash, or discard work.
- Delete branches only with current cleanup authorization and repository policy.
- Report the pull request URL, resulting commit, validation, and final worktree.
