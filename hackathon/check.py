#!/usr/bin/env python3
"""Fail if the college-hackathon floor drifts away from the skills."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_EVENT_KEYS = (
    "event_name:",
    "campus:",
    "workshop_hours:",
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

SKILLS = ("1-start", "2-scope", "3-prd", "4-spec", "5-build", "6-ship")
FLOOR_LINE = "skills/hackathon-floor.md"


def main() -> None:
    failures: list[str] = []

    event = (ROOT / "hackathon" / "event.md").read_text()
    for key in REQUIRED_EVENT_KEYS:
        if key not in event:
            failures.append(f"hackathon/event.md missing {key}")

    floor_rules = ROOT / "skills" / "hackathon-floor.md"
    if not floor_rules.exists():
        failures.append("missing skills/hackathon-floor.md")

    skill0 = (ROOT / "skills" / "0-floor" / "SKILL.md").read_text()
    if "name: 0-floor" not in skill0 or "devpost/floor.md" not in skill0:
        failures.append("0-floor skill is missing its name or floor file")
    template = ROOT / "skills" / "0-floor" / "templates" / "floor-template.md"
    if "doc: floor" not in template.read_text():
        failures.append("floor template missing")

    for name in SKILLS:
        text = (ROOT / "skills" / name / "SKILL.md").read_text()
        if FLOOR_LINE not in text:
            failures.append(f"{name} does not point at the floor rules")

    start = (ROOT / "skills" / "1-start" / "SKILL.md").read_text()
    if "hackathon/" not in start:
        failures.append("1-start folder check does not ignore hackathon/")

    spec = (ROOT / "skills" / "4-spec" / "SKILL.md").read_text()
    if "only when `offline_demo` is true" not in spec:
        failures.append("4-spec treats wifi-off as required")

    ship = (ROOT / "skills" / "6-ship" / "SKILL.md").read_text()
    if "require_live_demo" not in ship:
        failures.append("6-ship does not follow the event file's live demo flag")

    ignore = (ROOT / ".gitignore").read_text()
    for path in ("/devpost/learner-profile.md", "/devpost/floor.md"):
        if path not in ignore:
            failures.append(f".gitignore missing {path}")

    room = (ROOT / "hackathon" / "room.html").read_text()
    if "Start the hackathon" not in room:
        failures.append("room board missing the start phrase")
    if "fonts.googleapis.com" in room or "cdn." in room:
        failures.append("room board depends on a network asset")

    for name in ("AGENTS.md", "START.md", "ORGANIZER.md", "PREREQUISITES.md"):
        if not (ROOT / name).exists():
            failures.append(f"missing {name}")

    prereq = (ROOT / "PREREQUISITES.md").read_text()
    if "git config --global user.name" not in prereq or "does not care which model" not in prereq:
        failures.append("PREREQUISITES.md is missing git identity or the agent-agnostic rule")
    if "Cursor desktop" in prereq or "Type this in Cursor" in room:
        failures.append("workshop copy still requires Cursor")

    link = ROOT / ".cursor" / "skills" / "0-floor"
    if not link.is_symlink() or not (link / "SKILL.md").exists():
        failures.append(".cursor/skills/0-floor symlink is missing or broken")

    if failures:
        raise SystemExit("\n".join(failures))
    print("hackathon floor ok")


if __name__ == "__main__":
    main()
