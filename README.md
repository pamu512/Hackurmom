# hackurmom

A campus workshop for planning and building a small AI-assisted proof of concept before you demo it. A team finishes inside one room: one laptop, a live demo on that laptop, and no hard time limit — the room runs on milestones and a build freeze before the demo slot. Most people in the room have never written code. They decide what it does and try it in the browser. The agent writes the code.

Students: read [START.md](START.md), open this folder in any coding agent, and type **Start the hackathon**.

Organizers: read [PREREQUISITES.md](PREREQUISITES.md) and [ORGANIZER.md](ORGANIZER.md), then edit [hackathon/event.md](hackathon/event.md) before doors open — and consider running the pre-mixer in [hackathon/mixer.md](hackathon/mixer.md) the week before. Project the room board at [hackathon/room.html](hackathon/room.html).

## What a team leaves with

- A working proof of concept, not a product
- `devpost/scope.md`, `prd.md`, `spec.md`, and `checklist.md` — the plan they actually approved
- `RUN.md` — how a judge starts the demo
- A public GitHub repository
- A rehearsed live demo (300 seconds at HKUST; `demo_seconds` in `hackathon/event.md` is the slot)

A demo video and a Devpost submission are off unless `hackathon/event.md` turns them on.

## Sequence

| Step | Skill | What happens | Output |
|---|---|---|---|
| Floor | `0-floor` | Who is here, who types, what "done" means today | `devpost/floor.md` (gitignored) |
| 1 | `1-start` | Six steps, workspace check, idea and experience | `devpost/learner-profile.md` (gitignored) |
| 2 | `2-scope` | Sharpen the idea and cut it to a proof of concept | `devpost/scope.md` |
| 3 | `3-prd` | Screens, behavior, edge cases. No code talk | `devpost/prd.md` |
| 4 | `4-spec` | Technical plan the team agrees to | `devpost/spec.md` |
| 5 | `5-build` | Build in verified slices, then a short learning wrap-up | the app, `devpost/checklist.md`, `devpost/app-map.html`, `RUN.md` |
| 6 | `6-ship` | Rehearse the live demo, publish the repo, team-written turn-in | public repository |

Work through the steps in order at the team's pace; the estimate above is typical, not a rule.

Expect most teams to take about `workshop_hours` (3 by default) of active work; there is no hard time limit, and the only deadline is the build freeze before the demo slot (`build_freeze_minutes` in [hackathon/event.md](hackathon/event.md)). The agent interviews. The team supplies the idea and the decisions. A clear "looks good" approves a plan that is on screen. The team writes the project name, the demo words, and any form answers. The agent does not draft them.

One person drives the keyboard. Everyone else can answer. Starting a fresh chat between skills is fine. The `devpost/` files carry the context.

## Run it

What has to be installed and signed in beforehand is [PREREQUISITES.md](PREREQUISITES.md). Any coding agent that can read this folder, edit files, and run git will do. Cursor, Claude Code, and Codex are examples, not a requirement. Node is only for the optional upstream install below.

1. Clone or copy this folder. Build the project here so the skills and `hackathon/event.md` stay in the same workspace.
2. Open the folder in the agent and start a conversation that is allowed to edit files and run commands.
3. Type: `Start the hackathon`

`AGENTS.md` points every agent at `skills/`. `CLAUDE.md` is the same file for Claude Code. `.cursor/rules` and `.cursor/skills` are there for Cursor, and nothing else depends on them. On Windows, enable Developer Mode — or set `git config --global core.symlinks true` — before cloning, so those Cursor links survive; and run the check as `python hackathon/check.py`.

Personal names stay in `devpost/floor.md` and `devpost/learner-profile.md`, which are gitignored. That does not make the chat private. Before the repo goes public, look for secrets anyway.

## Optional: install the skills into an empty project

```
npx skills add <this-repo> --all -y
```

That copies `skills/` only. The college finish line will not apply unless `hackathon/event.md` is in the project you open. For a hackathon, open this repo instead.

## How progress is tracked

There is no separate progress file. `devpost/` is the state.

- `scope.md`, `prd.md`, `spec.md`, and `checklist.md` carry `status: draft | approved`. "Looks good" approves the plan on screen. Silence does not.
- `learner-profile.md` is experience and pacing, not progress.
- `floor.md` is who is in the room and which finish line the organizer set.
- `checklist.md` tracks slices, hands-on checks, final review, and the learning wrap-up. Checked slices alone do not mean the build is done.

Every skill reads `devpost/` first and routes from the files. Curriculum templates do not count as progress.

## Layout

```
skills/<name>/SKILL.md          the skill
skills/<name>/templates/        document templates
skills/<name>/references/       material the skill reads on demand
skills/hackathon-floor.md       college rules the skills follow when event.md exists
hackathon/event.md              organizer settings
hackathon/mixer.md              optional pre-mixer guide
hackathon/room.html             projector board
```

## License

The curriculum in this repository (the `skills/` directory, `hackathon/`, and the guides) is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE](LICENSE). A team's project files built during the workshop belong to that team.

## Check

```
python3 hackathon/check.py
```
