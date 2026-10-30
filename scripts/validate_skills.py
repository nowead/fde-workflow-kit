#!/usr/bin/env python3
"""Zero-dependency structural checks for the kit's skills, AGENTS.md template, and installer."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / ".agents" / "skills"
EXPECTED = {"kickoff", "clarify", "checkpoint", "audit", "wrapup", "debrief"}
MAX_SKILL_WORDS = 700
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


found = {p.name for p in SKILL_ROOT.iterdir() if p.is_dir()}
check(found == EXPECTED, f"Expected skills {sorted(EXPECTED)}; found {sorted(found)}")

for name in sorted(found & EXPECTED):
    path = SKILL_ROOT / name / "SKILL.md"
    raw = path.read_bytes().decode("utf-8")
    check("\r" not in raw, f"CRLF line endings: {path}")
    m = re.match(r"\A---\n(.*?)\n---\n", raw, flags=re.S)
    if not m:
        errors.append(f"Missing YAML frontmatter: {path}")
        continue
    props = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    skill_name = props.get("name", "").strip()
    description = props.get("description", "").strip()
    check(skill_name == name, f"Frontmatter name must equal folder name: {path}")
    check(re.fullmatch(r"[a-z0-9-]{1,64}", skill_name) is not None, f"Invalid name: {path}")
    check(description.startswith("Use when"), f"Description should start with 'Use when': {path}")
    check(50 <= len(description) <= 1024, f"Description length must be 50-1024 chars: {path}")
    words = len(raw.split())
    check(words <= MAX_SKILL_WORDS, f"Skill too long ({words} > {MAX_SKILL_WORDS} words): {path}")
    check("## Boundaries" in raw, f"Missing '## Boundaries' section: {path}")
    print(f"skill    {name:<11} {words:>4} words")

check((SKILL_ROOT / "kickoff" / "templates.md").is_file(), "kickoff/templates.md is missing")

template = ROOT / "templates" / "AGENTS.md"
text = template.read_bytes().decode("utf-8")
check(len(text.encode("utf-8")) < 32 * 1024, "templates/AGENTS.md exceeds Codex's 32 KiB default")
for needle in ("git push", "0.0.0.0", "computer-use", "UNVERIFIED", "TZ=KST-9",
               "docs/requirements.md", "docs/adr/", "docs/progress.md", "Finishing"):
    check(needle in text, f"templates/AGENTS.md is missing {needle!r}")
for name in EXPECTED:
    check(f"${name}" in text, f"templates/AGENTS.md does not mention ${name}")
print(f"template AGENTS.md    {len(text.encode('utf-8')):>4} bytes, {len(text.split())} words")

for rel in ("install.sh", "README.md"):
    data = (ROOT / rel).read_bytes()
    check(b"\r" not in data, f"CRLF line endings: {rel}")

if errors:
    print("\nFAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("All structural checks passed. Runtime Codex discovery must be tested separately.")
