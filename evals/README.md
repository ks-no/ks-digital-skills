# Testtekster

Tekstene i `cases.json` tester sikkerhetsskillene (se
[Sikkerhetsskillene](#sikkerhetsskillene)), `universell-utforming` (se
[universell-utforming](#universell-utforming)) og reglene for KI-markører i
`asd-ste100-english` og `norsk-sprakvask`. Tekstene for KI-markørene inneholder:

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
  sikkerhetsskill og for `universell-utforming`. Hver tekst har en `id`, en `type`,
  selve teksten (`text`) og kravet til et riktig svar (`pass`).
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
  én setning i stedet for skillen. Setningen for hver skill står i `SENTENCES` i
  `run.py`.
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

### Resultater for container-security

Kjørt 15. oktober 2026 med agenter i Claude Code, to kjøringer per tekst og variant, på
Opus og Sonnet. En egen KI-agent vurderte svarene til hver tekst uten å vite varianten.
Ingen person har kontrollert vurderingene ennå.

| Tekster | Variant | Opus: krav oppfylt | Opus: virker | Sonnet: krav oppfylt | Sonnet: virker |
| --- | --- | --- | --- | --- | --- |
| C1–C8 | Uten skill | 0,77 | 0,72 | 0,77 | 0,81 |
| C1–C8 | Med skillen | 0,95 | 0,97 | 0,97 | 0,91 |
| C9–C10 | Uten skill | 0,92 | 1,00 | 0,82 | 0,88 |
| C9–C10 | Med skillen | 1,00 | 1,00 | 1,00 | 1,00 |

- «Virker» er andelen svar der filen bygger og kjører, eller der kommandoene virker,
  uten verdier som agenten har funnet på.
- Skillen ble skrevet etter at C1–C8 var kjørt uten skill. C9 og C10 ble laget etter at
  skillen var skrevet, med mønstre som skillen ikke nevner.
- Uten skill var 27 av 40 svar for omfattende: nye ressurser, prober og
  `readOnlyRootFilesystem` uten kjente stier, og lange forklaringer. Med skillen var
  ingen av dem det.
- Uten skill viste tre av fire svar på C7 passordet i et valgfritt steg, og de fleste
  ga kommandoer som starter pods på nytt. Ingen svar med skillen viste passordet.
- Skillen sier at en verdi fra en Secret i en miljøvariabel er riktig. C4 bruker den
  samme løsningen, så resultatet for C4 sier lite om annen trygg konfigurasjon. C9 er
  trygg konfigurasjon med andre mønstre.
- Etter kjøringen ble åtte svake punkter i skillen rettet, blant annet plassholdere i
  `FROM`, en valgfri `rollout restart` i en sjekkoppgave og en ServiceAccount som ikke
  finnes. C1, C2, C3, C6, C7 og C8 ble kjørt på nytt med Opus og Sonnet for å sjekke
  rettelsene. Alle svarene oppfylte kravene til sikkerhet. Ett svar fra Sonnet på C2
  bruker fortsatt en standardverdi i Helm som ikke virker når verdiblokken mangler.
- C9 hadde en feil i teksten: `ADD` fra en URL gir filen modus 600, så en bruker som
  ikke er root, kan ikke lese den. Ingen av kravene måler dette, og bare ett av åtte
  svar så feilen. Teksten har nå `--chmod=644`. Tallene over gjelder den første
  teksten. Med den rettede teksten og den endelige skillen oppfylte begge svarene
  (Opus og Sonnet) alle kravene.

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
- En ny sjekk med tolv skills testet `container-security` med tre oppgaver: en
  Dockerfile, en pod som krasjer med «Permission denied», og en liten endring i et
  Helm-template. Agenten lastet `container-security` i alle de tolv kjøringene, også
  uten linjene.
- Den fjerde oppgaven var et bash-skript som sletter gamle loggfiler. Ingen kjøring
  lastet `container-security`. Med linjene lastet begge modellene `secure-coding`, og
  begge la til et testskript som brukeren ikke ba om.
- Listen og regelen sto i prompten. Et verktøy viser listen på sin egen måte, ofte
  sammen med mange andre skills og verktøy. Sjekken viser derfor at beskrivelsene
  passer til vanlige oppgaver, men ikke at et verktøy laster skillene.
- README anbefaler derfor linjene i `AGENTS.md`. Agenten leser instruksjonsfilen hver
  gang, men en skill bare når den velger den selv.
- Ingen har gjort sjekken i et ekte verktøy ennå.

## universell-utforming

U1–U17 tester `universell-utforming`. Det er syv typer tekster:

- `plan`: en plan for økter med deltakere som bruker ulike hjelpemidler
- `review`: en testplan eller en PR med hull og noen deler som er riktige
- `analyse`: notater fra økter med funn som trolig er feil, og funn som testlederen
  ikke så
- `ready`: kode som skal brukertestes, med hindringer for hjelpemidler og noen
  mønstre som er riktige
- `write`: en ny komponent der agenten selv må gjøre koden tilgjengelig
- `transfer`: deltakere med behov som skillen ikke nevner
- `neutral`: en endring i et skjema uten noen brukertest, eller kode uten
  grensesnitt. Den måler om agenten gjør mer enn brukeren ba om.

Kjør og vurder tekstene på samme måte som tekstene for sikkerhetsskillene, med
`--baseline none`. Varianten med én setning er ikke kjørt for denne skillen.

### Resultater for universell-utforming

Kjørt 20. oktober 2026 med agenter i Claude Code, to kjøringer per tekst og variant, på
Opus og Sonnet. En egen KI-agent (Opus) vurderte svarene til hver tekst uten å vite
varianten. Ingen person har kontrollert vurderingene ennå.

- «Brukbar» er andelen svar som teamet kan bruke slik de er: riktige, praktiske og
  uten mye innhold som brukeren ikke trengte. «Ord» er snittet av antall ord per svar.
- Skillen ble skrevet etter at U1–U6 var kjørt uten skill. Reglene for øktene kommer
  fra sjekklisten i UX Norge, og U1–U3 tester om agenten følger dem. U5 og U7–U13 ble
  laget med behov og mønstre som skillen ikke nevnte da de ble laget. For U14 og U15,
  se «Etter en polish-kjøring».

#### Brukertester (U1–U8)

Første versjon av skillen, U1–U7, 14 svar per variant og modell:

| Variant | Opus: krav oppfylt | Opus: brukbar | Opus: ord | Sonnet: krav oppfylt | Sonnet: brukbar | Sonnet: ord |
| --- | --- | --- | --- | --- | --- | --- |
| Uten skill | 0,83 | 0,79 | 1243 | 0,76 | 0,71 | 1044 |
| Med skillen | 0,97 | 1,00 | 880 | 0,95 | 0,93 | 792 |

- Uten skill var planene lange (U1: i snitt 2420 ord med Opus og 2078 med Sonnet). De
  manglet de fleste punktene som er særegne for sjekklisten:
  - blandet erfaring
  - spørsmål om hvor lenge deltakeren orker
  - lavere talehastighet og hva den gjør med tiden
  - at en skjermleserbruker går forbi noe for å få oversikt
  - samme krav til bestått
  - hvordan økten slutter
- Med skillen var planene omtrent halvparten så lange og oppfylte 0,98–1,00 av
  kravene.
- U5 har døve og tunghørte deltakere. Krav oppfylt gikk fra 0,71 til 1,00 med Opus og
  fra 0,71 til 0,93 med Sonnet. Med skillen tok ingen svar med råd for
  skjermleserbrukere.
- I U3 godtok alle de fire svarene uten skill at en lenke var vanskelig å finne fordi
  skjermleserbrukeren gikk forbi den. Ingen av svarene med skillen gjorde det.
- Etter kjøringen ble to punkter rettet: en oppgave til backloggen skal si hvilket
  resultat rettelsen må gi, og agenten skal ikke be brukeren kjøre en annen skill. U3 og
  U5 ble kjørt på nytt. I U3 fikk to av fire svar en rettelse for bekreftelsessiden mot
  null før. Ingen svar på U5 ba brukeren kjøre en skill.
- U8 ble laget etter rettelsene, med navn på deltakerne i notatene. Uten skill skrev
  alle de fire svarene navn eller diagnose inn i sakene til Jira. Med skillen gjorde
  ingen det. Krav oppfylt gikk fra 0,89 til 1,00 med Opus og fra 0,75 til 0,93 med
  Sonnet.

#### Sjekk av kode (U4, U6, U7, U9–U11)

Skillen sjekker hver endring i grensesnittet, ikke bare før en brukertest. Tabellen
gjelder U4, U7, U9 og U10 med versjon v4 av teksten, åtte svar per variant og modell:

| Variant | Opus: krav oppfylt | Opus: brukbar | Opus: ord | Sonnet: krav oppfylt | Sonnet: brukbar | Sonnet: ord |
| --- | --- | --- | --- | --- | --- | --- |
| Uten skill | 0,89 | 0,12 | 872 | 0,82 | 0,50 | 653 |
| Med skillen | 0,99 | 1,00 | 468 | 0,99 | 0,88 | 409 |

- Uten skill fant agentene de fleste hindringene, men svarene var for omfattende:
  lovtekst, store omskrivinger, testplaner og råd for skjermleser når ingen deltaker
  bruker skjermleser. U9 uten skill med Sonnet mistet fokus etter sletting og meldte
  ikke fra om slettingen (0,64).
- En mellomversjon ba om tester også når agenten ikke ser prosjektet. Da skrev ett svar
  en testfil med pakker som prosjektet kanskje ikke har, og alle fire svarene på U10
  la til teststeg i en gjennomgang. Fra v4 ber teksten om tester bare når agenten
  kan kjøre testene i prosjektet. Med den fikk alle de fire svarene på U10 1,00.
- U6 og U11 er nøytrale: et nytt felt i et skjema, og et endepunkt uten grensesnitt.
  Alle svarene fikk 1,00, med og uten skill, og ingen svar med skillen nevnte
  universell utforming i U11.
- To svar fra Sonnet på U4 brukte `autocomplete="bday"` på elevens fødselsdato. Regelen
  sier nå at `autocomplete` gjelder opplysninger om den som fyller ut skjemaet. Med den
  nye teksten gjorde ingen av to svar det, og begge svarene på U6 beholdt
  `autoComplete="tel"`.
- Svake punkter: ett svar fra Sonnet på U7 flyttet fokus til en overskrift mens
  dialogen fortsatt var åpen, og flere svar fra Sonnet viste til feil
  suksesskriterium for en gjentatt knappetekst.

#### Etter en gjennomgang mot kildene

20. oktober 2026 gikk en KI-agent gjennom skillen mot kilder om universell utforming:
WCAG 2.1 og Understanding-sidene til W3C, ARIA Authoring Practices Guide (APG),
Uutilsynet, WebAIM Million 2026, GOV.UK, Designsystemet og Aksel. Ingen ekspert på
universell utforming har lest gjennomgangen ennå.

- Regelen om synlig ledetekst ble stående. Uutilsynet sier at en placeholder som blir
  borte når brukeren skriver, bryter 3.3.2. Manglende ledetekster er den tredje
  vanligste feilen i WebAIM Million (51 % av forsidene).
- Fakta som ble rettet:
  - Offentlige virksomheter må følge 48 krav (ikke 1.2.3 og 1.2.4).
  - 1.2.5 gjelder video fra 1. februar 2024.
  - 4.1.1 regnes nå som oppfylt for HTML.
  - Landemerker er ikke et krav i seg selv.
- Regler som kom til:
  - fokus i dialoger, når et element forsvinner og ved bytte av side i klienten
  - statusmeldinger i en live region som finnes fra før
  - oppsummering av feil i skjemaer
  - bekreftelse eller angre ved sletting (3.3.4)
  - WCAG 2.2 bare som råd
  - flere grupper av deltakere i brukertester
- U12 og U13 ble laget for de nye reglene, med mønstre som skillen ikke nevner.

Krav oppfylt med den endelige teksten (v6) og uten skill:

| Tekst | Opus uten | Opus med | Sonnet uten | Sonnet med |
| --- | --- | --- | --- | --- |
| U12: endre navn i en liste | 1,00 | 1,00 | 0,71 | 1,00 |
| U13: stemmestyring og skjelving | 0,75 | 0,93 | 0,57 | 0,96 |
| U9: liste med sletting | 1,00 | 1,00 | 0,64 | 1,00 |

- U12 uten skill: begge svarene fra Opus var riktige, men for omfattende. Begge svarene
  fra Sonnet mistet fokus når tekstfeltet forsvant.
- U13: teksten for «avtal hvordan dere snakker» gjaldt først bare skjermleser, og
  begge svarene fra Sonnet tok det bare halvveis med for stemmestyring. Regelen gjelder
  nå også stemmestyring. U13 er derfor ikke lenger en uavhengig test av den regelen.
- U9: en mellomversjon (v5) mistet bekreftelse eller angre ved sletting i tre av fire
  svar. Den endelige teksten har regelen, og alle fire svarene fikk 1,00.
- De andre tekstene ble kjørt på nytt med v5 for å se etter tilbakegang: U1, U2, U5,
  U6 og U11 med én kjøring per modell, U4, U7 og U10 med to. Ingen gikk tilbake.
  Begge svarene fra Opus på U10 byttet en meny som åpnet ved hover, med en knapp som
  åpner og lukker menyen. Det er mønsteret som APG anbefaler, men ikke den minste
  endringen.
- Skillen nevner nå dialoger, fokus etter sletting, tolk og stemmestyring. U5, U7, U9
  og U13 er derfor tester av regler som står i skillen, ikke uavhengige tester.
- Svake punkter: Sonnet regner fortsatt en gjentatt knappetekst som en hindring, og
  ett svar fra Sonnet la til `inputMode="numeric"` på et datofelt.

#### polish

`polish` 0.3.0 har et pass for universell utforming i hver runde. Det er ikke kjørt en
full test av `polish` på en testapp. I stedet simulerte agenter runde 1 på en ny
branch. Branchen hadde faner, en lenke med teksten «Klikk her», et bilde med filnavn
som alternativ tekst og et filter som var snudd. En KI-agent vurderte fire svar med den
gamle og fire med den nye `polish` uten å vite versjonen:

- Krav oppfylt var 0,96 (Opus) og 0,89 (Sonnet) med den gamle, og 1,00 og 0,96 med
  den nye. Tre av fire svar var brukbare med den gamle, og alle fire med den nye.
- Forskjellen er liten, fordi README i fixturen sier at universell utforming gjelder,
  og den gamle `polish` regner det allerede som et krav.
- På en branch uten grensesnitt hoppet begge svarene over passet.
- En full test av passet trenger en testapp med feil i universell utforming som
  skillen ikke nevner. Den er ikke kjørt ennå.
- Resultatene for `polish` 0.3.0 etter polish-kjøringen står i «Etter en
  polish-kjøring».

#### Etter en polish-kjøring

20. oktober 2026 gikk `polish` gjennom branchen. Gjennomgangen førte til disse
endringene i skillene:

- Sjekken av kode bruker ikke `guided-click-through` og kjører ingen kommando som
  starter appen eller en nettleser. Svaret på en sjekk nevner de automatiske sjekkene
  som ikke ble kjørt, og har én `Check:`-linje for hver fil eller del som agenten ikke
  har.
- Svaret har plass til `Check:`-linjer og til delene som en annen skill ber om.
- Tekst i en kontroll trenger 4,5:1 i kontrast. Det som viser en kontroll og
  tilstanden til den, trenger 3:1.
- Fokus går inn i en dialog og tilbake når den lukkes. Tab skal bare bli i en dialog
  som er modal.
- En sak i backloggen kan nevne hjelpemiddelet det skal testes med, men ikke sammen med
  koden til deltakeren.
- I `polish` er universell utforming et krav for hvert grensesnitt, med mindre kravene
  sier at det ikke gjelder. Tekstene som passet skriver, får språkvask. Må en rettelse
  endre en tekst som en snapshot- eller kontrakttest låser, blir hindringen et åpent
  funn.
- Merknaden om at ingen fagperson har gått gjennom skillen, kommer bare når brukeren
  spør om løsningen oppfyller kravene.

En KI-agent (Opus) vurderte svarene uten å vite varianten. Det var én kjøring per
variant og modell, med unntakene som står i teksten, så små forskjeller er støy. Ingen
person har kontrollert vurderingene.

Første runde, krav oppfylt. Rettelsene for kontrast og dialoger hadde da en første
versjon («kantene på kontrollen trenger 3:1», «Tab blir bare i en modal dialog»), som
andre runde endret:

| Tekster | Opus før | Opus etter | Sonnet før | Sonnet etter |
| --- | --- | --- | --- | --- |
| U4, U7, U9, U10, U12 og U16 (kontrast) | 1,00 | 0,99 | 0,94 | 0,97 |
| U8: notater med navn og hjelpemidler | 1,00 | 1,00 | 0,86 | 0,86 |
| `polish` på en branch med grensesnitt | 1,00 | 1,00 | 0,94 | 0,94 |
| `polish` på en branch uten grensesnitt | 1,00 | 1,00 | 0,88 | 0,88 |

- U8: den gamle teksten fikk Sonnet til å skrive P2 sammen med bryterstyring i en sak
  til Jira. Med den nye teksten gjorde ingen svar det.
- En mellomversjon skrev «denne skillen legger bare til disse delene». Da la Sonnet til
  en egen liste over det koden gjør for tilgjengeligheten, i U12 og U7. Med den
  endelige teksten («hvert svar har bare disse delene», og delene som en annen skill
  ber om) gjorde ingen av fire svar det.
- Ett svar fra Sonnet på U12 skjulte statusmeldingen visuelt, selv om brukeren ba om
  at den skulle vises.

Andre runde:

- 3:1 gjelder det som viser en kontroll og tilstanden til den, ikke kantene alene.
- Fokus går inn i og ut av alle dialoger, og Tab blir bare i en modal dialog.
- Ingen kommando starter appen eller en nettleser.
- Merknaden om fagperson kommer bare når brukeren spør om løsningen oppfyller kravene.
- I `polish` står unntaket for universell utforming der kravene blir definert.

| Tekster | Opus før | Opus etter | Sonnet før | Sonnet etter |
| --- | --- | --- | --- | --- |
| U7, U12 og U16: krav oppfylt | 1,00 | 0,97 | 0,92 | 0,92 |
| U7, U12 og U16: ord | 337 | 462 | 430 | 469 |
| U17 (blind): krav oppfylt | 1,00 | 1,00 | 0,83 | 0,92 |
| `polish` på en branch med grensesnitt | 0,94 | 1,00 | 0,83 | 1,00 |

- U17 ble laget av en agent som ikke hadde lest skillen. Uten skill fikk U17 0,67 med
  Opus og 0,75 med Sonnet. Med den gamle teksten ba Sonnet om 3:1 for fokusmarkeringen
  fra nettleseren, som 1.4.11 unntar. Med den nye teksten gjorde den ikke det.
- Svarene ble lengre med den nye teksten, mest fordi de fikk flere `Check:`-linjer.
  AGENTS.md sier at en endring ikke skal gjøre svarene lengre. Tredje runde ga
  `Check:`-linjene en grense (se under).
- Merknaden om fagperson ble testet med to kjøringer av Sonnet per variant på U16 (en
  sjekk før en merge). Med den gamle teksten kom merknaden i begge svarene, og ingen av
  dem var brukbare. Med den nye kom den i ingen av dem. Når brukeren spurte om et skjema
  oppfyller kravene, kom merknaden i alle fire svarene, to med hver tekst.

Tredje runde ga `Check:`-linjene en grense: én linje for hver fil eller del som agenten
ikke har, og ingen linje for en del som koden ikke inneholder. De automatiske sjekkene
for tilgjengelighet som ikke ble kjørt fordi de starter en nettleser, står på én linje.

| Tekster | Opus før | Opus etter | Sonnet før | Sonnet etter |
| --- | --- | --- | --- | --- |
| U7, U12 og U16: krav oppfylt | 1,00 | 1,00 | 0,94 | 0,94 |
| U7, U12 og U16: ord | 412 | 385 | 404 | 441 |

- I samme kjøring ble svarene fra Opus kortere med grensen (412 mot 385 ord), men
  svarene fra Sonnet ble lengre på alle tre tekstene (404 mot 441). Lengden er derfor
  fortsatt et åpent funn.
- Ett av tre svar fra Sonnet på U16 hadde fortsatt merknaden om fagperson.

Gjennomgangen etter tredje runde fant flere hull. Rettelser for seks av dem ble prøvd på
U7, U12, U16 og U17 med én kjøring av Opus og to av Sonnet per variant:

| Tekster | Opus før | Opus etter | Sonnet før | Sonnet etter |
| --- | --- | --- | --- | --- |
| U7, U12, U16 og U17: krav oppfylt | 1,00 | 1,00 | 0,96 | 0,91 |
| U7, U12, U16 og U17: brukbare svar | 4 av 4 | 4 av 4 | 8 av 8 | 6 av 8 |
| U7, U12, U16 og U17: ord | 366 | 373 | 406 | 485 |

- Med rettelsene la Sonnet til lister og forklaringer som brukeren ikke ba om. Teksten i
  skillen ble derfor satt tilbake. Disse hullene er åpne funn:
  - de to setningene om `Check:`-linjer kan leses slik at de motsier hverandre
  - en test som starter en nettleser, blir ikke nevnt når den ikke blir kjørt
  - regelen for 1.4.11 mangler «som trengs for å kjenne igjen» kontrollen
  - unntaket for kontroller som ikke er aktive, gjelder bare 1.4.11 i teksten
  - en test i prosjektet som feiler, blir bare nevnt når agenten selv har skrevet tester
  - merknaden om fagperson kommer ikke når brukeren vil bruke sjekken som bevis
- Rettelsen for 1.4.11 i `references/wcag-check.md` ble beholdt, men ingen av disse
  tekstene leser den filen.

Regel R13 (avtal hvordan dere snakker) nevner eksemplene fra U13 (se over).
Gjennomgangen ba om en regel med generelle ord. Den ble prøvd slik:
«når hjelpemiddelet snakker, eller lytter til stemmen til deltakeren». To nye tekster
testet den:

- U14 (talemaskin, bryterstyring med lyd og en skjermleser) ble laget av samme agent
  rett etter at regelen ble skrevet om. U14 er derfor ikke en blind test.
- U15 (opplesingsprogram for en deltaker med dysleksi, og to deltakere uten
  hjelpemidler som snakker) ble laget av en agent som ikke hadde lest skillen.

| Tekst | Opus uten | Opus dagens | Opus generell | Sonnet uten | Sonnet dagens | Sonnet generell |
| --- | --- | --- | --- | --- | --- | --- |
| U14 | 0,83 | 0,89 | 1,00 | 0,78 | 1,00 | 1,00 |
| U15 | 1,00 | 0,67 | 0,61 | 0,72 | 0,67 | 0,61 |

- Med den generelle regelen ga begge modellene rådene om lyd og tenke høyt også til de
  to deltakerne som ikke bruker et hjelpemiddel som snakker. Regelen ble derfor satt
  tilbake.
- Også dagens tekst ga et råd til feil deltaker: Sonnet ga rådene for skjermleser til
  deltakeren med opplesingsprogram. Problemet er derfor hvilken deltaker en regel
  gjelder for, ikke bare ordene i R13.
- På U15 gjorde skillen svaret fra Opus dårligere enn uten skill (0,67 mot 1,00). Svarene
  med skillen manglet mer om opplesingsprogrammet og om oppsettet i rommet. Dette er et
  åpent problem. Det trengs flere kjøringer og en ny blind tekst før en ny regel blir
  lagt til.

### Laster agenten skillen?

Samme sjekk som for sikkerhetsskillene, med ni skills i listen og syv oppgaver, på Opus
og Sonnet:

- Agenten lastet `universell-utforming` i alle de ti kjøringene med en oppgave om
  grensesnitt eller brukertest med personer med funksjonsnedsettelser (fem oppgaver,
  to modeller). Den lastet skillen også når oppgaven ikke nevnte universell utforming
  (for eksempel en nedtrekksmeny eller en `aria-label`).
- Den lastet ikke skillen for en refaktorering uten grensesnitt (to av to kjøringer).
- Sonnet lastet skillen for en vanlig brukertest med kolleger. Beskrivelsen sier nå at
  skillen ikke gjelder en brukertest uten deltakere med funksjonsnedsettelser. Med den
  nye beskrivelsen lastet ingen av to kjøringer skillen for den oppgaven, og begge
  kjøringene med en brukertest med svaksynte lastet den.
