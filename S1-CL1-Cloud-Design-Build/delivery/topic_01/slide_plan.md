# Topic 1 — Cloud literacy · Slide plan

*The single source for this Topic's teaching + exercise slides, in deck order. (Pairs with `coverage.md`, the UoC/AT spec.)*

**Depth ceiling.** Topic 1 teaches only the cloud literacy AT1 Appendix 2 **Q1–Q5** tests — *recognise / explain / classify*, not build. Components map to the appendix: **C1→Q2, C2→Q1, C3→Q4, C4→Q3, C5→Q5.**

**How to build the single deck:** walk this file top-to-bottom. Each line is one slide, in final order.
- **`[AWS Mx Sy]`** — copy slide `y` from Module `x` (in `source_slides/`).
- **`[BESPOKE]`** — create the slide from the content block beneath it.
- **`[EX]`** — an exercise slide (teach the component, then its exercise, then the next component).

Bespoke exercises run on the **practice system (YAT Accounting System / Ledgerline)**; the AT does the same on the LMS. Decks this Topic **owns** (kept in `source_slides/`): ACF **M1, M2, M3, M9**.

---

### Opener

- **`[BESPOKE]`** Topic framing
```
Topic 1 — Cloud literacy
Enough cloud to write the Business Case — not to build anything (yet)
- You're an MTS consultant; before weighing "renew on-prem vs move to cloud" you
  need to speak cloud: models, building blocks, standards, pricing.
- Goal: answer Business Case Appendix 2 Q1–Q5, and reason about options + cost.
  Building these services is AT2.
```

- **`[BESPOKE]`** Practice system sketch (referenced by every exercise below)
```
We'll practise on the YAT Accounting System (Ledgerline), in AWS:
  Internet → ALB → EC2 / Auto Scaling Group (Ledgerline app, Windows Server)
          → RDS for SQL Server   (+ S3 for scanned invoices/POs, CloudWatch)
In the assessment (AT1) you'll do the same on the LMS — different system, same skills.
```

- **`[EX] [BESPOKE]`** Orientation — get to know YAT (on the intranet)
```
Open the YAT intranet and find your way around. Answer:
  1. What kind of organisation is YAT — what it does, roughly how big?
  2. What does YAT already use in the cloud today?
  3. What is Ledgerline (the Accounting System) used for, and who relies on it?
  4. Where does Ledgerline run today, and on what infrastructure?
  5. What availability does the business expect of it?
~10 min, then share. Purpose: orient students in their working environment +
seed the org context every later justification leans on.
Indicative: small VET RTO, Cremorne VIC · Office 365/SaaS already in use ·
accounting+office-admin for finance/admin staff · on-prem ageing server ·
business-hours, ~99.5% target.
```

---

### C1 — Cloud fundamentals & deployment models  *(→ Q2)*

- `[AWS M1 S05]` What is cloud computing?
- `[AWS M1 S06]` Cloud computing defined (pay-as-you-go)
- `[AWS M1 S07]` Infrastructure as software
- `[AWS M1 S11]` Cloud deployment models (public / private / hybrid / on-prem)
- **`[BESPOKE]`** Deployment models — YAT framing
```
The cluster's decision = move an on-prem system INTO public cloud.
YAT today is hybrid: on-prem servers + Office 365 (SaaS). Know the other models
as context; the decision here is on-prem vs public cloud.
```
- **`[EX] [BESPOKE]`** *(Q2 form)*
```
For the Accounting System sketch: which deployment model is it, and why is that the
right fit for YAT? (one short paragraph)
```

---

### C2 — Service models: IaaS / PaaS / SaaS  *(→ Q1)*

- `[AWS M1 S10]` Cloud service models — IaaS / PaaS / SaaS
- **`[BESPOKE]`** The "who manages what" decision lens
```
IaaS (e.g. EC2)        you manage OS + app — use to preserve an existing stack
PaaS (e.g. RDS, ALB)   provider runs the platform — use to offload ops when cloud skills are thin
SaaS (e.g. Office 365) provider runs everything — you just use it
Choosing = control vs operational burden. Classify each part of a solution, and say why.
```
- `[AWS M1 S13]` Cloud concepts — Section 1 key takeaways
- **`[EX] [BESPOKE]`** *(Q1 form)* — classify familiar/described services (no AWS knowledge needed; C3 attaches the AWS names later)
```
For each, name the service model + why:
  1. Office 365                                              → SaaS
  2. A VPS that comes with an OS, that you configure + run   → IaaS
  3. A service to rent compute+memory + install your own OS  → IaaS
  4. A managed database (provider runs/patches/backs up the
     engine; you just connect your app + store data)        → PaaS
Discriminator: "do YOU manage the OS?" yes → IaaS. Items 2 & 3 are both IaaS
despite sounding different.
```
- `[EX] [AWS M1 S43]` Knowledge check (cloud concepts) — *optional formative*

---

### C3 — Core AWS services: name + role  *(→ Q4)*

- `[AWS M1 S24]` What is AWS?
- `[AWS M3 S08]` Selecting a Region (data governance / residency)
- `[AWS M3 S09]` Availability Zones
- `[AWS M3 S16]` AWS categories of services
- `[AWS M3 S18]` Compute category (EC2, EC2 Auto Scaling)
- `[AWS M3 S17]` Storage category (EBS, S3)
- `[AWS M3 S19]` Database category (RDS)
- `[AWS M3 S20]` Networking & content delivery (VPC, Elastic Load Balancing)
- **`[BESPOKE]`** The multi-tier web workload pattern
```
        Internet → ALB → EC2 / Auto Scaling Group → RDS   (+ S3, CloudWatch)
- ALB (PaaS) distributes traffic    - EC2+ASG (IaaS) app tier, scales with demand
- RDS (PaaS) managed database       - S3 object storage; EBS block disks; CloudWatch monitoring
Same shape underlies BOTH the LMS and the Accounting system. You'll BUILD it in AT2;
here, just name each piece + its role.
```
- `[EX] [AWS M3 S24–S26]` Management Console clickthrough (classify services by category; has answer key)
- **`[EX] [BESPOKE]`** *(Q4 form)*
```
For the Accounting System sketch, name each AWS service and its general feature / role
in one line each.
```
- `[EX] [AWS M3 S29]` Knowledge check — *optional*

---

### C4 — Industry technology standards  *(→ Q3)*

- `[AWS M9 S06]` What is the AWS Well-Architected Framework?
- `[AWS M9 S07]` The six pillars *(flag Reliability — backbone of AT3)*
- **`[BESPOKE]`** Standards that inform a migration — name the right one for the decision
```
NIST SP 800-145        defines IaaS/PaaS/SaaS         → §6 service-type choices
AWS Well-Architected   6 pillars (incl. Reliability)   → design + §10 methods
ISO/IEC 27017          cloud security controls          → §8 security
ACSC Essential Eight   AU baseline cyber mitigations    → §10 controls
ITIL 4                 service management               → change-management alignment
```
- `[EX] [AWS M9 S15–S40]` Well-Architected Design Principles activity (pillar breakouts) — *optional, large; can run just the Reliability + Cost breakouts*
- **`[EX] [BESPOKE]`** *(Q3 form)*
```
Match each migration decision (service-type choice · security controls · change-mgmt
alignment · the HA approach · defining IaaS/PaaS/SaaS) to the standard that informs it.
One line each on why.
```
- `[EX] [AWS M9 S63]` Knowledge check — *optional*

---

### C5 — Cloud cost models & economics  *(→ Q5)*

- `[AWS M2 S05]` AWS pricing model — 3 cost drivers (compute / storage / data transfer)
- `[AWS M2 S06]` How do you pay for AWS? (pay-as-you-go · reserve · pay-less-as-you-grow)
- `[AWS M2 S08]` Pay less when you reserve — Reserved Instances
- `[AWS M2 S20]` AWS Pricing Calculator
- `[AWS M2 S21]` Reading an estimate
- **`[BESPOKE]`** Match the pricing model to the workload
```
Predictable baseline   → Reserved Instances
Variable / peak        → On-demand or autoscaling
Interruptible          → Spot (cheapest; not production baseline)
Storage / data         → pay-as-you-go (scales with usage)
So total cloud cost grows roughly with demand — the heart of the Topic 3 CBA.
Note: Accounting System carries SQL Server + Ledgerline LICENSING (BYOL vs licence-
included) — a cost factor the open-source LMS doesn't have.
```
- `[EX] [AWS M2 S22]` Pricing Calculator activity — **run on Accounting System specs** (also seeds the Topic 3 CBA) *(Q5 form)*
- `[EX] [AWS M2 S56]` Knowledge check — *optional*

---

### Close

- **`[BESPOKE]`** From literacy to the job
```
- You've practised classify / name / cost on the Accounting System.
- In AT1, the same is tested directly in Business Case Appendix 2 (Q1–Q5) and
  underpins your Options (§6), CBA (§7), and Strategic Alignment (§3).
```

---

## Build notes

- **Slide count:** ~22 teach + ~9 exercise (several exercise checks optional) + ~9 bespoke = a tight single deck. Drop the *optional* module knowledge checks if it runs long.
- **Owns vs borrows:** all four decks (M1, M2, M3, M9) are owned by Topic 1 and live in `source_slides/`. No borrowed decks.
- **Practice specs needed:** a one-page Accounting System sizing sheet for the M2 S22 calculator activity (users, data footprint, business-hours load) — draw from the Accounting docs on the YAT intranet.
- **Indicative answers** (trainer): IaaS = EC2/EBS; PaaS = RDS/ALB; S3 = object storage; Office 365 = SaaS but out of scope. Deployment model = public cloud. Standards per the C4 list. Cost models per the C5 teach.
- **Artefacts to publish (flag as we go):** some exercises may need a supporting artefact on the YAT website (e.g. the Accounting sizing sheet for the calculator activity) — note them here per exercise as they arise.
