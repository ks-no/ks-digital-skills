---
name: polish
description: Use when the user asks to polish the current branch, or to clean up, proofread and review a change round by round until a round finds nothing more, before a pull request or a merge. The user can give a maximum number of rounds.
disable-model-invocation: true
argument-hint: [max-rounds]
---

# Polish the current branch

## Where things stand

Before the first round, find the base: the default branch of the remote, such as
`origin/main`, or the local default branch if there is no remote. Do not use the
upstream of the current branch, because for a pushed branch it is the same branch. If
you cannot tell which branch is the default branch, ask the user. Run these and read the
output:

- `git branch --show-current`
- `git log <base>..HEAD`
- `git status --short`
- `git diff --stat --merge-base <base>`

In this skill, "the diff" is `git diff --merge-base <base>` plus the untracked files that
`git status --short` shows. It includes the commits and the uncommitted changes.

The stated requirements are in the task, the issue, the pull request text and the full
commit messages. They also include the rules that the project or its domain must obey,
such as universell utforming (accessibility) for public-sector services in Norway. A
finding matters when it affects correctness or a stated requirement.

If a restriction, such as the sandbox or a permission, stops a command, report the
command and the restriction, and stop the run. Do not try another way to do what the
command does. Do not suggest a change to the sandbox, the permissions or the tool
configuration.

If a skill that this skill uses is not installed, skip the work that needs it, and say so
in the report.

## The check

Find it once, before the first round, and tell the user what it is: the gates the project
documents, the `package.json` scripts, or the CI config. It has to pass or fail on its
own. "The reviewer had nothing more to say" is not a check. Leave out each gate that
starts the app, a server or a browser, such as end-to-end tests, and name it in the
report. If the project has no check, say so in the report, and use the stop rule
without it.

In a pnpm project, for example, the check can be `pnpm lint`, `pnpm test`, and the
`test:*` gates that the change touches. It can also be a snapshot or contract test that
must stay byte-identical to the default branch, unless the change is meant to move it.

If the diff changes what a user sees or does in a web interface, use
`guided-click-through` before the first round. Use its sections to find what to check
and to write and run behaviour tests for the change, but not for the click-through yet.
Fix what the tests show. Give the other findings in the code to the correctness reviewer
of round 1, and triage them with its findings. The tests are part of the check in every
round, so the check fails at once if a cleanup breaks the behaviour. If the project has
no component tests, say so in the report, and suggest that the project adds them.

## The loop

At most the number of rounds the user gives, default 3. One round is:

1. **Cleanup review** of the diff: reuse, simplification, efficiency, and code at the
   wrong level of abstraction. It looks for quality, not bugs: a bug you notice here goes
   to the correctness review in step 3.
2. **Language pass** on the prose that the diff adds or changes. From round 2, only on
   prose that changed since the last language pass. Prose is docs, comments, docstrings,
   test names, error and log messages, and strings that a person or a model reads.
   Rewrite English with `asd-ste100-english`, and Norwegian with `asd-ste100-norsk` and
   then `norsk-sprakvask`. Do not change identifiers, quotations, strings that the code
   matches against user input, or messages that a snapshot or contract test pins. When
   you change a message that another test asserts on, update the test in the same edit.
3. **Correctness review** of the diff: bugs, unhandled cases, and broken contracts. The
   review also covers the language pass. In the same step, do the security review (see
   "The security review in step 3").
4. **Run the check.** A failure is a finding that matters. Fix the cause and run the
   check again.

The reviews in steps 1 and 3:

- If your tool has a built-in command for a cleanup review, use it in step 1. If it has
  a built-in code-review command that looks for bugs, use it for the correctness review
  in step 3. If not, and you can start a separate agent with a fresh context, let that
  agent review. If a command applies its changes itself, treat each change as a finding,
  and undo the changes that do not survive your triage.
- Give each reviewer the diff with the untracked files named, and the findings that you
  already skipped. Also give the correctness reviewer each edit of the language pass in
  this round, with the old and the new text. Tell it that a rewrite that changes a
  meaning or removes a hedge is a finding. From round 2, also tell each reviewer what
  changed since the last review.
- Tell the correctness reviewer what counts: gaps that affect correctness or a stated
  requirement. Give it the stated requirements. Tell it that no findings is a valid
  answer.
- Apply the findings that survive your triage (see "Do not touch what the findings do
  not reach").

The security review in step 3:

- Select the security skills from the files in the diff:
  - `secure-coding` for application code.
  - `github-actions-security` for GitHub Actions workflows, composite actions and the
    Dependabot configuration.
  - `container-security` for Dockerfiles and Containerfiles, Helm charts, Kustomize
    files, and Kubernetes or OpenShift manifests.
- If no file in the diff is for a security skill, do not do the security review. Say so
  in the report.
- One security reviewer does the review for all the selected skills. If you can start a
  separate agent with a fresh context, let that agent review. If not, do the review
  yourself. Do not use a built-in command for a security review in its place.
- Tell the security reviewer to use each selected skill in review mode, only on the
  files for that skill. Give it the same input as the correctness reviewer, but not the
  edits of the language pass.
- Tell the security reviewer what counts: a finding with the severity Critical, High or
  Medium in the selected skill. Tell it that no findings is a valid answer.
- Triage and apply the security findings as the other findings.

Call each skill by its name. A tool that prefixes plugin skills with the plugin name
gives them these full names: `asd-ste100-english:asd-ste100-english`,
`asd-ste100-norsk:asd-ste100-norsk`, `norsk-sprakvask:norsk-sprakvask`,
`guided-click-through:guided-click-through`, `secure-coding:secure-coding`,
`github-actions-security:github-actions-security` and
`container-security:container-security`.

Stop when a round finds nothing that matters and the check passes, or at the cap.

The run ends on a correctness review of the final tree. If you applied anything in or
after step 3 of the last round, run step 3 and the check once more. A cosmetic fix and a
fix for a failed check also count as applied. Apply nothing from this last step 3 and
check. If they find something that matters, and the cap allows another round, start that
round, and give the finding to its step 3. If the cap does not allow it, report the
finding as open.

**Cosmetic fixes do not extend the run.** Examples are whitespace, a helper in an
awkward place, and a comment that you would write differently. Apply them or skip them.
They do not make the round count as one that found something. If they did, a blank line
could make the loop start again forever. The language pass is cosmetic too, unless the
old text could make a reader do the wrong thing. A new test that closes a gap in the
tests, and fixes no defect, counts the same way. So does a fix for a security finding
with the severity Low, because Low is hardening with no known attack path.

## What makes this converge

**Tell the reviewer what counts.** A reviewer that you ask to find gaps will report
some in sound work, because that is its task. If you fix all of them, you get defensive
code and abstraction that nobody wanted. The list of findings that you already skipped
stops the reviewer from reporting them again.

**Never end on a cleanup.** A cleanup pass adds defects of its own, and the review after
it finds them. This is why the language pass comes before the review, not after it.

**Break every new or changed check before you trust it.** Undo the thing that it must
catch, see that the check fails, and restore the code. A green check that you did not
break has not measured anything. Also make sure that the edit changed the file: a revert
that matched nothing passes for the wrong reason. If the check cannot catch a fix, say
so in the report.

**Fix the cause, not each symptom.** When several findings point at one mechanism, make
one fix upstream of all of them. Say so, and do not patch three places.

**Do not touch what the findings do not reach.** Skip a finding when its fix would
change intended behaviour or needs work well outside the diff, or when you judge it a
false positive. Note the skip in one line. Do not argue with it.

**Do not decide what the requirements leave open.** Some fixes need a choice that the
stated requirements do not make, such as which input a field accepts. Fix what is wrong
under every option. Keep the rest as the change has it, and report the choice as an open
decision. Then the change stays small if the user makes the choice later.

## Report at the end

Start with one to three lines about what can change the next action of the reader.
Then give the behaviour tests from before round 1 and the fixes they caused, if any.
Then, per round: what was fixed, what the language pass changed (one line, not every
sentence), what was skipped and why, and what the check said. Then say which reason
ended the run, and give the other notes that this skill sends to the report, such as a
gate that you left out or a skill that is not installed. Then give the open findings:
each finding that matters and that the run did not fix, with the reason. Then give the
open decisions that the run found but did not take. Keep the two lists apart, so that
the reader can see what is a defect and what is a choice.

For a change to a web interface, end the report with a click-through of the final tree
from `guided-click-through`. Give the skill the open decisions. Also give it, as a risk
to check, each fix that the check cannot catch and that changes what a user sees or
does. In this use, the skill changes no file. From its output, give only the
click-through, the risks that it left out, and each defect that it finds. Report each
defect as an open finding. If the skill gives no click-through, end the report with its
reason in one line. The click-through is not a step in the loop, because it needs a
person and the run must be able to finish without one.

When the user reports a failed step or selects an option in a decision step, apply the
change, review it and run the check, as for any other change.
