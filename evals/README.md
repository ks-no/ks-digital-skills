# Testtekster

Tekstene i `cases.json` tester sikkerhetsskillene (se [Sikkerhetsskillene](#sikkerhetsskillene))
og reglene for KI-markører i `asd-ste100-english` og `norsk-sprakvask`:

- kontraster av typen «not just X, it is Y»
- bilder og sammenligninger som skal forklare noe
- skryt og dramatikk
- det som skal stå, for eksempel sammenligninger av samme slag, roller i en prompt,
  vanlige rettelser og fagord som er bilder (`watchdog`)

Ingen av setningene står i skillene. Testen måler derfor om agenten bruker regelen,
ikke om den kjenner igjen et eksempel. `scripts/validate.py` feiler hvis en skill
får en setning fra en testtekst.

## Innhold

- `cases.json`: tekstene, med `en` for engelsk og `no` for norsk. Hver tekst har en
  `id`, en `type`, selve teksten (`text`) og kravet til et riktig svar (`pass`).
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

`cases.json` har også tekster for sikkerhetsskillene, under navnet på skillen. G1–G8
tester `github-actions-security`. Det er fire typer tekster:

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
- `--workdir` kjører modellen i en tom mappe, så den ikke leser prosjektet.
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

### Laster agenten skillen selv?

I alle kjøringene over fikk agenten beskjed om å lese skillen først. Tallene viser
derfor hvor godt skillen virker når agenten har lastet den, ikke om agenten laster den
selv. I Claude Code, Codex og Copilot velger agenten en skill ut fra beskrivelsen.

En liten sjekk 15. oktober 2026 testet beskrivelsen. Agenten fikk en liste med elleve
skills (navn, beskrivelse og fil) og en regel om å bruke en skill når oppgaven passer
til beskrivelsen. Den fikk to vanlige oppgaver som ikke nevner sikkerhet eller en
skill: en ny workflow som kommenterer pull requests, og en ny versjon av en action.
Hver oppgave ble kjørt med og uten linjen fra README i `AGENTS.md`, på Opus og Sonnet.

- Agenten lastet `github-actions-security` i alle de åtte kjøringene, også uten
  linjen.
- Listen og regelen sto i prompten. Et verktøy viser listen på sin egen måte, ofte
  sammen med mange andre skills og verktøy. Sjekken viser derfor at beskrivelsen
  passer til vanlige oppgaver, men ikke at et verktøy laster skillen.
- README anbefaler derfor linjen i `AGENTS.md`. Agenten leser instruksjonsfilen hver
  gang, men en skill bare når den velger den selv.
- Ingen har gjort sjekken i et ekte verktøy ennå.
