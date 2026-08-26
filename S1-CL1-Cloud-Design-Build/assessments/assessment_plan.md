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
| **AT2** | Cloud foundation build | Individual | Portfolio (Deployment Report) + direct observation + contextual reflective questions | **ICTCLD401** |
| **AT3** | High-availability design, implementation & project closure | Individual | **A** HA Design · **B** HA Deployment Report (implementation, simulation evidence, feedback + sign-off) + contextual reflective questions | **ICTCLD502** + cross-unit closure |

The YAT case study carries through all three; KE is embedded contextually in each AT (no standalone
questioning task). **Why three not five:** folding the closure work into AT3 (its natural terminal phase) and
distributing the knowledge questions contextually keeps coverage intact while reading as appropriately sized
to QA reviewers.

### AT1 — Strategic alignment and migration plan
- **Mode / Format / Unit focus:** Individual; analyse the YAT strategic plan + ICT environment, evaluate
  gaps, propose changes, build the CBA + action plan, present to the superior; contextual reflective
  questions; ICTICT517 (+ cloud-fundamentals KE from 401/502 reframed against the YAT proposal).
- **UoC coverage:** [ICTICT517 PC 1.1–1.4, 2.1–2.4, 3.1–3.3] · [ICTICT517 PE 1–6] · [ICTICT517 KE 1–4] · [ICTICT517 FS Get the work done] · [ICTICT517 FS Interact with others] · [ICTICT517 FS Navigate the world of work] · [ICTICT517 FS Numeracy] · [ICTICT517 FS Oral Communication] · [ICTICT517 FS Reading] · [ICTICT517 FS Writing] · [ICTCLD401 PC 1.8, 4.1, 4.2] · [ICTCLD401 KE 1–4, 11] · [ICTCLD502 PC 1.2, 5.2] · [ICTCLD502 KE 1–3] · [ICTCLD502 FS Oral communication]
- **Scenario requirements:** SR-CL1-02 · SR-CL1-03 · SR-CL1-04 · SR-CL1-06

### AT2 — Cloud foundation build
- **Mode / Format / Unit focus:** Individual; build the YAT cloud foundation (IAM, VPC/subnets, EC2 + web
  app, RDS, multi-layer app with target group / load balancer / launch template / autoscaling), documented
  as a Deployment Report; contextual reflective questions; ICTCLD401.
- **UoC coverage:** [ICTCLD401 PC 1.1–1.7, 2.1–2.6, 3.1, 3.2, 4.3] · [ICTCLD401 PE 1–3] · [ICTCLD401 KE 5–10] · [ICTCLD401 FS Learning] · [ICTCLD401 FS Planning and organising] · [ICTCLD401 FS Reading] · [ICTCLD401 FS Self-management skills] · [ICTCLD401 FS Writing] · [ICTCLD502 PC 1.3, 4.1–4.3]
- **Scenario requirements:** SR-CL1-01 · SR-CL1-04 · SR-CL1-05 · SR-CL1-07

### AT3 — High-availability design, implementation & project closure
- **Mode / Format / Unit focus:** Individual; two written deliverables submitted together, with no
  presentation or observation event. **Part A — HA Design:** the HA-equivalent architecture superseding the
  AT2 baseline (SPOFs, recovery objectives, multi-AZ database, cross-AZ compute and load balancing,
  monitoring, implementation sequencing, simulation plan). **Part B — HA Deployment Report:** the
  implementation during a simulated maintenance window, the failure and resize simulation outcomes,
  availability measured across the window, any post-simulation adjustments, and engagement closure — the
  feedback record and the final sign-off block completed within the report, filed per YAT's records
  procedures. Contextual reflective questions; ICTCLD502 + cross-unit closure.
- **UoC coverage:** [ICTCLD502 PC 1.1, 2.1–2.5, 3.1–3.5, 4.1–4.6, 5.1–5.3] · [ICTCLD502 PE 1–5] · [ICTCLD502 KE 4–9] · [ICTCLD502 FS Problem solving] · [ICTCLD502 FS Reading] · [ICTCLD502 FS Self-management] · [ICTCLD401 PC 4.1, 4.3] · [ICTCLD401 FS Learning] · [ICTCLD401 FS Planning and organising] · [ICTCLD401 FS Reading] · [ICTCLD401 FS Self-management skills] · [ICTCLD401 FS Writing]
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
Closure reuses the 502 AT2 feedback/sign-off pattern, carried inside the HA Deployment Report as its
feedback record and final sign-off block, filed per YAT's records procedures.

**Author basis:** brownfield — the three units have standalone source assessments (audited; the YAT case
study is the heaviest reuse asset). New authoring is the contextual-question sets, the inter-AT bridges,
and the AT3 HA Design deliverable.

---

## 5. Coverage verification

The per-AT **UoC coverage** in §3 is the authoritative item→AT mapping; this is the rollup proof that
nothing is unassessed (across `consolidated_uoc.md`, 126 items: 106 PC/FS/PE/KE + 20 AC).

- **PC** (52) — 401 in AT2 (`1.1–3.2, 4.3`) + AT1/AT3 (`1.8, 4.1, 4.2`); 502 split AT1 (`1.2, 5.2`) / AT2
  (`1.3, 4.1–4.3`) / AT3 (`1.1, 2.1–5.3`); 517 in AT1 (`1.1–3.3`).
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
| **SR-CL1-05** | A deployable app-tier web endpoint — a placeholder page served by the app tier (provisioned by the AT3 baseline lab-pack) — sufficient to demonstrate the ALB, health checks and HA failover. The LMS application itself is **out of scope** (YAT in-house; not student-deployed in AT2/AT3) | AT2, AT3 | — |
| **SR-CL1-06** | The supplied CBA and Draft-Plan templates (ICTICT517) | AT1 | — |
| **SR-CL1-07** | The artefact thread — the AT1 action plan is the AT2 brief; the AT2-built environment is the AT3 starting state | AT2, AT3 | — |
| **SR-CL1-08** | YAT's documented change-management procedure as the formal closure process (change request, risk assessment, ICT-manager sign-off) | AT3 | — |

---

## 7. Worklist

None outstanding — all three ATs are authored, generated and approved.

---

## 8. Open questions / TBDs

None outstanding.

---

## Changelog

- **2026-05-26 (authoring):** AT1/AT2/AT3 authored on the institutional **Project Assessment template**.
  AT1 evidences its KE in the **Business Case Appendix + post-presentation Q&A** (AT2/AT3 use contextual
  reflective question sets).
