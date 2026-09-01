# S1-CL3 Cloud Infrastructure Improvement — Cluster Assessment Plan

> **STATUS: DRAFT.** Turns the cluster's settled design into the spec the AT instruments are built from,
> with the coverage proof that every UoC item lands in an assessment. Conforms to the assessment-plan
> format standard (`docs/assessment-plan-format.md`).
>
> **Scenario binding:** maps to the **Semester-1 YAT** scenario — the scenario plan (to be written) is the
> cross-cluster source the `SR-*` below are validated against; current scenario sources are
> `scenario/scenario-flow.md` + `scenario/cluster-3-scenario-{assessment,practice}.md`.
>
> **What is settled** (AT model reasoned from the two units' requirements, approved 2026-06-16):
> - One integrated engagement — **a team improves a cloud system's infrastructure** — combining
>   **ICTCLD504** (the technical improve-cycle, individual) and **BSBXTW401** (leading the team, group).
> - **The seam between individual and group work is the *YAML write*, not the technical deliverable.** Of
>   design / write the IaC / deploy, **design (504 el 1–2) and deploy (504 el 3) are individual**, while
>   **writing the CloudFormation is not 504-assessed** (it is ICTCLD505, done in CL2). So the write is the
>   one job free to divide — dividing it **by component** gives BSBXTW401 its individually-accountable team
>   work without touching any individual 504 evidence.
> - **Three ATs:** **AT1 (individual) Design** (`504 el 1–2`) · **AT2 (group) Team Implementation**
>   (`401 el 1–4`, the divided write) · **AT3 (individual) Implement** (`504 el 3–4`).
> - **No business case** (neither UoC requires one; the 504 approval gate is the AT1 design presentation;
>   the cost-benefit justification is a task in the AT1 workbook).
> - **The improvement is open — there is no target architecture.** The Improvement Requirements are
>   outcomes (stable, reliable, fit for purpose, compliant), and IR-2 asks for improvements proportionate
>   to an internal, business-hours finance system. Database high availability is available to the design
>   if the student judges it warranted; leaving the database single-instance with a tested restore is
>   equally defensible if argued on cost against the recovery need. What is marked is the reasoning, not
>   which answer they reach. Scalability = elastic-capacity-on-demand (demonstrable, not forecast).
>   Parameterised CloudFormation; a light India residency slice (CERT-In + Companies-Act).

---

## 1. Integration approach

One integrated cluster assessment that reads as a single engagement on one system. **Shape:** *design the
improvement (individual) → plan and build it as a team (group) → deploy and operate it (individual)*, all on
Ledgerline. The units meet without colliding because they are evidenced on **different jobs**: 504 owns the
**design** (AT1) and **deploy-and-operate** (AT3), both individual; 401 owns the **team write** (AT2), the
only job free to divide. It is CL1 AT3's improve-loop widened (security + reliability + scalability + cost)
and run by a team.

**Approval moments (UoC-faithful):** AT1 Part B = design sign-off, *obtain sign off to proceed*
(`[ICTCLD504 PC 2.5]`, individual); AT2 Part B = team validates the combined template (a project gate, not a
504 PC); AT3 = final sign-off (`[ICTCLD504 PC 4.3]`, individual).

**Knowledge evidence — contextual, on the student's own work:** technical KE rides the AT1 design + the AT3
deployment documents; leadership KE rides the AT2 reflection. No abstract recall.

---

## 2. Scenario

**Reuse the YAT world.** By CL3, **Ledgerline** (the Accounting system) sits at a **single-AZ cloud
baseline** (on-prem in CL1 → migrated → improved in CL3). The engagement is triggered by YAT's India-campus
partnership: MTS is engaged to confirm Ledgerline is stable, reliable, fit for purpose and compliant with
the applicable Indian regulatory requirements, and to improve it across the four concerns. The student team
designs the improvement, builds it as code, and deploys it. The improvement is **open** — its shape follows
the analysis, proportionate to an internal business-hours finance system (IR-2).

**Provided framing (not the answer):** the engagement framing (MSA, Role Brief, Improvement Requirements
IR-1…7, ICT Manager Consultation Notes, Indian Regulatory Requirements) is supplied; each student's
analysis, compliance assessment and improvement design (AT1) are student-authored. The engagement then
adopts a single **agreed improvement Solution Design** (provided), which AT2 encodes into IaC and AT3
deploys.

**Vehicle (per `scenario-flow.md`):** assess on **Ledgerline** (single-AZ cloud), practise on the
**website** (no-leakage: the website is assessed in CL2). The testable scenario needs are the `SR-*` in §3 +
the register in §6.

---

## 3. Assessment structure

| AT | Working title | Mode | Format | Unit focus |
|----|---|---|---|---|
| **AT1** | Design | **Individual** | **Project Assessment** workbook — **A** analyse + design the whole improvement · **B** presentation + sign-off | **ICTCLD504** el 1–2 |
| **AT2** | Team Implementation | **Group** | **Project Assessment** workbook, one per student — planning meeting · own component · observed led meeting · reflections · team review | **BSBXTW401** el 1–4 |
| **AT3** | Implement | **Individual** | **Project Assessment** workbook — deploy the approved improvement + demonstrate all four concerns + refine + document + final sign-off | **ICTCLD504** el 3–4 |

### AT1 — Design
- **Mode / Format / Unit focus:** Individual; a guided workbook — Part A analyses the baseline and designs
  the whole improvement across all four concerns, including the compliance assessment and a cost-benefit
  justification per improvement (15 tasks); Part B is the observed presentation and sign-off (3 tasks, the
  first unmarked preparation). 3 knowledge questions. ICTCLD504 el 1–2.
- **UoC coverage:** [ICTCLD504 PC 1.1–1.6, 2.1–2.5] · [ICTCLD504 PE 1, 3] · [ICTCLD504 KE 1–6, 8, 9] · [ICTCLD504 FS Oral communication] · [ICTCLD504 FS Reading] · [ICTCLD504 FS Writing] · [ICTCLD504 AC 5]
- **Scenario requirements:** SR-CL3-03 · SR-CL3-04 · SR-CL3-05 · SR-CL3-06 · SR-CL3-10

### AT2 — Team Implementation
- **Mode / Format / Unit focus:** Group work, individual assessment — each student completes their own
  workbook. Part A is a planning-meeting agenda worked through with the team (6 tasks); Part B records the
  student's own component and their part in integration; Part C is one team meeting they lead with the
  assessor observing; Part D is three written reflections (a conflict, a coaching instance, a team issue);
  Part E is the performance review, feedback, development actions and a leadership reflection. 17 tasks and
  3 knowledge questions. BSBXTW401 el 1–4. *(The CloudFormation write is 401's vehicle — not 504-assessed,
  and its technical quality is not marked here.)*

  **The observed meeting is not the sole evidence.** BSBXTW401 ties coaching, issue resolution and conflict
  management to no meeting, and its assessment conditions require only a safe working or simulated
  environment. Those criteria are carried by the Part D reflections; the observation confirms the student
  can communicate objectives, allocate with instruction and draw the team in.
- **UoC coverage:** [BSBXTW401 PC 1.1–1.4, 2.1–2.4, 3.1–3.4, 4.1–4.4] · [BSBXTW401 PE 1–5] · [BSBXTW401 KE 1–10] · [BSBXTW401 FS Get the work done] · [BSBXTW401 FS Interact with others] · [BSBXTW401 FS Navigate the world of work]
- **Scenario requirements:** SR-CL3-01 · SR-CL3-07 · SR-CL3-08

### AT3 — Implement
- **Mode / Format / Unit focus:** Individual; a guided workbook — deploy the baseline, record the scope the
  student's own AT1 sign-off approved, apply the improvement as an update, measure against their own AT1
  metrics, then demonstrate reliability, security, scalability and cost optimisation one task each, apply
  refinements traced to test results, document the as-deployed result and a long-term strategy, obtain final
  sign-off and tear down. 13 tasks and 2 knowledge questions. ICTCLD504 el 3–4. *(An assessor reference
  combined template is the fallback so a team integration failure can't block this individual evidence.)*
- **UoC coverage:** [ICTCLD504 PC 3.1–3.4, 4.1–4.3] · [ICTCLD504 PE 2, 4, 5] · [ICTCLD504 KE 7, 10] · [ICTCLD504 FS Problem solving] · [ICTCLD504 FS Self-management] · [ICTCLD504 FS Writing]
- **Scenario requirements:** SR-CL3-01 · SR-CL3-02 · SR-CL3-06 · SR-CL3-07

**Template basis:** all three instruments are built on the institutional **Project Assessment** template
(assessor + student), with a guided workbook rendered inside it — see `docs/assessment-workbook-format.md`.
**No YAT deliverable template is used.** ICTCLD504's and BSBXTW401's assessment conditions are environment
conditions and name no document format, so `[ICTCLD504 PC 2.4]` "document and present" and
`[ICTCLD504 PC 4.1]` "document as-deployed architecture" are met by the workbook itself, and no exemplar is
required. The AT2 led-meeting observation record is a table inside the workbook, completed and signed by the
assessor in the room. No business case; no separate "Architecture Analysis" type (the analysis is the
workbook's review tasks).

---

## 4. Provenance

**Lightest cluster, heaviest reuse.** The technical workflow (analyse → design → deploy → test → document →
sign-off) is structurally CL1 AT3 + CL2, re-pointed at Ledgerline with a team-leadership overlay on the
write.

- **Reused / proven:** CL1 AT3's improve-an-existing-baseline shape + the lab-pack standard
  (`docs/lab-pack-standard.md`); the shared workbook engine and the Kangan Project Assessment instrument
  assembly; the scenario world; and the validators. Students learned IaC in CL2 (505), so the AT2 write
  reuses an existing skill (not re-assessed).
- **New (CL3-specific):** the AT2 workbook — the only group assessment in the semester, and the only one
  carrying an assessor observation record; and the deployable improved lab-pack + assessor reference
  fallback for AT3.
- **Author-fresh (accepted):** no standalone ICTCLD504 / BSBXTW401 source assessments located — CL3 is
  greenfield by design (step-3 audit not applicable).

---

## 5. Coverage verification

The per-AT **UoC coverage** in §3 is the authoritative item→AT mapping; this section is the rollup proof
that nothing is unassessed (across `consolidated_uoc.md`, 82 items).

- **PC** — 504: AT1 `1.1–2.5`, AT3 `3.1–4.3` (all 18). 401: AT2 `1.1–4.4` (all 16).
- **PE** — 504: AT1 `1, 3`, AT3 `2, 4, 5` (all 5). 401: AT2 `1–5` (all 5).
- **KE** — 504: AT1 `1–6, 8, 9`, AT3 `7, 10` (all 10). 401: AT2 `1–10` (all 10).
- **FS** — 504: AT1 Oral/Reading/Writing, AT3 Problem-solving/Self-management/Writing (all 5). 401: AT2
  Get-the-work-done/Interact-with-others/Navigate-the-world-of-work (all 3).
- **AC** — environment/legislative ACs are discharged via the `SR-*` register (§6, AC link column); the
  assessor-requirement ACs (`[ICTCLD504 AC 8]`, `[BSBXTW401 AC 2]`) are institutional, one statement per AT
  cover sheet.

**Verification:** every consolidated PC / PE / KE / FS is covered by ≥1 AT above; **401 lands entirely in
AT2; 504 entirely in AT1 (design) + AT3 (deploy/operate).** (Confirmed mechanically — `validate-cluster-
coverage` = 72/72.)

---

## 6. Scenario requirements register

The conditions the scenario must enable for these assessments. The scenario plan must satisfy every `SR-*`;
the **AC link** names the UoC Assessment Condition each environmental requirement discharges.

| SR | Condition the scenario must enable | AT(s) | AC link |
|----|---|---|---|
| **SR-CL3-01** | AWS Academy Learner Lab (us-east-1) — cloud vendor services, managed DB, console/SDK/CLI, IDE, browser, SSH/RDP; the team build + individual deploy/operate environment | AT2, AT3 | [ICTCLD504 AC 1] · [ICTCLD504 AC 2] · [ICTCLD504 AC 3] · [ICTCLD504 AC 4] · [ICTCLD504 AC 6] · [ICTCLD504 AC 7] · [BSBXTW401 AC 1] |
| **SR-CL3-02** | Deployable single-AZ Ledgerline **baseline lab-pack** (EC2+ASG / internal ALB / single-AZ RDS for SQL Server / S3 / VPC; encrypted at rest, empty DB) — the as-is system AT3 deploys then improves | AT3 | — |
| **SR-CL3-03** | Engagement framing — Master Services Agreement, Engagement Role Brief, Improvement Requirements (IR-1…7), ICT Manager Consultation Notes | AT1 | — |
| **SR-CL3-04** | Indian Regulatory Requirements (CERT-In logging + Companies-Act books-of-account) driving the compliance assessment + the India residency slice | AT1 | [ICTCLD504 AC 5] |
| **SR-CL3-05** | Current-state ICT records (baseline Solution Design, infrastructure/application specs, operational costing) carrying the Multi-AZ database limitation breadcrumb (TF-03) | AT1 | — |
| **SR-CL3-06** | A required-personnel stakeholder who role-plays the design review + sign-off (AT1 Part B) and the final sign-off (AT3) | AT1, AT3 | — |
| **SR-CL3-07** | The agreed "to be" improvement Solution Design provided to the team (AT2 build input) + an assessor reference combined template (AT3 fallback) | AT2, AT3 | — |
| **SR-CL3-08** | A student team of four (the MTS improvement team) for the group write | AT2 | [BSBXTW401 AC 1] |
| **SR-CL3-10** | The website (an object-storage-dependent system) for the contextual `[ICTCLD504 KE 6]` contrast question + the CL3 practice vehicle | AT1 | — |

---

## 7. Worklist

- **AT1** — the Design workbook (Part A analyse + design, Part B presentation and sign-off) rendered as the
  Student/Assessor instrument pair, with a derived marking guide and bidirectional UoC traceability.
- **AT2** — the Team Implementation workbook, one per student, including the assessor observation record;
  rendered as the Student/Assessor pair.
- **AT3** — the Implement workbook; the deployable improved lab-pack (combined template + assessor reference
  fallback; **proven live**, apply-as-update change-set, RDS create-only); rendered as the Student/Assessor
  pair.
- **Cluster** — this plan; `mappings/` per-unit Assessment Mapping docs (built); `consolidated_uoc.md`
  realignment to the write-is-the-seam model (the prose still describes the superseded owned-dimension /
  business-case model).

---

## 8. Open questions / TBDs

1. **Component breakdown — resolved:** four CloudFormation component stacks (**network / compute / database /
   storage**) = the AT2 write-allocation units (one per member, teams of four).
2. **Team model — resolved:** teams of 4; rotating-chair working meetings (each chairs ≥1; assessor observes
   the chair).
3. **Business case — dropped:** out of sequence; cost-benefit rides in the Solution Design.
4. **Encryption / data — resolved:** baseline encrypted at rest, lab DB empty; encryption is not an
   improvement and data migration is out of scope; every AT3 change is an in-place/additive change-set.
5. **`consolidated_uoc.md` prose — `[TBD]`:** still describes the old owned-dimension / business-case model;
   realign to write-is-the-seam (the item inventory is unaffected).
6. **Pre-validation** — downstream institutional gate (run after authoring).

---

## Changelog

- **2026-06-07 → 2026-06-21 (v1–v9):** initial integrated three-AT model through the write-is-the-seam
  restructure (v8) and the database-reliability-via-backup/DR resolution (v9). See git history for the full
  evolution (owned-dimension → owned-component → write-is-the-seam; business case dropped; Multi-AZ DB
  limitation breadcrumb TF-03). All 82 items remained placed throughout.
- **2026-06-22 (v10 — reformat to the assessment-plan standard):** restructured to
  `docs/assessment-plan-format.md` — per-AT **UoC coverage** as canonical tags (now the authoritative
  item→AT mapping, derived from the AT benchmarks), §5 recast as coverage verification, and a new **§6
  scenario requirements register** (`SR-CL3-01…10`, with AC-link discharge of the environmental conditions).
  No assessment-design change — only the plan's structure + the explicit scenario-requirement capture.
