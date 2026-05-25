# YAT College — Cost-Benefit Analysis: Cost Inputs

**Relevant to:** S1-CL1 AT1

**UoC references this document satisfies:**
- [ICTICT517 PC 3.1] Develop action plan to implement proposed changes including prioritised schedule and consistency with organisational policy and procedures
- [ICTICT517 KE 1] Key sections of an action plan for ICT implementation projects
- [ICTICT517 FS Numeracy] Interprets numerical data and applies mathematical calculations to assess the financial implications of introducing changes
- Supports the AT1 CBA work (port of the structure of 517 AT3 Part 1)

**Source status:** ✅ Authored 2026-05-23 (Claude). Provides the YAT-internal cost inputs and common assumptions the student needs to undertake the CBA. **The student is responsible for sourcing cloud-side cost figures and producing the comparison and recommendation themselves — this pack provides inputs, not the analysis.** All dollar figures are Claude-proposed plausible values for the YAT scenario — they are **not** real YAT figures. **TBD** confirm or replace with real planning figures before live delivery.

---

## 1. Purpose and how to use this pack

This pack provides:

- **YAT-internal data** about the current on-premises LMS environment that you (the MTS consultant) couldn't reasonably know without working with YAT — current server age, electricity costs, server-room rent allocation, current backup arrangements, current MTS contract value, current ICT staff allocations.
- **Common assumptions** YAT has set for this engagement (user population, growth, availability targets, indicative downtime cost, fully-loaded ICT FTE cost).
- **Methodology guidance** for how the CBA should be structured.
- **Pointers** to where to research the cloud-side cost data.

What this pack **does not** provide:

- The cloud-side (AWS) cost figures. **You must research current AWS pricing yourself** using the AWS Pricing Calculator and AWS service pricing pages, sized to the cloud architecture you propose. Your CBA submission must show your sizing assumptions and the AWS line items you derived.
- The 5-year projection.
- The comparison.
- The recommendation.

All of that is your CBA work. This pack is the inputs. Populate the supplied CBA template (`ICTICT517_Cost Benefit Analysis template.xlsx`) with the inputs below and your researched cloud-side figures.

All figures below are in **Australian Dollars (AUD)**, exclusive of GST, at 2026 price levels.

### Scope of the consulting engagement vs scope of the CBA

The **MTS consulting engagement scope** (see `internal-lms-migration-role-brief-S1-CL1-AT1.md` § Scope of the MTS consulting engagement) covers the cloud infrastructure only. LMS application installation, data migration, cutover, and organisational change management are **YAT in-house IT's responsibility**.

The **CBA scope is different and broader.** The Business Case is for the YAT board; the board is approving the *whole change*, not just the MTS share. So the CBA must include both:

- **MTS-priced costs** — what YAT will pay MTS for consulting work (one-off project labour + ongoing infrastructure support)
- **AWS-direct costs** — what YAT will pay AWS (compute, database, network, storage, monitoring, support tier)
- **YAT-internal costs** — what YAT bears as in-house cost: YAT IT staff time during the project + application deployment + data migration + cutover + organisational change management + decommissioning

A CBA that omits YAT-internal cost categories gives the board an unrealistic basis for decision-making and will be marked as incomplete. The Action Plan (§10 of the Business Case) distributes responsibility for who does what; the CBA totals the cost of doing it all.

## 2. Common assumptions

| Assumption | Value | Source |
|---|---|---|
| LMS user population | ~800 students + ~60 staff | `public-org-structure.md` |
| Concurrent users (typical / peak) | 200–300 / 500–700 | `internal-lms-application-spec-S1-CL1-AT1.md` |
| Annual student growth | +15% per year | YAT Business Objectives (affects scale-up assumptions in out-years — factor this into your cloud sizing and your "staying on-prem" capacity projections) |
| Current measured LMS availability | 99.2% | `internal-lms-migration-role-brief-S1-CL1-AT1.md` |
| Target LMS availability | 99.9% | YAT ICT Strategic Plan |
| Indicative cost of downtime to YAT | $750 per hour during teaching hours, $0 outside teaching hours | **TBD** YAT-estimated; reflects student impact, staff productivity, reputational risk |
| Fully-loaded ICT FTE cost | $115,000 per FTE/year | **TBD** — reflects salary + superannuation + on-costs |
| Analysis period | 5 years | Per the action plan brief and `ICTICT517_Cost Benefit Analysis template.xlsx` |
| Inflation factor | (configurable in the CBA template — applied at your discretion with justification) | — |

## 3. Current on-prem (Option A baseline) — YAT-supplied cost inputs

You are evaluating both *continuing on-prem* (a real option YAT may choose) and *migrating to cloud*. The on-prem option requires YAT to refresh the current end-of-life LMS server. Below are the cost inputs YAT has identified for the on-prem renewal option.

### 3.1 One-off capital required for on-prem renewal

| Item | Cost |
|---|---:|
| Replacement LMS server (mid-range enterprise, dual PSU, RAID-10 SSDs, 5-year warranty) | $25,000 |
| Backup tape library refresh + drive | $8,000 |
| UPS upgrade (server-room rack UPS) | $3,000 |
| Migration labour to move LMS to new server (one-off, in-house) | $15,000 |

### 3.2 Current recurring on-prem costs (per year)

These are the actual costs YAT incurs today for the LMS. Use these as the baseline for the on-prem option; if you propose changes to the on-prem operation, adjust with justification.

| Category | Item | Annual cost |
|---|---|---:|
| Software licensing | Windows Server Standard (per-server) | $1,500 |
| | Antivirus / EDR (server) | $300 |
| | Monitoring and management tooling | $2,000 |
| Power and facilities | Electricity for LMS server + cooling allocation | $1,200 |
| | LMS share of server-room rent / cooling allocation | $5,000 |
| | UPS battery replacement (amortised annually) | $500 |
| Backup | Tape media (annual consumption) | $1,500 |
| | Offsite tape storage service contract | $2,400 |
| | Backup software maintenance | $1,500 |
| Staff time (YAT ICT) | LMS administration, patching, monitoring (~0.20 FTE) | (apply $115k FTE rate) |
| | Incident response (~0.05 FTE) | (apply $115k FTE rate) |
| External support | Current MTS application support contract (existing engagement, ongoing) | $30,000 |

## 4. Cloud (Option B) — methodology guidance and research pointers

The cloud-side cost figures are **your work**. The points below are what YAT expects to see covered in your AWS option, and where to source the pricing data.

### 4.1 Categories your AWS option must include

At minimum, your AWS line items must cover:

- **Compute** — the EC2 instances (or equivalent compute) hosting the LMS web/application tier; include base capacity and any scaling/peak capacity assumptions.
- **Database** — the managed database service (per `internal-ha-database-requirements-S1-CL1-AT3.md` you are required to use AWS RDS Multi-AZ for MySQL or equivalent).
- **Network** — load balancer, NAT gateway, data transfer.
- **Storage** — EBS volumes, S3 for LMS attachments, AWS Backup or equivalent.
- **Monitoring** — CloudWatch metrics, logs, alarms.
- **Support tier** — AWS Business Support (or higher) is required to meet the 1-hour severity-1 response SLA in `internal-lms-cloud-migration-requirements-S1-CL1-AT1.md`.

### 4.2 One-off project costs you must include for the cloud option

The one-off project costs split across **three cost-bearers**. Your CBA must include line items for each — totalled together they are the Year-1 outlay for Option B.

**MTS-priced (one-off):**

- MTS consulting labour to design, build, HA-harden, and hand over the cloud infrastructure (the AT2 + AT3 consulting work end-to-end)

**YAT-internal (one-off) — handled by YAT IT in-scenario:**

- **Project oversight + acceptance** — YAT ICT staff time during the migration project (requirements coordination, attendance at MTS milestone meetings, acceptance testing of the infrastructure handover). Indicative: ~0.30 FTE × 6 months
- **LMS application deployment** — YAT IT effort to install the DOODLE LMS application onto the new AWS infrastructure once MTS hands it over. Indicative: ~80–120 hours
- **Data migration** — YAT IT effort to extract the MySQL database from the on-prem LMS and load it into AWS RDS, including data transformation and post-migration verification. Indicative: ~60–100 hours
- **Cutover** — parallel running of on-prem and cloud during the transition window (~1–2 months of dual-running infrastructure cost), DNS switch, user redirection, post-cutover incident response ramp. Indicative effort: ~40–60 hours plus the parallel-running infrastructure cost
- **Organisational change management** — Change Advisory Board (CAB) process per YAT's documented change-management procedure, end-user communications (staff + students), training collateral preparation and delivery, post-cutover support ramp. Indicative: ~80–120 hours of YAT ICT + Administrative staff time
- **Decommissioning** — on-prem LMS server hardware retirement, secure data destruction (per Privacy Act / records management obligations), facility reclamation. Indicative: ~$2,500 in materials + ~16 hours of YAT ICT time

Apply the $115k/FTE/year rate from §2 to convert FTE-fractions and hours to dollars (1 FTE-year ≈ 1,820 productive hours).

### 4.3 Out-year operational cost changes you should consider

If you migrate to cloud, several recurring on-prem cost lines should reduce or disappear (electricity, server-room rent allocation, tape media, offsite tape storage, on-prem-server-specific staff time). Other cost lines may change (MTS support contract — typically reduced because managed services reduce app-support burden, but justify your assumption).

### 4.4 Sources for cloud pricing data

- **AWS Pricing Calculator** — [https://calculator.aws](https://calculator.aws) — the canonical place to build your sized estimate. Generate an estimate, export it, attach to your CBA submission as evidence of your figures.
- **AWS service pricing pages** — [https://aws.amazon.com/pricing/](https://aws.amazon.com/pricing/) — per-service pricing detail. Use Australia (`ap-southeast-2`) prices per the data-residency requirement in `internal-privacy-policy.md`.
- **AWS Reserved Instance / Savings Plan documentation** — if you propose reserved/savings-plan pricing instead of on-demand, cite the term length and the discount you've applied. Document the trade-off.

## 5. Indirect benefit lines you must consider

The dollar comparison alone is not the full picture. Your CBA submission must also quantify (or at least narratively address) the following indirect benefits:

- **Avoided downtime cost.** At the target 99.9% availability vs the current 99.2%, the avoided downtime is ~61 hours per year. Apply the $750/hour indicative figure (during teaching hours) — note your assumption about how much of that 61 hours falls during teaching hours.
- **Capacity for student growth.** The 15% annual student growth requires capacity headroom in either option. State how each option handles this.
- **Capacity for assessment-week peaks.** The LMS sees ~3× concurrent load during the two-week assessment submission windows each term. State how each option handles this.
- **Staff capability development.** The case study notes YAT ICT staff lack cloud experience. State the implications for either option.
- **Other intangibles** — vendor lock-in, sustainability, cyber security maturity, disaster recovery (whole-campus loss), data residency — surface those that are material to YAT's decision.

## 6. Submission requirements

Your CBA submission for AT1 must include:

1. The populated `ICTICT517_Cost Benefit Analysis template.xlsx` with line items, year-by-year projections, and totals for both options.
2. A short written narrative (1–2 pages) covering: your sizing assumptions for AWS, the source of your AWS pricing figures, sensitivity analysis around the key assumptions (especially MTS-support cost, staff-time reduction, RI discount), Year-1 cash-flow profile differences between the two options, intangible factors per §5, and your recommendation.
3. Supporting evidence — at minimum, an AWS Pricing Calculator export attached to the submission.

The CBA flows into your action plan: the option you recommend in the CBA becomes the basis for the prioritised changes you propose.