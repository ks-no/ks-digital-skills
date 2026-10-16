# Sikkerhet

Har du funnet en sårbarhet i KS Digital Skills? Takk for at du sier fra.

## Slik melder du

Bruk «Report a vulnerability» under fanen **Security** i dette repoet. Meldingen er
privat til vi har rettet feilen. Ikke meld en sårbarhet i en vanlig issue, fordi alle
kan lese den.

Vi svarer så raskt vi kan.

## Hva du melder her

En skill er instruksjoner som en agent følger. Meld det her når:

- en skill får agenten til å vise, logge eller sende videre en secret, et token eller
  personopplysninger
- en skill får agenten til å kjøre en kommando som brukeren ikke har bedt om, eller til
  å endre innstillingene for sandboxen eller tilgangene
- noen kan endre `main` eller lese secrets i dette repoet uten å være vedlikeholder

Et råd i en skill som er feil, også et sikkerhetsråd, melder du i en vanlig issue.

## Ikke legg ved

Ta aldri med ekte tokens, passord, nøkler eller personopplysninger. Beskriv hva som
skjer, og hvordan du fikk det til. Skriv hvilken skill og hvilken versjon det gjelder,
og hvilket verktøy og hvilken modell du brukte.
