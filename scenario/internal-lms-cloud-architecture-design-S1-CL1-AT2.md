# YAT LMS Cloud Architecture — Baseline Design

**Document type:** Technical design — baseline cloud architecture for the YAT LMS migration
**Authored by (in-scenario):** MTS Senior Architecture Team, in consultation with YAT ICT
**Status (in-scenario):** Approved for implementation
**Relevant to:** S1-CL1 AT2

**UoC references this document supports as a scenario artefact:**
- [ICTCLD502 AC 3] information and data sources required to design and implement cloud infrastructure
- [ICTCLD502 AC 5] business and functionality requirements
- [ICTCLD401 PC 1.8] *(implements the workload defined in AT1 — referenced here)*

---

> **⚠️ AUTHORING NOTE (out-of-scenario) — not to be included in the final scenario artefact:**
>
> This is a **markdown scaffold** of the technical design content. To be production-ready as a scenario artefact for student download from the YAT intranet, the following extra work is required:
>
> 1. **Topology diagrams** — VPC layout, subnet structure, traffic flow, IAM model, autoscaling/load-balancing relationships. Likely tooling: draw.io / Lucidchart / similar.
> 2. **Formal design document layout** — convert to a presentable design document (consultancy-style cover sheet, version control, executive summary, signed-off-by section, professional formatting). Likely tooling: Word or LaTeX export, or a website-rendered page on the YAT intranet.
> 3. **Final design review pass** — sanity-check the technical specifics (instance types, region pricing, security group rules) against current AWS service catalogue at delivery time.
> 4. **TBD content gaps** — items marked `TBD` below need confirmation against delivery context.

---

## 1. Purpose and scope

This document specifies the **baseline AWS architecture** to be implemented by MTS as the first phase of the YAT LMS cloud migration. It translates the action plan approved at the end of the Business Case engagement into a concrete, implementable design.

**In scope (this design):**
- Production cloud foundation for the DOODLE LMS application
- All compute, networking, identity, storage, database, autoscaling, and monitoring components required to run the LMS as a multi-tier web workload in AWS
- Single-region, single-AZ deployment in `ap-southeast-2` (Sydney)

**Out of scope (this design):**
- High-availability hardening (Multi-AZ database, cross-AZ compute resilience, failover testing) — to be addressed in a follow-on HA design phase
- Disaster recovery to a second AWS region — follow-on phase
- DR runbook and tabletop testing — follow-on phase
- Application re-platforming (the LMS remains Windows Server 2016 + DOODLE + MySQL per the migration brief)

**Out of MTS scope entirely (handled by YAT IT — noted here so the design boundary is clear):**

Per `internal-lms-migration-role-brief-S1-CL1-AT1.md` § Scope of the MTS consulting engagement, the following activities are **YAT in-house IT's responsibility**, not MTS's. The MTS-built infrastructure must be ready to support them, but MTS does not execute them:

- **LMS application installation** — DOODLE LMS install on the EC2 instance(s) once handover is complete
- **Database migration** — extract from on-prem MySQL, load into AWS RDS (see §7.2 below — kept for engagement-wide visibility only)
- **Cutover** — DNS switch, parallel running, decommissioning, user redirection
- **Organisational change management** — CAB, end-user communications, staff and student training, post-cutover support ramp

This design therefore stops at *infrastructure ready for application deployment* — the EC2 instance is provisioned with the OS via AMI, the RDS instance is provisioned with an empty MySQL schema, the ALB is configured with placeholder health checks, but no application binaries or production data are placed on the infrastructure as part of the MTS build.

## 2. Design assumptions and constraints

| # | Assumption / Constraint | Source |
|---|---|---|
| A1 | Region must be `ap-southeast-2` (Sydney) for data residency | `internal-lms-application-spec-S1-CL1-AT1.md` §Data residency + `internal-privacy-policy.md` |
| A2 | LMS application stack is preserved: Windows Server 2016, MySQL, DOODLE LMS application | `internal-lms-migration-role-brief-S1-CL1-AT1.md` |
| A3 | Current data footprint ~178 GB, growing ~25 GB/year (course attachments + student submissions dominate) | `internal-lms-application-spec-S1-CL1-AT1.md` §Data stored |
| A4 | Concurrent users typical 200–300, peak 500–700 (assessment windows) | `internal-lms-application-spec-S1-CL1-AT1.md` §User population |
| A5 | All YAT student PII must remain within Australia | Privacy Act 1988, APP 8 |
| A6 | LMS authenticates via Active Directory; cloud build must preserve AD-LDAP integration over private network back to YAT campus AD | `internal-lms-application-spec-S1-CL1-AT1.md` §Authentication / SSO |
| A7 | This baseline is **not** HA. Achieving YAT's 99.9% availability target is deferred to the follow-on HA design phase. | Scoping decision |
| A8 | AWS Academy lab environments are the authorised build environment for this engagement | Cluster delivery context |

## 3. AWS account and region

- **AWS account:** as provisioned by the MTS-YAT engagement (AWS Academy lab environment for assessment-driven implementation).
- **Region:** `ap-southeast-2` (Sydney). No deployment outside Australian regions.
- **Availability Zone:** `ap-southeast-2a` for the baseline deployment. (AT3 HA work will introduce a second AZ.)

## 4. Identity and Access Management (IAM)

### 4.1 IAM groups and access pattern

| Group | Purpose | Indicative permissions |
|---|---|---|
| `YAT-ICT-Admins` | YAT internal ICT staff — day-to-day operations after handover | Read-only on infrastructure, full access to CloudWatch + RDS console + EC2 console (no IAM modifications) |
| `MTS-Consultants` | MTS personnel during build and ongoing support | Full administrative access during migration; reduced post-handover |
| `Application-Service` | EC2 instance role used by the LMS application itself | RDS read/write to LMS database; S3 read/write to attachments bucket; CloudWatch logs write |
| `Read-Only-Auditors` | YAT compliance + external auditors | Read-only on logs, metrics, configurations — no service mutations |

### 4.2 IAM principles

- Use AWS managed policies where available; custom inline policies only when no managed policy fits
- **MFA required** for all user accounts in `YAT-ICT-Admins` and `MTS-Consultants` (per ACSC Essential Eight + `internal-user-access-policy.md`)
- No long-lived access keys for human users; programmatic access via IAM roles only
- Resource access by EC2 instances via instance profile, not embedded credentials

**Configuration decision left to implementer:** specific permission boundaries on the `MTS-Consultants` group during build vs after handover.

## 5. Network topology

### 5.1 VPC

- **VPC CIDR:** `10.0.0.0/16` (private RFC1918 range, room for future expansion)
- **DNS hostnames + DNS resolution:** enabled
- **VPC flow logs:** enabled to CloudWatch Logs

### 5.2 Subnets (single AZ — `ap-southeast-2a`)

| Subnet | CIDR | Tier | Internet-facing? |
|---|---|---|---|
| `public-web-a` | `10.0.1.0/24` | Web / public load balancer | Yes |
| `private-app-a` | `10.0.11.0/24` | Application / LMS EC2 instances | No |
| `private-data-a` | `10.0.21.0/24` | Database (RDS) | No |

> AT3 HA hardening will add the corresponding `-b` subnets in `ap-southeast-2b`.

### 5.3 Gateways and routing

- **Internet Gateway** attached to the VPC for public-subnet traffic
- **NAT Gateway** in `public-web-a` for outbound internet from the private app subnet (e.g. for Windows Updates, package management)
- **Route tables:**
  - Public route table: default route to Internet Gateway; associated with `public-web-a`
  - Private app route table: default route to NAT Gateway; associated with `private-app-a`
  - Private data route table: no default route to internet; associated with `private-data-a`

### 5.4 Connectivity back to YAT campus (TBD)

The LMS must reach YAT's on-campus Active Directory for authentication. Two options:

- **Option (a) — Site-to-Site VPN** between YAT campus router and an AWS VPN Gateway. Lower setup cost; acceptable for AD-LDAP traffic.
- **Option (b) — AWS Direct Connect** dedicated link. Higher cost; consider only if VPN latency becomes a problem at scale.

**Baseline choice for this design: Option (a) Site-to-Site VPN.** Direct Connect deferred unless required by later performance assessment.

## 6. Compute layer

### 6.1 EC2 instances (LMS application tier)

- **Instance family:** general-purpose x86 (e.g. `m6i.large` or `m5.large` — see configuration decision below)
- **AMI:** Windows Server 2016 Datacentre (preserves current application stack per A2)
- **Placement:** `private-app-a` subnet only (no public IPs on application instances)
- **EBS root volume:** `gp3`, 100 GB
- **Additional EBS data volume:** `gp3`, sized to cover LMS application data + attachments — **configuration decision: implementer to compute size from the data footprint in `internal-lms-application-spec-S1-CL1-AT1.md` plus 12-month growth + 50% headroom**

### 6.2 Application Load Balancer (ALB)

- **Placement:** `public-web-a` (internet-facing)
- **Listener:** HTTPS:443 → forward to LMS target group
- **Target group:** EC2 instances in the Auto Scaling Group (see §6.3)
- **Health check:** HTTP GET against LMS health endpoint; 30 s interval; threshold 2 unhealthy → instance taken out of service
- **TLS certificate:** ACM-issued for the LMS DNS name (TBD — confirm DNS strategy with YAT ICT)

### 6.3 Auto Scaling Group (ASG)

- **Launch template:** as specified in §6.1
- **Capacity (baseline):** min=1, desired=1, max=2
- **Scaling policy:** target tracking on EC2 CPU at **70%** (configurable)
- **Health checks:** ELB + EC2
- **Cooldown:** 300 s

> AT3 HA hardening will expand ASG capacity (min=2, multi-AZ) and add a load-based scaling policy tuned to assessment-window peaks.

**Configuration decision left to implementer:** specific instance type from the general-purpose family, based on the workload sizing in the LMS application spec.

## 7. Database layer

### 7.1 RDS for MySQL

- **Engine:** Amazon RDS for MySQL (preserves current MySQL data + schema per A2)
- **Engine version:** **TBD** — confirm compatible MySQL version against the DOODLE application's supported matrix
- **Instance class:** general-purpose (e.g. `db.m6i.large` or `db.m5.large` — implementer selects based on workload)
- **Multi-AZ:** **disabled** (baseline only — AT3 HA hardening enables Multi-AZ)
- **Storage:** `gp3`, initial size sized to cover the LMS MySQL data footprint + 12-month growth — **configuration decision: implementer computes size**
- **Storage encryption:** enabled (AWS KMS, AWS-managed key acceptable for baseline)
- **Placement:** `private-data-a` subnet group
- **Public accessibility:** disabled
- **Backup retention:** 7 days, automated; backup window 22:00–04:00 AEST (aligns with current maintenance window per LMS app spec)
- **Maintenance window:** Sunday 02:00–06:00 AEST (preserved from current LMS maintenance window)

### 7.2 Schema migration *(out of MTS scope — YAT IT responsibility, noted here for completeness)*

> Per `internal-lms-migration-role-brief-S1-CL1-AT1.md` § Scope of the MTS consulting engagement, **data migration is YAT IT's responsibility**, not MTS's. MTS provisions the RDS instance per §7.1 above; YAT IT performs the schema/data load once the infrastructure is handed over.
>
> Documented here for engagement-wide visibility only — students must **not** perform data migration as part of AT2 build evidence.

Indicative approach YAT IT is expected to follow (subject to YAT IT's own change management):

1. Full mysqldump + restore during the cutover window, **OR**
2. AWS DMS continuous replication during a cutover-with-rollback period.

YAT IT's expected baseline choice: mysqldump + restore during a planned maintenance window. DMS reserved for if extended parallel-running is needed. Final method is YAT IT's call, not MTS's.

## 8. Storage

| Resource | Type | Purpose |
|---|---|---|
| EC2 root volume | EBS `gp3` 100 GB | OS + LMS application install |
| EC2 application data volume | EBS `gp3` (sized by implementer) | LMS application data, attachments staging |
| LMS attachments bucket | S3 (`yat-lms-attachments-<env>-<region>`) | Course attachments, student submissions, with lifecycle to S3 Glacier Deep Archive after 24 months |
| Backups bucket | S3 (`yat-lms-backups-<env>-<region>`) | Off-instance copies of mysqldump exports, application file snapshots |

**S3 settings (both buckets):**
- Block all public access
- Server-side encryption (SSE-S3 acceptable for baseline)
- Versioning enabled
- Access logging to a dedicated log bucket

## 9. Security

### 9.1 Security groups

| SG name | Inbound | Outbound |
|---|---|---|
| `sg-alb` | HTTPS:443 from `0.0.0.0/0` | HTTP/HTTPS to `sg-app` |
| `sg-app` | HTTP/HTTPS from `sg-alb`; RDP:3389 from MTS-Consultants bastion (TBD bastion design) | MySQL:3306 to `sg-db`; HTTPS to NAT Gateway for outbound updates; LDAP/LDAPS to YAT campus AD over VPN |
| `sg-db` | MySQL:3306 from `sg-app` only | none |

### 9.2 Encryption in transit

- ALB → EC2: HTTPS (LMS supports HTTPS application traffic)
- EC2 → RDS: TLS-protected MySQL connection
- All AWS service-to-service calls over TLS via VPC endpoints where available

### 9.3 Encryption at rest

- EBS volumes: enabled (default KMS key acceptable for baseline)
- RDS storage: enabled
- S3 buckets: SSE-S3

### 9.4 Shared security responsibility

This deployment operates under the **AWS Shared Responsibility Model**.

| Layer | Responsibility | Owner |
|---|---|---|
| AWS regions, AZs, hardware, hypervisor | "Security of the cloud" | AWS |
| Guest OS patching (Windows Server 2016) | "Security in the cloud" | YAT ICT (post-handover) + MTS support |
| Application configuration + LMS application security | "Security in the cloud" | YAT ICT |
| IAM users, groups, MFA, key management | "Security in the cloud" | YAT ICT |
| Data classification, access governance, audit | "Security in the cloud" | YAT |
| End-user device security | "Security in the cloud" | YAT + end users |

## 10. Monitoring baseline

### 10.1 CloudWatch metrics

Standard service metrics enabled for: EC2 (CPU, network, disk), RDS (CPU, connections, free storage, replication lag — N/A for single-AZ), ALB (request count, target response time, 5XX count), Auto Scaling (group capacity, scale events).

### 10.2 CloudWatch alarms (baseline only — HA-tuned alarms come in AT3)

| Alarm | Metric | Threshold | Action |
|---|---|---|---|
| EC2 CPU high | `AWS/EC2 CPUUtilization` ≥ 80% over 10 min | (sustained) | Notify; ASG scaling policy may have already acted |
| RDS CPU high | `AWS/RDS CPUUtilization` ≥ 80% over 10 min | (sustained) | Notify |
| RDS free storage low | `AWS/RDS FreeStorageSpace` < 15% | | Notify; trigger manual storage scale |
| ALB 5XX | `AWS/ApplicationELB HTTPCode_Target_5XX_Count` > 10/min | | Notify |
| RDS connections high | `AWS/RDS DatabaseConnections` > 80% of `max_connections` | | Notify |

### 10.3 Logging

- VPC flow logs → CloudWatch Logs (90-day retention)
- ALB access logs → S3 access-log bucket
- EC2 OS-level logs via CloudWatch Agent (Windows Event Log critical channels)
- RDS general + error logs → CloudWatch Logs

## 11. Naming and tagging conventions

### 11.1 Resource naming

Pattern: `yat-lms-<resource-type>-<env>-<az-or-purpose>` — e.g. `yat-lms-alb-prod`, `yat-lms-rds-prod`, `yat-lms-asg-prod`.

### 11.2 Mandatory tags

| Tag | Value | Required on |
|---|---|---|
| `Project` | `YAT-LMS-Migration` | All resources |
| `Environment` | `Production` | All resources |
| `Owner` | `YAT-ICT` | All resources |
| `ManagedBy` | `MTS-Migration` (during build); change to `YAT-ICT` post-handover | All resources |
| `CostCentre` | `YAT-LMS` | All resources |
| `DataClassification` | `Confidential` (anything touching student PII) or `Internal` | EBS, RDS, S3 buckets |

## 12. Backup baseline

| Resource | Mechanism | Retention | Restore-tested by |
|---|---|---|---|
| RDS database | Automated daily backups + transaction log retention | 7 days | AT2 connectivity testing |
| EC2 EBS volumes | Daily AMI snapshot via Data Lifecycle Manager | 14 days | (AT3 will test restore as part of HA validation) |
| LMS attachments (S3) | S3 Versioning + lifecycle to Glacier Deep Archive | Versioned; archive after 24 months | (handover testing) |
| Configuration / IaC | (TBD: IaC tooling choice — CloudFormation / CDK / Terraform / manual + Config drift detection) | n/a | n/a |

> Cross-Region backup copies are **out of scope** for this baseline and addressed in AT3 HA work.

## 13. Out of scope (deferred to follow-on HA design)

Listed explicitly so the implementer knows what *not* to build:

- Multi-AZ database
- Cross-AZ subnets (private-app-b, private-data-b)
- ASG capacity ≥ 2 across multiple AZs
- HA-tuned monitoring (e.g. cross-AZ latency, RDS replica lag)
- Cross-Region backup copies and DR runbook
- Failure-simulation testing
- Automated availability metric reporting (e.g. service-level dashboard against the 99.9% target)

These are the deliberate inputs into the **AT3 HA design exercise**.

## 14. Configuration decisions left to the implementer

The supplied design is intentionally **opinionated where it matters and silent where the implementer must demonstrate judgement**. Specifically:

| # | Decision | Why left open | Where to evidence the decision |
|---|---|---|---|
| C1 | Specific EC2 instance type within the general-purpose family | Implementer must size against the LMS workload | §5 Configuration decisions in the Deployment Report |
| C2 | Specific RDS instance class within the general-purpose family | Same | Deployment Report §5 |
| C3 | EBS application data volume size + RDS storage size | Implementer must compute from data footprint + growth | Deployment Report §5 |
| C4 | ASG scaling threshold within the recommended range | Implementer rationalises against expected CPU profile | Deployment Report §5 |
| C5 | Permission boundary policy specifics for `MTS-Consultants` | Implementer adapts to lab environment access scope | Deployment Report §5 |
| C6 | Bastion / jump-host design for RDP access into `sg-app` | Left for implementer | Deployment Report §5 |
| C7 | MySQL engine version | Implementer confirms against DOODLE compatibility matrix | Deployment Report §5 |
| C8 | DNS strategy + ACM certificate domain | Implementer confirms with YAT ICT for the LMS hostname (TBD) | Deployment Report §5 |

## 15. References

- `internal-lms-application-spec-S1-CL1-AT1.md` — workload, SLAs, data footprint, integration points
- `internal-lms-cloud-migration-requirements-S1-CL1-AT1.md` — SLA targets, RPO/RTO targets
- `internal-lms-migration-role-brief-S1-CL1-AT1.md` — engagement scope, OS/application preservation
- `internal-ict-environment-overview-S1-CL1-AT1.md` — current state to migrate from
- `internal-on-prem-network-diagram-S1-CL1-AT1.md` — current network topology
- `internal-privacy-policy.md` — Australian data residency
- `internal-user-access-policy.md` — MFA, RBAC, joiner/mover/leaver
- `internal-security-and-incident-response.md` — Essential Eight baseline
- `internal-industry-standards-reference.md` — applicable industry standards (AWS Well-Architected, ACSC Essential Eight, etc.)

---

## Document control (in-scenario)

| | |
|---|---|
| **Version** | 1.0 (Approved for implementation) |
| **Approved by (in-scenario)** | Pat Lin, MTS Senior Consultant · Sam Walker, YAT ICT Manager |
| **Date approved** | TBD |
| **Implementation phase** | AT2 (foundation build) |
| **Successor phase** | AT3 (HA hardening + project closure) |
