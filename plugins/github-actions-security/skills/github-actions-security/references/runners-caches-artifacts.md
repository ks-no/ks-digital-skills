# Runners, caches and artifacts

Load this file when a workflow uses self-hosted runners, caches, or artifacts from
another workflow.

## Self-hosted runners

- Do not use self-hosted runners in a public repository. A pull request from a fork
  can run code on them, and that code can stay on the machine for later jobs.
- In a private repository, each user who can open a pull request can run code on
  the runner. Treat that as a risk too.
- Use ephemeral or just-in-time runners, so that each runner does one job and is
  then removed.
- Put runners for deploy and release jobs in a separate runner group. Do not let
  other repositories or workflows use that group.
- Keep long-lived credentials off the runner machine.

## Caches

- A run can restore caches from its own branch and from the default branch. A
  pull request run can also restore caches from its base branch. So a cache entry
  on the default branch reaches all branches.
- Privileged triggers (`pull_request_target`, `issue_comment`, `workflow_run`) run
  in the context of the default branch. If such a job runs untrusted code, that
  code can write a cache entry that a later release job restores ("cache
  poisoning").
- Do not restore a cache in a job that publishes, signs or deploys. Many `setup-*`
  actions cache through an input. Turn it off in those jobs:
  - `actions/setup-node`: do not set `cache:`, and set
    `package-manager-cache: false`, because newer versions cache npm by default
    when `package.json` names npm as the package manager
  - `actions/setup-python`: do not set `cache:`
  - `actions/setup-java`: do not set `cache:`
  - `actions/setup-go`: set `cache: false`, because it caches by default
- Do not use caches in a privileged job that runs untrusted code.

## Artifacts

- An artifact from another workflow run is data from that run. If a fork could
  control that run, the artifact is attacker input.
- Download it into `runner.temp`, not into the workspace. Then it cannot replace a
  file that a later step runs.
- Do not run, source, import or extract files from it into a place where a later
  step runs code.
- Check each value before use, for example that a number is only digits.

## Credentials in artifacts

`actions/checkout` stores the token in `.git/config` unless
`persist-credentials: false` is set. If a job uploads the workspace, the token can
be in the artifact. Set `persist-credentials: false` and upload only the build
output, not the whole workspace.
