# Language models and agents in workflows

Load this file when a step sends repository, issue or pull request text to a
language model or an agent.

## The risk

Text in an issue, a comment, a pull request or a file in a pull request can contain
instructions for the model ("prompt injection"). The model cannot reliably tell
your instructions from the attacker's. So give the model step only the power that
you accept an attacker to have.

## Rules

1. **Read-only model step.** The job that calls the model has no write scope in
   `permissions:`, or `permissions: {}`. The only secret in it is the model API key,
   in the `env:` of the step that calls the model.
2. **Data, not code.** Pass the untrusted text through `env:` or a file. Do not
   put it in `${{ }}` in `run:` (see [injection.md](injection.md)).
3. **No tools for untrusted input.** Do not give the model shell access, file
   writes or a GitHub token when it reads text from outsiders. If an agent needs
   tools, run it only for trusted users and only on trusted code.
4. **Structured output.** Ask for output in a fixed format, for example JSON with
   a list of labels. Treat the output as untrusted too.
5. **A separate job applies the result.** This job has the write scope (for
   example `issues: write`). It does not call the model. It parses the output,
   keeps only values from a fixed allow-list, and applies them with fixed commands.
6. **No secrets in the prompt.** Do not send secrets, tokens or private data that
   the issue author must not see. The model output can contain anything that was
   in the prompt.
7. **Limits.** Set a timeout and a maximum size for the input and the output, so
   that a long issue cannot make the run slow or expensive.

## Shape of a summary workflow

This workflow asks a model for a short summary of a new issue and posts it as a
comment. Replace each `<SHA>` with the real commit SHA of the action.

```yaml
on:
  issues:
    types: [opened]
permissions: {}
jobs:
  summarize:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@<SHA> # v4
        with:
          persist-credentials: false
      - env:
          LLM_TOKEN: ${{ secrets.LLM_TOKEN }}
          ISSUE_TITLE: ${{ github.event.issue.title }}
          ISSUE_BODY: ${{ github.event.issue.body }}
        run: ./scripts/summarize.sh > "$RUNNER_TEMP/summary.txt"
      - uses: actions/upload-artifact@<SHA> # v4
        with:
          name: summary
          path: ${{ runner.temp }}/summary.txt
  comment:
    needs: summarize
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - uses: actions/download-artifact@<SHA> # v4
        with:
          name: summary
          path: ${{ runner.temp }}/in
      - env:
          GH_TOKEN: ${{ github.token }}
          ISSUE: ${{ github.event.issue.number }}
        run: |
          head -c 2000 "$RUNNER_TEMP/in/summary.txt" > "$RUNNER_TEMP/body.txt"
          gh issue comment "$ISSUE" --repo "$GITHUB_REPOSITORY" --body-file "$RUNNER_TEMP/body.txt"
```

- The `summarize` job has the model key but no write token. The `comment` job has
  the write token but does not call the model.
- The script `summarize.sh` comes from the default branch, not from the issue.
- The comment shows model output to everyone. The output can contain links or
  mentions that the issue author chose. Limit the length, and tell the user about
  this risk.
- When the result is a choice, such as labels, the `comment` job accepts only
  values from a fixed list and ignores all other text.
