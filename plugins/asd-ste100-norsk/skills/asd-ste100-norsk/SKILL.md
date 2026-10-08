---
name: asd-ste100-norsk
description: >-
  Skriv norsk teknisk tekst som ikke kan misforstås, med disiplinen fra
  ASD-STE100 (Simplified Technical English) tilpasset norsk grammatikk. Bruk
  denne når en feillesning koster noe: instruksjoner og prosedyrer,
  feilmeldinger, driftsvarsler, rutiner og runbooks, felt- og
  skjemabeskrivelser på norsk, statusrapporter og beskjeder mellom agenter.
  Bruk den også når brukeren sier «STE på norsk», «STE100», «forenklet teknisk
  norsk», «kontrollert språk», «80 % STE», «skriv så det ikke kan misforstås»
  eller «gjør dette enklere å lese». Bruk den sammen med norsk-sprakvask, som
  eier rettskriving, tegnsetting og valget mellom norsk og engelsk fagord. Ikke
  for markedsføring eller tekst der stemmen er poenget. Engelsk tekst går til
  asd-ste100-english.
---

# ASD-STE100 på norsk

Norsk teknisk tekst der hvert ord har én betydning og hver setning bare kan leses på
én måte.

## Hvorfor denne skillen finnes

ASD-STE100 er en standard for kontrollert engelsk fra luftfartsindustrien. Den ble
laget for at mekanikere ikke skulle misforstå vedlikeholdsmanualer, og den fjerner de
to største kildene til feillesning: ord med flere betydninger og setninger som kan
bygges opp på flere måter. Språkmodeller kjenner standarden. Ber du om den, blir
teksten kortere, mer presis og lettere å lese.

Det finnes ingen norsk STE-standard. Denne skillen overfører prinsippene til norsk,
men ikke reglene ord for ord. Engelsk og norsk grammatikk er så ulike at flere av de
engelske reglene blir feil på norsk: partikkelverb er ofte det enkleste norske ordet,
perfektum er vanligere enn på engelsk, og sammensatte ord skrives i ett. Språkmodeller
skriver dessuten norsk med engelsk setningsbygning. En engelsk regel brukt rett på
norsk gjør det verre, ikke bedre.

## Når den gjelder

- instruksjoner, prosedyrer, rutiner og runbooks
- feilmeldinger, varsler og driftsmeldinger til kommuner og brukere
- felt- og skjemabeskrivelser som mennesker leser på norsk
- statusrapporter og beskjeder som en annen agent eller et system skal handle på
- README, PR-beskrivelser og dokumentasjon, med den mildere graden (se under)

Ikke for markedsføring, kronikker eller tekst der stemme og nyanse er poenget. STE er
flatt og bokstavelig med vilje.

Engelsk tekst går til `asd-ste100-english`. Verktøy- og skjemabeskrivelser som en
språkmodell leser, skrives på engelsk, fordi de er modellens prompt.

## Forholdet til norsk-sprakvask

De to skillene deler jobben:

| Denne skillen | `norsk-sprakvask` |
| --- | --- |
| setningsbygning, setningslengde og struktur | rettskriving og bøyning |
| én instruksjon per setning, aktiv form | tegnsetting, tall og datoer |
| ett ord, én betydning | formvalg og husnorm |
| modalitet og presisjon | valget mellom norsk og engelsk fagord |

Bruk denne skillen først og `norsk-sprakvask` etterpå. Sier de noe ulikt om
rettskriving, tegnsetting eller ordvalg, gjelder `norsk-sprakvask`. Unntaket er
semikolon: det bruker du ikke, selv om `norsk-sprakvask` tillater det. Svarformatet i
denne skillen gjelder likevel: gi den omskrevne teksten, ikke oppsummeringen av
rettelser som `norsk-sprakvask` ber om.

### Uten norsk-sprakvask installert

Skillene er separate plugin-er, så denne kan være installert alene. Er den det, er
dette minimumet:

- sammensatte ord i ett: `organisasjonsnummer`, ikke `organisasjons nummer`
- norske vendinger, ikke oversatte: `Vennligst merk at` → `Merk at`, `du trenger å` →
  `du må`, `din konto` → `kontoen din`
- «anførselstegn», komma som desimaltegn og dato som `16.10.2026`
- aldri lang bindestrek (U+2014). Bruk komma, kolon eller punktum, eller bindestrek med
  mellomrom (` - `) når ingen av dem passer. `–` står bare i intervaller: `kl. 9–15`.
- én form gjennom hele teksten, og `-en` i bestemt form i ny tekst: `filen`, ikke
  `fila`. En tekst som bruker `-a` gjennomgående, er ikke feil.
- til lesere som ikke er utviklere: det norske ordet. Står det engelske ordet i
  verktøyet de bruker, skriv det i parentes første gang. Det samme gjelder når
  utviklere også leser teksten.
- til utviklere: Git-, GitHub- og CI-ord står på engelsk og bøyes på norsk: `merge`,
  `merget`, `branchen`

## To grader

Velg grad før du skriver om. Sier ikke brukeren hvilken, velg ut fra teksttypen. Ikke
si hvilken du valgte, med mindre brukeren ber om regeltabellen.

**Streng.** Instruksjoner, feilmeldinger, driftsvarsler, feltbeskrivelser og
sikkerhetstekst: all tekst der en feillesning koster noe. Strukturreglene og
sjekklisten gjelder fullt ut, også lengdegrensene. Ordreglene følger du så langt du kan.

**STE-preget.** README, PR-beskrivelser, endringslogger og forklarende tekst.
Strukturreglene og sjekklisten gjelder fullt ut. Ordreglene er råd, så verbene kan
variere. Prosa trenger litt variasjon, og en streng omskriving av prosa gjør teksten
stiv uten å gjøre den klarere. Ber brukeren
om «80 % STE» eller «nesten STE», er det denne graden.

## Strukturreglene

Disse kan du bruke med sikkerhet. De handler om formen på setningen, ikke om en
ordliste.

| Regel | Gjør | Ikke |
| --- | --- | --- |
| Imperativ i instruksjoner | `Slett filen.` | `Du må slette filen.` `bør` blir imperativ bare når kilden mener det som et krav. En anbefaling som lar leseren velge, blir stående. |
| Én instruksjon per setning | `Åpne filen. Les linje 3.` | `Åpne filen og les linje 3, og sjekk deretter om den stemmer.` |
| Aktiv form | `Systemet sletter filen.` | `Filen blir slettet av systemet.` Passiv er riktig når den som handler, er ukjent eller uinteressant. |
| Ikke s-passiv i instruksjoner | `Fyll ut skjemaet.` | `Skjemaet fylles ut.` Leseren vet ikke om det er en beskjed eller en beskrivelse av hva systemet gjør. |
| Setningslengde | Høyst 20 ord i instruksjoner og høyst 25 i beskrivelser. | Lange setninger med flere innskudd. |
| Ikke semikolon | Del i to setninger. | Semikolon i det hele tatt. |
| Korte sammensetninger | Høyst tre ledd: `konfigurasjonsfilen for tilgangsstyring` | `tilgangsstyringskonfigurasjonsfilen`. Særskriving er aldri løsningen. |
| Ikke utelat ord | `Filen ble ikke funnet.` Er det vår tjeneste som leter, skriv `Vi fant ikke filen.` | `Fil ikke funnet.` Knapper og overskrifter er unntatt. |
| Behold modaliteten | `Forespørselen kan ha feilet.` | `Forespørselen feilet.` Det er en annen påstand. |
| Ett navn per ting | Velg ett navn for hver ting, og bruk det i hele teksten. | `bruker`, `innbygger` og `søker` om samme person. |
| Verb framfor substantiv | `Vurder loggen.` | `Foreta en vurdering av loggen.` |
| Ett tema per avsnitt | Høyst seks setninger. | Avsnitt om flere ting. |
| Lister for rekkefølger | Nummerert liste for tre steg eller flere. | Alle stegene i én setning. |

### Tid: enkle former, men perfektum er norsk

STE tillater bare enkle tider. På engelsk er `we received the report` riktig STE,
mens `we have received the report` ikke er det. På norsk passer ikke regelen: `Vi har
fått søknaden din` er den naturlige formen når resultatet gjelder nå, og `Vi fikk
søknaden din` krever et tidspunkt (`i går`, `16. oktober`).

- Bruk presens og preteritum som standard.
- Bruk perfektum når resultatet gjelder nå: `Jobben har kjørt ferdig, og resultatet
  ligger i mappen.`
- Ikke stablede former: ✗ `Meldingen vil ha blitt sendt før kl. 12.` → ✓ `Meldingen
  blir sendt før kl. 12.` Ikke legg til en som handler, hvis kilden ikke har det.
- Modaliteten går foran tidsregelen: `kan ha feilet` beholder `ha`.

### `kan` har to betydninger

`kan` betyr både «det er mulig at» og «det er lov å». `Secreten kan mangle` kan leses
som at det er greit at den mangler. Når `kan` kan leses begge veier, skriv usikkerheten
med `kanskje` eller `det kan hende at`: `Secreten mangler kanskje.` Behold styrken: `kan
ha feilet` og `har kanskje feilet` er like usikre, `har trolig feilet` er sikrere.

## Ordreglene: en retning, ikke en fasit

Fullt STE bygger på en ordliste med om lag 900 godkjente engelske ord. Det finnes ingen
norsk ordliste, og den engelske kan ikke deles videre. Ordreglene under er derfor en
retning, ikke krav du kan kontrollere. Si aldri at en tekst «følger STE-ordlisten».

| Regel | Gjør | Ikke |
| --- | --- | --- |
| Ett verb per handling | Velg ett verb per handling og hold på det: alltid `kontrollere`, eller alltid `sjekke`. | `sjekke`, `kontrollere` og `verifisere` om samme handling i én tekst. |
| Vanlige ord | `bruke`, `få`, `hvis` | `benytte`, `motta`, `dersom` |
| Partikkelverb med én betydning | `slå av`, `logge inn`, `legge til` | `deaktivere`, `autentisere seg`, `addere` |
| Ikke partikkelverb med flere betydninger | `konfigurere`, `planlegge`, `øke` | `sette opp` (konfigurere, planlegge eller øke?), `ta ut` (hente eller fjerne?) |

**Partikkelverb er ikke forbudt.** STE forbyr engelske phrasal verbs (`take off`, `spin
up`) fordi delene ikke forteller hva ordet betyr. Mange norske partikkelverb er derimot
det enkleste og vanligste ordet. Å bytte `slå av` mot `deaktivere` gjør teksten tyngre,
ikke klarere. På norsk er regelen at ordet skal ha én betydning i teksten, ikke at det
skal være ett ord.

**Fagord er tekniske navn.** Det er STE-begrepet for fagord som ikke står i den vanlige
ordlisten, men som et fagfelt trenger. Prinsippet er at du skriver navnet slik det står
på tingen. Derfor heter det `merge` når Git kaller det merge, og `organisasjonsnummer`
når Enhetsregisteret kaller det det. Følg regelen «Fagord skrives slik det står på
tingen» i `norsk-sprakvask`. Hele regelen, med eksempler, står i referansefilen
`ordliste.md` der, og den trenger du bare ved tvil. Forklar fagordet første gang hvis
leseren ikke kjenner det, og bruk det samme ordet hele teksten: ikke `endepunkt` i ett
avsnitt og `endpoint` i det neste.

Synonymer som ofte veksler i maskinskrevet norsk. Velg ett ord per gruppe:

- `sjekke`, `kontrollere`, `verifisere`, `bekrefte`
- `slette`, `fjerne`
- `starte`, `kjøre`, `sette i gang`, `initiere`
- `hente`, `laste ned`
- `feil`, `avvik`, `problem`
- `bruker`, `innbygger`, `søker` når de betyr samme person

## Sjekkliste

Seks vaner står for det meste av det som gjør maskinskrevet norsk vanskelig å lese.
Hver av dem er mekanisk: du kan peke på ordet eller tegnet. Se etter alle seks før du
skriver om.

1. **Synonymveksling.** Samme ting har flere navn i én tekst, og leseren vet ikke om
   det er én ting eller tre. Velg ett navn.
2. **Stablede garderinger.** `Dette kan potensielt bidra til å forbedre`. Behold én
   gardering med samme styrke, og stryk resten: `Dette kan bidra til å forbedre`. Ikke
   gjør påstanden om til et faktum.
3. **Substantivsyke.** `foreta en vurdering av`, `gjennomføre en oppdatering av`. Bruk
   verbet: `vurdere`, `oppdatere`.
4. **Reklameord.** `sømløs`, `robust`, `kraftig`, `banebrytende`, `helhetlig`. Stryk
   ordet, eller bytt det ut med målingen som viser påstanden.
5. **Lange setninger med innskudd.** Flere tanker bundet sammen med komma, semikolon
   eller bindestrek. Én tanke per setning.
6. **Engelsk setningsbygning.** `Vennligst merk at`, `du trenger å`, `når det kommer
   til`, `din konto`. Her tar `norsk-sprakvask` over.

## Arbeidsmåte

1. Velg grad: streng eller STE-preget.
2. Les teksten én gang for meningen. Ikke begynn å skrive om før du vet hva teksten
   fortsatt skal si etterpå.
3. Finn identifikatorene. Navn i kode, JSON-nøkler, API-felt, URL-stier, enum-verdier og
   miljøvariabler endres aldri, heller ikke for å rette en skrivefeil. Egennavn og sitater
   beholder sin egen skrivemåte.
4. Gå gjennom teksten setning for setning. Marker hvert brudd på strukturreglene og hver
   vane fra sjekklisten. I streng grad markerer du også brudd på ordreglene.
5. Skriv om hver markerte setning, og behold meningen nøyaktig. Mister omskrivingen
   nødvendig presisjon (et sikkerhetsvilkår, en avgrensning, et tall), behold den lange
   formen og si fra.
   - **Sjekk modaliteten før du skriver om.** `kan`, `kanskje`, `noen ganger` og
     `trolig` bærer sikkerheten til den som skrev, og sikkerhet er innhold. En kortere
     setning som gjør en gardering om til et faktum, er en annen påstand. Dette er den
     vanligste feilen i STE-omskrivinger, fordi lengdegrensen frister til å stryke
     garderinger.
   - Ikke legg til fakta eller instruksjoner som kilden ikke har. En omskriving som
     leses bedre fordi den har fått en årsak, en hyppighet, en mekanisme eller et neste
     steg, er ikke lenger en omskriving. Mangler kilden noe, si det i en `Sjekk:`-linje.
6. Kjør sjekkene i `norsk-sprakvask` på resultatet.
7. Gi den omskrevne teksten. Følger teksten allerede reglene, si det, og ikke endre den.

## Svarformat

**Standard: bare den omskrevne teksten.** Ingen innledning om skillen, ingen grad,
ingen opptelling av brudd, ingen oppsummering av endringer og ikke noe tilbud om å
forklare.

To tillegg er lov, hvert på én linje etter teksten:

- `Beholdt:` det du med vilje lot stå, og som kan se ut som et brudd: en lang
  formulering fra trinn 5, perfektum eller passiv der den som handler, er ukjent. Si hva
  en enklere form ville mistet eller lagt til.
- `Sjekk:` innhold som kilden gjør uklart, utelater eller som du har gjettet på: et
  produktnavn som kanskje er feil, en henvisning som kan bety to ting, et neste steg
  leseren trenger. Ikke rett eller fyll ut innholdet selv.

Er det ingenting å melde, la linjene være.

**På forespørsel: regeltabellen.** Ber brukeren om å se resonnementet («vis
endringene», «hvilke regler brøt den», «før og etter»), gi den omskrevne teksten først
og deretter denne tabellen:

```markdown
| Regel | Før | Etter |
| --- | --- | --- |
| S-passiv i instruksjon | «Skjemaet sendes inn før fristen.» | «Send inn skjemaet før fristen.» |
| Substantivsyke | «Vi foretar en vurdering av søknaden.» | «Vi vurderer søknaden.» |

Grad: streng. 5 brudd.
```

Etter tabellen skriver du én linje om det du med vilje ikke forenklet, og hvorfor. Her
kan du også foreslå en kort forklaring på fagord som må stå.

## Grenser

**Skillen skal:**

- skrive om tett eller tvetydig norsk til korte, aktive setninger der hvert ord har én
  betydning
- bare gi den omskrevne teksten, med mindre brukeren ber om regeltabellen
- beholde hvert faktum, hvert vilkår og hver avgrensning
- beholde styrken i hver gardering og ikke legge til påstander eller instruksjoner
- la identifikatorer, egennavn og sitater stå
- foreslå en kort forklaring på fagord som må stå, når brukeren ber om regeltabellen

**Skillen skal ikke:**

- late som den kjenner en norsk STE-ordliste, for den finnes ikke
- forenkle markedsføring, kronikker eller tekst der stemmen er poenget
- fjerne et sikkerhetsvilkår, et unntak eller en avgrensning for å korte ned
- gjøre `kan ha feilet` om til `feilet`, eller `kan skyldes X` om til `skyldes X`
- gjøre tom tekst nyttig. STE retter formen, ikke innholdet. Har teksten ingenting å
  si, si det.
- korte ned forbi det klare: målet er å fjerne tvetydighet, ikke ord

## Referanser

Les en fil bare når den trengs.

| Fil | Les den når |
| --- | --- |
| [skriveregler.md](references/skriveregler.md) | Du er usikker på om en STE-regel passer på norsk, eller brukeren spør om standarden og tilpasningen. Gjennomgår de ni delene av STE: hva som kan overføres, hva som endres og hvorfor. |
| [eksempler.md](references/eksempler.md) | Du er usikker på hvor langt du skal gå, eller brukeren ber om regeltabellen. Har før og etter for feilmelding, driftsvarsel, prosedyre, feltbeskrivelse og README. |

## Kilder og opphav

Strukturen, gradene, sjekklisten og svarformatet er tilpasset fra
`danyuchn/asd-ste100-skill` (Copyright (c) 2026 Dustin Yuchen Teng, MIT-lisens).
Lisensteksten står i `LICENSE-asd-ste100-skill.txt` i denne mappen. Reglene bygger på
den offentlige beskrivelsen av ASD-STE100 Issue 9 fra januar 2025, se asd-ste100.org.
Tilpasningen til norsk (partikkelverb, perfektum, s-passiv og sammensatte ord) er skrevet
for KS Digital. Skillen er ikke utgitt eller godkjent av ASD og inneholder ikke
STE-ordlisten.
