# KS Digital Skills

Åpne skills for AI-agenter fra KS Digital. En skill er en mappe med instruksjoner
(`SKILL.md`) som agenten leser når oppgaven passer, for eksempel når den skriver norsk
tekst eller en feilmelding som ikke skal kunne misforstås.

Skillene er skrevet uten stier eller kommandoer som bare finnes i ett verktøy. De kan
brukes i GitHub Copilot, Claude Code, Codex, OpenCode og Pi.

Repoet er nytt. Innhold og struktur kan endre seg.

## Skills

| Skill | Kategori | Hva den gjør |
| --- | --- | --- |
| `norsk-sprakvask` | skriving | skriv og språkvask norsk bokmål etter Språkrådets normer og klarspråksrådene, og fanger engelsk smitte, inkonsekvente former, særskriving og KI-preg |
| `asd-ste100-norsk` | skriving | skriv norsk teknisk tekst som ikke kan misforstås, etter prinsippene i ASD-STE100 tilpasset norsk grammatikk |
| `asd-ste100-english` | skriving | skriv engelsk etter ASD-STE100 (Simplified Technical English), så verktøybeskrivelser, feilmeldinger og instruksjoner ikke kan misforstås av en agent eller en leser |

`asd-ste100-norsk` er laget for å brukes sammen med `norsk-sprakvask`. Den første tar
setningsbygningen, og den andre tar rettskriving, tegnsetting og ordvalg. Installer
begge.

## Installer

### Claude Code

Legg til repoet som plugin-marketplace, og installer de skillene du vil ha:

```text
/plugin marketplace add ks-no/ks-digital-skills
/plugin install norsk-sprakvask@ks-digital-skills
```

- `/plugin` viser alle plugins i marketplacen.
- Start en ny økt etterpå. Plugins lastes ved oppstart.
- Hent nye versjoner med `/plugin marketplace update ks-digital-skills`.

### Codex

Repoet har en Codex-marketplace i `.agents/plugins/marketplace.json`:

```sh
git clone https://github.com/ks-no/ks-digital-skills.git
cd ks-digital-skills
codex plugin marketplace add .
```

### GitHub Copilot, OpenCode, Pi og andre verktøy

Kopier skill-mappen til mappen der verktøyet leter etter skills:

| Verktøy | Personlig skill-mappe | Skill-mappe i et prosjekt |
| --- | --- | --- |
| GitHub Copilot | `~/.copilot/skills` | `.github/skills` |
| Claude Code | `~/.claude/skills` | `.claude/skills` |
| Codex | `~/.agents/skills` | `.agents/skills` |
| OpenCode | `~/.config/opencode/skills` | `.opencode/skills` |
| Pi | `~/.pi/agent/skills` | `.pi/agent/skills` |

macOS og Linux:

```sh
git clone https://github.com/ks-no/ks-digital-skills.git
mkdir -p ~/.copilot/skills
cp -R ks-digital-skills/plugins/norsk-sprakvask/skills/norsk-sprakvask ~/.copilot/skills/
```

Windows (PowerShell):

```powershell
git clone https://github.com/ks-no/ks-digital-skills.git
New-Item -ItemType Directory -Force "$HOME\.copilot\skills"
Copy-Item -Recurse ks-digital-skills\plugins\norsk-sprakvask\skills\norsk-sprakvask "$HOME\.copilot\skills\"
```

Vil du at endringer følger med når du kjører `git pull`, kan du lage en symlink i
stedet for en kopi:

```sh
ln -s "$PWD/ks-digital-skills/plugins/norsk-sprakvask/skills/norsk-sprakvask" ~/.copilot/skills/norsk-sprakvask
```

På Windows krever symlinker utviklermodus eller administratorrettigheter, så der er
kopi enklest. I Pi kjører du `/reload` eller starter Pi på nytt etter at du har
installert en skill.

## Legg til en skill

Hver skill er en egen plugin under `plugins/`:

```text
plugins/min-skill/
├── .claude-plugin/plugin.json
├── .codex-plugin/plugin.json
└── skills/min-skill/
    ├── SKILL.md
    └── references/
```

- `SKILL.md` begynner med frontmatter med `name` og `description`. `name` skal være
  lik mappenavnet, og det samme navnet står i begge `plugin.json`-filene og i begge
  marketplace-filene.
- Legg plugin-en til i `.claude-plugin/marketplace.json`,
  `.agents/plugins/marketplace.json` og i tabellen over.
- Skriv skillen uten stier, kommandoer eller begreper som bare finnes i ett verktøy.
- Repoet er offentlig. Ikke ta med interne adresser, Jira-nøkler, personopplysninger
  eller hemmeligheter.

Kjør valideringen før du lager en pull request:

```sh
python3 scripts/validate.py
```

Valideringen sjekker at navnene stemmer, at marketplace-filene og README er i synk, at
lenkene i skillene virker, og at ingen tekstfil har lang bindestrek (U+2014). CI kjører
den samme sjekken. Alle reglene står i [AGENTS.md](AGENTS.md).

## Lisens

MIT, se [LICENSE](LICENSE).

`asd-ste100-english` og `asd-ste100-norsk` bygger på
[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) (MIT), og
lisensteksten står i skill-mappene. Skillene er ikke utgitt eller godkjent av ASD
eller Språkrådet, og de inneholder ikke ordlisten i ASD-STE100.
