# ASD-STE100 writing rules: summary and sources

This file summarizes the public, official description of ASD-STE100 (Simplified
Technical English). It paraphrases the rule *categories*. It does not reproduce the
text of the standard or its dictionary of approximately 900 words. For the official
document, request the free download on the official site.

Adapted from `references/writing-rules.md` in
[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) (MIT).

## What ASD-STE100 is

ASD-STE100 is a controlled natural language. AECMA released the first version in
1986 as document PSC-85-16598. AECMA is now ASD (the AeroSpace and Defense
Industries Association of Europe). European airlines asked for it, because most of
their staff were not native English speakers and needed maintenance documentation
that they could not misread. On an aircraft, a misread instruction can kill people.
The Simplified Technical English Maintenance Group (STEMG) maintains the standard.
It has been free to download since Issue 6 (2013). The current edition is Issue 9
(January 2025).

## How to get the standard

ASD-STE100 is free to get, but it is not free to redistribute. The copyright notice in
Issue 9 does not permit reproduction or publication of the standard, in whole or in
part, without written permission from ASD. The free reproduction rights apply only to
a short list of categories: ASD/AIA/AIAC member associations and their member companies
and customers, defence ministries, A4A, airworthiness authorities, and universities and
research institutes for education. Thus the dictionary is not in this repository.

To get the standard, use the request form on the
[official downloads page](https://www.asd-ste100.org/STE_downloads.html). The form sends
a link by e-mail. It is not a direct download.

## Structure

- **53 writing rules in 9 sections** about word choice, grammar, sentence structure
  and style.
- **A dictionary** of approximately 900 approved words, each with one meaning and
  one part of speech, and approximately 1,200 words to avoid, with replacements.
- **A terminology allowance.** An organization can define its own dictionary of
  approved technical nouns and verbs in addition to the base dictionary, for domain
  words that the base dictionary does not cover. In this repository, Norwegian
  public-sector terms such as `organisasjonsnummer` are in this category.

## Rule categories (paraphrased)

**Word choice**

- Use approved words only, with their approved meaning and part of speech.
- Each word has one meaning. Do not use context to select one of several meanings.
- Prefer the plain, short, common word to a formal or rare synonym.
- Use an approved verb for an action, not a noun that comes from that verb
  (Rule 3.7).
- Do not make phrasal verbs from a verb and a preposition (Rule 9.3). The parts do
  not predict their meaning, and non-native readers and translation systems both
  misread them.

**Verb forms**

- Permitted forms: the infinitive, the imperative, the simple present, the simple
  past, the simple future, and the past participle as an adjective only.
- No present perfect, past perfect or other compound forms with helper verbs. "We
  have received" is not permitted. "We received" is permitted.
- An "-ing" form is permitted only as part of a technical name ("landing gear"), not
  as a verb form or a plain modifier. Common nouns that end in "-ing", such as
  "warning", are nouns, so the rule does not apply to them.

**Voice**

- Use active voice for procedures and instructions.
- Passive voice is permitted only in descriptive text, and only when the actor is
  unknown or not relevant to the reader.

**Sentence structure**

- One instruction per sentence.
- Approximately 20 words or fewer per sentence in procedures and instructions.
  Approximately 25 words or fewer in descriptive text.
- Do not remove parts of a sentence (the verb, the subject, the article) to make
  it shorter. The standard warns that this causes ambiguity, not clarity.
- A noun cluster (nouns stacked as a modifier) has 3 words or fewer.
- Semicolons are not permitted (Rule 8.1). All other standard English punctuation
  marks are permitted, also the em dash. Write separate sentences.

**Paragraph and document structure**

- One topic per paragraph.
- Approximately 6 sentences or fewer per paragraph.
- Use vertical lists (numbered or bulleted) for sequences, conditions and complex
  lists. Do not put them in a sentence of prose.

**Safety instructions**

- A safety instruction starts with a clear command or condition. Do not put it in
  the middle of a sentence.

## Why STE is useful for agent output

STE was made for a reader who cannot ask a question: a technician at an aircraft,
who works from a manual and cannot call the author. An AI agent that reads the
output of another agent, a tool description or a system message is in the same
position. It cannot ask if a passive sentence means that the caller does X or that
the callee does X. The rules that prevent a mechanic from misreading a torque value
also prevent an agent from misreading an instruction.

## Sources

- [ASD-STE100 official site](https://www.asd-ste100.org/)
- [ASD-STE100: About STE](https://www.asd-ste100.org/about_STE.html)
- [ASD Europe: Simplified Technical English](https://www.asd-europe.org/standards-specifications/simplified-technical-english/)
- [Simplified Technical English on Wikipedia](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- [TechScribe: ASD-STE100 Simplified Technical English](https://www.techscribe.co.uk/techw/asd-simplified-technical-english.htm)
- [SKYbrary: Simplified Technical English (STE)](https://skybrary.aero/articles/simplified-technical-english-ste)
