# Prerequisites

What has to be true before anyone types **Start the hackathon**. If one of these is missing at the door, that team loses the first half hour and probably the demo.

The curriculum does not care which model or product the team uses. It cares that the agent can work in this folder. The student app does not need an API key. The agent does need a network connection for the whole workshop. Those are different things.

## Not required

- A specific product. Cursor, Claude Code, Codex, or another coding agent are all fine. A team picks one and stays with it.
- A specific model vendor inside the project. Paid APIs are optional: use one only if the team already has a key. Nobody gets a credit card out at HKUST.
- Coding experience, or a plan-first workflow. The skills teach that.
- Node, Python, or a framework. The team picks a small local stack during spec. Python on the organizer's machine is only for `python3 hackathon/check.py`.
- An API key or a credit card for the project.
- A demo that still runs with wifi off. Nice if a team happens to have one. Do not plan around it, and do not block a team that needs the network for the live demo.
- An agent account for every teammate. One driver laptop per team.
- Devpost, Discord, a camera, or a slide deck, unless you turned that on in `hackathon/event.md`.

A chat box in a browser that cannot read this folder, edit files, and run commands cannot run the workshop.

## The room

- A block of time, about `workshop_hours` (3 by default) for a typical team, where teams are not also at a ceremony. There is no hard limit; budget for teams that use more.
- Power for every driver laptop.
- Wifi that can reach that team's agent provider and `github.com` for the whole event. The agent needs that network. The demo does not have to survive wifi being off.
- A USB stick with this folder already on it. Do not depend on cloning at the start.
- A projector or a shared screen with [hackathon/room.html](hackathon/room.html), if you have one. The workshop runs without it.
- Mentors who have read the card in [ORGANIZER.md](ORGANIZER.md). They walk the room by signal (a team stuck on early milestones while others build, or a team gone quiet), not by the clock.

If the campus already has a site license, use it. Do not buy a second vendor for this workshop, and do not require every team to use the same one.

## Each driver laptop

Do this the day before, on the account the student will actually use. An installed agent that nobody is signed in to is not ready.

1. **A coding agent with this folder as its workspace.** It must be able to read `AGENTS.md` and `skills/*/SKILL.md`, create and edit files, and run terminal commands, including git. Send one real message and confirm it can create a file. Delete that file afterward. If the account hits a usage wall on that message, it will hit it again once the workshop is underway.
2. **Git on `PATH`.** `git --version` prints a version. On Windows, install Git for Windows so the terminal the agent uses can see it. `5-build` stops if git is missing. On Windows, also enable Developer Mode (or set `git config --global core.symlinks true`) before getting this folder, so the `.cursor/skills` links survive. Without them the workshop still runs through `AGENTS.md`.
3. **A commit identity.**
   ```
   git config --global user.name
   git config --global user.email
   ```
   Both must print a value. Every build slice is committed. With no identity, the first commit fails and the checklist cannot move.
4. **This folder, and only this folder.** It must contain `skills/`, `hackathon/event.md`, and `AGENTS.md`. Do not open the student's home directory, Downloads, or another repo. Build the proof of concept here so the skills stay next to the app.
5. **A few gigabytes free**, plus a browser. The demo is whatever the team builds, almost always something they open locally.
6. **Permission for the agent to edit files and run terminal commands**, including `git commit`. If a campus policy blocks the terminal, the build skill cannot run.

Speech-to-text is optional. The scope skill asks for it because a spoken brain dump is better than a short prompt. The OS dictation shortcut is enough.

## The person who publishes

One person per team, and it can be the driver.

- A GitHub account that can create a **public** repository. Create it before the event. Password resets mid-build are how demos die.
- Push already works from this laptop. Sign in once (SSH key or HTTPS) and prove it with a push to a test repo. Do not try the first login during `6-ship`.
- They know the repo will be public, including history. `devpost/floor.md` and `devpost/learner-profile.md` are gitignored because they contain names. That does not make the agent chat private.

## Organizer, the day before

- Run the pre-mixer ([hackathon/mixer.md](hackathon/mixer.md)) if you are doing one: laptop checks, GitHub accounts and a first push, and teams saying their idea out loud once. It is the cheapest way to protect event-day momentum.
- Replace the placeholders in [hackathon/event.md](hackathon/event.md). If you change the demo length, change the judging line on [hackathon/room.html](hackathon/room.html) too. The board runs on milestones, so pacing changes need no projector edit.
- Run `python3 hackathon/check.py`. It should print `hackathon floor ok`.
- Copy the folder to the USB stick after that edit, so every machine has the same finish line.
- Do not send teams through `npx skills add`. That copies skills into an empty project and leaves `hackathon/event.md` behind. Node is only for that optional path.

## Ten-minute dry run

On one machine, in the agent the team will actually use:

1. Open this folder.
2. Type `Start the hackathon`.
3. Confirm it asks who is in the room and states the finish line from `hackathon/event.md` (live laptop demo, public GitHub). It should not send you to Devpost, and it should not require the demo to work with wifi off.
4. Stop. Delete `devpost/floor.md` if it was created, so the real team starts clean.

If that conversation does not happen, the workshop is not ready. Fix the account, the folder, or the event file before doors open.

## Only if you turned them on

Leave these off unless `hackathon/event.md` says otherwise.

| You set | You also need |
|---|---|
| `require_video: true` | A way to record the screen and a place judges can watch the file without asking for access. |
| a real `devpost_url` | A Devpost hackathon the team is registered for, and time to type their own form answers. The agent will not write them. `none` means this row does not apply. |
| a `discord_url` | A projects channel. Posting is optional and must be the team's own words. |
| `paid_apis: true` | A key every team already has. This event is `optional`, so a team without a key builds without one. |
