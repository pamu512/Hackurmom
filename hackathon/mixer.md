# Pre-mixer

An optional 45–60 minute session in the days before the hackathon. It has one job: when teams sit down on event day, `Start the hackathon` works on the first try, and the room already knows what the workshop is and how to get the most out of it.

This is not a lecture and not a shorter version of the workshop. Nothing here starts the build. Teams leave with a working laptop, a GitHub account, and an idea they have said out loud.

## What to cover

A workable shape for 60 minutes. Drop the last two blocks for a 45-minute version.

| Minutes | Block | What happens |
|---|---|---|
| 0–10 | **What this is** | The finish line: a proof of concept demoed live from this laptop, a public GitHub repo, a rehearsed demo. Not a startup, no slide decks. Show [hackathon/room.html](room.html) if you have a screen. |
| 10–20 | **How to get the most out of it** | The agent interviews; the team decides. One driver per team. The agent writes all the code. What a good answer looks like: brain dumps beat one-line prompts. This is the flipped-interaction pitch, in your own words. |
| 20–35 | **Laptop check** | Run the checklist below on the account the student will actually use. Mentors walk the room. Fix failures here, not on event day. |
| 35–50 | **GitHub and a push** | Everyone who will publish creates the account now, signs in once, and pushes to a throwaway test repo. A password reset mid-build is how demos die. |
| 50–60 | **Say the idea out loud** | Teams that already have a rough idea say it to another team once. No feedback round, no pitch coaching. Saying it once out loud makes the scope interview on event day much faster. |

## Laptop checklist (the block that matters)

From [PREREQUISITES.md](../PREREQUISITES.md), compressed to what a mentor can check in one pass:

- A coding agent is installed, signed in, and can edit files and run commands in this folder. Send one real message; confirm it can create a file. Delete the file afterward.
- `git --version` prints a version, and `git config --global user.name` / `user.email` both print a value.
- The publisher's GitHub account exists and a push from this laptop already works.
- A few gigabytes free, a browser, power for the whole event.
- On Windows: Developer Mode enabled (or `git config --global core.symlinks true`) before cloning, so the `.cursor/skills` links survive.

## What you say about the clock

"We would rather give you the time to finish a small thing well than rush you through a big thing. Work at the pace of the team, and use the milestones as your guide, not the wall clock."

The workshop itself now runs on milestones, not a countdown. Point teams at [Milestones](../START.md#what-you-will-do) and [The build freeze](../ORGANIZER.md#the-build-freeze) instead of quoting times. The only fixed length on event day is the judging slot (`demo_seconds` in [event.md](event.md)).

## What the mixer is not

- A place to start `1-start` or capture learner profiles. Onboarding happens fresh on event day.
- A required gate. Teams who miss the mixer can still succeed; they just spend their first half hour on setup.
- A curriculum. No slides, no quiz, no homework beyond the laptop checklist.

## After the mixer

- Note which teams still have a red laptop checklist. Pair a mentor with each at event-day open.
- If you promised a shared notes page or chat, post the link once. Do not require anyone to use it.
- Re-run `python3 hackathon/check.py` if you edited [event.md](event.md) after printing materials.
