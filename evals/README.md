# Testtekster

Tekstene i `cases.json` tester sikkerhetsskillene (se [Sikkerhetsskillene](#sikkerhetsskillene))
og reglene for KI-markører i `asd-ste100-english` og `norsk-sprakvask`. Tekstene for
KI-markørene inneholder:

- kontraster av typen «not just X, it is Y»
- bilder og sammenligninger som skal forklare noe
- skryt og dramatikk
- det som skal stå, for eksempel sammenligninger av samme slag, roller i en prompt,
  vanlige rettelser og fagord som er bilder (`watchdog`)

Ingen av setningene står i skillene. Testen måler derfor om agenten bruker regelen,
ikke om den kjenner igjen et eksempel. `scripts/validate.py` feiler hvis en skill
får en setning fra en testtekst.

## Innhold

- `cases.json`: tekstene, med `en` for engelsk, `no` for norsk og en liste for hver
  sikkerhetsskill. Hver tekst har en `id`, en `type`, selve teksten (`text`) og kravet
  til et riktig svar (`pass`).
- `run.py`: kjører tekstene gjennom en modell og setter svarene ved siden av kravene.

## Kjøring

Skriptet trenger Python 3, git og en kommando som leser prompten fra stdin og skriver
svaret til stdout.

```sh
python3 evals/run.py --cmd "ollama run llama3.1" --before main --out evals/results/llama.md
```

- `--cmd`: kommandoen som kjører modellen, for eksempel `ollama run <modell>` eller
  `claude -p`.
- `--before`: en git-ref. Hver tekst kjører da også med skillene slik de er der, så du
  kan sammenligne før og etter en endring. Uten `--before` kjører bare skillene i
  arbeidskopien.
- `--only`: bare disse tekstene, for eksempel `E3,E7,N3`.
- `--runs`: antall kjøringer per tekst og versjon. Standard er 1.
- `--out`: filen svarene skrives til. Uten `--out` kommer de på stdout.

`evals/results/` står i `.gitignore`.

## Vurdering

Skriptet vurderer ikke svarene. Les hvert svar mot `pass`, og sett riktig, delvis eller
feil. Kravene handler om innhold: om svaret beholder påstandene, garderingene og
avgrensningene, og om det legger til noe som ikke står i kilden.

Lar du en modell vurdere, les vurderingene selv. En modell som vurderer etter de samme
reglene, sjekker lett om svaret følger reglene, og ikke om meningen er den samme.

## Nye tekster

- Skriv minst én ny tekst for hver ny regel og hvert nytt unntak. Skriv gjerne også en
  tekst som regelen ikke skal treffe.
- Bruk ord og eksempler som ikke står i skillene.
- Skriv i `pass` hva svaret må beholde, og hva det ikke må legge til.
- Gi teksten neste ledige `id`. Ikke gjenbruk en `id`, så resultatene kan sammenlignes.

## Resultater

Kjørt med Claude (agenter i Claude Code) 12. og 14. oktober 2026, én kjøring per
tekst. «Før» er skillene før #3, og «etter» er skillene i #3.

| Tekster | Før | Etter |
| --- | --- | --- |
| E1–E14 | 12 riktige, 1 delvis (E3), 1 feil (E10) | 12 riktige, 2 delvis (E3, E7) |
| N1–N9 | 6 riktige, 3 feil (N1, N2, N3) | 9 riktige |
| E15, E16, N10, N11 | ikke kjørt | 4 riktige |

Tallene for E1–E14 etter endringen er fra en tidligere versjon av punkt 7 i
`asd-ste100-english`. E15, E16, N10 og N11 kjørte med versjonen som ble merget.

Svake punkter etter endringen:

- E3: agenten leser lagringen i 90 dager som det teksten mener med «far more», men
  sier fra om at det er en tolkning.
- E7: agenten gjetter hva kokken og servitøren står for, men sier fra om at det er en
  tolkning.

## Sikkerhetsskillene

`cases.json` har også tekster for sikkerhetsskillene, under navnet på skillen. G1–G11
tester `github-actions-security`, og S1–S9 tester `secure-coding`. Det er fire typer
tekster:

- `write`: en oppgave der den usikre løsningen ligger nær
- `review`: en workflow med en feil som agenten skal finne
- `safe`: en workflow som ser usikker ut, men som er trygg. Den måler falske funn.
- `neutral`: en oppgave uten noe å beskytte. Den måler om agenten gjør mer enn
  brukeren ba om.

`pass` sier både hva som må være sikkert, og hva som må virke.

### Kjøring

Kjør hver tekst i tre varianter: uten skill, med én setning og med skillen.

```sh
python3 evals/run.py --cmd "claude -p" --only G1,G2 --baseline none,sentence --runs 3 --workdir "$(mktemp -d)"
```

- `--baseline none,sentence` legger til en variant uten skill og en variant med
  én setning om sikkerhet i stedet for skillen.
- `--workdir <mappe>` kjører modellen i mappen. Er mappen tom, leser ikke modellen
  prosjektet.
- Et agentverktøy som `claude -p` kan laste skills som du har installert, også i
  variantene uten skill. Slå av skillene fra dette repoet før du kjører.
- `--dump <mappe>` skriver promptene til filer og kaller ingen modell. Bruk det når
  agenter kjører promptene.
- Et `files`-felt i en tekst legger flere filer fra skillen til i prompten.

Kjør på en sterk og en svakere modell som folk faktisk bruker, for eksempel Claude
Opus og Sonnet.

### Vurdering

Bland svarene fra alle variantene, og fjern variantnavnene før du vurderer. Vurder
hvert krav i `pass` som riktig, delvis eller feil. Vurder også om workflowen virker,
og om svaret tar med mer enn brukeren ba om.

Foreløpig vurderer en KI-agent svarene, ikke en person. En agent sjekker lett om et
svar følger reglene, men ikke alltid om svaret er riktig. Målet er at en person går
gjennom et utvalg av vurderingene, særlig de som avgjør om en regel blir stående.
Til da:

- Les tallene som en retning, ikke som et fasitsvar.
- Små forskjeller, for eksempel 0,97 mot 0,98, er innenfor det som varierer fra
  kjøring til kjøring.
- Si alltid i en PR at en KI-agent vurderte svarene.

### Resultater for github-actions-security

Kjørt 15. oktober 2026 med agenter i Claude Code, tre kjøringer per tekst og variant.
En egen KI-agent vurderte svarene til hver tekst uten å vite varianten. Ingen person
har kontrollert vurderingene ennå. Haiku er med som en nedre grense.

| Variant | Opus: krav oppfylt | Opus: virker | Haiku: krav oppfylt | Haiku: virker |
| --- | --- | --- | --- | --- |
| Uten skill | 0,97 | 0,92 | 0,92 | 0,54 |
| Én setning | 0,97 | 0,88 | 0,88 | 0,33 |
| Med skillen | 0,98 | 1,00 | 0,98 | 0,96 |

- «Krav oppfylt» er snittet av kravene i `pass` (riktig = 1, delvis = 0,5).
  «Virker» er andelen svar der workflowen gjør det brukeren ba om, og kan kjøre.
- Med én setning tok Opus med OWASP-tabeller, ekstra filer og lange forklaringer i
  nesten alle svarene. Med skillen gjorde ingen av svarene det, og svarene var
  kortere enn uten skill.
- Etter kjøringen ble seks svake punkter i skillen rettet. G6, G7 og G8 ble kjørt på
  nytt med Opus og Sonnet for å sjekke rettelsene.
- Skillen nevner `pull_request.number` og `github.sha` som trygge verdier, og G4
  bruker de samme verdiene. G4 viser derfor ikke om skillen virker på trygge verdier
  som den ikke nevner. Opus fikk 1,00 i G4 også uten skill. Haiku gikk fra 0,80 til
  1,00, og noe av økningen kommer trolig av at skillen nevner verdiene.

### Rettelser etter en gjennomgang

En gjennomgang av branchen og testene 15. oktober 2026 fant fire feil i skillen. Hver
rettelse ble testet med teksten før og etter rettelsen, med to kjøringer per modell på
Opus og Sonnet. En egen KI-agent vurderte svarene uten å vite versjonen. Ingen person
har kontrollert vurderingene ennå.

- Regel 9 sa ikke at noen `setup-*`-actions cacher uten at du ber om det.
  - G2 og den nye teksten G10 (Gradle, som skillen ikke nevner) oppfylte alle kravene
    med begge versjonene.
  - Med den nye teksten slo alle fire Sonnet-svarene på G2 av cachen i
    publiseringsjobben. Med den gamle gjorde ingen av de to det.
  - Den nye teksten G11 (Go) oppfylte alle kravene før og etter den siste endringen
    av ordlyden. G11 bruker `cache: false` på `actions/setup-go`, som regel 9 nevner.
    To av de fire svarene etter endringen brukte ikke `actions/setup-go` i
    release-jobben.
- Eksempelet i `ai-agents-in-workflows.md` kjørte et skript uten checkout. G5
  oppfylte alle kravene med begge versjonene.
- «Labels as approval» i `triggers-and-privilege.md` sa at en label kan godkjenne en
  kjøring med skrivetilgang, i strid med kjerneregel 5. G8 fikk det samme resultatet
  med begge versjonene.
- `actions/checkout` v7 stopper en checkout av en fork under `pull_request_target` og
  `workflow_run`, med mindre steget setter `allow-unsafe-pr-checkout: true`. Skillen
  sier nå at agenten ikke skal sette denne verdien, men si fra og overlate valget til
  en person. Den nye teksten G9 tester dette:
  - Med den opprinnelige skillen satte ett av fire svar verdien selv, og ett stoppet
    ved sperren uten å si fra. De to andre brukte v4 av `actions/checkout`, som ikke
    har sperren.
  - En mellomversjon ba agenten sette verdien. Da gjorde alle fire svarene det.
  - Med den endelige teksten om sperren satte ingen av de fire svarene verdien, og
    alle sa fra.
  - G9 bruker en verdi som skillen nevner. Testen viser derfor om agenten følger
    regelen, ikke om den finner sperren selv.
- «Labels as approval» sa ikke at jobben som kjører koden, bare skal starte når
  labelen blir satt. En jobb som bare sjekker at pull requesten har labelen, kjører
  igjen etter et nytt push. Skillen sier dette nå, og G9 krever det. Alle de tolv
  svarene på G9, fire med den nye teksten og åtte med den gamle, startet jobben bare
  når labelen ble satt. Rettelsen endret derfor ikke resultatet. Kravet kom inn i G9
  etter at regelen var skrevet, så G9 er ikke en uavhengig test av regelen.
- G5 og G8 ble kjørt før de siste endringene i regel 9, i sikkerhetsreglene og i
  avsnittet om labels. Endringene i regel 9 ble testet med G2, G10 og G11, og
  endringene om sperren og labelen med G9.
- Mellom to versjoner endret snittlengden på svarene seg med opptil 94 ord, både opp
  og ned. To kjøringer av samme versjon kunne skille seg med opptil 145 ord.
- G3, G4 og G7 er gjennomganger. De har nå `review.md` i `files`, så også en modell
  som ikke kan lese filer, får filen som skillen ber om.

### Resultater for secure-coding

Kjørt 15. oktober 2026 med agenter i Claude Code, to kjøringer per tekst og variant, på
Opus og Sonnet. En egen KI-agent vurderte svarene til hver tekst uten å vite varianten.
Ingen person har kontrollert vurderingene ennå.

| Variant | Opus: krav oppfylt | Opus: virker | Sonnet: krav oppfylt | Sonnet: virker |
| --- | --- | --- | --- | --- |
| Uten skill | 0,90 | 0,62 | 0,92 | 0,31 |
| Med skillen | 1,00 | 0,94 | 0,97 | 0,94 |

- «Virker» er andelen svar der koden gjør det brukeren ba om, kan kjøre og bare kaller
  navn som finnes.
- Uten skill var de fleste svarene for omfattende: rate limiting, ekstra
  avhengigheter, hjelpefunksjoner som ikke finnes, og lange forklaringer. Med skillen
  var ingen av svarene det.
- Tabellen gjelder S1–S8 med den første versjonen av skillen.
- S4 er trygg kode. Uten skill fant agentene problemer som ikke finnes (0,55 med Opus
  og 0,65 med Sonnet). Den første versjonen av skillen nevnte de samme mønstrene som
  S4, så resultatet sa lite om annen kode. Nå sier skillen bare prinsippet. Med den
  nye teksten fikk alle de fire svarene på S4 fortsatt 1,00.
- S9 er en ny tekst med trygg kode og mønstre som skillen ikke nevner. Den ble laget
  etter at skillen var skrevet. Uten skill fikk Opus 0,75 og Sonnet 0,56, og tre av
  fire svar var for omfattende. Med skillen fikk alle fire svarene 1,00, og ingen var
  for omfattende.
- Etter kjøringen ble fem svake punkter i skillen rettet, blant annet tester som
  passerer av feil grunn. S1, S3, S5 og S7 ble kjørt på nytt med Sonnet for å sjekke
  rettelsene.

### Laster agenten skillen selv?

I alle kjøringene over fikk agenten beskjed om å lese skillen først. Tallene viser
derfor hvor godt skillene virker når agenten har lastet dem, ikke om agenten laster
dem selv. I Claude Code, Codex og Copilot velger agenten en skill ut fra beskrivelsen.

En liten sjekk 15. oktober 2026 testet beskrivelsene. Agenten fikk en liste med elleve
skills (navn, beskrivelse og fil) og en regel om å bruke en skill når oppgaven passer
til beskrivelsen. Den fikk seks vanlige oppgaver på norsk og engelsk som ikke nevner
sikkerhet eller en skill:

- tre oppgaver med applikasjonskode: et endepunkt som henter ett objekt, en
  nedlasting av filer og en gjennomgang av en diff før merge
- to oppgaver med workflows: en ny workflow som kommenterer pull requests, og en ny
  versjon av en action
- én datofunksjon uten noe å beskytte

Hver oppgave ble kjørt med og uten linjene fra README i `AGENTS.md`, på Opus og
Sonnet.

- Agenten lastet riktig skill i alle de 20 kjøringene med kode eller workflows, også
  uten linjene.
- For datofunksjonen lastet ingen av modellene `secure-coding` uten linjene. Med
  linjene lastet begge den, men la ikke til noe i koden.
- Med linjene lastet agenten også `secure-coding` i tre av fire kjøringer med
  workflows. Det gjør prompten lengre.
- Listen og regelen sto i prompten. Et verktøy viser listen på sin egen måte, ofte
  sammen med mange andre skills og verktøy. Sjekken viser derfor at beskrivelsene
  passer til vanlige oppgaver, men ikke at et verktøy laster skillene.
- README anbefaler derfor linjene i `AGENTS.md`. Agenten leser instruksjonsfilen hver
  gang, men en skill bare når den velger den selv.
- Ingen har gjort sjekken i et ekte verktøy ennå.
