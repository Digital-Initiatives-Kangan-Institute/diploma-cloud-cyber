# S1-CL1 Cloud Design and Build — Consolidated UoC

> **STATUS: DRAFT (Claude v1).** This is a consolidation of every Performance Criterion (PC), Foundation Skill (FS), Performance Evidence (PE), Knowledge Evidence (KE), and Assessment Condition (AC) from the three units in this cluster — ICTCLD401, ICTCLD502, ICTICT517 — quoted **verbatim** from the source UoCs and grouped where the items look like they could plausibly be covered by a single assessment item. Groupings, comments and assessment ideas are Claude's first-pass analysis. **No grouping or assessment idea here has been approved by Tim.** Treat everything as a proposal to react to.
>
> Every item carries a source reference tag — `[UNIT SECTION numbering]` (e.g. `[ICTCLD401 PC 1.2]`, `[ICTCLD502 KE 4]`). Tags are the foreign key back to the source `.md` files in `units_of_competency/`.
>
> Items not numbered in source (FS, PE, KE, AC) are numbered here in the order they appear in source.

---

## Source units

| Code | Title | Source file |
|---|---|---|
| ICTCLD401 | Configure cloud services | `units_of_competency/ICTCLD401_Complete_R1.md` |
| ICTCLD502 | Design and implement highly-available cloud infrastructure | `units_of_competency/ICTCLD502_Complete_R1.md` |
| ICTICT517 | Match ICT needs with the strategic direction of the organisation | `units_of_competency/ICTICT517_Complete_R1.md` |

---

## Group 1 — Cloud computing fundamentals: models, solutions, services, standards

**Why grouped:** all of these are "what is cloud computing, what models/services exist, what are the industry standards" knowledge/discussion items. 401 carries most of it; 502 echoes the standards/hardware items at a higher level.

**Assessment idea (TBD):** one written/questioning item — short-answer or scenario-driven — covering cloud models (IaaS/PaaS/SaaS, on-prem/private/hybrid/public), industry standards, and product comparison. Could double as the entry knowledge check for the cluster.

- 1.1 Discuss and compare different cloud computing solutions, models and services according to business requirements and needs [ICTCLD401 PC 1.1]
- 1.3 Select best cloud computing solution and service according to business requirements and needs [ICTCLD401 PC 1.3]
- industry technology standards used in cloud computing solutions and services [ICTCLD401 KE 1]
- industry standard hardware and software products, their general features, capabilities and application, including storage technology [ICTCLD401 KE 2]
- principles and functions of cloud computing solutions and technologies, including: [ICTCLD401 KE 3]
  - Infrastructure as a Service (IaaS)
  - Platforms as a Service (PaaS)
  - Software as a Service (SaaS)
- functions, uses and differences of cloud models, including: [ICTCLD401 KE 11]
  - on-premise and private cloud
  - hybrid cloud
  - public cloud.
- industry technology standards used in cloud computing solutions and services [ICTCLD502 KE 1]
- current industry standard hardware and software products, their general features, capabilities and application, including storage technology [ICTCLD502 KE 2]

---

## Group 2 — Shared security responsibility model

**Why grouped:** identical concept appears in both 401 and 502 PCs and is reinforced in 401's KE.

**Assessment idea (TBD):** one short scenario item ("here is a workload — what's the customer's responsibility, what's the vendor's?") satisfies all three references at once.

- 1.2 Identify impact of shared security responsibility models [ICTCLD401 PC 1.2]
- 1.7 Identify and assign security responsibilities according to security policies, business protocols and work function [ICTCLD401 PC 1.7]
- user, business and vendor responsibilities according to shared security responsibility models [ICTCLD401 KE 7]
- security policies, protocols and mechanisms as they relate to cloud technologies and methodologies including: [ICTCLD401 KE 9]
  - securities as it applies to limiting network traffic within virtual networks
  - security responsibilities as it applies to different work functions and user access
- 1.3 Identify level of shared security responsibility models according to business needs [ICTCLD502 PC 1.3]

---

## Group 3 — Identity, access, users, groups and permissions

**Why grouped:** all in 401, but they cluster naturally around "set up identity and access on the cloud platform so the workload can be built". Single hands-on lab exercise covers the lot.

**Assessment idea (TBD):** one observation item during the cluster build — student creates the account/IAM setup that the rest of the project's infrastructure depends on. Evidence is the working IAM configuration.

- 1.4 Access account on cloud platform according to business requirements and needs [ICTCLD401 PC 1.4]
- 1.5 Identify user access protocols and policies according to business requirements and needs [ICTCLD401 PC 1.5]
- 1.6 Configure access functions within cloud environment according to users, groups and required permissions [ICTCLD401 PC 1.6]
- 2.1 Create users and groups to create and manage infrastructure according to business requirements and needs [ICTCLD401 PC 2.1]
- user access protocols and policies according to organisation hierarchy and job function [ICTCLD401 KE 8]

---

## Group 4 — Workload and business-needs definition

**Why grouped:** small group — the act of pinning down what the workload actually is, before building anything. Sits between strategic context (517) and the technical build (401/502).

**Assessment idea (TBD):** part of the cluster's project brief — student documents the target workload and the business needs it serves. Same artefact feeds Group 6 and Group 8.

- 1.8 Define workload according to business requirements and needs [ICTCLD401 PC 1.8]
- 1.2 Determine cloud infrastructure according to business needs [ICTCLD502 PC 1.2]

---

## Group 5 — Cloud cost models and economics

**Why grouped:** both KEs about cloud cost — 401 covers the general comparison, 502 narrows to scaling-related cost.

**Assessment idea (TBD):** one written item — cost comparison applied to the cluster project (cloud vs non-cloud / scaled vs static). Possibly cross-link to 517 numeracy if a financial-impact calc is included.

- different cost models and cloud economic theories as they apply to different cloud services and non-cloud services, and benefits to each [ICTCLD401 KE 4]
- different cloud cost models as they relate to scalability of cloud infrastructure [ICTCLD502 KE 3]

---

## Group 6 — Virtual network build (the foundation infrastructure)

**Why grouped:** 401's entire Element 2 + Element 3 + its PEs + the related KEs are one coherent build exercise — virtual network, VMs, storage, managed DB, tested. This is the artefact that 502 then hardens for HA (Group 8).

**Assessment idea (TBD):** one extended project task — student builds the workload's virtual network end-to-end. Direct observation + the resulting configuration artefacts cover all of these in one go. The same network becomes the input to the 502 HA exercise, so this is the "spine" of the cluster build.

- 2.2 Create virtual multi-tier network to support core services and autoscaling [ICTCLD401 PC 2.2]
- 2.3 Create virtual machine according to business processing and operating system requirements [ICTCLD401 PC 2.3]
- 2.4 Define, add and expand storage on virtual machine according to business requirements and needs [ICTCLD401 PC 2.4]
- 2.5 Deploy a managed database within virtual network according to business requirements and needs [ICTCLD401 PC 2.5]
- 2.6 Test external network access and access between resources within virtual network and fix errors [ICTCLD401 PC 2.6]
- build at least one simple virtual network capable of supporting a workload using cloud services [ICTCLD401 PE 1]
- configure compute, storage, database and autoscaling resources within virtual network [ICTCLD401 PE 2]
- conduct simple tests to confirm access to resources. [ICTCLD401 PE 3]
- functions, features and uses of different virtual machine, networking and scaling options, including: [ICTCLD401 KE 5]
  - virtual machine sizing including CPU, memory, storage and network bandwidth
  - load balancing and autoscaling
  - performance monitoring and alarms
  - storage backups and lifecycle
  - virtual networks and traffic routing
- functions, benefits and differences of: [ICTCLD401 KE 6]
  - vertical and horizontal scaling
  - virtual and physical machines
  - relational, data warehouse and no SQL databases
  - self-hosted, managed and cloud-native database solutions
  - storage options including:
    - block storage
    - object storage
    - archive storage
    - network filesystems
- purpose of domain name system (DNS) required to connect remote servers when web browsing [ICTCLD401 KE 10]

---

## Group 7 — Autoscaling (configure, test, design for availability)

**Why grouped:** 401 configures and tests autoscaling; 502 designs autoscaling for HA; 502 KE 8 is the underpinning knowledge. Same student artefact, two assessment lenses.

**Assessment idea (TBD):** one task in the cluster project — student configures autoscaling on the workload's virtual network (401), then justifies it as part of the HA design (502). One implementation, two pieces of evidence.

- 3.1 Configure and apply autoscaling to virtual machines to scale according to business defined metrics [ICTCLD401 PC 3.1]
- 3.2 Test automatic scaling and fix errors as required [ICTCLD401 PC 3.2]
- design and deploy automated infrastructure scaling for at least one business need [ICTCLD502 PE 2]
- purpose and features of load balancing and autoscaling as related to improve availability within cloud environment [ICTCLD502 KE 8]

---

## Group 8 — High-availability architecture (review, design, implement, simulate)

**Why grouped:** the core of 502 — the entire Elements 1–4 PCs, the HA-focused PEs, and most of the HA-focused KEs. Coherent multi-phase exercise: review a non-cloud reference architecture → design HA cloud equivalent → implement → simulate failure.

**Assessment idea (TBD):** one extended project task layered on top of the Group 6 virtual network — student reviews a supplied non-cloud architecture, redesigns it for HA in the cloud, implements the redesign, then runs failure-simulation tests. Single sustained artefact (architecture-review doc → design doc → implementation → simulation report) covers the whole group.

- 1.1 Determine reliability, recoverability and service levels required for application [ICTCLD502 PC 1.1]
- 2.1 Review architecture of traditional multi-tier web application in non-cloud environment and identify high availability requirements [ICTCLD502 PC 2.1]
- 2.2 Identify any single points of failure [ICTCLD502 PC 2.2]
- 2.3 Estimate recovery objectives for multi-tier web components and for overall architecture [ICTCLD502 PC 2.3]
- 2.4 Determine components that must scale vertically and the potential impact on system availability [ICTCLD502 PC 2.4]
- 2.5 Document architecture review findings according to business needs [ICTCLD502 PC 2.5]
- 3.1 Design equivalent architecture for high availability using cloud services [ICTCLD502 PC 3.1]
- 3.2 Identify and remove single points of failure as required [ICTCLD502 PC 3.2]
- 3.3 Estimate recovery objectives for each component and overall architecture [ICTCLD502 PC 3.3]
- 3.4 Determine components that must scale vertically and the potential impact on system availability [ICTCLD502 PC 3.4]
- 3.5 Document architecture design according to business needs [ICTCLD502 PC 3.5]
- 4.1 Implement architecture design in cloud environment [ICTCLD502 PC 4.1]
- 4.2 Demonstrate connectivity between resources at all tiers [ICTCLD502 PC 4.2]
- 4.3 Monitor and measure availability of resources [ICTCLD502 PC 4.3]
- 4.4 Simulate failures of component and confirm that infrastructure is fault tolerant [ICTCLD502 PC 4.4]
- 4.5 Simulate resizing components likely to impact performance and measure availability impact [ICTCLD502 PC 4.5]
- 4.6 Compare and document simulation findings according to documented design [ICTCLD502 PC 4.6]
- design and implement at least one fault tolerant cloud infrastructure on a cloud platform resilient to networking, compute, storage, database and data centre failures [ICTCLD502 PE 1]
- simulate failures of at least one component and demonstrate is fault tolerant. [ICTCLD502 PE 3]
- use cloud management console, software development kits or command line tools [ICTCLD502 PE 4]
- define, monitor and record resource availability in cloud environment, including: [ICTCLD502 PE 5]
  - reliability
  - recoverability
  - service levels
  - scalability.
- definitions, functions, features and uses of different cloud infrastructure resources as they apply in cloud architecture to high availability, including: [ICTCLD502 KE 4]
  - fault tolerance and single points of failure
  - reliability as defined by mean time to failure (MTTF), to repair (MTTR) and between failures (MTBF)
  - recoverability as measured by recovery time (RTO) and recovery point (RPO) objectives
  - service level agreements (SLAs)
  - vertical and horizontal scalability
- testing and debugging techniques, including techniques to avoid single point failures [ICTCLD502 KE 5]
- tools and techniques to measure availability impact [ICTCLD502 KE 6]
- features of cloud services, including differences between built-in fault tolerance and infrastructure designed for fault tolerance [ICTCLD502 KE 7]
- techniques, methods and industry standard metrics used to monitor performance of cloud resources. [ICTCLD502 KE 9]

---

## Group 9 — Strategic ICT alignment, gap analysis, action planning

**Why grouped:** all of 517's PCs and PEs and KEs sit together — it's a single strategic-evaluation flow (evaluate current → evaluate proposed changes → plan implementation).

**Assessment idea (TBD):** one organisation-scenario project — student receives a strategic plan + current ICT state, produces gap analysis, evaluates proposed changes, prioritises, builds an action plan. The strategic scenario can deliberately be *the same* scenario that frames the 401/502 technical work, threading 517 into the cluster narrative.

- 1.1 Analyse and document current strategic plan of organisation against industry environment and organisational objectives [ICTICT517 PC 1.1]
- 1.2 Determine and document current state of ICT systems and practices in organisation [ICTICT517 PC 1.2]
- 1.3 Compare strategic plan objectives and current state of ICT to determine ICT gaps, improvement opportunities, and proposed changes [ICTICT517 PC 1.3]
- 2.1 Evaluate impact of proposed changes to ICT systems and products against strategic objectives of organisation [ICTICT517 PC 2.1]
- 2.2 Evaluate the difficulty of implementing proposed changes to ICT systems and products [ICTICT517 PC 2.2]
- 2.3 Prioritise proposed changes to refine opportunities and assist in scheduling implementation [ICTICT517 PC 2.3]
- 3.1 Develop action plan to implement proposed changes including prioritised schedule and consistency with organisational policy and procedures [ICTICT517 PC 3.1]
- 3.2 Detail standards, targets and implementation methods in action plan [ICTICT517 PC 3.2]
- interpret a strategic plan and objectives of the organisation [ICTICT517 PE 1]
- evaluate the current state of ICT in the organisation [ICTICT517 PE 2]
- identify possible gaps and opportunities in ICT and evaluate organisational impact with reference to the strategic plan and the objectives [ICTICT517 PE 3]
- determine and prioritise proposed changes to meet organisational needs [ICTICT517 PE 4]
- evaluate the difficulty of implementing proposed changes [ICTICT517 PE 5]
- develop an action plan for implementation [ICTICT517 PE 6]
- Key sections of an action plan for ICT implementation projects [ICTICT517 KE 1]
- Methods of evaluation and planning approaches to technical problems and strategic objectives [ICTICT517 KE 2]
- Methods of evaluation of competing and complementary internal and external ICT systems and products [ICTICT517 KE 3]
- Current and emerging system and product trends and directions [ICTICT517 KE 4]

---

## Group 10 — Documentation, stakeholder feedback and sign-off (cluster closure)

**Why grouped:** the strongest cross-unit candidate. All three units conclude with a "document the work → seek feedback → get sign-off" cycle. The *content* of what's documented differs per unit, but the act of structured documentation + feedback + sign-off is one process.

**Assessment idea (TBD):** one consolidated documentation pack at the end of the cluster project — covering all three units' content streams — submitted to a "required personnel" / "superior" role-played by the assessor, with a feedback round and a final sign-off. Single closure cycle, evidence against all three units.

- 4.1 Document and communicate work to required personnel [ICTCLD401 PC 4.1]
- 4.2 Seek and respond to feedback as required [ICTCLD401 PC 4.2]
- 4.3 Save and store user documentation according to organisational policies and procedures [ICTCLD401 PC 4.3]
- 5.1 Adjust and improve availability of architecture according to simulations as required [ICTCLD502 PC 5.1]
- 5.2 Confirm, seek and respond to feedback with required personnel [ICTCLD502 PC 5.2]
- 5.3 Obtain final sign off from required personnel [ICTCLD502 PC 5.3]
- 1.4 Report on proposed changes, gaps and improvement opportunities to superior [ICTICT517 PC 1.4]
- 2.4 Document evaluation process and provide to superior for feedback [ICTICT517 PC 2.4]
- 3.3 Provide action plan to superior for feedback and approval [ICTICT517 PC 3.3]

---

## Group 11 — Foundation Skill: Reading

**Why grouped:** all three units have a Reading FS. Words differ but the underlying capability — interpreting complex technical documentation — is the same and is exercised throughout the cluster project.

**Assessment idea (TBD):** evidenced implicitly across the cluster project (analysing UoCs, organisation documents, vendor docs). No dedicated assessment item; map to the project artefacts.

- **Reading** — Analyses and consolidates information and data from a range of sources against defined criteria and requirements, and checks for accuracy and completeness [ICTCLD401 FS Reading]
- **Reading** — Interprets complex technical and operational documentation to determine and confirm job requirements [ICTCLD502 FS Reading]
- **Reading** — Reviews, analyses and evaluates complex online and hard copy documentation containing ICT specific terminology, diagrams and numerical information to determine ICT gaps and improvement opportunities [ICTICT517 FS Reading]

---

## Group 12 — Foundation Skill: Writing

**Why grouped:** 401 and 517 both have Writing FS. (502 does not list Writing explicitly but does require documentation in Group 10.) Both exercised through the cluster's documentation pack.

**Assessment idea (TBD):** mapped to the documentation outputs in Group 10 — no dedicated item.

- **Writing** — Records required information and prepares documentation outlining work performed using appropriate language [ICTCLD401 FS Writing]
- **Writing** — Uses plain English, together with vocabulary, grammatical structures, terminology, diagrams, numerical information, formatting and structure relevant to the job role and organisation [ICTICT517 FS Writing]

---

## Group 13 — Foundation Skill: Oral Communication

**Why grouped:** 502 and 517 both have Oral Communication FS. (401 does not.) Both speak to articulating technical concepts to stakeholders.

**Assessment idea (TBD):** evidenced through stakeholder-feedback role-play in Group 10. No dedicated item.

- **Oral communication** — Uses listening and questioning techniques to articulate complex concepts and requirements using industry language for intended audience [ICTCLD502 FS Oral communication]
- **Oral Communication** — Uses plain English, translating technical terminology when necessary, to communicate with a range of personnel and determine objectives, articulate ideas and requirements, and develop plans<br>Elicits information using effective listening and questioning techniques [ICTICT517 FS Oral Communication]
  Elicits information using effective listening and questioning techniques

---

## Group 14 — Foundation Skills: planning, self-management, problem-solving, learning

**Why grouped:** a loose family of "manage yourself and your work" FSs that all three units carry under various names. Hard to assess discretely; evidenced through the whole cluster project's delivery.

**Assessment idea (TBD):** evidenced by completion of the cluster project to schedule and quality. No dedicated item; map to overall project delivery.

- **Learning** — Identifies ideas for other applications and considers them in current contexts [ICTCLD401 FS Learning]
- **Planning and organising** — Plans and implements routine tasks and workload, making limited decisions on sequencing, timing and collaboration, and seeks assistance in setting priorities [ICTCLD401 FS Planning and organising]
- **Self-management skills** — Makes low-impact decisions within familiar situations, based on a range of predefined or routine solutions, and evaluates effectiveness of outcome [ICTCLD401 FS Self-management skills]
- **Problem solving** — Uses a mix of intuitive and formal processes to identify key information and issues, evaluates alternative strategies, anticipates consequences and considers implementation issues and contingencies<br>Uses knowledge of context to address common problems in cloud computing applications and cloud-based environments [ICTCLD502 FS Problem solving]
  Uses knowledge of context to address common problems in cloud computing applications and cloud-based environments
- **Self-management** — Demonstrates a sophisticated knowledge of principles, concepts, language and practices associated with cloud computing and the digital world and uses them to troubleshoot and understand the uses and potential of new technology [ICTCLD502 FS Self-management]
- **Navigate the world of work** — Accepts responsibility and ownership for the task and makes decisions according to organisational needs and the need for coordination with others<br>Takes personal responsibility for following explicit and implicit policies, procedures and legislative requirements [ICTICT517 FS Navigate the world of work]
  Takes personal responsibility for following explicit and implicit policies, procedures and legislative requirements
- **Interact with others** — Selects and uses appropriate conventions and protocols when communicating with clients and colleagues in a range of work contexts<br>Recognises and accommodates basic differences and priorities of others<br>Cooperates with others and contributes to work practices where joint outcomes are expected and deadlines are to be met [ICTICT517 FS Interact with others]
  Recognises and accommodates basic differences and priorities of others
  Cooperates with others and contributes to work practices where joint outcomes are expected and deadlines are to be met
- **Get the work done** — Accepts responsibility for planning and sequencing complex tasks and workload, negotiating key aspects with others and taking into account capabilities, efficiencies and effectiveness<br>Applies systematic and analytical decision making processes for complex and non-routine situations<br>Investigates new and innovative ideas as a means to continuously improve work practices and processes through consultation and formal and analytical thinking<br>Uses and investigates new digital technologies and applications to manage and manipulate data and communicate effectively with others in a secure and stable digital environment [ICTICT517 FS Get the work done]
  Applies systematic and analytical decision making processes for complex and non-routine situations
  Investigates new and innovative ideas as a means to continuously improve work practices and processes through consultation and formal and analytical thinking
  Uses and investigates new digital technologies and applications to manage and manipulate data and communicate effectively with others in a secure and stable digital environment

---

## Group 15 — Assessment Conditions: cloud platform and supporting tools

**Why grouped:** the practical-environment access items required by 401 and 502. Same lab environment satisfies both.

**Assessment idea (TBD):** single cluster lab/environment specification.

- cloud vendor service provider [ICTCLD401 AC 1]
- cloud managed database service [ICTCLD401 AC 2]
- internet and web browser [ICTCLD401 AC 3]
- cloud vendor service provider [ICTCLD502 AC 1]
- cloud managed database service [ICTCLD502 AC 2]
- integrated development environment (IDE) [ICTCLD502 AC 4]
- internet and web browser [ICTCLD502 AC 6]
- secure shell (SSH) or remote desktop protocol (RDP) client to connect to cloud-hosted instances [ICTCLD502 AC 7]

---

## Group 16 — Assessment Conditions: information / data sources for the scenario

**Why grouped:** all three units require access to scenario information (business requirements, organisational policies, current-state data). One scenario pack satisfies all.

**Assessment idea (TBD):** single cluster scenario document covering the workload's business context, organisational policies, current-state ICT description.

- data to gather information from to determine output and user requirements, including user access and business protocols. [ICTCLD401 AC 4]
- information and data sources required to design and implement cloud infrastructure [ICTCLD502 AC 3]
- specific requirements and industry standards, organisational procedures and legislative requirements, including business and functionality requirements, as required [ICTCLD502 AC 5]
- data to gather information from to determine output and user requirements, including user access and business protocols. [ICTCLD502 AC 8]
- Detailed information relating to a strategic organisation plan, objectives, and direction [ICTICT517 AC 2]
- Organisational policies and procedures relating to the implementation of ICT changes [ICTICT517 AC 3]
- Information on current ICT systems and practices in the organisation including operating systems, hardware, and security [ICTICT517 AC 5]

---

## Group 17 — Assessment Conditions: statutory assessor requirements

**Why grouped:** identical-in-substance statutory wording across all three units. Single statement covers them all.

**Assessment idea (TBD):** standard institutional assessor-qualification check; covered once at cluster level.

- Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards. [ICTCLD401 AC 5]
- Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards. [ICTCLD502 AC 9]
- Assessors of this unit must satisfy the assessor requirements in applicable vocational education and training legislation, frameworks and/or standards. [ICTICT517 AC 6]

---

## Ungrouped items

Items below do not fit cleanly into any of the above groups. Included for completeness as required.

- **Numeracy** — Interprets numerical data and applies mathematical calculations to assess the financial implications of introducing changes [ICTICT517 FS Numeracy]

  *Could weakly link to Group 5 (cost models) if the cluster project includes a financial-implications calculation; left ungrouped because it's an FS, not a KE/PC, and 401/502 don't carry an equivalent Numeracy FS.*

- A site where ICT needs and strategic directions of the organisation are coordinated [ICTICT517 AC 1]

  *517-specific environmental condition; no direct equivalent in 401/502.*

- Individual superior in the organisation [ICTICT517 AC 4]

  *517-specific role required for the unit's "provide to superior" PCs (1.4, 2.4, 3.3). 401/502 use "required personnel" rather than "superior", so the roles aren't identical even if the underlying need is similar.*

---

## Validation — completeness check

The validator at `/tmp/validate_consolidated_uoc.py` parses every reference tag in this document and checks each one against the expected inventory drawn from the three source UoCs.

Expected counts (from source `.md` files):

| UoC | PC | FS | PE | KE | AC | Total |
|---|---:|---:|---:|---:|---:|---:|
| ICTCLD401 | 19 | 5 | 3 | 11 | 5 | 43 |
| ICTCLD502 | 22 | 4 | 5 | 9 | 9 | 49 |
| ICTICT517 | 11 | 7 | 6 | 4 | 6 | 34 |
| **Total** | **52** | **16** | **14** | **24** | **20** | **126** |

Result: see validator output (run after this document was finalised).
