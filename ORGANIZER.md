# Organizer guide

A workshop inside a college hackathon. Teams leave with a proof of concept they can demo live, a plan they approved, and a public repo. They do not leave with a startup. There is no hard time limit: teams work at their own pace toward the milestones, and the room's only deadline is the build freeze before the demo slot. For the default pacing picture (most teams finish in about `workshop_hours`), keep the estimate in [hackathon/event.md](hackathon/event.md), as an estimate, never a countdown.

The setup that has to be true before doors open is [PREREQUISITES.md](PREREQUISITES.md). Edit [hackathon/event.md](hackathon/event.md) before you print anything. Then open [hackathon/room.html](hackathon/room.html) on the projector. The board runs on milestones, so it matches any pace; if you change the demo slot length, update the judging line on that page too.

## The night before

- Run the pre-mixer ([hackathon/mixer.md](hackathon/mixer.md)) in the days before the event, if you are doing one. It moves laptop setup, GitHub accounts, and first-try friction out of event day.
- Install Git and one coding agent on the lab machines, or confirm students can sign in to their own. The agent must be able to edit this folder and run commands. Do not require a specific vendor. Confirm `git --version` works for the student account.
- Put this folder on a USB stick as a backup copy. Cloning over wifi is fine.
- Tell teams to create GitHub accounts beforehand. Account recovery mid-build ruins the demo.
- The finish line is already set in `hackathon/event.md`: hackurmom at HKUST, a 300-second live demo, public GitHub, no video, no Devpost. Paid APIs are optional.
- Skim the six skills only if you want to know what "flipped interaction" means: the agent interviews, the team decides, the agent writes the plan down after they answer.

You do not need Node unless someone insists on `npx skills add`. That path drops `hackathon/event.md`. Tell teams to open this folder instead.

## Room setup

- One laptop per team, plugged in. Extra laptops watch; they do not each run an agent on a different copy.
- Projector on `hackathon/room.html`.
- Most people here have never written code. A mentor stays at the laptop for the first few minutes, until the agent is asking them about the idea in plain words. They should not be looking at a terminal or a framework menu.
- Mentors walk the room by signal rather than by the clock: when a team is still shaping the idea while neighboring teams are already building, and whenever a team has gone quiet for a while. The sign to look for is a page open in the browser, not a terminal.

## Milestones, not a countdown

Most teams need about `workshop_hours` of active work. That number is a planning estimate for you, not a clock the room runs on. Do not post countdowns and do not hurry a team that is moving. Your lever is the milestone list below: when a team is stuck on one, help them clear it; when a team is ahead, let them polish or deepen. Do not hand them a second feature.

| # | Milestone | A team has it when… |
|---|---|---|
| 1 | Started | Chat is open in this folder. One driver. The finish line is said back. |
| 2 | Idea cut | One sentence that is not "a platform for students." Something is cut. |
| 3 | Product defined | A judge could follow the core journey without a slide. |
| 4 | Plan agreed | No new accounts. Start steps are local and written down. |
| 5 | Built | Slice 1 is on screen. `RUN.md` exists. They have committed. |
| 6 | Shipped | They rehearsed once, out loud, on the demo path. Repo is public. |

## The build freeze

`build_freeze_minutes` (default 25) before the demo slot is the one deadline you enforce: all building stops, every team rehearses from `RUN.md`, and the driver practices the demo words out loud. Announce it out loud (twice, once as a warning) and hold the line even if the last slice is thin. A rehearsed kernel beats an unfinished second feature.

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
| The agent asked them to pick a language or framework | "Stop. One web page, opened in the browser. The agent writes the code. You click it." |
| They are staring at the terminal | "Close that. The agent runs the commands. You look at the page." |
| They think they are behind because they cannot code | "You are not the coder today. Your job is the idea and the clicks." |
| Scope is a whole product | "What is the one interaction? Everything else is later." Point them at `devpost/scope.md` section **Explicitly Cut**. |
| They are blocked on an API key | "The demo path cannot need a key. Ask the agent for sample data and a flag." |
| Nothing runs at the freeze | "Drop the next feature. Make slice 1 stay up." |
| They want the agent to write the pitch | "It can list the clicks. You say the sentences." |
| A key or `.env` is in the repo | Stop the push. Rotate the key. Do not tell them to force-push unless you are ready to walk through history with them. |
| The demo needs a network and the page will not load | Restart from `RUN.md`. If it still will not load, show the last committed slice. Do not send them off to build an offline version during judging. |
| They are behind and the freeze is near | "The freeze does not care how far you got. Rehearse the kernel you have; judges reward a finished small thing over a broken big one." |

## What you should not add

- A second curriculum, a quiz, or a required peer-review count.
- Paid credits "just for the weekend." The demo will depend on them and then fail on stage.
- A rule that every teammate must commit. One driver is the design. Rotate the driver if the team wants, between skills, not mid-slice.

## After the event

Teams may keep building. This workshop ends at `6-ship`. Anything past the proof of concept is their hackathon, not this curriculum.
