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
README.md                            # overview and installation (Norwegian)
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

## Validation

Run validation after every change:

```sh
python3 scripts/validate.py
```

It needs only Python 3. It checks that:

- each plugin has both manifests and a `skills/<name>/SKILL.md` with closed
  frontmatter, a valid `name` and a `description` of 1024 characters or fewer,
- `name` matches across the directory, both manifests and `SKILL.md`,
- both marketplaces list exactly the plugin directories with the right source paths,
- every plugin is in the README `## Skills` section,
- relative links in markdown files under `plugins/` point to files that exist,
- `SKILL.md` files do not contain obvious harness-specific paths,
- no text file contains U+2014, except files named `LICENSE*`,
- markdown files are not empty and have no trailing whitespace,
- every text file is valid UTF-8.

CI runs the same script on every push to `main` and on every pull request.

## Before you finish

- Run `python3 scripts/validate.py` and confirm that it prints `OK`.
- Update `README.md` if skills were added, removed, or renamed.
- Do not commit secrets or local config files (see `.gitignore`).
