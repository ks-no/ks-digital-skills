# Før og etter

Fem eksempler i Fiks-stil. Hvert eksempel viser bruddene, den omskrevne teksten og det
som med vilje står igjen. Eksemplene er laget for denne skillen og er ikke hentet fra
virkelige systemer.

Ordtellingen teller ord som er skilt med mellomrom. Tegnsetting teller ikke.

## 1. Feilmelding (streng)

**Før:**

> Det har oppstått en feil under behandlingen av forespørselen din, noe som muligens kan skyldes at sertifikatet som benyttes for autentisering mot Fiks-porten, har utløpt eller er ugyldig; vennligst ta kontakt med support.

**Brudd:**

- 33 ord i én setning med tre påstander: en feil, en mulig årsak og en beskjed.
- Semikolon.
- Substantivsyke: `under behandlingen av forespørselen`.
- Stablede garderinger: `muligens kan`.
- Engelsk smitte: `vennligst ta kontakt med`, `support`.
- Stivt ordvalg: `benyttes`.

**Etter:**

> Det oppstod en feil da forespørselen din ble behandlet. Feilen kan skyldes at sertifikatet for autentisering mot Fiks-porten er utløpt eller ugyldig. Kontakt brukerstøtten.

`Sjekk: Stoppet behandlingen, og er det vår tjeneste som behandler forespørselen? Da er «Vi kunne ikke behandle forespørselen din» bedre.`

- «kan skyldes» står. Kilden vet ikke årsaken, og meldingen skal ikke late som den gjør
  det. `muligens kan` ble til `kan`, fordi én gardering er nok til å vise usikkerheten.
- `teksttyper.md` i `norsk-sprakvask` foretrekker `Vi kunne ikke …` framfor `En feil
  oppstod`. Her er det en sterkere påstand enn kilden har: Kilden sier at det oppstod en
  feil, ikke at behandlingen stoppet. Påstanden går foran stilen, så spørsmålet går til
  forfatteren i en `Sjekk:`-linje.
- `under behandlingen` ble til bli-passiven «ble behandlet», ikke til en aktiv form,
  fordi kilden ikke sier hvem som behandler.

## 2. Driftsvarsel til kommuner (streng)

**Før:**

> Vi vil gjennomføre en deploy av ny versjon av Fiks-plattformen torsdag 16. oktober kl. 18.00–20.00, og i dette tidsrommet vil det kunne forekomme noe nedetid på enkelte tjenester, men dere trenger ikke å foreta dere noe.

**Brudd:**

- 36 ord og tre tanker i én setning.
- Substantivsyke: `gjennomføre en deploy av`.
- Utviklerord til lesere som ikke er utviklere: `deploy`.
- Stablet modalitet: `vil det kunne forekomme`.

**Etter:**

> Vi setter en ny versjon av Fiks-plattformen i drift torsdag 16. oktober kl. 18.00–20.00. I dette tidsrommet kan det bli noe nedetid på enkelte tjenester. Dere trenger ikke å gjøre noe.

`Sjekk: Hvor lenge kan nedetiden vare, og hvilke tjenester gjelder det?`

- `deploy` ble til `sette i drift`, fordi leserne er kommuner. Til utviklerteamet ville
  `deployer` stått. Se «Fagord: norsk eller engelsk» i `norsk-sprakvask`.
- `vil det kunne forekomme` ble til `kan det bli`. Usikkerheten er den samme, men den står
  i ett ord.
- `noe nedetid på enkelte tjenester` står. Kilden sier ikke hvor lenge eller hvilke
  tjenester, så omskrivingen gjør det heller ikke. Spørsmålet går til forfatteren i
  `Sjekk:`-linjen.
- `trenger ikke å` er riktig norsk. Det er `du trenger å` uten nektelse som er engelsk
  smitte.

## 3. Prosedyre (streng)

**Før:**

> For å fornye virksomhetssertifikatet skal det nye sertifikatet først lastes opp i administrasjonsgrensesnittet, og deretter må integrasjonen settes opp på nytt med den nye nøkkelen før det gamle sertifikatet tas ut av bruk.

**Brudd:**

- 33 ord, to instruksjoner og en frist i én setning.
- S-passiv i en prosedyre: `lastes opp`, `settes opp`, `tas ut av bruk`. Det er uklart om
  leseren eller systemet skal gjøre det, og `tas ut av bruk` kan leses som et påbud.
- Partikkelverb med flere betydninger: `sette opp` kan bety konfigurere, planlegge eller
  øke.

**Etter:**

> Slik fornyer du virksomhetssertifikatet: Last opp det nye sertifikatet i administrasjonsgrensesnittet. Konfigurer deretter integrasjonen på nytt med den nye nøkkelen før det gamle sertifikatet blir tatt ut av bruk.

`Beholdt: passiv i «blir tatt ut av bruk». En aktiv form må si hvem som tar sertifikatet ut av bruk. Kilden sier ikke hvem.`

`Sjekk: Når blir det gamle sertifikatet tatt ut av bruk, og av hvem?`

- Rekkefølgen er den samme som i kilden, og `deretter` gjør den synlig. En
  nummerert liste trengs først ved tre steg eller flere.
- `tas ut av bruk` er en frist i kilden, ikke en instruksjon, så omskrivingen gjør ikke
  fristen til et steg for leseren. Verbet blir bli-passiv, `blir tatt ut av bruk`, fordi
  s-passiv i en prosedyre kan leses som et skjult påbud (se `skriveregler.md`). Kilden
  knytter kravet (`må … før`) til det andre steget, og imperativen `Konfigurer … før`
  beholder kravet der.
- `ta ut av bruk` og `laste opp` står. Uttrykkene har bare én betydning, og de er de
  vanlige norske ordene for handlingene.

## 4. Feltbeskrivelse i API-dokumentasjon (streng)

**Før:**

> Feltet `mottakerOrgnr` benyttes til å angi organisasjonsnummeret til den mottakende virksomheten, og det er viktig å merke seg at verdien må være på 9 siffer uten mellomrom, ellers vil meldingen kunne bli avvist.

**Brudd:**

- 33 ord i én setning.
- Tom innskutt frase: `det er viktig å merke seg at`.
- Stablet modalitet: `vil meldingen kunne bli avvist`.
- Stivt ordvalg: `benyttes til å angi`. S-passiv er tillatt i en beskrivelse, men her
  gjør `er` jobben med færre ord.

**Etter:**

> `mottakerOrgnr` er organisasjonsnummeret til mottakeren. Verdien må være 9 siffer uten mellomrom. Ellers kan meldingen bli avvist.

`Beholdt: passiv i «kan meldingen bli avvist». En aktiv form må si hvem som avviser meldingen. Kilden sier ikke hvem.`

- `mottakerOrgnr` står uendret. Det er en identifikator, og det er ikke en skrivefeil for
  `mottakerOrganisasjonsnummer`.
- «kan meldingen bli avvist» beholder usikkerheten fra kilden. «blir avvist» hadde vært en
  sterkere påstand enn kilden har dekning for.

## 5. README (STE-preget)

**Før:**

> Denne tjenesten tilbyr en sømløs og robust integrasjon mot Fiks-plattformen; den håndterer alt fra autentisering via Maskinporten til automatisk fletting av pull requests når sjekkene er grønne, slik at du kan fokusere på det som virkelig betyr noe.

**Brudd:**

- Reklameord: `sømløs`, `robust`.
- Semikolon.
- Engelsk smitte: `tilbyr`, `fokusere på det som virkelig betyr noe`.
- Tom avslutning.
- Feil fagord til utviklere: `fletting`.

**Etter:**

> Tjenesten er en integrasjon mot Fiks-plattformen. Tjenesten tar seg av autentiseringen via Maskinporten og merger pull requests automatisk når sjekkene er grønne.

`Sjekk: Kilden sier «alt fra … til». Hva mer gjør tjenesten?`

- `fletting` ble til `merger`. Leserne er utviklere, og det er en Git-merge, så
  verktøyets ord gjelder. Hadde teksten handlet om å slå sammen konfigurasjon, var
  `sammenslåing` riktig, se «Fagord: norsk eller engelsk» i `norsk-sprakvask`.
- `tar seg av` er et partikkelverb med én betydning her, og det er det vanligste ordet.
- Kilden sier «alt fra … til», som antyder at tjenesten gjør mer. Omskrivingen nevner
  bare de to tingene kilden faktisk sier, og `Sjekk:`-linjen spør forfatteren om resten.
- STE-preget grad: rytmen fra en forklarende tekst får stå, og ordreglene er bare råd.
