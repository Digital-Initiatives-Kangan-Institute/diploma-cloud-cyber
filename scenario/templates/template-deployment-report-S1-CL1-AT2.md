# YAT LMS Deployment Report — Template

**Document type:** Student-fillable template (downloadable from the YAT intranet Templates section)
**Status:** DRAFT (Claude v1, 2026-05-25). All section prompts + KE questions + reflection prompts are Claude-drafted — **TBD** confirm wording before issuing to students.

---

> **⚠️ AUTHORING NOTES (out-of-template) — not to be included in the student-facing artefact:**
>
> This `.md` is the **source-of-truth** for the deployment report template. It will need to be transferred to a Word document for student download from the YAT intranet (mirror of the AT1 BC template approach — which itself is still TBD as a downloadable file).
>
> **UoC traceability map** (which template section evidences which UoC item — used by assessor benchmark; not visible to students):
>
> | Template section / appendix | UoC items evidenced |
> |---|---|
> | §1 Executive Summary | [ICTCLD401 PC 4.1] — partial co-evidence (document + communicate work) |
> | §2 Engagement Context | [ICTCLD502 AC 3, AC 5] (scenario data sources used) |
> | §3 Scope of Deployment | (scopes the work — supports rest of report) |
> | §4 Build Narrative | [ICTCLD401 PC 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1] · [ICTCLD502 PC 1.3, 4.1, 4.2] |
> | §5 Configuration Decisions | [ICTCLD401 PC 1.3] (justified service selection) |
> | §6 Testing and Validation | [ICTCLD401 PC 2.6, 3.2] · [ICTCLD502 PC 4.2, 4.3 — partial] |
> | §7 Operational Handover | [ICTCLD401 PC 4.3] (save documentation per organisational policies) |
> | §8 Knowledge Evidence Responses | [ICTCLD401 KE 5, 6, 7, 8, 9, 10] |
> | Appendix A — Build Evidence | Screenshot-level evidence for the build PCs (cross-references §4) |
> | Appendix B — Configuration Exports | Configuration-level evidence for the build PCs (cross-references §4) |
> | Appendix C — Test Evidence | Test-result evidence for [ICTCLD401 PC 2.6, 3.2] · [ICTCLD502 PC 4.2, 4.3] |
> | Appendix D — Reflections | [ICTCLD401 FS Learning, FS Planning and organising, FS Self-management] |
>
> Foundation Skills evidenced through the report itself: [ICTCLD401 FS Reading, FS Writing].

---

## Cover sheet

| | |
|---|---|
| **Engagement** | YAT LMS Cloud Migration — Foundation Build Phase |
| **Engagement reference** | YAT-LMS-MIG-2026 |
| **Report version** | 1.0 |
| **Submitted by (consultant name)** | [Your name] |
| **Consultant role** | MTS Consultant |
| **Student ID** | [Your student ID] |
| **Date submitted** | [DD/MM/YYYY] |
| **Submitted to** | Sam Walker, YAT ICT Manager · Pat Lin, MTS Senior Consultant |

---

## §1 Executive Summary

*Provide a brief (≤ 1 page) summary of what was delivered in this phase of the engagement. Write this section last, after the rest of the report is complete.*

Cover at minimum:
- What was deployed (one sentence — the baseline cloud foundation for the YAT LMS)
- Region and AZ
- Top 2–3 highlights of the build
- Any limitations or items deferred to the HA hardening phase
- Confirmation that the engagement is ready for the HA design phase

*[Your executive summary here — approximately 250–400 words]*

---

## §2 Engagement Context

*Brief context for the reader. Reference the prior work this build is based on. Keep to ≤ ½ page.*

Cover:
- The strategic context: the board-approved action plan from the Business Case engagement (reference the YAT LMS Migration Business Case, version and date)
- The supplied technical design: the *YAT LMS Cloud Architecture — Baseline Design* document (version 1.0, approved by Pat Lin / Sam Walker)
- Your role: MTS consultant returning from planned leave to implement the architecture designed by MTS Senior Architecture in consultation with YAT ICT
- Scope hand-off: confirmation that HA hardening is the next phase (covered separately)

*[Your engagement context here]*

---

## §3 Scope of Deployment

*What is included in this build, and what is deferred. ≤ ½ page.*

Restate from the supplied design (in your own words):

- **In scope of this report:** the baseline cloud foundation — IAM, network, compute, database, autoscaling, storage, monitoring baseline
- **Out of scope (deferred to the HA hardening phase):** Multi-AZ database, cross-AZ resilience, failover testing, DR runbook, cross-Region backup copies, HA-tuned monitoring

*[Your scope statement here]*

---

## §4 Build Narrative

*Layer-by-layer account of what was built and how. This is the substantive technical section of the report. For each layer below, write a short narrative paragraph or two and cross-reference the relevant screenshots in Appendix A and configuration exports in Appendix B.*

### 4.1 AWS account access and Identity and Access Management

*Cover: how you accessed the AWS account; the IAM groups, users, roles you created; how MFA is enforced; the instance profile used by the LMS application. Cross-reference: Screenshots A1, A2, A3. Configuration exports: B1, B2.*

*[Your IAM narrative here]*

### 4.2 Network topology

*Cover: the VPC, subnets (public-web-a, private-app-a, private-data-a), Internet Gateway, NAT Gateway, route tables. Cross-reference: Screenshots A4, A5, A6, A7. Configuration exports: B3.*

*[Your network narrative here]*

### 4.3 Compute layer (EC2 + ASG)

*Cover: the EC2 launch template, instance type chosen and why, the Auto Scaling Group config (min/desired/max, scaling policy threshold). Cross-reference: Screenshots A8, A9, A14. Configuration exports: B4.*

*[Your compute narrative here]*

### 4.4 Load balancing (ALB)

*Cover: the Application Load Balancer configuration, target group, listener, health check. Cross-reference: Screenshot A13. Configuration export: B5.*

*[Your load balancing narrative here]*

### 4.5 Database layer (RDS)

*Cover: the RDS instance class chosen and why, engine version, storage sizing, encryption, backup retention. Cross-reference: Screenshot A12. Configuration export: B6.*

*[Your database narrative here]*

### 4.6 Storage (EBS + S3)

*Cover: EBS volumes (root + data) for the EC2 instance, S3 buckets (attachments, backups), encryption settings, block-public-access settings. Cross-reference: Screenshots A10, A11. Configuration exports: B7.*

*[Your storage narrative here]*

### 4.7 Security (security groups + encryption)

*Cover: the three-tier security group model (sg-alb, sg-app, sg-db), encryption in transit + at rest, your additions to the shared-responsibility model. Cross-reference: Screenshot A8. Configuration export: B2.*

*[Your security narrative here]*

### 4.8 Monitoring baseline (CloudWatch)

*Cover: which CloudWatch alarms you configured and the thresholds you chose. (Note: this is the baseline only — HA-tuned monitoring is in the next phase.) Cross-reference: Screenshot A17.*

*[Your monitoring narrative here]*

---

## §5 Configuration Decisions

*The supplied design left specific decisions to you. For each item below, state your decision and briefly justify it against the YAT LMS workload (refer back to the LMS Application Specification on the YAT intranet).*

| # | Decision point (from supplied design §14) | Your decision | Rationale |
|---|---|---|---|
| C1 | Specific EC2 instance type within the general-purpose family | *[Your choice]* | *[1–3 sentences referencing workload + cost]* |
| C2 | Specific RDS instance class within the general-purpose family | *[Your choice]* | *[1–3 sentences]* |
| C3 | EBS application data volume size + RDS storage size | *[Your sizing — show the calc]* | *[Reference to LMS data footprint + growth assumption]* |
| C4 | ASG scaling threshold | *[Your threshold]* | *[Reference to expected CPU profile]* |
| C5 | Permission boundary policy specifics for MTS-Consultants | *[Your boundary]* | *[Rationale]* |
| C6 | Bastion / jump-host design for RDP access | *[Your approach]* | *[Rationale]* |
| C7 | MySQL engine version | *[Your version]* | *[DOODLE compatibility rationale]* |
| C8 | DNS strategy + ACM certificate domain | *[Your approach]* | *[Rationale]* |

---

## §6 Testing and Validation

*Document the tests you ran to verify the build works as intended. For each test, state the test, the result, and reference the supporting evidence in Appendix C.*

### 6.1 Connectivity tests

*Verify network reachability across the tiers — ALB reaches EC2; EC2 reaches RDS; EC2 reaches the internet via NAT Gateway. Cross-reference: Test evidence C1, C2.*

| Test | Outcome (Pass/Fail) | Notes |
|---|---|---|
| ALB → EC2 health check | | |
| EC2 → RDS MySQL connection | | |
| EC2 → internet via NAT (Windows Update reachability) | | |
| RDS → no public reachability (negative test) | | |

### 6.2 Autoscaling test

*Trigger a scaling event (e.g. by load-generating against the ALB) and confirm the ASG responds. Cross-reference: Test evidence C3.*

| Step | Outcome | Notes |
|---|---|---|
| Generate load to push EC2 CPU > scaling threshold | | |
| ASG triggers a scale-out event | | |
| New instance enters service behind the ALB | | |
| Load reduces; ASG scales back in | | |

### 6.3 Database connectivity + basic operations

*Confirm the LMS database tier is reachable and operational. Cross-reference: Test evidence C4.*

| Test | Outcome | Notes |
|---|---|---|
| MySQL client connection from EC2 over private network | | |
| Confirm MySQL version matches DOODLE compatibility requirement | | |
| Confirm encryption-in-transit on the connection | | |

### 6.4 Infrastructure end-to-end smoke test

*The LMS application itself is not installed by you (per the MTS scope statement in the role brief — LMS application deployment is YAT IT's responsibility). Your end-to-end smoke test therefore confirms the infrastructure is ready to serve traffic to whatever application YAT IT subsequently deploys.*

*Deploy a lightweight placeholder served from the EC2 instance(s) — for example a default IIS page, a static HTML "Infrastructure ready — awaiting application deployment" page, or a simple health endpoint — and confirm: (a) the ALB returns HTTP 200/302 when reached via its public DNS name, (b) the response is served from a backend EC2 instance behind the ALB, and (c) the EC2 instance can reach the RDS endpoint over the private network (basic connectivity, not LMS-specific operations). Cross-reference: Test evidence C5.*

*[Your infrastructure smoke-test description and outcome here]*

---

## §7 Operational Handover

*Hand-over information for YAT IT, who take over the infrastructure from here. Per the MTS scope statement in the role brief, the next steps after this handover — LMS application installation on the supplied infrastructure, MySQL data migration from on-prem into the AWS RDS instance, cutover from legacy to new, and organisational change management around the cutover — are all YAT IT's responsibility, not MTS's. This handover section provides YAT IT what they need to begin those activities.*

### 7.1 Access for YAT ICT

*Confirm: who has what access, MFA enforcement, post-handover IAM group changes.*

### 7.2 Runbook references

*Pointer to:*
- The supplied baseline design document (operational reference)
- The Naming and Tagging conventions section (so YAT ICT can identify resources)
- The Backup baseline (RDS automated backups, EBS snapshot policy)
- The CloudWatch alarms list and notification destination

### 7.3 Known limitations and what's next

*Be explicit about what isn't HA today and is coming in the next phase. The next-phase HA design will:*

- *Enable RDS Multi-AZ*
- *Add cross-AZ subnets and expand the ASG across two AZs*
- *Introduce HA-tuned monitoring (cross-AZ latency, replica lag, etc.)*
- *Add cross-Region backup copies*
- *Establish DR runbook and failure-simulation testing*

### 7.4 Documentation filing

*Per YAT's documented procedures, this report and its appendices are to be filed in the YAT ICT shared documentation repository (refer to the YAT Records Management Policy). Confirm filing and provide reference.*

| Item | Filed in | Reference |
|---|---|---|
| This Deployment Report (v1.0) | YAT ICT shared documentation | *[Reference]* |
| Configuration exports (Appendix B) | YAT ICT shared documentation | *[Reference]* |
| Test evidence (Appendix C) | YAT ICT shared documentation | *[Reference]* |

---

## §8 Knowledge Evidence Responses

*Answer each question below. Reference specific sections, decisions, or components of your own build — do not give generic textbook answers.*

### Q1 — Virtual machine, networking and scaling features

In §4 of your report you described the EC2, Auto Scaling Group, and Application Load Balancer you deployed. For each of these three components:
- (a) Briefly explain what feature it provides (compute capacity, traffic distribution, automatic scaling)
- (b) Explain how the choice you made for that component supports the YAT LMS workload — sizing for EC2, scaling threshold for ASG, health-check approach for ALB

*[Your response — ~250–350 words]*

### Q2 — Vertical vs horizontal scaling; managed services; storage options

Your deployment uses RDS (a managed relational database), EBS block storage on EC2, and S3 object storage.
- (a) Why is RDS preferred over a self-hosted MySQL on EC2 for the YAT LMS context?
- (b) Why are EBS and S3 used together in this deployment rather than just one or the other?
- (c) The ASG scales horizontally. Would vertical scaling (resizing the EC2 instance) have been viable instead? What's the trade-off in the YAT LMS context?

*[Your response — ~250–350 words]*

### Q3 — Shared security responsibility

Using the shared responsibility table in §9.4 of the supplied design as a starting point:
- (a) Identify two specific security responsibilities that fall on **YAT** (not AWS) in your deployed environment
- (b) Identify one responsibility that has **shifted from YAT to AWS** as a result of the migration

For each, briefly say why.

*[Your response — ~200–250 words]*

### Q4 — User access protocols and organisational hierarchy

Your IAM groups (§4.1 of this report) reflect different job functions at YAT and MTS. Pick **one** IAM group you created and:
- (a) Describe the permission set
- (b) Identify the job function it serves
- (c) Explain why this group's permissions need to be different from another group you created

*[Your response — ~150–250 words]*

### Q5 — Security policies and network traffic limits

Your security groups (§4.7) limit network traffic between tiers. Pick **one** security group you configured:
- (a) Describe what inbound and outbound traffic it allows
- (b) Explain why traffic is restricted in this way
- (c) Briefly describe what would be at risk if the restriction were removed

*[Your response — ~150–250 words]*

### Q6 — Role of DNS in the deployment

DNS plays a role at multiple points in your deployment (ALB DNS name, the LMS hostname end-users browse to, AD-LDAP lookups from EC2 back to YAT campus AD). In ~150–250 words:
- (a) Identify two specific points in your deployment where DNS resolution happens
- (b) For each, explain what is being resolved and what would fail if DNS were misconfigured

*[Your response]*

---

## Appendix A — Build evidence (Screenshots)

*Capture each screenshot below from the AWS Management Console after the build is complete. Each screenshot must clearly show the named items. Include the AWS region indicator (top-right) in each screenshot.*

| # | Screenshot description | What must be visible |
|---|---|---|
| A1 | **IAM dashboard — account access** | Signed-in user; AWS Account ID; region `ap-southeast-2` |
| A2 | **IAM Groups list** | All four created groups (`YAT-ICT-Admins`, `MTS-Consultants`, `Application-Service`, `Read-Only-Auditors`) with member counts |
| A3 | **IAM Users — MFA enforcement** | At least one user account showing MFA device assigned/enabled |
| A4 | **VPC overview** | The VPC with CIDR `10.0.0.0/16`, named per the convention, with DNS hostnames + DNS resolution enabled |
| A5 | **VPC Subnets list** | All three subnets (`public-web-a`, `private-app-a`, `private-data-a`) with correct CIDRs and AZ |
| A6 | **VPC Internet Gateway + NAT Gateway** | Both gateways attached/running in the VPC |
| A7 | **VPC Route tables** | At least the public route table (showing 0.0.0.0/0 → IGW) and the private app route table (showing 0.0.0.0/0 → NAT) |
| A8 | **EC2 Security Groups list with rules** | The three security groups (`sg-alb`, `sg-app`, `sg-db`) — rules visible (expand one to show inbound rules) |
| A9 | **EC2 Instances list** | The LMS application instance(s) in `running` state, with tags visible and correct AZ |
| A10 | **EC2 → EBS Volumes** | The EBS volumes (root + data) attached to the LMS application instance |
| A11 | **S3 Buckets list** | The two LMS buckets (attachments + backups) with **Block Public Access** column showing enabled |
| A12 | **RDS Databases list** | The LMS database in `available` state, showing Single-AZ, engine MySQL, encryption enabled |
| A13 | **EC2 → Load Balancers → Target group health** | ALB target group showing the EC2 instance(s) as **Healthy** |
| A14 | **EC2 → Auto Scaling Groups** | The ASG with launch template attached, min/desired/max values, scaling policy visible |
| A15 | **EC2 → Auto Scaling Groups → Activity history (scaling event)** | A scale-out event entry from your autoscaling test (capture during §6.2) |
| A16 | **CloudWatch → Metrics graph of the scaling test** | A graph showing CPU spike followed by the scale-out event (capture during §6.2) |
| A17 | **CloudWatch → Alarms list** | The baseline alarms you configured (per supplied design §10.2) |

---

## Appendix B — Configuration exports

*Export each configuration below from the AWS CLI or AWS Console and attach to this report. Place each export as a code block or attached file.*

| # | Export | Recommended source |
|---|---|---|
| B1 | IAM group permission policies (one document per created group) | IAM Console → Group → Permissions → Download as JSON |
| B2 | Security group rules (text or JSON dump for all three SGs) | `aws ec2 describe-security-groups --group-ids ... --output json` |
| B3 | VPC, subnet, route table configuration | `aws ec2 describe-vpcs`, `describe-subnets`, `describe-route-tables` |
| B4 | EC2 Launch Template + ASG configuration | `aws ec2 describe-launch-template-versions`, `aws autoscaling describe-auto-scaling-groups` |
| B5 | ALB + target group configuration | `aws elbv2 describe-load-balancers`, `describe-target-groups`, `describe-listeners` |
| B6 | RDS instance configuration | `aws rds describe-db-instances` |
| B7 | S3 bucket policy + public-access-block + encryption configuration | `aws s3api get-bucket-policy`, `get-public-access-block`, `get-bucket-encryption` |

---

## Appendix C — Test evidence

*Attach evidence supporting the test results recorded in §6. Each test entry below should be supported by a screenshot or a log excerpt.*

| # | Test | Evidence type |
|---|---|---|
| C1 | ALB → EC2 health check passing | Screenshot of ALB target group showing healthy targets (overlaps A13) |
| C2 | EC2 → RDS MySQL connection | Terminal screenshot showing successful `mysql` client connection from the EC2 instance |
| C3 | Autoscaling scale-out triggered during load test | Screenshot of ASG activity history showing the scale-out (overlaps A15) + CloudWatch CPU graph (A16) |
| C4 | MySQL version confirmation | Terminal output of `SELECT VERSION();` against the RDS endpoint |
| C5 | Infrastructure end-to-end smoke test (placeholder page served via ALB) | Screenshot of browser reaching the placeholder page via the ALB DNS name; OR `curl -I` output showing HTTP 200/302. *(Not the actual LMS — LMS application deployment is YAT IT's responsibility per the scope statement.)* |
| C6 | RDS not publicly reachable (negative test) | Terminal output of an attempted connection from outside the VPC showing connection refused/timeout |

---

## Appendix D — Reflections

*Two short reflective responses, ~150–250 words each. Be honest — these are about your own learning during this engagement.*

### R1 — Lessons applicable beyond this build

Looking back at this deployment, identify **one** thing you learned during the build that you could apply to a future cloud project (or a similar IT project of any kind).
- What was the lesson?
- How did you arrive at it during the build?
- How would you apply it next time?

*[Your reflection]*

### R2 — Decisions in hindsight

Identify:
- **One decision** you made during the build that turned out to be the right call — briefly evaluate why the outcome confirmed the decision
- **One decision (or assumption)** you would revise if you were to do this again — briefly evaluate what you'd do differently

*[Your reflection]*

---

## Document control

| | |
|---|---|
| **Document version** | 1.0 — Initial submission |
| **Author** | [Your name], MTS Consultant |
| **Engagement** | YAT LMS Cloud Migration — Foundation Build Phase |
| **Date submitted** | [DD/MM/YYYY] |
| **Distribution** | Sam Walker (YAT ICT Manager), Pat Lin (MTS Senior Consultant) |
| **Successor document** | YAT LMS HA Hardening Phase — Final Report (forthcoming) |
