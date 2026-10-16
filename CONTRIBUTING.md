# Bidra til KS Digital Skills

Alle kan bidra, også de som ikke jobber i KS Digital. Denne filen forklarer hvordan du
lager en endring, hvem som kan merge den, og hvordan repoet er satt opp på GitHub.

## Slik lager du en endring

1. Lag en fork av repoet.
2. Gjør endringen i en branch i forken.
3. Kjør `python3 scripts/validate.py`, og rett feilene den finner.
4. Åpne en pull request mot `main`.

Reglene for skillene står i [README.md](README.md) under «Legg til en skill» og i
[AGENTS.md](AGENTS.md).

Workflowen `Validate` kjører på pull requesten. Er du ikke medlem av ks-no, må noen med
skrivetilgang godkjenne kjøringen før den starter. En pull request fra en fork får
ingen secrets og bare lesetilgang til repoet.

Har du funnet en sårbarhet, følg [SECURITY.md](SECURITY.md) i stedet.

## Versjoner av actions

Dependabot oppdaterer actions i `.github/workflows/`. Den foreslår en ny versjon bare når
versjonen er minst 7 dager gammel. I den tiden kan utgiveren trekke tilbake en versjon som
er ødelagt eller kompromittert.

- Ikke endre versjonen av en action for hånd. La Dependabot gjøre det. Unntaket er en
  sikkerhetsfiks, se under.
- Legger du til en ny action, velg en versjon som ble utgitt på GitHub for minst 7 dager
  siden. Lås den til en full commit-SHA, med versjonen i en kommentar.
- En action som ikke er fra GitHub, ks-no eller en verifisert utgiver, må stå i listen
  over unntak under «Andre innstillinger». Ellers stopper workflowen med «Startup
  failure».

### Sikkerhetsfikser

Dependabot lager ingen varsler og ingen security updates for en action som er låst til en
SHA. Derfor slår zizmor opp hver action i GitHub Advisory Database. Det skjer i jobben
`validate`, på hver pull request, ved hver push til `main` og hver mandag. Har en action
vi bruker, en kjent sårbarhet, blir jobben rød. Er den planlagte kjøringen på mandag rød,
sender GitHub e-post til den som sist endret `schedule` i
`.github/workflows/validate.yml`.

Kjøringen på mandag finner en ny advisory også i uker uten pull requester. GitHub slår den
av når repoet har vært uten aktivitet i 60 dager. Da står det en advarsel under Actions →
Validate. Slå kjøringen på igjen med «Enable workflow».

Gjelder sårbarheten oss, bumper en vedlikeholder actionen for hånd med en gang:

1. Lag en egen pull request for fiksen.
2. Velg en versjon som advisoryen oppgir som rettet. Regelen om 7 dager gjelder ikke her.
3. Finn SHA-en til versjonen:

   ```sh
   git ls-remote https://github.com/<eier>/<action> 'refs/tags/vX.Y.Z' 'refs/tags/vX.Y.Z^{}'
   ```

   Viser kommandoen to linjer, er taggen annotert. Da står SHA-en til commiten på linjen
   med `^{}`.
4. Skriv SHA-en på `uses:`-linjen, med versjonen i kommentaren.
5. Skriv GHSA-ID-en i pull requesten.

Finnes det ingen rettet versjon ennå, eller gjelder sårbarheten ikke oss, legg GHSA-ID-en i
`.github/zizmor.yml`:

```yaml
rules:
  known-vulnerable-actions:
    config:
      allow:
        - GHSA-xxxx-xxxx-xxxx
```

Skriv grunnen i pull requesten. Fjern ID-en når en rettet versjon finnes. Ikke bruk
`# zizmor: ignore[known-vulnerable-actions]` på `uses:`-linjen, fordi den skjuler alle
advisoryene for actionen, også nye.

## Vedlikeholdere

Vedlikeholderne har rollen Maintain eller Admin på repoet. Bare de kan:

- pushe brancher og tagger til repoet
- merge pull requester til `main`

Det er to grunner til dette:

- En workflow som starter av en push, kjører slik den er i commiten som ble pushet. Den
  kan lese alle secrets som repoet har tilgang til. Den som kan pushe en branch eller en
  tag, kan derfor lese de samme secretene.
- Alle som installerer skillene, får det som står på `main`. En skill er instruksjoner
  som en agent følger, så en endring på `main` når agentene til alle brukerne.

Rollen Write gir ikke unntak fra reglene, fordi flere enn vedlikeholderne har den.

### Legg til en vedlikeholder

1. Gi personen rollen Maintain under Settings → Collaborators and teams.
2. Åpne regelen for `main` under Settings → Branches.
3. Legg personen til under «Restrict who can push to matching branches».
4. Skal personen få forespørsler om review, legg brukernavnet til i
   [.github/CODEOWNERS](.github/CODEOWNERS).

Når en vedlikeholder slutter, fjern personen fra de samme stedene.

### Godkjenn en kjøring fra en fork

Alle med skrivetilgang kan godkjenne en kjøring. Les endringene under `.github/` før du
godkjenner. En pull request kan endre workflowen som kjører.

## Innstillinger på GitHub

Disse innstillingene er satt på GitHub, ikke i filer, og ingenting i repoet kan sjekke
dem. Endrer du en innstilling, endre også listen her.

### Regler for brancher og tagger

- **Rulesetet `main`** (Settings → Rules → Rulesets):
  - En pull request kreves. Ingen godkjenning kreves, og en ny push avviser en
    godkjenning som noen har gitt.
  - Alle samtaler i pull requesten må være løst.
  - Jobben `validate` i `.github/workflows/validate.yml` må være grønn, og branchen må
    være oppdatert med `main`. Endrer du navnet på jobben, endre rulesetet når du
    merger. Ellers venter hver pull request på en sjekk som ikke kommer.
  - Funn fra CodeQL og varsler fra secret scanning som ikke er løst, stopper en merge.
  - Bare squash er lov, og historikken er lineær.
  - Ingen kan force-pushe til `main` eller slette den.
  - Ingen har unntak (bypass).
- **Rulesetet «Brancher: bare maintainers»** gjelder alle brancher unntatt `main`.
  Ingen kan lage, endre eller slette en branch, eller force-pushe til den. Rollene
  Repository admin og Maintain og appen Dependabot har unntak. Dependabot trenger
  unntaket for å pushe branchene til sine pull requester.
- **Rulesetet «Tagger: bare maintainers»** gjelder alle tagger og har de samme
  reglene. Rollene Repository admin og Maintain har unntak.
- **Den klassiske regelen for `main`** (Settings → Branches) har bare «Restrict who can
  push to matching branches» med vedlikeholderne, og «Do not allow bypassing the above
  settings». Bare vedlikeholderne kan derfor merge til `main`. Hver vedlikeholder står i
  listen med brukernavn, også de som er admin. Regelen er klassisk og ikke et ruleset,
  fordi et ruleset slipper vedlikeholderne gjennom bare med unntak. Da ber GitHub om et
  ekstra kryss ved hver merge.

### Andre innstillinger

- **Pull Requests** (Settings → General): bare «Allow squash merging» er på.
  «Automatically delete head branches» er på.
- **Features** (Settings → General): Issues er på. Wiki og Projects er av. Et ruleset
  gjelder ikke wikien, så med wikien på kunne alle med skrivetilgang endre den.
- **Actions permissions** (Settings → Actions → General): «Require actions to be pinned
  to a full-length commit SHA» er på. «Allow ks-no, and select non-ks-no, actions and
  reusable workflows» er valgt, med «Allow actions created by GitHub» og «Allow actions
  by Marketplace verified creators» krysset av, og dette unntaket:

  ```text
  zizmorcore/zizmor-action@*
  ```

  Listen har `@*`, fordi workflowen låser actionen til en SHA. En SHA i listen ville
  stoppet hver bump fra Dependabot.
- **Workflow permissions** (samme side): «Read repository contents and packages
  permissions» er valgt, og «Allow GitHub Actions to create and approve pull requests»
  er av.
- **Fork pull request workflows** (samme side): «Require approval for all external
  contributors» er valgt.
- **Sikkerhet**: CodeQL kjører med standardoppsettet for Actions og Python. Secret
  scanning, Dependabot alerts, Dependabot security updates og «Private vulnerability
  reporting» er på.
- **Secrets**: ingen workflow i repoet bruker secrets. Trenger en ny workflow en secret,
  ta det opp i en issue først.
