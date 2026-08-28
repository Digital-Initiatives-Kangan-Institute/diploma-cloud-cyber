# AT2 — build run sheet: task list

The source document for the AT2 instrument. It holds the **task list**, the **settings each task is
built to**, the **evidence each produces**, and the **UoC item each evidences** — the layer that has
never been written down for any AT in this course, and whose absence made the AT2 review archaeology.

> **Superseded as the source of truth (2026-08-28).** `scripts/s1_cl1/at2_run_sheet.py` is now the
> single definition of the AT2 run sheet — it holds the tasks, their settings, the evidence each
> produces and the UoC items each evidences, and both instruments render from it. The task list
> below is the earlier draft and has NOT been kept in step: it describes three subnets rather than
> five, a four-group IAM build with MFA rather than the single refused submission, and two S3
> buckets that were cut. Read it as the design record of how the run sheet was arrived at, not as a
> specification to build from or regenerate against.

## What the instrument is

A build run sheet the student works through and fills in. In-world it is the implementation runbook an
MTS implementation lead produced from the approved design — the student's job is to execute it, not to
work from the design directly. Out-of-world it is the assessment document.

**Settings are given. Navigation is not.** Each task states the job and the values it must be built
to. How to find things in the console is withheld, as is anything the unit asks the student to decide.

**Evidence sits with its task.** No appendix of collected screenshots.

**Two decisions, both inline** — the only two items in AT2's coverage carrying a decision verb.

## Environment

Region: `[scenario: ap-southeast-2 | deploy: us-east-1]` per `docs/region-substitution-standard.md`.

**Every value the run sheet specifies is one the environment will actually accept.** Sizes are the
smallest that do the job — free-tier or near it — so no task can be blocked by a service limit. This
removes the failure that cost the last cohort its time: a design specifying `m6i.large` and
`db.m6i.large`, and an exemplar modelling a build no student could launch.

Cost note: the NAT gateway and the load balancer are not free-tier and carry an hourly charge. Both
are required by the architecture, so they stay — but the run sheet tells students to delete the stack
when they finish a session.

## Build tasks

| # | Task | Built to | Evidence | Evidences |
|---|---|---|---|---|
| 1 | Sign in and confirm your working region | the engagement's region | console showing the region selector | `401 PC 1.4` |
| 2 | Create the VPC | `10.0.0.0/16`; DNS hostnames + resolution enabled | VPC details | `401 PC 2.2` · `401 PE 1` |
| 3 | Create the three subnets | `public-web-a 10.0.1.0/24` · `private-app-a 10.0.11.0/24` · `private-data-a 10.0.21.0/24`, all one AZ | subnet list with CIDRs and AZ | `401 PC 2.2` · `401 PE 1` |
| 4 | Create the internet gateway and NAT gateway | IGW attached to the VPC; NAT in `public-web-a` with a new Elastic IP | both, showing Attached / Available | `401 PC 2.2` · `401 PE 1` |
| 5 | Create the route tables | public → IGW; private-app → NAT; private-data → no internet route | all three with their routes and associations | `401 PC 2.2` · `401 PE 1` |
| 6 | Create the three security groups | `sg-alb` HTTP:80 from anywhere · `sg-app` from `sg-alb`, and 3306 out to `sg-db` · `sg-db` 3306 from `sg-app` only | all three with rules expanded | `401 PC 1.7` · `502 PC 1.3` |
| 7 | Create the IAM groups and enable MFA | the four groups from the design; MFA on one admin user | groups with members; MFA enabled | `401 PC 1.5` · `401 PC 1.6` · `401 PC 2.1` |
| 8 | Create the instance role | RDS + S3 + CloudWatch Logs write; attached as an instance profile | the role and its attached policies | `401 PC 1.6` · `401 PC 1.7` |
| 9 | **Create the launch template** — *decision C1* | Windows Server AMI; the instance role; user data installing the web server + placeholder page; root `gp3` 30 GB, data `gp3` 8 GB. **Instance type: choose `t3.micro` or `t3.small`** | launch template summary; **plus the C1 decision box** | `401 PC 2.3` · `401 PC 2.4` · `401 PC 1.1` · `401 PC 1.3` |
| 10 | Create the target group and load balancer | target group HTTP:80, health check `/`, 30 s, 2 unhealthy; internet-facing ALB in `public-web-a`, HTTP:80 listener | ALB and target group config | `401 PC 2.2` · `502 PC 4.1` |
| 11 | Create the Auto Scaling group | min 1 / desired 1 / max 2; target tracking on CPU at 70%; ELB health checks; 60 s cooldown, 60 s warm-up | ASG details showing capacity and policy | `401 PC 3.1` · `401 PE 2` |
| 12 | **Deploy the database** — *decision C2* | subnet group spanning two subnets; MySQL; Multi-AZ off; storage encrypted; not publicly accessible; 7-day backups; `sg-db`; `gp3` 20 GB. **Instance class: choose `db.t3.micro` or `db.t3.small`** | RDS showing Available, encryption, public access No; **plus the C2 decision box** | `401 PC 2.5` · `401 PC 1.1` · `401 PC 1.3` · `401 PE 2` |
| 13 | Create the two S3 buckets | attachments + backups; block all public access; SSE-S3; versioning on | both buckets' properties | `401 PC 2.4` · `401 PE 2` |
| 14 | Create the two CloudWatch alarms | ALB target health (any unhealthy target); RDS free storage < 15% | both alarms and their state | `502 PC 4.3` |

**Both decisions are a choice between two named, known-deployable options.** The student is not asked
to survey the instance catalogue — they compare the two in front of them, pick one, and say why
against the workload in the LMS Application Specification. Naming the gap — *"both are well below what
200–300 concurrent users need; in production I would size to X, but this environment caps me here"* —
is a **satisfactory** answer and arguably the best one, because it is the honest professional
judgement.

This is what keeps `[ICTCLD401 PC 1.1]` (*discuss and compare*) and `[ICTCLD401 PC 1.3]` (*select
best*) evidenced in AT2 at all. If the run sheet named a single instance type instead, there would be
nothing to compare and nothing to select, and both items would have to move to AT1.

**Decision C1** (task 9) — application-tier instance type: `t3.micro` or `t3.small`.

**Decision C2** (task 12) — database instance class: `db.t3.micro` or `db.t3.small`.

## Tests

Per `at2-deployment-report-template`, five instrumented tests: connect to the application server ·
reach the internet · reach the database on 3306 · reach the load balancer on 80 · automatic scaling by
moving the policy target. Each carries its steps and its screenshot slot.

`401 PC 2.6` · `401 PC 3.2` · `401 PE 3` · `502 PC 4.2`

## Handover

Where the completed run sheet is filed, per YAT's records procedures. `401 PC 4.3`

## Knowledge questions

Six contextual questions — the only sustained writing in the instrument.
`401 KE 5`–`KE 10` · `401 FS Reading` · `401 FS Writing`

## Coverage check

Every item on AT2's coverage line is evidenced above: `401 PC 1.1`–`1.7`, `2.1`–`2.6`, `3.1`, `3.2`,
`4.3` · `401 PE 1`–`3` · `401 KE 5`–`10` · `401 FS Reading`, `FS Writing` · `502 PC 1.3`, `4.1`–`4.3`.

## Open

- `[TBD — needs discussion: how the student gets a shell on the instance for tests 6.1–6.4. Session
  Manager needs only an instance-profile policy; SSH on Windows Server 2016 needs OpenSSH fetched and
  installed in user data, and fails silently if that fetch fails. Tim has asked for SSH; the decision
  belongs to the design review.]`
- `[TBD — every task's settings and every test command need one live Learner Lab run before issue.
  Nothing here has been executed. Confirm in particular that Windows Server runs usably on t3.micro
  (1 GiB) — if not, make t3.small the lower of the two options and t3.medium the upper.]`
