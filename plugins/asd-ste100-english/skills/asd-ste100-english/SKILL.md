---
name: asd-ste100-english
description: >-
  Write and rewrite English in the style of ASD-STE100 (Simplified Technical
  English), so that an AI agent, a downstream system or a non-native reader
  cannot misread it. Use when English text must be parsed without a human to
  resolve ambiguity and a misreading has a real cost: tool and function
  descriptions, error messages, prompts and system messages, inter-agent
  instructions, procedures, runbooks and status reports. Also use when text
  reads as dense, hedged or easy to misparse, and when the user says "STE",
  "STE100", "Simplified Technical English", "controlled language", "80% STE",
  "rewrite so an agent cannot misread this" or "make this plain". Not for
  creative or marketing copy. For Norwegian text, use asd-ste100-norsk.
---

# ASD-STE100 for English

ASD-STE100 is a controlled-language standard from the aerospace and defense
industry (ASD, the AeroSpace and Defense Industries Association of Europe). Its
purpose is to stop maintenance technicians from misreading English instructions.
It removes the two largest sources of misreading: words with more than one
meaning, and sentences with more than one possible structure.

This skill applies the same discipline to a different reader: an **AI agent or a
downstream system** that must parse an English string without a human who can
resolve ambiguity. Examples are an error message, a tool description, an
inter-agent instruction and a status report. If a technician can misread "close
the valve" as "the valve that is near", a language model can too.

## Why this skill exists

Language models know ASD-STE100. When you ask for it by name, you get shorter
sentences, fewer synonyms and fewer hedges, and the text is easier to read. The
full standard is strict, so a softer request ("80% of the way to ASD-STE100") often
gives better prose. This skill makes the request precise. It tells you which rules
to apply always, which rules are only a direction, and what you must never change.

## When to use

- Agent output (an explanation, an instruction, a log message, a tool
  description) is dense, full of jargon or ambiguous.
- Another agent, a translation pipeline or a non-native English reader will read
  the text, and a misreading has a real cost.
- You write a prompt, a system message or a tool description and want to remove
  ambiguity before a model reads it.
- The user wants a **before/after** comparison that shows which rule each change
  fixes. The user must ask for this. The default output is the rewritten text
  only (see Output format).

Do not use this skill for creative or marketing copy. STE is flat and literal on
purpose. Do not apply it where voice, nuance or persuasion is the point.

## Two modes

Select a mode before you rewrite. If the user does not select one, infer it from
the text type. Do not announce the mode unless the user asks for the rule table
(see Output format).

**Strict.** Procedures, error messages, tool and function descriptions,
inter-agent instructions and safety text: all text where a wrong reading has a
cost. Apply the structural rules and the scan checklist fully, including the hard
length limits. Apply the lexical rules as far as you can.

**STE-flavored.** READMEs, PR descriptions, changelogs and explanatory prose.
Apply the structural rules and the scan checklist fully. The lexical rules are
advice, so verbs can vary. Prose needs some range, and a strict rewrite of prose
changes its personality more than it makes it clear. A request for "80% STE" or
"80% of the way" means this mode.

## Source and scope

This skill encodes the **rule categories** of ASD-STE100 Issue 9 (January 2025):
53 writing rules in 9 sections about word choice, grammar, sentence structure and
style. The standard also has a dictionary of approximately 900 approved words (one
meaning and one part of speech each) and approximately 1,200 words to avoid, with
replacements. See [writing-rules.md](references/writing-rules.md) for the rule
summary and the sources.

This skill does **not** contain the ASD dictionary, because ASD does not permit
others to redistribute it. Instead, apply the *principle* behind the dictionary:
select the plainest, most common word and use it in the same way every time. When
exact ASD-approved wording is necessary (for example, in real aircraft maintenance
documentation), get the standard and check each word against the real dictionary.
[writing-rules.md](references/writing-rules.md) tells how to get it.

## Core rewrite rules

STE has two kinds of rules, and this skill can fully apply only one kind.
**Structural rules** describe the shape of a sentence. You can apply them from the
description alone. **Lexical rules** depend on the official dictionary, which this
skill does not contain. Without the dictionary, a lexical rule becomes a
preference for plain words, not a standard that you can check.

Apply the structural rules with confidence. Apply the lexical rules as a
direction. Do not claim dictionary compliance that you cannot verify.

### Structural rules: apply these

| Rule | Do | Do not |
| --- | --- | --- |
| Active voice | "The agent deletes the file." | "The file is deleted (by the agent)." Passive is correct only when the actor is unknown or not relevant. |
| No phrasal verbs (Rule 9.3) | "Remove the panel." / "Start the job." | "Take off the panel." / "Spin up the job." The two words together have meanings that the parts do not predict. |
| One instruction per sentence | "Open the file. Read line 3." | "Open the file and read line 3, then check if it matches." |
| Sentence length | 20 words or fewer for instructions and procedures. 25 words or fewer for descriptions. | Long sentences with many clauses. |
| No semicolons (Rule 8.1) | Write separate sentences. | Any semicolon. STE prohibits the mark, not only its use between clauses. Rule 8.1 permits all other standard punctuation, also the em dash. The house style does not permit the em dash (see Norwegian context). |
| Noun clusters | 3 nouns or fewer in a noun phrase ("fuel pump valve") | 4 or more stacked nouns ("high pressure fuel pump inlet valve assembly") |
| No ellipsis | Keep the subject, the verb and the article, even if the sentence gets longer. | Remove words to save space ("Files not backed up will be lost": which files?). |
| Keep modality | "The request **may have** failed." stays "may have". When "may" can also read as permission (right after "permits" or "allows"), write the hedge another way at the same strength: "might", or "tries to" for an attempt. A "should" becomes an imperative only when the source means it as a requirement. A recommendation that lets the reader choose stays a recommendation. | Make a hedge into a fact ("The request failed."), or add a certainty that the source does not state. |
| One name for one thing | Select one name for each thing and use it in all of the text. | "the user", "the customer" and "the client" for the same person. |
| Verb, not noun (Rule 3.7) | "Analyze the log." | "Perform an analysis of the log." The noun form makes the sentence longer and hides who does the action. |
| Paragraph limits | One topic per paragraph, 6 sentences or fewer. | Paragraphs with more than one topic. |
| Lists for sequences | A numbered or bulleted list for 3 or more steps or conditions. In a string that a UI or an API shows on one line (an error message, a field description), use short sentences in sequence. | A sequence inside one sentence of prose. |

### Lexical rules: a direction only

| Rule | Do | Do not | Why this is weaker here |
| --- | --- | --- | --- |
| One verb for one action | Select one verb for one action and use it every time. For example, always "check", and never "check", "verify" and "confirm" for the same action. | Use different verbs for the same action in one document. | You can check consistency in a document. You cannot check which verb is the *approved* verb without the dictionary. |
| One part of speech per word | "Apply oil to the valve" (oil is a noun). | "Oil the valve" (oil is a verb). | Only the dictionary tells if "oil" is approved as a noun only. Prefer the noun when both forms are equally clear. Do not claim compliance. |
| Technical names | Keep necessary technical nouns and verbs. Define each one the first time if the reader might not know it. STE permits a project glossary in addition to the base dictionary. | Use jargon that the reader does not know, and never define it. | The glossary allowance is real STE, but the base dictionary is not here. |

### Simple tenses: apply with one exception

STE permits the infinitive, the imperative, the simple present, the simple past,
the simple future, and the past participle as an adjective. It does not permit the
present perfect or other compound forms: "we received the report", not "we have
received the report". An "-ing" form is permitted only as part of a technical name
("caching layer"), not as a verb or a plain modifier ("while processing", "existing
stack"). Common nouns that end in "-ing", such as "warning" or "setting", are nouns,
not verb forms, so the rule does not apply to them.

Aircraft manuals do not need the present perfect, so the rule costs them nothing.
Other text can need it. "The job has completed" (and its output is available now)
and "the job completed" (at a time in the past) are two different statements.
Status text often needs the first one. **When the compound form carries
information that the simple form cannot carry (current relevance, or a hedge as in
"may have failed"), keep it and report it in a `Kept as-is:` line.** In all other
cases, obey the rule.

## Scan checklist

These six habits cause most of the problems in machine-written English. Each one
is mechanical: you can point to the word or the punctuation mark that breaks the
rule. Scan for all six before you rewrite.

1. **Synonym rotation.** One thing has several names in one document ("the user",
   "the customer", "the client"). The reader cannot know if this is one thing or
   three. Fix: select one name and use it every time.
2. **Hedge stacking.** Helper verbs and qualifiers accumulate until the sentence
   says nothing ("it is important to note that this may potentially help to
   improve"). Fix: keep one hedge at the original strength and delete the others
   ("this may help to improve"). Do not make the claim into a fact.
3. **Nominalization.** An action becomes a noun ("perform an analysis of",
   "provides assistance to"). Fix: use the verb ("analyze", "helps").
4. **Marketing adjectives.** Words that claim quality and do not show it:
   seamless, robust, powerful, cutting-edge, effortless, blazing-fast. Fix: delete
   the word, or replace it with the measurement that supports the claim. Some of
   these words also limit scope ("all your favourite tools"). If the deletion makes
   the claim broader, keep the limit in plain words.
5. **Run-on sentences.** Several ideas in one sentence, joined by semicolons, em
   dashes or spaced hyphens. Fix: one idea per sentence.
6. **Soft phrasal verbs.** Spin up, reach out, dive into, kick off. Fix: use one
   plain verb (start, contact, read, begin).

## Norwegian context

This skill is for teams in Norway, and English text from these teams often
contains Norwegian names and terms. Apply these rules in addition to the rules
above.

- **Identifiers do not change.** Names in code, JSON keys, API fields, URL paths,
  query parameters, enum and status values, environment variables and log keys are
  references, not prose. Keep them exactly as they are, also when they contain
  Norwegian words or a spelling error. `orgnr` stays `orgnr`. If you are not sure
  if a string is an identifier, it is an identifier.
- **Norwegian domain terms are technical names.** STE permits a project glossary
  for technical names. A Norwegian term that names a legal or administrative
  concept, or a field that the reader will see in the data, stays Norwegian. An
  English translation would give it a different meaning. Use the same form every
  time. Define it the first time if the reader might not know it. If the source says
  "by organisasjonsnummer", keep the term: "Get one organisation by
  organisasjonsnummer (the 9-digit Norwegian organisation number)." Do not add the
  term next to an identifier that already names the same thing. A Norwegian reader of an error message knows the term, so do not
  define it there. A gloss of a public term is not an added fact. A statement about
  what an identifier contains is an added fact. Do not add one that the source does
  not give.
- **No em dash (U+2014).** STE permits it, but the KS Digital house style does not,
  because it reads as machine-written. Use a comma, a colon, a full stop or
  parentheses.
- **Product and service names** have the form that the owner uses: Fiks-porten,
  Fiks-plattformen, ID-porten, Maskinporten, Altinn, KS Digital.
- **Tool and schema descriptions that a language model reads are in English**,
  also in a Norwegian team, because they are part of the model's prompt. The
  Norwegian domain terms stay in them.
- **Norwegian text is not for this skill.** English STE rules do not transfer
  directly to Norwegian grammar. Use `asd-ste100-norsk` for the structure of
  Norwegian text and `norsk-sprakvask` for spelling, punctuation and term choice.

## Process

1. Select the mode (Strict or STE-flavored).
2. Read the input text once for meaning. Do not start to rewrite before you know
   what the text must still say after the rewrite.
3. Find the identifiers. You will not change them.
4. Read the text sentence by sentence. Mark each violation of the structural
   rules and each habit from the scan checklist. In Strict mode, also mark the
   violations of the lexical rules.
5. Rewrite each marked sentence. Fix the violation and keep the meaning exactly.
   If a rewrite removes necessary precision (a safety condition, a scope
   qualifier, a number), keep the longer text and report it in a `Kept as-is:`
   line.
   - **Check modality before you rewrite.** Hedges ("may", "could", "sometimes",
     "is likely to") carry the confidence of the author, and confidence is
     content. A shorter sentence that makes a hedge into a fact is not a
     simplification. It is a different claim. This is the most frequent error in
     STE rewrites, because a length limit makes it tempting to remove hedges.
   - Do not add a fact or an instruction that the source does not state. A
     rewrite that reads better because it adds a cause, a frequency, a mechanism or
     a next step is not a rewrite. If the source lacks something, report it in a
     `Check:` line.
6. Give the rewritten text (see Output format). Keep the mode and the rule
   analysis to yourself, unless the user asks for them.
7. If the input already obeys the rules, say so. Do not change text that obeys
   the rules.

## Output format

**Default: the rewritten text only.** Most users want a result that they can
paste into a tool description, an error string or a prompt. Give the simplified
text alone. Do not add an introduction about this skill, the mode, a count of
violations, a summary of changes, a rule table or an offer to explain.

Two additions are permitted, each on one line after the text:

- `Kept as-is:` something that you kept on purpose and that a reader can think is
  a violation: a longer phrase from step 5, a compound tense, a passive for an
  unknown actor. Name the information that a simpler form would lose or add.
- `Check:` content that the source makes unclear, leaves out or that you had to
  interpret: a name that may be wrong, a reference with two possible meanings, a
  next step that the reader needs. Do not correct or complete the content
  yourself.

If there is nothing to report, do not add the lines.

**On request: the rule table.** When the user asks to see the reasoning ("show
the diff", "which rules did it break", "explain the changes", "before/after"),
give the rewritten text first and then this table:

```markdown
| Rule violated | Original | Simplified |
| --- | --- | --- |
| Present perfect tense | "We have received your request." | "We received your request." |
| Noun cluster (4 or more nouns) | "the agent task queue priority handler" | "the handler for task-queue priority" |

Mode: Strict. 7 violations found.
```

After the table, add one line about text that you did **not** simplify, and why.
The usual reason is that a simpler text would lose necessary precision. In this
mode, you can also suggest a one-line glossary entry for each technical name that
must stay.

## Boundaries

**This skill will:**

- Rewrite ambiguous or dense English into short, active sentences where each word
  has one meaning.
- Give only the rewritten text by default, and name the rules when the user asks.
- Keep each fact, condition and scope qualifier from the original.
- Keep the strength of each hedge, and add no claim or instruction that the source
  does not make.
- Keep identifiers and Norwegian technical names unchanged.
- Suggest a one-line glossary entry for each technical name that must stay, when
  the user asks for the rule table.

**This skill will not:**

- Give the official ASD dictionary as if it knows it word for word. The official
  download is the only source for the exact approved words.
- Simplify creative, marketing or persuasive copy, where voice and nuance are the
  point.
- Remove a safety condition, an exception or a scope qualifier to make a sentence
  shorter. It will report the trade-off.
- Change "may have failed" into "failed", or "could be caused by X" into "X is the
  cause". A hedge that disappears changes the claim.
- Guarantee a document that complies with STE at aerospace or defense level. This
  is a general clarity tool that uses STE as a model. It is not a certified STE
  authoring tool.
- Make weak content true or useful. STE fixes the *form* of a text, not its
  content. A hollow paragraph that you rewrite with these rules becomes a short,
  clean, hollow paragraph. If the text has nothing to say, say so. Do not polish
  it.
- Shorten past the point of clarity. The goal is to remove ambiguity, not to
  remove words. Stop when the sentence is not ambiguous, not when it is shortest.

## References

Load a file only when its trigger applies.

| File | Load it when |
| --- | --- |
| [writing-rules.md](references/writing-rules.md) | The user asks about the standard, a rule number or the sources, or you are not sure which STE rule applies. |
| [examples.md](references/examples.md) | You are not sure how far to go, or the user asks for the rule table. It has STE examples, agent output and a Fiks tool description. |

## Source and attribution

This skill is adapted from
[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill),
Copyright (c) 2026 Dustin Yuchen Teng, under the MIT License. The license text is
in `LICENSE-asd-ste100-skill.txt` in this directory. The main changes are the
Norwegian context section, the identifier rule and the "80%" request. The upstream
linter is not included.

This skill is not published or approved by ASD, and it does not contain the
ASD-STE100 dictionary.
