# Injection

Load this file when a `run:`, a `script:` or a composite action uses event data or
inputs, or when a step writes to `GITHUB_ENV`, `GITHUB_OUTPUT` or `GITHUB_PATH`.

## How expression injection works

GitHub replaces each `${{ }}` expression with its value before the shell or the
JavaScript runtime reads the script. The value becomes part of the code. A quote,
a backtick or `$(...)` in the value can end a string and start a command.

Unsafe:

```yaml
- run: echo "New issue: ${{ github.event.issue.title }}"
```

Safe:

```yaml
- env:
    TITLE: ${{ github.event.issue.title }}
  run: echo "New issue: $TITLE"
```

The shell reads `$TITLE` as data. Always put the variable in double quotes.

## Values that an attacker can set

GitHub Docs give this rule: a context field is untrusted if its name ends in
`body`, `default_branch`, `email`, `head_ref`, `label`, `message`, `name`,
`page_name`, `ref` or `title`. Examples:

- `github.event.issue.title`, `github.event.issue.body`
- `github.event.pull_request.title`, `github.event.pull_request.body`
- `github.event.comment.body`, `github.event.review.body`
- `github.head_ref`, `github.event.pull_request.head.ref`,
  `github.event.pull_request.head.label`
- `github.event.head_commit.message`, `github.event.head_commit.author.email`,
  `github.event.commits[*].message`
- `github.event.workflow_run.head_branch`

Treat these as text too, also when only users with write access can set them:

- `inputs.*` of `workflow_dispatch`, `workflow_call` and composite actions
- `github.event.release.tag_name`, `github.event.release.name`, `github.ref_name`
- `steps.*.outputs.*` and `needs.*.outputs.*` that come from any value above

## Values that are not injection

These values cannot contain shell syntax. Do not report them:

- `github.event.pull_request.number`, `github.event.issue.number`
- `github.sha`, `github.event.pull_request.head.sha`
- `github.run_id`, `github.run_number`, `github.run_attempt`
- `github.repository`, `github.event_name`, `github.workflow`

The rule "pass through `env:`" is still good style for them, but a missing `env:`
is not a finding.

## actions/github-script

The `script:` input is JavaScript code, so the same problem applies. Read the
value from `context.payload` or from `process.env`:

```yaml
- uses: actions/github-script@<SHA> # v7.0.1
  env:
    TITLE: ${{ github.event.issue.title }}
  with:
    script: |
      const title = process.env.TITLE;
```

## Composite actions and reusable workflows

In a composite action, `${{ inputs.name }}` in `run:` is also replaced before the
shell runs. The caller can pass attacker text. Map each input to `env:` in the
step.

## Argument injection

A value that starts with `-` can become an option of the command. Branch names can
start with `-`. Mark the end of the options before an untrusted argument. Git uses
`--end-of-options` before a revision. Many other tools use `--`:

```yaml
- env:
    BRANCH: ${{ github.head_ref }}
  run: git log --oneline --end-of-options "$BRANCH"
```

## GITHUB_ENV, GITHUB_OUTPUT and GITHUB_PATH

These files set variables and paths for later steps. Each line sets one value.

- In the form `NAME=value`, a line break in the value starts a new line, and that
  line can set a new variable.
- In the form `NAME<<DELIMITER`, the value ends at the first line that equals the
  delimiter. If the text contains that line, the lines after it set new variables.

A variable such as `LD_PRELOAD`, or a new entry in `PATH`, can make a later step run
code that the attacker chose.

- Do not write untrusted text to `GITHUB_ENV` or `GITHUB_PATH`.
- Pass untrusted data to later steps as a file, for example in `runner.temp`.
- If you must write a multi-line value to `GITHUB_OUTPUT`, use a random delimiter
  that the text cannot contain:

```yaml
- run: |
    delimiter="$(openssl rand -hex 16)"
    {
      echo "summary<<$delimiter"
      cat "$RUNNER_TEMP/summary.md"
      echo "$delimiter"
    } >> "$GITHUB_OUTPUT"
```

A fixed delimiter such as `EOF` is not safe, because the text can contain it.

## Text in comments

A comment that a workflow posts can show user text, for example a title. The text
can contain `@` mentions and links, and the bot account posts them. Put user text
in a code span or a quote block, and limit its length.
