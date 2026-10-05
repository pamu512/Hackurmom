---
event_name: hackurmom
campus: HKUST
workshop_hours: 3
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
- `workshop_hours` — active time for this curriculum, usually 3. A longer hackathon does not mean a bigger proof of concept.
- `demo_seconds` — the live judging slot.
- `paid_apis` — `optional` means a team may use a paid API they already have. It is not required. `false` forbids one. `true` expects every team to already have a key. Never send anyone to enter a credit card at the event.
- `offline_demo` — leave `false`. A demo that still runs during a network blip is nice, not a finish line, and not a prerequisite. Set `true` only if you want teams to plan for it.
- `mostly_new_to_code` — `true` for this room. About 9 in 10 people have never written code. The agent writes the code. They decide what it does and try it in the browser.
- `require_video` — `true` only if judges will watch videos instead of live demos.
- `devpost_url` — `none` or empty means this event does not use Devpost. The agent will not ask for an exit survey.
- `discord_url` — leave empty if you have no projects channel.
- `submission_note` — the one turn-in instruction, in your words.

If you change `workshop_hours` or `demo_seconds`, update the times on `hackathon/room.html` so the projector matches.
