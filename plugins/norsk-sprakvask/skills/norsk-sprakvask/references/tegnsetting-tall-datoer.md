# Tegnsetting, tall og datoer

Reglene her følger Språkrådets skriveregler. Ved tvil om et konkret tilfelle: slå
opp på sprakradet.no i stedet for å resonnere deg fram til en regel.

## Komma

Norsk har færre komma enn engelsk, men noen står på andre steder. De fem reglene som
dekker nesten alt:

1. **Komma mellom to helsetninger** som er bundet sammen med `og`, `men`, `for`,
   `så`, `eller`: `Tjenesten er oppe igjen, og alle meldinger er levert.` Alltid
   komma foran `men`.
2. **Komma etter leddsetning som står først:** `Hvis tokenet er utløpt, får du
   401.` `Når du har lagret, kan du lukke vinduet.`
3. **Komma etter innskutt leddsetning**, ikke foran, når leddsetningen er nødvendig
   for meningen: `Meldinger som ikke er kvittert innen 24 timer, slettes.`
   `Kommuner som har tatt i bruk tjenesten, får varsel.` Dette er den kommafeilen
   som oftest mangler i KI-tekst.
4. **Komma rundt unødvendige innskudd** (kan strykes uten at meningen endres):
   `Fiks-porten, som ble lansert i 2023, brukes av …`
5. **Ikke komma** foran `og` i oppramsing, etter innledende uttrykk uten verb (`For
   å logge inn må du …`, `I 2025 lanserte vi …`), eller mellom subjekt og verbal.

Komma foran `at`, `om`, `fordi`, `som` bare når regel 3 eller 4 gjelder, ikke som
standard.

## Punktum, kolon og semikolon

- **Kolon** foran oppramsing, forklaring eller sitat. Etter kolon: liten forbokstav
  hvis det som følger ikke er en hel setning, stor hvis det er en hel setning eller
  et sitat.
- **Semikolon** er sjelden nødvendig. Det står mellom to helsetninger som hører
  tett sammen, aldri foran en oppramsing (der er det kolon).
- **Punktum i overskrifter:** nei. I knapper og ledetekster: nei. I feilmeldinger
  på én hel setning: ja, hvis det er flere setninger; ellers valgfritt, men vær
  konsekvent i samme grensesnitt.
- **Bare ett punktum** når en setning slutter med en forkortelse: `… mat, drikke
  osv.`

## Bindestrek

- **Bindestrek (-, U+002D)** i sammensetninger: `Fiks-porten`, `API-nøkkel`, `e-post`,
  `to-faktor-autentisering` (eller `tofaktorautentisering`), og ved sideordning:
  `inn- og utlogging`.
- **Bindestrek med mellomrom** (` - `) som innskudd i en setning: `Vi lanserer i mai -
  hvis testene er grønne.` Ofte er komma, kolon eller punktum bedre. Dette er husvalget
  for tekst vi skriver; Språkrådets norm har ` – ` med mellomrom, så en tekst fra andre
  som gjør det konsekvent, er ikke feil.
- **Bindestrek i intervaller (–, U+2013)** som «fra–til» uten mellomrom: `kl. 9–15`,
  `2024–2026`, `s. 12–14`. Ikke `fra kl. 9–15` (`fra … til` eller strek, ikke begge).
- **Lang bindestrek (U+2014)** brukes ikke i norsk.
- **Minus** i tall er den samme streken som i intervaller: `–5 °C`.

## Anførselstegn og apostrof

- Anførselstegn: `«…»`. Sitat i sitat: `‘…’` eller `"…"` når «» allerede er i
  bruk. Komma og punktum står utenfor: `«Vi ses», skrev hun.` Spørsmålstegn som
  hører til sitatet, står innenfor: `«Kommer du?» spurte hun.`
- Ord som omtales, kan stå i anførselstegn eller kursiv: knappen «Lagre» eller
  knappen *Lagre*. Velg ett per tekst.
- Apostrof bare i genitiv av navn på s, x, z (`KS' løsninger`, `Anders' oppgave`) og
  ved utelatte bokstaver. Aldri `Ola's`, aldri `pc'en`.

## Punktlister

- Innledes med en setning som slutter på kolon.
- Punkter som er hele setninger: stor forbokstav og punktum.
- Punkter som fortsetter innledningssetningen eller er stikkord: liten forbokstav,
  ingen punktum (heller ikke etter siste punkt).
- Alle punkter i samme liste har samme form: alle imperativ, alle substantiv, alle
  hele setninger. Ikke bland.
- Ikke fet frase med kolon først i hvert punkt som standardmønster. Det er et
  KI-mønster.

## Tall

- **Tusenskille er mellomrom**, helst hardt mellomrom: `1 000`, `12 500`,
  `3 200 000`. Firesifrede tall kan stå uten: `1000` eller `1 000`. Vær konsekvent.
- **Desimalskille er komma:** `3,5`, `0,25`. Aldri punktum.
- **Tall til og med tolv skrives med bokstaver** i løpende tekst (`tre kommuner`,
  `sju dager`), større tall med siffer. Unntak: tekniske tekster og tabeller, der
  siffer er greit hele veien. Vær konsekvent innenfor én setning: `3 av 15`, ikke
  `tre av 15`.
- **Prosent:** `25 %` med mellomrom, eller `25 prosent`. Ikke `25%`.
- **Beløp:** `450 kroner`, `450 kr` (uten punktum), `1,2 millioner kroner`,
  `12 500 000 kr`. Valutakode etter tallet: `450 NOK` bare i tekniske sammenhenger.
- **Telefonnummer:** `22 00 32 00`, mobil `912 34 567`. Med landkode: `+47 912 34
  567`.
- **Store tall i tekst til ledelse:** `1,2 millioner` er lettere å lese enn
  `1 200 000`.

## Datoer og klokkeslett

- Dato i prosa: `16. oktober 2026` eller `16.10.2026`. Ikke `16/10`, ikke
  `16.10.26`, ikke `2026-10-16` (ISO-formatet hører hjemme i filnavn, logger, JSON
  og tabeller som skal sorteres).
- Ukedag: `mandag 16. oktober`, med liten forbokstav og uten komma mellom dag og dato.
- Klokkeslett: `kl. 09.00` eller `kl. 09:00`. Begge er riktige, velg ett. Hele
  timer kan skrives `kl. 9`. Ikke `9am`, ikke `09.00 timer`.
- Tidsrom: `kl. 9–15`, `16.–18. oktober`, `2024–2026`.
- **Frister:** `innen 1. oktober` er tvetydig (er 1. oktober med?). Skriv `senest
  1. oktober`, `fristen er 1. oktober` eller `før 1. oktober`.
- Varighet: `3 timer`, `2,5 timer`, `10 minutter`. Ikke `3t`, ikke `10 min.` i prosa.

## Paragrafer og henvisninger

- `§ 5`, `§ 5 andre ledd`, `§§ 5–7`, med mellomrom etter paragraftegnet.
- Lovnavn med liten forbokstav og gjerne kortform: `personopplysningsloven`,
  `forvaltningsloven § 11`, `GDPR artikkel 6`.
- `jf.` (jamfør) for henvisning, `se` når leseren skal slå opp.

## Stor og liten forbokstav, kort

- Overskrifter, knapper, menypunkter: bare første ord.
- Titler og stillinger: små (`daglig leder`, `produkteier`).
- `du`, `deg`, `din`: alltid små.
- Ukedager, måneder, høytider, språk, nasjonaliteter, fag: små.
- Institusjoner og offentlige organer: stor forbokstav i første ord
  (`Digitaliseringsdirektoratet`, `Kommunal- og distriktsdepartementet`,
  `Bergen kommune`, `Vestland fylkeskommune`). Kortformer som er blitt egennavn:
  `Digdir`, `KS`, `NAV`, `Skatteetaten`.
- Produkter og tjenester: som eieren skriver dem (`Fiks-porten`, `ID-porten`,
  `Altinn`, `Maskinporten`).
- Etter kolon: liten hvis det som følger ikke er en hel setning.
