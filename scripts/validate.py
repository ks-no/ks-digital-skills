#!/usr/bin/env python3
"""Validate the structure and text conventions of this repository.

Run it from anywhere with `python3 scripts/validate.py`. It needs only the Python 3
standard library. It prints one line per error and exits with 1 if there are errors.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
CASES = ROOT / "evals" / "cases.json"

# Built with chr() so that this file does not contain the characters it rejects.
LONG_DASH = chr(0x2014)
LONG_DASH_ESCAPE = chr(92) + "u2014"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_MAX = 64
DESCRIPTION_MAX = 1024
HARNESS_PATHS = (
    "~/.claude",
    ".claude/",
    "CLAUDE.md",
    "~/.copilot",
    ".github/copilot",
    "~/.codex",
    ".agents/",
)
# Components that the tool starts as processes, which can run outside the agent's sandbox.
PROCESS_FILES = (".mcp.json", ".lsp.json", "hooks/hooks.json")
PROCESS_KEYS = ("mcpServers", "lspServers", "hooks")
SKILLS_ONLY = "plugins contain skills only, not MCP servers, LSP servers or hooks"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)[^)]*\)")
FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.MULTILINE | re.DOTALL)
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "build", "dist"}
CASE_KEYS = ("id", "type", "text", "pass")
SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")
# Shorter sentences, such as "It runs in each cluster.", can occur in a skill by chance.
SENTENCE_MIN = 25

errors = []


def rel(path):
    return path.relative_to(ROOT).as_posix()


def error(path, message):
    errors.append(f"{rel(path)}: {message}")


def list_files():
    """Return the files git would track: tracked plus untracked, not ignored."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            capture_output=True,
            check=True,
        )
        names = [n for n in result.stdout.decode("utf-8").split("\0") if n]
        return sorted({ROOT / n for n in names if (ROOT / n).is_file()})
    except (OSError, subprocess.CalledProcessError):
        print("git could not list the files, so every file outside .git is checked.")
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        files.extend(Path(dirpath) / f for f in filenames)
    return sorted(files)


def lines_with(text, needle):
    return [str(i) for i, line in enumerate(text.splitlines(), 1) if needle in line]


def check_text_file(path):
    """Check one file. Return its text, or None if it is binary or not UTF-8."""
    data = path.read_bytes()
    if b"\0" in data:
        if path.suffix == ".md":
            error(path, "markdown file is binary")
        return None
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        error(path, f"not valid UTF-8 ({exc.reason} at byte {exc.start})")
        return None

    if not path.name.startswith("LICENSE"):
        found = lines_with(text, LONG_DASH)
        if found:
            error(path, f"long dash (U+2014) on line {', '.join(found)}")
        if path.suffix == ".json":
            found = lines_with(text, LONG_DASH_ESCAPE)
            if found:
                error(path, f"escaped long dash on line {', '.join(found)}")

    if path.suffix == ".md":
        if not text.strip():
            error(path, "markdown file is empty")
        trailing = [
            str(i)
            for i, line in enumerate(text.splitlines(), 1)
            if line != line.rstrip(" \t")
        ]
        if trailing:
            error(path, f"trailing whitespace on line {', '.join(trailing)}")
    return text


def load_json(path):
    if not path.is_file():
        error(path, "file is missing")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        error(path, f"not valid JSON ({exc})")
        return None


def parse_frontmatter(path, text):
    """Return the top-level `key: value` pairs of the frontmatter, or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        error(path, "does not start with frontmatter (---)")
        return None
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        error(path, "frontmatter is not closed (---)")
        return None

    fields = {}
    key = None
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip()
            if value in (">", ">-", "|", "|-"):
                value = ""
            fields[key] = value.strip("\"'")
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def check_plugin(plugin_dir):
    """Check one plugin. Return the version in its manifests, or None."""
    name = plugin_dir.name
    if not NAME_RE.match(name) or len(name) > NAME_MAX:
        error(plugin_dir, f"directory name must match {NAME_RE.pattern} and be {NAME_MAX} characters or fewer")

    versions = {}
    for manifest in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        data = load_json(plugin_dir / manifest)
        if data is not None and data.get("name") != name:
            error(plugin_dir / manifest, f"name is {data.get('name')!r}, expected {name!r}")
        check_no_processes(plugin_dir / manifest, data)
        if data is not None:
            versions[manifest] = data.get("version")
    if len(set(versions.values())) > 1:
        found = ", ".join(f"{v!r} in {m}" for m, v in versions.items())
        error(plugin_dir, f"the manifests have different versions: {found}")
    version = next(iter(versions.values()), None)
    for path in PROCESS_FILES:
        if (plugin_dir / path).exists():
            error(plugin_dir / path, SKILLS_ONLY)

    skill = plugin_dir / "skills" / name / "SKILL.md"
    if not skill.is_file():
        error(skill, "file is missing")
        return version
    text = skill.read_text(encoding="utf-8", errors="replace")
    fields = parse_frontmatter(skill, text)
    if fields is not None:
        if fields.get("name") != name:
            error(skill, f"frontmatter name is {fields.get('name')!r}, expected {name!r}")
        description = fields.get("description", "")
        if not description:
            error(skill, "frontmatter has no description")
        elif len(description) > DESCRIPTION_MAX:
            error(skill, f"description has {len(description)} characters, the limit is {DESCRIPTION_MAX}")
    for needle in HARNESS_PATHS:
        found = lines_with(text, needle)
        if found:
            error(skill, f"harness-specific reference {needle!r} on line {', '.join(found)}")
    return version


def check_no_processes(path, data, label=""):
    """Report each key in a manifest or a marketplace entry that makes the tool start a process."""
    if not isinstance(data, dict):
        return
    for key in PROCESS_KEYS:
        if key in data:
            error(path, f"{label}has {key!r}, but {SKILLS_ONLY}")


def check_marketplace(path, versions, source_of):
    names = list(versions)
    data = load_json(path)
    if data is None:
        return
    entries = data.get("plugins", [])
    listed = [entry.get("name") for entry in entries]
    for dup in sorted({n for n in listed if listed.count(n) > 1}):
        error(path, f"{dup!r} is listed more than once")
    for missing in sorted(set(names) - set(listed)):
        error(path, f"plugin {missing!r} is not listed")
    for extra in sorted(set(listed) - set(names)):
        error(path, f"{extra!r} is listed, but plugins/{extra} does not exist")
    for entry in entries:
        check_no_processes(path, entry, f"{entry.get('name')!r} ")
        expected = f"./plugins/{entry.get('name')}"
        if source_of(entry) != expected:
            error(path, f"{entry.get('name')!r} has source {source_of(entry)!r}, expected {expected!r}")
        name = entry.get("name")
        if "version" in entry and name in versions and entry["version"] != versions[name]:
            error(path, f"{name!r} has version {entry['version']!r}, the manifests have {versions[name]!r}")


def check_readme(names):
    readme = ROOT / "README.md"
    if not readme.is_file():
        error(readme, "file is missing")
        return
    text = readme.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^## Skills\s*$(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not match:
        error(readme, "has no '## Skills' section")
        return
    for name in names:
        if f"`{name}`" not in match.group(1):
            error(readme, f"plugin {name!r} is not in the '## Skills' section")


def check_links(path, text):
    for target in LINK_RE.findall(FENCE_RE.sub("", text)):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        file_part = target.split("#", 1)[0]
        if file_part and not (path.parent / file_part).exists():
            error(path, f"link target {target!r} does not exist")


def check_cases(texts):
    """Check evals/cases.json, and that no skill file contains a sentence from a case.

    A case must use words that are not in the skills. If a skill copies a sentence from
    a case, the case measures if the agent knows the example, not if it uses the rule.
    """
    if not CASES.is_file():
        return
    data = load_json(CASES)
    if data is None:
        return
    if not isinstance(data, dict) or not all(isinstance(v, list) for v in data.values()):
        error(CASES, "must be an object with a list of cases for each language")
        return
    skills = " ".join(
        " ".join(text.split()).casefold() for path, text in texts.items() if PLUGINS in path.parents
    )
    seen = set()
    for case in (case for cases in data.values() for case in cases):
        case_id = case.get("id") if isinstance(case, dict) else None
        missing = [key for key in CASE_KEYS if not isinstance(case, dict) or not case.get(key)]
        if missing:
            error(CASES, f"case {case_id!r} has no {', '.join(missing)}")
            continue
        if case_id in seen:
            error(CASES, f"case {case_id!r} occurs more than once")
        seen.add(case_id)
        files = case.get("files", [])
        if not isinstance(files, list):
            error(CASES, f"case {case_id!r}: files must be a list of paths")
            files = []
        for name in files:
            if not isinstance(name, str) or not (ROOT / name).is_file():
                error(CASES, f"case {case_id!r}: file {name!r} does not exist")
        for sentence in SENTENCE_END_RE.split(" ".join(case["text"].split())):
            sentence = sentence.rstrip(".!?").casefold()
            if len(sentence) >= SENTENCE_MIN and sentence in skills:
                error(CASES, f"case {case_id!r}: a skill contains {sentence!r}. Write a new case.")


def main():
    texts = {}
    for path in list_files():
        text = check_text_file(path)
        if text is not None:
            texts[path] = text

    plugin_dirs = sorted(
        d for d in PLUGINS.iterdir() if d.is_dir() and not d.name.startswith(("_", "."))
    ) if PLUGINS.is_dir() else []
    versions = {d.name: check_plugin(d) for d in plugin_dirs}
    names = list(versions)

    check_marketplace(
        ROOT / ".claude-plugin" / "marketplace.json", versions, lambda e: e.get("source")
    )
    check_marketplace(
        ROOT / ".agents" / "plugins" / "marketplace.json",
        versions,
        lambda e: (e.get("source") or {}).get("path"),
    )
    check_readme(names)

    for path, text in texts.items():
        if path.suffix == ".md" and PLUGINS in path.parents:
            check_links(path, text)
    check_cases(texts)

    if errors:
        for line in errors:
            print(line)
        print(f"{len(errors)} error(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
