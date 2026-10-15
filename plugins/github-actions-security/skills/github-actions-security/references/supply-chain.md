# Supply chain

Load this file when you add or update an action or a reusable workflow, pin
versions, configure Dependabot, or publish a release.

## Why tags are not enough

A tag such as `v4` can move to another commit. If an attacker gets write access to
an action, they can move its tags to malicious code. Each workflow that uses the
tag then runs that code with its own token and secrets. In March 2025 this
happened to `tj-actions/changed-files` (CVE-2025-30066). The new code printed
secrets to the build logs. Workflows that pinned a full commit SHA did not run it.

## Pin to a full commit SHA

- Use the full 40-character SHA. A short SHA can match more than one commit.
- Write the version in a comment, so that people and Dependabot can read it:
  `uses: actions/checkout@<SHA> # v4.2.2`.
- Get the SHA from the repository of the action:
  `git ls-remote --tags https://github.com/OWNER/REPO vX.Y.Z`. An annotated tag
  gives two lines. Use the SHA on the line that ends in `^{}`.
- Do not take a SHA from a fork. GitHub can resolve a commit from a fork through
  the parent repository (an "impostor commit"). The SHA must be reachable from a
  tag or a branch in the repository of the action.
- Do not invent a SHA. If you cannot look it up, keep the version tag and tell the
  user to pin it.
- Pin reusable workflows the same way:
  `uses: OWNER/REPO/.github/workflows/build.yml@<SHA>`.
- Pin container images by digest: `image: name@sha256:<digest>`.

## Workflow dependency lockfiles

GitHub has a lockfile for workflow dependencies,
`.github/workflows/actions.lock`. It records the commit of each action, also of
actions that other actions use. It is in public preview. If the repository already
has the file, keep it current with the command that the project documents. Do not
edit it by hand. If the repository does not have it, pin SHAs.

## Keep pins current

- A SHA pin does not get Dependabot security alerts. Use Dependabot version
  updates for the `github-actions` ecosystem, which update the SHA and the comment.
- A `cooldown` delays new versions for some days, so that the community can find a
  compromised release first:

```yaml
version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
    cooldown:
      default-days: 7
```

- Do not set `insecure-external-code-execution: allow` in a Dependabot
  configuration.

## Choosing an action

- Prefer actions from GitHub (`actions/*`, `github/*`) and from the vendor of the
  tool that the action wraps.
- Prefer a few lines of `run:` to an action that does a small job, for example
  `gh pr comment` instead of an action that posts a comment.
- Read what an action does with the token and the secrets before you give them
  to it.
- An organization or repository policy can allow only listed actions, block
  named actions and require SHA pins. Suggest it to the user. Do not change it.

## Tools that steps download

- Do not pipe a download into a shell (`curl ... | sh`) without a checksum check.
- Pin the version of each tool. Check the checksum or the signature that the
  vendor publishes.
- Install dependencies from the lock file (`npm ci`, `pip install --require-hashes`,
  `dotnet restore --locked-mode`).

## Release integrity

- Protect release tags with a ruleset, so that nobody can move or delete them.
- Build the release in a clean job from a pinned commit. Do not restore a cache.
- Create build provenance, for example with an artifact attestation
  (`actions/attest-build-provenance`) or the provenance that the registry makes.
- Sign the packages if the registry or the users check signatures. Keep the
  signing key in an environment with required reviewers, or use keyless signing
  with OIDC.
