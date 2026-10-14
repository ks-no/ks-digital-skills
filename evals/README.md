# Testtekster for KI-markørene

Tekstene i `cases.json` tester reglene for KI-markører i `asd-ste100-english` og
`norsk-sprakvask`:

- kontraster av typen «not just X, it is Y»
- bilder og sammenligninger som skal forklare noe
- skryt og dramatikk
- det som skal stå, for eksempel sammenligninger av samme slag, roller i en prompt,
  vanlige rettelser og fagord som er bilder (`watchdog`)

Ingen av setningene står i skillene. Testen måler derfor om agenten bruker regelen,
ikke om den kjenner igjen et eksempel. `scripts/validate.py` feiler hvis en skill
får en setning fra en testtekst.

## Innhold

- `cases.json`: tekstene, med `en` for engelsk og `no` for norsk. Hver tekst har en
  `id`, en `type`, selve teksten (`text`) og kravet til et riktig svar (`pass`).
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
