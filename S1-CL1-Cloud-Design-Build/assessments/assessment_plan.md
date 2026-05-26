# S1-CL1 Cloud Design and Build — Cluster Assessment Plan

> **STATUS: DRAFT (Claude v2).** Synthesis plan drawing from the three units' existing standalone assessments + the consolidated UoC. **No element here has been approved.** Every scenario choice, structural decision, reuse/drop call, and authoring proposal is **TBD** pending Tim's review.
>
> **v2 changes (2026-05-23):** restructured from 5 ATs to **3 ATs**. The standalone knowledge-questioning AT (previously "AT5") is gone — its content distributes across AT1–AT3 as **contextual reflective question sections** at the end of each AT, asking students to reason about their own design choices rather than answering abstract recall questions. The standalone closure AT (previously "AT4") folds into **AT3** as that AT's consolidated final deliverable. Timelines have been removed entirely — each AT is the assessment event at the end of a teaching + practice phase, with phase duration to be allocated separately.
>
> Companion documents:
> - `consolidated_uoc.md` (cluster root) — every PC/FS/PE/KE/AC verbatim + 17 groupings + ungrouped items.
> - `original_materials/DipIT_20260313/S1-CL1-Cloud-Design-Build/{ICTCLD401,ICTCLD502,ICTICT517}/` — the source standalone assessments referenced below.

---

## 1. Synthesis approach

**Goal:** one integrated cluster assessment that feels like a single project from first phase to submission, not three units stapled together. Across the cluster a single business scenario, a single stakeholder voice, and a single artefact thread.

**Proposed shape:** one continuous case-study project running across the cluster, broken into three delivery phases. Each phase is a teach → practice → assess cycle: students are taught the underlying material, given a chance to practise, and then assessed at the end of the phase. Each AT bundles the practical work + documentation + feedback/sign-off cycle + a section of contextual reflective questions on the underlying theory **as applied to the student's own design choices**. There is no separate standalone questioning AT.

```
   Phase 1                     Phase 2                       Phase 3
   Strategic alignment    →    Cloud foundation build   →    HA + project closure
       ↓                            ↓                              ↓
       AT1                          AT2                            AT3

   Each AT bundles: practical work + documentation + feedback/sign-off
   + contextual reflective questions on the underlying theory
   applied to the student's own design choices.
```

**No timelines yet.** Phase duration is deferred to delivery planning. The phase ordering is what's proposed here; the weeks-per-phase decision is separate.

**Contextual reflective questions, not abstract recall.** Knowledge-evidence is assessed by asking students to reason about their own work — *not* abstract questions divorced from the project. Example pattern: instead of "Explain the difference between SaaS, PaaS and IaaS", ask "Which parts of your proposed YAT solution use SaaS, PaaS, or IaaS? Identify which component aligns with which cloud service type, and explain why you chose that type for each part." Per QA team preference.

---

## 2. Scenario decision — recommended: **YAT College** (TBD)

The two strongest existing standalone scenarios are essentially the same shape (small org, on-prem ICT, needs cloud migration with HA):

| | YAT College *(from 517)* | Llamazonia *(from 502 AT2)* |
|---|---|---|
| Org type | Single-campus RTO with mission-critical LMS at end of life | E-commerce site (llama-themed merch) hosted in founder's aunt's basement |
| What's been authored already | Full strategic plan, ICT goals, current ICT environment description, network diagram, change-management procedure, hierarchy (superior consultant + ICT manager + MTS) | Boss interview, on-prem network diagram (one), specific availability/recovery requirements, peak-demand context |
| Student framing | Professional consultant working for MTS, advising YAT | "New cloud architect" volunteered by their boss |
| Tone | Professional, structured stakeholder relationships | Informal, jokey ("No Probllama" mugs, "Llamapalooza Friday") |

**Recommendation: use YAT throughout.** Reasoning:
- 517's strategic content is the heaviest authoring asset of the three. YAT comes with strategic plan, ICT goals, current environment description, hierarchy, change-management procedure — exactly what 517 needs. Reusing this is a substantial reduction in new-authoring work.
- 502 AT2's HA activities (terminate an instance, demonstrate failover, measure availability) are largely scenario-agnostic — they port to YAT-LMS-cloud-migration with rename-only changes.
- "Consultant advising an RTO" framing is more appropriate for a Diploma-level professional assessment than "the boss's volunteer cloud architect".
- YAT already includes a documented change-management procedure → natural fit for Group 10 (closure / sign-off).

**Cost of choosing YAT instead of Llamazonia:** 502 AT2's existing prose (Llamazonia, alpaca farm, llama socks) gets rewritten to YAT-LMS. The structural activities don't change; the scenario wrapper does.

**Open consideration (TBD):** YAT is an RTO — same industry as Tim's actual workplace. May want to confirm that's not too on-the-nose. If a substitute industry is desired, the YAT structure can be reskinned (e.g. as a community-services org or a regional manufacturer) without losing the assets.

---

## 3. Proposed cluster assessment structure

Working titles (TBD):

| Component | Working title | Format | Primary unit focus |
|---|---|---|---|
| **AT1** | Strategic alignment and migration plan | Written case-study + report + observation + contextual reflective questions | ICTICT517 |
| **AT2** | Cloud foundation build | Portfolio + direct observation + contextual reflective questions | ICTCLD401 |
| **AT3** | High-availability design, implementation, and project closure | Portfolio + direct observation + simulation + consolidated closure pack + stakeholder sign-off + contextual reflective questions | ICTCLD502 + cross-unit closure |

The case study (YAT) carries through AT1 → AT2 → AT3. No separate written/questioning task — knowledge-evidence is embedded in each AT contextually.

**Why three and not five:** auditors and QA reviewers respond to assessment count separately from the actual student workload. Five ATs (even if the substance is identical to three) reads as over-assessing; three reads as appropriately sized. Folding the closure work into AT3 (its natural terminal phase) and distributing the knowledge questions contextually across AT1–AT3 keeps coverage intact while presenting cleanly.

---

## 4. Provenance — what each AT draws from

### AT1 — Strategic alignment and migration plan

**Practical work drawn from:**
- **517 AT2** (Evaluate Strategic Plan) — Part 1 (analyse strategic plan + gap analysis + proposed changes) and Part 2 (formal report to superior). Used **largely as-is**.
- **517 AT3 Part 1** (CBA) — Cost-Benefit Analysis comparing in-house vs cloud LMS deployment over 5 years. Used **as-is**.
- **517 AT3 Part 2** (Observation: meet with superior and colleague) — preserved as a presentation/discussion with the superior + a peer; provides Foundation Skill Oral Communication evidence.
- **517 AT4** (Develop Action Plan and Obtain Approval) — Part 1 (action plan draft including prioritised schedule, standards, targets, implementation methods) and Part 2 (provide to superior for approval). Used **as-is**.
- **517 Cost Benefit Analysis template** (`original_materials/.../ICTICT517_Cost Benefit Analysis template.xlsx`) — supplied to students for CBA work.
- **517 Draft Plan template** (`ICTICT517_Draft Plan template.docx`) — supplied for action plan drafting.
- **517 Feedback Record template** (`ICTICT517_Feedback Record template.docx`) — used to capture observation feedback.

**Contextual reflective questions — source material reframed against YAT proposal:**
- 401 AT1 Q1 (industry standards), Q2 (hardware/software products), Q3 (IaaS/PaaS/SaaS), Q4 (cost models), Q13 (cloud models on-prem/private/hybrid/public)
- 502 AT1 Q1 (industry standards), Q2a/Q2b (hardware/software), Q3 (cost models / scalability)
- 517 AT1 Q1–Q3 (action plan key sections, strategic-plan analysis process, ICT product/system evaluation methods)

Each becomes a contextual question asking the student to apply the concept to their own AT1 proposal (e.g. "For each layer of your proposed YAT cloud solution, identify whether it is IaaS/PaaS/SaaS and explain why you chose that service type"; "Which cost models from your CBA apply to which YAT cloud components, and how does each scale with demand?").

**Thread to next AT:** the action plan student produces at the end of AT1 **becomes the input** to AT2. So in Phase 2 the student is implementing the plan they themselves proposed in Phase 1. This is a thread that doesn't exist in 517's standalone form.

### AT2 — Cloud foundation build

**Practical work drawn from:**
- **401 AT2 (Questioning Assessment Task Two)** — Parts 1–5 in full. This is misnamed in source (cover sheet says "Knowledge Questions" but it is a 6–8 hour AWS practical with screenshot evidence). Includes:
  - Part 1.1 (cloud solution comparison)
  - Part 1.2 (IAM setup: identify, configure policies, groups, users)
  - Part 2 (VPC + subnets + IGW + verification)
  - Part 3 (EC2 + web app deployment + storage extension)
  - Part 4 (RDS managed DB + remote connection)
  - Part 5 (multi-layer web app: target group, load balancer, launch template, autoscaling group, autoscaling policy, test, documentation, feedback)

**Contextual reflective questions — source material reframed against YAT build:**
- 401 AT1 Q6 (functions/features of services), Q7 (scaling/VM/DB differences), Q8 (storage options), Q9 (shared security responsibility), Q10 (user access protocols), Q11 (network security mechanisms), Q12 (DNS purpose — **with the Q12 placeholder bug fixed when reframing**)

Each becomes a contextual question asking the student to reason about the YAT environment they've just built (e.g. "Where does the shared-security-responsibility line fall across the components you've configured for YAT, and which responsibilities sit with the cloud vendor vs YAT ICT vs MTS vs end-users?"; "Why are your IAM groups structured the way they are — what business or workload requirement drove each group's permission set?"; "What role does DNS play in your YAT architecture, and what would fail if DNS were misconfigured?").

**What changes in the practical:**
- **Part 1.1** currently uses three abstract "Requirement #1/2/3" cloud-solution comparisons (RDS vs DynamoDB, EC2 vs S3, single EC2 vs ASG+LB+multiple). **Replace** with YAT-specific solution choices drawn from the AT1 action plan. Same skill (compare two cloud solutions for a stated requirement); different content tied to the cluster scenario.
- **Part 1.2** IAM tasks: rewrite the "software development team" framing to "YAT ICT staff + external MTS consultants + students" — same task (identify three groups with different permissions), different cast.
- **Web application target**: 401 AT2 currently uses a sample Python web app from a public GitHub repo (`ictcld401-python-app`). Either keep as the deployment payload (it's a generic web app) or substitute with a YAT-LMS stub. Keeping the existing payload is simpler; can be reframed as "a placeholder web service that will eventually be replaced by the YAT LMS once migrated."
- **Part 5.6** (Seek and respond to feedback): make the feedback request route through YAT's documented change-management procedure (already in the case study).

**Threads:** the cloud environment built in AT2 is the starting state for AT3 — AT3's HA work hardens what AT2 produced rather than starting from scratch.

### AT3 — High-availability design, implementation, and project closure

**Practical work drawn from:**
- **502 AT2 (Portfolio-Observation-Report Assessment Task)** — all five activities in full:
  - Activity 1: Identify HA requirements (from interview)
  - Activity 2: Evaluate architecture availability (review on-prem env, identify SPOFs, estimate RTO/RPO, draft email outlining issues)
  - Activity 3: Design cloud-based architecture for HA (network diagram + email to superior for feedback + revised diagram + sign-off email)
  - Activity 4: Implement cloud HA (build env, demonstrate connectivity, monitoring, simulate failure, demonstrate fault tolerance, resize without downtime)
  - Activity 5: HA database (managed multi-AZ database + RPO/RTO + vertical-scaling availability impact)

**Closure work drawn from:**
- **502 AT2 Activity 3.1b/3.1c** (boss feedback emails, sign-off request emails) — extended to cover the full cluster project not just the HA design.
- **517 AT3 Part 2** (meeting with superior + colleague) pattern — reused as the formal cluster closure meeting (a second observation event covering Foundation Skill Oral Communication).
- **517 AT4 Part 2** (provide action plan to superior for approval) pattern — repurposed as "submit the final cluster project pack to the superior for sign-off".
- **401 AT2 Part 5.5/5.6** (documentation + seek and respond to feedback) — folded into the AT3 closure pack.
- **YAT change-management procedure** (already in 517 case study) — used as the formal process the closure pack must follow (change request form, risk assessment, ICT manager sign-off, change application notification).

**Contextual reflective questions — source material reframed against YAT HA design:**
- 502 AT1 Q4a/Q4b (HA definitions, fault tolerance, SPOF, SLAs, scalability, reliability/MTTF/MTTR/MTBF, recoverability/RTO/RPO), Q5a/Q5b (testing/debugging, SPOF avoidance), Q6 (availability impact tools), Q7a/Q7b (cloud-service features, built-in vs designed FT), Q8a/Q8b (load balancing, autoscaling for availability), Q9a/Q9b (monitoring techniques and metrics)

Each becomes a contextual question against the student's own AT3 design (e.g. "What RPO and RTO does your YAT HA design achieve, and how do those compare to the on-prem environment's RPO/RTO you measured in your review?"; "For each AWS service you used in the HA design, was its fault tolerance built-in or did you have to design it in? What does that mean for cost and complexity?"; "Which CloudWatch metrics did you select for monitoring availability and why — what failure modes do they detect?").

**What changes in the practical:**
- **Wholesale rebrand** Llamazonia → YAT-LMS-cloud-migration. The "boss" voice → YAT's consultant/superior voice (already established in AT1).
- **Activity 1's "boss interview" requirements list** → replace with YAT's documented ICT goals (already in 517 case study: "Achieve 99.9% availability for critical systems by the end of 2022", "Reduce dependency on in-house server infrastructure", etc.). Requirements now consistent with what the student themselves analysed in AT1.
- **Activity 2's on-prem environment diagram** → use YAT's existing on-prem environment diagram (already in 517 case study) instead of Llamazonia's basement server.
- **Activity 4's web instance** → keep using the same web app payload deployed in AT2; the HA work hardens what AT2 built.
- **Activity 5's HA database** → ties back to the RDS instance deployed in AT2 (Part 4). The work in AT3 Activity 5 is "convert AT2's RDS into a multi-AZ HA managed database service" rather than build a new one.

**New consolidated closure deliverable:** the AT3 closure pack is a single documentation pack covering strategic context (from AT1) + foundation build (from AT2) + HA implementation (from AT3) + a new **Security Responsibilities Matrix** sub-deliverable (mapping each component of the YAT cloud architecture to its security responsibility owner: cloud vendor / YAT / MTS / students/end-users). Submitted via YAT's change-management procedure with one stakeholder feedback meeting + one final sign-off.

---

## 5. Group coverage map

For every group in `consolidated_uoc.md`, which AT covers it. This is the "audit trail" that proves the cluster covers every UoC item.

| Group | Covered in | How |
|---|---|---|
| **Group 1** — Cloud computing fundamentals | AT1 | Contextual reflective Qs: IaaS/PaaS/SaaS choices for YAT, cloud models (public/private/hybrid) for YAT, industry standards informing the migration recommendation, hardware/software product choices. Sourced from 401 AT1 Q1/Q2/Q3/Q13 + 502 AT1 Q1/Q2 reframed against the YAT proposal. |
| **Group 2** — Shared security responsibility | AT2 + AT3 | AT2 operationalises via IAM build + identifies the shared responsibility outcome (per `consolidated_uoc.md` Group 2: [ICTCLD401 PC 1.2, 1.7] · [ICTCLD401 KE 7, 9] · [ICTCLD502 PC 1.3] — all AT2). AT3 closure pack includes the Security Responsibilities Matrix as a sub-deliverable — see §6. |
| **Group 3** — IAM (identity, access, users/groups, permissions) | AT2 | 401 AT2 Part 1.2 A/B/C/D in full + contextual reflective Qs on rationale for the IAM design. |
| **Group 4** — Workload / business-needs definition | AT1 + AT2 | AT1 strategic analysis surfaces YAT's workload requirements; AT2 Part 1 explicitly defines the workload per business needs. |
| **Group 5** — Cloud cost models | AT1 | CBA in AT1 is the applied artefact. Contextual reflective Qs explore cost-model choices and scaling cost effects against the YAT proposal. |
| **Group 6** — Virtual network build | AT2 | 401 AT2 Parts 2/3/4/5 in full + contextual reflective Qs on VM/networking/storage/DB choices, DNS role, and the reasoning behind each. |
| **Group 7** — Autoscaling | AT2 + AT3 | AT2 Part 5 (configure + test). AT3 (HA-driven autoscaling design + implementation + simulation). Contextual reflective Qs on autoscaling for availability in AT3. |
| **Group 8** — High-availability architecture | AT2 (partial — implementation foundations) + AT3 (primary — HA design + simulation) | **AT2** evidences [ICTCLD502 PC 4.1] (implement architecture design in cloud environment) · [ICTCLD502 PC 4.2] (demonstrate connectivity between resources at all tiers) · [ICTCLD502 PC 4.3, baseline only] (monitor and measure availability — basic CloudWatch baseline). These are non-HA-specific implementation PCs that fit the AT2 foundation build naturally. **AT3** evidences the HA-specific items: [ICTCLD502 PC 1.1, 2.1–2.5, 3.1–3.5, 4.4–4.6, 5.1] + contextual reflective Qs on HA concepts (RTO/RPO, SPOFs, FT, monitoring metrics) applied to the YAT design. |
| **Group 9** — Strategic ICT alignment | AT1 | 517 AT2 + AT3 Part 1 + AT4 in full + contextual reflective Qs on action-plan structure and evaluation methods. |
| **Group 10** — Documentation, feedback, sign-off | AT1 + AT2 + AT3 | Each AT closes with its own document → feedback → sign-off cycle, satisfying the per-unit PCs. AT3 carries the consolidated cross-unit closure pack and final sign-off via YAT's change-management procedure. |
| **Group 11** — FS Reading | All ATs (implicit) | Implicit across all written work; explicit in AT1 (analysing strategic plan and ICT environment docs). |
| **Group 12** — FS Writing | All ATs (implicit) | Implicit in all reports/documentation; explicit in AT1 formal report and AT3 closure pack. |
| **Group 13** — FS Oral Communication | AT1 + AT3 | AT1 includes the 517 AT3 Part 2 superior/colleague meeting (observation). AT3 includes the closure sign-off meeting (observation). |
| **Group 14** — FS planning / self-mgmt / problem-solving | All ATs (implicit) | Evidenced by the student's delivery of the cluster project to schedule and quality across the cluster. |
| **Group 15** — AC: cloud platform & supporting tools | AT2 + AT3 | AWS Academy Cloud Foundations [104469] + Cloud Architecting [172221] used throughout — satisfies vendor service provider, managed DB, web browser, SSH/RDP, IDE access. |
| **Group 16** — AC: scenario information / data sources | AT1 (primary) | YAT case study supplies strategic plan, ICT environment description, organisational policies, change-management procedure. |
| **Group 17** — AC: statutory assessor requirements | All ATs (governance) | Standard institutional cover (one statement per AT). |
| **Ungrouped** | | |
| ICTICT517 FS Numeracy | AT1 | CBA in AT1 (517 AT3 Part 1) provides explicit numerical-analysis evidence. |
| ICTICT517 AC 1 (coordination site) | AT1 | YAT campus = the site where ICT needs and strategic directions are coordinated. |
| ICTICT517 AC 4 (individual superior) | AT1 + AT3 | The trainer/assessor role-plays the superior consultant role established in YAT case study across both observation meetings. |

**Verification:** every group + every ungrouped item from `consolidated_uoc.md` has an explicit row. No group is unaddressed.

---

## 6. Required modifications and additions

Things that need explicit authoring work beyond simple reuse:

### Modifications (rewrite existing content)

1. **401 AT2 Part 1.1 rescenario**: replace abstract "Requirement #1/2/3" with YAT-specific solution-comparison items. Carry forward into the action plan in AT1 so the AT1 → AT2 thread is explicit.
2. **401 AT2 Part 1.2 cast**: rewrite "software development team" framing to YAT's ICT staff + external consultants + students.
3. **502 AT2 rebrand**: Llamazonia → YAT-LMS-cloud-migration throughout (Activity 1 boss interview → YAT ICT goals; Activity 2 network diagram → YAT's on-prem LMS environment; Activity 5 database service → YAT LMS database).
4. **401 AT1 Q12 placeholder bug**: when reframing as a contextual reflective DNS question in AT2, fix the placeholder that currently repeats the shared-security-responsibility prompts from Q9.
5. **Cover-sheet template clean-up** across all source ATs: remove "Note to assessment designer" orange text, finalise time-allowed/resources-required/submission fields, fix the 401 AT1+AT2 cover-sheet header that currently has "QUESTIONINGASSSESMENT" (typo) doubled.

### Additions (new authoring)

6. **Contextual reflective question sections** at the end of each AT — author a question set for each AT that asks the student to reason about their own design choices using the underlying theory (per §4 above). Source material from 401 AT1, 502 AT1, 517 AT1, and possibly 517 AT5, but reframed contextually. Coverage must hit every KE item.
7. **AT1 → AT2 thread**: bridging instruction "the action plan you produced in AT1 will be the brief for AT2. Your AT2 implementation work must reflect the prioritised changes in your AT1 action plan." Plus an assessor check that the AT2 build matches the AT1 plan.
8. **AT2 → AT3 thread**: bridging instruction "the cloud environment you built in AT2 is the starting state for AT3. Your AT3 HA design work targets the actual environment you've already created." Plus an explicit instruction for AT3 Activity 5 to convert the AT2 RDS instance into a multi-AZ HA database (rather than build a new one).
9. **AT3 consolidated closure pack**: author the cluster closure brief — single documentation pack covering strategic context (from AT1) + foundation build (from AT2) + HA implementation (from AT3), submitted via YAT's documented change-management procedure, with one stakeholder feedback meeting + one final sign-off.
10. **Security Responsibilities Matrix** (covers Group 2): new one-page sub-deliverable inside the AT3 closure pack. Student produces a matrix mapping each component of the YAT-cloud architecture to who is responsible for which aspect of security (cloud vendor / YAT / MTS / students/end-users).
11. **PC 4.3 (save documentation per organisational policies)**: explicit instruction in AT3 that the closure pack must be filed per YAT's documented procedures (already in the case study).
12. **Cluster-level cover sheet / instructions**: a single front document that lays out the project narrative (YAT case + the three-AT structure) so students see the cluster as a coherent whole rather than three separate things.

### Things to drop / set aside

13. **517 AT3 Part 1 CBA** is currently authored against 5-year LMS comparison. Keep as-is — already targets the YAT LMS scenario.
14. **502 AT2's reference to AWS Academy Cloud Architecting Module 10 lab** ("Creating a Highly Available Environment"). Keep — useful pointer for learners; verify the lab is still accessible in current AWS Academy.
15. **517 AT5 (multiple-choice knowledge quiz)** on broader concepts (data vs info, best practices, innovation, consulting with users, gap analysis): **TBD**. Most are tangential to 517's KE 1–4 and don't readily reframe as contextual questions about the student's own work. Recommendation: drop. If any concept feels important enough to retain, reformulate as a contextual question in AT1.
16. **401 AT1 Q4** (AWS-specific cost models: pay-as-you-go / Reserved / Spot Instances): when reframing as a contextual AT1 question on YAT's CBA cost-model choices, keep the AWS specifics as the applied/vendor-specific extension rather than dropping them.

---

## 7. Open questions for review

1. **Scenario choice** — YAT throughout (recommended) vs Llamazonia throughout vs a reskinned alternative. RTO context for YAT may feel too close to Tim's workplace.
2. **517 AT5 MCQs** — drop entirely (recommended), or selectively reformulate any as contextual questions inside AT1?
3. **Web app payload in AT2** — keep the existing public Python sample (`ictcld401-python-app`) or substitute a YAT-LMS stub? Keeping is simpler.
4. ~~**AWS Academy environment**~~ — **Resolved (2026-05-23):** AWS is the preferred cloud platform; students have access to AWS Academy Cloud Foundations [104469] and AWS Academy Cloud Architecting [172221]. Both are authorised lab environments for this cluster. See `documentaion/project_overview.md` § Delivery context.
5. **Oral Communication evidence sufficiency** — two observation meetings (one in AT1 stakeholder presentation, one in AT3 closure sign-off) cover all three units' Oral Communication FS items. Is that enough, or does the cluster need a third mid-project check-in?
6. **Pre-validation review** — once the modifications/additions are drafted, run the institutional Pre-Validation Tool (from `_TEMPLATES/`) over each AT before submission.

---

## 8. Critical-path next steps (if this plan is approved)

Not committed — just the natural sequencing if the plan is taken forward.

1. Resolve open questions in §7 (Tim + stakeholder review).
2. Draft AT1 against the modifications/additions in §6 (YAT scenario already in place; bridges + contextual reflective questions to add).
3. Draft AT2 with the Part 1.1/1.2 scenario substitutions + contextual reflective questions.
4. Draft AT3 with the Llamazonia → YAT rebrand + consolidated closure pack + Security Responsibilities Matrix + contextual reflective questions.
5. Run the Pre-Validation Tool.
6. Run a UoC-coverage validator analogous to `scripts/validate_consolidated_uoc.py` but mapping every item to a specific AT line/sub-task (this is a new tool to build).
7. Complete an assessment mapping document (official template) for each UoC mapping it against the assessments.
8. Transfer all assessment tasks into official assessment templates - Assessor version.
9. Transfer all assessment tasks into official assessment templates - Student version.
10. Stakeholder review.

---

## Changelog

- **2026-05-22:** Initial draft (v1). Synthesis recommendation: YAT scenario, four-phase project + consolidated questioning AT (5 ATs total). Every element TBD.
- **2026-05-23:** Revised to v2. Restructured to 3 ATs: standalone questioning AT removed (knowledge-evidence now embedded contextually in each AT), standalone closure AT folded into AT3 as the consolidated terminal deliverable. Removed timelines pending separate delivery-time-allocation discussion. Critical-path additions from Tim (assessment mapping doc + official-template transfers, items 7–10) preserved.
- **2026-05-23 (later):** AWS confirmed as preferred cloud platform; AWS Academy Cloud Foundations [104469] + Cloud Architecting [172221] confirmed as authorised lab environments. Open Question 4 resolved. Project context captured in `documentaion/project_overview.md` § Delivery context.
- **2026-05-24:** AT1 authoring under way — Project Assessment institutional template confirmed (rather than Written Assessment) because of native Part A / Part B structure. Knowledge Evidence finalised as two locations: BC Appendix 2 (written) + post-presentation Q&A (verbal). Marking-criteria rule confirmed: bidirectional UoC traceability with full unit references; consolidation OK for highly similar requirements; AT-scope discipline (only claim what's mapped to the AT). Scenario folder moved to `<repo_root>/scenario/` for course-wide reuse. **Current AT1 state lives in memory entry `s1cl1_at1_in_flight.md`** — defer to that for "what's done and what's next" rather than maintaining duplicate state here.
- **2026-05-26:** AT3 v1.0 first draft committed (both .docx populated). Project Assessment template, two-part — Part A: HA Design (student-produced, mirrors AT2 supplied design shape with added architecture-review and implementation-sequencing sections); Part B: HA Deployment Report (mirrors AT2 Deployment Report shape with HA-specific prompts; §6 expanded for failure + resize simulation; §7 adds Feedback Record + Sign-off subsections for PCs 5.2 + 5.3). No closure ceremony / no observation event / no separate Security Responsibilities Matrix sub-deliverable — all closure-flavoured PCs evidenced in writing. AT3 scope simplified to recognise it's a post-cutover phase: LMS app already deployed by YAT IT after AT2; AT3 hardens running infrastructure in-place. Maintenance-window framing baked in (simulated Saturday late-night ~3.5h slot; brief blips acceptable). AT2 baseline CloudFormation template placeholder authored in new `scenario/assessor-resources/` folder (for assessor-only operational artefacts) — YAML content TBD. See memory `s1cl1_in_flight.md` for current state across all three ATs.
- **2026-05-25:** AT1 v1.0 complete (both .docx finalised). AT2 authoring under way — Project Assessment institutional template confirmed for AT2 also (single-task, no Part A/B split; "implementation is a project even if the deliverable is written"). AT2 deliverable shape: Deployment Report (written) with 4 appendices (build screenshots, configuration exports, test evidence, reflections); no presentation/observation event. AT2 implements a supplied baseline architecture design (in-scenario narrative: produced by MTS Senior Architecture + YAT IT while the student was on annual leave); design-production responsibility is deferred to AT3 (where ICTCLD502 PCs 3.1, 3.5, PE 1, PE 2 require it). **502 PC reassignment from AT3 to AT2:** [ICTCLD502 PC 1.3] (shared security responsibility — co-evidenced with [ICTCLD401 PC 1.2, 1.7] per Group 2), [ICTCLD502 PC 4.1] (implement architecture in cloud env), [ICTCLD502 PC 4.2] (demonstrate connectivity between tiers), [ICTCLD502 PC 4.3] (monitor availability — baseline only; HA-tuned monitoring stays AT3). Group 2 and Group 8 coverage rows in §5 updated to reflect this. AT3 still owns all 502 HA-design, HA-evaluation, HA-test, HA-closure PCs.
