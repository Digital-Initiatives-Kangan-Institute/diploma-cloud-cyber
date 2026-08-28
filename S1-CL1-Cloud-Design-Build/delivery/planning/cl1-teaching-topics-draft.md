# S1-CL1 — teaching Topic sequence (DRAFT)

**Status:** DRAFT, renumbered 2026-06-02. The cluster's **teaching content** expressed as a linear sequence of **Topics**. A **Topic** is the coherent unit we build teaching + exercise materials for, and the level we schedule into sessions. A Topic groups one or more **chunks** (the finer components), and is **not** session-bound: one Topic may span two sessions, or two small Topics may share one session. Session allocation is a later step.

**Topics vs assessments (settled 2026-06-02).** **Assessments are not Topics.** Content Topics are numbered **1–14** (the things we build teaching materials for). Assessment events and other non-teaching class sessions (report-prep, rehearsals, exams, deploy windows) are listed **in delivery order** alongside the Topics but **lettered a–i**, not numbered — they consume class time but aren't teaching units.

**Terminology (settled 2026-05-31):** `AT → Topic → chunk`. "Topic" (the delivery unit) aligns with the Delivery Plan template's *"Topic and description"* field and the AWS bespoke *"Topic 1–4"* decks. "chunk" = the finer teaching/activity component (formerly called "topic" in the decomposition drafts). The per-Topic **chunks** column below is a first cut; the authoritative per-Topic coverage (UoC + AT mapping) is worked out in each `topic_NN/coverage.md` (derived from the AT assessor doc + the per-unit mapping docs). Deck mapping in `aws-deck-catalogue-draft.md`.

**Teach / practice / assess rhythm:** content Topics teach + build a *practice* artefact in a **different scenario** than YAT (the Accounting System engagement); the lettered assessment sessions are where students produce/defend their **real** AT against YAT (the LMS engagement).

**Bookend anchors (fixed, from `cl1-delivery-sessions-draft.md`):** S1 = onboarding; S29 = AT3 baseline-deploy prep; S30 = AT3 implementation/outage window; S31–S32 = catch-up/resit. Everything else flows across S2–S28.

**TBD:** AT2/AT3 Topic groupings (Topics 6+) are proposed; chunk→Topic mapping and exact ordering not locked.

---

## Topic 0 — Onboarding *(S1, fixed)*
Orientation, systems/email/LMS access, scenario introduction. Not a content Topic.

## AT1 — Business Case *(content Topics 1–5)*

| # | Topic | chunks | Teaching source | Nature |
|---|---|---|---|---|
| 1 | **Cloud literacy** (knowledge base) | AT1 T1–T5 | AWS decks (ACF M01/M02/M04/M06–M10, ACA M02) | teach + light activity |
| 2 | **The case for change** (diagnosis) | AT1 T6–T8 | bespoke | teach + practice (BC §3–§5) |
| 3 | **Building the evidence** (evaluation) | AT1 T9–T12 | mixed (Pricing Calculator activity + bespoke) | teach + practice (BC §6–§8, App. 1) |
| 4 | **The decision & the plan** | AT1 T13–T15 | bespoke | teach + practice (BC §9–§11) |
| 5 | **Making the case** (communication) | AT1 T16–T19 | bespoke | teach + practice presentation (of the practice BC) |

**Non-Topic class sessions** *(AT1 — delivery order; assessment/prep, not counted as Topics):*
- **a — AT1 report preparation** — students produce their real Business Case (Part A) · *assessment*
- **b — AT1 presentation rehearsal** — rehearse the real board presentation
- **c — AT1 presentation assessment** — deliver Part B board presentation + Q&A + sign-off · *assessment*

*Topics 2–5 build one cumulative practice business case (the Accounting System, different scenario); Topic 1 is the shared foundation with AT2.*

## AT2 — Cloud Foundation Build *(content Topics 6–10, proposed)*

| # | Topic | chunks | Teaching source | Nature |
|---|---|---|---|---|
| 6 | **Build foundations** — working to a supplied design, console/region/evidence discipline, IAM, shared responsibility | AT2 T1,T2,T3,T11 | AWS decks (ACA M02/M03, ACF M03/M04) + bespoke (evidence discipline) | teach + practice build |
| 7 | **Network & security base** — VPC, security groups, DNS | AT2 T4,T5,T12 | AWS decks (ACF M05, ACA M07) | teach + practice build |
| 8 | **The workload tier** — EC2/EBS, ALB+ASG, RDS, S3 | AT2 T6,T7,T8,T9 | AWS decks (ACF M06–M08/M10, ACA M04/M05/M06, M10) | teach + practice build (largest Topic) |
| 9 | **Operability & justification** — CloudWatch baseline, config-decision justification, testing/validation | AT2 T10,T13,T14 | mixed (ACF M10 / ACA M10 + bespoke for the justify-against-workload + test discipline) | teach + practice build |
| 10 | **Evidencing & documenting** — evidence capture inside the run sheet, contextual KE, filing under the records policy | AT2 T16-T17, T1-T5, Q1-Q6 | bespoke | teach + practice |

**Non-Topic class sessions** *(AT2 — delivery order):*
- **d — AT2 build assessment** — build the supplied YAT design in lab · *assessment*
- **e — AT2 run-sheet completion** — finish the run sheet in place: tests, knowledge questions, and filing (no separate deliverable, no presentation) · *assessment*

*Topics 6–10 build one cumulative practice stack (the Accounting System, different workload); the real YAT LMS build is the AT2 assessment (d). Cloud literacy (Topic 1) is assumed — these Topics build the services students met conceptually there.*

## AT3 — High Availability *(content Topics 11–14, proposed)*

| # | Topic | chunks | Teaching source | Nature |
|---|---|---|---|---|
| 11 | **HA concepts** — fault tolerance/SPOFs/recovery objectives, scaling, built-in vs designed FT, LB+autoscaling for availability | AT3 T1–T4 | bespoke 502 Topics 1–3 + ACF M09 / ACA M10 | teach + light activity |
| 12 | **HA design** — baseline review & SPOFs, design the HA-equivalent, sequencing, simulation planning | AT3 T5–T8 | bespoke 502 Topic 2–3 + ACA M06/M10 | teach + practice (Part A skills) |
| 13 | **HA implementation & simulation** (practice) — implement in-place, failure sim, resize sim, availability measurement, compare/adjust, testing | AT3 T9–T14 | bespoke 502 Topic 4 + ACA M10/M11 | teach + practice build/simulate |
| 14 | **Closure & documentation** — handover and sign-off with the ICT Manager, filing, contextual KE, reflection | AT3 T25-T28, Q1-Q6, R1-R3 | bespoke | teach + practice |

**Non-Topic class sessions** *(AT3 — delivery order):*
- **f — AT3 Part A: design** — students complete the design tasks in the workbook (no separate design document) · *assessment*
- **g — AT3 baseline-deploy prep** *(S29, fixed)* — deploy the supplied AT2 baseline via CloudFormation to a known start state · *assessment prep*
- **h — AT3 Part B: implementation + simulation window** *(S30, fixed)* — in-place HA hardening + failure/resize simulations in the ~3.5h maintenance window · *assessment*
- **i — AT3 closure** — record the simulation outcomes and adjustments, hand over to the role-played ICT Manager for feedback and sign-off, and file the completed workbook — all inside the workbook · *assessment*

## Catch-up *(class sessions S31–S32, fixed)*
Spare / resit / extra time; finished students may skip. Not a content Topic.

---

## Sequence summary

`S1 onboarding →`
`[AT1 content: 1 literacy · 2 case-for-change · 3 evidence · 4 decision/plan · 5 making-the-case] → a report-prep · b rehearsal · c Part-B assessment →`
`[AT2 content: 6 foundations · 7 network/security · 8 workload · 9 operability · 10 documenting] → d build assessment · e Deployment Report →`
`[AT3 content: 11 HA concepts · 12 HA design · 13 implement/simulate · 14 closure] → f HA-Design assessment · g baseline prep (S29) · h window (S30) · i report+closure →`
`S31–32 catch-up`

**14 content Topics (1–14) + 9 assessment / non-Topic sessions (a–i)**, across the 27 teaching sessions (S2–S28) plus the fixed S29/S30 anchors.

> **Note on `chunks` column IDs:** the `AT1 T1–T5`-style identifiers are *chunk* IDs inherited from the decomposition drafts (which used a `T` prefix). They are chunks, not Topics, and can be relabelled when the explicit chunk→Topic mapping is formalised.

## Upcoming steps (not yet done)

1. **Explicit chunk→Topic mapping** — formalise/verify which chunks belong to which Topic (the `chunks` column above is the first cut).
2. **Flesh out each remaining Topic** — per-Topic `coverage.md` → `slide_plan.md` → Kangan deck (AT1 Topics 1–5 done; AT2/AT3 Topics 6–14 outstanding).
3. **Size Topics against the tempo bands** and lay them — with the lettered assessment sessions — onto S2–S28.
