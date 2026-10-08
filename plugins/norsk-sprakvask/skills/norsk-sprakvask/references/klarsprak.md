# Klarspråk

Klarspråk er korrekt, klart og brukertilpasset språk. Offentlige virksomheter er
forpliktet til det gjennom språkloven, og Språkrådet og Digitaliseringsdirektoratet
har veiledere for klart språk i digitale tjenester. Denne filen er en
arbeidsversjon av rådene, tilpasset det KS Digital skriver.

Klarspråk handler ikke om å forenkle innholdet. Det handler om at leseren finner
det de trenger, forstår det de finner, og kan bruke det til å gjøre det de skal.

## 1. Begynn med leseren

Før du skriver, svar på tre spørsmål:

- **Hvem leser?** En saksbehandler i en kommune, en utvikler hos en leverandør, en
  IT-leder, en kollega? De kan ulike ord og har ulik tid.
- **Hva skal de gjøre etter å ha lest?** Ta en beslutning, gjøre en handling,
  vite noe? Det avgjør hva som skal først.
- **Hva vet de allerede?** Ikke forklar Fiks-porten for noen som drifter den. Ikke
  forutsett OAuth2-kunnskap hos en økonomisjef.

I tekst til kommuner: gå ut fra at leseren har lite tid, leser på skjerm og skal
gjøre noe konkret.

## 2. Det viktigste først

- Åpne med hva teksten gjelder og hva leseren skal gjøre. Bakgrunn og begrunnelse
  kommer etterpå, for den som vil ha det.
- I e-post og varsler: si det viktigste i emnefeltet og første linje.
- I dokumentasjon: en setning om hva tjenesten gjør, så hvordan man kommer i gang,
  så detaljer.
- I beslutningsunderlag: anbefalingen først, så begrunnelsen.

## 3. Overskrifter som bærer

- Overskriften skal si hva avsnittet svarer på, ikke hva det «handler om». `Slik
  henter du et token` er bedre enn `Token`. `Meldingen slettes etter 24 timer` er
  bedre enn `Sletting`.
- Én overskriftsstil per tekst: alle imperativ, alle substantivfraser eller alle
  hele setninger. Ikke spørsmål som overskrifter.
- Bare første ord med stor forbokstav.

## 4. Setninger

- **Korte.** Én tanke per setning. Setninger på over 25 ord bør deles, særlig i
  tekst til kommuner.
- **Verbet tidlig.** Norsk har verbet på andreplass. Lange innledende ledd skyver
  det bakover og gjør setningen tung.
- **Den som handler, er subjekt.** `Kommunen sender søknaden` heller enn `Søknaden
  sendes av kommunen`. Passiv er greit når handleren er ukjent eller uviktig
  (`Meldingen ble levert kl. 14.02`), og som feilskjuler er den aldri greit (`Det
  ble gjort en feil`).
- **Verb, ikke substantiv.** Substantivsyke gjør teksten tung og upersonlig.

| Substantivsyke | Klarspråk |
| --- | --- |
| foreta en vurdering av | vurdere |
| gjennomføre en registrering | registrere |
| gi en tilbakemelding | svare, si fra |
| ta en beslutning om | bestemme, beslutte |
| ha behov for | trenge |
| være av betydning | bety noe |
| komme til anvendelse | gjelde |
| innsending gjøres | send inn |
| det er mulighet for | du kan |

- **Ikke stable innskudd.** `Løsningen, som …, og som …, vil …`: del opp.
- **Unngå dobbel nekting og hedging.** `Det er ikke usannsynlig at` → `Trolig`.

## 5. Ord

- **Vanlige ord framfor stive.** `bruke` ikke `benytte`, `få` ikke `motta`, `om`
  ikke `vedrørende`/`angående`, `før` ikke `i forkant av`, `derfor` ikke `av den
  grunn`, `hvis` ikke `dersom`/`såfremt` (dersom er greit i avtaletekst), `mange`
  ikke `en rekke`, `nå` ikke `på nåværende tidspunkt`, `senere` ikke `på et senere
  tidspunkt`.
- **Fagord forklares første gang** når leseren ikke er fagperson: `et token (en
  tidsbegrenset tilgangsnøkkel)`. Deretter bare fagordet.
- **Ett ord per begrep.** Ikke `tjeneste`, `løsning` og `applikasjon` om samme ting
  for variasjonens skyld. Variasjon forvirrer; gjentakelse er tydelig.
- **Forkortelser skrives ut første gang** hvis leseren kan være usikker:
  `Digitaliseringsdirektoratet (Digdir)`. Unntak er de alle kjenner: `KS`, `NAV`,
  `PDF`.
- **Konkrete ord framfor abstrakte.** `120 kommuner` ikke `et betydelig antall
  kommuner`. `innen fredag` ikke `i løpet av kort tid`.
- **Kansellistil ut.** `Det vises til`, `Undertegnede`, `Man`, `Vedlagt følger`,
  `Herved`, `Det bes om at`. Skriv `vi` og `du`.

## 6. Du og vi

- **`du`** til leseren, også i tekst til kommuner. `De` er ikke i bruk i offentlig
  sektor lenger og virker fremmed.
- **`dere`** når leseren er en gruppe (kommunen som organisasjon) og det er tydelig
  at det ikke er én person som skal handle. Driftsvarsler og informasjonsbrev til
  alle kommuner er typiske `dere`-tekster; hjelpetekster, feilmeldinger og
  veiledninger er `du`-tekster. Vær konsekvent innenfor én tekst.
- **Blandet publikum** (et varsel som både IT-leder og integrasjonsutvikler leser):
  skriv for den som vet minst, og sett fagordet i parentes første gang: `prøver på
  nytt (retry)`, `tilgangsnøkkel (token)`. Utvikleren mister ingenting; lederen
  forstår.
- **`vi`** om KS Digital. Ikke `KS Digital` i tredje person om oss selv i løpende
  tekst, og ikke `man`.
- **Ikke «brukeren» om leseren.** Skriv til personen: `Du får en e-post`, ikke
  `Brukeren mottar en e-post`, med mindre teksten beskriver systemet for en
  tredjepart (systemdokumentasjon til utviklere).

## 7. Digitale tjenester

Fra Digdirs veileder for klart språk i digitale tjenester, tilpasset:

- **Knapper sier hva som skjer:** `Send søknad`, `Lagre og gå videre`, `Slett
  meldingen`, ikke `OK`, `Send`, `Bekreft` alene når det finnes noe mer presist.
- **Ledetekster og hjelpetekster er korte** og står der de trengs, ikke i en
  generell hjelpeside.
- **Feilmeldinger sier hva som gikk galt og hva leseren kan gjøre**, i den
  rekkefølgen, uten koder først: `Vi fant ingen kommune med dette
  organisasjonsnummeret. Sjekk nummeret, eller søk på navn.` Teknisk detalj og
  feilkode til slutt, for den som skal rapportere.
- **Tomme tilstander forklarer og peker videre:** `Du har ingen meldinger ennå. Nye
  meldinger vises her når en kommune sender til deg.`
- **Statusmeldinger sier hva som skjer nå:** `Sender … Det tar omtrent et minutt.`
  Ikke `Vennligst vent`.
- **Bekreftelser sier hva som er gjort og hva som skjer videre:** `Søknaden er
  sendt. Kommunen svarer innen tre uker.`
- **Samme ord i menyen, overskriften og knappen** for samme ting.

## 8. Sjekk til slutt

Les teksten som leseren. Spør:

- Skjønner jeg etter første avsnitt hva dette gjelder og hva jeg skal gjøre?
- Er det ord jeg måtte slå opp?
- Er det setninger jeg måtte lese to ganger?
- Kunne jeg strøket et avsnitt uten at noe gikk tapt?
- Er det tydelig hvem som gjør hva, og når?

Er svaret feil på noen av dem, rett teksten, ikke leseren.
