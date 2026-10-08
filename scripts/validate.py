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
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)[^)]*\)")
FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.MULTILINE | re.DOTALL)
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "build", "dist"}

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
    name = plugin_dir.name
    if not NAME_RE.match(name) or len(name) > NAME_MAX:
        error(plugin_dir, f"directory name must match {NAME_RE.pattern} and be {NAME_MAX} characters or fewer")

    for manifest in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        data = load_json(plugin_dir / manifest)
        if data is not None and data.get("name") != name:
            error(plugin_dir / manifest, f"name is {data.get('name')!r}, expected {name!r}")

    skill = plugin_dir / "skills" / name / "SKILL.md"
    if not skill.is_file():
        error(skill, "file is missing")
        return
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


def check_marketplace(path, names, source_of):
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
        expected = f"./plugins/{entry.get('name')}"
        if source_of(entry) != expected:
            error(path, f"{entry.get('name')!r} has source {source_of(entry)!r}, expected {expected!r}")


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


def main():
    texts = {}
    for path in list_files():
        text = check_text_file(path)
        if text is not None:
            texts[path] = text

    plugin_dirs = sorted(
        d for d in PLUGINS.iterdir() if d.is_dir() and not d.name.startswith(("_", "."))
    ) if PLUGINS.is_dir() else []
    names = [d.name for d in plugin_dirs]
    for plugin_dir in plugin_dirs:
        check_plugin(plugin_dir)

    check_marketplace(
        ROOT / ".claude-plugin" / "marketplace.json", names, lambda e: e.get("source")
    )
    check_marketplace(
        ROOT / ".agents" / "plugins" / "marketplace.json",
        names,
        lambda e: (e.get("source") or {}).get("path"),
    )
    check_readme(names)

    for path, text in texts.items():
        if path.suffix == ".md" and PLUGINS in path.parents:
            check_links(path, text)

    if errors:
        for line in errors:
            print(line)
        print(f"{len(errors)} error(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
