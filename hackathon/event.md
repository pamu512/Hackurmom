---
event_name: hackurmom
campus: HKUST
workshop_hours: 3
build_freeze_minutes: 25
demo_seconds: 300
paid_apis: optional
offline_demo: false
mostly_new_to_code: true
require_live_demo: true
require_public_github: true
require_video: false
devpost_url: none
discord_url:
submission_note: Leave your public GitHub URL with the judging table. No slide deck.
---

# Organizer settings

Students do not need to edit this file. `0-floor` copies it into the team's `devpost/floor.md`.

Change the fields above before doors open:

- `event_name` and `campus` — what mentors say out loud. Replace the placeholders.
- `workshop_hours` — a planning estimate: how long a typical team needs, not a limit. There is no hard time limit. Do not run a countdown at this event, and do not rush a team that is making progress.
- `build_freeze_minutes` — the one operational deadline: minutes before the demo slot when all building stops and every team rehearsees. Announce it out loud; it is the room's only "clock" moment.
- `demo_seconds` — the live judging slot.
- `paid_apis` — `optional` means a team may use a paid API they already have. It is not required. `false` forbids one. `true` expects every team to already have a key. Never send anyone to enter a credit card at the event.
- `offline_demo` — leave `false`. A demo that still runs during a network blip is nice, not a finish line, and not a prerequisite. Set `true` only if you want teams to plan for it.
- `mostly_new_to_code` — `true` for this room. About 9 in 10 people have never written code. The agent writes the code. They decide what it does and try it in the browser.
- `require_video` — `true` only if judges will watch videos instead of live demos.
- `devpost_url` — `none` or empty means this event does not use Devpost. The agent will not ask for an exit survey.
- `discord_url` — leave empty if you have no projects channel.
- `submission_note` — the one turn-in instruction, in your words.

If you change `demo_seconds`, update the judging line on `hackathon/room.html` so the projector matches. The board runs on milestones, not wall-clock times, so `workshop_hours` no longer needs a matching edit. Consider running the optional pre-mixer in [mixer.md](mixer.md) the week before.
