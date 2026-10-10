# Ordliste og husnorm

To ting i én fil: formvalgene vi bruker når vi skriver ny tekst (husnorm), og
hvilke ord vi bruker om det vi jobber med (terminologi og utviklerord).

Husnormen er et forslag til KS Digital og kan endres av teamet. Poenget er ikke
hvilke former som velges, men at samme tekst bruker samme form hele veien. Ved
språkvask av eksisterende tekst gjelder alltid tekstens egne former først.

## Husnorm for ny tekst

Moderat bokmål, slik det er vanlig i offentlig sektor i dag. Alle formene er
tillatt etter gjeldende rettskriving; dette er valg, ikke regler.

| Velg | Ikke | Merknad |
| --- | --- | --- |
| fram, framover, framdrift | frem, fremover, fremdrift | språkmodeller trekker mot `frem` |
| nå | nu | |
| sju, tjue, tretti | syv, tyve, tredve | |
| bare | kun | `kun` er tillatt, men stivt |
| også | òg | |
| senere, senest | seinere, seinest | begge tillatt; velg én |
| hvis | dersom, såfremt | `dersom` er greit i avtaletekst |
| bruke | benytte, anvende | |
| få, sende | motta, oversende | |
| tid, tidspunkt | | ikke `på nåværende tidspunkt`, skriv `nå` |
| filen, boken, listen | fila, boka, lista | `-en` i bestemt form av hunkjønnsord, se under |
| og | samt | |
| personen, den det gjelder | vedkommende | |
| feil | usann | |
| stemmer | er sann, holder | om en påstand: `AGENTS.md stemmer fortsatt` |
| Gjenstår å teste | Ikke testet ennå | sier hva som er igjen, ikke hva som mangler |
| e-post | epost, mail, e-mail | Språkrådets form |
| nettside, nettsted | webside, website, hjemmeside | `hjemmeside` er forsiden |
| app, program, tjeneste | applikasjon | `applikasjon` når fagsammenhengen krever det |
| KI, kunstig intelligens | AI | `AI` er greit i uformell teknisk tekst |
| pålogging, logge inn / logge på | innlogging, login | velg `logge inn` eller `logge på` og hold på det |
| kl. 09.00 | kl. 09:00 | begge riktige; velg én per tekst |

Husnormen har `-en` i bestemt form av hunkjønnsord: `filen`, `listen`, `roten`,
`boken`, `tiden`, `meldingen`. Aldri `fila`, `lista`, `rota`. Retter du en tekst som
gjennomgående bruker `-a`, er den ikke feil; gjør den konsekvent i stedet for å bytte
form. Ikke bland i én tekst.

## Fagord: norsk eller engelsk

Prinsippet er lånt fra ASD-STE100: et fagord er et *teknisk navn*, og et teknisk navn
skrives slik det står på tingen. Gå gjennom spørsmålene i rekkefølge, og stopp ved det
første som passer:

1. **Er det en identifikator?** Navn i kode, kommandoer, felt og verdier står uendret:
   `orgnr`, `git rebase`. I markdown står de i kodeformat. I ren tekst, som logger og
   meldinger i et grensesnitt, står de uten backticks.
2. **Er leseren ikke utvikler?** Kommuner, saksbehandlere og ledelse får det norske ordet:
   `sette i drift`. Står det engelske ordet i verktøyet de bruker, skriv det i parentes
   første gang: `tilgangsnøkkel (token)`. Det samme gjelder når utviklere også leser
   teksten. Se tabellen «Teknologi» lenger ned.
3. **Er det et begrep fra forvaltning, juss eller kommunesektoren med et etablert norsk
   navn?** Bruk det: `innbygger`, `organisasjonsnummer`, `saksbehandler`, `vedtak`. Det
   gjelder også i engelsk tekst. Forklar det første gang hvis leseren ikke kjenner det.
   IT-ord hører ikke hit, selv om de har en norsk oversettelse.
4. **Bruker teamet og repoet allerede et norsk ord for det?** La det stå: `bygg`,
   `endepunkt`, norske stegnavn i CI. Testen er hva en norsk utvikler på teamet sier
   høyt. Et ord som bare står i repoet fordi en modell har oversatt det (`fletting`,
   `gren`), er ikke etablert.
5. **Ellers:** bruk ordet verktøyet selv har på tingen, bøyd slik tabellen «Utviklerord»
   viser: `merge`, `branch`, `workflow`, `secret`. Git har ingen knapp som heter «flette», og GitHub kaller det en
   workflow, ikke en arbeidsflyt.

Er leseren ikke oppgitt, gjelder dette: README, runbooks, commit-meldinger og PR-er er
til utviklere. Driftsvarsler og e-post til kommuner er til lesere som ikke er
utviklere.

Når ordet er valgt, bruker du det gjennom hele teksten. `endepunkt` i ett avsnitt og
`endpoint` i det neste leses som to ting. Det motsatte er like farlig: ett ord for to
ting. `merge` er både Git-merge og sammenslåing av konfigurasjon eller data. Står begge
i samme tekst, eller står `branch` i nærheten, skriv den andre som `sammenslåing`.

## Utviklerord

Tabellen viser skrivemåte og bøyning for vanlige ord fra steg 5 over.

| Skriv | Ikke | Merknad |
| --- | --- | --- |
| merge, merget, mergen | flette, flettet, fletting | `PR-en er merget` |
| workflow, workflowen, workflowene | arbeidsflyt, byggearbeidsflyt | om GitHub Actions |
| deploy, deploye, deployes, deployen | utrulling, rulles ut | `main deployes til dev` |
| branch, branchen, brancher | gren, grenen | `branchnavn` |
| pull request, PR-en, PR-er | | |
| push, rebase, squash, commit | | `pushet`, `rebaset`, `commiten` |
| secret, secreten | hemmelighet (om GitHub-secrets) | |
| token, tokenet, tokens | tokener | `tokenet er utløpt`, `hent nye tokens` |
| image, imaget; chart, chartet | | Docker-image, Helm-chart |
| tekststreng, tekststrengen, tekststrenger | streng (om string) | `streng` alene kan også bety «strict», slik ASD-STE100-skillene bruker ordet |

Til kommuner, saksbehandlere og ledelse gjelder tabellen «Teknologi» lenger ned.

## Kommunesektoren

Ord vi bruker om dem vi lager løsninger for.

| Bruk | Ikke | Merknad |
| --- | --- | --- |
| kommune, fylkeskommune | | små forbokstaver: `Bergen kommune`, `Vestland fylkeskommune` |
| kommunal sektor, kommunesektoren | kommunene (om hele sektoren) | sektoren omfatter også fylkeskommunene |
| innbygger | borger, bruker (om innbyggere) | `bruker` om den som bruker et system |
| saksbehandler | case worker, handler | |
| virksomhet | organisasjon, bedrift (om offentlige) | `bedrift` bare om private |
| leverandør | vendor, tredjepart (som eneste ord) | |
| fellesløsning | felles løsning, plattformtjeneste | i ett ord |
| fagsystem | | kommunens egne systemer, f.eks. sak-arkiv |
| sak- og arkivsystem, sak-arkivsystem | saksarkiv | velg én skrivemåte per tekst |
| organisasjonsnummer | org.nr. (i prosa), orgnr | `orgnr` bare som feltnavn |
| vedtak | beslutning (om forvaltningsvedtak) | |
| forvaltningen, offentlig sektor | det offentlige | |
| KS | Kommunenes Sentralforbund | KS er navnet |
| KS Digital | KS digital, KSD | |
| Digitaliseringsdirektoratet (Digdir) | DigDir | |
| Skatteetaten, NAV, Statsforvalteren | | som organene skriver dem |

## Fiks-plattformen

Skrivemåter for egne produkter. Egennavn skrives som eieren skriver dem, uavhengig
av reglene for store og små bokstaver.

| Skriv | Ikke | Merknad |
| --- | --- | --- |
| Fiks-plattformen | Fiks plattformen, FIKS | |
| Fiks-porten | Fiksporten, Fiks Porten, Fiks-portalen | Fiks-portalen finnes ikke |
| en Fiks-tjeneste, Fiks-tjenestene | Fiks tjeneste | bindestrek i sammensetning |
| Fiks-konto | Fiks konto | |

Teamet bør fylle ut denne tabellen med produktnavnene som er i bruk og
skrivemåten på hvert av dem, gjerne med en linje per tjeneste. Uten en slik liste
gjetter modellene, og de gjetter forskjellig fra gang til gang.

## Nasjonale fellesløsninger og aktører

| Skriv | Merknad |
| --- | --- |
| ID-porten, Maskinporten, Ansattporten | Digdirs skrivemåte, bindestrek bare i ID-porten |
| Altinn | |
| Folkeregisteret | ikke «Det sentrale folkeregister» i prosa |
| Kontakt- og reservasjonsregisteret (KRR) | |
| Enhetsregisteret | |
| eInnsyn, eSignering | små e-er er eiernes skrivemåte |
| Helsenorge, HelseID | |
| Datatilsynet, Arkivverket, Nasjonal sikkerhetsmyndighet (NSM) | |

## Teknologi: norske ord når leseren ikke er utvikler

Til utviklere kan de engelske fagordene stå. Til kommuner, saksbehandlere og
ledelse bruker vi disse.

| Engelsk / lånord | Norsk til ikke-utviklere |
| --- | --- |
| API | grensesnitt, programmeringsgrensesnitt (API) |
| endpoint | endepunkt |
| token | tilgangsnøkkel, token (forklart) |
| access token / refresh token | tilgangstoken / fornyelsestoken, eller forklar |
| authentication / authorization | autentisering / autorisasjon (tilgangskontroll) |
| client (OAuth) | klient |
| scope | rettighet, tilgangsomfang |
| deploy, deployment | sette i drift, produksjonssetting (til utviklere: deploy) |
| release | versjon, utgivelse |
| downtime | nedetid |
| outage / incident | driftsavbrudd / hendelse |
| bug | feil |
| feature | funksjon |
| backend / frontend | baksystem / brukergrensesnitt |
| database | database |
| cloud | sky, skytjeneste |
| on-premise | lokalt, i eget datasenter |
| log / logging | logg / logging |
| audit log | sporingslogg, revisjonslogg |
| message queue | meldingskø |
| webhook | webhook (forklar: automatisk varsel til deres system) |
| integration | integrasjon |
| migration | migrering (data), overgang (organisatorisk) |
| onboarding | innfasing, oppstart, tilkobling (av en kommune) |
| rollout | innføring |
| roadmap | veikart, plan |
| backlog | arbeidsliste, restanseliste (Jira: backlog kan stå) |
| sprint | sprint |
| stakeholder | interessent, berørt part |
| SLA | tjenestenivåavtale (SLA) |
| GDPR | personvernforordningen (GDPR) |
| encryption | kryptering |
| certificate | sertifikat |
| environment (dev/test/prod) | miljø (utvikling/test/produksjon) |
| rate limiting | begrensning av antall kall |
| timeout | tidsavbrudd |
| retry | nytt forsøk |
| payload | innhold (i meldingen), nyttelast |

## Ord som ofte forveksles

| Riktig | Feil eller forvekslet | Forklaring |
| --- | --- | --- |
| eventuelt (= kanskje) | eventuelt (= til slutt) | engelsk *eventually* |
| aktuelt (= relevant nå) | aktuelt (= faktisk) | engelsk *actually* |
| kontrollere (= sjekke) | kontrollere (= styre) | engelsk *control* |
| konsekvent (om oppførsel) | konsistent | *consistent*; `konsistent` er om stoffer |
| enda (grad: enda bedre) | ennå (tid: ikke ennå) | |
| da (fortid, én gang) | når (gjentatt, framtid) | |
| å (infinitiv) | og | `å sende og motta`, `sende og motta` |
| overfor (i forhold til) | ovenfor (over) | |
| vidt (så vidt jeg vet) | vist | |
| lenger (tid, avstand) | lengre (om noe som er langt) | `ikke lenger`, `en lengre tekst` |
| få (om antall) | lite (om mengde) | `få feil`, `lite tid` |
