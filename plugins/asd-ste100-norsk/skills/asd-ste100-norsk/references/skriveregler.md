# STE-reglene på norsk

Denne filen går gjennom de ni delene av ASD-STE100. For hver del står det hva standarden
sier, hva som kan overføres til norsk, hva som må endres og hvorfor. Reglene er
gjenfortalt etter den offentlige beskrivelsen av standarden. Standardens tekst og
ordliste er ikke gjengitt.

## Om standarden

- Første utgave kom i 1986 fra AECMA, som nå heter ASD (AeroSpace and Defence Industries
  Association of Europe). Simplified Technical English Maintenance Group (STEMG)
  vedlikeholder den.
- Standarden har vært gratis å laste ned siden Issue 6 (2013), men den kan ikke deles
  videre. Gjeldende utgave er Issue 9 fra januar 2025.
- Den har 53 skriveregler i ni deler, en ordliste med om lag 900 godkjente ord og om lag
  1 200 ord som skal unngås.
- En organisasjon kan lage sin egen liste over tekniske navn og tekniske verb som
  fagfeltet trenger.

Det finnes ingen norsk utgave og ingen norsk ordliste. Det som står under, er en
tilpasning skrevet for KS Digital.

## 1. Ord

**STE:** Bruk bare godkjente ord, og bare i den godkjente betydningen og ordklassen.
Tekniske navn (navn på ting i fagfeltet) og tekniske verb (handlinger som hører til
faget) er tillatt utenom ordlisten.

**På norsk:** Uten ordliste er det prinsippet som kan overføres: velg det vanligste
ordet, og bruk det i samme betydning gjennom hele teksten.

Begrepet *teknisk navn* er nøkkelen til spørsmålet om et fagord skal stå på norsk
eller engelsk. Et teknisk navn skrives slik det står på tingen. Git kaller det merge,
så det heter `merge`, bøyd på norsk: `merget`, `mergen`. Enhetsregisteret kaller det
organisasjonsnummer, så det heter `organisasjonsnummer`, også i engelsk tekst.
Beslutningsregelen står under «Fagord: norsk eller engelsk» i referansefilen
`ordliste.md` i `norsk-sprakvask`.

## 2. Substantivfraser

**STE:** Høyst tre substantiv i en kjede (`fuel pump valve`).

**På norsk:** Engelsk stabler løse substantiv. Norsk setter dem sammen til ett ord
(`drivstoffpumpeventil`). Regelen blir derfor: høyst tre ledd i et sammensatt ord eller
en substantivfrase. Lengre sammensetninger deler du opp med en preposisjon:

- ✗ `tilgangsstyringskonfigurasjonsfilen`
- ✓ `konfigurasjonsfilen for tilgangsstyring`

Særskriving er aldri løsningen. `tilgangsstyring konfigurasjonsfil` er feil norsk og kan
endre betydningen.

## 3. Verb

**STE:** Bruk godkjente verb, og verb framfor substantiv (regel 3.7). Bare enkle tider.
Aktiv form i prosedyrer. `-ing`-former bare som del av et teknisk navn.

**På norsk:**

- **Verb framfor substantiv** kan overføres direkte. Regelen treffer substantivsyke, som
  er et kjent problem i norsk forvaltningsspråk: `foreta en vurdering av` → `vurdere`,
  `innsending av skjemaet skjer ved` → `send skjemaet ved`.
- **Tid:** Perfektum er tillatt når resultatet gjelder nå. Norsk bruker perfektum oftere
  enn engelsk: `Vi har fått søknaden din` er naturlig norsk, mens `Vi fikk søknaden
  din` uten tidspunkt kan høres oversatt ut. Stablede former som `vil ha blitt sendt` er
  ikke tillatt.
- **To passiver:** Norsk har bli-passiv (`ble slettet`) og s-passiv (`slettes`). S-passiv
  brukes både i beskrivelser og som skjult påbud (`Skjemaet sendes inn innen fristen`).
  I instruksjoner er den tvetydig: er det leseren som skal sende, eller systemet som gjør
  det? Bruk imperativ. I beskrivelser er s-passiv greit når den som handler, er ukjent
  eller uinteressant.
- **Verbalsubstantiv på `-ing`** (`oppdatering`, `innsending`, `behandling`) er det
  norske motstykket til engelske `-ing`-former. Som navn på en ting er de greie
  (`oppdateringen er tilgjengelig`). Som omskriving av en handling er de substantivsyke.

## 4. Setninger

**STE:** Én instruksjon per setning. Høyst om lag 20 ord i instruksjoner og 25 i
beskrivelser. Ikke utelat subjekt, verb eller artikkel for å spare plass. Bruk lister.

**På norsk:**

- **Lengdegrensene** kan overføres, og klarspråksrådene sier det samme (om lag 25 ord).
  Fordi norske sammensetninger er ett ord, har en norsk setning ofte færre ord enn en
  engelsk med samme innhold. Grensen er altså litt mildere på norsk. Ikke la det friste
  til lengre setninger.
- **Ikke utelat ord.** Telegramstil som `Fil ikke funnet` og `Bruker opprettet` er vanlig
  i norske systemmeldinger. Skriv hele setninger i meldinger: `Filen ble ikke funnet.`
  Er det vår tjeneste som leter, skriv `Vi fant ikke filen.`, slik regelen om `vi` i
  `teksttyper.md` i `norsk-sprakvask` sier.
  Knapper og overskrifter skal være korte (`Lagre`, `Ny bruker`).
- **Verbet tidlig.** Norsk har verbet på andreplass i hovedsetningen. Står en lang
  leddsetning først, kommer hovedverbet sent: ✗ `Etter at du har kontrollert at
  opplysningene i skjemaet stemmer, må du trykke på Send.` → ✓ `Kontroller at
  opplysningene i skjemaet stemmer. Trykk deretter på Send.`

## 5. Prosedyrer

**STE:** Imperativ. Én instruksjon per setning. Betingelsen først. Nummererte steg.

**På norsk:**

- Imperativ (`Slett`, `Åpne`, `Kjør`) er riktig og tydelig norsk. Den er klarere enn
  `du må`, `man må` og s-passiv. `bør` blir imperativ bare når kilden mener det som et
  krav. En anbefaling som lar leseren velge, blir stående.
- Ikke `Vennligst` foran imperativen. Det er engelsk høflighet, og den gjør
  instruksjonen lengre uten å gjøre den vennligere.
- Betingelsen først, med komma etter: `Hvis tokenet er utløpt, hent et nytt.`
- Nummerert liste for tre steg eller flere, ett steg per punkt.

## 6. Beskrivende tekst

**STE:** Høyst om lag 25 ord per setning, ett tema per avsnitt og høyst seks setninger
per avsnitt. Det viktigste først. Passiv er tillatt når den som handler, er ukjent.

**På norsk:** Kan overføres direkte og passer med klarspråksrådene. Se `klarsprak.md` i
`norsk-sprakvask`.

## 7. Sikkerhetsinstruksjoner

**STE:** En advarsel begynner med en tydelig kommando eller betingelse, og sier hva som
skjer hvis leseren ikke følger den.

**På norsk:** Gjelder advarsler i dokumentasjon, driftsvarsler og bekreftelsesdialoger.
Nektelsen står først i norsk imperativ: `Ikke slett nøkkelen.` er mer naturlig enn
`Slett ikke nøkkelen.` Si konsekvensen i en egen setning: `Ikke slett nøkkelen. Uten den
kan ingen lese de krypterte dataene.`

## 8. Tegnsetting og ordtelling

**STE:** Alle vanlige tegn er tillatt, unntatt semikolon (regel 8.1). Standarden har egne
regler for hvordan ord telles.

**På norsk:**

- Ikke semikolon. Del i to setninger.
- Ellers gjelder norsk tegnsetting fra `norsk-sprakvask`: «anførselstegn», ingen lang
  bindestrek (U+2014), komma etter leddsetning som står først, og komma etter innskutt
  leddsetning.
- Tell ord som er skilt med mellomrom. Et sammensatt ord, et tall og en forkortelse teller
  som ett ord.

## 9. Skrivepraksis

**STE:** Blant annet ingen phrasal verbs (regel 9.3), fordi delene ikke forteller hva
uttrykket betyr, og konsekvent bruk av ord.

**På norsk:** Partikkelverb er ikke forbudt. `slå av`, `logge inn`, `legge til` og `ta
med` er de enkleste og vanligste norske ordene for handlingene. Å bytte dem mot
`deaktivere`, `autentisere seg`, `addere` eller `inkludere` gjør teksten tyngre og ofte
mer engelsk.

Regelen på norsk er at uttrykket skal ha én betydning i teksten. Unngå partikkelverb som
har flere betydninger i fagfeltet:

| Uttrykk | Kan bety | Skriv heller |
| --- | --- | --- |
| `sette opp` | konfigurere, planlegge, øke | `konfigurere`, `planlegge`, `øke` |
| `ta ut` | hente ut, fjerne, ta fri | `hente`, `fjerne` |
| `gå gjennom` | lese nøye, bli godkjent | `lese gjennom`, `bli godkjent` |
| `legge inn` | registrere, installere | `registrere`, `installere` |
| `legge ut` | publisere, laste opp, betale for noen | `publisere`, `laste opp` |

Hvis betydningen er klar i sammenhengen og ordet brukes likt hele teksten, kan det stå.

## Det STE ikke dekker

Rettskriving, bøyning, formvalg, tegnsetting utover semikolon og valget mellom norsk og
engelsk fagord hører til `norsk-sprakvask`.

## Kilder

- [ASD-STE100, offisielt nettsted](https://www.asd-ste100.org/)
- [ASD Europe: Simplified Technical English](https://www.asd-europe.org/standards-specifications/simplified-technical-english/)
- [Simplified Technical English på Wikipedia](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- [Språkrådet: klarspråk](https://www.sprakradet.no/klarsprak/)
- `danyuchn/asd-ste100-skill` (MIT), som denne tilpasningen bygger på
