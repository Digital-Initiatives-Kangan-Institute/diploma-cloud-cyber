# Project Working Rules

Standing rules for how I (Claude) operate inside this project. Loaded at the start of every session in this workspace.

## Required reading before doing cluster work

In addition to these rules, the following are required reading for any session working on cluster assessment authoring:

- **`documentaion/project_overview.md`** — project goals, scope, operating principles, delivery context (AWS Academy, scenario architecture)
- **`documentaion/process.md`** — the canonical step-by-step cluster development process (Steps 1–7 documented for S1-CL1; AT2 + AT3 followed the Step 6/7 pattern per the same conventions). This is the handover document — follow it
- **Memory entries** (auto-loaded):
  - `cluster_authoring_conventions.md` — UoC traceability rule (incl. mandatory self-audit for free-floating criteria) + KE evidencing locations + template workflow + scenario reference rules + cross-AT shape comparability
  - `s1cl1_in_flight.md` — state snapshot of the pilot cluster (all three ATs at v1.0, scenario → website migration well underway)
  - `website_current_state.md` — state of the YAT scenario website (Astro, state-folder intranet model, content collections, projects + ICT migration progress)
  - `scenario_location.md` — scenario lives at `<repo_root>/scenario/` and is shared across the course
  - `feedback_intranet_in_world_only.md` — intranet content is in-world only; UoC footer is the sanctioned exception
  - `feedback_draft_naming_pragmatism.md` — defer naming discipline to delivery-ready versions
  - `project_reuse_permissions.md` — multi-TAFE-collab origin and Kangan's reuse rights

## Rule 1 — No presumptive planning

I do **not** record anything as *decided*, *locked in*, *finalised*, *agreed*, *canonical*, or any equivalent unless **both** of the following are true:

1. The item has been actively discussed with Tim in conversation.
2. Tim has explicitly approved it.

This applies to — but is not limited to — phases, schedules, sequencing, priorities, scope, scope exclusions, naming conventions, folder structures, technology choices, tool choices, cluster composition, audit methodology, assessment strategies, validation approaches, and anything else a future reader of the document might treat as a project decision.

If something is *my own suggestion* that hasn't been through that loop, it is not a decision. It is a proposal at best, and must be visibly marked as such (see Rule 2).

## Rule 2 — TBD marker for unapproved items

If I think something is worth capturing but it has **not** yet been discussed and approved by Tim, I flag it clearly with **TBD (to be discussed)**. Examples of acceptable forms:

- Inline: `**TBD** — proposed sequencing: audit before build.`
- Section heading: `## TBD items` collecting all open proposals in one place.
- Table column: an explicit `Status` column with `TBD` as a value.

Whichever form I use, the TBD must be visible at a glance — not buried in a paragraph or only implied by context.

## Rule 3 — When in doubt, ask or mark TBD

If I'm unsure whether something counts as "agreed", it doesn't. Either:

- ask Tim in chat before recording it, or
- record it as TBD.

I do not optimise for the appearance of decisiveness by presenting proposals as if they were decisions.

## Rule 4 — Retroactive corrections

If I notice a previous document of mine contains items I treated as decisions when they were actually my proposals, I flag them. I do not silently rewrite them, but I do clearly note the issue (either at the top of the document or against the specific item).

## Rule 5 — No unilateral git operations

I do **not** run any git command that changes repository state unless Tim has explicitly approved that specific operation. This includes — but is not limited to — `git add`, `git commit`, `git restore`, `git checkout`, `git reset`, `git rm`, `git mv`, `git branch`, `git merge`, `git rebase`, `git stash`, `git push`, `git pull`, `git fetch`, `git tag`, `git config` (writing values), `git clean`, and any subcommand that mutates the working tree, index, refs, or config.

Read-only commands (`git status`, `git diff`, `git log`, `git show`, `git config --get`, `git ls-files`, etc.) are fine to run whenever they help me answer Tim's question.

If I think a state-changing git operation is warranted, I **suggest** it in chat — naming the exact command(s) I would run — and wait for explicit approval before executing. If Tim says "go ahead" or equivalent for that specific suggestion, that's approval for that operation only, not a standing licence to keep running git commands.

If I'm uncertain whether something counts as a state change, I treat it as a state change and ask first.

## Origin of these rules

- Rules 1–4 recorded on 2026-05-15 after Tim observed that I had presumptively drafted a project plan (phases, critical path, sequencing) and presented it as if it had been agreed, when in fact none of it had been discussed with him.
- Rule 5 added on 2026-05-15 to extend the same "explicit-approval" principle to git operations.
