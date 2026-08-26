# Topic 1 — Cloud literacy · Coverage

**Topic 1 of 14** in the CL1 teaching sequence · **AT1 content Topic** (knowledge foundation) · teaching source: AWS decks (ACF M01/M02/M04/M06–M10, ACA M02).

This file is the **coverage spec** — what this Topic must cover, in UoC and AT1 terms. `teaching.md` and `exercise/` are built to satisfy it.

---

## What this Topic must cover

The cloud knowledge base a consultant needs *before* analysing or designing a migration — breadth, at a "recognise / explain / classify" level (the hands-on *building* of these services is AT2). Five components:

- **C1 — Cloud fundamentals & deployment models.** What cloud computing is; the deployment models (public / private / hybrid / community) and when each applies; the on-prem→public-cloud shift.
- **C2 — Service models: IaaS / PaaS / SaaS.** Definitions, the who-manages-what split, and classifying real services + the reasoning for choosing a service type.
- **C3 — Core AWS services for a multi-tier web workload.** EC2/EBS, RDS, Application Load Balancer, Auto Scaling, S3, NAT/Internet Gateway, CloudWatch — general features and role in the stack.
- **C4 — Industry technology standards.** NIST SP 800-145, AWS Well-Architected Framework, ISO/IEC 27017, ACSC Essential Eight, ITIL — what each is and which decision it informs.
- **C5 — Cloud cost models & economics.** On-demand vs Reserved Instances vs Spot vs pay-as-you-go; how cost scales with demand; the RI-discount rationale.

---

## 1. UoC mapping

Knowledge Evidence **taught / developed** in this Topic:

| UoC item | Descriptor | Component |
|---|---|---|
| [ICTCLD401 KE 11] | Cloud models — on-premises / private / hybrid / public | C1 |
| [ICTCLD401 KE 3] | Principles and functions of cloud computing solutions and technologies, incl. IaaS / PaaS / SaaS | C2 |
| [ICTCLD401 KE 2] | Industry standard hardware and software products | C3 |
| [ICTCLD502 KE 2] | Industry standard hardware and software products | C3 |
| [ICTCLD401 KE 1] | Industry technology standards | C4 |
| [ICTCLD502 KE 1] | Industry technology standards | C4 |
| [ICTCLD401 KE 4] | Cost models and cloud economic theories | C5 |
| [ICTCLD502 KE 3] | Cloud cost models and scalability | C5 |

> C1–C5 are simply the things this Topic covers. These UoC items are **taught** here but formally **evidenced for assessment** in AT1 Appendix 2 (§2 below) — Topic 1 *develops* the UoC, the AT *evidences* it.

---

## 2. AT1 equivalence / alignment

What in the real AT1 (Business Case) this Topic prepares students for:

| AT1 element | Criterion | How Topic 1 aligns |
|---|---|---|
| **Appendix 2 — Knowledge Evidence, selection-style Q1–Q5** | A11 | Direct 1:1 — the Topic teaches exactly what these questions test: **Q1** IaaS/PaaS/SaaS (C2), **Q2** deployment model (C1), **Q3** industry standards (C4), **Q4** industry-standard products (C3), **Q5** cost models & scalability (C5). |
| **§6 + Appendix 1 — Cost-Benefit Analysis** | A5 | Cost-model knowledge (C5) underpins researching/justifying AWS pricing; service knowledge (C3/C4) underpins choosing which services get priced. |
| **§5 — Options Considered & Evaluation** | A4 | Service-type and service-catalogue knowledge (C2/C3) underpins defining the workload and articulating the cloud option. |
| **§2 — Strategic Alignment Analysis** | A3 | Industry-standards / technology-trend awareness (C4) feeds the external industry context. |

**Practice-activity alignment:** the Topic's exercise mirrors **Appendix 2 Q1–Q5** in *contextual* form — classify a sample solution's components by service model, name the likely AWS service, and identify the cost model — set against the **practice scenario (YAT Accounting System / Ledgerline)**, not the LMS.

---

## Out of scope for this Topic (covered elsewhere)

- **517 knowledge** — action-plan sections (KE 1), evaluation methods (KE 2), evaluation of competing systems (KE 3), current/emerging trends (KE 4) → Topics 2–4.
- **Hands-on building** of these services (IAM, VPC, EC2, RDS, etc.) → the AT2 build Topics (6–10). Topic 1 is conceptual breadth only.
- **CLD401 KE 5–10** (VM/scaling features, shared responsibility, access protocols, DNS, etc.) → evidenced in AT2, taught in its Topics.

---

## Coverage checklist (for `teaching.md` + `exercise/` to satisfy)

- [ ] Every UoC item in §1 is taught in `teaching.md`.
- [ ] Each of C1–C5 has teaching content (deck reference and/or bespoke framing).
- [ ] The exercise lets students *practise* the Appendix 2 Q1–Q5 knowledge contextually, on the practice scenario.
- [ ] AT1 alignment (§2) is explicit enough that a student leaving this Topic could attempt the related AT1 elements.
