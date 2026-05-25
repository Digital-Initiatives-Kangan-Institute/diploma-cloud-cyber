# AT2 — Deployment Report (Assessor) — content for the .docx

> **Status: DRAFT (Claude v1, 2026-05-25).** Companion markdown for `AT2-DeploymentReport-Assessor.docx` (institutional Project Assessment - Assessor template, single-task — no Part A/B split). Paste content into the .docx then delete this file per cluster authoring convention §3.
>
> **Convention:** *italic notes in this file like this* are authoring annotations and should not be pasted into the .docx.

---

# Project Assessment – Assessor Instructions

## Details

| Field | Value |
|---|---|
| Qualification code and title | ICT50220 Diploma of Information Technology |
| Unit code and title | ICTICT517 Match ICT needs with the strategic direction of the organisation<br>ICTCLD401 Configure cloud services<br>ICTCLD502 Design and implement highly-available cloud infrastructure |
| Assessment task title | AT2 — Cloud Foundation Build: YAT LMS Migration |
| Assessment task number | 2 of 3 |
| Due Date | (leave blank — per delivery) |
| Teacher/Assessor name | (leave blank — per delivery) |

---

## Teacher/Assessor instructions

### Assessment overview

Students are assessed on the implementation of a supplied AWS cloud architecture for the YAT LMS migration, and the production of a Deployment Report documenting the build.

The assessment is a **single-task project** delivered as one written artefact (the Deployment Report) with four populated appendices. Implementation occurs in the AWS Academy lab environment authorised for this cluster. There is **no presentation or observation event** — all assessment evidence is captured in the Deployment Report and its appendices.

This is an **open-book practical assessment**. Students may use the YAT intranet (https://www.placeholder.com.au), the AWS Pricing Calculator, AWS Academy lab environments, AWS documentation, course reference materials, and external research (which must be cited) throughout.

AT2 is the second of three assessment tasks in the S1-CL1 Cloud Design and Build cluster. It builds on AT1 (Business Case + presentation event) and feeds into AT3 (HA hardening + project closure). The student remains in the same MTS consultant role across all three.

**Reasonable adjustment** for this assessment may include extending the time allowed, varying the lab access arrangement (e.g. extended lab hours), allowing alternative screenshot-evidence formats where assistive technology requires it, or providing one-on-one verbal explanation of the supplied design where needed.

**Teacher/assessor support level:** the teacher/assessor may clarify task requirements, scenario context, or the supplied design but must not guide students to specific configuration decisions or correct knowledge-evidence answers. The eight Configuration Decisions left to the implementer (per the supplied design §14) must be made by the student.

**Submission:** the completed Deployment Report (`.docx`) with all four appendices populated is submitted via the LMS.

The assessment will not proceed if for any reason it is not safe to do so. You must advise the student of the reason for suspending the assessment, and what safety action should be taken. Advise the student of revised arrangements for the assessment when it is safe to do so.

There is a zero tolerance for plagiarism, cheating and collusion. Students will be expected to make a declaration that all work is their own prior to submission. Refer to the Training and Assessment Policy for further information.

### Task to be assessed

> All scenario materials, organisational policies, supplied design, report template, and previous-project examples for YAT College are available on the **YAT intranet** at **https://www.placeholder.com.au** — students sign in to the intranet at the start of the engagement and refer to it throughout.

Following the YAT board's approval of the action plan in the student's AT1 Business Case engagement, the student took a period of planned annual leave (in-scenario narrative). During that time MTS Senior Architecture worked with YAT ICT to translate the approved direction into a detailed technical design — the **YAT LMS Cloud Architecture — Baseline Design** — which is now the student's build specification.

The student has returned to MTS to lead the foundation-build phase of the engagement. The task has two parts that combine into a single deliverable:

1. **Implement the supplied AWS architecture** for the YAT LMS migration foundation build, in the AWS Academy lab environment authorised for this engagement.
2. **Produce a Deployment Report** documenting the build, using the YAT-provided Deployment Report template. The report covers what was built, configuration decisions made where the supplied design left them open, testing and validation outcomes, an operational handover for YAT ICT, written responses to six contextual Knowledge Evidence questions about the student's own build, and four appendices of evidence.

The Deployment Report is the **single submitted deliverable**. All build evidence (screenshots, configuration exports, test results, reflections) is captured in the report's appendices — there is no separate portfolio submission and no presentation event.

The architecture being implemented is **intentionally non-HA at this stage**. HA hardening is the next phase (AT3) and is explicitly out of scope for AT2.

**MTS scope: cloud infrastructure provisioning only.** Per the LMS Migration Role Brief on the YAT intranet (§ Scope of the MTS consulting engagement), students must **not** perform LMS application installation, MySQL data migration, cutover activities, or organisational change management as part of AT2. Those are YAT in-house IT's responsibility in-scenario. The AT2 deliverable stops at infrastructure ready for application deployment. Assessors should not award credit for application-deployment work that falls outside this scope; equally, students who include such work in their report should be redirected to focus their evidence on the in-scope infrastructure deliverables.

### Time allowed

(leave blank)

### Location

(leave blank)

### Resources required

#### Teacher/assessor supplied resources

- Access to the YAT intranet (https://www.placeholder.com.au) — supplying the supplied baseline design, the Deployment Report template, the example previous deployment report, and all other scenario materials
- AWS Academy lab access — Cloud Foundations [104469] + Cloud Architecting [172221]
- Deployment Report Benchmark (later in this document) for marking the submitted report

#### Student supplied resources

- Computer with web browser
- Word-processing software (e.g. Microsoft Word or equivalent)
- A screenshot tool

### Assessment criteria

To receive a Satisfactory outcome for this assessment the student must:

1. Achieve Satisfactory on every criterion in the **Marking Guide** below
2. Submit a completed Deployment Report (`.docx`) using the YAT-supplied template, with every section and every appendix populated

### Second attempt

If the student is deemed not satisfactory, they will be given one (1) more attempt at this assessment (or part thereof) or you can negotiate a further assessment with the student as required. The second attempt must be completed within 10 working days from the date your feedback is given.

*(institutional boilerplate — preserve as-is)*

### Assessment retention

Documentation including supporting papers/forms must be retained in accordance with the BKI Records Disposal and Transfer Procedure.

*(institutional boilerplate — preserve as-is)*

---

## Assessment Conditions & Setup Requirements

These are conditions the assessor verifies as present before marking begins. They are not student-performance criteria — they are the conditions under which the assessment can validly be conducted.

| # | Pre-condition | UoC reference(s) | Verified? |
|---|---|---|---|
| C1 | Lab environment is accessible to the student throughout the assessment — AWS Academy Cloud Foundations [104469] + AWS Academy Cloud Architecting [172221] — providing cloud vendor service provider access, cloud managed database service (RDS), IDE / console / CLI / SSH-RDP tooling, and internet/web browser access | [ICTCLD401 AC 1] · [ICTCLD401 AC 2] · [ICTCLD401 AC 3] · [ICTCLD502 AC 1] · [ICTCLD502 AC 2] · [ICTCLD502 AC 4] · [ICTCLD502 AC 6] · [ICTCLD502 AC 7] | ☐ Yes |
| C2 | The YAT scenario site / intranet is accessible to the student throughout the assessment at https://www.placeholder.com.au — supplying the baseline design, Deployment Report template, example previous deployment report, LMS application specification, organisational policies, and reference documents | [ICTCLD401 AC 4] · [ICTCLD502 AC 3] · [ICTCLD502 AC 5] · [ICTCLD502 AC 8] | ☐ Yes |

---

# Project Assessment – Marking Guide

Every marking criterion below is linked to one or more specific UoC requirements (using the full `[UNIT SECTION numbering]` notation). A bidirectional coverage table at the end (§*UoC coverage verification*) confirms that every UoC requirement AT2 claims to evidence is met by at least one criterion.

AT2 evidences a defined subset of the cluster's UoC requirements; the remaining UoC requirements are evidenced by AT1 (Business Case + presentation) and AT3 (HA design + project closure). The §*UoC coverage verification* table scopes itself to what AT2 claims.

## Assessment criteria — the Deployment Report

| # | Criterion | UoC reference(s) | Satisfactory? | Assessor comment |
|---|---|---|---|---|
| A1 | §1 Executive Summary — student produces a concise (≤ 1 page) summary of what was delivered, with explicit acknowledgement that HA hardening is deferred to AT3, and numbers/components reconcile with the body of the report | [ICTCLD401 PC 4.1] *(document and communicate work — written communication evidence)* | ☐ Yes ☐ No | |
| A2 | §4.1 + §4.2 + §4.7 Build narrative — Foundation tier (IAM, network, security) — student describes the IAM groups/users/MFA enforcement, the VPC + subnets + gateways + routing, and the security-group model; cross-references to Appendix A screenshots and Appendix B configuration exports | [ICTCLD401 PC 1.4] · [ICTCLD401 PC 1.5] · [ICTCLD401 PC 1.6] · [ICTCLD401 PC 1.7] · [ICTCLD401 PC 2.1] · [ICTCLD401 PC 2.2] · [ICTCLD502 PC 1.3] | ☐ Yes ☐ No | |
| A3 | §4.3 + §4.4 + §4.5 + §4.6 Build narrative — Workload tier (compute, load balancing, database, storage) — student describes the EC2 + ALB + ASG, the RDS managed database, and the EBS + S3 storage; cross-references to Appendix A screenshots and Appendix B configuration exports | [ICTCLD401 PC 2.3] · [ICTCLD401 PC 2.4] · [ICTCLD401 PC 2.5] · [ICTCLD502 PC 4.1] | ☐ Yes ☐ No | |
| A4 | §4.8 Build narrative — Operability (autoscaling configuration, baseline CloudWatch monitoring) — student describes the ASG scaling policy + the baseline CloudWatch alarms; identifies the shared security responsibility outcome of the build | [ICTCLD401 PC 1.2] · [ICTCLD401 PC 3.1] · [ICTCLD502 PC 4.3] *(monitoring baseline only — full availability monitoring is AT3)* | ☐ Yes ☐ No | |
| A5 | §5 Configuration Decisions — student justifies all 8 decision points (C1–C8 from the supplied design §14) with rationale tied to the YAT LMS workload (referencing the LMS Application Specification), not generic justifications | [ICTCLD401 PC 1.1] *(discuss and compare cloud computing solutions)* · [ICTCLD401 PC 1.3] *(select best cloud computing solution and service)* | ☐ Yes ☐ No | |
| A6 | §6 Testing and Validation — student ran the four required test categories (connectivity, autoscaling, database connectivity, end-to-end smoke); results documented with cross-reference to Appendix C evidence | [ICTCLD401 PC 2.6] · [ICTCLD401 PC 3.2] · [ICTCLD502 PC 4.2] | ☐ Yes ☐ No | |
| A7 | §7 Operational Handover — student documents access information for YAT ICT, names known limitations carried into AT3, and confirms filing of the report per YAT's documented records procedures | [ICTCLD401 PC 4.3] | ☐ Yes ☐ No | |
| A8 | §8 Knowledge Evidence Responses — student answers all 6 KE questions with specific reference to their own build, not generic textbook answers | [ICTCLD401 KE 5] · [ICTCLD401 KE 6] · [ICTCLD401 KE 7] · [ICTCLD401 KE 8] · [ICTCLD401 KE 9] · [ICTCLD401 KE 10] | ☐ Yes ☐ No | |
| A9 | Appendix A Build Evidence — all 17 named screenshots (A1–A17) present, correct AWS region visible, named items visible per the template's requirements | [ICTCLD401 PE 1] · [ICTCLD401 PE 2] *(the built artefacts are the evidence)* | ☐ Yes ☐ No | |
| A10 | Appendix B Configuration Exports — all 7 named exports (B1–B7) present, exported from the actual deployed environment (consistent with the screenshots in Appendix A) | [ICTCLD401 PE 2] *(deeper configuration evidence)* | ☐ Yes ☐ No | |
| A11 | Appendix C Test Evidence — test outcomes documented with supporting evidence; outcomes consistent with §6 narrative | [ICTCLD401 PE 3] · [ICTCLD502 PC 4.2] *(connectivity evidence)* · [ICTCLD502 PC 4.3] *(baseline monitoring evidence)* | ☐ Yes ☐ No | |
| A12 | Appendix D Reflections — two honest reflective responses present, both specific to the student's own build experience | [ICTCLD401 FS Learning] · [ICTCLD401 FS Planning and organising] · [ICTCLD401 FS Self-management skills] | ☐ Yes ☐ No | |
| A13 | Document quality — Deployment Report uses plain English, appropriate technical vocabulary, structure, formatting, and depth relevant to a professional consulting deliverable for an RTO client; student has correctly interpreted the supplied design and other complex technical documentation in the build | [ICTCLD401 FS Writing] · [ICTCLD401 FS Reading] · [ICTCLD502 FS Reading] | ☐ Yes ☐ No | |

## UoC coverage verification (reverse map)

This table closes the loop on bidirectional traceability: every UoC requirement AT2 claims to evidence is named below with the marking criterion (or criteria) that evidence it. No UoC requirement claimed by AT2 is left without a criterion.

### ICTCLD401 — Configure cloud services (AT2-evidenced items)

| UoC item | Evidenced by criterion(ia) |
|---|---|
| PC 1.1 — Discuss and compare different cloud computing solutions, models and services | A5 (justifications in §5 Configuration Decisions implicitly compare options) |
| PC 1.2 — Identify impact of shared security responsibility models | A4 |
| PC 1.3 — Select best cloud computing solution and service | A5 |
| PC 1.4 — Access account on cloud platform | A2 |
| PC 1.5 — Identify user access protocols and policies | A2 |
| PC 1.6 — Configure access functions within cloud environment | A2 |
| PC 1.7 — Identify and assign security responsibilities | A2 |
| PC 2.1 — Create users and groups | A2 |
| PC 2.2 — Create virtual multi-tier network | A2 |
| PC 2.3 — Create virtual machine | A3 |
| PC 2.4 — Define, add and expand storage | A3 |
| PC 2.5 — Deploy a managed database | A3 |
| PC 2.6 — Test external network access | A6 |
| PC 3.1 — Configure and apply autoscaling | A4 |
| PC 3.2 — Test automatic scaling | A6 |
| PC 4.3 — Save and store user documentation per organisational policies | A7 |
| PE 1 — Build at least one simple virtual network capable of supporting a workload | A9 |
| PE 2 — Configure compute, storage, database and autoscaling resources within virtual network | A9 · A10 |
| PE 3 — Conduct simple tests to confirm access to resources | A11 |
| KE 5 — VM/networking/scaling features (VM sizing, load balancing, autoscaling, monitoring, storage backups, virtual networks/traffic routing) | A8 (Q1) |
| KE 6 — Vertical vs horizontal scaling; VM vs physical; RDBMS/DW/NoSQL; self-hosted vs managed vs cloud-native DB; storage options (block/object/archive/network filesystems) | A8 (Q2) |
| KE 7 — User, business and vendor responsibilities according to shared security responsibility models | A8 (Q3) |
| KE 8 — User access protocols and policies according to organisation hierarchy and job function | A8 (Q4) |
| KE 9 — Security policies, protocols and mechanisms as they relate to cloud (network traffic limits + security responsibilities per work function/user access) | A8 (Q5) |
| KE 10 — Purpose of DNS for connecting remote servers when web browsing | A8 (Q6) |
| FS Reading | A13 |
| FS Writing | A13 |
| FS Learning | A12 |
| FS Planning and organising | A12 |
| FS Self-management skills | A12 |
| AC 1 — Cloud vendor service provider | C1 (pre-condition) |
| AC 2 — Cloud managed database service | C1 (pre-condition) |
| AC 3 — Internet and web browser | C1 (pre-condition) |
| AC 4 — Data to gather information from to determine output and user requirements | C2 (pre-condition) |

*(Note: 401 PCs not listed above (PC 1.8, PC 4.1, PC 4.2) are evidenced in AT1. 401 KEs not listed (KE 1, 2, 3, 4, 11) are evidenced in AT1 Appendix 2.)*

### ICTCLD502 — Design and implement highly-available cloud infrastructure (AT2-evidenced items only)

| UoC item | Evidenced by criterion(ia) |
|---|---|
| PC 1.3 — Identify level of shared security responsibility models according to business needs | A2 (co-evidenced with [ICTCLD401 PC 1.2] · [ICTCLD401 PC 1.7] via Group 2 of consolidated UoC) |
| PC 4.1 — Implement architecture design in cloud environment | A3 |
| PC 4.2 — Demonstrate connectivity between resources at all tiers | A6 · A11 |
| PC 4.3 — Monitor and measure availability of resources | A4 · A11 *(baseline monitoring only — HA-tuned monitoring is AT3)* |
| FS Reading | A13 |
| AC 1 — Cloud vendor service provider | C1 (pre-condition) |
| AC 2 — Cloud managed database service | C1 (pre-condition) |
| AC 3 — Information and data sources required to design and implement cloud infrastructure | C2 (pre-condition) |
| AC 4 — Integrated development environment (IDE) | C1 (pre-condition — AWS Console + CLI counts as IDE) |
| AC 5 — Specific requirements + industry standards + organisational procedures + legislative requirements + business and functionality requirements | C2 (pre-condition — supplied via YAT intranet) |
| AC 6 — Internet and web browser | C1 (pre-condition) |
| AC 7 — Secure shell (SSH) or remote desktop protocol (RDP) client | C1 (pre-condition — RDP for Windows EC2 instances) |
| AC 8 — Data to gather information from to determine output and user requirements | C2 (pre-condition) |

*(Note: 502 PCs not listed above (PC 1.1, 1.2, 2.1–2.5, 3.1–3.5, 4.4–4.6, 5.1, 5.2, 5.3) are evidenced in AT1 (PC 1.2, 5.2) or AT3 (the rest). 502 KEs not listed (KE 1, 2, 3) are evidenced in AT1 Appendix 2; KEs 4–9 are evidenced in AT3.)*

## Notes on rubric application

- **All 13 criteria must be Satisfactory** for the overall AT2 result to be Satisfactory. A single criterion marked NYS results in NYS for the assessment and may require resubmission (see institutional Second attempt clause above).
- **Pre-conditions (C1, C2) must be verified** before marking begins. A "No" on any pre-condition means the assessment cannot validly proceed and the situation must be resolved with the student before re-attempt.
- **Assessor comments are expected for any NYS** to support the student's resubmission.
- **Critical criteria** where NYS forces overall NYS regardless of other strengths: A3 (workload tier build narrative), A5 (Configuration Decisions), A6 (Testing and Validation), A8 (KE Responses), A9 (Appendix A Build Evidence). A student cannot pass AT2 by writing a polished report about a build that wasn't actually completed or wasn't tested.
- **Supporting criteria** where NYS may be balanced against compensating evidence elsewhere in the report: A1 (Executive Summary), A12 (Reflections — only if the rest of the report is otherwise strong).
- **Note on report sections §2 (Engagement Context) and §3 (Scope of Deployment):** these are required sections of the template (students must complete them for a coherent report) but they are **not separately graded criteria** — they don't trace to specific UoC items. Their absence or weakness manifests in A13 (Document Quality) rather than as a dedicated criterion.

---

# Instructions to Student

*This section mirrors the detailed task instructions in the student docx. The assessor sees the same task content the student is given, in the same form, so the assessor knows what students have been told.*

## The engagement — picking up where AT1 left off

YAT College is migrating their mission-critical Learning Management System (LMS) from on-premises to AWS. You are an **MTS Consultant** on this engagement, reporting to **Pat Lin** (MTS Senior Consultant). **Sam Walker** (YAT ICT Manager) is your primary YAT-side stakeholder.

At the end of the AT1 engagement, the YAT board approved your action plan. You then took planned annual leave. During that period, MTS Senior Architecture worked with YAT ICT to translate the approved direction into a detailed cloud architecture design — the **YAT LMS Cloud Architecture — Baseline Design**, available from the *Engagement Documents* section of the YAT intranet.

You have returned to MTS, and your assignment is the **foundation build phase** of the engagement: stand up the supplied architecture in the AWS Academy lab environment, then hand it over to YAT IT with a Deployment Report.

## Scope of your work in this assessment

Per the **LMS Migration Role Brief** on the YAT intranet (§ Scope of the MTS consulting engagement), your assessment scope is **cloud infrastructure provisioning only**. The following activities are **YAT in-house IT's responsibility**, not yours:

- LMS application installation on the AWS infrastructure you build
- Migration of the MySQL database from on-prem to the AWS RDS instance
- Cutover from legacy to new (DNS switch, parallel running, decommissioning)
- Organisational change management around the cutover (CAB process, end-user communications, training)
- Ongoing application support post-handover

Your AT2 deliverable stops at **infrastructure ready for application deployment**. You hand the infrastructure over to YAT IT with the Deployment Report — they take it from there. Do not install the LMS application, migrate production data, or perform cutover activities as part of this assessment.

## Part 1 — Build the supplied design

Using AWS Academy, implement the architecture exactly as specified in the supplied design. The design is opinionated where it matters (region, network topology, IAM model, service categories, security controls, tagging) and intentionally silent where you must demonstrate professional judgement. The supplied design's §14 *Configuration decisions left to the implementer* enumerates the eight decisions you must make and justify (C1 through C8).

For each of those configuration decisions, make a deliberate, justified choice based on the YAT LMS workload as described in the LMS Application Specification on the YAT intranet. You will document the choice and rationale in §5 of your Deployment Report.

Important constraints on the build:

- **The deployment is single-AZ and non-HA by design.** HA hardening is the next phase (AT3). Do not pre-empt that work.
- **All security, encryption, tagging, and naming conventions in the supplied design are mandatory.** These are non-negotiable.
- **Take the screenshots listed in Appendix A of the Deployment Report template *as you go*, not at the end.**
- **Test outcomes (§6 of the template) require you to actually run the tests** — do not fabricate.

## Part 2 — Produce the Deployment Report

Download the **Deployment Report template** from the YAT intranet's *Templates* section. Populate every section and every appendix. The template provides explicit prompts in each section — follow them.

**Before starting your own report**, review at least one **Example previous Deployment Report** from the YAT intranet's *Document Archive* section.

---

## Tips for success

- **Review the example past Deployment Report first** before starting your own work
- **Read the supplied design end-to-end before building**
- **Screenshots as you go, not at the end** — this is the single most common failure mode
- **Justify every configuration decision against the YAT workload** — generic justifications are not credible
- **Don't paper over the eight Configuration Decisions** — §5 is one of the most-scrutinised sections
- **The Knowledge Evidence responses (§8) are about your own build** — every answer should reference specific sections, components, or decisions in your report
- **The reflections in Appendix D are honest, not promotional**
- **File the report per YAT's records procedures** (§7.4 of the template) — this is part of what's being assessed

---

# Deployment Report Benchmark

*Per-section marking guidance for the assessor. What "Satisfactory" looks like for each section of the report. Model answers for the contextual KE questions. Common deductions.*

## 1. Marking framework

- The Deployment Report is marked **Satisfactory / Not Yet Satisfactory** as a whole, with per-section judgements feeding the overall.
- Each report section evidences specific UoC items (see the section-level UoC mapping in the Marking Guide above).
- A section is **Satisfactory** when the UoC items it evidences are demonstrated through the student's content.
- Students may arrive at different specific configuration choices (e.g. `m6i.large` vs `m5.large`, scaling thresholds 60% vs 70%) — that's acceptable as long as their justifications are internally consistent and tied to the YAT workload.
- **Critical sections** (where NYS forces overall NYS regardless of strengths elsewhere): §4 Build Narrative (workload tier — criterion A3), §5 Configuration Decisions (A5), §6 Testing and Validation (A6), §8 Knowledge Evidence (A8), Appendix A Build Evidence (A9).
- **Supporting sections** (where NYS may be balanced against compensating evidence elsewhere): §1 Executive Summary (A1), Appendix D Reflections (A12).
- **§2 Engagement Context + §3 Scope of Deployment** are required template sections but not separately graded — they support the rest of the report and any weakness shows up under A13 (Document Quality).

---

## 2. Marking §1 Executive Summary

**UoC evidenced:** [ICTCLD401 PC 4.1] *(document and communicate work — written executive-level communication evidence)*.

**Satisfactory looks like:**
- One page or less
- Names what was delivered (the AWS foundation for the LMS)
- Region + AZ stated
- Top 2–3 highlights of the build called out
- Explicit acknowledgement that HA is deferred to AT3
- Confirmation the engagement is ready for the next phase

**NYS:**
- Missing or absent
- Reads as a full report rather than a summary
- Does not reconcile with the body (e.g. mentions multi-AZ when the body shows single-AZ)

---

## 3. Marking §2 Engagement Context

**UoC evidenced:** scoping context (supports the rest of the report).

**Satisfactory looks like:**
- References the AT1 Business Case engagement and its board-approved action plan
- Names the supplied baseline design as the build specification (and notes its approval status)
- Names Pat Lin and Sam Walker as the in-scenario stakeholders
- Frames the AT2 work as the foundation-build phase

**NYS:** vague about the prior work, or treats AT2 as a greenfield engagement disconnected from AT1.

---

## 4. Marking §3 Scope of Deployment

**Satisfactory looks like:**
- Clear list of what is in this build (IAM, network, compute, ALB, DB, storage, autoscaling, baseline monitoring)
- Clear list of what is deferred to AT3 (Multi-AZ DB, cross-AZ resilience, failure simulation, DR, cross-Region backup, HA-tuned monitoring)

**NYS:** scope unclear; HA elements implicitly assumed to be in this phase.

---

## 5. Marking §4 Build Narrative

**UoC evidenced:** [ICTCLD401 PC 1.2, 1.4, 1.5, 1.6, 1.7, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1] · [ICTCLD502 PC 1.3, 4.1, 4.3 — partial].

**Satisfactory looks like, per sub-section:**

### 5.1 §4.1 IAM (criterion A4)
- IAM groups named match the supplied design (or rationale provided for any addition)
- MFA enforcement evidenced
- EC2 instance role / `Application-Service` permissions described
- Cross-references Screenshot A1, A2, A3 + Configuration export B1, B2

### 5.2 §4.2 Network (criterion A4)
- VPC CIDR + subnet layout matches supplied design
- Internet Gateway + NAT Gateway documented
- Route table behaviour documented
- Cross-references A4, A5, A6, A7 + B3

### 5.3 §4.3 + §4.4 Compute + ALB (criterion A5)
- EC2 instance type stated (per C1 decision)
- ASG configuration stated (min/desired/max + scaling policy threshold per C4)
- ALB configuration + target group health check
- Cross-references A9, A13, A14 + B4, B5

### 5.4 §4.5 Database (criterion A5)
- RDS instance class stated (per C2)
- MySQL engine version (per C7)
- Single-AZ deployment confirmed
- Encryption at rest confirmed
- Cross-references A12 + B6

### 5.5 §4.6 Storage (criterion A5)
- EBS volumes (root + data) sizing documented
- S3 buckets (attachments + backups) with block-public-access confirmed
- Cross-references A10, A11 + B7

### 5.6 §4.7 Security (criterion A4)
- Three-tier security group model documented
- Encryption-in-transit between tiers documented
- Shared responsibility table from §9.4 of the supplied design referenced
- Cross-references A8 + B2

### 5.7 §4.8 Monitoring baseline (criterion A6)
- Baseline CloudWatch alarms named (per the supplied design's §10.2 list)
- Acknowledged that HA-tuned monitoring is deferred to AT3
- Cross-references A17

**NYS for the build narrative:**
- Any sub-section missing
- Any sub-section that contradicts the screenshot evidence in Appendix A
- "Build narrative" reads like generic AWS documentation rather than a description of what *was actually built*

---

## 6. Marking §5 Configuration Decisions

**UoC evidenced:** [ICTCLD401 PC 1.1] · [ICTCLD401 PC 1.3]. **Critical section.**

**Satisfactory looks like:**
All 8 decision points justified with rationale tied to the YAT LMS workload (not generic):

| # | Decision | What a credible justification references |
|---|---|---|
| C1 | EC2 instance type | Concurrent-user load from the LMS application spec (200–300 typical, 500–700 peak); cost envelope from AT1 CBA; growth headroom |
| C2 | RDS instance class | Database workload characteristics (relatively read-heavy for an LMS); concurrent-connection load |
| C3 | EBS data volume + RDS storage sizing | The 178 GB current footprint + ~25 GB/year growth from the LMS app spec; 12-month projection + headroom |
| C4 | ASG scaling threshold | CPU profile expectations during assessment-week peaks; cooldown/cool-off implications |
| C5 | Permission boundary for MTS-Consultants | Specifically the AWS Academy lab access scope |
| C6 | Bastion / RDP design | Security trade-off: bastion host vs SSM Session Manager vs VPN-only |
| C7 | MySQL engine version | DOODLE compatibility (the migration brief says no application upgrade) |
| C8 | DNS strategy + ACM cert | LMS hostname strategy; ACM auto-renewal considerations |

**Acceptable variance:** specific choices can differ between students (e.g. m5.large vs m6i.large), as long as the justification holds. The benchmark is the quality of reasoning, not a single correct answer.

**NYS:**
- Any of C1–C8 left blank or with "TBD"
- Generic justifications ("m6i.large is a good general-purpose instance") not tied to YAT workload
- Justification contradicts the workload (e.g. picking a tiny instance after acknowledging 700 peak concurrent users)
- Sizing decisions without calculations shown

---

## 7. Marking §6 Testing and Validation

**UoC evidenced:** [ICTCLD401 PC 2.6, 3.2] · [ICTCLD502 PC 4.2, 4.3 partial]. **Critical section.**

**Satisfactory looks like, per test category:**

| Test category | Satisfactory evidence |
|---|---|
| 6.1 Connectivity | All four tests recorded with Pass/Fail; Appendix C C1, C2 evidence attached |
| 6.2 Autoscaling | Load applied, scale-out occurred, instance entered service, scale-in followed; Appendix C C3 evidence attached |
| 6.3 DB connectivity | MySQL client connection established from EC2 over private network; version confirmation matches C7 decision; Appendix C C4 evidence attached |
| 6.4 End-to-end smoke | LMS reachable via ALB DNS name; HTTP success status; Appendix C C5 evidence attached |

**NYS:**
- Any test category left blank or "not tested"
- Tests recorded as Pass without evidence to support
- Evidence contradicts the recorded outcome
- No negative test (RDS NOT publicly reachable) — this is a deliberate test of security posture

---

## 8. Marking §7 Operational Handover

**UoC evidenced:** [ICTCLD401 PC 4.3] *(save and store user documentation per organisational policies and procedures)*.

**Satisfactory looks like:**
- Access information for YAT ICT documented (which IAM groups, who has access post-handover)
- Runbook references to baseline design + tagging + backup baseline + alarms
- §7.4 Documentation filing — student names how/where the report was filed per YAT records procedures (refer to the Backup and Retention Policy or the Records Management Policy on the YAT intranet)

**NYS:**
- §7.4 filing not addressed (PC 4.3 not evidenced)
- Handover section reads as a checklist without actual handover content
- Known limitations section claims AT2 is HA when it isn't

---

## 9. Marking §8 Knowledge Evidence Responses

**UoC evidenced:** [ICTCLD401 KE 5, 6, 7, 8, 9, 10]. **Critical section.**

Below are model answers for each question. Student answers may differ in detail but must demonstrate the underlying knowledge applied to their own Deployment Report.

### Q1 — VM/networking/scaling features [ICTCLD401 KE 5]

**Model coverage:** Student names each of EC2, ASG, ALB with the feature they provide and explains how the choice supports YAT LMS specifically.

- *EC2:* compute capacity to run the Windows Server 2016 + DOODLE LMS stack; sized for the 200–300 typical / 500–700 peak concurrent user load (per LMS app spec).
- *ASG:* horizontal auto-scaling so that the LMS can scale-out during assessment-window peaks without manual intervention; CPU threshold chosen at X% based on Y reasoning.
- *ALB:* distributes traffic across the ASG members; HTTPS termination via ACM cert; health-check approach ensures unhealthy instances are removed from rotation quickly.

**NYS:** generic feature explanations without ties to YAT; doesn't address all three components; ignores the workload context.

### Q2 — Vertical vs horizontal scaling; managed services; storage [ICTCLD401 KE 6]

**Model coverage:**
- *(a) RDS over self-hosted:* managed backups, patching, monitoring; reduces operational burden on YAT ICT (which lacks cloud expertise per the scenario context); HA-readiness (Multi-AZ is one config change away — coming in AT3).
- *(b) EBS + S3 together:* EBS for OS + application binaries + frequently-accessed application data (low latency, block-level); S3 for course attachments + student submissions + backups (cheaper at scale, virtually unlimited, versioning + lifecycle to Glacier supports records retention).
- *(c) Vertical vs horizontal:* vertical would require downtime to resize (poor fit for an LMS that must stay available during assessment windows); horizontal via ASG scales without downtime and handles the assessment-week 3× spike pattern. Trade-off: horizontal needs the application to support stateless/sticky-session patterns; LMS sessions may need session affinity at the ALB.

**NYS:** textbook definitions only; no reference to YAT specifics; missing one or more of the three sub-parts.

### Q3 — Shared security responsibility [ICTCLD401 KE 7]

**Model coverage:**
- *(a) Two YAT responsibilities:* e.g. (1) Windows Server 2016 OS patching post-handover; (2) IAM users + MFA management for YAT ICT staff. Both fall on YAT's side of the shared responsibility line.
- *(b) One responsibility shifted from YAT to AWS:* hardware refresh + data centre cooling/power (used to be YAT's server-room overhead; now AWS's). Or: backup-tape rotation (now AWS-managed RDS backups). Or: physical data centre security.

**NYS:** copy-paste from supplied design without identifying specific responsibilities; gets the responsibility line wrong (e.g. claims patching is AWS's).

### Q4 — User access protocols [ICTCLD401 KE 8]

**Model coverage:** Student picks one IAM group, describes its permissions, names the job function, explains why permissions differ from another group.

Example: `YAT-ICT-Admins` has read-only on infrastructure + full access to CloudWatch and RDS console + no IAM modifications. Job function: day-to-day operations after handover. Different from `MTS-Consultants` (full admin during build) because YAT ICT shouldn't be modifying IAM (that's a security boundary), and different from `Read-Only-Auditors` (no service mutations) because YAT ICT need to acknowledge/clear alarms.

**NYS:** group described without job function context; permissions stated without rationale.

### Q5 — Security policies + network traffic limits [ICTCLD401 KE 9]

**Model coverage:** Student picks one SG (e.g. `sg-db`), describes its rules, explains why traffic is restricted that way, names the risk if removed.

Example: `sg-db` allows MySQL:3306 inbound only from `sg-app` (no public ingress at all), no outbound. Restricted because the database must only be reachable from the application tier — direct database access from the internet would expose student PII (Privacy Act 1988 risk). Removing the restriction would mean anyone on the internet could attempt to brute-force MySQL credentials.

**NYS:** SG rules stated without rationale; risk statement absent or generic.

### Q6 — Role of DNS [ICTCLD401 KE 10]

**Model coverage:** Student identifies two DNS resolution points and explains what fails if misconfigured.

Examples:
- *ALB DNS name* — end-users browse to the LMS hostname which resolves (via Route 53 or YAT's authoritative DNS) to the ALB DNS name, which AWS resolves to one of the ALB's IPs. If misconfigured, end-users get the wrong IP or no IP → can't reach the LMS.
- *RDS endpoint* — the EC2 instance connects to RDS via its DNS endpoint (which AWS uses to abstract away which underlying instance is the primary). If misconfigured (e.g. wrong endpoint in app config), the application can't reach the database.

**NYS:** generic "DNS resolves names to IPs" without YAT-specific resolution points named.

### Marking checks for Appendix 2 (§8) overall

**Award credit for:**
- All 6 questions answered
- Each answer references specific sections of the student's own report
- The cited content is actually present in their report

**Common deductions:**
- Generic textbook answers ("IaaS provides infrastructure")
- Citations to report sections that don't contain what the answer claims
- Repeating the supplied design verbatim instead of synthesising

---

## 10. Marking Appendix A — Build Evidence (Screenshots)

**UoC evidenced:** [ICTCLD401 PE 1, PE 2]. **Critical section.**

**Satisfactory looks like:**
- All 17 screenshots (A1–A17) present
- AWS region indicator visible in each (top-right of console)
- Named items visible per the template's screenshot description
- Screenshots are from the actual deployed environment (not Photoshopped, not from AWS marketing material)

**Common deductions:**
- Region indicator not visible — can't verify ap-southeast-2
- Screenshot doesn't show the named items (e.g. A14 doesn't show the launch template attached to the ASG)
- Screenshot from a tutorial / shared resource rather than the student's own deployment

---

## 11. Marking Appendix B — Configuration Exports

**UoC evidenced:** [ICTCLD401 PE 2].

**Satisfactory looks like:**
- All 7 exports (B1–B7) present
- Exports are consistent with the screenshots in Appendix A (e.g. the security group rules in B2 match the rules visible in A8)
- Exports are recognisably from the AWS environment (JSON/text dump format consistent with `aws ec2 describe-*` output)

**NYS:**
- Exports missing
- Exports inconsistent with screenshots (suggests fabrication)
- Generic example configurations rather than the student's own

---

## 12. Marking Appendix C — Test Evidence

**UoC evidenced:** [ICTCLD401 PE 3] · [ICTCLD502 PC 4.2, 4.3].

**Satisfactory looks like:**
- All 6 evidence items (C1–C6) present
- Evidence is consistent with the outcomes recorded in §6
- Test C6 (negative test — RDS not publicly reachable) explicitly demonstrated

**NYS:**
- Evidence missing for one or more tests
- Evidence shows the opposite of the recorded §6 outcome
- Negative test missing — security posture not verified

---

## 13. Marking Appendix D — Reflections

**UoC evidenced:** [ICTCLD401 FS Learning, FS Planning and organising, FS Self-management skills].

**Satisfactory looks like:**
- Both reflections present
- Each is specific to the student's own build (not generic)
- R1 names a transferable lesson and how it was arrived at
- R2 names a decision validated AND a decision the student would revise

**NYS:**
- Reflections absent or one-sentence-each
- All reflections positive — no honest "would revise" content
- Generic reflections that don't engage with the actual build (could be cut-pasted into any deployment report)

---

## 14. Common deductions across the Deployment Report

- **Generic content rather than YAT-specific.** Every section needs to be about *this build* — not about cloud architecture in the abstract.
- **Screenshot evidence inconsistent with narrative.** §4 says one thing, screenshots show another.
- **Test outcomes recorded without supporting evidence.** §6 claims a Pass without an Appendix C item supporting it.
- **Configuration Decisions left blank or "TBD".** §5 is critical; gaps here fail the assessment.
- **HA work creeping into AT2.** Multi-AZ DB, cross-AZ subnets, or HA monitoring in the build means the student has pre-empted AT3 — flag the scope but do not penalise per se; HA design itself is AT3-evidenced.
- **Lack of records-procedure filing in §7.4.** PC 4.3 specifically requires this; cannot be evidenced without it.

---

## 15. Overall result calculus

For AT2 to be marked **Satisfactory** overall:

- All 5 critical criteria Satisfactory: A3 (workload tier build narrative), A5 (Configuration Decisions), A6 (Testing and Validation), A8 (KE Responses), A9 (Appendix A Build Evidence)
- All other criteria (A1, A2, A4, A7, A10, A11, A12, A13) Satisfactory OR evidence elsewhere in the bundle compensates
- Submission complete (all sections + all four appendices)

If any critical criterion is NYS, the overall is NYS and resubmission is required for that section.

---

## Authoring notes

- **Dependencies on scenario authoring (not yet built — flagging for the scenario checklist):**
  - Final rendering of the supplied baseline design (currently markdown; needs topology diagrams + formal layout — flagged on supplied design file)
  - Example previous Deployment Report (currently scaffold only — to be batch-authored with other exemplars)
  - Deployment Report template needs transfer to Word for student download from the YAT intranet
- **Placeholder URL:** `https://www.placeholder.com.au` used throughout for the YAT intranet — replace when the real URL is decided
- **Names:** Sam Walker and Pat Lin are placeholder names for the role-played YAT ICT Manager and MTS Senior Consultant — confirm before issuing to students (consistent with AT1)
