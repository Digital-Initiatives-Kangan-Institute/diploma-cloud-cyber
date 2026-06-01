# Cluster delivery-planning process — for LLM agents

**Audience:** an LLM agent picking up the cluster **delivery-planning** task. Not a human-facing document. Sister document to `process.md` (which covers the assessment-creation process).

**Status:** Active (2026-05-31). The process is in *The process* below; proven on S1-CL1 (Topic 1 worked end-to-end). When picking this up, continue from where the recorded work stops (remaining Topics, Steps 2 and 3), surfacing each proposed next step to Tim.

**Relationship to `process.md`:** `process.md` records how the cluster's **assessment artefacts** are created (Steps 1–7: UoC validation → consolidation → audit → assessment plan → scenario → assessor templates → student templates). This document records how a cluster's **delivery plan** is produced — the trainer-facing schedule that sequences delivery and assessment across sessions. The two processes share inputs (the consolidated UoC, the assessment plan, the scenario) but produce different outputs.

**Prerequisites you must read before acting:**
- `CLAUDE.md` (repo root) — working rules. Rule 1: nothing recorded as decided without Tim's explicit approval. Rule 5: no unilateral git operations.
- `project_overview.md` — project scope, delivery context (AWS Academy lab environments, scenario architecture), success criteria (a delivery plan is success-criterion #1 per cluster).
- `process.md` — the assessment-creation process whose outputs this plan sequences.
- **Memory entries** (auto-loaded): `s1cl1_in_flight.md` (cluster state), `cluster_authoring_conventions.md`, `scenario_location.md`.

**Working rules for documents produced (same as `process.md`):**
- Nothing recorded as a decision unless actively discussed with Tim and explicitly approved. Proposals are marked **TBD**.
- Mark produced documents as **DRAFT** while in progress.
- Do not modify anything under `original_materials/`. It is read-only reference.
- The institutional delivery-plan format-of-record is `templates/Delivery_Plan_Template_v0.1.docx`.

---

## Input state (S1-CL1)

- Cluster folder: `S1-CL1-Cloud-Design-Build/`
- `delivery/` now holds **`topic_01/` … `topic_22/`** (each with `coverage.md` + `slide_plan.md` + `source_slides/`) plus `planning/` (the retained spine, session scaffold, and deck catalogue).
- Available inputs: the three populated AT `.docx` (source of truth), `consolidated_uoc.md`, `assessments/assessment_plan.md`, the shared `scenario/` + the YAT website, and the per-UoC mapping docs under `mappings/`.
- Institutional template: `templates/Delivery_Plan_Template_v0.1.docx`.

---

## Semester 1 structure (planning context)

Provided by Tim 2026-05-31 as the planning frame for S1 cluster delivery plans. Teaching hours are **goals** — a few hours may be shifted between clusters if a plan needs it.

**Semester 1 = 18 weeks = 2 terms.**

**Delivery sequencing:**
- **CL1** — delivered first, on its own, **weeks 1–8** (8 weeks).
- **CL2 + CL3** — delivered **in parallel** after CL1 completes, **weeks 9–18** (10 weeks).

**Per-cluster hours, session model, and variance:**

| Cluster | Goal hrs | Weeks | Session model | Sessions | Delivered hrs | Variance vs goal |
|---|---:|---|---|---:|---:|---:|
| CL1 | 104 | 1–8 (8 wks) | 4 × 3h sessions/wk = 12h/wk | 32 | 96 | **+8** (under / unused) |
| CL2 | 84 | 9–18 (10 wks) | 3 × 3h sessions/wk = 9h/wk | 30 | 90 | **−6** (over) |
| CL3 | 56 | 9–18 (10 wks) | 2 × 3h sessions/wk = 6h/wk | 20 | 60 | **−4** (over) |

Variance sign convention: **+** = delivers fewer than goal (unused budget); **−** = delivers more than goal.

**Net variance across the semester:** +8 − 6 − 4 = **−2 hours** (the session model delivers ~2h over the combined 244h goal). Close enough to target.

**Student weekly load:** weeks 1–8 = 4 sessions/wk (CL1, 12h); weeks 9–18 = 5 sessions/wk (CL2's 3 + CL3's 2, 15h).

> **Current focus:** CL1 (weeks 1–8, 32 sessions). The CL2/CL3 figures are recorded for reference and are not needed for the CL1 delivery plan.

---

## Delivery strategy — teach / practice / assess

The basic approach for the cluster (per Tim 2026-05-31). Each Topic / competency area moves through a three-phase cycle:

1. **Teach** — deliver the theory: slides, class discussion, activities, and practical demonstration. A demonstration may be a **recorded video** (where one is available) rather than a live in-class demo.

2. **Practice** — students practise what they have learned through in-class activities that reinforce the learning and prepare them for assessment. Because the authored assessment tasks already cover every required UoC item, the lowest-hanging practice design is a **practice task that mirrors the assessment but set in a different scenario / under different circumstances** — close enough to build the skill, different enough that it is not rote rehearsal of the real assessment. A practice task may be split into **several exercises that, taken together, cover all parts of the related assessment**.

3. **Assess** — assess the student using the **already-authored assessment tasks** (the ATs produced via `process.md`).

**Design implication:** practice tasks are derived from the ATs (so coverage is guaranteed) but re-scenarioed away from the real assessment context. The session plan interleaves these three phases across the teaching block (S2–S28 for CL1) ahead of each assessment point.

---

## The process

**Model:** `AT → Topic → component`. A **Topic** is the delivery unit (one `topic_NN/` folder — the level you build materials for and schedule into sessions; aligns with the Delivery Plan template's "Topic and description" field). A Topic's **components** (C1, C2, …) are the things it covers, defined *inside* its `coverage.md`, derived straight from the AT — there is no separate decomposition document.

**Framing already established** (above): Semester 1 structure; the teach / practice / assess strategy; the **practice scenario** (YAT Accounting System / Ledgerline — same org, different system, added to the AT1 intranet as a peer engagement to the LMS, indistinguishable until the task is handed out); and the session bookend scaffold.

**Per-Topic folder:**
```
topic_NN/
├── coverage.md          — UoC + AT alignment (the spec) — kept
├── Topic_NN_Slides.pptx — the assembled deck — THE ARTEFACT OF RECORD
├── slide_plan.md        — the build sheet: teach + exercise slides interleaved, in deck order
│                          ([AWS Mx Sy] = copy that slide · [BESPOKE] = build from its content block)
│                          — DISPOSABLE: a working aid; delete once the deck is assembled
└── source_slides/       — only the decks this Topic OWNS (git-ignored)
```
The deck is built **once**, in PowerPoint, from the plan. Don't keep the plan synced to the deck slide-by-slide — it's about to be deleted; the deck is the source of truth.

### Step 1 — Break the AT into Topics
**Purpose:** from the assessment itself, identify the conceptual **Topics** — coherent teaching units anchored to the AT's own structure (deliverable sections, appendix/KE questions, marking criteria; the natural movements of producing the deliverable).
**Inputs:** the AT **`.docx`** (Student + Assessor) — the source of truth (see quirks).
**Method:** read both; name the Topics (e.g. Business Case = *know the tech → diagnose → build evidence → decide & plan → make the case*); place them in the cluster Topic sequence (content + assessment Topics) against the fixed bookend sessions; create a `topic_NN/` folder each.
**Result (S1-CL1):** 22 Topics across AT1/AT2/AT3 + onboarding (S1) + catch-up (S31–32).

### Step 2 — Spec each Topic (`coverage.md`)
**Purpose:** state what the Topic must cover, in **UoC** and **AT** terms — the contract its materials satisfy. **The AT sets the depth ceiling** — don't teach deeper than the assessment requires (e.g. Topic 1 = exactly Appendix 2 Q1–Q5, *recognise/explain/classify*, not build).
**Method:** list the Topic's components C1..Cn (from the AT); per component, the UoC it **teaches** (full `[UNIT SECTION num]` tags) + the **AT alignment** (which criteria / deliverable sections / appendix questions it prepares for); distinguish *taught here* vs *applied (taught earlier)*; state what's out of scope (covered elsewhere); end with a coverage checklist. **Only UoC + AT cross-references** — nothing pointing at working drafts, so the file stands alone when those are deleted.
**Result (S1-CL1):** Topics 1 & 2 done as the pattern.

### Step 3 — Build the slide plan, then the deck (reuse-first)
**Purpose:** write the build sheet (`slide_plan.md`), then assemble the single Topic deck from it. The **deck is the canonical artefact**; the plan is a working aid, deleted when the deck is done.
**Method:** walk the Topic's components top-to-bottom; for each, **teach then its exercise**, interleaved in deck order:
- **Teach slides:** pin the **AWS deck slice** that covers the component (`[AWS Mx Sy]`) and/or author **bespoke slide content** (`[BESPOKE]`, content block inline) only for gaps. The AT sets the depth ceiling.
- **Exercise slide(s):** an existing **AWS activity** where one fits (`[EX] [AWS Mx Sy]`) and/or a **bespoke exercise** (`[EX] [BESPOKE]`) on the **practice scenario**, mirroring the AT's form (builds the skill without rehearsing the real answers).
- One document for both teaching and exercise planning — no separate exercises file (it duplicated the source of truth). Flag any supporting artefact an exercise needs (e.g. a sizing sheet to publish on the website) inline in the slide plan.
- **Owns vs borrows:** copy a deck into `topic_NN/source_slides/` only in the one Topic that **owns** it; borrowers cite "deck + slides" without copying — stops the same decks bloating every Topic.

**Slide-build rules (apply as you place each slide):**
- **The plan holds briefs, not finished copy.** A `[BESPOKE]` block is the *substance* of a slide; write the actual title + bullets at build time (drafted on demand as the deck is assembled).
- **Student-facing slides stay in-world** — same rule as the intranet. No course/assessment language *on the slide*: no "AT1 / Appendix 2 / Business Case §x", and nothing that tips **which system is the assessed one** (students practise on the Accounting System; the real engagement is handed out later). Put the UoC / AT / appendix mapping in the **speaker/trainer notes** only.
- **No forward references in an exercise** — it may use only what's been taught *by that point in the deck*. If an exercise needs a service or concept from a later component, reorder, or re-cast it onto things already known (e.g. classify *described* services, not yet-unnamed AWS products).
- **Reused activities must respect the depth ceiling** — a large AWS activity often runs far deeper than the AT needs; drop it for this Topic (it belongs to a later, deeper one) rather than overshoot.

**Tempo bands** (for later session-sizing; a Topic may span >1 session): ~15–20 min teach / 40–45 activity = 3 small components per class · ~20–30 / 60–70 = 2 medium · ~30–40 / 140–150 = 1 big/practical-heavy.
**Result (S1-CL1):** Topic 1 deck built end-to-end (opener → 5 components, each *teach → exercise → takeaways* → close), reuse-first off ACF M1/M2/M3/M9 with bespoke only for the gaps; exercises run on the Accounting practice scenario. Pattern proven; the plan is now disposable.

### Still to do (S1-CL1)
Work the remaining Topics through Steps 2–3 · pin AWS deck slide-ranges · size Topics against the tempo bands and lay them onto S2–S28 (deferred until the materials reveal each Topic's real footprint).

---

## Quirks and gotchas encountered

1. **The `.docx` is the source of truth for each AT, not the `.md`.** The markdown companions were an intermediate step toward the institutional `.docx`; downstream edits may have landed only in the `.docx`. Extract from the `.docx`. (Per Tim 2026-05-31.)
2. **`docx_to_text` extraction on Windows.** The repo's `scripts/validate_uoc.py` has a reusable `docx_to_text(Path)`. Printing its output straight to the Windows console fails on non-cp1252 glyphs (e.g. `☐` ballot box); and native Python doesn't resolve bash's `/tmp`. Write the extracted text to a file under `tempfile.gettempdir()` with `encoding='utf-8'`, then read it.
3. **`.pptx` extraction + long paths.** No shared pptx helper exists; slide text lives in `ppt/slides/slideN.xml` as `<a:t>` elements (namespace `http://schemas.openxmlformats.org/drawingml/2006/main`) — iterate them per slide, ordered by N. **Two Windows traps:** (a) the AWS deck folder has deeply-nested duplicate directories that push paths past the 260-char `MAX_PATH` limit — `zipfile.ZipFile` then fails even though MSYS `find`/`cp` see the file (the `\\?\` long-path prefix did **not** reliably work); (b) native Python doesn't resolve MSYS `/tmp`. **Fix that worked:** `cp` the needed decks (via bash, which handles long paths) into a short **Windows-addressable** dir such as `/c/Users/<u>/AppData/Local/Temp/<x>`, then point Python at the `C:/Users/.../Temp/<x>` form.
