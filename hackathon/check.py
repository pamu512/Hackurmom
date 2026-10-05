#!/usr/bin/env python3
"""Fail if the college-hackathon floor drifts away from the skills."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_EVENT_KEYS = (
    "event_name:",
    "campus:",
    "workshop_hours:",
    "build_freeze_minutes:",
    "demo_seconds:",
    "paid_apis:",
    "mostly_new_to_code:",
    "offline_demo:",
    "require_live_demo:",
    "require_public_github:",
    "require_video:",
    "devpost_url:",
    "discord_url:",
    "submission_note:",
)

CURRICULUM_SKILLS = ("1-start", "2-scope", "3-prd", "4-spec", "5-build", "6-ship")
ALL_SKILLS = ("0-floor",) + CURRICULUM_SKILLS
FLOOR_LINE = "skills/hackathon-floor.md"

SUPPORT_FILES = {
    "0-floor": ("templates/floor-template.md",),
    "1-start": ("templates/learner-profile-template.md",),
    "2-scope": ("templates/scope-template.md",),
    "3-prd": ("templates/prd-template.md", "references/prd-guide.md"),
    "4-spec": ("templates/spec-template.md", "references/spec-patterns.md"),
    "5-build": ("templates/checklist-template.md", "references/code-tour.md"),
    "6-ship": (),
}


def event_values(text):
    """Read the key: value pairs out of the hackathon/event.md frontmatter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    values = {}
    for line in lines[1:end]:
        key, sep, value = line.partition(":")
        if sep and key.strip() and not key.strip().startswith(("-", "#")):
            values[key.strip()] = value.strip()
    return values


def main() -> None:
    failures = []

    def read(path):
        try:
            return path.read_text()
        except OSError:
            failures.append(f"cannot read {path.relative_to(ROOT)}")
            return None

    event = read(ROOT / "hackathon" / "event.md")
    if event is not None:
        for key in REQUIRED_EVENT_KEYS:
            if key not in event:
                failures.append(f"hackathon/event.md missing {key}")
    settings = event_values(event or "")

    if not (ROOT / "skills" / "hackathon-floor.md").exists():
        failures.append("missing skills/hackathon-floor.md")

    for name in ALL_SKILLS:
        skill = read(ROOT / "skills" / name / "SKILL.md")
        if skill is None:
            continue
        if f"name: {name}" not in skill:
            failures.append(f"{name} is missing its frontmatter name")
        for rel in SUPPORT_FILES[name]:
            if not (ROOT / "skills" / name / rel).exists():
                failures.append(f"{name} is missing skills/{name}/{rel}")

    floor_skill = read(ROOT / "skills" / "0-floor" / "SKILL.md") or ""
    if "devpost/floor.md" not in floor_skill:
        failures.append("0-floor skill is missing its floor file")
    template = read(ROOT / "skills" / "0-floor" / "templates" / "floor-template.md") or ""
    if "doc: floor" not in template:
        failures.append("floor template missing")

    for name in CURRICULUM_SKILLS:
        skill = read(ROOT / "skills" / name / "SKILL.md") or ""
        if FLOOR_LINE not in skill:
            failures.append(f"{name} does not point at the floor rules")

    start = read(ROOT / "skills" / "1-start" / "SKILL.md") or ""
    if "hackathon/" not in start:
        failures.append("1-start folder check does not ignore hackathon/")

    spec = read(ROOT / "skills" / "4-spec" / "SKILL.md") or ""
    if "only when `offline_demo` is true" not in spec:
        failures.append("4-spec treats wifi-off as required")

    ship = read(ROOT / "skills" / "6-ship" / "SKILL.md") or ""
    if "require_live_demo" not in ship:
        failures.append("6-ship does not follow the event file's live demo flag")

    ignore = read(ROOT / ".gitignore") or ""
    for path in ("/devpost/learner-profile.md", "/devpost/floor.md"):
        if path not in ignore:
            failures.append(f".gitignore missing {path}")

    room = read(ROOT / "hackathon" / "room.html") or ""
    if "Start the hackathon" not in room:
        failures.append("room board missing the start phrase")
    if "fonts.googleapis.com" in room or "cdn." in room:
        failures.append("room board depends on a network asset")
    if "Milestones" not in room:
        failures.append("room board no longer shows milestones")
    if re.search(r"\d{1,2}:\d{2}", room):
        failures.append("room board still shows wall-clock times")
    seconds = settings.get("demo_seconds", "")
    if seconds and f"{seconds} second" not in room:
        failures.append(f"room board does not match demo_seconds ({seconds})")
    if not (ROOT / "hackathon" / "mixer.md").exists():
        failures.append("missing hackathon/mixer.md (pre-mixer guide)")

    agents = read(ROOT / "AGENTS.md") or ""
    if "skills/0-floor/SKILL.md" not in agents or "hackathon/event.md" not in agents:
        failures.append("AGENTS.md no longer routes agents into the skills")
    claude = read(ROOT / "CLAUDE.md") or ""
    if claude != agents:
        failures.append("CLAUDE.md differs from AGENTS.md")

    for name in ("AGENTS.md", "START.md", "ORGANIZER.md", "PREREQUISITES.md"):
        if not (ROOT / name).exists():
            failures.append(f"missing {name}")

    prereq = read(ROOT / "PREREQUISITES.md") or ""
    if "git config --global user.name" not in prereq or "does not care which model" not in prereq:
        failures.append("PREREQUISITES.md is missing git identity or the agent-agnostic rule")
    if "Cursor desktop" in prereq or "Type this in Cursor" in room:
        failures.append("workshop copy still requires Cursor")

    rules = read(ROOT / ".cursor" / "rules" / "hackathon.mdc") or ""
    if rules and "AGENTS.md" not in rules:
        failures.append(".cursor/rules no longer defers to AGENTS.md")

    for name in ALL_SKILLS:
        link = ROOT / ".cursor" / "skills" / name
        if not link.is_symlink() or not (link / "SKILL.md").exists():
            failures.append(
                f".cursor/skills/{name} symlink is missing or broken "
                "(on Windows: enable Developer Mode and re-clone)"
            )

    if failures:
        raise SystemExit("\n".join(failures))
    print("hackathon floor ok")


if __name__ == "__main__":
    main()
