#!/usr/bin/env python3
"""Run the held-out texts in evals/cases.json through a model.

Each text runs with the skills in this checkout. With --before, each text also runs
with the skills at an earlier git ref, so you can compare the two. With --baseline,
each text also runs without a skill, or with one sentence in place of the skill. The
script does not score the answers. The result puts the pass criterion of each case
next to the answers.

The model command gets the prompt on stdin and must write the answer to stdout:

    python3 evals/run.py --cmd "ollama run llama3.1" --before main --out evals/results/llama.md

With --dump, the script writes each prompt to a file and calls no model. Use this when
an agent or a person runs the prompts.

It needs only the Python 3 standard library and git.
"""

import argparse
import json
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = Path(__file__).resolve().parent / "cases.json"

# The files that the model reads for each group of cases, relative to the repo root.
# A case can add more files with a "files" list, for example the references that the
# skill tells the agent to load for that kind of task.
SKILL_FILES = {
    "en": ["plugins/asd-ste100-english/skills/asd-ste100-english/SKILL.md"],
    "no": [
        "plugins/norsk-sprakvask/skills/norsk-sprakvask/SKILL.md",
        "plugins/norsk-sprakvask/skills/norsk-sprakvask/references/ki-markorer.md",
    ],
    "github-actions-security": [
        "plugins/github-actions-security/skills/github-actions-security/SKILL.md",
    ],
}

SECURITY_TASK = (
    "Task: do what the text asks. Give the answer that you would give to the user who "
    "asked."
)

TASKS = {
    "en": "Task: rewrite this text with the skill. Select the mode that the skill gives "
    "for the text type. Reply with only the output that the skill tells you to give.",
    "no": "Oppgave: språkvask denne teksten med skillen. Svar bare med det skillen ber "
    "deg gi.",
    "github-actions-security": SECURITY_TASK,
}

# Variants without a skill. Use them to find out if a skill does better than no help,
# and better than one short sentence. They run only for the groups with SECURITY_TASK,
# because the sentence is about security and the other tasks tell the model to use a skill.
BASELINES = {
    "none": ("No skill", None),
    "sentence": (
        "One sentence",
        "Make the result secure. Follow OWASP guidance, and report the security "
        "problems that you find.",
    ),
}


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def read_file(ref, name):
    """Return one file from the checkout or from a git ref, or None if it does not exist."""
    if not ref:
        path = ROOT / name
        return path.read_text(encoding="utf-8") if path.is_file() else None
    result = subprocess.run(
        ["git", "show", f"{ref}:{name}"], cwd=ROOT, capture_output=True, text=True,
        encoding="utf-8",
    )
    return result.stdout if result.returncode == 0 else None


def skill_text(ref, names):
    """Return the skill files as one text, or None if a file does not exist at ref."""
    parts = []
    for name in names:
        text = read_file(ref, name)
        if text is None:
            return None
        parts.append(f'<file path="{name}">\n{text}\n</file>')
    return "\n\n".join(parts)


def prompt(task, text, skill=None, sentence=None):
    if skill is not None:
        head = f"Follow this skill.\n\n<skill>\n{skill}\n</skill>\n\n"
    elif sentence:
        head = f"{sentence}\n\n"
    else:
        head = ""
    return f"{head}{task}\n\n---\n{text}\n---\n"


def ask(cmd, text, timeout, workdir):
    try:
        result = subprocess.run(
            cmd, input=text, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=timeout, cwd=workdir,
        )
    except subprocess.TimeoutExpired:
        return f"(no answer after {timeout} seconds)"
    except OSError as error:
        return f"(the command could not start: {error})"
    if result.returncode != 0:
        return f"(the command failed with exit code {result.returncode}) {result.stderr.strip()}".strip()
    return result.stdout.strip()


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--cmd", help='model command, for example "ollama run llama3.1"')
    parser.add_argument("--before", help="git ref with the skills to compare with, for example main")
    parser.add_argument(
        "--baseline",
        help="comma-separated variants without a skill, for the security cases only: none, sentence",
    )
    parser.add_argument("--only", help="comma-separated case IDs, for example E3,E7,N3")
    parser.add_argument("--runs", type=int, default=1, help="runs per case and version (default 1)")
    parser.add_argument("--timeout", type=int, default=600, help="seconds per answer (default 600)")
    parser.add_argument("--workdir", help="directory to run the model command in")
    parser.add_argument("--dump", help="write each prompt to a file in this directory, and call no model")
    parser.add_argument("--out", help="result file (default stdout)")
    args = parser.parse_args()

    if not args.cmd and not args.dump:
        sys.exit("give --cmd, or --dump to write the prompts to files")
    if args.workdir and not Path(args.workdir).is_dir():
        sys.exit(f"--workdir: {args.workdir!r} is not a directory")
    cmd = shlex.split(args.cmd) if args.cmd else None
    if cmd and "/" in cmd[0]:
        # A relative path must not change meaning when --workdir changes the directory.
        cmd[0] = str(Path(cmd[0]).resolve())
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    only = set(args.only.split(",")) if args.only else None
    if args.before and subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{args.before}^{{commit}}"],
        cwd=ROOT, capture_output=True,
    ).returncode != 0:
        sys.exit(f"--before: {args.before!r} is not a commit in this repo")
    baselines = args.baseline.split(",") if args.baseline else []
    unknown = [name for name in baselines if name not in BASELINES]
    if unknown:
        sys.exit(f"--baseline: unknown variant {', '.join(unknown)}. Use {', '.join(BASELINES)}.")

    # Each version is (label, git ref or None for the checkout, sentence, uses a skill).
    versions = [(BASELINES[name][0], None, BASELINES[name][1], False) for name in baselines]
    if args.before:
        versions.append(("Before", args.before, None, True))
    versions.append(("After", None, None, True))

    head = git("rev-parse", "--short", "HEAD").strip()
    if git("status", "--porcelain", "--", "plugins"):
        head += " with uncommitted changes"
    lines = [
        "# Held-out texts\n",
        f"Model command: `{args.cmd}`. After: the checkout ({head}).",
        f"Before: `{args.before}`.\n" if args.before else "",
    ]
    dump = Path(args.dump) if args.dump else None
    if dump:
        dump.mkdir(parents=True, exist_ok=True)
    skills = {}
    for group in SKILL_FILES:
        group_cases = [case for case in cases.get(group, []) if not only or case["id"] in only]
        group_versions = versions
        if group_cases and baselines and TASKS[group] != SECURITY_TASK:
            group_versions = [version for version in versions if version[3]]
            print(f"{group}: --baseline is only for the security cases", file=sys.stderr)
        for case in group_cases:
            names = tuple(SKILL_FILES[group] + case.get("files", []))
            lines += [
                f"## {case['id']}: {case['type']}\n",
                f"Input: {case['text']}\n",
                f"Pass: {case['pass']}\n",
            ]
            for label, ref, sentence, uses_skill in group_versions:
                skill = None
                if uses_skill:
                    if (ref, names) not in skills:
                        skills[ref, names] = skill_text(ref, names)
                    skill = skills[ref, names]
                    if skill is None:
                        where = f"`{ref}`" if ref else "the checkout"
                        note = f"the skill files do not exist in {where}"
                        print(f"{case['id']} {label.lower()}: {note}", file=sys.stderr)
                        lines += [f"### {label}\n", f"({note})\n"]
                        continue
                text = prompt(TASKS[group], case["text"], skill, sentence)
                if dump:
                    path = dump / f"{case['id']}-{slug(label)}.txt"
                    path.write_text(text, encoding="utf-8")
                    continue
                for run in range(1, args.runs + 1):
                    print(f"{case['id']} {label.lower()} {run}", file=sys.stderr)
                    start = time.monotonic()
                    answer = ask(cmd, text, args.timeout, args.workdir)
                    seconds = time.monotonic() - start
                    heading = f"### {label}" + (f", run {run}" if args.runs > 1 else "")
                    heading += f" ({len(answer.split())} words, {seconds:.0f} s)"
                    lines += [f"{heading}\n", f"````text\n{answer}\n````\n"]

    if dump:
        print(f"Wrote the prompts to {dump}", file=sys.stderr)
        return
    output = "\n".join(lines)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(output, encoding="utf-8")
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
