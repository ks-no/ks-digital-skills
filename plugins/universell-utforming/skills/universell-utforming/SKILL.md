---
name: universell-utforming
description: >-
  Use when you write, change or review a user interface: HTML, CSS, JSX or TSX,
  templates, components, forms, dialogs, menus, error and status messages, or the
  texts on a screen. It checks the interface against the requirements for universell
  utforming (accessibility) and the WCAG success criteria that the Norwegian regulation
  requires. Also use when the user mentions universell utforming, uu, tilgjengelighet,
  accessibility, a11y, WCAG, screen readers or other assistive technology, and when a
  team plans, prepares, runs, reviews or follows up a user test (brukertest, usability
  test) with people with disabilities, or has notes from such sessions to make into
  findings, backlog tasks or code fixes. Not for code that has no user interface, and
  not for a user test where no participant has a disability.
---

# Universell utforming

In Norway, ICT solutions for the public must meet requirements for universell
utforming: the WCAG success criteria that the regulation lists. A check of the code
finds many barriers. It does not show if a person who uses assistive technology every
day can use the solution and get the task done. A user test with people with
disabilities shows that. This skill makes you check each change to an interface, and
helps a team to test with people with disabilities and to make the results into fixes.
Most rules for the test sessions restate a checklist by Frank Dahle (Digdir) in UX
Norge (see Sources).

## What you do and do not do

- You read the code and the project docs, run the tests of the project, and write
  code, tests, plans, scripts, texts for participants, findings and fixes.
- The team recruits the participants and runs the sessions. You do not see a session.
  Do not write that a solution "is accessible", "passes", "meets the requirements" or
  "is universelt utformet" because of your own check. Say what you checked, and what
  only people can show.
- Do not add test packages, tools or dependencies to a project unless the user asks.
  You can suggest automatic accessibility checks for the project in one line.
- Do not suggest a change to the sandbox, the permissions or the tool configuration.
  If a restriction stops a command, report the command and the restriction, and stop.
- Answer in the language of the user. Write text for participants in their language,
  with short sentences and plain words.
- Never put the name of a participant or information about their health in a backlog,
  an issue, a commit or a pull request. Use a code, such as "P1". A task can name the
  assistive technology to check with, but not together with a participant code.
- Do not give the rule IDs or the file names of this skill in the answer, because the
  user cannot see the skill.
- No human accessibility expert has reviewed this skill. When the user asks if a
  solution meets the requirements, say this in one line, and point to Uutilsynet and a
  person with accessibility expertise.

## Select the task

| The user | Task |
| --- | --- |
| asks you to write or change interface code | Code check of your own change, before you answer |
| asks for an accessibility check or a review of interface code | Code check |
| asks if a solution is ready for a user test | Code check, as a ready check |
| asks for a plan, a session script, an invitation or a consent text for a user test | Plan |
| gives a test plan or a script and asks you to check it | Review of a plan |
| gives notes, a summary of recordings or a report from sessions | Findings |

A request can have more than one task. Do them in the order of the table.

## Code check

1. Find the code to check. When you write or change code, check the code that you
   write or change. When the user asks for a check, check the code that the user gives,
   or the screens and the flows that the user names or that the tasks of a test use.
2. Check each control, field, image and message in that code:
   - **Names, roles and states.** Assistive technology can read the name, the role
     and the state of each control, and the name contains the visible text. An image
     that gives information has a text alternative, and a decorative image is hidden
     from assistive technology (1.1.1, 2.5.3, 4.1.2).
   - **Native elements.** Use a native HTML element, and do not add ARIA that the
     element already has. When a custom widget is necessary, use a component from the
     design system of the project, or follow the pattern in the ARIA Authoring
     Practices Guide, with its keyboard behaviour.
   - **Forms.** Each field has a visible label that stays when the user types (3.3.2).
     A field for personal data about the person who fills in the form, not about
     another person, tells its purpose with `autocomplete` (1.3.5). An error tells in
     text what is wrong and how to correct it, and `aria-describedby` links it to its
     field (3.3.1, 3.3.3). After a submit with errors, the focus goes to a summary of
     the errors or to the first field with an error. Do not disable the submit button
     to show that the form is not complete. When the user deletes data, or makes a
     legal or financial commitment, the user can check, correct or undo it, or must
     confirm it (3.3.4).
   - **Keyboard and focus.** The keyboard can reach and use each function, in a
     logical order, with a visible focus, and the focus does not get stuck (2.1.1,
     2.1.2, 2.4.3, 2.4.7). When a dialog opens, the focus goes into it, and when it
     closes, the focus goes back to the control that opened it. In a modal dialog, Tab
     stays in the dialog. Follow the APG pattern for the other keys, such as Esc to
     close. When the focused element is removed, the focus goes to a sensible place.
     After a change of page in the client, the title changes, and the focus goes to the
     new content or the change is announced. Move the focus only to an element that is
     on the page and can take the focus at that time, for example after the render, and
     not behind an open dialog.
   - **Status messages.** A status message goes into a live region that is on the
     page before the message comes. Use `role="status"` for most messages, and
     `role="alert"` only for urgent ones (4.1.3).
   - **Structure and language.** The page has a title (2.4.2) and the correct `lang`,
     also on parts in another language (3.1.1, 3.1.2). Headings, lists and tables that
     the screen shows are also in the markup (1.3.1), and the user can skip blocks
     that repeat (2.4.1). No criterion requires landmarks, so a missing landmark alone
     is not a finding.
   - **Layout and colour.** The content works at 320 CSS pixels width without scroll
     in two directions, except for content such as a data table or a map (1.4.10).
     The page does not block zoom or lock the orientation (1.4.4, 1.3.4). More spacing
     in the text does not hide content, so look for a fixed height on a text container
     (1.4.12). Text has a contrast of at least 4.5:1, also the text in a control, and
     large text at least 3:1 (1.4.3). The parts that show a control and its state, a
     focus indicator that the author styles, and graphics that give information have at
     least 3:1 to the colours next to them (1.4.11). Disabled controls are exempt.
     Colour is not the only way to give information (1.4.1).
   - **Time, motion and media.** The user can extend or turn off a time limit (2.2.1),
     and can pause content that moves by itself for more than 5 seconds (2.2.2).
     Recorded video with sound has captions (1.2.2).

   WCAG 2.2 is not part of the Norwegian rules yet. You can suggest its new criteria,
   such as target size, as advice, but do not report them as a breach.

   For a check of a full page or flow, or when the user asks for a full WCAG check,
   also read [wcag-check.md](references/wcag-check.md).
3. Report only barriers that the code shows. A correct pattern is not a finding. If
   the code that you have cannot show a result, such as a colour in a stylesheet that
   you do not have, say so in a `Check:` line. Give one line for each file or part that
   you do not have, with the criteria that it would show. Do not add a `Check:` line
   for a part that the code under check does not contain, such as the page title of a
   component.
4. Fix the barriers with a minimal change. Use a native HTML element before you add
   ARIA. Keep the behaviour, the texts and the structure that the fix does not need to
   change.
5. When you can run commands in the project, run its tests and its automatic
   accessibility checks, but not a command that starts the app or a browser. If the
   project has component tests, write tests for the accessible behaviour of the
   change, such as the name of a control or where the focus goes. When you cannot see
   the tests of the project, do not write a test file.
6. For a ready check, also check that the participants can open the test version from
   their own devices (R5).

When you write or change code, the answer has these parts:

1. The change, complete, in the style of the code around it.
2. The tests, only when you wrote them in step 5. If a test of the project fails, say
   which one.
3. Up to three short notes, only about a barrier that the change cannot fix or a choice
   that the user must make.
4. The `Check:` lines from step 3, if any.
5. For a new screen or flow, one line about what only people can check: a test with a
   screen reader, or a user test with people with disabilities.

When you check code that the user gives, the answer has these parts:

1. The result in one sentence. For a ready check: ready or not ready.
2. The barriers, the barriers that stop a task first. For each barrier, give the WCAG
   success criterion and the fix.
3. The `Check:` lines from step 3, if any.
4. Only when you can run commands in the project: which tests you ran and their result,
   or one line that the project has no tests. In one line, name the automatic
   accessibility checks that you did not run because they start the app or a browser.
5. One line about what only people can show. Do not add test steps or a click-through
   here.

Each answer has only these parts. When another skill is in use, also give the parts
that it asks for. Do not add a text about universell utforming, a test plan or a list
of checks that the user did not ask for.

## Rules for the sessions

The Plan, the Review of a plan and the Findings use these rules. Apply R11 and R12 only
when a participant uses a screen reader, and R13 when a participant uses a screen
reader or controls the device with the voice. For other assistive technology and other
needs, apply R4, R6, R8 and R9 to that tool or need, and these rules when they apply:

- A participant who uses magnification shares the magnified view, so that you see
  what they see.
- A participant with a cognitive impairment or dyslexia gets each task in plain words,
  also in writing, and shorter blocks of work with breaks.
- A Deaf or hard-of-hearing participant gets the interpreter that they prefer, such as
  a sign language interpreter or a skrivetolk. Book the interpreter early.

### Participants

- **R1. Recruit through the organisations.** Ask the user organisations for the
  disability groups (interesseorganisasjoner) to help you find participants. A
  municipality can also ask its råd for personer med funksjonsnedsettelse. Start about
  one month before the sessions.
- **R2. Mix the experience.** Do not select only participants who test often. Much
  test experience becomes a source of error, and you lose the view of a user who does
  not know the service. Include people who have used assistive technology all their
  lives and people who had to learn it as adults. Include the disability groups that
  the service must work for, such as blind people, people with low vision, reduced
  motor function, dyslexia, hearing loss or cognitive impairments. Do not draw a
  conclusion about a group from one person.
- **R3. Learn about the whole person.** Ask about experience, language, education,
  knowledge, goals, needs, difficulties and expectations, not only about the
  disability. Collect only what the test needs, usually the assistive technology and
  the experience with it, not the diagnosis. Also this information tells that the
  person has a disability, so it is health data, a special category of personal data
  (GDPR Article 9). It needs a legal basis under Article 9, usually explicit consent.

### Before the session

- **R4. Ask each participant what to arrange.** Before the session, ask about travel,
  how to get to the place, the room, an assistant, a guide dog, toilets and other
  facilities. Ask how long the participant can work. This varies more than for
  participants without disabilities.
- **R5. Offer their own equipment and place.** Let the participant use their own
  device and settings, and have the session at home or remote, if they want. Make sure
  that the test version opens on their device. A test environment that only opens on
  an internal network stops this. Use test users and synthetic data. Never ask a
  participant to enter real personal data.
- **R6. Learn the assistive technology.** Ask which assistive technology each
  participant uses, and how. Learn how it works before the session, from the
  participant and from the documentation of the tool.
- **R7. Pay all costs.** Offer to pay travel and all other costs, in addition to the
  usual gift card.
- **R8. Plan up to double time.** Some participants need more time to get ready and to
  do the tasks. Rank the tasks so that the most important come first. Plan breaks, and
  stop when the participant needs it. Practise the session with a colleague before the
  first participant.
- **R9. Prepare remote sessions.** Remote sessions let you test with participants from
  all of the country. Some participants need help in the room, so offer both kinds of
  session. Offer the participant an assistant in the room. Make a short test call
  before the session to check the setup. If the participant uses a screen reader, the
  participant must share the computer sound, so that you hear the screen reader in the
  call and in the recording. Before you record, ask the participant to close
  notifications and other windows that the shared screen can show.
- **R10. Get consent to record.** Ask for consent before you record video or make a
  transcript. Say that the recording is only for internal use in the project, who can
  see it, when you delete it, and that the participant can withdraw. Use a video tool
  that your organisation has approved for recordings, also for sessions in a room. Ask
  the data protection officer (personvernombud) about the legal basis and the storage.

### During the session

- **R11. Ask for a lower speech rate.** Screen reader users often use a high speech
  rate to move fast, and then other people cannot follow. Ask for a lower rate, so that
  you hear what the screen reader says. Then the participant works more slowly than
  usual, so do not use the time as a measure.
- **R12. Expect another way to explore.** A sighted user quickly gets an overview and
  then reads the details. A screen reader user must move through the page to get the
  overview. When the participant moves past the entry to a task, it does not mean that
  they cannot find it.
- **R13. Agree how to talk.** The usual instruction "think aloud and tell what you
  find" is hard when the participant and the moderator must also hear the screen
  reader, and speech can start commands when the participant controls the device with
  the voice. Agree before the session how you will talk during the tasks.
- **R14. Run the rest as a normal test.** Use the same introduction and the same pass
  criteria as in other tests of the service. Speak to the participant, not to the
  person who helps them. A task passes only when the participant finds the way,
  understands the content and the dialogue, and gets the need solved. Look for false
  positives and false negatives during all of the session.

### After the session

- **R15. End with a summary.** Give a short summary, and ask for more or new input.
  The participant can want to say more after you stop the recording.
- **R16. Thank with examples.** Thank the participant with concrete examples of
  findings, and tell how you will use them. The participant must leave with the
  feeling that the session was useful.
- **R17. Ask about later contact.** Ask if you can contact the participant again, or
  add them to your pool of participants (brukerbank). Keep the contact details only
  with consent.

## Plan

Write the plan for this team, these participants and this solution. The plan has only
these parts, in this order:

1. **Before the sessions:** the ready check, recruitment (R1, R2), the questions to
   each participant (R3, R4, R6), equipment and place (R5), costs (R7), time and tasks
   (R8), the test call (R9) and consent (R10).
2. **During each session:** the rules that apply to these participants (R11 to R14).
3. **After each session:** R15 to R17, and the notes for the Findings task: what the
   participant did and said, separate from the conclusions of the moderator.

Write one line for each action, as an instruction to the team. Give a reason only when
the team cannot see it from the action. Use only the rules that apply to these
participants.

An invitation or a consent text for participants says, in plain words:

- what the test is about, and how long it takes
- where: at home, remote or at your place, as the participant prefers
- that you ask about needs before the session, and that an assistant is welcome
- what you pay
- what you record, why, who can see it and when you delete it (R10)
- two ways to reply, such as e-mail and phone

Put the text in the body of the e-mail, not only in an attachment or an image.

## Review of a plan

Check the plan or the script against the rules. Give:

1. The gaps, the most important first. For each gap, give in one sentence what is
   missing or wrong, and in one sentence the change.
2. One line about the parts that are already good, when a reader can think that they
   are gaps.

Do not rewrite the full plan unless the user asks for it.

## Findings

Use this task when the user gives notes or a report from the sessions.

1. Separate what the participant did and said from the conclusions of the moderator.
2. Check each conclusion. Mark it as uncertain when:
   - a screen reader user moved past an element, and the conclusion is that they could
     not find it (R12)
   - the measure is the time, but the speech rate was changed, or the time is
     compared with participants without disabilities (R11)
   - the fix changes only what a sighted user sees, but the problem is for a user who
     does not see the screen
3. Look for false negatives: the participant says that the task went well, but the
   notes show a problem. The notes are the finding.
4. Look for false positives: the participant reached the end of the task, but did not
   understand the result, or the need was not solved (R14).
5. For each finding, give the participant code, what happened, how certain the finding
   is, the cause in the solution if the code or the notes show it, the WCAG success
   criterion if one applies, and the fix.
6. Make a backlog task for each finding, and state in it the result that the fix must
   give, such as what the participant must be able to read or do. When the cause is
   known, the task gives the fix. When the finding is real but the cause is not known,
   the task finds the cause first. When the finding itself is uncertain, the task
   checks it, for example with the same assistive technology or in a new session.
7. When the user asks for fixes, fix the code as in steps 4 and 5 of the code check.
   Ask the team to check each fix with the same assistive technology, and in a new
   session with the participant if the participant agreed to later contact (R17).

## Rules in Norway

The likestillings- og diskrimineringsloven requires universell utforming of the ICT
solutions that public and private businesses aim at the public. The regulation for ICT
solutions (forskrift om universell utforming av IKT-løsninger) lists the WCAG success
criteria, and Uutilsynet (Tilsynet for universell utforming av IKT) supervises it.

- Public bodies must meet 48 success criteria: all criteria at level A and AA in WCAG
  2.1, except 1.2.3 and 1.2.4. 1.2.5 applies to recorded video that is published on
  1 February 2024 or later. The rules also apply to intranets and extranets that are
  new or substantially changed after 1 February 2023. Each website and app must have
  a tilgjengelighetserklæring in the tool from Digdir, updated at least once a
  year.
- Other businesses must meet 35 success criteria from WCAG 2.0, without 1.2.3, 1.2.4
  and 1.2.5.
- Check against the requirements for public bodies, unless the user says that the
  solution is for a business with a smaller set. The set for public bodies also covers
  the smaller set.
- The rules change, so tell the user to check the current status at uutilsynet.no.

A user test does not replace these requirements, and the requirements do not replace a
user test. Mention the regulation only when the user asks about requirements, or when a
finding breaks a success criterion.

## Other skills

- If norsk-sprakvask is installed, apply it yourself to Norwegian text for
  participants. Do not ask the user to run a skill.

## Sources

All text in this skill is original. These public sources informed it:

- Frank Dahle (Digdir), "Sjekkliste for brukertesting med personer med
  funksjonsnedsettelser", UX Norge, 20 October 2026
  (uxnorge.no/sjekkliste-for-brukertesting-med-personer-med-funksjonsnedsettelser).
  R1 to R17 restate this checklist in new words, with additions from the sources
  below. The article states no license, so the skill does not copy its text.
- Uutilsynet, "Brukertesting med funksjonshemmede"
  (uutilsynet.no/veiledning/brukertesting-med-funksjonshemmede/193), the WCAG list for
  the regulation (uutilsynet.no/wcag-standarden/wcag-standarden/86), and the pages
  about the regulation.
- W3C WAI, "Involving Users in Evaluating Web Accessibility"
  (w3.org/WAI/test-evaluate/involving-users), the forms tutorial
  (w3.org/WAI/tutorials/forms) and the ARIA Authoring Practices Guide
  (w3.org/WAI/ARIA/apg).
- GOV.UK Service Manual, "Running research sessions with people with disabilities"
  and "Finding participants for user research" (gov.uk/service-manual), and the
  GOV.UK Design System pages on error summaries and buttons.
- WebAIM, "The WebAIM Million" (webaim.org/projects/million), for the most common
  failures.
- Designsystemet from Digdir (designsystemet.no) and Aksel from NAV (aksel.nav.no),
  which the rules were also checked against.
- WCAG 2.1 (w3.org/TR/WCAG21). The skill gives the numbers of the success criteria,
  not their text.

An AI agent wrote this skill from these sources. AI agents also checked it against the
sources and graded its tests. No human accessibility expert has reviewed it.

This skill is not published or approved by UX Norge, Digdir, Uutilsynet, W3C, WebAIM,
NAV or GOV.UK.
