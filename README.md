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
| `polish` | produktivitet | rydd opp i, språkvask, sjekk universell utforming og gå gjennom branchen, også for sikkerhet, i runder til sjekken passerer og en runde ikke finner flere feil, og avslutt alltid med en gjennomgang |
| `guided-click-through` | testing | test oppførselen til en endring i grensesnittet med komponenttestene i prosjektet, og lag en kort sjekkliste som brukeren klikker gjennom for det testene ikke ser, som layout, stil og synlig fokus |
| `github-actions-security` | sikkerhet | skriv og gå gjennom workflowene i GitHub Actions med regler for risikoene i OWASP Top 10 og OWASP Top 10 CI/CD Security Risks, så tekst, kode og artefakter fra forks, issues og kommentarer ikke når tokenet og secretene |
| `secure-coding` | sikkerhet | skriv og gå gjennom applikasjonskode i Java, Kotlin, C#, Python og TypeScript med regler for risikoene i OWASP Top 10, OWASP API Security Top 10 og OWASP Top 10 for LLM Applications, også for Maskinporten og ID-porten, uten ekstra kode og uten falske funn |
| `container-security` | sikkerhet | skriv og gå gjennom Dockerfiler, Helm-charts og manifester for Kubernetes og OpenShift med regler for risikoene i OWASP Top 10 og OWASP Kubernetes Top 10, uten gjetteverdier som stopper arbeidslasten, og uten kommandoer som viser secrets |
| `universell-utforming` | testing | sjekk hver endring i grensesnittet mot kravene til universell utforming og suksesskriteriene i WCAG som forskriften krever, planlegg brukertester med personer med funksjonsnedsettelser etter sjekklisten til Frank Dahle (Digdir) i UX Norge, og gjør notatene om til funn og rettelser i koden |

`asd-ste100-norsk` er laget for å brukes sammen med `norsk-sprakvask`. Den første tar
setningsbygningen, og den andre tar rettskriving, tegnsetting og ordvalg. Installer
begge.

`polish` bruker de tre språkskillene i språkvasken, `universell-utforming` på koden for
grensesnittet og de tre sikkerhetsskillene i gjennomgangen. Hver sikkerhetsskill går
bare gjennom filene den gjelder for. En hindring som bryter et suksesskriterium som
gjelder, er et funn som betyr noe, med mindre kravene til prosjektet sier at universell
utforming ikke gjelder. Da retter `polish` hindringen som en kosmetisk endring. Er en av
skillene ikke installert, hopper `polish` over den skillen og sier fra i rapporten.
Endrer branchen grensesnittet og prosjektet har komponenttester, skriver `polish` tester
for oppførselen med `guided-click-through` før første runde. Rapporten slutter med en
sjekkliste fra samme skill når testene ikke viser alt, eller når et valg er lettere å ta
i appen.

`guided-click-through` starter ikke appen og bruker ingen nettleser. Har prosjektet
komponenttester, tester agenten oppførselen selv. Mangler prosjektet slike tester,
foreslår agenten å legge dem til, men gjør det bare når du ber om det. Deretter skriver
den steg for det testene ikke ser, og du klikker gjennom i appen slik du pleier. Du
svarer «ok» eller oppgir stegene som feilet, og agenten retter dem. Er et valg lettere
å ta når du ser appen, kan sjekklisten også be deg velge mellom to eller tre løsninger.

`universell-utforming` sjekker hver endring i grensesnittet mot kravene til universell
utforming, med suksesskriteriene i WCAG 2.1 som forskriften krever av offentlige
virksomheter. Agenten retter hindringene med så små endringer som mulig og melder ikke
mønstre som er riktige. En sjekk av koden finner ikke alt, så agenten sier ikke at
løsningen oppfyller kravene.

Skillen hjelper også teamet å teste med personer som bruker hjelpemidler: agenten lager
plan, invitasjon og samtykketekst, og går gjennom notatene etterpå. Agenten skiller det
deltakeren gjorde, fra det testlederen konkluderte, og lager rettelser med tester.
Agenten rekrutterer ikke deltakere og ser ikke øktene. Det gjør teamet.

Skriv linjen for `universell-utforming` i `AGENTS.md` i prosjektet, så sjekker agenten
hver endring i grensesnittet. Se [Linjer i AGENTS.md](#linjer-i-agentsmd).

**Merk: ingen fagperson har gått gjennom `universell-utforming`.** En KI-agent skrev
skillen ut fra offentlige kilder: sjekklisten i UX Norge, Uutilsynet, W3C, WebAIM og
GOV.UK. KI-agenter gikk gjennom skillen mot kildene og mot Designsystemet og Aksel, og
vurderte svarene i testene. Ingen person med fagkunnskap om
universell utforming har kontrollert reglene eller resultatene.

- Bruk skillen som en hjelp til å finne og rette hindringer, ikke som bevis for at en
  løsning oppfyller kravene.
- Kravene står i forskriften, og Uutilsynet fører tilsyn med dem. Sjekk viktige valg på
  uutilsynet.no, og med en fagperson når du kan.
- Har du fagkunnskap og ser en feil, si fra i en issue.

### Sikkerhet

Sikkerhetsskillene hjelper agenten å unngå svakhetene i listene fra OWASP som
tabellen over nevner for hver skill. Skillene er generelle. De bygger på offentlige
kilder og inneholder ingen opplysninger om interne systemer.

- Bruk en sterk modell når du ber om en sikkerhetsgjennomgang. Kjernereglene står i
  `SKILL.md`, så også en mindre modell får det viktigste.
- Skriv linjene for sikkerhetsskillene i `AGENTS.md` i prosjektet. Se
  [Linjer i AGENTS.md](#linjer-i-agentsmd).

### Linjer i AGENTS.md

Agenten leser instruksjonsfilen til prosjektet hver gang, men en skill bare når den
velger den selv. Skriv derfor linjene for skillene du bruker, i `AGENTS.md` i
prosjektet:

```text
Before you write, change or review a user interface, use the skill universell-utforming.
Before you write, change or review code, use the skill secure-coding.
Before you create or change a GitHub Actions workflow, use the skill github-actions-security.
Before you create, change or review a Dockerfile, a Helm chart or a Kubernetes or OpenShift manifest, or run oc, kubectl or helm, use the skill container-security.
```

Codex, Copilot og OpenCode leser `AGENTS.md`. Claude Code leser `AGENTS.md` fra versjon
2.1.277, men bare når det ikke finnes en `CLAUDE.md` eller `CLAUDE.local.md` i
prosjektmappen eller i en mappe over den. Skriv `@AGENTS.md` på en egen linje i
`CLAUDE.md` hvis

- prosjektet allerede har en `CLAUDE.md`
- noen i teamet har en `CLAUDE.local.md`
- noen i teamet bruker en eldre versjon av Claude Code

Da leser Claude Code `AGENTS.md` i alle tilfellene, og aldri to ganger. Se
[dokumentasjonen til Claude Code](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools).

## Installer

### Claude Code

Legg til repoet som plugin-marketplace, og installer de skillene du vil ha:

```text
/plugin marketplace add ks-no/ks-digital-skills
/plugin install norsk-sprakvask@ks-digital-skills
```

- `/plugin` viser alle plugins i marketplacen.
- Start en ny session etterpå. Plugins lastes ved oppstart.
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
- En plugin inneholder bare skills. Den tar ikke med MCP-servere, LSP-servere eller
  hooks, fordi verktøyet kan starte dem utenfor sandboxen.
- Repoet er offentlig. Ikke ta med interne adresser, Jira-nøkler, personopplysninger
  eller hemmeligheter.

Kjør valideringen før du lager en pull request:

```sh
python3 scripts/validate.py
```

Valideringen sjekker at navnene stemmer, at marketplace-filene og README er i synk, at
lenkene i skillene virker, at ingen plugin tar med MCP-servere, LSP-servere eller
hooks, og at ingen tekstfil har lang bindestrek (U+2014). CI kjører den samme sjekken.
Alle reglene står i [AGENTS.md](AGENTS.md).

Lag endringen i en fork, og åpne en pull request mot `main`.
[CONTRIBUTING.md](CONTRIBUTING.md) forklarer hvem som kan merge, og hvordan repoet er
satt opp på GitHub.

## Meld en sårbarhet

Har du funnet en sårbarhet, meld den privat slik [SECURITY.md](SECURITY.md) forklarer.
Ikke meld den i en vanlig issue.

## Lisens

MIT, se [LICENSE](LICENSE).

`asd-ste100-english` og `asd-ste100-norsk` bygger på
[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) (MIT), og
lisensteksten står i skill-mappene. Skillene er ikke utgitt eller godkjent av ASD
eller Språkrådet, og de inneholder ikke ordlisten i ASD-STE100.

`github-actions-security` har bare egen tekst. Kildene står i skillen: dokumentasjonen
fra GitHub og npm, zizmor, OpenSSF, [OWASP Top 10](https://owasp.org/www-project-top-ten/)
og [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/).
Fra OWASP bruker vi bare ID-ene og navnene på risikoene. Skillen er ikke utgitt eller
godkjent av GitHub eller OWASP, og den sier ikke at kode eller workflows er i samsvar
med noe fra OWASP.

`secure-coding` har også bare egen tekst. Kildene står i skillen: OpenSSF, Digdir,
Microsoft Learn, [OWASP Top 10](https://owasp.org/www-project-top-ten/),
[OWASP API Security Top 10](https://owasp.org/www-project-api-security/) og
[OWASP Top 10 for LLM Applications](https://genai.owasp.org/). Fra OWASP bruker vi bare
ID-ene og navnene på risikoene. Skillen er ikke utgitt eller godkjent av OWASP, og den
sier ikke at kode er i samsvar med noe fra OWASP.

`container-security` har også bare egen tekst. Kildene står i skillen: dokumentasjonen
fra Kubernetes, Red Hat OpenShift og Docker,
[OWASP Top 10](https://owasp.org/www-project-top-ten/) og
[OWASP Kubernetes Top 10](https://owasp.org/www-project-kubernetes-top-ten/). Fra OWASP
bruker vi bare ID-ene og navnene på risikoene. Skillen er ikke utgitt eller godkjent av
OWASP, Red Hat eller Kubernetes-prosjektet, og den sier ikke at filer er i samsvar med
noe fra OWASP.

`universell-utforming` har også bare egen tekst. Kildene står i skillen: sjekklisten til
Frank Dahle (Digdir) i UX Norge, Uutilsynet, W3C WAI med ARIA Authoring Practices Guide,
GOV.UK, WebAIM, Designsystemet fra Digdir, Aksel fra NAV og
[WCAG 2.1](https://www.w3.org/TR/WCAG21/). Sjekklisten i UX Norge
oppgir ingen lisens, og lisensen til W3C tillater ikke endrede kopier. Skillen gjengir
derfor innholdet med egne ord og bruker bare numrene på suksesskriteriene i WCAG. Skillen
er ikke utgitt eller godkjent av UX Norge, Digdir, Uutilsynet, W3C, WebAIM, NAV eller
GOV.UK.
