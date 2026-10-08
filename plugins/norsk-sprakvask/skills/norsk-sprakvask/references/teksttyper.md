# Teksttyper

Hva som er godt norsk, avhenger av hvor teksten skal stå. Denne filen gir regler
per teksttype for det KS Digital skriver mest av.

## Grensesnittekster

Knapper, menypunkter, ledetekster, hjelpetekster, tomme tilstander, statusmeldinger.

- **Imperativ i knapper og handlinger:** `Lagre`, `Send søknad`, `Legg til
  mottaker`. Ikke substantiv (`Lagring`), ikke infinitiv (`Å lagre`), ikke
  «Klikk her for å …».
- **Bare første ord stor:** `Legg til ny bruker`, ikke `Legg Til Ny Bruker`.
- **Ingen punktum** i knapper, menypunkter og ledetekster. Hjelpetekster på hel
  setning får punktum.
- **`du`, ikke `brukeren`.** `Du har ingen meldinger`, ikke `Brukeren har ingen
  meldinger`.
- **Samme ord for samme ting** overalt: hvis menyen sier `Meldinger`, sier
  overskriften og knappen også `Meldinger`, ikke `Innboks` eller `Beskjeder`.
- **Ikke `Vennligst`**, ikke `Trykk knappen` (`Trykk på knappen`), ikke `Ja/Nei`
  som eneste svar på et spørsmål brukeren ikke har sett.
- **Plassholdertekst i felt er eksempler**, ikke ledetekst: `f.eks. 912 345 678`.
- Sammensatte ord i ett: `brukernavn`, `passordfelt`, `innloggingsside`.

## Feilmeldinger

Rekkefølge: hva gikk galt, hva kan du gjøre, teknisk detalj til slutt.

```text
Vi fant ingen kommune med organisasjonsnummer 912 345 678.
Sjekk nummeret, eller søk på kommunenavn.
Feilkode: ORG_NOT_FOUND
```

- Skriv til leseren, ikke om systemet: `Vi kunne ikke lagre endringene` framfor
  `Lagring feilet` eller `En feil oppstod`. Bruk `vi` bare når det er vår tjeneste som
  gjorde handlingen. Feilet noe i leserens eget system eller i en pipeline hos en
  leverandør, si hva som feilet: `Deploy til testmiljøet feilet.`
- Si aldri bare `Noe gikk galt`. Hvis vi ikke vet hva, si det og si hva som
  skjer: `Vi kunne ikke hente meldingene dine akkurat nå. Prøv igjen om noen
  minutter. Feilen er registrert hos oss.`
- Ikke skyld på brukeren: `Passordet stemmer ikke`, ikke `Du skrev feil passord`.
- Ikke utropstegn, ikke `Oops`, ikke humor i feilmeldinger fra en offentlig
  tjeneste.
- Feilkoder og HTTP-statuser er identifikatorer og oversettes ikke.

## Brukerdokumentasjon og veiledninger

- Første setning: hva tjenesten gjør og for hvem. Så «Kom i gang». Så detaljer.
- **Steg-for-steg i nummererte lister**, ett steg per punkt, imperativ: `1. Logg inn
  i Fiks-porten. 2. Velg …`
- **Overskrifter som svarer på leserens spørsmål:** `Slik henter du et token`,
  `Hva skjer når fristen er passert`.
- **Skjermelementer i anførselstegn eller kursiv**, konsekvent: velg «Innstillinger»
  eller velg *Innstillinger*.
- **Kode, kommandoer, filnavn, URL-er og feltnavn** i kodeformat, og aldri
  oversatt: `orgId`, `POST /v1/meldinger`.
- Forklar fagord første gang når leseren ikke er utvikler.
- Ikke `Merk:` og `NB!` i hver andre setning. Er noe viktig, skriv det som en
  vanlig setning på riktig sted.

## README og teknisk dokumentasjon

README i Fiks-repoer kan være på norsk eller engelsk; følg det repoet allerede
bruker. Er den norsk:

- Første avsnitt sier hva komponenten gjør, hvem som eier den, og hvordan man
  kjører den lokalt.
- Overskrifter på norsk, kodeord på engelsk: `## Kom i gang`, `## Konfigurasjon`,
  `## Kjør testene`. Ikke `## Getting started` i en norsk README.
- Bruk ordet teamet sier: `deploy`, `merge`, `workflow`, `branch`, `pipeline`,
  `container`, `pull request`, ikke `utrulling`, `flette`, `arbeidsflyt` eller `gren`.
  Bøy dem på norsk: `deployes`, `merget`, `workflowen`, `branchen`, `PR-en`, `imaget`.
  Se «Utviklerord» i [ordliste.md](ordliste.md).
- Sammensetninger med engelsk fagord får bindestrek: `deploy-skript`,
  `Docker-image`, `pull request-flyt` (eller skriv om).

## API-beskrivelser

Beskrivelsesfelt i OpenAPI-spesifikasjoner og API-dokumentasjon.

- Skriv på det språket spesifikasjonen ellers bruker. Er den norsk, er
  beskrivelsene norsk, mens felt, parametre, enum-verdier og feilkoder aldri
  oversettes.
- **Én setning som sier hva operasjonen gjør, i presens, uten «Denne operasjonen
  …»:** `Henter alle meldinger for en konto.` Ikke `Dette endepunktet lar deg hente
  …`.
- Feltbeskrivelser er substantivfraser eller korte setninger uten punktum hvis de
  er én linje: `Organisasjonsnummer til avsender, ni siffer`.
- Ikke `Returnerer` som første ord i beskrivelsen av en GET; si hva leseren får.

## Commit-meldinger og PR-beskrivelser

Følg språket repoet bruker. Er det norsk:

- **Emnelinjen følger formen repoet bruker.** Les de siste commitene: prefiks eller
  ikke (`backend:`, `docs:`, `feat:`), stor eller liten forbokstav etter prefikset,
  imperativ (`Legg til validering`) eller en setning om det som nå stemmer (`docs:
  deploy, ikke utrulling`). Har repoet ingen fast form, skriv imperativ, kort, uten
  punktum og med bare første ord stor: `Legg til validering av organisasjonsnummer`,
  `Rett kommafeil i feilmeldinger`. Ikke `Lagt til …`, ikke `Fikset …`.
- Konvensjonelle prefikser kan stå på engelsk (`feat:`, `fix:`, `chore:`) hvis
  repoet bruker dem; resten av linjen på norsk.
- **Brødtekst sier hvorfor**, ikke hva (diffen sier hva): `Kommuner med
  organisasjonsnummer på ti siffer ble avvist uten forklaring.`
- **PR-beskrivelse:** hva endringen gjør, hvorfor, hvordan den er testet, hva
  den som ser på den, bør se nærmest på. Ingen `Denne PR-en …` som innledning. Gå
  rett på.
- **Har repoet en PR-mal, fyll den ut** i stedet for å lage din egen oppbygning.
- **Med squash blir PR-tittelen og PR-beskrivelsen commit-meldingen på `main`.** Skriv
  dem som en commit-melding: hva som endres og hvorfor.
- **Testing:** `Prøvd:` for det du har kjørt, og `Gjenstår å teste:` for det som ikke
  er prøvd ennå, med hva som gjenstår (`Hele flyten med en ekte lommebok.`). Ikke
  `Ikke testet ennå`: det leses som en mangel, ikke som neste steg.
- **Ingen `Co-Authored-By`, `Generated with` eller annen attribusjon** til verktøy
  eller modell, verken i commit-meldingen eller i PR-en.
- Jira-nøkler og issue-referanser står som de er.

## Tekst i kode, CI og verktøy

Følg repoets egen regel hvis det har en. Har det ingen, er dette utgangspunktet:

- **Kodekommentarer** har ett språk per blokk og står bare der de forklarer hvorfor.
  Fagord som står på engelsk i koden, står på engelsk i kommentaren også.
- **Stegnavn i CI** er norske, fordi en person leser dem i PR-en: `Typesjekk`,
  `Formatering`, `Tester`. Jobbnavn er identifikatorer og står som de er.
- **Det et skript eller en CLI skriver til en person**, er norsk: meldinger,
  feilmeldinger og hjelpetekst.
- **Verktøy- og skjemabeskrivelser som en språkmodell leser**, er engelske, fordi de er
  modellens prompt. De norske domeneordene står i dem: `Get one organisation by
  organisasjonsnummer.`

## Løfter og kontaktinformasjon

Gjelder SECURITY.md, kontaktsider, README, PR- og issue-maler, feilmeldinger og e-post.

- **Lov aldri en svartid.** Skriv `Vi kommer tilbake til deg så raskt vi kan`, ikke
  `Du får svar innen en uke` eller `Vi svarer innen 48 timer`. Det gjelder også når
  bestillingen ber om en frist: skriv det uforpliktende og si fra at du endret det.
- **Ikke skriv en e-postadresse, et telefonnummer eller en annen kanal** som ingen har
  bekreftet finnes og er den riktige. At adressen står i en bestilling eller på en
  nettside, er ikke en bekreftelse. Pek heller på kanaler som virker: GitHubs «Report a
  vulnerability», teamet i `CODEOWNERS`, en sak eller en pull request.

## Jira-saker

- **Tittel:** hva som skal gjøres eller hva som er galt, i én linje, ingen punktum:
  `Meldinger over 10 MB avvises uten feilmelding`. Ikke `Feil i meldinger`.
- **Feilrapport:** hva skjedde, hva forventet du, hvordan reprodusere, miljø.
  Korte setninger, ikke fortelling.
- **Brukerhistorie**, hvis teamet bruker det: `Som saksbehandler i kommunen vil jeg
  … slik at …`. Skriv det på norsk, ikke `Som en bruker …` (uten artikkel: `Som
  bruker`).
- Akseptansekriterier som punktliste med parallell form.

## E-post og varsler

- **Emnefeltet sier hva det gjelder og eventuelt hva mottakeren skal gjøre:**
  `Fiks-porten: planlagt nedetid 16. oktober kl. 18–20`, `Svar innen fredag:
  testmiljø for Fiks IO`.
- **Hilsen:** `Hei, Anna` eller `Hei Anna`. Begge er riktige, uten komma etter.
  `Hei` alene uten tegn. Til en kommune som organisasjon: `Hei` eller `Til
  Bergen kommune`.
- **Første setning er saken.** Ikke `Håper alt står bra til`, ikke `Jeg skriver til
  deg fordi`.
- **Avslutning uten komma, tittel med liten forbokstav:**

  ```text
  Vennlig hilsen
  Kari Nordmann
  produkteier, Fiks-porten
  KS Digital
  ```

- `Med vennlig hilsen` og `Vennlig hilsen` er begge riktige. Ikke `Mvh.` til
  eksterne. Ikke `Beste hilsen` (engelsk), ikke `Hilsen Kari` i formell e-post.
- **Varsler om drift:** hva skjer, når, hvem berøres, hva de må gjøre, hvor de
  finner mer. I den rekkefølgen. Ikke `Vi beklager ulempen dette medfører`; si
  heller hva vi gjør for å unngå det neste gang, hvis det er sant.

## Rapporter og beslutningsunderlag

- **Sammendrag først**, i klarspråk, uten sjargong. Det leses av folk som ikke er
  utviklere.
- **Anbefalingen tidlig og tydelig.** Ikke gjem den i konklusjonen.
- Prosa framfor punktlister i resonnementer; punktlister for parallelle enheter
  (alternativer, krav, tiltak).
- Tall med kilde og dato. `120 kommuner (per september 2026)`.
- Ikke oppblåste ord. En rapport som sier at løsningen er «robust og sømløs», sier
  ingenting. Si hva som er målt.
