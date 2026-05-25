# S1-CL1 Scenario — Documents/Pages Checklist

> **STATUS: DRAFT.** Working checklist of every document, page, or artefact the cluster's mock scenario (YAT College) needs to publish so that students have a single reference source for the cluster assessments. Each item carries the UoC reference(s) it satisfies and the source status (already exists / needs port / needs new authoring). **Nothing here is decided** — list is for review and reaction.
>
> **Delivery vehicle (proposed, TBD):** mock YAT public website + mock intranet behind a fake SSO sign-in. Public site carries the org-facing content; intranet carries policies, procedures, ICT environment, project-engagement materials. Replaces handing students a bundle of separate documents.
>
> Status legend:
> - ✅ **Exists** in YAT case study (517 AT2 / 517 source) — port across
> - 🟢 **Portable from Llamazonia** (502 AT2) — rebrand-only port
> - 🟡 **Partial** — exists but thin / implicit, needs extension
> - ❌ **New authoring required**

---

## Public-facing site (no sign-in required)

- [ ] **About / Mission / Vision** — ✅ Exists in YAT (Mission, Vision)
  - [ICTICT517 AC 2] Detailed information relating to a strategic organisation plan, objectives, and direction
- [ ] **Strategic plan summary (public)** — ✅ Exists in YAT (Strategic Business Goals, Business Objectives)
  - [ICTICT517 AC 2] strategic plan, objectives, and direction
  - [ICTICT517 PC 1.1] Analyse and document current strategic plan
- [x] **About our people / org structure** — ✅ Authored 2026-05-23 (YAT roles preserved; Claude-proposed headcount, reporting lines, decision authority — all **TBD** confirm). See `public-org-structure.md`.
  - [ICTICT517 AC 4] Individual superior in the organisation
  - [ICTICT517 AC 1] A site where ICT needs and strategic directions are coordinated *(the "site" framing)*
- [ ] **Locations / campus** — ✅ Authored 2026-05-23 (175 Cremorne St, Cremorne VIC 3121 — see `public-locations-campus.md`)
  - [ICTICT517 AC 1] coordination site

---

## Intranet — ICT environment (internal)

- [ ] **Current ICT environment overview** — ✅ Exists in YAT (Network, Network Services, System Management, Application Services, LMS, Email, Storage, Desktops, Printers, Network Security, ICT Facilities)
  - [ICTICT517 AC 5] Information on current ICT systems and practices including operating systems, hardware, and security
  - [ICTICT517 PC 1.2] Determine current state of ICT systems and practices
  - [ICTCLD502 PC 2.1] Review architecture of traditional multi-tier web application in non-cloud environment
- [x] **On-prem network diagram** — ✅ Authored 2026-05-23 (Mermaid topology + component summary; original YAT image still to be re-rendered for the intranet UI). See `internal-on-prem-network-diagram-S1-CL1-AT1.md`.
  - [ICTICT517 AC 5] current ICT systems
  - [ICTCLD502 PC 2.1] review traditional multi-tier architecture
  - [ICTCLD502 PC 2.2] Identify any single points of failure
- [x] **LMS server specifications and current status** — ✅ Authored 2026-05-23 (YAT narrative preserved; Claude-proposed specs and utilisation **TBD** confirm). See `internal-lms-server-status-S1-CL1-AT1.md`.
  - [ICTICT517 AC 5] current ICT systems including OS, hardware, security
  - [ICTCLD502 PC 2.3] Estimate recovery objectives for multi-tier web components
- [x] **Current backup and recovery process** — ✅ Rebranded 2026-05-23 from Llamazonia (load-balancer step removed for YAT single-server on-prem topology; tape-from-offsite preserved). See `internal-backup-recovery-process-S1-CL1-AT1.md`.
  - [ICTCLD502 PC 2.3] Estimate recovery objectives
  - [ICTCLD502 KE 4] recoverability (RTO/RPO)
- [x] **Hardware / software inventory summary** — ✅ Authored 2026-05-23 (tabular collation; vendor/model placeholders left as **TBD**). See `internal-hardware-software-inventory-S1-CL1-AT1.md`.
  - [ICTICT517 AC 5] hardware and security
  - [ICTCLD502 AC 5] industry standards (which the products align to)

---

## Intranet — Policies and procedures

- [ ] **ICT change management procedure** — ✅ Exists in YAT (full 13-step procedure: change request form, risk and impact analysis, ICT manager approval, senior management sign-off, rollout/rollback, debrief)
  - [ICTICT517 AC 3] Organisational policies and procedures relating to the implementation of ICT changes
  - [ICTICT517 PC 3.1] action plan consistency with organisational policy and procedures
  - [ICTCLD401 PC 4.3] Save and store user documentation according to organisational policies and procedures
  - [ICTCLD502 PC 5.3] Obtain final sign off from required personnel
- [x] **User access policy** — ✅ Authored 2026-05-23 (formal 12-section policy: role matrix, joiner/mover/leaver, passwords, MFA, PAM, remote access, reviews, sanctions, ownership). Claude-authored using ACSC Essential Eight + Privacy Act defaults — **TBD** confirm specifics. See `internal-user-access-policy.md`.
  - [ICTCLD401 AC 4] user access and business protocols
  - [ICTCLD502 AC 8] user access and business protocols
  - [ICTCLD401 KE 8] user access protocols and policies according to organisation hierarchy and job function
  - [ICTCLD401 PC 1.5] Identify user access protocols and policies
- [x] **Acceptable use policy** — ✅ Authored 2026-05-23 (8-section policy; cross-refs User Access + Privacy + WHS). See `internal-acceptable-use-policy.md`.
  - [ICTCLD401 AC 4] business protocols
  - [ICTCLD502 AC 8] business protocols
- [x] **WHS policy** — ✅ Authored 2026-05-23 (9-section policy aligned to Vic OHS Act 2004; covers ICT-specific safety inc. server-room responsibilities). See `internal-whs-policy.md`.
  - Not directly required by any AC, but supports the realism of [ICTCLD502 AC 5] organisational procedures
- [x] **Privacy / data handling policy** — ✅ Authored 2026-05-23 (10-section policy aligned to Privacy Act 1988 + APPs + Standards for RTOs 2015 + Notifiable Data Breaches; includes Australian data-residency requirement). See `internal-privacy-policy.md`.
  - [ICTCLD502 AC 5] legislative requirements
- [x] **Backup and retention policy** — ✅ Authored 2026-05-23 (8-section policy; retention-period table covers student records, financial, ICT logs, WHS records; restoration-testing cadence; disposal procedures). See `internal-backup-retention-policy.md`.
  - [ICTCLD502 AC 5] organisational procedures
- [x] **Security baseline / incident response** — ✅ Authored 2026-05-23 (7-section combined policy; Essential Eight baseline mapped to YAT controls; 4-tier severity definitions; 6-stage NIST-style response process; external notification obligations). See `internal-security-and-incident-response.md`.
  - [ICTCLD502 AC 5] organisational procedures
- [-] **Records Management Policy** — ⏳ Placeholder authored 2026-05-25; content to be authored later. Backs the "save and store documentation per organisational policies" requirement at the cluster scale (records vs working docs, filing locations, naming + version control, retention cross-ref, disposal). See `internal-records-management-policy.md`.
  - [ICTCLD401 PC 4.3] save and store user documentation per organisational policies and procedures
  - [ICTCLD502 AC 5] organisational procedures
  - [ICTICT517 AC 3] organisational policies and procedures for ICT changes (tangential)

---

## Intranet — Project / engagement materials (the cluster brief)

- [ ] **ICT strategic plan (detail)** — ✅ Exists in YAT (ICT Goals, ICT Objectives, Planned ICT Initiatives — including LMS-first migration directive)
  - [ICTICT517 AC 2] strategic plan, objectives, and direction
  - [ICTICT517 PC 1.1] Analyse and document current strategic plan
- [ ] **LMS migration role brief** — ✅ Exists in YAT ("Your role requirements" block: MTS consultant + LMS recommendations: 100% resource increase, 99.2% → 99.9% availability, no OS/app changes)
  - [ICTICT517 AC 4] Individual superior in the organisation
  - [ICTICT517 PC 1.4] Report on proposed changes to superior
- [x] **LMS application requirements / spec** — ✅ Authored 2026-05-23 (functional spec covering user functions, concurrent load, data stored, SSO, integrations, SLA targets, accessibility, data residency). Claude-proposed values **TBD** confirm. See `internal-lms-application-spec-S1-CL1-AT1.md`.
  - [ICTCLD502 AC 5] business and functionality requirements
  - [ICTCLD502 AC 3] information and data sources required to design and implement cloud infrastructure
  - [ICTCLD401 PC 1.8] Define workload according to business requirements
- [x] **Functional and non-functional requirements (the LMS cloud-migration brief)** — ✅ Rebranded 2026-05-23 from Llamazonia (Linux→Windows; 99%→99.9%; AWS cert claim reattributed to MTS). See `internal-lms-cloud-migration-requirements-S1-CL1-AT1.md`.
  - [ICTCLD502 AC 5] business and functionality requirements
  - [ICTCLD502 PC 1.1] Determine reliability, recoverability and service levels required for application
  - [ICTCLD502 PC 1.2] Determine cloud infrastructure according to business needs
- [x] **HA database requirements (multi-AZ etc.)** — ✅ Rebranded 2026-05-23 from Llamazonia (refrained as upgrade to managed multi-AZ MySQL on AWS for the migrated LMS). See `internal-ha-database-requirements-S1-CL1-AT3.md`.
  - [ICTCLD502 PE 1] design fault-tolerant cloud infrastructure
  - [ICTCLD502 AC 5] business and functionality requirements
- [x] **Consultation notes — ICT manager interview** — ✅ Authored 2026-05-23 as narrative meeting record between MTS consultants and YAT ICT Manager; maps onto requirements list. **TBD** confirm placeholder names. See `internal-ict-manager-consultation-notes-S1-CL1-AT1.md`.
  - [ICTCLD401 AC 4] data to gather information from to determine output and user requirements
  - [ICTCLD502 AC 3] information and data sources required to design and implement cloud infrastructure
  - [ICTCLD502 AC 8] data to gather information from to determine output and user requirements
- [x] **Cost inputs for CBA** — ✅ Authored 2026-05-23, restructured to inputs-only 2026-05-23 after Tim flagged the original draft was doing the analysis *for* the student. Now provides: common assumptions, current on-prem cost inputs (YAT-internal data students couldn't research), methodology guidance, pointers for cloud-cost research. Cloud-side figures + comparison + recommendation are student work. The worked analysis Claude originally drafted has been moved to the assessor benchmark at `assessments/AT1/cba-assessor-benchmark.md`. See `internal-cba-cost-inputs-S1-CL1-AT1.md`.
  - [ICTICT517 PC 3.1] action plan including prioritised schedule
  - [ICTICT517 KE 1] action plan key sections
  - [ICTICT517 FS Numeracy] financial implications of changes
  - Supports the AT1 CBA work (port of 517 AT3 Part 1)

- [x] **LMS cloud architecture design (baseline, for AT2 implementation)** — ✅ Authored 2026-05-25 as `.md` scaffold. Specifies the AT2 baseline architecture (single-AZ, single-instance ASG behind ALB, single-AZ RDS-MySQL, basic monitoring) for student implementation. Deliberately not HA — leaves HA hardening for AT3. **TBD before live delivery:** topology diagrams (draw.io or similar), formal design-document layout for intranet rendering, final review against current AWS catalogue. See `internal-lms-cloud-architecture-design-S1-CL1-AT2.md`.
  - [ICTCLD502 AC 3] information and data sources required to design and implement cloud infrastructure
  - [ICTCLD502 AC 5] business and functionality requirements
  - Implements the workload defined in [ICTCLD401 PC 1.8]; supplied to student as the design they implement in AT2

---

## Intranet — Templates (downloadable blank templates for students to fill in)

Per Tim 2026-05-25: student-fillable templates live in `scenario/templates/`. These are the blank documents the YAT intranet exposes for download — distinct from the workspace-level institutional Word templates (which are gitignored).

- [-] **Business Case template** — ⏳ Empty placeholder file in place (`templates/template-business-case.md`). Referenced from AT1. Content TBD.
- [-] **Board Presentation Deck template** — ⏳ Placeholder file in place (`templates/template-business-case-pptx.md`). Referenced from AT1. Content TBD.
- [-] **Feedback Record template** — ⏳ Placeholder file in place (`templates/template-feedback-record.md`). Referenced from AT1 (and reused at the AT3 closure meeting). Content TBD.
- [-] **Change Request Form template** — ⏳ Placeholder authored 2026-05-25 (`templates/template-change-request-form.md`). Operationalises the 13-step `internal-change-management-procedure.md`. Used heavily in AT3 closure; referenced from AT1 action plan + AT2 cutover. Content TBD.
  - [ICTICT517 PC 3.1] action plan consistent with organisational procedures
  - [ICTCLD401 PC 4.3] save documentation per org procedures
  - [ICTCLD502 PC 5.3] obtain final sign off
- [-] **HA Design template (student-produced output, AT3)** — ⏳ Placeholder authored 2026-05-25 (`templates/template-ha-design-S1-CL1-AT3.md`). Mirrors the AT2 baseline design's shape but student-authored. Carries the bulk of 502's design-production PCs. Content TBD.
  - [ICTCLD502 PC 1.1, 2.1–2.5, 3.1–3.5] · [ICTCLD502 PE 1, PE 2]
- [-] **Closure Pack template (AT3 deliverable)** — ⏳ Placeholder authored 2026-05-25 (`templates/template-closure-pack-S1-CL1-AT3.md`). Single consolidated deliverable for AT3 — consolidates AT1 + AT2 + AT3, submitted via change-management procedure, with stakeholder feedback meeting + final sign-off. Content TBD.
  - [ICTCLD502 PC 5.1, 5.2, 5.3] · [ICTCLD401 PC 4.3] · [ICTICT517 PC 3.3]
- [-] **Security Responsibilities Matrix template (AT3 sub-deliverable)** — ⏳ Placeholder authored 2026-05-25 (`templates/template-security-responsibilities-matrix-S1-CL1-AT3.md`). Sub-deliverable inside the closure pack mapping each architecture component to its security-responsibility owner. Covers Group 2 at project-closure scale. Content TBD.
  - [ICTCLD401 PC 1.2, 1.7] · [ICTCLD401 KE 7] · [ICTCLD502 PC 1.3] (all reinforced beyond AT2)
- [x] **Deployment Report template** — ✅ Authored 2026-05-25. Full template covering Cover / §1 Exec Summary / §2 Engagement Context / §3 Scope / §4 Build Narrative (4.1–4.8) / §5 Configuration Decisions (C1–C8 from supplied design) / §6 Testing & Validation / §7 Operational Handover / §8 Knowledge Evidence (Q1–Q6 covering 401 KE 5–10) / Appendix A — Build Evidence (17 named screenshots) / Appendix B — Configuration Exports / Appendix C — Test Evidence / Appendix D — Reflections (2 FS-evidencing prompts). UoC traceability map in authoring header. TBD for live delivery: confirm KE/reflection question wording, transfer to Word for student download. See `templates/template-deployment-report-S1-CL1-AT2.md`.
  - [ICTCLD401 KE 5, 6, 7, 8, 9, 10] (Knowledge Evidence appendix)
  - [ICTCLD401 FS Learning, Planning and organising, Self-management] (Reflections appendix)
  - Plus the PCs evidenced through the report body — see the authoring header's UoC traceability map

---

## Intranet — Document Archive (exemplars — nice-to-have, not assessment-critical)

Per Tim 2026-05-25: the YAT intranet hosts a Document Archive of past MTS deliverables so students learn that whenever they need to produce a business document they should look for prior examples to model from. Exemplars are a nice-to-have learning aid; assessments can run without them. To be authored as a batch, separately from assessment-task authoring.

- [-] **Example previous Business Case** — ⏳ Placeholder file in place (`exemplars/internal-document-exemplar-business-case.md`). Content TBD.
- [-] **Example previous Board Presentation Deck** — ⏳ Placeholder file in place (`exemplars/internal-presentation-exemplar-business-case.md`). Content TBD.
- [-] **Example previous Deployment Report** — ⏳ Scaffold authored 2026-05-25 (`exemplars/internal-document-exemplar-deployment-report.md`). Content TBD.
- [-] **Example previous Closure Pack** — ⏳ Placeholder authored 2026-05-25 (`exemplars/internal-document-exemplar-closure-pack.md`). Referenced from AT3 (when drafted). Content TBD.

---

## Intranet — References (background reading)

- [x] **Industry standards reference list** — ✅ Authored 2026-05-23 (cloud definitions, security/privacy, architecture frameworks, operational management, web/data, network/identity, RTO-sector). See `internal-industry-standards-reference.md`.
  - [ICTCLD401 KE 1] industry technology standards used in cloud computing solutions and services
  - [ICTCLD502 KE 1] industry technology standards
  - [ICTCLD502 AC 5] industry standards
- [x] **Legislative requirements applicable to YAT (RTO context)** — ✅ Authored 2026-05-23 (privacy, RTO regulation, WHS, anti-discrimination, employment/financial, online safety, IP, critical infrastructure). See `internal-legislative-requirements-reference.md`.
  - [ICTCLD502 AC 5] legislative requirements
  - [ICTICT517 FS Navigate the world of work] following legislative requirements
- [x] **Reference architectures** — ✅ Authored 2026-05-23 (NIST cloud definitions, AWS Well-Architected, AWS CAF, multi-tier web app, multi-AZ RDS, IAM, migration "6 Rs", operational patterns). See `internal-reference-architectures.md`.
  - [ICTCLD401 KE 3] principles and functions of cloud computing solutions and technologies, including IaaS/PaaS/SaaS
  - [ICTCLD401 KE 11] functions, uses and differences of cloud models

---

## Cross-AT framing artefacts (not really documents, but worth noting)

- [x] **Mock SSO sign-in gate** — ✅ 2026-05-23 — folded into `website.md` §3 (visual / behaviour / copy / implementation specs). No separate document; it's a UX device described in the website spec rather than a content page.
- [x] **Cluster project narrative / front page** — ✅ Authored 2026-05-23 (two-layer page: upper half = public YAT homepage, lower half = MTS-consultant engagement framing for S1-CL1; cluster-specific framing in §4 will need revision per cluster). See `public-cluster-project-narrative.md`.

## Delivery vehicle (meta)

- [x] **Website specification** — ✅ Authored 2026-05-23 (`website.md`) — overall intent, site structure, SSO gate spec, state-versioning behaviour, hosting/build/SSG decisions (TBD). Meta-document for the team building the mock site; not part of the content set itself.

---

## Summary by status

Status of authoring as of 2026-05-23 (after the CBA cost data pack authoring pass — **all scenario content items complete**):

| Status | Count |
|---|---|
| ✅ Authored / complete (content) | 27 |
| ❌ Still to author from scratch (content) | 0 |
| **Total content items** | **27 items** |
| Meta — website spec (`website.md`) | ✅ Authored separately |

**🎉 All scenario content items now drafted.** Many items carry inline **TBD** markers where Claude has invented specifics (names, headcounts, cost figures, retention periods, etc.) — these are flagged for Tim's review and confirmation before live delivery.

Next-phase work (separate from scenario authoring):
- Tim's review of the drafted scenario content + confirmation/adjustment of TBD items
- Stakeholder review (per `assessment_plan.md` §8 critical path)
- Build the actual mock website (per `website.md` — pick SSG, set up hosting, build pipeline)
- Author the cluster AT briefs themselves (referenced by the scenario but not part of it)
- Complete the assessment mapping document (official template) + transfer ATs to official templates (per `assessment_plan.md` §8 items 7–9)
