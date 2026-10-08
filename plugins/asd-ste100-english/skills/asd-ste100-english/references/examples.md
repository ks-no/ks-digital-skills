# Before and after examples

Parts 1 and 2 are from `examples/before-after.md` in
[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) (MIT), with
small edits. Part 3 is new for this repository.

## Part 1: Official STE examples

These illustrate real ASD-STE100 rules, drawn from public secondary sources (see [writing-rules.md](writing-rules.md)). They are paraphrased illustrations of the rule, not quotes from the standard itself.

| Rule | Before | After | Why |
| --- | --- | --- | --- |
| One meaning per word | "Verify the system." / "Check the connections." / "Confirm receipt." | "Make sure the system is correct." (one approved term used consistently) | Three near-synonyms force the reader to guess whether they mean the same action. |
| One part of speech per word | "Oil the valve." | "Apply oil to the valve." | If "oil" is approved only as a noun, using it as a verb breaks the one-word-one-role guarantee. |
| Precise verb meaning | "Follow the safety instructions." | "Obey the safety instructions." | "Follow" can mean "come after" or "obey". STE picks the unambiguous one. |
| Simple tense only | "We have received the technical reports from HQ." | "We received the technical reports from HQ." | Present perfect adds a second parse ("received, and still relevant now?") that simple past avoids. |
| Verb, not noun | "Perform an inspection of the filter." | "Inspect the filter." | The noun form hides the action and adds a filler verb that carries no meaning. |
| No phrasal verbs | "Take off the access panel." | "Remove the access panel." | "Take off" also means "depart" and "deduct". The two words together do not predict the meaning. |

## Part 2: Applied to agent output

These are original examples built for this skill's actual use case: rewriting AI agent output so another agent, a translation layer, or a non-native reader can parse it without ambiguity. They are illustrations, not quotes from any real system.

Word counts below are whitespace-separated tokens (`text.split()`), punctuation not counted separately. A different tokenizer will produce a different number.

### Example A: Tool description

**Before:**
> This tool will attempt to synchronize state across the various backends that have been configured, and if a conflict is detected it may resolve it automatically depending on the strategy that has been set, or otherwise it will surface the conflict for manual review.

**Violations flagged:**
- Two instructions in one sentence (sync + resolve/surface).
- Present perfect in the relative clauses ("have been configured", "has been set").
- An "-ing" form that is not part of a technical name ("depending on the strategy").
- Passive voice where the actor is known ("if a conflict is detected"). The tool is the subject of the rest of the sentence, so the rewrite names it, as in Part 3.
- 44 words, far over the 25-word descriptive cap.

Note what is *not* flagged: "will attempt to" and "may resolve". Those are hedges, not violations. The tool is not promised to succeed, and the rewrite must not promise it either.

**After:**
> The tool tries to synchronize state across the configured backends. If it finds a conflict and the strategy permits the tool to resolve conflicts automatically, the tool tries to resolve the conflict. If the tool does not resolve the conflict, it reports the conflict for manual review.

`Check: "depending on the strategy" can also mean that the strategy decides how the tool resolves a conflict, not only if it does.`

"May resolve" became "tries to resolve", because "may" right after "permits" reads as permission, not as a hedge. "Tries" keeps the hedge: the tool is not promised to succeed. The last sentence branches on whether the conflict was resolved, not on what the strategy permits. That is what "or otherwise" meant in the original: the fallback covers a permitted resolution that still did not happen.

### Example B: Error message

**Before:**
> An error may have occurred while processing your request due to a possible mismatch in the expected data format, which could be caused by an outdated client version.

**Violations flagged:**
- One sentence carrying three separate claims (a possible error, a format mismatch, a client version).
- An "-ing" form that is not part of a technical name ("while processing your request").
- Passive voice where the actor is known ("could be caused by an outdated client version").
- 28 words, over the descriptive cap.

Not flagged: the hedges "may have" and "could". The message is written by a system that does not know what went wrong. Both hedges are accurate reporting of that ignorance.

**After:**
> An error may have occurred when your request was processed. The cause may be a data format that does not match the expected format. An outdated client can cause this mismatch.

`Kept as-is: the compound form "may have occurred". The simple past would lose the doubt: the system does not know if an error occurred.`

`Check: the message does not tell the reader what to do next.`

**This example is the reason the modality rule exists.** An earlier version of this file rewrote the first sentence as "The request failed", and the third as "an outdated client **is the most common cause**". Both read better. Both are wrong: the first asserts a failure the system only suspects, and the second invents a frequency claim that appears nowhere in the input. A rewrite that supplies a cause, a frequency, or a mechanism has stopped being a rewrite. The same applies to an instruction: "Check your client version" would read well at the end, but the source does not tell the reader to do anything.

The rewrite says that an error may have occurred, not that the request failed: the source does not say that processing stopped. The rewrite uses the passive "was processed" because the source does not say who processes the request.

Note also that "may have occurred" keeps a compound verb form that the simple-tense rule would otherwise remove. **When the tense rule and the modality rule conflict, modality wins.** Dropping the auxiliary here would delete the uncertainty along with the tense.

### Example C: Inter-agent instruction

**Before:**
> Once the upstream job has completed and assuming no errors were raised, the downstream agent should proceed to consume the output artifact, though it is worth noting that partial artifacts are sometimes produced under timeout conditions.

**Violations flagged:**
- Present perfect ("has completed") and subordinate-clause stacking ("assuming...", "though it is worth noting...").
- "-ing" forms that are not part of a technical name ("assuming", "worth noting").
- One sentence, three separate facts (completion condition, next action, edge-case warning).
- 36 words, over the 20-word instruction cap.

**After:**
> When the upstream job finishes with no errors, read the output artifact. Warning: after a timeout, the artifact can be partial.

`Check: the source does not say what to do if the job has errors or the artifact is partial.`

Two deliberate calls worth stating rather than hiding:
- "should proceed to consume" became the imperative "read". In an instruction to the agent that executes it, this "should" is a requirement, not advice. A recommendation that lets the reader choose stays a recommendation. Do not make the same move in descriptive text.
- The rewrite does not tell the agent what to do with a partial artifact. "Check that the artifact is complete before you use it" would make the warning actionable, but it is an instruction the source does not give. The `Check:` line reports the gap to the author instead.

### Example D: README prose (STE-flavored mode)

**Before:**
> Our caching layer is designed to slot seamlessly into your existing stack with minimal friction and no vendor lock-in; it leverages semantic similarity to dramatically reduce the cache misses that traditionally plague LLM workloads.

**Violations flagged:**
- Marketing adjectives and claims without measurement ("seamlessly", "minimal friction", "dramatically").
- An "-ing" form that is not part of a technical name ("existing stack"). "Caching layer" is a technical name, so it stays.
- Semicolon joining two separate ideas.
- Passive voice where the actor is known ("is designed to"), and soft phrasing ("slot into", "leverages").
- 34 words, over the 25-word descriptive cap.

**After:**
> We designed our caching layer to fit into your current stack, with no vendor lock-in. The caching layer uses semantic similarity to reduce cache misses in LLM workloads.

Flavored mode kept the explanatory rhythm and did not force one fixed verb per action. It still cut the marketing adjectives, the semicolon, and the length. It kept only the claims in the source: "minimal friction" and "dramatically" had no measurement, so they went, and the rewrite does not add a mechanism that the source does not state. If the reader needs to know how semantic similarity reduces misses, ask the author in a `Check:` line. Do not invent it.

## Part 3: Applied to a Fiks tool description

This example shows the Norwegian context rules: identifiers and Norwegian technical
names stay, and the technical names get a gloss the first time.

**Before:**
> This tool can be leveraged to retrieve the relevant organisation details from Enhetsregisteret, and it should be noted that the orgnr parameter has to be provided as a 9-digit string; in cases where the organisation cannot be found, an empty result will be returned.

**Violations flagged:**
- Filler and marketing verbs ("can be leveraged to", "it should be noted that").
- A semicolon that joins two ideas.
- Passive voice where the actor is known ("has to be provided", "cannot be found", "will be returned").
- 44 words, far over the 25-word descriptive cap.

**After:**
> Get the data for one organisation in Enhetsregisteret (the Norwegian register of legal entities). Give `orgnr` as a string of 9 digits. If the tool does not find the organisation, it returns an empty result.

What stays and why:
- `orgnr` is the parameter name. It is an identifier, so it does not change, also if
  a Norwegian reader would write `organisasjonsnummer` in prose. The rewrite does not
  add a second name for it, and it does not define it: the source does not say more
  than "a 9-digit string".
- `Enhetsregisteret` is a technical name. The reader will meet it in Norwegian
  documentation, so it stays Norwegian. It gets a short gloss the first time. A gloss
  of a public term is not an added fact about the system.
- "cannot be found" became "does not find", not "does not exist". The tool knows
  only that it did not find the organisation. A rewrite that says the organisation
  does not exist adds a claim.

## How to read these examples

Part 1 shows the actual rules this skill is built on. Part 2 shows the transfer: the same discipline (one meaning per word, active voice, simple tense, one instruction per sentence, explicit conditions instead of buried subordinate clauses) makes machine-to-machine and cross-language text safer to parse, not just aircraft manuals. Part 3 shows what stays unchanged in text from a Norwegian team.
