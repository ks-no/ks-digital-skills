#!/usr/bin/env python3
"""Run the held-out texts in evals/cases.json through a model.

Each text runs with the skills in this checkout. With --before, each text also runs
with the skills at an earlier git ref, so you can compare the two. The script does not
score the answers. The result puts the pass criterion of each case next to the answers.

The model command gets the prompt on stdin and must write the answer to stdout:

    python3 evals/run.py --cmd "ollama run llama3.1" --before main --out evals/results/llama.md

It needs only the Python 3 standard library and git.
"""

import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = Path(__file__).resolve().parent / "cases.json"

# The files that the model reads for each language, relative to the repo root.
SKILL_FILES = {
    "en": ["plugins/asd-ste100-english/skills/asd-ste100-english/SKILL.md"],
    "no": [
        "plugins/norsk-sprakvask/skills/norsk-sprakvask/SKILL.md",
        "plugins/norsk-sprakvask/skills/norsk-sprakvask/references/ki-markorer.md",
    ],
}

TASKS = {
    "en": "Task: rewrite this text with the skill. Select the mode that the skill gives "
    "for the text type. Reply with only the output that the skill tells you to give.",
    "no": "Oppgave: språkvask denne teksten med skillen. Svar bare med det skillen ber "
    "deg gi.",
}


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def skill_text(ref, lang):
    """Return the skill files for one language, from the checkout or from a git ref."""
    parts = []
    for name in SKILL_FILES[lang]:
        text = git("show", f"{ref}:{name}") if ref else (ROOT / name).read_text(encoding="utf-8")
        parts.append(f'<file path="{name}">\n{text}\n</file>')
    return "\n\n".join(parts)


def prompt(skill, lang, text):
    return (
        f"Follow this skill.\n\n<skill>\n{skill}\n</skill>\n\n"
        f"{TASKS[lang]}\n\n---\n{text}\n---\n"
    )


def ask(cmd, text, timeout):
    try:
        result = subprocess.run(
            cmd, input=text, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return f"(no answer after {timeout} seconds)"
    if result.returncode != 0:
        return f"(the command failed with exit code {result.returncode}) {result.stderr.strip()}".strip()
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--cmd", required=True, help='model command, for example "ollama run llama3.1"')
    parser.add_argument("--before", help="git ref with the skills to compare with, for example main")
    parser.add_argument("--only", help="comma-separated case IDs, for example E3,E7,N3")
    parser.add_argument("--runs", type=int, default=1, help="runs per case and version (default 1)")
    parser.add_argument("--timeout", type=int, default=600, help="seconds per answer (default 600)")
    parser.add_argument("--out", help="result file (default stdout)")
    args = parser.parse_args()

    cmd = shlex.split(args.cmd)
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    only = set(args.only.split(",")) if args.only else None
    if args.before and subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{args.before}^{{commit}}"],
        cwd=ROOT, capture_output=True,
    ).returncode != 0:
        sys.exit(f"--before: {args.before!r} is not a commit in this repo")

    versions = [("After", None)]
    if args.before:
        versions.insert(0, ("Before", args.before))
    skills = {(ref, lang): skill_text(ref, lang) for _, ref in versions for lang in SKILL_FILES}

    head = git("rev-parse", "--short", "HEAD").strip()
    if git("status", "--porcelain", "--", "plugins"):
        head += " with uncommitted changes"
    lines = [
        "# Held-out texts\n",
        f"Model command: `{args.cmd}`. After: the checkout ({head}).",
        f"Before: `{args.before}`.\n" if args.before else "",
    ]
    for lang in SKILL_FILES:
        for case in cases[lang]:
            if only and case["id"] not in only:
                continue
            lines += [
                f"## {case['id']}: {case['type']}\n",
                f"Input: {case['text']}\n",
                f"Pass: {case['pass']}\n",
            ]
            for label, ref in versions:
                for run in range(1, args.runs + 1):
                    print(f"{case['id']} {label.lower()} {run}", file=sys.stderr)
                    answer = ask(cmd, prompt(skills[ref, lang], lang, case["text"]), args.timeout)
                    heading = f"### {label}" + (f", run {run}" if args.runs > 1 else "")
                    lines += [f"{heading}\n", f"````text\n{answer}\n````\n"]

    output = "\n".join(lines)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(output, encoding="utf-8")
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
