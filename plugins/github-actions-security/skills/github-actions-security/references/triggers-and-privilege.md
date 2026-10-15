# Triggers and privilege

Load this file when a workflow uses `pull_request_target`, `issue_comment`,
`issues` or `workflow_run`, or when the user wants to run code from a pull request
on request.

## Why some triggers are dangerous

GitHub runs these triggers with the workflow file from the default branch, a token
that can write, and access to secrets:

- `pull_request_target`
- `issue_comment` (also for comments on pull requests)
- `issues`, `discussion`, `discussion_comment`
- `workflow_run`

Any GitHub user can start them in a public repository. The workflow file itself is
safe, because it comes from the default branch. The danger is what the workflow
does with the pull request, the event text and the artifacts.

A "pwn request" is a privileged job that checks out the code of a pull request and
then builds, installs or runs it. The code can then read the token and the secrets.
These steps also run code from the pull request:

- `npm install`, `npm ci`, `pip install`, `mvn`, `gradle`, `dotnet build`, `make`
- a test runner, a linter with plugins, or a script in the repository
- an action that is referenced with a local path (`uses: ./...`) after the checkout

## pull_request_target

Use it only for work that does not need the code of the pull request, for example
to add a label or a comment. Do not set `ref:` on `actions/checkout` to the head or
the merge commit of the pull request in this workflow.

If you need to build the pull request, use `pull_request` instead. A fork then gets
a read-only token and no secrets, and the build is safe.

## A command or a label that runs code from a pull request

A user may want a maintainer to start a job on a pull request, for example
`/deploy-preview` or `/run-e2e`. Prefer this design:

1. A maintainer adds a label. Only users with triage or write access can add
   labels.
2. A `pull_request` workflow with `types: [labeled]` runs the code. It has a
   read-only token and no secrets. It uploads the result as an artifact, together
   with the pull request number.
3. A `workflow_run` workflow posts the result. It does not run code from the
   artifact. It reads the result as a file and checks the number.

An event that the `GITHUB_TOKEN` causes does not start other workflows. So a
workflow cannot add the label with that token and expect step 2 to start.

If the command must come from a comment (`issue_comment`), use separate jobs:

1. **Gate job.** Read the permission of the commenter from the API, for example
   `gh api "repos/$REPO/collaborators/$COMMENTER/permission" --jq .permission`.
   Continue only for `admin`, `maintain` or `write`. Do not trust
   `author_association` alone. Read the head SHA of the pull request at this time,
   and give it to the next job as an output.
2. **Run job.** `permissions: contents: read`, no secrets, no cache. Check out the
   SHA from the gate job, with `persist-credentials: false`. Run the code. Save the
   result as an artifact or a file.
3. **Post job.** It has `pull-requests: write` and does not check out or run code
   from the pull request. It reads the result as data and posts it with
   `--body-file`.

Show the SHA in the comment, so that the maintainer sees which commit ran. A new
push after the comment does not change the SHA that the run job uses.

The run job still runs in the context of the default branch. Code in it can write
cache entries that other workflows on the default branch restore. Keep caches out
of release jobs (see [runners-caches-artifacts.md](runners-caches-artifacts.md)).

## workflow_run

- The artifacts of the triggering run come from code that a fork controls. Treat
  each file as attacker input.
- Download artifacts into `${{ runner.temp }}`, not into the workspace, so that
  they cannot replace files that a later step uses.
- Do not run, source or import files from the artifact.
- Check each value before use. A pull request number must match `^[0-9]+$`.
- `github.event.workflow_run.head_branch` and similar fields are attacker text.
- For a fork, `github.event.workflow_run.pull_requests` is empty. That is why
  workflows send the number in the artifact. Check that it is a number. Then read
  the pull request from the API, and continue only if its head SHA equals
  `github.event.workflow_run.head_sha`. Else a fork can make the workflow comment on
  another pull request.
- A download of an artifact from the triggering run needs `actions: read`.

## Labels as approval

A label does not make a privileged job safe. Core rule 5 in the skill still applies,
so first offer the design above. If the user still wants a label to start a
privileged run of code from the pull request, limit it:

- Run the job that runs the code only when `github.event.action` is `labeled` and
  `github.event.label.name` is that label. A check that the pull request has the
  label is not enough, because a new push keeps the label and starts the workflow
  again.
- Check out `github.event.pull_request.head.sha`, not the branch name.
- From v7, `actions/checkout` blocks a checkout of a fork under
  `pull_request_target` and `workflow_run`, unless the step sets
  `allow-unsafe-pr-checkout: true`. Do not set this input, and do not use an older
  version to avoid the block. Tell the user that the block stops the workflow, and
  that a person who accepts the risk must add the input.
- Remove the label on the `synchronize` event, in a job that runs no code from the
  pull request. Then a maintainer must read the new code and add the label again.

## Identity checks

- `github.actor` is the user who caused the latest event. It is not the author of
  the code. Do not decide trust with it alone.
- A check such as `github.actor == 'dependabot[bot]'` can be wrong when another
  user starts a new run. Check the author of the pull request
  (`github.event.pull_request.user.login`) and the event type together.
- Runs from first-time contributors can need approval. That is a repository
  setting, not a security boundary for privileged triggers.
