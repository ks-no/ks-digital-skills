---
name: norsk-sprakvask
description: >-
  Skriv og språkvask norsk bokmål etter Språkrådets normer og klarspråksrådene for
  offentlig sektor, tilpasset KS Digital og kommunesektoren. Bruk denne hver gang
  du skriver eller retter norsk tekst som andre skal lese: grensesnittekster,
  feilmeldinger, brukerdokumentasjon, README, API-beskrivelser, commit-meldinger,
  PR-beskrivelser, Jira-saker, e-post og notater til kommuner eller kolleger.
  Bruk den også når brukeren sier «språkvask», «korrektur», «rydd opp i teksten»,
  «skriv dette på norsk», «høres dette engelsk ut?» eller «fjern KI-preget», og
  når du selv genererer norsk tekst uten at noen har bedt om språkvask, fordi
  språkmodeller systematisk skriver norsk med engelsk setningsbygning, engelsk
  tegnsetting og inkonsekvente former. Bruk den også når du skal velge mellom et
  norsk og et engelsk fagord, som «fletting» eller «merge».
---

# Norsk språkvask

Norsk tekst som leses som om den er skrevet av en som kan norsk, ikke oversatt fra
engelsk av en maskin.

## Hvorfor denne skillen finnes

Språkrådet har målt språkkvaliteten i tekst fra ChatGPT, Copilot, Le Chat og
NorMistral. Alle gjorde 1,3–2,2 feil per 100 ord på bokmål og 2,3–3,3 på nynorsk,
altså omtrent én feil i annenhver setning på nynorsk. Feilene er sjelden stavefeil.
De er engelsk setningsbygning og fraseologi som skinner gjennom, tilfeldig veksling
mellom likestilte former, konservative former, engelsk tegnsetting, særskriving og
kommafeil. På toppen kommer et gjenkjennelig KI-preg: oppblåste ord, tomme
innledninger og tvungne tredelinger.

Dette er ikke kosmetikk. KS Digital skriver for kommuner, fylkeskommuner og
leverandører som leser mye tekst fra oss. Tekst med engelsk rytme og «Vennligst
merk at» koster leseren tid og svekker tilliten til at vi kan faget vårt.

## Når den gjelder

Alltid når teksten er norsk og skal leses av mennesker:

- grensesnittekster: knapper, ledetekster, feilmeldinger, tomme tilstander
- brukerdokumentasjon, veiledninger, README-filer og API-beskrivelser
- commit-meldinger, PR-beskrivelser og Jira-saker skrevet på norsk
- e-post, varsler og notater til kommuner, leverandører og kolleger
- rapporter, sammendrag og beslutningsunderlag

Den gjelder **ikke** identifikatorer, se under.

Skillen dekker bokmål. Ber brukeren om nynorsk, si det tydelig og be om at teksten
enten skrives på bokmål og oversettes med et regelbasert verktøy (for eksempel
Nynorskroboten fra NTB Arkitekst eller Nynorobot fra Nynodata), eller går til en
person som skriver nynorsk. Ikke generer nynorsk direkte uten å si at kvaliteten er
vesentlig lavere.

### Prosa eller identifikator

Avgjør dette først, hver gang. **Prosa** er det et menneske leser som språk: markdown,
kommentarer og strenger som skrives ut, vises eller logges. **Identifikator** er alt
annet: navn i kode, JSON-nøkler, API-felt, URL-stier, query-parametre, enum- og
statusverdier, kodeverk, loggnøkler, CSS-klasser, miljøvariabler og skriptnavn.

Språkvask endrer prosa. Den endrer aldri en identifikator, heller ikke for å rette en
skrivefeil. En identifikator er en referanse, og det den peker på, bytter ikke
skrivemåte. `orgId` skal ikke bli `organisasjonsId`. Er du i tvil om hvilken side en
streng står på, er den en identifikator.

**En streng som sammenlignes med det brukeren skriver, er et mønster.** Står den i en
`in`-test, `startswith`, `endswith`, et regulært uttrykk eller en liste det søkes i, og
den andre siden kommer fra et skjema, en forespørsel eller et søkefelt, skal den treffe
det folk faktisk skriver. Folk skriver `kjor pa`, `ma jeg` og `nar` uten æ, ø og å.
Retter du stavingen, forsvinner halvparten av treffene uten at noe feiler: ingen test
blir rød, sjekken slutter bare å slå til. Rør den ikke.

**Sitater beholder sin egen skrivemåte:** lovnavn (`opplæringslova`), tekst hentet fra
en kommunes skjema og nynorsk som et team har skrevet. Egennavn på produkter og
tjenester skrives slik eieren skriver dem: Fiks-porten, Altinn, ID-porten.

## Arbeidsmåte

Språkmodeller får bedre resultat når de skriver først og retter etterpå, i faste
gjennomganger, enn når de prøver å gjøre alt i én omgang. Derfor:

1. **Avklar register og mottaker om det er uklart.** Standard for KS Digital er
   profesjonelt nøytralt bokmål med «du» til leseren. Formelt (til ledelse, i
   avtaletekst) og uformelt (chat, interne notater) er unntak brukeren må be om.
   Tiltale: «du» til én person eller til den som sitter med skjermen; «dere» i
   utsendelser til kommuner som organisasjoner (driftsvarsler, informasjonsbrev).
   Har teksten både tekniske og ikke-tekniske lesere, skriv for de ikke-tekniske
   og la fagordet stå i parentes første gang: «prøver på nytt (retry)».
2. **Skriv eller rett teksten.** Hold deg til meningen. Språkvask endrer form, ikke
   innhold. Er noe faktisk uklart eller feil i innholdet, si det separat i stedet
   for å gjette deg til en rettelse.
3. **Gå gjennom sjekkene under, én om gangen.** De står i den rekkefølgen feilene
   faktisk forekommer i maskinskrevet norsk. Les teksten én gang per sjekk; det
   fanger mer enn én lesning der du ser etter alt.
4. **Er teksten lengre enn et avsnitt, les [klarsprak.md](references/klarsprak.md).**
   Rettskriving gjør teksten riktig. Klarspråk gjør at den blir lest.
5. **Skriver du en bestemt teksttype**, se [teksttyper.md](references/teksttyper.md)
   for grensesnitt, feilmeldinger, dokumentasjon, commit og PR, Jira og e-post.
6. **Sjekk terminologi** mot [ordliste.md](references/ordliste.md) når teksten
   handler om Fiks, kommunesektoren eller teknologi med etablerte norske ord. Om et
   fagord skal stå på norsk eller engelsk, avgjør du etter regelen «Fagord skrives slik
   det står på tingen» under «Etter sjekkene».

Referansefilene lastes én om gangen og bare ved behov. Sjekkene nedenfor dekker det
meste.

## Sjekkene

### 1. Engelsk smitte i ordvalg og vendinger

Den største gruppen. Ordene er norske, men setningen er tenkt på engelsk.

| Oversatt fra engelsk | Norsk |
| --- | --- |
| når det kommer til | når det gjelder |
| ta plass (take place) | finne sted, skje |
| la meg vite / gi meg beskjed om | si fra |
| vennligst fyll ut | fyll ut |
| du trenger å | du må |
| adressere et problem | ta tak i, løse |
| fasilitere | legge til rette for, lede |
| lokasjon | sted, plassering |
| utnytte (leverage) | bruke, dra nytte av |
| implementere en løsning | innføre, ta i bruk, utvikle |
| tilby en mulighet (offer) | gi en mulighet |
| for nå (for now) | foreløpig, inntil videre |
| over tid (over time) | etter hvert, med tiden |
| møte et behov / krav | dekke et behov, oppfylle et krav |
| i tillegg til dette | dessuten, i tillegg |
| gjøre en forskjell | bety noe, ha betydning |
| fokus på | vekt på, oppmerksomhet om, eller skriv om |

Se [engelsk-smitte.md](references/engelsk-smitte.md) for flere vendinger, lånte
betydninger og grammatisk smitte som `deres` for `sin` og foranstilt eiendomsord.

### 2. Én form per ord, og moderne former

Bokmål har mange likestilte former. Modellene veksler tilfeldig mellom dem (`frem`
og `fram`, `nå` og `nu`, `boken` og `boka`), ofte i samme avsnitt, og trekker mot
de mest konservative. Regelen er enkel:

- **Retter du en tekst**, følg formene teksten allerede bruker mest, og gjør den
  konsekvent.
- **Skriver du ny tekst**, bruk formene i [ordliste.md](references/ordliste.md)
  under «Husnorm». De er moderate og vanlige i offentlig sektor. Husnormen har `-en` i
  bestemt form: `filen`, `listen`, `roten`, aldri `fila`, `lista`, `rota`.
- **Rett aldri en form som er tillatt** til favoritten din. Jobben er konsekvens,
  ikke smak.

### 3. Bindestrek og anførselstegn

- **I en setning er streken en bindestrek med mellomrom** (` - `, U+002D): `Vi ses
  lørdag - alle får det samme.` Ofte gjør komma, kolon eller punktum jobben bedre, se
  sjekk 10.
- **Bindestrek i intervaller** (–, U+2013) står uten mellomrom, mellom tall: `kl. 9–15`,
  `16.–18. oktober`, `2024–2026`.
- Dette er et husvalg for tekst vi skriver. Språkrådets norm har ` – ` med mellomrom i
  setninger, så en tekst fra andre som gjør det konsekvent, er ikke feil.
- **Lang bindestrek (U+2014) finnes ikke i norsk.** Den er det sikreste
  enkelttegnet på oversatt eller maskinskrevet tekst. Å bytte den mot en kortere strek
  retter tegnet, men ikke vanen den kom fra, se sjekk 10.
- **Anførselstegn er «…»**, ikke "…". Komma står utenfor: `«Vi ses», skrev hun.`
  Sitat i sitat: `‘…’`.
- **Ikke apostrof i genitiv:** `Olas bil`, `NAVs skjema`, `EUs regler`, `Fiks-portens
  API`. Apostrof bare når navnet slutter på s, x eller z: `KS' tjenester`, `Anders'
  bil`. Bøyning av forkortelser med bindestrek: `pc-en`, `API-et`, `sms-en`, ikke
  `pc'en`.

### 4. Komma: færre enn på engelsk, men på noen andre steder

- **Ikke komma foran `og`** i oppramsinger (ikke Oxford-komma): `kommuner,
  fylkeskommuner og leverandører`.
- **Ikke komma etter innledende uttrykk uten verb:** ✗ `For å logge inn, må du …`
  → ✓ `For å logge inn må du …`
- **Komma etter leddsetning som står først:** `Når tokenet er utløpt, må du hente
  et nytt.`
- **Komma mellom to helsetninger**, og alltid foran `men`.
- **Komma etter innskutt leddsetning:** ✗ `Meldinger som ikke er kvittert
  slettes` → ✓ `Meldinger som ikke er kvittert, slettes`. Dette er den kommafeilen
  Språkrådet oftest fant i KI-tekst.

Detaljer i [tegnsetting-tall-datoer.md](references/tegnsetting-tall-datoer.md).

### 5. Sammensatte ord skrives i ett

Særskriving er den mest utbredte feilen i norsk, og den endrer betydning. Engelsk
skriver `user name`; norsk skriver `brukernavn`.

- ✗ `bruker navn`, `tilgangs styring`, `test miljø`, `integrasjons punkt`
- ✓ `brukernavn`, `tilgangsstyring`, `testmiljø`, `integrasjonspunkt`
- Sammensetning med egennavn eller forkortelse får bindestrek: `Fiks-tjeneste`,
  `API-nøkkel`, `OAuth2-klient`, `Jira-sak`.
- Noen uttrykk skal likevel stå i flere ord: `i dag`, `i gang`, `til stede`, `for
  øvrig`, `etter hvert`, `en del`.

### 6. Stor forbokstav bare der norsk har det

- **Overskrifter og knapper:** bare første ord. ✗ `Legg Til Ny Bruker` → ✓ `Legg til
  ny bruker`.
- **Titler og stillinger er små:** `daglig leder`, `produkteier Kari Nordmann`,
  `avdelingsdirektør`.
- **`du`, `deg`, `din` er alltid små.** Stor `Du` er feil, ikke høflig.
- **Måneder, ukedager, språk, nasjonaliteter og fag er små:** `mandag 16. oktober`,
  `norsk`, `informatikk`.
- **Institusjoner har stor forbokstav bare i første ord:** `Kommunal- og
  distriktsdepartementet`, `Digitaliseringsdirektoratet`, `Bergen kommune`.
  Unntak er egennavn med egen skrivemåte: `KS Digital`, `Fiks-porten`.

### 7. Tall, beløp, datoer og klokkeslett

- Tusenskille er mellomrom, desimalskille er komma: `1 000`, `12 500 kroner`,
  `3,5 sekunder`. Aldri `1,000` eller `3.5`.
- `25 %` med mellomrom, eller `25 prosent`.
- `16. oktober 2026` eller `16.10.2026`. Aldri skråstrek, aldri `2026-10-16` i
  løpende tekst (fint i filnavn og logger).
- `kl. 09.00` og `kl. 09:00` er begge riktige. Velg ett og hold deg til det.
- `innen 1. oktober` er tvetydig. Skriv `senest 1. oktober` eller `fristen er
  1. oktober`.

### 8. Eiendomsord etter substantivet

Norsk foretrekker bestemt form med etterstilt eiendomsord. Foranstilt er tillatt,
men er engelsk rytme og legger trykk på eieren.

- ✗ `din konto`, `ditt token`, `dine innstillinger`, `vår løsning`
- ✓ `kontoen din`, `tokenet ditt`, `innstillingene dine`, `løsningen vår`

Unntak: når trykket faktisk skal ligge på eieren (`det er *ditt* ansvar, ikke
leverandørens`).

### 9. Aktiv framfor passiv, verb framfor substantiv

Engelsk fagspråk og KI-tekst er tunge på passiv og på verb som er gjort om til
substantiv («substantivsyke»). Norsk klarspråk vil ha den som handler, og verbet.

- ✗ `Det ble foretatt en vurdering av behovet for endring av konfigurasjonen.`
- ✓ `Vi vurderte om konfigurasjonen måtte endres.`
- ✗ `Innsending gjøres ved å trykke på knappen.` → ✓ `Trykk på knappen for å sende
  inn.`

Passiv er riktig når den som handler er ukjent eller uinteressant: `Meldingen ble
levert kl. 14.02.`

### 10. KI-preg

Tekst som er riktig, men som alle ser er skrevet av en maskin.

- **Stryk innledninger og avslutninger uten innhold:** `Det er verdt å merke seg
  at …`, `I dagens digitale landskap …`, `Kort oppsummert …`, `Avslutningsvis …`,
  og et siste avsnitt som gjentar hele teksten.
- **Ikke oppblåste ord:** `sømløs`, `robust`, `banebrytende`, `helhetlig`,
  `holistisk`, `avgjørende`, `essensiell`, `betydelig`. Si hva det faktisk gjør.
- **Ikke oversatte favoritter:** `dykke ned i` → gå rett på; `reise` (journey) →
  prosess, forløp; `landskap` → område, marked; `sikre at` (ensure) → sørge for
  at, passe på at, eller stryk.
- **Ikke tvungne tredelinger, retoriske spørsmål som overskrifter, kolon i hver
  overskrift, fet skrift overalt eller emoji som punktmarkører.**
- **Ikke falsk balanse** («på den ene siden … på den andre siden») når teksten
  faktisk har et standpunkt.
- **Ikke bindestrek som rytme.** Mer enn én i et avsnitt er en vane, ikke et valg,
  og den overlever at tegnet byttes ut: ` - ` er like mye en vane som lang bindestrek
  (U+2014). Komma, punktum, kolon eller parentes gjør som regel jobben bedre.
- **Én tanke per setning, korte setninger.** Modellene lager lange setninger med
  mange innskudd fordi engelsk tåler det bedre enn norsk.

Se [ki-markorer.md](references/ki-markorer.md).

### 11. Forkortelser

- `ev.` (eventuelt), `ift.` (i forhold til), `md.` (måned), `osv.`, `f.eks.`,
  `bl.a.`, `mht.`, `jf.`, `pga.`, ikke `evt.`, `ifht.`, `mnd.` og `etc.`
- I løpende tekst er det oftest bedre å skrive ordet ut.
- `KI` i formell tekst og i tekst til kommuner, `AI` er greit i uformell teknisk
  tekst. `API`, `URL`, `JSON` og andre tekniske forkortelser står som de er.

### 12. E-posthilsener og signaturer

- `Hei, Anna` (komma foran navnet) og `Hei Anna` er begge godtatt. Aldri komma
  etter navnet på samme linje, og `Hei` alene står uten tegn.
- Avslutningen har ikke komma, og tittelen har liten forbokstav:

  ```text
  Vennlig hilsen
  Kari Nordmann
  produkteier, Fiks-porten
  ```

- Ikke `Mvh.` i e-post til kommuner eller leverandører. Skriv ordene ut.
- Ikke `Vi beklager ulempen`. Si hva som skjedde og hva som skjer nå.

## Etter sjekkene

Si kort hva du rettet, og bare det som betyr noe: «Rettet særskriving i fire
overskrifter, byttet ut sju oversatte vendinger og gjorde formvalget konsekvent (fram,
ikke frem).» En liste over hvert komma er støy.

**Ikke rett det som er riktig.** Likestilte former er likestilte.

**Fagord skrives slik det står på tingen.** Gå gjennom disse i rekkefølge, og stopp ved
det første som passer:

1. Identifikatorer står uendret.
2. Lesere som ikke er utviklere, får det norske ordet (`sette i drift`). Står det
   engelske ordet i verktøyet de bruker, står det i parentes første gang
   (`tilgangsnøkkel (token)`). Leser også utviklere teksten, gjelder trinn 1 i
   arbeidsmåten.
3. Begreper fra forvaltning, juss og kommunesektoren står på norsk (`organisasjonsnummer`,
   `vedtak`).
4. Et norsk ord som teamet og repoet faktisk bruker, står (`bygg`, `endepunkt`).
5. Ellers står verktøyets eget ord på engelsk og bøyes slik tabellen «Utviklerord» i
   ordliste.md viser (`merge`, `merget`; `branch`, `branchen`; `workflow`, `workflowen`;
   `deploy`, `deployes`; `PR-en`; `tokens`). Ikke oversett dem til
   `flette`, `gren`, `arbeidsflyt` eller `utrulling` i tekst til utviklere.

Bruk samme ord gjennom hele teksten. Er du i tvil, les «Fagord: norsk eller engelsk» i
[ordliste.md](references/ordliste.md), som har eksempler og standardleser per teksttype.

**Skal teksten ikke kunne misforstås**, som i instruksjoner, feilmeldinger og
driftsvarsler, bruk også skillen `asd-ste100-norsk`. Den tar setningsbygningen, og denne
skillen tar rettskrivingen.

**Er du i tvil om et ord eller en bøyning, slå det opp** i Bokmålsordboka på
ordbokene.no i stedet for å gjette. Ordbøkene er fasiten for gjeldende rettskriving.
Gjetter du likevel, si at du gjettet. Bruk ikke egen språkfølelse som kilde til
«regler»: språkmodeller hallusinerer språkregler like gjerne som fakta.

## Referanser

| Fil | Når |
| --- | --- |
| [engelsk-smitte.md](references/engelsk-smitte.md) | Oversatte vendinger, lånte betydninger, grammatisk smitte, engelsk tegnsetting |
| [ki-markorer.md](references/ki-markorer.md) | Oppblåste ord, tomme fraser og strukturmønstre som avslører KI-tekst |
| [tegnsetting-tall-datoer.md](references/tegnsetting-tall-datoer.md) | Komma, kolon, punktlister, tall, beløp, datoer, klokkeslett, paragrafer |
| [klarsprak.md](references/klarsprak.md) | Klarspråk for offentlig sektor: leseren først, struktur, setninger, ordvalg, digitale tjenester |
| [teksttyper.md](references/teksttyper.md) | Grensesnitt, feilmeldinger, dokumentasjon og README, API-beskrivelser, commit og PR, tekst i kode og CI, løfter og kontaktinformasjon, Jira, e-post |
| [ordliste.md](references/ordliste.md) | Husnorm for formvalg, regelen for norsk eller engelsk fagord, utviklerord, KS- og kommuneterminologi, norske ord for teknologibegreper |

## Kilder og opphav

Normene er Språkrådets: rettskrivingsreglene, skriverådene og klarspråkssidene på
sprakradet.no, og Bokmålsordboka på ordbokene.no. Tallene om KI-feil er fra
Språkrådets «Rapport om språklig kvalitet i tekster produsert av prateroboter» (2025).
Klarspråksrådene bygger på Språkrådets og Digitaliseringsdirektoratets veiledning for
klart språk i digitale tjenester.

Sjekklistens oppbygning og flere eksempler er inspirert av de åpne
(MIT-lisensierte) skillene `sivert-io/sprakvask` og `bokmaal-proof` fra
`tenki-labs/public-claude-skills`. Denne skillen er skrevet for KS Digital og er ikke
utgitt av eller godkjent av Språkrådet.
