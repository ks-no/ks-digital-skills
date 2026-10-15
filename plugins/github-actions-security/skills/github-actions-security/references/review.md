# Review of workflows

Load this file when the user asks for a review or an audit of workflows, actions or
a Dependabot configuration.

## Scope

- For a branch or a pull request, review the workflow files that the change adds or
  changes. Compare with the merge base of the default branch. Also read the
  workflows that call or are called by a changed file.
- For an audit, review all files in `.github/workflows/`, each `action.yml` in the
  repository, and the Dependabot configuration.
- Say at the start what you reviewed and what you did not review.

## Method

1. **Inventory.** For each workflow, list the triggers, the jobs, the token
   permissions of each job, the secrets, the runners and the actions.
2. **Untrusted input.** Mark each value that an outsider can control: event text,
   code and files from a pull request, artifacts and caches from other runs, and
   model output. Use the table in the skill and the lists in
   [injection.md](injection.md).
3. **Trace.** Follow each untrusted value to the places where it can do harm: a
   `run:` or `script:`, `GITHUB_ENV`, `GITHUB_OUTPUT`, `GITHUB_PATH`, a checkout, a
   build, a cache, a comment, a release.
4. **Supply chain.** Check the pin of each action, reusable workflow and image.
5. **Function.** Check that each fix that you propose keeps the workflow working.

## When to report a finding

Report a finding only when you can describe a concrete path from an attacker to an
impact, and you are at least 80% sure that it works. Name the attacker: any GitHub
user, a user with read access, or a user with write access. Describe the path in
words. Do not write a working payload.

| Severity | Typical example |
| --- | --- |
| Critical | Any GitHub user gets code execution in a job with a write token or secrets. Examples: a pwn request, or injection under `issue_comment`. |
| High | Any GitHub user can read a secret, or can run code in a job with a write token on a public repository. A third-party action on a tag gets publish or deploy secrets. |
| Medium | Only users with write access can exploit it, or the impact is limited. Examples: a missing `permissions:` block with a write default, or `secrets: inherit` to a pinned workflow. |
| Low | Hardening without a known attack path. Examples: a GitHub action on a version tag in a read-only job, or no Dependabot for actions. |

## These are not findings

- `github.event.pull_request.number`, `github.event.issue.number`, `github.sha`,
  `github.run_id` and `github.repository` in `run:`.
- `secrets.*` in a `pull_request` workflow. A fork gets empty values.
- `pull_request_target` that does not check out, build or run code from the pull
  request, and that does not put event text into scripts.
- `workflow_dispatch` inputs in `run:` when only users with write access can start
  the workflow. Report it as low, not higher.
- A `permissions:` block that is stricter than needed.

## Finding format

For each finding, give:

- **Title** and **severity** (critical, high, medium or low)
- **Location**: `file:line`
- **Attacker and path**: who can do it, and how, in two or three sentences
- **Impact**: what the attacker gets
- **Fix**: the smallest change, as YAML
- **ID**: the OWASP CI/CD risk and, if useful, the CWE

Start the report with one to three lines that give the result. Order the findings
from critical to low. If you find nothing, say "No findings", and list what you
checked. That is a valid result.

If your tool can start a separate agent with a fresh context, give it each critical
or high finding, and let it confirm or reject the finding. If not, check each one
again yourself against the list "These are not findings".

## OWASP Top 10 CI/CD Security Risks

| ID | Name | Typical workflow finding |
| --- | --- | --- |
| CICD-SEC-1 | Insufficient Flow Control Mechanisms | A release or deploy without required reviewers or protected tags |
| CICD-SEC-2 | Inadequate Identity and Access Management | Broad personal access tokens, broad OIDC trust policies |
| CICD-SEC-3 | Dependency Chain Abuse | Actions on tags, no checksum for downloads |
| CICD-SEC-4 | Poisoned Pipeline Execution | A pwn request, expression injection |
| CICD-SEC-5 | Insufficient PBAC (Pipeline-Based Access Controls) | Write scopes for all jobs, `secrets: inherit` |
| CICD-SEC-6 | Insufficient Credential Hygiene | Secrets in arguments, logs or artifacts, long-lived keys |
| CICD-SEC-7 | Insecure System Configuration | Self-hosted runners for public repositories |
| CICD-SEC-8 | Ungoverned Usage of 3rd Party Services | Apps and actions with more access than they need |
| CICD-SEC-9 | Improper Artifact Integrity Validation | No provenance or signatures for releases |
| CICD-SEC-10 | Insufficient Logging and Visibility | No audit of who changed workflows or secrets |

## zizmor audit names

If the project runs zizmor, its findings use these names. They can help you
connect your finding to a zizmor result: `template-injection`, `dangerous-triggers`,
`excessive-permissions`, `unpinned-uses`, `impostor-commit`, `artipacked`,
`cache-poisoning`, `github-env`, `secrets-inherit`, `overprovisioned-secrets`,
`self-hosted-runner`, `bot-conditions`, `dependabot-cooldown`,
`use-trusted-publishing`.
