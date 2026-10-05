# Organizer guide

A 3-hour workshop inside a college hackathon. Teams leave with a proof of concept they can demo live, a plan they approved, and a public repo. They do not leave with a startup.

The setup that has to be true before doors open is [PREREQUISITES.md](PREREQUISITES.md). Edit [hackathon/event.md](hackathon/event.md) before you print anything. Then open [hackathon/room.html](hackathon/room.html) on the projector. If you change the workshop length or the demo slot, change the times on that page too.

## The night before

- Install Git and one coding agent on the lab machines, or confirm students can sign in to their own. The agent must be able to edit this folder and run commands. Do not require a specific vendor. Confirm `git --version` works for the student account.
- Put this folder on a USB stick as a backup copy. Cloning over wifi is fine.
- Tell teams to create GitHub accounts beforehand. Account recovery during hour two ruins the demo.
- The finish line is already set in `hackathon/event.md`: hackurmom at HKUST, a 300-second live demo, public GitHub, no video, no Devpost. Paid APIs are optional.
- Skim the six skills only if you want to know what "flipped interaction" means: the agent interviews, the team decides, the agent writes the plan down after they answer.

You do not need Node unless someone insists on `npx skills add`. That path drops `hackathon/event.md`. Tell teams to open this folder instead.

## Room setup

- One laptop per team, plugged in. Extra laptops watch; they do not each run an agent on a different copy.
- Projector on `hackathon/room.html`.
- Most people here have never written code. A mentor stays at the laptop for the first few minutes, until the agent is asking them about the idea in plain words. They should not be looking at a terminal or a framework menu.
- Mentors walk the room at two points: minute 40 (one concrete thing a judge can see, or a feature list?) and minute 90 (a page open in the browser, not a terminal).

## Schedule (3 hours)

| Clock | Teams are in | Mentor looks for |
|---|---|---|
| 0:00–0:10 | `0-floor` and `1-start` | Chat is open in this folder. One driver. |
| 0:10–0:35 | `2-scope` | One sentence that is not "a platform for students." Something is cut. |
| 0:35–1:00 | `3-prd` | A judge could follow the core journey without a slide. |
| 1:00–1:20 | `4-spec` | No new accounts. Start command is local. |
| 1:20–2:35 | `5-build` | Slice 1 is on screen. `RUN.md` exists. They have committed. |
| 2:35–3:00 | `6-ship` | They rehearse once, out loud, on the demo path. Repo is public. |

Hold the line at 2:35 even if the last slice is thin. A rehearsed kernel beats an unfinished second feature.

## Judging

Three checks. No slide deck.

1. The kernel is visible in the live demo, started from `RUN.md`, within the demo slot.
2. The team can name one decision they made and one thing they cut. If they cannot, the agent did the hackathon.
3. The GitHub repo is public and contains no secrets. `devpost/learner-profile.md` and `devpost/floor.md` should not be in it.

Planning docs in `devpost/` are a plus only because they show the team made choices. Do not grade prose.

## Mentor card

Use these when a team is stuck. Do not take the keyboard except to recover a machine.

| What you see | What you say |
|---|---|
| The agent is writing the idea | "Pause. What do you want a judge to see? Tell the agent that, in your words." |
| The agent asked them to pick a language or framework | "Stop. One web page, opened in the browser. You write the code. They click it." |
| They are staring at the terminal | "Close that. The agent runs the commands. You look at the page." |
| They think they are behind because they cannot code | "You are not the coder today. Your job is the idea and the clicks." |
| Scope is a whole product | "What is the one interaction? Everything else is later." Point them at `devpost/scope.md` section **Explicitly Cut**. |
| They are blocked on an API key | "The demo path cannot need a key. Ask the agent for sample data and a flag." |
| Nothing runs at minute 90 | "Drop the next feature. Make slice 1 stay up." |
| They want the agent to write the pitch | "It can list the clicks. You say the sentences." |
| A key or `.env` is in the repo | Stop the push. Rotate the key. Do not tell them to force-push unless you are ready to walk through history with them. |
| The demo needs a network and the page will not load | Restart from `RUN.md`. If it still will not load, show the last committed slice. Do not send them off to build an offline version during judging. |

## What you should not add

- A second curriculum, a quiz, or a required peer-review count.
- Paid credits "just for the weekend." The demo will depend on them and then fail on stage.
- A rule that every teammate must commit. One driver is the design. Rotate the driver if the team wants, between skills, not mid-slice.

## After the event

Teams may keep building. This workshop ends at `6-ship`. Anything past the proof of concept is their hackathon, not this curriculum.
