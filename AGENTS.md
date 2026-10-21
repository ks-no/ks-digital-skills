# AGENTS.md

Guidance for AI agents working in this repository.

## What this is

KS Digital Skills is a public, MIT-licensed collection of skills for AI agents,
packaged as Claude Code and Codex plugin marketplaces. Each skill is its own plugin
under `plugins/`: a `plugins/<name>/.claude-plugin/plugin.json` manifest, a
`plugins/<name>/.codex-plugin/plugin.json` manifest, plus the skill itself at
`plugins/<name>/skills/<name>/SKILL.md`. In Claude Code the repo is added with
`/plugin marketplace add ks-no/ks-digital-skills`. In Codex the repo can be added as
a plugin marketplace. Other tools (GitHub Copilot, OpenCode, Pi) use a copy or a
symlink of the skill directory. See `README.md` for installation details.

## Structure

```text
.claude-plugin/marketplace.json      # Claude Code marketplace
.agents/plugins/marketplace.json     # Codex marketplace
plugins/<skill-name>/
├── .claude-plugin/plugin.json       # Claude Code plugin manifest
├── .codex-plugin/plugin.json        # Codex plugin manifest
└── skills/<skill-name>/
    ├── SKILL.md                     # required, with frontmatter
    └── references/                  # optional supporting files
scripts/validate.py                  # repository validation
evals/cases.json                     # held-out test texts for the AI-marker rules, security skills and universell-utforming
evals/run.py                         # runs the test texts through a model
.github/workflows/validate.yml       # CI: runs validate.py and zizmor
.github/dependabot.yml               # updates the pinned actions
.github/CODEOWNERS                   # maintainers who review each pull request
README.md                            # overview and installation (Norwegian)
CONTRIBUTING.md                      # how to contribute, and the GitHub settings (Norwegian)
SECURITY.md                          # how to report a vulnerability (Norwegian)
```

## Creating or editing a skill

- A skill is a plugin under `plugins/<name>/` with `.claude-plugin/plugin.json` and
  `.codex-plugin/plugin.json` manifests, plus the skill at `skills/<name>/SKILL.md`.
  Copy an existing plugin as a starting point.
- `SKILL.md` must start with frontmatter that has `name` and `description`:

  ```md
  ---
  name: my-skill
  description: Use this skill when ...
  ---

  # My Skill
  ```

- `name` uses lowercase letters, digits and single hyphens, and is 64 characters or
  fewer. It **must be identical** across the plugin directory, both `plugin.json`
  manifests, the `SKILL.md` frontmatter, and both marketplace entries.
- `description` is 1024 characters or fewer. It should concretely describe when the
  skill applies (trigger phrases), since tools use it to decide whether the skill is
  relevant.
- Relative paths inside a `SKILL.md` are resolved against the skill directory. Refer
  to another skill by its name, not by a path, because each skill can be installed
  alone.
- Skills must be harness-agnostic. Do not hardcode paths, commands, or concepts that
  only exist in one tool, such as Claude Code, GitHub Copilot, Codex, OpenCode, or
  Pi. Harness-specific packaging belongs in plugin manifests and marketplace files,
  not in `SKILL.md` instructions.
- A plugin contains skills only. Do not add MCP servers, LSP servers or hooks: no
  `.mcp.json`, `.lsp.json` or `hooks/hooks.json`, and no `mcpServers`, `lspServers` or
  `hooks` key in a manifest or a marketplace entry. The tool can start these outside
  the sandbox that the agent's commands run in.
- A skill must not tell the agent or the user to install tools for the agent, add tool
  servers, or change sandbox or permission settings. A skill can suggest a dependency
  for the project itself, such as a test framework. The agent adds it only when the
  user asks. If a restriction, such as the sandbox or a permission, can stop a command
  that the skill runs, the skill tells the agent to report the restriction and stop.
- Add the plugin to `.claude-plugin/marketplace.json` (with `source`
  `./plugins/<name>`), add it to `.agents/plugins/marketplace.json` (with
  `source.path` `./plugins/<name>`), and add a row to the `## Skills` table in
  `README.md`.

## This repository is public

- Do not add internal URLs or hostnames, Jira keys, internal repository or channel
  names, personal data beyond author names, secrets, or unpublished product details.
- Public names of KS and Fiks products and of national services (Fiks-porten,
  ID-porten, Altinn and similar) are fine.
- Keep third-party license texts next to the content they cover, in files named
  `LICENSE*`, and credit the source in the skill.
- ASD-STE100 is free to get but not free to redistribute. Never add the ASD
  dictionary, word lists taken from it, or verbatim text from the standard.
  Paraphrase the rules and cite rule numbers.
- The OWASP lists, Cheat Sheets and ASVS are CC BY-SA, and the OWASP Kubernetes
  Top 10 is CC BY-NC-SA. Do not copy their text. Cite IDs and names only.
- `universell-utforming` uses a checklist from UX Norge. The checklist states no
  license. The W3C WAI pages and WCAG are under the W3C Document License, which does
  not permit changed copies. Restate the content of the checklist, the WAI pages and
  WCAG in new words, and credit each source. Give WCAG success criteria by number only.
- Security skills are generic. Do not describe the setup, tools or findings of KS
  Digital or of any other organization.

## Conventions

- `README.md` is written in Norwegian. Skill files may be written in English when
  that is better for agent consumption. Preserve a skill's existing language when
  editing.
- No long dash (em dash, U+2014) in any text file, also not as a JSON `\u2014`
  escape. Use a comma, colon, full stop or parentheses. Files named `LICENSE*` are
  exempt.
- No trailing whitespace in markdown files, and markdown files must not be empty.
- All text files are UTF-8.
- Follow the style of existing `SKILL.md` files for tone and structure.

## Testing a rule change

`validate.py` checks structure, not behaviour. When you change a rule that tells an
agent how to rewrite text, run the rule with an agent before and after the change.
For the AI-marker rules in `asd-ste100-english` and `norsk-sprakvask`, use the test
texts in `evals/`. `evals/README.md` tells how to run them and how to add a text. A
new rule or exception gets at least one new text, with words that are not in any
skill. Do not copy a sentence from a test text into a skill.

For a security skill and for `universell-utforming`, use its cases in
`evals/cases.json`. Run each case without the skill and with the skill, on a strong
model and on a weaker model that people use. Grade the answers blind. A change must not
make an answer longer or stop a workflow or program from working. `evals/README.md`
tells how.

Do not put the examples of a test text in a skill either: its code patterns, field
names or values. When a test result leads to a new rule, write the rule in general
words, and check it on a new text that uses other examples.

## Validation

Run validation after every change:

```sh
python3 scripts/validate.py
```

It needs only Python 3. It checks that:

- each plugin has both manifests and a `skills/<name>/SKILL.md` with closed
  frontmatter, a valid `name` and a `description` of 1024 characters or fewer,
- `name` matches across the directory, both manifests and `SKILL.md`,
- `version` matches across both manifests and the Claude Code marketplace entry,
- no plugin or marketplace entry brings MCP servers, LSP servers or hooks,
- both marketplaces list exactly the plugin directories with the right source paths,
- every plugin is in the README `## Skills` section,
- relative links in markdown files under `plugins/` point to files that exist,
- `SKILL.md` files do not contain obvious harness-specific paths,
- no text file contains U+2014, except files named `LICENSE*`,
- markdown files are not empty and have no trailing whitespace,
- every text file is valid UTF-8,
- each case in `evals/cases.json` has an `id`, a `type`, a `text` and a `pass`,
  the IDs are unique, each path in a `files` list exists, and no skill file
  contains a sentence from a case.

CI runs the same script, and zizmor on the workflows, on every push to `main`, on every
pull request and once a week.

## Workflows and GitHub settings

- A workflow in this repo uses no secrets, has `permissions: contents: read`, and has no
  `pull_request_target` or `workflow_run` trigger.
- Pin each action to a full commit SHA, with the version tag in a comment. Set
  `persist-credentials: false` on each checkout.
- Do not change the version of an action by hand. Dependabot changes it when the new
  version is at least 7 days old. When you add a new action, select a version that
  GitHub released at least 7 days before. An action that is not from GitHub, ks-no or a
  verified creator must also be in the allow list in `CONTRIBUTING.md`.
- Dependabot makes no security updates for an action that is pinned to a SHA. zizmor in
  the `validate` job finds the advisories. For an action with an advisory, a maintainer
  changes the version at once. `CONTRIBUTING.md` (Sikkerhetsfikser) tells how.
- `CONTRIBUTING.md` records the GitHub settings, such as the rulesets. Nothing in the
  repo can check them. If a change affects a setting, update `CONTRIBUTING.md` in the
  same pull request. For example, the ruleset for `main` requires the job `validate` by
  its name.

## Before you finish

- Run `python3 scripts/validate.py` and confirm that it prints `OK`.
- Update `README.md` if skills were added, removed, or renamed.
- If you changed a plugin, raise its `version` in both `plugin.json` manifests and
  in its entry in `.claude-plugin/marketplace.json`. Claude Code stores each
  installed plugin by version, so users do not get a change until the version
  changes.
- Do not commit secrets or local config files (see `.gitignore`).
