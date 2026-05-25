# AT2 — Deployment Report (Student) — content for the .docx

> **Status: DRAFT (Claude v1, 2026-05-25).** Companion markdown for `AT2-DeploymentReport-Student.docx` (institutional Project Assessment - Student template, single-task — no Part A/B split). Paste content into the .docx then delete this file per cluster authoring convention §3.
>
> **Convention:** *italic notes in this file like this* are authoring annotations and should not be pasted into the .docx.

---

# Project Assessment – Student Instructions

## Details

| Field | Value |
|---|---|
| Qualification code and title | ICT50220 Diploma of Information Technology |
| Unit code and title | ICTICT517 Match ICT needs with the strategic direction of the organisation<br>ICTCLD401 Configure cloud services<br>ICTCLD502 Design and implement highly-available cloud infrastructure |
| Assessment task title | AT2 — Cloud Foundation Build: YAT LMS Migration |
| Assessment task number | 2 of 3 |
| Due Date | (leave blank — per delivery) |
| Teacher/Assessor name | (leave blank — per delivery) |
| Teacher/Assessor email | (leave blank — per delivery) |

---

## Student instructions

### Assessment overview

You are being assessed on the implementation of a supplied AWS cloud architecture for the YAT LMS migration, and the production of a Deployment Report documenting your build.

This is an **open-book practical assessment**. You may use the YAT intranet (https://www.placeholder.com.au), AWS Academy lab environments, AWS documentation, course reference materials, and external research (which must be cited) throughout.

AT2 is the second of three assessment tasks in the S1-CL1 Cloud Design and Build cluster. It builds on AT1 (the Business Case engagement) and feeds into AT3 (HA hardening and project closure). You continue in the same MTS consultant role across all three.

**Submission:** the completed Deployment Report (`.docx`) with all appendices populated, submitted via the LMS.

The assessment will not proceed if for any reason it is not safe to do so. The assessor must advise you of the reason for suspending the assessment, what safety action should be taken, and of revised arrangements when it is safe to resume.

There is zero tolerance for plagiarism, cheating and collusion. You will be expected to make a declaration that all work is your own prior to submission. Refer to the Training and Assessment Policy for further information.

### Task to be assessed

Following the YAT board's approval of the action plan in your AT1 Business Case engagement, you took a period of planned annual leave. During that time MTS Senior Architecture worked with YAT ICT to translate the approved direction into a detailed technical design — the **YAT LMS Cloud Architecture — Baseline Design** — which has been approved by Pat Lin and Sam Walker and is now your build specification.

You have returned to MTS to lead the foundation-build phase of the engagement. Your task has two parts that combine into a single deliverable:

1. **Implement the supplied AWS architecture** for the YAT LMS migration foundation build, in the AWS Academy lab environment authorised for this engagement.
2. **Produce a Deployment Report** documenting your build, using the YAT-provided Deployment Report template. The report includes Configuration Decision justifications (where the supplied design left choices to you), testing outcomes, an operational handover for YAT ICT, written responses to six Knowledge Evidence questions about your own build, and four appendices of evidence (build screenshots, configuration exports, test results, reflections).

The Deployment Report is your single submitted deliverable. All build evidence (screenshots, configuration exports, test results) is captured in the report's appendices — there is no separate portfolio submission.

This phase is the foundation build only. The architecture is intentionally **non-HA** at this stage — HA hardening is the next phase (AT3) and is out of scope here.

### Resources required

#### Provided to you (download from the YAT intranet)

- **YAT LMS Cloud Architecture — Baseline Design** (intranet *Engagement Documents* section) — the design you implement
- **Deployment Report template** (intranet *Templates* section) — the template you fill in
- **Example previous Deployment Report** (intranet *Document Archive* section) — review at least one before starting your own
- All other scenario materials (LMS application spec, current ICT environment, organisational policies, your AT1 Business Case)

#### Provided externally

- AWS Academy lab access — Cloud Foundations [104469] + Cloud Architecting [172221]

#### You supply

- Computer with web browser
- Word-processing software (Microsoft Word or equivalent)
- A screenshot tool

### Time allowed

(leave blank)

### Location

(leave blank)

### Assessment criteria

To receive a Satisfactory result for AT2 you must:

1. Achieve Satisfactory on every criterion in the Assessment Criteria table (below)
2. Submit a completed Deployment Report (`.docx`) with every section and every appendix populated, using the YAT-provided Deployment Report template

### Second attempt

If you are deemed not satisfactory for this assessment, you will be given one (1) more attempt at this assessment (or part thereof), or your teacher/assessor will negotiate a further assessment with you. The second attempt must be completed within 10 working days from the date your feedback is given.

*(institutional boilerplate — preserve as-is)*

### Important information

You can access further information regarding assessment, including Recognition of Prior Learning, Reasonable Adjustment and Assessment Appeals in the Student handbook which can be found on the MyLearning portal.

*(institutional boilerplate — preserve as-is)*

### How to submit

Submit the completed Deployment Report (`.docx`) to the LMS by the due date. The report includes all four appendices populated; no separate files are submitted.

---

# Detailed task instructions

*Place this section immediately after "Task to be assessed" in the docx — keeping the substantive task description ahead of the criteria table for natural reading order.*

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

Using AWS Academy, implement the architecture exactly as specified in the supplied design. The design is opinionated where it matters — region, network topology, IAM model, service categories, security controls, tagging — and intentionally silent where you must demonstrate professional judgement (specific instance types, sizing, scaling thresholds, etc.). The supplied design's §14 *Configuration decisions left to the implementer* enumerates the eight decisions you must make and justify (C1 through C8).

For each of those configuration decisions, make a deliberate, justified choice based on the YAT LMS workload as described in the LMS Application Specification on the YAT intranet. You will document the choice and rationale in §5 of your Deployment Report.

Important constraints on the build:

- **The deployment is single-AZ and non-HA by design.** HA hardening is the next phase (AT3). Do not pre-empt that work — Multi-AZ database, cross-AZ subnets, cross-Region backup copies, failure simulation, DR runbook are all out of scope for this phase.
- **All security, encryption, tagging, and naming conventions in the supplied design are mandatory.** These are non-negotiable.
- **Take the screenshots listed in Appendix A of the Deployment Report template *as you go*, not at the end.** Trying to recreate the state for a screenshot after you've moved on is painful and sometimes impossible.
- **Test outcomes (§6 of the template) require you to actually run the tests** — do not fabricate. Screenshot the test evidence as you run.

## Part 2 — Produce the Deployment Report

Download the **Deployment Report template** from the YAT intranet's *Templates* section. Populate every section and every appendix. The template provides explicit prompts in each section — follow them.

Your report covers:

- §1 Executive Summary (write this last)
- §2 Engagement Context (referring back to your AT1 Business Case + the supplied design)
- §3 Scope of Deployment (what's in this phase, what's deferred to AT3)
- §4 Build Narrative (chronological account by layer — IAM, network, compute, ALB, DB, storage, security, monitoring)
- §5 Configuration Decisions (justifications for the eight points the design left to you — C1 through C8)
- §6 Testing and Validation (results from the tests in §6 of the template)
- §7 Operational Handover (information YAT ICT needs to operate the environment, including filing the report per YAT's records procedures)
- §8 Knowledge Evidence Responses (six contextual questions about choices in your own build)
- Appendix A — Build Evidence (17 named AWS console screenshots — the template lists them explicitly)
- Appendix B — Configuration Exports (IAM policies, security group rules, VPC config, etc.)
- Appendix C — Test Evidence (logs, screenshots of test outcomes)
- Appendix D — Reflections (two short reflective responses on the build experience)

**Before starting your own report**, review at least one **Example previous Deployment Report** from the YAT intranet's *Document Archive* section. The example shows what a completed report looks like in style, depth, and structure — model your work on it.

---

## Tips for success

- **Review the example past Deployment Report first.** It shows what good looks like and saves you guessing about depth and structure.
- **Read the supplied design end-to-end before building** — including the "out of scope" section (§13) and the "configuration decisions left to the implementer" section (§14). The build is faster when you know the constraints upfront.
- **Screenshots as you go, not at the end.** This is the single most common failure mode in this assessment.
- **Justify every configuration decision against the YAT workload.** Generic justifications ("m6i.large is a good choice for general-purpose workloads") are not credible. Specific justifications ("m6i.large handles the expected 200–300 concurrent users with headroom for assessment-window peaks per the LMS application spec, at a unit cost consistent with the AT1 CBA Year-1 budget") are.
- **Don't paper over the eight Configuration Decisions.** The §5 table is one of the most-scrutinised sections.
- **The Knowledge Evidence responses (§8) are about your own build.** Every answer should reference specific sections, components, or decisions in your report. Generic textbook answers about cloud concepts won't pass.
- **The reflections in Appendix D are honest, not promotional.** A genuine "here's a decision I'd revise" earns more credit than a varnished "everything was perfect".
- **File the report per YAT's records procedures** (§7.4 of the template) — this is part of what's being assessed.

---

## Assessment criteria table

*Mirrors the Assessor Marking Guide, in "you" voice and without UoC reference tags.*

| # | Criterion | Satisfactory? |
|---|---|---|
| A1 | §1 Executive Summary — you produced a concise (≤ 1 page) summary of what was delivered, with explicit acknowledgement that HA hardening is deferred to AT3, and numbers/components reconcile with the body of the report | ☐ Yes ☐ No |
| A2 | §4.1 + §4.2 + §4.7 Build narrative — Foundation tier (IAM, network, security) — you described the IAM model, network topology, and security-group model, with cross-references to Appendix A screenshots and Appendix B configuration exports | ☐ Yes ☐ No |
| A3 | §4.3 + §4.4 + §4.5 + §4.6 Build narrative — Workload tier (compute, load balancing, database, storage) — you described the EC2 + ALB + ASG, the RDS managed database, and the EBS + S3 storage | ☐ Yes ☐ No |
| A4 | §4.8 Build narrative — Operability (autoscaling configuration, baseline monitoring) — you described the ASG scaling policy and the baseline CloudWatch alarms; you identified the shared security responsibility outcome of your build | ☐ Yes ☐ No |
| A5 | §5 Configuration Decisions — you justified all 8 decision points (C1–C8 from the supplied design §14) with rationale tied to the YAT LMS workload | ☐ Yes ☐ No |
| A6 | §6 Testing and Validation — you ran the four required test categories (connectivity, autoscaling, database connectivity, end-to-end smoke); results are documented with cross-reference to Appendix C evidence | ☐ Yes ☐ No |
| A7 | §7 Operational Handover — you documented access information for YAT ICT, named known limitations carried into AT3, and confirmed filing of the report per YAT's documented records procedures | ☐ Yes ☐ No |
| A8 | §8 Knowledge Evidence Responses — you answered all 6 KE questions with specific reference to your own build, not generic textbook answers | ☐ Yes ☐ No |
| A9 | Appendix A Build Evidence — all 17 named screenshots (A1–A17) are present, the AWS region indicator is visible, and the named items are visible per the template's requirements | ☐ Yes ☐ No |
| A10 | Appendix B Configuration Exports — all 7 named exports (B1–B7) are present, exported from the actual deployed environment | ☐ Yes ☐ No |
| A11 | Appendix C Test Evidence — test outcomes are documented with supporting evidence; outcomes are consistent with §6 | ☐ Yes ☐ No |
| A12 | Appendix D Reflections — two honest reflective responses are present, both specific to your own build experience | ☐ Yes ☐ No |
| A13 | Document quality — the Deployment Report uses plain English, appropriate technical vocabulary, structure, formatting, and depth relevant to a professional consulting deliverable for an RTO client | ☐ Yes ☐ No |

*Note: §2 (Engagement Context) and §3 (Scope of Deployment) are still required template sections — you must complete them for a coherent report. They are not separately listed as graded criteria above because they don't trace to specific UoC requirements, but any weakness in these sections will be reflected in criterion A13 (Document Quality).*

---

## Document control

| | |
|---|---|
| **AT2 brief version** | DRAFT v1 (2026-05-25) |
| **Owner** | [FILL IN — institution] |
| **Companion artefacts** | `AT2-DeploymentReport-Assessor.docx` (assessor instructions + marking guide + benchmark) · `scenario/templates/template-deployment-report-S1-CL1-AT2.md` (student-fillable template) · `scenario/internal-lms-cloud-architecture-design-S1-CL1-AT2.md` (supplied baseline design) |
