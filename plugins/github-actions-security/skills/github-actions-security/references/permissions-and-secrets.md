# Permissions and secrets

Load this file when a workflow uses secrets, OIDC, an environment or a GitHub App
token, or when it publishes, signs or deploys.

## GITHUB_TOKEN permissions

- Set `permissions:` at the top of each workflow. Use `contents: read`, or `{}`
  when no job needs the repository.
- Give write scopes per job. A job-level block replaces the top-level block. It
  does not add to it.
- A scope that you do not list is `none` when a `permissions:` block exists.

| Task | Scope |
| --- | --- |
| Check out the repository | `contents: read` |
| Push commits or tags, create a release | `contents: write` |
| Comment on, label or edit a pull request | `pull-requests: write` |
| Comment on or label an issue | `issues: write` |
| Push to GitHub Packages or GHCR | `packages: write` |
| Download an artifact from another run | `actions: read` |
| Get an OIDC token | `id-token: write` |
| Create an artifact attestation | `attestations: write` and `id-token: write` |
| Upload code scanning results | `security-events: write` |

Suggest to the user that the repository or organization default for workflow
permissions is "read". Do not change the setting yourself.

## Secrets

- Give a secret to the one step that uses it, through `env:`. Do not set it at
  the workflow or job level.
- Do not put a secret in a command argument or a URL. Logs and error messages can
  show them. Use standard input (for example `--password-stdin`), an environment
  variable or a file in `runner.temp`.
- Pass signing keys and passwords through `env:`, not through `${{ }}` in the
  script text.
- GitHub masks the exact value of a secret in logs. It does not mask a value that
  a step derives from the secret, for example a Base64 form or a token from an API.
  Mask it with `echo "::add-mask::$VALUE"` before you use it.
- Do not store JSON or YAML as one secret. Masking works on the whole value, not on
  the parts. Make one secret for each value.
- Do not use `toJSON(secrets)`. It gives all secrets to one step.
- `secrets: inherit` gives all secrets of the caller to a reusable workflow. Use it
  only for a workflow that you control and pin. Else pass named secrets.
- If a secret shows in a log, delete the log and rotate the secret.

## Environments

- Put deploy secrets in an environment with required reviewers.
- The deployment rules of an environment can allow branches and tags. A rule that
  allows only `main` blocks a job that a tag starts. Add the tag pattern, for
  example `v*`, when a release tag starts the deploy.

## OIDC instead of stored keys

- Use OIDC for cloud providers and registries that support it. The job then gets a
  short-lived token, and the repository stores no long-lived key.
- Give `id-token: write` only to the job that needs it.
- The trust policy in the cloud must check the `sub` claim. Allow one repository
  and one environment or one ref, for example
  `repo:OWNER/REPO:environment:production`. Do not use a wildcard for the
  repository or the organization.

## Publishing packages

- **npm:** use trusted publishing. It needs npm CLI 11.5.1 or later, Node
  22.14.0 or later and a GitHub-hosted runner. The publish job needs
  `id-token: write`, and it needs no npm token. npm adds provenance for a public
  package from a public repository. If the user cannot use trusted publishing, use
  a granular access token that can publish only this package.
- **PyPI:** use trusted publishing with `id-token: write` in the publish job.
- **Other registries:** use the shortest-lived and narrowest credential that the
  registry offers. Give it only to the publish step.
- Run the tests in a job before the publish job. The publish job does not run code
  from a pull request and does not restore a cache.

## GitHub App tokens and personal access tokens

- Prefer a GitHub App installation token to a personal access token. Limit it to
  the repositories and permissions that the job needs.
- An event that the `GITHUB_TOKEN` causes does not start new workflows. This stops
  loops. A personal access token or an App token does start them, so check that
  the workflow cannot start itself without end.
