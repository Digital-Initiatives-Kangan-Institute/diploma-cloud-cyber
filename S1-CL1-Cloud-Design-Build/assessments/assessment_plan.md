# S1-CL1 Cloud Design and Build — Cluster Assessment Plan

> **STATUS: CONTINUOUS IMPROVEMENT
>
> **Scenario binding:** maps to the **Semester-1 YAT** scenario — the cross-cluster source the `SR-*` below
> are validated against; scenario sources are the YAT case study (from ICTICT517) + `scenario/`.
>
> **Companion document:** `consolidated_uoc.md` — every PC/FS/PE/KE/AC verbatim, with 17 groupings and the
> ungrouped items.

---

## 1. Integration approach

**Goal — an ambition, not a constraint.** We aim for one integrated cluster assessment that reads as a
single project from first phase to submission, not three units stapled together — a single business
scenario, a single stakeholder voice, a single artefact thread — **as far as that is consistent with a
good student experience.** Seamlessness is the lower priority: where making the cluster feel like one
project would make the student's experience of it more stressful, more confusing or more fragile, we
deviate. Integration is never a reason to require work that no UoC item demands.

**Shape:** one continuous case-study project across the cluster in **three delivery phases**, each a
teach → practise → assess cycle. Each AT bundles the practical work + documentation + feedback/sign-off
cycle + a section of **contextual reflective questions** on the underlying theory *as applied to the
student's own design choices*. There is no separate standalone questioning AT.

```
   Phase 1                  Phase 2                      Phase 3
   Strategic alignment  →   Cloud foundation build   →   HA + project closure
        AT1                      AT2                          AT3
```

**Approval / thread moments:** each AT closes with its own document → feedback → sign-off cycle. The
artefact thread is explicit: the **AT1 action plan becomes the AT2 brief**; the **AT2-built environment is
the AT3 starting state** (AT3 hardens it rather than starting fresh).

**Knowledge evidence — contextual, not abstract recall.** KE is assessed by asking students to reason about
their own work — e.g. not "explain IaaS/PaaS/SaaS" but "for each layer of your proposed YAT solution,
identify whether it is IaaS/PaaS/SaaS and explain why" (per QA-team preference).

---

## 2. Scenario

**YAT College** carries through AT1 → AT2 → AT3 — a single-campus RTO with a mission-critical LMS at end of
life, migrating to the cloud; the student is a **professional consultant working for MTS** advising YAT.

The scenario supplies: a full strategic plan, ICT goals, a current ICT environment description, an on-prem
network diagram, a stakeholder hierarchy (superior consultant + ICT manager + MTS), and a documented
change-management procedure used as the closure/sign-off process.

**Vehicle (per `scenario-flow.md`):** assess on the **YAT LMS cloud migration**; AWS Academy labs are the
build environment. The testable scenario needs are the `SR-*` in §3 + the register in §6.

---

## 3. Assessment structure

| AT | Working title | Mode | Format | Unit focus |
|----|---|---|---|---|
| **AT1** | Strategic alignment and migration plan | Individual | Written case-study + report + observation + contextual reflective questions | **ICTICT517** |
| **AT2** | Cloud foundation build | Individual | Guided build workbook — build tasks with evidence captured in place, connectivity + scaling tests, and contextual knowledge questions | **ICTCLD401** |
| **AT3** | High-availability design, implementation & project closure | Individual | Guided design-and-build workbook — **A** led design questions · **B** a run sheet that builds the student's own Part A answers, with simulation evidence and closure captured in place, and contextual knowledge questions | **ICTCLD502** + cross-unit closure |

The YAT case study carries through all three; KE is embedded contextually in each AT (no standalone
questioning task). **Why three not five:** folding the closure work into AT3 (its natural terminal phase) and
distributing the knowledge questions contextually keeps coverage intact while reading as appropriately sized
to QA reviewers.

### AT1 — Strategic alignment and migration plan
- **Mode / Format / Unit focus:** Individual; analyse the YAT strategic plan + ICT environment, evaluate
  gaps, propose changes, build the CBA + action plan, present to the superior; contextual reflective
  questions; ICTICT517 (+ cloud-fundamentals KE from 401/502 reframed against the YAT proposal).
- **UoC coverage:** [ICTICT517 PC 1.1–1.4, 2.1–2.4, 3.1–3.3] · [ICTICT517 PE 1–6] · [ICTICT517 KE 1–4] · [ICTICT517 FS Get the work done] · [ICTICT517 FS Interact with others] · [ICTICT517 FS Navigate the world of work] · [ICTICT517 FS Numeracy] · [ICTICT517 FS Oral Communication] · [ICTICT517 FS Reading] · [ICTICT517 FS Writing] · [ICTCLD401 PC 1.8, 4.1, 4.2] · [ICTCLD401 KE 1–4, 11] · [ICTCLD502 PC 1.2, 5.2, 5.3] · [ICTCLD502 KE 1–3] · [ICTCLD502 FS Oral communication]
- **Scenario requirements:** SR-CL1-02 · SR-CL1-03 · SR-CL1-04 · SR-CL1-06

### AT2 — Cloud foundation build
- **Mode / Format / Unit focus:** Individual; build the YAT cloud foundation (IAM, VPC/subnets, EC2 +
  launch template, target group / load balancer / autoscaling, RDS, S3, security groups, baseline
  monitoring) to the supplied design, then test it; ICTCLD401.
- **Form of the instrument — a guided build workbook, not a report.** Nearly every item AT2 carries is
  a *create / configure / deploy / test* verb, so the instrument is a sequence of build tasks rather
  than a written deliverable. Each task states the job and the settings it must be built to, and
  carries the evidence slot for it. The prose an earlier draft asked for — a build narrative
  describing what had just been built and screenshotted — evidenced nothing the screenshot did not.
  - **Settings are given; navigation is not.** The student is handed an approved design and builds to
    it, as an implementer would. What is withheld is how to find things in the console, and anything
    the unit asks them to decide.
  - **Evidence sits with the task that produces it**, never in an appendix of collected captures.
  - **Two decision points, both inline.** Only `[ICTCLD401 PC 1.1]` (*discuss and compare*) and
    `[ICTCLD401 PC 1.3]` (*select best*) carry decision verbs. They are exercised at the two tasks
    where the choice is actually made — the application-tier instance type, and the database instance
    class and storage size — each asking for the options considered, the choice, and why. Every other
    task is implement-to-spec.
  - **Tests are instrumented**: what the test demonstrates, the steps to run it, and the capture it
    produces. Every test must be runnable from the console with what the design tells the student to
    build — no VPN, no jump host, and nothing to install locally.
  - **Knowledge questions are the only sustained writing**, and carry `[ICTCLD401 FS Writing]`.
- **Sections:** build tasks (with the two inline decisions) → tests → handover and filing → knowledge
  questions.
- **UoC coverage:** [ICTCLD401 PC 1.1–1.7, 2.1–2.6, 3.1, 3.2, 4.3] · [ICTCLD401 PE 1–3] · [ICTCLD401 KE 5–10] · [ICTCLD401 FS Reading] · [ICTCLD401 FS Writing] · [ICTCLD502 PC 1.3, 4.1–4.3]
- **Scenario requirements:** SR-CL1-01 · SR-CL1-04 · SR-CL1-05 · SR-CL1-07

### AT3 — High-availability design, implementation & project closure
- **Mode / Format / Unit focus:** Individual; one guided workbook in two parts, submitted as a single
  document, with no presentation or observation event. **Part A — design:** the workbook opens with the
  current architecture supplied to the student (description, diagram, key-facts table), then leads them
  question by question to design its HA equivalent — availability-zone placement, cross-AZ compute,
  Multi-AZ database, cross-AZ load balancing, HA-tuned monitoring, the single points of failure each
  change removes, the recovery objectives the design achieves, the order the changes will be applied in,
  and the simulations that will verify them. **Part B — implementation:** a run sheet. Task 1 deploys the
  supplied baseline lab-pack to reach the starting state Part A describes; each task after it builds one
  part of the student's own design, carrying forward the settings they decided in the numbered Part A
  questions. Then the failure and resize simulations, availability measured across the maintenance
  window, any post-simulation adjustments, and engagement closure — the student hands the completed work
  to the YAT ICT Manager (played by the assessor), records the feedback and the final sign-off in place,
  and files the documentation per YAT's records procedures. Contextual reflective questions; ICTCLD502 +
  cross-unit closure.
- **Form of the instrument — a guided workbook, not two reports.** ICTCLD502 asks the student to design
  an HA architecture *and* implement it, inside one assessment. Left as two open written deliverables,
  the design work is where students stall, and a student whose design is unsound then has nothing sound
  to build. The workbook removes the stall without removing the thinking: it supplies the structure of
  the design task — the order of the questions — and nothing else.
  - **Questions are given; answers are not.** This is the inverse of AT2, and the distinction is the
    basis of AT3's evidence. AT2 hands the student an approved design and withholds console navigation.
    AT3 hands the student a sequence of questions and withholds every finding and every design decision —
    which zone, what capacity, which threshold, and above all which components are single points of
    failure. A step may say *"work through each tier below and record whether its failure would take the
    LMS down"*; it may not say *"the database is a single point of failure — fix it"*. Two performance
    criteria (`[ICTCLD502 PC 2.2]`, `[ICTCLD502 PC 3.2]`) turn on the student doing the identifying.
  - **Part B builds Part A.** Each implementation task names the Part A question whose answer it uses,
    and the student copies that answer into the task before building to it. This is what keeps
    `[ICTCLD502 PE 1]` and `[ICTCLD502 PE 2]` intact: both require the same candidate to design **and**
    implement the same infrastructure, so the design and the build cannot be separate artefacts produced
    by separate hands. It also makes the chain auditable — one thread runs from a Part A answer, through
    the Part B task, to the capture it produces.
  - **The starting state is deployed, not assumed.** Part B task 1 deploys the baseline lab-pack, putting
    every student at the architecture Part A describes regardless of what they personally built in AT2.
  - **Evidence sits with the task that produces it**, never in an appendix of collected captures.
  - **Knowledge questions are the only sustained writing**, and carry `[ICTCLD401 FS Writing]`.
- **Sections:** supplied current architecture → Part A design questions → Part B run sheet (lab-pack
  deploy → build tasks → simulations → availability measurement → adjustments) → closure and filing →
  reflections → knowledge questions.
- **UoC coverage:** [ICTCLD502 PC 1.1, 2.1–2.5, 3.1–3.5, 4.1–4.6, 5.1, 5.2] · [ICTCLD502 PE 1–5] · [ICTCLD502 KE 4–9] · [ICTCLD502 FS Problem solving] · [ICTCLD502 FS Reading] · [ICTCLD502 FS Self-management] · [ICTCLD401 PC 4.3] · [ICTCLD401 FS Learning] · [ICTCLD401 FS Planning and organising] · [ICTCLD401 FS Reading] · [ICTCLD401 FS Self-management skills] · [ICTCLD401 FS Writing]
- **Scenario requirements:** SR-CL1-01 · SR-CL1-03 · SR-CL1-04 · SR-CL1-05 · SR-CL1-07 · SR-CL1-08

---

## 4. Provenance

**AT1** draws from **517 AT2** (Evaluate Strategic Plan — analysis, gap analysis, proposed changes, formal
report to superior — largely as-is), **517 AT3 Part 1** (CBA, as-is), **517 AT3 Part 2** (observation: meet
superior + colleague → Oral Communication evidence), **517 AT4** (Develop Action Plan + obtain approval,
as-is), and the 517 CBA / Draft-Plan templates. Contextual reflective questions reframe
401 AT1 Q1–Q4/Q13 + 502 AT1 Q1–Q3 + 517 AT1 Q1–Q3 against the YAT proposal. **Thread:** the AT1 action plan
becomes the AT2 brief.

**AT2** draws from **401 AT2** (Parts 1–5 in full — IAM, VPC, EC2 + web app, RDS, multi-layer app +
autoscaling; misnamed "Knowledge Questions" in source but a 6–8h AWS practical with screenshot evidence).
Contextual reflective questions reframe 401 AT1 Q6–Q12 (the Q12 DNS placeholder bug fixed). **Changes:**
Part 1.1 abstract requirement-comparisons → YAT-specific choices from the AT1 action plan; Part 1.2 IAM cast
"software dev team" → YAT ICT staff + MTS consultants + students; web payload is a generic placeholder page
served by the app tier (LMS application installation out of scope — YAT in-house); Part 5.6 feedback routed
through YAT's change-management procedure. **Thread:** the AT2 environment is
the AT3 starting state.

**AT3** draws from **502 AT2** (all five activities — HA requirements, availability evaluation + SPOFs +
RTO/RPO, HA cloud design + feedback + sign-off, HA implementation + failure simulation + resize, multi-AZ
database), rebranded Llamazonia → YAT-LMS; Activity 1's boss-interview requirements → YAT's documented ICT
goals; Activity 2's diagram → YAT's on-prem environment; Activity 4/5 harden + convert the AT2 environment.
The five activities supply the substance; the workbook supplies the order — each activity becomes a run of
numbered questions or tasks rather than a section of a written deliverable. Closure reuses the 502 AT2
feedback/sign-off pattern, carried inside the workbook's closure section as its feedback record and final
sign-off, filed per YAT's records procedures.

**Author basis:** brownfield — the three units have standalone source assessments (audited; the YAT case
study is the heaviest reuse asset). New authoring is the contextual-question sets, the inter-AT bridges,
and AT3's design questions and run sheet.

---

## 5. Coverage verification

The per-AT **UoC coverage** in §3 is the authoritative item→AT mapping; this is the rollup proof that
nothing is unassessed (across `consolidated_uoc.md`, 126 items: 106 PC/FS/PE/KE + 20 AC).

- **PC** (52) — 401 in AT2 (`1.1–3.2, 4.3`) + AT1 (`1.8, 4.1, 4.2`) + AT3 (`4.3`); 502 split AT1 (`1.2, 5.2, 5.3`) / AT2
  (`1.3, 4.1–4.3`) / AT3 (`1.1, 2.1–5.2`); 517 in AT1 (`1.1–3.3`).
- **PE** (14) — 401 AT2 (`1–3`); 502 AT3 (`1–5`); 517 AT1 (`1–6`, the sub-bullets of the single PE).
- **KE** (24) — 401 AT1 (`1–4, 11`) + AT2 (`5–10`); 502 AT1 (`1–3`) + AT3 (`4–9`); 517 AT1 (`1–4`).
- **FS** (16) — 401 across AT2/AT3; 502 Oral→AT1, others→AT3; 517 all seven →AT1.
- **AC** (20) — discharged via the `SR-*` register (§6, AC link); the assessor-requirement ACs
  (`[ICTCLD401 AC 5]`, `[ICTCLD502 AC 9]`, `[ICTICT517 AC 6]`) are institutional, one statement per AT.

**Verification:** every consolidated PC / PE / KE / FS is covered by ≥1 AT above. (Confirmed mechanically —
`validate-cluster-coverage` = 106/106.)

---

## 6. Scenario requirements register

The conditions the scenario must enable for these assessments; the **AC link** names the UoC Assessment
Condition each environmental requirement discharges.

| SR | Condition the scenario must enable | AT(s) | AC link |
|----|---|---|---|
| **SR-CL1-01** | AWS Academy Learner Lab (us-east-1) — cloud vendor services, managed DB, IDE, browser, SSH/RDP | AT2, AT3 | [ICTCLD401 AC 1] · [ICTCLD401 AC 2] · [ICTCLD401 AC 3] · [ICTCLD502 AC 1] · [ICTCLD502 AC 2] · [ICTCLD502 AC 4] · [ICTCLD502 AC 6] · [ICTCLD502 AC 7] |
| **SR-CL1-02** | The YAT College case study — strategic plan, ICT goals, current ICT environment description, on-prem network diagram, stakeholder hierarchy | AT1, AT2, AT3 | [ICTICT517 AC 1] · [ICTICT517 AC 2] · [ICTICT517 AC 3] · [ICTICT517 AC 5] |
| **SR-CL1-03** | A superior/stakeholder (the MTS consultant / YAT ICT manager) to role-play the AT1 presentation + the AT3 closure sign-off | AT1, AT3 | [ICTICT517 AC 4] |
| **SR-CL1-04** | Requirements + data sources to determine user/business requirements (incl. user-access + business protocols) | AT1, AT2, AT3 | [ICTCLD401 AC 4] · [ICTCLD502 AC 3] · [ICTCLD502 AC 5] · [ICTCLD502 AC 8] |
| **SR-CL1-05** | A deployable app-tier web endpoint — a placeholder page served by the app tier — sufficient to demonstrate the ALB, health checks and HA failover. In **AT2** the student stands it up as part of the build, from the web-server install the supplied design specifies in the launch template; without it the target group has nothing healthy to report and neither ALB test can pass. In **AT3** it arrives pre-built in the baseline lab-pack. The LMS application itself is **out of scope** (YAT in-house; not student-deployed in AT2/AT3) | AT2, AT3 | — |
| **SR-CL1-06** | The supplied CBA and Draft-Plan templates (ICTICT517) | AT1 | — |
| **SR-CL1-07** | The artefact thread — the AT1 action plan is the AT2 brief; the AT2-built environment is the AT3 starting state | AT2, AT3 | — |
| **SR-CL1-08** | YAT's documented change-management procedure as the formal closure process (change request, risk assessment, ICT-manager sign-off) | AT3 | — |

---

## 7. Worklist

- **AT3 — re-author as the guided workbook described in §3.** The instrument, its criteria and its
  benchmark are all anchored to the two-report shape and re-anchor to numbered questions and tasks. The
  baseline lab-pack is reviewed as part of this, since Part B task 1 deploys it.

---

## 8. Open questions / TBDs

- `[TBD — needs discussion: the baseline lab-pack's specification.]` Whether AT3's starting state stays
  exactly what AT2 builds, or is re-specified to suit the run sheet. It needs a pass either way — it
  currently creates an `AlarmAlb5xx` alarm the supplied design no longer specifies.

---

## Changelog

- **2026-05-26 (authoring):** AT1/AT2/AT3 authored on the institutional **Project Assessment template**.
  AT1 evidences its KE in the **Business Case Appendix + post-presentation Q&A** (AT2/AT3 use contextual
  reflective question sets).
