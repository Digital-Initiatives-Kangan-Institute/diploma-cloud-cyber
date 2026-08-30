# S1-CL3 Cloud Infrastructure Improvement — Consolidated UoC

> **STATUS: DRAFT.** Every assessable item (PC / FS / PE / KE / AC) from the two cluster units, quoted **verbatim** from the validated UoC transcriptions and tagged `[UNIT SECTION numbering]`. Items are organised under a **topic** structure that follows the engagement workflow (analyse → design/approve → deploy/test → finalise), with a **technical strand** (ICTCLD504) and a **leadership strand** (BSBXTW401) per phase. **The group-level *assessment ideas* are proposals — marked TBD per CLAUDE.md Rule 1.** The cluster uses a **three-AT individual → group → individual** division (AT1 individual Design — 504 el 1–2 / AT2 group Team Implementation — 401 el 1–4 / AT3 individual Implement — 504 el 3–4); see the assessment plan for the full structure and coverage map.

**Cluster units**

| Unit | Title | Primary contribution |
|---|---|---|
| ICTCLD504 | Improve cloud-based infrastructure | The technical improve-cycle — analyse architecture, design improvements (security/reliability/scalability/cost), deploy/monitor/test, finalise |
| BSBXTW401 | Lead and facilitate a team | The leadership overlay — plan team outcomes, coordinate, support, monitor team performance |

**The integrated cluster:** *lead a team to improve a cloud system's infrastructure.* The 504 improvement project is the work; 401 is how the student (as team leader) runs it.

**Item inventory**

| Unit | PC | FS | PE | KE | AC | Total |
|---|---|---|---|---|---|---|
| ICTCLD504 | 18 | 5 | 5 | 10 | 8 | 46 |
| BSBXTW401 | 16 | 3 | 5 | 10 | 2 | 36 |
| **Total** | **34** | **8** | **10** | **20** | **10** | **82** |

**Reference-tag format.** `[<UNIT> <SECTION> <numbering>]` — e.g. `[ICTCLD504 PC 1.1]`, `[ICTCLD504 FS Reading]`, `[BSBXTW401 PE 2]`, `[ICTCLD504 KE 4]`, `[BSBXTW401 AC 1]`. PCs keep their source numbering; FS uses the verbatim skill name; PE/KE/AC are numbered `1..N` in source order. KE items with nested sub-bullets are quoted as one item (parent + children) under the parent's tag.

---

## Topic & assessment structure

The cluster organises into **four workflow phases**, each with a **technical group** (504) and a **leadership group** (401), plus cross-cutting foundation skills and assessment conditions. The same phases structure both teaching and assessment.

| Phase / Topic | Groups | Units | Assessment (AT — mode) |
|---|---|---|---|
| **1. Analyse & Plan** | G1 (analyse architecture), G2 (plan team outcomes) | 504, 401 | **AT1** (G1 — individual analysis) + **AT2** (G2 — team plan) |
| **2. Design & Approve** | G3 (design/improve + present + sign-off), G4 (coordinate team) | 504, 401 | **AT1** (G3 — design + sign-off) + **AT2** (G4 — coordinate/allocate) |
| **3. Deploy, Test & Support** | G5 (deploy/monitor/test), G6 (support team) | 504, 401 | **AT3** (individual, G5) + **AT2** (group, G6) |
| **4. Finalise & Review** | G7 (finalise improvements), G8 (monitor team performance) | 504, 401 | **AT3** (individual, G7) + **AT2** (group, G8) |
| **Cross-cutting** | G9 (foundation skills), G10 (environment & resource access), G11 (assessor requirements) | 504, 401 | both / environment / institutional |

**AT deliverables (three ATs — individual → group → individual; see the assessment plan §3):**
- **AT1 — Design** *(individual; 504 el 1–2)* — the Solution Design: **individually analyse** the baseline (review, business-impact, the compliance assessment against the Indian Regulatory Requirements, options) and design the improvement across security/reliability/scalability/cost, then document and present it and obtain **sign-off to proceed to deployment** (`[ICTCLD504 PC 2.4]` / `[ICTCLD504 PC 2.5]`, FS oral). No team leadership — that is AT2.
- **AT2 — Team Implementation** *(group; 401 el 1–4)* — lead the team that builds the approved design: author the team plan and **allocate one infrastructure component per member**, then coordinate / support / monitor the team as it writes and integrates the CloudFormation across individually-led meetings, to a team sign-off. The IaC write is the leadership vehicle — it is **not** 504-assessed (that is ICTCLD505, CL2).
- **AT3 — Implement** *(individual; 504 el 3–4)* — deploy the baseline and apply the approved improvement as a CloudFormation **change-set**, monitor / test / demonstrate it against the metrics, apply short-term refinements, document the as-deployed result + long-term strategy, and obtain **final sign-off** (`[ICTCLD504 PC 4.3]`).

**Two approval moments (UoC-faithful):** end of **AT1** = sign-off to proceed to deployment (`[ICTCLD504 PC 2.5]`); end of **AT3** = final sign-off (`[ICTCLD504 PC 4.3]`). *(AT2 also carries its own internal team sign-off on the completed build.)*

**Vehicle (per `scenario-flow.md`):** **Ledgerline** (the Accounting system), single-AZ cloud — the system whose cloud infrastructure is improved. CL3 **assesses on Ledgerline**; the **website is the practice vehicle**. *`[ICTCLD504 KE 6]` (object storage for static web sites) is evidenced as a **contextual knowledge question** in AT1's design knowledge — the student contrasts Ledgerline with an object-storage-dependent system (e.g. a website) and explains how they would provision that storage if needed.*

**Cross-cutting & delivery environment.** G9 (foundation skills) is co-evidenced inside both ATs' deliverables; G10 (environment & resource access) is provided by the scenario site + AWS Academy labs; G11 (assessor requirements) is the institutional assessor condition.

---

# Topic 1 — Analyse & Plan → AT1 (analyse, G1) + AT2 (plan team, G2)

Analyse the system (AT1) and set the team up (AT2) before designing changes.

## Group 1 — Analyse cloud architecture (ICTCLD504, element 1)

**Why grouped:** the opening of the improve-cycle — review the existing architecture, evaluate it and its business impact, weigh options against the business model, and set the improvement goals.

**Assessment:** an **individual** architecture analysis of the supplied baseline (Ledgerline's current single-AZ cloud infrastructure) — review, business-impact evaluation, the compliance assessment against the Indian Regulatory Requirements, options, and the security / reliability / scalability / cost goals + metrics. This is the analysis half of **AT1** (the individual Solution Design), so the holistic element-1 evidence (PC 1.1, PC 1.6) is valid per student; it feeds the design (G3, also AT1).

- 1.1 Identify and review business’s cloud architecture design [ICTCLD504 PC 1.1]
- 1.2 Evaluate cloud architecture and identify business impact of design decisions [ICTCLD504 PC 1.2]
- 1.3 Identify design patterns and architectural options [ICTCLD504 PC 1.3]
- 1.4 Determine and assess benefits and differences of cloud computing and architectural design against current business model and needs [ICTCLD504 PC 1.4]
- 1.5 Confirm system design decisions according to business needs [ICTCLD504 PC 1.5]
- 1.6 Set business goals as they relate to security, reliability, high-performance and cost efficiencies of cloud architecture according to business requirements and needs [ICTCLD504 PC 1.6]
- assess, identify and improve cloud architecture on a cloud platform, according to design decisions [ICTCLD504 PE 1]
- determine performance metrics and business goals [ICTCLD504 PE 3]
- industry technology standards used in cloud computing solutions and services [ICTCLD504 KE 1]
- industry standard hardware and software products, their general features, capabilities and application [ICTCLD504 KE 2]
- methods and impacts of cloud adoption as they relate to IT system changes [ICTCLD504 KE 3]

## Group 2 — Plan team outcomes (BSBXTW401, element 1)

**Why grouped:** setting the team up for the engagement — common objectives, performance expectations, accountability, and contingency planning.

**Assessment idea (TBD):** a team plan for the improvement engagement — objectives/responsibilities, per-member performance expectations and accountability, and contingencies.

- 1.1 Identify common objectives of workplace team, responsibilities and required outcome(s) [BSBXTW401 PC 1.1]
- 1.2 Use performance plans to establish expected outcomes, goals, and behaviours for individual team members in accordance with team objective and relevant policies [BSBXTW401 PC 1.2]
- 1.3 Select appropriate strategies to ensure team members are accountable for their roles and responsibilities [BSBXTW401 PC 1.3]
- 1.4 Plan for contingencies that could impact the team [BSBXTW401 PC 1.4]
- organisational requirements relevant to workplace teams: [BSBXTW401 KE 1]
  - workplace policies
  - codes of conduct
  - organisational reputation and culture
- legislative requirements relevant to the workplace [BSBXTW401 KE 2]
- typical workplace contingencies that can impact teams: [BSBXTW401 KE 9]
  - unplanned leave or absence of workers
  - re-allocation of work tasks
  - succession planning for important team roles

---

# Topic 2 — Design & Approve → AT1 (design/approve, G3) + AT2 (coordinate, G4)

Design the improvements, allocate the work, and get approval to deploy.

## Group 3 — Design and improve architecture (ICTCLD504, element 2)

**Why grouped:** the design half of the improve-cycle — confirm performance metrics, select and improve the resource tiers, improve for security/reliability/scalability/cost, then document, present and obtain sign-off to deploy.

**Assessment idea (TBD):** an improvement design (the proposed architecture) with performance metrics + the security/reliability/scalability/cost improvements, documented and presented for deploy sign-off.

- 2.1 Evaluate and confirm performance metrics for business applications according to business needs [ICTCLD504 PC 2.1]
- 2.2 Select and improve compute, storage, database and network resources according to business needs [ICTCLD504 PC 2.2]
- 2.3 Review and improve architecture required to enhance security, reliability, scalability and cost optimisation [ICTCLD504 PC 2.3]
- 2.4 Document and present proposed architecture for review to required personnel [ICTCLD504 PC 2.4]
- 2.5 Obtain sign off to proceed to deployment with required personnel [ICTCLD504 PC 2.5]
- design principles for cloud applications [ICTCLD504 KE 4]
- migrating principles for cloud applications [ICTCLD504 KE 5]
- use of object storage for static web sites [ICTCLD504 KE 6]
- tools and uses of security layers and security-focused content within cloud services [ICTCLD504 KE 8]
- features of cloud services, including techniques to improve security, reliability, scalability and costs [ICTCLD504 KE 9]

## Group 4 — Coordinate the team (BSBXTW401, element 2)

**Why grouped:** running the team through the design phase — communicate objectives, allocate tasks with instruction, facilitate respectful collaboration across diverse members, and find cross-collaboration opportunities.

**Assessment idea (TBD):** task allocation + communication of the engagement objectives to the (simulated) team, with respectful collaboration and cross-team opportunities evidenced.

- 2.1 Communicate common team objectives and responsibilities to team members [BSBXTW401 PC 2.1]
- 2.2 Allocate tasks to team members based on staff expertise or development potential and provide appropriate instructions [BSBXTW401 PC 2.2]
- 2.3 Facilitate open and respectful communication and collaboration between team members, considering the needs of those from diverse backgrounds [BSBXTW401 PC 2.3]
- 2.4 Identify opportunities for cross collaboration amongst external and internal teams and individuals [BSBXTW401 PC 2.4]
- assign tasks to team members with appropriate instruction and considering any required contingencies [BSBXTW401 PE 1]
- facilitation techniques to encourage team cohesion and effectiveness [BSBXTW401 KE 3]
- different methods and styles of communication [BSBXTW401 KE 6]
- key principles of cross-cultural communication and communication with individuals with special needs or disabilities [BSBXTW401 KE 7]

---

# Topic 3 — Deploy, Test & Support → AT3 (deploy/test) + AT2 (team support)

Deploy the approved improvements, prove them, and support the team through delivery.

## Group 5 — Deploy, monitor and test (ICTCLD504, element 3)

**Why grouped:** the implementation half — deploy the approved architecture, monitor/measure against the metrics and goals, test and demonstrate the security/reliability/scalability/cost improvements, and apply short-term refinements.

**Assessment idea (TBD):** deploy the approved improvement to the lab, measure against the metrics/goals, test and demonstrate the improvements, and refine per results.

- 3.1 Deploy approved architecture on cloud platform [ICTCLD504 PC 3.1]
- 3.2 Monitor and measure architecture against performance metrics and business goals [ICTCLD504 PC 3.2]
- 3.3 Test and demonstrate security, reliability, scalability and cost optimisation of deployed resources [ICTCLD504 PC 3.3]
- 3.4 Apply short-term refinements to deployed resources according to test results [ICTCLD504 PC 3.4]
- deploy, test and measure at least one architecture design, against architecture principles, metrics and business goals. [ICTCLD504 PE 2]
- use cloud management consoles, software development kits or command line tools [ICTCLD504 PE 4]
- testing and debugging techniques, including techniques to avoid single point failures [ICTCLD504 KE 7]
- techniques, methods and industry standard metrics and business goals used to monitor performance of cloud resources. [ICTCLD504 KE 10]

## Group 6 — Support the team (BSBXTW401, element 3)

**Why grouped:** supporting the team through delivery — coaching to enhance culture, supporting individuals toward the goals, facilitating issue resolution, and problem-solving team/task/individual challenges.

**Assessment idea (TBD):** coaching/support records and an issue-resolution/problem-solving episode during the (simulated) delivery.

- 3.1 Provide coaching to staff to enhance workplace culture [BSBXTW401 PC 3.1]
- 3.2 Support individuals according to organisational requirements to work towards common team goals [BSBXTW401 PC 3.2]
- 3.3 Facilitate team to identify, brainstorm, report and resolve task related issues and inefficiencies [BSBXTW401 PC 3.3]
- 3.4 Use problem solving skills to deal with any team, task or individual challenges [BSBXTW401 PC 3.4]
- provide feedback and assistance to team members [BSBXTW401 PE 2]
- manage conflicts and challenges according to organisational requirements. [BSBXTW401 PE 5]
- mentoring and coaching techniques to support team members [BSBXTW401 KE 4]
- strategies for conflict resolution and negotiation [BSBXTW401 KE 5]
- professional behaviours to role model as a leader [BSBXTW401 KE 8]
- teamwork challenges relevant to performance evidence: [BSBXTW401 KE 10]
  - difficulties performing tasks
  - conflicts with clients or team members
  - potential risks or safety hazards
  - unethical or inappropriate behaviour.

---

# Topic 4 — Finalise & Review → AT3 (finalise) + AT2 (team review)

Close out the technical improvement and review team performance.

## Group 7 — Finalise improvements (ICTCLD504, element 4)

**Why grouped:** closing the technical work — document the as-deployed architecture and test results against the approved design, describe long-term improvement strategies, and obtain final sign-off.

**Assessment idea (TBD):** an as-deployed report (changes/improvements vs the approved design + test results), a long-term improvement strategy, and final sign-off.

- 4.1 Document as-deployed architecture and test results, and highlight changes and improvements from approved design [ICTCLD504 PC 4.1]
- 4.2 Describe long-term improvement strategies and their benefits as applied to deployed resources [ICTCLD504 PC 4.2]
- 4.3 Obtain final sign off from required personnel [ICTCLD504 PC 4.3]
- create documentation of deployment and testing steps. [ICTCLD504 PE 5]

## Group 8 — Monitor team performance (BSBXTW401, element 4)

**Why grouped:** the leadership close-out — measure performance against the work plans, give constructive feedback, identify development opportunities, and implement action plans for training needs.

**Assessment idea (TBD):** performance measurement against the plans, feedback records, collated team/individual performance, and development/action plans.

- 4.1 Measure team member performance against agreed work plans [BSBXTW401 PC 4.1]
- 4.2 Provide timely and constructive performance feedback to team members according to expected organisational standards [BSBXTW401 PC 4.2]
- 4.3 Identify specific learning and development opportunities to improve team and individual performance and behaviours [BSBXTW401 PC 4.3]
- 4.4 Implement action plans to address individual and team training needs [BSBXTW401 PC 4.4]
- collate feedback on individual and team performance [BSBXTW401 PE 3]
- identify and implement development opportunities for others [BSBXTW401 PE 4]

---

# Cross-cutting (not a topic)

## Group 9 — Foundation skills

**Why grouped:** the language/literacy/employment skills essential to performance, co-evidenced inside both ATs' deliverables and interactions (the marking guides note where each is naturally evidenced rather than assessing it separately).

ICTCLD504:
- **Oral communication** — Uses listening and questioning techniques to confirm requirements and articulate complex concepts<br>Presents proposed solutions to required personnel using appropriate industry language [ICTCLD504 FS Oral communication]
- **Reading** — Interprets complex technical and operational documentation to determine and confirm job requirements [ICTCLD504 FS Reading]
- **Writing** — Writes and edits code and technical data in a logical manner using required syntax and language [ICTCLD504 FS Writing]
- **Problem solving** — Uses a mix of intuitive and formal processes to identify key information and issues, evaluates alternative strategies, anticipates consequences and considers implementation issues and contingencies<br>Uses knowledge of context to address common problems in cloud computing applications and cloud-based environments [ICTCLD504 FS Problem solving]
- **Self-management** — Demonstrates a sophisticated knowledge of principles, concepts, language and practices associated with cloud computing and the digital world and uses them to troubleshoot and understand the uses and potential of new technology [ICTCLD504 FS Self-management]

BSBXTW401:
- **Interact with others** — Uses appropriate communication practices when communicating with team members and facilitating activities<br>Establishes and builds relationships and rapport with team members to foster a positive team environment<br>Recognises the perspectives of team members and diversity of opinion, and manages conflict as required [BSBXTW401 FS Interact with others]
- **Navigate the world of work** — Understands and explains ethical and legal, regulatory and organisational responsibilities to team [BSBXTW401 FS Navigate the world of work]
- **Get the work done** — Plans, organises and implements work activities in line with organisational policies and procedures [BSBXTW401 FS Get the work done]

## Group 10 — Assessment conditions: required environment & resource access

**Why grouped:** the Assessment Conditions "access to" requirements — the simulated/working environment, tooling and reference materials the assessment must provide. Provided by the scenario website + AWS Academy labs; defines the delivery environment rather than mapping to a marking criterion.

ICTCLD504:
- cloud vendor service provider [ICTCLD504 AC 1]
- cloud managed database service [ICTCLD504 AC 2]
- cloud management console, software development kit or command line tools [ICTCLD504 AC 3]
- integrated development environment (IDE) [ICTCLD504 AC 4]
- specific requirements and industry standards, organisational procedures and legislative requirements, including business and functionality requirements, as required [ICTCLD504 AC 5]
- internet and web browser [ICTCLD504 AC 6]
- secure shell (SSH) or remote desktop protocol (RDP) client to connect to cloud-hosted instances. [ICTCLD504 AC 7]

BSBXTW401:
- A safe working or simulated environment [BSBXTW401 AC 1]

## Group 11 — Assessment conditions: assessor requirements

**Why grouped:** the identical trailing Assessment Conditions clause in each unit — assessor competency/qualification requirements. Institutional boilerplate, common to both units.

**Assessment idea (TBD):** satisfied by the institution's assessor-qualification policy; no AT artefact required.

- Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards. [ICTCLD504 AC 8]
- Assessors of this unit must satisfy the assessor requirements in applicable vocational education and training legislation, frameworks and/or standards. [BSBXTW401 AC 2]
