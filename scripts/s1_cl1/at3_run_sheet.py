#!/usr/bin/env python3
"""The S1-CL1 AT3 HA design-and-build workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), exactly as AT2 does.

  Part A  the student designs the HA-equivalent of the environment AT2 built. The workbook
          supplies the current architecture and the ORDER of the tasks; every finding
          and every design decision is the student's.
  Part B  a run sheet. Task 1 deploys the assessor-provided baseline lab-pack; each task
          after it names the Part A task whose answer it builds, and the student copies
          that answer across before building. That copy-forward is what keeps
          [ICTCLD502 PE 1] and [ICTCLD502 PE 2] intact — same candidate, same infrastructure,
          designed and implemented.

THE MARKING MODEL. Values in this document are ours, invented so the student has a concrete
task; the unit's wording is vague by design. Each element therefore carries two things: the
`uoc` tags it evidences, and a `standard` naming what must be true for them to be met. An
assessor marks the standard, never the table. A student who sets a minimum of 3 where we said
2 has met [ICTCLD502 PE 2]; a student who leaves it at 1 has not — and not because it differs
from ours, but because one instance in one zone is not resilient to a data-centre failure.

STARTING STATE. AT3 begins from the end state of the AT2 run sheet (at2_run_sheet.py), NOT
from the earlier supplied baseline design. The lab-pack reproduces that end state so every
student starts from the architecture AT2 asked them to build, whatever they personally got to.

The four single points of failure AT3 exists to remove are all present by construction in
AT2's build: only us-east-1a carries load, the ASG runs one instance in one subnet, the
database is deliberately single-AZ, and there is one NAT gateway. The load balancer already
spans two zones — task 9 is what finds out whether the student checked.
"""
from pathlib import Path  # noqa: E402

import run_sheet_render as R  # noqa: E402  (shared primitives; AT2 keeps its own copies for now)

SITE = "https://yat.timbaird.com"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "YAT College's Learning Management System now runs on AWS. You are an MTS Consultant on this "
    "engagement, reporting to Pat Lin (MTS Senior Consultant). Sam Walker (YAT IT Manager) is your "
    "primary YAT-side stakeholder.",
    "You built the cloud foundation in the previous phase and handed it over. YAT IT installed the "
    "LMS on it, migrated the database and ran the cutover, and the system has been live for a term. "
    "It works — but it was never built to survive a failure, and YAT's strategic target of 99.9% "
    "availability has not been met.",
    "The board has approved a final phase: harden the environment for high availability. You design "
    "the HA-equivalent architecture in Part A, then implement it in Part B during a maintenance "
    "window. The engagement closes when Sam Walker signs it off.",
]

RESOURCES = [
    ("LMS Application Specification (AWS-Hosted) — the workload the availability targets are set against",
     f"{SITE}/intranet/s1-cl1-at3/ict/lms-application-spec-cloud"),
    ("LMS Cloud Migration Requirements — the availability and recovery targets you design against",
     f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
    ("Records Management Policy — where a completed engagement document has to be filed",
     f"{SITE}/intranet/s1-cl1-at3/policies/records-management"),
]

ASSESSOR_PROVIDES = ("Your assessor will provide the baseline lab-pack — a CloudFormation template "
                     "that builds the current environment described below. You deploy it as the "
                     "first task of Part B. Ask your assessor where to download it from.")

INSTRUCTIONS = [
    "This is an open-book assessment. You may use the YAT intranet, AWS documentation, and anything "
    "you have from class — including your own notes and any practice work you have done. What you "
    "may not use is another student.",
    "Part A is the design. Work the tasks in order — each one builds on the answer before it. "
    "They tell you what to decide; they do not tell you what to decide it to.",
    "Part B is the build. Every task names the Part A task it comes from — copy your own answer "
    "into the task before you build it. You are implementing your design, not ours.",
    "Take each screenshot as you finish the task, not at the end. Recreating a screen after you have "
    "moved on is painful and sometimes impossible.",
    "Answer the knowledge questions about your own design and your own build. Generic answers about "
    "high availability will not pass.",
]

# ---------------------------------------------------------------- the supplied current state

NETWORK_DIAGRAM = ("Network diagram — this environment drawn out, including the campus it connects "
                   "back to",
                   f"{SITE}/intranet/s1-cl1-at3/ict/network-diagram-post-cutover")

CURRENT_ARCH_INTRO = [
    "This is the environment you are hardening. It is what the previous phase built and handed over, "
    "and the lab-pack in Part B task 19 recreates it exactly. Read it before you answer anything — "
    "several tasks below turn on noticing what is already there.",
]

CURRENT_ARCH = [
    ("Region", [("For the scenario this infrastructure sits in the Sydney region, ap-southeast-2. "
                 "Use that region if it is available to you. ", False),
                ("If you are working in AWS Academy Learner Lab or a similar restricted "
                 "environment, Sydney will not be offered — build in us-east-1, or whichever "
                 "region you do have. The work is identical either way.", True)]),
    ("Network", "VPC yat-lms-vpc, 10.0.0.0/16"),
    ("Subnets", "zone names below follow us-east-1; in another region read -1a and -1b as that "
                "region's first two zones  ·  public-web-a  10.0.1.0/24  (us-east-1a)  ·  public-web-b  10.0.2.0/24  (us-east-1b)  ·  "
                "private-app-a  10.0.11.0/24  (us-east-1a)  ·  private-data-a  10.0.21.0/24  (us-east-1a)  ·  "
                "private-data-b  10.0.22.0/24  (us-east-1b)"),
    ("Where the load actually is", "everything that serves the LMS runs in us-east-1a. public-web-b and "
                                   "private-data-b were created because the load balancer and the database "
                                   "subnet group each refuse to be created with only one zone. Nothing has "
                                   "ever been placed in them."),
    ("Internet in", "internet gateway yat-lms-igw; public-rt routes 0.0.0.0/0 to it, associated with both public subnets"),
    ("Internet out", "one NAT gateway yat-lms-nat in public-web-a; private-app-rt routes private-app-a's "
                     "0.0.0.0/0 to it"),
    ("Compute", "Auto Scaling group across private-app-a only — desired 1, minimum 1, maximum 2; launch "
                "template yat-lms-lt (Windows Server, IIS installed at boot, serving a placeholder page)"),
    ("Load balancing", "internet-facing ALB yat-lms-alb in public-web-a and public-web-b, HTTP :80, "
                       "forwarding to target group yat-lms-tg (health check HTTP /, 30s, unhealthy threshold 2)"),
    ("Database", "MySQL on RDS, single-AZ with no standby, gp3 20 GB, encrypted, 7-day backup retention, "
                 "in subnet group yat-lms-db-subnet-group (private-data-a + private-data-b)"),
    ("Security groups", "yat-lms-alb-sg  HTTP 80 from anywhere  ·  yat-lms-app-sg  HTTP 80 from the ALB group  ·  "
                        "yat-lms-db-sg  MySQL 3306 from the app group"),
    ("Monitoring", "two alarms notifying SNS topic yat-lms-alerts — yat-lms-unhealthy-hosts "
                   "(UnHealthyHostCount ≥ 1) and yat-lms-db-storage-low (FreeStorageSpace below 15%)"),
]

# ---------------------------------------------------------------- Part A — design
# n        — task number, referenced by the Part B tasks that build this answer
# title    — the heading
# prompt   — what the student is asked
# uoc      — items this task evidences
# standard — what must be true for those items to be met (assessor-only)
# table    — (columns, model_rows) for a capture table; or
# points   — key points for a written response
# diagram  — optional caption for a drawing slot

DESIGN = [
    dict(n=1, title="The targets this design has to meet",
         resources=[
             ("LMS Cloud Migration Requirements — the availability, recovery and service-level targets the board signed off on. The figures you need are here",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
             ("LMS Application Specification (AWS-Hosted) — the workload those targets are set against: who uses it, how many at once, and when",
              f"{SITE}/intranet/s1-cl1-at3/ict/lms-application-spec-cloud"),
         ],
         prompt="Before you design anything, establish what the design is held to. Read the LMS Cloud "
                "Migration Requirements and the LMS Application Specification (AWS-Hosted), and record the "
                "availability, recovery and service-level targets the HA design must achieve. Name the "
                "document each figure came from.",
         uoc=["ICTCLD502 PC 1.1", "ICTCLD502 FS Reading"],
         standard="the student states an availability target, a recovery point objective and a recovery "
                  "time objective, and attributes each to a source document rather than inventing it. "
                  "The exact figures are in the supplied documents; a student who transcribes them "
                  "correctly has met the item. Additional service-level rows are welcome, not required.",
         given=1, blank_rows=4,
         table=(["Requirement", "Target", "Where it came from"],
                [["Availability", "99.9%", "LMS Cloud Migration Requirements"],
                 ["Recovery point objective (RPO)", "≤ 1 hour", "LMS Cloud Migration Requirements"],
                 ["Recovery time objective (RTO)", "≤ 4 hours", "LMS Cloud Migration Requirements"],
                 ["Peak concurrent users", "the figure in the application specification",
                  "LMS Application Specification (AWS-Hosted)"]])),

    dict(n=2, title="Review the current environment against those targets",
         resources=[
             ("Network Diagram — the environment drawn out, so you can see which tier sits where. Your work is the AWS side only",
              f"{SITE}/intranet/s1-cl1-at3/ict/network-diagram-post-cutover"),
             ("LMS Server Status — what is actually running post-cutover, tier by tier",
              f"{SITE}/intranet/s1-cl1-at3/ict/lms-server-status-post-cutover"),
         ],
         prompt="Go through the current environment tier by tier. For each, say whether it meets the "
                "targets you recorded in task 1, and if it does not, why not. Work from what is "
                "described above — not from what you would expect a cloud environment to look like.",
         uoc=["ICTCLD502 PC 2.1", "ICTCLD401 FS Reading"],
         standard="every tier is reviewed and the judgement is tied to the task 1 targets, not to a "
                  "general sense that something is 'not best practice'. A review that reads as a "
                  "description of the architecture rather than an assessment against targets has not met "
                  "the item.",
         given=1, blank_rows=6,
         table=(["Tier", "Meets the targets?", "Why / why not"],
                [["Network", "No", "every subnet carrying load is in us-east-1a; losing that zone loses the LMS"],
                 ["Compute", "No", "one instance, minimum 1 — losing it takes the LMS down until a replacement boots"],
                 ["Load balancing", "Yes", "already spans us-east-1a and us-east-1b"],
                 ["Database", "No", "single-AZ, no standby; recovery means restoring a backup, well beyond RTO 4h"],
                 ["Internet out", "No", "one NAT gateway in one zone; its loss cuts outbound for the app tier"],
                 ["Monitoring", "Partly", "alarms detect an unhealthy target and low storage, but nothing "
                                          "reports per-zone health or a database failover"]])),

    dict(n=3, title="Single points of failure",
         resources=[
             ("Network Diagram — read it looking for anything there is only one of",
              f"{SITE}/intranet/s1-cl1-at3/ict/network-diagram-post-cutover"),
         ],
         prompt="Identify every single point of failure in the current environment — every component "
                "whose failure takes the LMS down or degrades it below the targets. For each, say what "
                "the failure looks like and what YAT loses. Be thorough: one you miss here is one your "
                "design will not remove and your simulations will not catch. "
                "Work through the environment tier by tier and ask what happens if that one component stops. Anything that exists once, in one place, is where to look.",
         uoc=["ICTCLD502 PC 2.2"],
         standard="the student identifies the availability-zone concentration, the single application "
                  "instance and the single-AZ database. Those three are the substance of the item. The "
                  "NAT gateway is a fourth and a strong answer finds it. Consequences must be stated in "
                  "terms of the LMS, not as generic risk language.",
         given=0, blank_rows=6,
         table=(["Component", "Failure mode", "Consequence for YAT"],
                [["us-east-1a", "availability-zone failure", "total LMS outage — every tier that serves traffic is in it"],
                 ["The single EC2 instance", "instance or host failure",
                  "LMS unreachable until the Auto Scaling group boots a replacement (minutes, not seconds)"],
                 ["The RDS instance", "instance or storage failure",
                  "LMS down until a backup is restored — hours, against an RTO of 4"],
                 ["yat-lms-nat", "NAT gateway or zone failure",
                  "app tier loses outbound access; patching and any outbound integration stop"]])),

    dict(n=4, title="Recovery objectives the current environment actually achieves",
         resources=[
             ("LMS Cloud Migration Requirements — the RPO and RTO targets you are measuring today's environment against",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
             ("LMS Server Status — the backup arrangements currently in place, which set the RPO you can actually achieve",
              f"{SITE}/intranet/s1-cl1-at3/ict/lms-server-status-post-cutover"),
         ],
         prompt="For each component, estimate what the current environment delivers today — how much "
                "data would be lost, and how long recovery would take. Put numbers on it. “Worse than "
                "target” is not an estimate.",
         uoc=["ICTCLD502 PC 2.3"],
         standard="figures are quantified per component and compared against the task 1 targets. The "
                  "precise numbers are estimates and will vary — what is being assessed is that the "
                  "student reasons from the actual configuration (7-day automated backups, no standby, "
                  "ASG replacement time) rather than guessing.",
         given=1, blank_rows=3,
         table=(["Component", "Current RPO", "Current RTO", "Meets target?"],
                [["Application tier", "n/a — stateless", "5–10 min (ASG boots a replacement)", "No"],
                 ["Database", "up to 24 h (last automated backup)", "2–6 h (restore + cutover)", "No"],
                 ["Whole service", "up to 24 h", "hours — nothing to fail over to", "No"]])),

    dict(n=5, title="Components that have to scale vertically",
         resources=[
             ("LMS Application Specification (AWS-Hosted) — the load each tier carries, which is what tells you whether growth means more of them or bigger ones",
              f"{SITE}/intranet/s1-cl1-at3/ict/lms-application-spec-cloud"),
         ],
         prompt="Some components can only be made bigger, not more numerous. Identify which components "
                "in this environment are in that position, and what happens to availability while they "
                "are being resized. "
                "Look across compute, storage and the database — for each, ask whether you could add another one alongside it, or whether the only option is a bigger one.",
         uoc=["ICTCLD502 PC 2.4"],
         standard="the student identifies the database as the vertically-scaled component and states that "
                  "resizing it interrupts service in the current single-AZ configuration. Recognising "
                  "that the application tier scales horizontally instead is part of a complete answer.",
         given=0, blank_rows=4,
         table=(["Component", "Why it must scale vertically", "Availability impact while it scales"],
                [["RDS instance", "one database instance serves all traffic; you change its class, not its count",
                  "outage for the duration of the change — single-AZ has nothing to fail over to"],
                 ["EBS volumes", "storage attached to a specific instance", "brief; can be done on a replacement instance"],
                 ["Application tier", "it does not — the ASG adds instances instead", "none, if more than one instance is running"]])),

    dict(n=6, title="Summarise your review",
         resources=[
             ("LMS Migration Role Brief — who Sam Walker is and what they are accountable for. You are writing this summary for them",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/role-brief"),
             ("LMS Cloud Migration Requirements — the targets the gap you are summarising is measured against",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
         ],
         prompt="Write a short summary of what you found: the gap between the current environment and "
                "the targets from task 1, and which components drive that gap. Sam Walker will read "
                "this before approving the work, so write it for someone who runs YAT's ICT rather than "
                "someone who built this environment. Around 200 words.",
         uoc=["ICTCLD502 PC 2.5"],
         standard="the summary states the gap in terms of the targets and names the components "
                  "responsible. It has to be readable by the ICT Manager — a summary that assumes the "
                  "reader already knows the architecture has not documented the findings 'according to "
                  "business needs'.",
         points=["Names the availability gap against the 99.9% target and the recovery gap against RPO 1 h / RTO 4 h.",
                 "Attributes the gap to the zone concentration, the single instance and the single-AZ database.",
                 "States what YAT is exposed to today in plain terms — an outage of hours from a single failure.",
                 "Written for the ICT Manager, not for another engineer."]),

    dict(n=7, title="Design — the network",
         resources=[
             ("LMS Cloud Architecture — Baseline Design — the addressing plan and naming conventions the environment already follows",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/cloud-architecture-baseline"),
         ],
         prompt="Your application tier has to be able to run in two availability zones. Look at the "
                "subnets that already exist. What do you need to add, and where? Record the subnet or "
                "subnets you are designing in, then sketch the network you are aiming for. "
                "Name it the way the existing subnets are named — what it carries, and which zone it is in.",
         uoc=["ICTCLD502 PC 3.1", "ICTCLD502 PE 1"],
         standard="the student designs a private application subnet in the second availability zone. "
                  "That is the item — the environment has public and data subnets in us-east-1b already, "
                  "but no application subnet, so this cannot be answered by enabling something that "
                  "exists. The CIDR chosen is context; it must be inside 10.0.0.0/16 and must not "
                  "collide with an existing subnet.",
         given=0, blank_rows=2,
         table=(["Subnet name", "CIDR", "Zone", "What it carries"],
                [["private-app-b", "10.0.12.0/24", "us-east-1b", "application instances — the second-zone half of the tier"]]),
         diagram="the environment you are designing — both zones, and which resources sit in each"),

    dict(n=8, title="Design — the application tier",
         resources=[
             ("LMS Application Specification (AWS-Hosted) — the concurrent-user load and the peak periods your capacity numbers have to carry",
              f"{SITE}/intranet/s1-cl1-at3/ict/lms-application-spec-cloud"),
         ],
         prompt="You now have somewhere for a second application instance to run. Design the Auto "
                "Scaling group's configuration so the loss of one availability zone leaves the LMS "
                "serving. Give a reason for the capacity numbers you choose.",
         uoc=["ICTCLD502 PC 3.1", "ICTCLD502 PE 2"],
         standard="the group spans two availability zones and its MINIMUM is at least two, so a zone "
                  "failure leaves at least one instance serving. That is the item. Whether the minimum is "
                  "2 or 3, the maximum, the scaling target and the warm-up are all context — a workable "
                  "alternative is not a defect. A minimum of 1 does not meet the item, whatever the "
                  "reasoning, because one instance in one zone is not resilient to a zone failure.",
         given=1, blank_rows=5,
         table=(["Setting", "Your design", "Why"],
                [["Subnets", "private-app-a and private-app-b", "one instance in each zone"],
                 ["Minimum", "2", "a zone failure must still leave one instance serving"],
                 ["Desired", "2", "one per zone under normal load"],
                 ["Maximum", "4", "headroom for the assessment-period peak"],
                 ["Scaling policy", "target tracking, average CPU 70%", "unchanged from the baseline — it was not the problem"]])),

    dict(n=9, title="Design — the load balancer",
         prompt="What did you decide about the load balancer, and why? Look at what is already there "
                "before you answer.",
         uoc=["ICTCLD502 PC 3.1"],
         standard="the correct answer is that no change is required, with the reason: the load balancer "
                  "was created across public-web-a and public-web-b, so it already spans both zones, and "
                  "the Auto Scaling group registers new instances into the target group automatically. "
                  "What is being assessed is that the student checked the current state before designing. "
                  "A student who proposes rebuilding or extending it has not looked; a student who says "
                  "'no change' with no reason has not demonstrated anything either. A student who "
                  "correctly identifies no change but adds a cross-zone load balancing check has "
                  "exceeded the item, not missed it.",
         points=["No change is required to the load balancer itself.",
                 "Reason: it was created in public-web-a and public-web-b, so it is already spread across both zones.",
                 "The target group needs no manual change either — the Auto Scaling group registers instances into it.",
                 "A student who says 'make it highly available' without checking has missed the point of the task."]),

    dict(n=10, title="Design — the database",
         resources=[
             ("LMS HA Database Requirements — what the database specifically has to achieve, and the constraints on how",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/ha-database-requirements"),
             ("LMS Cloud Migration Requirements — the RPO and RTO the database change has to deliver",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
         ],
         prompt="The database is the component with the worst recovery numbers in task 4. Design "
                "the change that fixes it, and state what it gives you that the current configuration "
                "does not. "
                "The settings worth considering include how the deployment is spread across availability zones, how long backups are retained, and what the application connects to. You do not need all of them — start with what fixes the recovery numbers.",
         uoc=["ICTCLD502 PC 3.1", "ICTCLD502 PE 1"],
         standard="the student designs a Multi-AZ deployment — a standby in the second zone with "
                  "automatic failover. That is the item; nothing else in the service meets an RTO of 4 "
                  "hours. A student who proposes a read replica instead has not met it (a replica is not "
                  "automatic failover) unless they also design the promotion process and account for its "
                  "time. Retention and window settings are context.",
         given=0, blank_rows=4,
         table=(["Setting", "Your design", "Why"],
                [["Multi-AZ", "yes — standby in us-east-1b", "automatic failover instead of restoring a backup"],
                 ["Endpoint", "unchanged", "the application connects to the same name; failover is transparent"],
                 ["Backup retention", "7 days, unchanged", "the standby addresses RTO; backups still address RPO"],
                 ["Expected RTO after the change", "1–2 minutes", "failover time, against the 4-hour target"]])),

    dict(n=11, title="Design — the outbound path",
         prompt="Your application tier will now run in two zones. Think about what the instances in the "
                "new zone use to reach the internet. Design your answer, and be explicit if you are "
                "accepting a risk rather than removing it. "
                "Things you might record here: the gateway itself, and the route table that decides where a subnet's traffic goes.",
         uoc=["ICTCLD502 PC 3.1", "ICTCLD502 PC 3.2"],
         standard="the student recognises that a single NAT gateway in us-east-1a leaves the new zone "
                  "dependent on the old one, and either designs a second NAT gateway in public-web-b with "
                  "its own route table, or explicitly accepts the shared gateway and states the residual "
                  "risk. Both are satisfactory — the item is identifying and dealing with the point of "
                  "failure, not a particular remedy. Saying nothing about it is not.",
         given=0, blank_rows=4,
         table=(["Setting", "Your design", "Why"],
                [["NAT gateway", "a second one in public-web-b", "so private-app-b does not depend on us-east-1a"],
                 ["Route table", "private-app-b-rt — 0.0.0.0/0 to the new NAT gateway", "each zone routes out through its own zone"],
                 ["If you accept the shared gateway instead", "state it here and say what breaks if us-east-1a fails",
                  "an accepted, documented risk is a legitimate design position"]])),

    dict(n=12, title="Design — monitoring",
         resources=[
             ("LMS Cloud Migration Requirements — the service levels your monitoring has to be able to report against",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
         ],
         prompt="The two existing alarms tell you a target is unhealthy or storage is low. Neither tells "
                "you a zone has gone or a database has failed over. Design the monitoring that would tell "
                "you, and say what each alarm detects. "
                "An alarm needs a metric, a threshold and a failure it would catch. The two that exist today catch an unhealthy target and low database storage — start from what they would miss.",
         uoc=["ICTCLD502 PC 3.1", "ICTCLD502 PE 5"],
         standard="the student designs at least one alarm that would reveal a loss of availability the "
                  "current set would miss. The model shows one per zone, which is the complete "
                  "answer; a single alarm on one zone still meets the item — per-zone healthy host count, a database failover event, or an "
                  "equivalent. Thresholds are context. Restating the two existing alarms is not designing "
                  "monitoring for high availability.",
         given=0, blank_rows=4,
         table=(["Alarm", "What it measures", "Threshold", "What it detects"],
                [["Healthy hosts, us-east-1a", "HealthyHostCount for the target group in that zone",
                  "below 1", "that zone has stopped serving even though the LMS is still up"],
                 ["Healthy hosts, us-east-1b", "HealthyHostCount for the target group in that zone",
                  "below 1", "the same for the second zone. An alarm watches one zone, so covering "
                  "both takes one alarm each — the baseline alarm counts unhealthy hosts across the "
                  "whole target group and cannot see a zone go dark at all"],
                 ["Database connections lost", "DatabaseConnections, for the database instance",
                  "below 1", "nothing is connected to the database — which is what a Multi-AZ "
                  "failover looks like while it happens, and also what an application outage looks "
                  "like. (A failover itself is an RDS event, not a CloudWatch metric: subscribing to "
                  "it is done under RDS, Event subscriptions, not here.) EXPECT THIS ONE TO FIRE "
                  "IMMEDIATELY AND STAY FIRING: the instances serve a placeholder page and never "
                  "connect to the database, because installing the LMS application is YAT IT's job "
                  "and out of scope here. The alarm is correct for the real system; this environment "
                  "simply cannot exercise it. A student who builds it and notes that it alarms for "
                  "that reason has understood more than one whose alarms all sit quietly in OK."]])),

    dict(n=13, title="Which single points of failure does your design remove?",
         prompt="Go back to your answer to task 3. For each single point of failure you found there, "
                "say what in your design removes it — or state plainly that it remains, and why you "
                "accepted it.",
         uoc=["ICTCLD502 PC 3.2"],
         standard="every point of failure from the student's own task 3 is accounted for, either "
                  "removed or explicitly accepted with a reason. An unaccounted-for entry is the failure "
                  "condition here, not a wrong remedy.",
         given=0, blank_rows=5,
         table=(["Point of failure (from task 3)", "Removed by", "Or accepted because"],
                [["us-east-1a concentration", "application subnet, ASG capacity and database standby in us-east-1b", "—"],
                 ["Single EC2 instance", "ASG minimum of two, one per zone", "—"],
                 ["Single-AZ database", "Multi-AZ deployment with automatic failover", "—"],
                 ["Single NAT gateway", "second NAT gateway in public-web-b", "or: accepted, with the outbound risk stated"]])),

    dict(n=14, title="Recovery objectives your design achieves",
         resources=[
             ("LMS Cloud Migration Requirements — the targets you are checking your design against",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
         ],
         prompt="Redo task 4 against your design. What does each component deliver now, and does the "
                "whole service meet the targets from task 1?",
         uoc=["ICTCLD502 PC 3.3"],
         standard="figures are quantified and the overall service is compared against the task 1 "
                  "targets. If the design does not meet a target, saying so with a reason is "
                  "satisfactory; claiming it does when the design plainly does not is the failure.",
         given=1, blank_rows=3,
         table=(["Component", "Designed RPO", "Designed RTO", "Meets target?"],
                [["Application tier", "n/a — stateless", "seconds — the other zone is already serving", "Yes"],
                 ["Database", "≤ 5 min (standby is synchronous)", "1–2 min (automatic failover)", "Yes"],
                 ["Whole service", "≤ 5 min", "1–2 min", "Yes — meets 99.9% / RPO 1 h / RTO 4 h"]])),

    dict(n=15, title="What still has to scale vertically?",
         prompt="Redo task 5 against your design. Which components still can only be made bigger, "
                "and what does resizing cost you in availability now? "
                "Start from the components you listed in task 5.",
         uoc=["ICTCLD502 PC 3.4"],
         standard="the student recognises that the database still scales vertically, but that Multi-AZ "
                  "changes the cost of doing it — the resize happens on the standby and a failover "
                  "switches to it, so the interruption is a failover rather than an outage.",
         given=0, blank_rows=3,
         table=(["Component", "Still scales vertically?", "Availability impact now"],
                [["RDS instance", "Yes", "resize applies to the standby, then fails over — seconds, not an outage"],
                 ["Application tier", "No", "the ASG adds instances; no resize needed"]])),

    dict(n=16, title="Is your design complete?",
         prompt="Read back over tasks 7 to 15 as one document. Does it hang together — does every "
                "layer have an answer, do the answers agree with each other, and would Sam Walker be "
                "able to approve it without asking you what you meant? Note anything you had to change "
                "on this read-through.",
         uoc=["ICTCLD502 PC 3.5"],
         standard="the design is internally consistent and addresses YAT's stated business needs. "
                  "Contradictions between answers are the failure condition — for example a second NAT "
                  "gateway designed in task 11 with no route table for it, or an ASG spanning a "
                  "subnet that task 7 never created. A student who finds and records their own "
                  "inconsistency here has demonstrated the item well.",
         points=["Every layer of the environment has a design answer or an explicit 'no change, because'.",
                 "The answers do not contradict each other.",
                 "The design is stated in enough detail to be built from — a reader could implement it.",
                 "Anything corrected on the read-through is noted, not silently fixed."]),

    dict(n=17, title="The order you will do it in",
         resources=[
             ("Change Management Procedure — YAT's rules for changing a production system: notice, approval, and what a rollback plan has to contain",
              f"{SITE}/intranet/s1-cl1-at3/policies/change-management"),
         ],
         prompt="You have a maintenance window of about 3.5 hours on a Saturday night. Plan the order "
                "you will apply your changes in. For each change give how long you expect it to take, "
                "what the LMS looks like to a user while it happens, how you will confirm it worked, and "
                "what you will do if it does not. State the total and the buffer you have left.",
         uoc=["ICTCLD401 FS Planning and organising"],
         standard="the changes are sequenced, not just listed, and the sequence is defensible — additive "
                  "work before the disruptive database conversion. Each change carries a duration, a "
                  "verification and a rollback, and the durations total less than the window with a stated "
                  "buffer. Exact durations are estimates; the item is planning the work, not predicting "
                  "AWS accurately.",
         given=1, blank_rows=6,
         table=(["#", "Change", "Time", "Impact on the LMS", "How you verify it", "If it fails"],
                [["1", "Create private-app-b", "5 min", "none", "subnet visible, correct zone", "delete it and retry"],
                 ["2", "Second NAT gateway + route table", "10 min", "none", "instance in the new subnet reaches the internet", "leave private-app-b on the existing route table"],
                 ["3", "Extend the ASG to both subnets, min 2", "10 min", "none — capacity is added, not moved", "second instance healthy in the target group", "return min and subnets to the previous values"],
                 ["4", "Convert the database to Multi-AZ", "30–60 min", "brief interruption at failover", "Multi-AZ shows Yes; LMS still loads", "the conversion is reversible; disable Multi-AZ"],
                 ["5", "HA alarms", "15 min", "none", "alarms in OK state", "delete and re-create"],
                 ["Total", "roughly 90 minutes against a 3.5-hour window", "", "", "", "buffer: about 2 hours"]])),

    dict(n=18, title="How you will prove it works",
         prompt="A design is a claim until something tests it. Plan the simulations you will run in Part "
                "B: at least one failure simulation and at least one resize simulation. For each, say "
                "what you will do, what you expect to happen, and how you will know whether it did.",
         uoc=["ICTCLD502 PC 4.6"],
         standard="at least one failure and one resize simulation are planned, each with a stated "
                  "expected outcome. The expected outcome is what matters — Part B compares actual "
                  "against it, and a simulation with no prediction cannot be compared to anything.",
         given=2, blank_rows=3,
         table=(["#", "Simulation", "What you will do", "What you expect", "How you will know"],
                [["F1", "Instance failure", "terminate one application instance",
                  "the LMS stays reachable; the ASG launches a replacement",
                  "browser stays up; ASG activity shows the replacement"],
                 ["F2", "Database failover", "reboot the database with failover",
                  "brief interruption, then service resumes on the standby",
                  "RDS events show the failover; LMS loads again within a minute or two"],
                 ["R1", "Resize", "change the ASG desired capacity, or the database instance class",
                  "capacity changes with no loss of service",
                  "new instance enters service; availability measurement shows no gap"]])),
]

# ---------------------------------------------------------------- Part B — implementation
# from_q — the Part A task whose answer this task builds (None for task 19)

BUILD = [
    dict(n=19, title="Deploy the baseline environment",
         from_q=None,
         job="Deploy the lab-pack your assessor provided. It builds the environment described at the "
             "start of Part A, so that everyone starts the maintenance window from the same place.",
         steps=["Download the lab-pack template from wherever your assessor has made it available.",
                [("Set your region before anything else — the stack builds into whichever region "
                  "is selected. For the scenario this is Sydney, ap-southeast-2; use it if the "
                  "region selector offers it. ", False),
                 ("If you are working in AWS Academy Learner Lab or a similar restricted "
                  "environment, Sydney will not be listed — choose us-east-1, or whichever region "
                  "you do have. The template builds the same thing in any region.", True)],
                "Open CloudFormation → Create stack → Upload a template file, and select it.",
                "Give the stack a name. Every parameter is defaulted except the database master "
                "password — type one of at least 8 characters and keep a note of it. Then "
                "launch the stack.",
                "Wait until the stack reads CREATE_COMPLETE. This takes 10–15 minutes.",
                "Open the load balancer's DNS name in a browser and confirm the placeholder page loads. Type http:// in front of it — the load balancer only listens on HTTP port 80, and a browser left to itself will try HTTPS and fail."],
         note="if the stack fails, read the Events tab — the first failure in the list is the cause; the "
              "rest are rollbacks of it. Tell your assessor before you start again.",
         capture="the stack at CREATE_COMPLETE, and the placeholder page loading through the load balancer.",
         uoc=["ICTCLD502 PE 4"],
         standard="the baseline is deployed and serving. This task evidences console/CLI use; it is not "
                  "assessing the student's design, which has not been built yet."),

    dict(n=20, title="Create the application subnet in the second zone",
         from_q=7,
         job="Create the subnet you designed. Copy your own answer across first, then build exactly that.",
         capture="the subnet list filtered to yat-lms-vpc, showing your new subnet and its Availability Zone.",
         uoc=["ICTCLD502 PC 4.1", "ICTCLD502 PE 1"],
         standard="a private application subnet exists in the second availability zone and matches what "
                  "the student designed in task 7. The CIDR is context — any non-overlapping range "
                  "inside the VPC is fine."),

    dict(n=21, title="Give the new subnet a path out",
         from_q=11,
         job="Build the outbound path you designed. If you designed a second NAT gateway, create it and "
             "its route table now. If you accepted the shared gateway, associate the new subnet with the "
             "existing private route table instead — and say so in the box.",
         note="a NAT gateway takes a few minutes to become Available. You cannot route to it until it is.",
         capture="the route table associated with your new subnet, showing its 0.0.0.0/0 route and the "
                 "target it points at.",
         uoc=["ICTCLD502 PC 4.1"],
         standard="the new subnet has a working outbound route, built to whichever option the student "
                  "designed. Both options are satisfactory. A subnet with no route out is not."),

    dict(n=22, title="Extend the application tier across both zones",
         from_q=8,
         job="Edit the Auto Scaling group to match your design — the subnets it launches into, and its "
             "capacity. Then wait for the second instance to launch and become healthy.",
         note="a new instance is not healthy the moment it launches. It has to boot and install its "
              "web server first, and while that happens the target group reports it Unhealthy with "
              "Request timed out — correctly, because nothing is listening on port 80 yet. On "
              "Windows it takes about six minutes, and can take ten. Wait for it. Do not change "
              "settings, terminate the instance or start over: an instance that looks stuck is "
              "almost always one that is still installing, and intervening is how you turn a "
              "five-minute wait into a rebuild.",
         capture="the Auto Scaling group's instances, showing instances in two different Availability "
                 "Zones, and the target group showing both healthy.",
         uoc=["ICTCLD502 PC 4.1", "ICTCLD502 PE 2"],
         standard="the group runs across two availability zones with a minimum of at least two, and both "
                  "instances are healthy in the target group. The exact minimum, maximum, warm-up and "
                  "scaling target are context. A group left at minimum 1, or confined to one subnet, does "
                  "not evidence the item.",
         assessor_note="this is the task where the copy-forward matters most. Check the student's task "
                       "8 answer against what they built — the item is that they implemented their own "
                       "design, not that they arrived at the same numbers as anyone else."),

    dict(n=23, title="Convert the database",
         from_q=10,
         job="Apply the database change you designed. Start this before the alarms task — it runs in the "
             "background and takes the longest of anything in this window.",
         note="apply it immediately rather than in the next maintenance window, or it will not have "
              "happened by the time you need to test it. The database stays available while it converts; "
              "the brief interruption comes later, when you fail it over.",
         capture="the database's Configuration tab showing Multi-AZ, and the zone its standby is in.",
         uoc=["ICTCLD502 PC 4.1", "ICTCLD502 PE 1"],
         standard="the database is running with a standby in a second availability zone and the "
                  "application still reaches it. This is the item that carries the fault-tolerance "
                  "requirement for the data tier — there is no alternative configuration that meets it "
                  "within the recovery targets."),

    dict(n=24, title="Build your HA monitoring",
         from_q=12,
         job="Create the alarms you designed, notifying the existing yat-lms-alerts topic. Build at least "
             "the first one; build the others if the window allows.",
         capture="your new alarm or alarms in the CloudWatch console, showing the metric, the threshold "
                 "and the state.",
         uoc=["ICTCLD502 PC 4.3", "ICTCLD502 PE 5"],
         standard="at least one alarm exists that would reveal a loss of availability the baseline pair "
                  "would miss, and it is the one the student designed. Thresholds are context."),
]

# ---------------------------------------------------------------- tests and simulations

TESTS = [
    dict(n="T1", title="Confirm every tier still works, in both zones",
         job="Before you break anything deliberately, confirm the environment you have just changed is "
             "healthy. A simulation against a broken environment tells you nothing.",
         steps=["Open the load balancer's DNS name in a browser — with http:// in front — and "
                "confirm the placeholder page loads.",
                "Open the target group and confirm both instances are healthy, in two different zones.",
                "Connect to one instance with Session Manager and run the first command below. "
                "TcpTestSucceeded : True means the application tier reaches the database privately. "
                "Get the endpoint from RDS → Databases → your database → Connectivity & security.",
                "Now run the same command on your OWN computer, not on the instance — the second one "
                "below. It must FAIL. That timeout is the evidence: the database has no public "
                "address and its security group accepts the application tier only. Confirm it "
                "alongside RDS → Connectivity & security, where Publicly accessible reads No."],
         code=("Run these", ["# on the instance, via Session Manager - expect TcpTestSucceeded : True",
                             "Test-NetConnection <YOUR-DB-ENDPOINT> -Port 3306",
                             "",
                             "# on your own computer - expect it to time out and fail",
                             "# Windows, in PowerShell:",
                             "Test-NetConnection <YOUR-DB-ENDPOINT> -Port 3306",
                             "# macOS or Linux, in Terminal:",
                             "nc -zv -w 10 <YOUR-DB-ENDPOINT> 3306"]),
         capture="the browser showing the page, the target group showing two healthy targets in two "
                 "zones, the port test from the instance returning TcpTestSucceeded : True, and the "
                 "same test from your own computer failing.",
         uoc=["ICTCLD502 PC 4.2"],
         standard="connectivity is demonstrated at every tier and across both zones — public entry "
                  "through the load balancer, application to database privately, and the database still "
                  "closed to the internet. A test run against only one zone has not demonstrated the "
                  "item."),

    dict(n="T2", title="Failure simulation",
         job="Run the failure simulation you planned in task 18. Watch what happens to the LMS while "
             "you do it — that is the evidence, not the console screen afterwards.",
         steps=["Open the load balancer's address in a browser (http://, not https://) and set it refreshing, or keep reloading "
                "it by hand. This is how you will see whether the LMS stayed up.",
                "Execute the failure you planned — terminate an instance, or reboot the database with "
                "failover.",
                "Record the time it happened, what the browser did, and how long before it was normal "
                "again.",
                "Confirm the environment recovered — the Auto Scaling group replaced the instance, or "
                "the database came back on its standby."],
         note="if the LMS goes down and stays down, stop and fix it before continuing. A failed "
              "simulation you recovered from and documented is worth more than one you skipped.",
         capture="three things, whichever simulation you ran: the ACTION you took (the terminating instance, or the RDS event showing the failover); the SERVICE while it happened (your browser still loading the page — include a clock or timestamp if you can); and the RECOVERY (the Auto Scaling group activity showing the replacement, or the target group returning to healthy). If the service did go down, capture that honestly — a recorded outage is evidence, and you compare it against what you predicted in task 18.",
         uoc=["ICTCLD502 PC 4.4", "ICTCLD502 PE 3"],
         standard="a real failure was executed against the student's own environment and the outcome "
                  "recorded with timings. The item is demonstrating fault tolerance, so the service "
                  "surviving matters — but a simulation that exposed a gap, honestly recorded and then "
                  "addressed in task 20, also evidences it. “I would have tested” does not."),

    dict(n="T3", title="Resize simulation",
         job="Run the resize simulation you planned in task 18, and measure what it costs in "
             "availability.",
         steps=["Keep the browser refreshing against the load balancer.",
                "Execute the resize you planned — change the desired capacity, or the database instance "
                "class.",
                "Record how long the change took and whether the LMS was affected at any point.",
                "Return the setting to where it was."],
         capture="the resize in progress or complete, and what the service did while it happened.",
         uoc=["ICTCLD502 PC 4.5"],
         standard="a resize was executed and its availability impact measured, not estimated. Finding "
                  "that the impact was nil is a valid result if it is supported by observation."),

    dict(n="T4", title="Measure availability across the window",
         job="You have been changing a production system for the last few hours. Report what the LMS's "
             "availability actually was across that time, and say how you measured it.",
         steps=["Open the load balancer's monitoring, or the target group's healthy-host metric, for the "
                "period of your maintenance window.",
                "Identify every period where the service was not serving — your simulations will show "
                "up here.",
                "Write one or two sentences reading the graph: whether the service stayed up, and "
                "what any dips were. A dip in one zone is not an outage if the other kept "
                "serving.",
                "Note the time range on the capture, so the period it covers is unambiguous."],
         capture="the metric graph across the whole window, both zones of the current target group, with "
"the time range visible.",
         uoc=["ICTCLD502 PC 4.3", "ICTCLD502 PE 5"],
         standard="the student set the measurement up, captured it across the window, and can say "
                  "what it shows. That is the whole of [ICTCLD502 PC 4.3] and [ICTCLD502 PE 5] — "
                  "define, monitor, record. Neither item asks for a percentage, and this graph "
                  "cannot honestly support one: it is stacked, its axis steps in tens of minutes, "
                  "and a short outage is invisible on it. Do NOT ask for a calculation here. "
                  "Knowledge question Q3 carries [ICTCLD502 KE 6] and asks for one explicitly, "
                  "worked from the student's own timings during the simulations rather than from "
                  "this graph. What fails here is a capture of the wrong period, of the wrong "
                  "target group, or a reading that calls a single-zone dip an outage.",
         assessor_note="expect somewhere between 99.5% and 99.9% across the window depending on how long "
                       "the failover blip ran. The figure is not the point; the measurement is."),
]

# ---------------------------------------------------------------- closing out

CLOSEOUT = [
    dict(n=25, title="What actually happened, against what you predicted",
         prompt="Go back to task 18. For each simulation, put your expected outcome next to what "
                "actually happened. Where they differ, say why. Where they matched, say what that "
                "confirms about your design.",
         uoc=["ICTCLD502 PC 4.6"],
         standard="every planned simulation is compared against its own predicted outcome and "
                  "divergences are explained. This is the item that makes the task 18 plan load-"
                  "bearing. “Everything worked as expected” with no specifics has not compared "
                  "anything.",
         table=(["#", "What you expected (task 18)", "What actually happened", "Why they differ"],
                [["F1", "LMS stays up; ASG replaces the instance", "LMS stayed up; replacement healthy after ~4 min", "—"],
                 ["F2", "brief interruption, then service resumes", "≈ 50 s unreachable, then normal",
                  "failover is not instant — the application reconnects after DNS updates"],
                 ["R1", "capacity changes with no loss of service", "no interruption observed", "—"]])),

    dict(n=26, title="What you changed as a result",
         prompt="Did your simulations reveal anything you needed to fix? If so, say what you changed and "
                "why. If nothing needed changing, say that — and say what evidence makes you confident, "
                "rather than just that nothing broke.",
         uoc=["ICTCLD502 PC 5.1"],
         standard="either an adjustment is documented with its reason, or the absence of one is justified "
                  "from evidence. Both are satisfactory. What is not satisfactory is a simulation that "
                  "clearly exposed a gap — a failover longer than the recovery target, an alarm that "
                  "never fired — with nothing recorded against it.",
         points=["If something was adjusted: what, why, and what the simulation showed that prompted it.",
                 "If nothing was: the evidence that supports leaving it — the measured figures against the targets.",
                 "A gap the simulations exposed and the student ignored is the failure condition here."]),

    dict(n=27, title="Hand it over",
         resources=[
             ("Change Management Procedure — the feedback and approval steps this engagement closes through",
              f"{SITE}/intranet/s1-cl1-at3/policies/change-management"),
         ],
         prompt="Take your completed work to Sam Walker, the YAT ICT Manager — your assessor plays this "
                "role. Walk them through what you changed and what the simulations showed. Record the "
                "feedback you get, your response to it, and anything you changed as a result.",
         uoc=["ICTCLD502 PC 5.2"],
         standard="feedback was sought from the stakeholder, recorded, and responded to. A response of "
                  "“no change required, because…” is a response. An empty feedback record is not — "
                  "the item is confirming, seeking and responding, all three.",
         table=(["Feedback received", "From", "Your response", "What you changed"],
                [["e.g. can the LMS survive losing a whole zone?", "Sam Walker, YAT ICT Manager",
                  "walked through the F1 and F2 results", "none — evidence already covered it"]])),

    dict(n=28, title="File it",
         resources=[
             ("Records Management Policy — where a completed engagement document has to be filed",
              f"{SITE}/intranet/s1-cl1-at3/policies/records-management"),
             ("Backup and Retention Policy — how long it has to be kept once it is there",
              f"{SITE}/intranet/s1-cl1-at3/policies/backup-retention"),
         ],
         prompt="File this completed workbook where YAT's records procedures require, so YAT ICT can "
                "find it after the engagement ends. State where you filed it and which YAT policy "
                "required that location.",
         uoc=["ICTCLD401 PC 4.3"],
         standard="the student names the actual location and the policy that governs it — the Records "
                  "Management Policy, or the Backup and Retention Policy. “I would file it "
                  "appropriately” has not evidenced the item.",
         points=["Names the actual location the workbook was filed in, not a general intention.",
                 "Names the YAT policy that requires that location.",
                 "The policy is on the intranet — a student who guesses has not read it."]),
]

# ---------------------------------------------------------------- knowledge questions

QUESTIONS = [
    dict(n="Q1", uoc=["ICTCLD502 KE 4"],
         q="Choose at least three of these and explain each in your own words, then say where it "
           "appears in your own work and how it shaped a decision you made: fault tolerance, single "
           "points of failure, reliability (MTTF / MTTR / MTBF), recoverability (RPO / RTO), service "
           "level agreements, vertical versus horizontal scalability.",
         points=["At least three concepts, defined in the student's own words rather than quoted.",
                 "Each one located in their own design or build — 'RPO is why I chose Multi-AZ over a "
                 "nightly backup', not a textbook definition.",
                 "A decision traced to the concept, showing it did work rather than decorating the answer.",
                 "Fewer than three concepts, or three concepts with no reference to their own work, is not satisfactory."]),

    dict(n="Q2", uoc=["ICTCLD502 KE 5"],
         q="From your own testing: (a) how did you avoid creating a new single point of failure while "
           "you were testing? (b) something did not go as expected at some point — how did you work out "
           "what was causing it? If nothing went wrong, describe how you would have isolated the most "
           "likely problem.",
         points=["(a) A real technique — e.g. keeping one zone untouched while failing the other, so "
                 "there was always a known-good comparison.",
                 "(b) A diagnostic approach, not a guess — checking the RDS event log and the target "
                 "group health before concluding where a failure was.",
                 "Both halves answered. One half is half the item."]),

    dict(n="Q3", uoc=["ICTCLD502 KE 6"],
         resources=[
             ("LMS Cloud Migration Requirements — the availability target your measurement is reported against",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
         ],
         q="Which tools did you use to measure the availability impact of a failure? Show the "
           "calculation you did for one specific simulation, using your own timing data, and name one "
           "thing your method could not see.",
         points=["Names the actual tools used — CloudWatch metrics, the target group health history, the "
                 "RDS event log, a browser refresh.",
                 "Shows a real calculation with their own numbers, not a formula.",
                 "Names a genuine limitation — e.g. a refresh every few seconds cannot see a shorter blip.",
                 "A student who cannot show the calculation has not measured anything."]),

    dict(n="Q4", uoc=["ICTCLD502 KE 7"],
         resources=[
             ("LMS Cloud Architecture — Baseline Design — which services the environment uses, so you can draw the responsibility line for each",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/cloud-architecture-baseline"),
         ],
         q="For the services in your environment — the load balancer, the database, object storage — "
           "explain which fault tolerance AWS provides for you and which you had to design yourself. Be "
           "precise about where the line falls for each.",
         points=["Load balancer: capable of spanning zones from the moment it is created, but you choose "
                 "which zones — and this environment already had both.",
                 "Database: single-AZ by default; the standby and automatic failover are something you "
                 "design and enable.",
                 "Object storage: redundant across zones within a region by default; cross-region needs "
                 "replication configured.",
                 "The distinction is drawn per service, not asserted generally."]),

    dict(n="Q5", uoc=["ICTCLD502 KE 8"],
         q="Load balancing and autoscaling deliver something together that neither delivers alone. "
           "Explain what, then point to the specific moment in your own testing where that combination "
           "was what kept the LMS up.",
         points=["The load balancer routes away from unhealthy targets; the scaling group makes sure "
                 "healthy targets exist. Either alone leaves a gap.",
                 "Tied to their own F1 result: the instance was terminated, the load balancer stopped "
                 "sending to it, the group launched a replacement.",
                 "A generic description with no reference to their own simulation does not meet the item."]),

    dict(n="Q6", uoc=["ICTCLD502 KE 9"],
         q="Name one high-availability metric you configured in task 12 and built in task 24. State "
           "what it measures, the threshold you set, why that threshold, and the failure it would catch "
           "that the baseline alarms would have missed.",
         points=["A real metric from their own build.",
                 "A threshold with a reason behind it, not a default.",
                 "The failure it catches, stated as something the two baseline alarms could not see — "
                 "e.g. one zone dark while the service still looks up."]),
]

# ---------------------------------------------------------------- reflections

REFLECTIONS = [
    dict(n="R1", title="Decisions in hindsight",
         resources=[
             ("LMS Cloud Migration Requirements — the service levels a monitoring metric would report against",
              f"{SITE}/intranet/s1-cl1-at3/projects/lms-cloud-infrastructure/migration-requirements"),
         ],
         prompt="Name one decision in your HA work you would make the same way again, and why it proved "
                "right. Then name one you would revise, and what you would do differently.",
         points=["Both halves present — a validated decision and a revised one.",
                 "Specific to their own design and build, not general observations about cloud work.",
                 "An answer where everything went perfectly has not reflected."]),

    dict(n="R2", title="Working under time pressure",
         prompt="Describe a moment in the maintenance window where something did not go as expected and "
                "you had to decide how to respond — what happened, how you diagnosed it, and the call "
                "you made. If nothing went wrong, say so honestly and describe the problem you were "
                "watching for and how you would have handled it.",
         points=["A real moment, with the decision that was made and the reasoning behind it.",
                 "Or an honest statement that nothing went wrong, with the contingency they were holding.",
                 "The item is judgement under pressure, not whether they had a crisis."]),

    dict(n="R3", title="What you would carry forward",
         prompt="Describe one lesson from this work that you would take into a future cloud project. Say "
                "how you arrived at it — what happened here that taught it to you — and why it would "
                "apply somewhere else.",
         points=["A lesson traced to something that actually happened during the work.",
                 "Applied beyond this project — the item is about carrying an idea into a new context.",
                 "A restatement of what they built is not a lesson."]),
]

# ---------------------------------------------------------------- rendering


def _element(doc, h2, el, mode, label="Task", notes=False):
    """A Part A design task or a close-out task — prompt, tags, capture. Both carry performance
    criteria, so both are framed as tasks; only the knowledge section asks questions."""
    R.flag(doc, f"{label} {el['n']}")
    h2(el["title"])
    R.p(doc, el["prompt"], after=6)
    if el.get("resources"):
        R.resources_block(doc, el["resources"])
    if el.get("table"):
        cols, rows = el["table"]
        R.design_table(doc, cols, rows, mode,
                       blank_rows=el.get("blank_rows", 3), given=el.get("given", 0),
                       exemplar=el.get("exemplar", 0))
    if el.get("points"):
        R.response_slot(doc, None, mode, points=el["points"])
    if el.get("diagram"):
        R.diagram_slot(doc, el["diagram"], mode)
    R.uoc_line(doc, el.get("uoc", []), mode)
    if el.get("standard"):
        R.standard_line(doc, el["standard"], mode)
    if el.get("consider"):
        R.consider(doc, el["consider"])
    if notes:
        R.notes_box(doc)


def render_front_matter(doc, h1):
    h1("Scenario")
    for para in SCENARIO:
        R.p(doc, para, after=8)
    h1("Required resources (assessment conditions)")
    for label, url in RESOURCES:
        par = doc.add_paragraph()
        par.paragraph_format.left_indent = R.Cm(0.6)
        par.paragraph_format.space_after = R.Pt(6)
        par.add_run("•  ").font.size = R.Pt(R.BODY_PT)
        R.add_hyperlink(par, label, url, size_pt=R.BODY_PT)
    R.p(doc, ASSESSOR_PROVIDES, after=8, italic=True, size=9.5, colour=R.GREY)
    h1("Instructions to Student")
    for para in INSTRUCTIONS:
        R.p(doc, para, after=8)


def report_evidence(evidence_dir, build=None, tests=None):
    """What the exemplar folder covers, printed at build time so a gap is not silent."""
    build = BUILD if build is None else build
    tests = TESTS if tests is None else tests
    keys = [f"task-{t['n']}" for t in build] + [f"test-{t['n'].lower()}" for t in tests]
    found = {k: R.evidence_images(evidence_dir, k) for k in keys}
    missing = [k for k, v in found.items() if not v]
    placed = sum(len(v) for v in found.values())
    print(f"Exemplar evidence: {placed} capture(s) placed across "
          f"{len(keys) - len(missing)}/{len(keys)} tasks and tests.")
    if missing:
        print(f"  NO CAPTURE ON FILE for: {', '.join(missing)} — "
              f"these render as the description alone.")
    orphans = sorted(p.name for p in Path(evidence_dir).glob("*.png")
                     if not any(p in v for v in found.values()))
    if orphans:
        print(f"  NOT PLACED (name matches no task or test): {', '.join(orphans)}")


def render(doc, h1, h2, mode="student", design=None, build=None, tests=None,
           closeout=None, questions=None, reflections=None, current_arch=None,
           network_diagram=None, notes=False, evidence_dir=None):
    """Render the whole workbook into `doc`. mode = student | assessor.

    The content lists default to AT3's own. The PRACTICE sheet passes its own — same
    renderer, same shapes, Ledgerline instead of the LMS — so the two can never drift
    structurally even though every value in them differs.

    evidence_dir — a folder of exemplar captures from a worked run (see
    `run_sheet_render.evidence_images` for the naming). When given AND mode is assessor, each
    Part B evidence box carries the real screenshot under its description instead of the
    description alone, so a regenerated assessor copy is worked rather than blank. Defaults to
    None: the student and practice sheets render exactly as before and cannot pick these up.
    """
    DESIGN_ = DESIGN if design is None else design
    BUILD_ = BUILD if build is None else build
    TESTS_ = TESTS if tests is None else tests
    CLOSEOUT_ = CLOSEOUT if closeout is None else closeout
    QUESTIONS_ = QUESTIONS if questions is None else questions
    REFLECTIONS_ = REFLECTIONS if reflections is None else reflections
    # ---- Part A ----
    h1("Part A — Design")
    h2("The environment you are hardening")
    for para in CURRENT_ARCH_INTRO:
        R.p(doc, para, after=6)
    R.settings_table(doc, current_arch or CURRENT_ARCH)
    label, url = network_diagram or NETWORK_DIAGRAM
    par = doc.add_paragraph()
    par.paragraph_format.space_after = R.Pt(4)
    par.add_run("\u2022  ").font.size = R.Pt(R.BODY_PT)
    R.add_hyperlink(par, label, url, size_pt=R.BODY_PT)
    R.p(doc, "Your work in this assessment is the AWS side only — the campus network is not yours to "
             "change and is not in scope.", italic=True, size=9.5, colour=R.GREY, after=10)
    for el in DESIGN_:
        _element(doc, h2, el, mode, notes=notes)

    # ---- Part B ----
    h1("Part B — Implementation")
    R.p(doc, "Your maintenance window is about 3.5 hours. Work the tasks in order — the order you "
             "planned in task 17 is the one to follow where it differs from the numbering here.",
        italic=True, size=9.5, colour=R.GREY, after=10)
    for task in BUILD_:
        R.flag(doc, f"Task {task['n']}")
        h2(task["title"])
        R.p(doc, task["job"], after=6)
        if task.get("resources"):
            R.resources_block(doc, task["resources"])
        if task.get("from_q"):
            # Columns, model rows and scaffolding all come from the Part A task this builds,
            # so the copy-forward table cannot drift from the design task it copies. The
            # assessor copy shows that task's model answer filled in — what a correctly
            # carried-forward design looks like; the student copy is theirs to fill.
            src = next(d for d in DESIGN_ if d["n"] == task["from_q"])
            cols, rows = src["table"]
            R.p(doc, f"From your design — copy your answer to task {task['from_q']} into this "
                     f"table before you build.", bold=True, size=9.5, after=3)
            # `exemplar` is deliberately NOT carried across. In Part A it shows the shape of an
            # answer; here the instruction is to copy your own answer in, and a worked row
            # sitting where that answer goes contradicts it.
            R.design_table(doc, cols, rows, mode,
                           blank_rows=src.get("blank_rows", 3),
                           given=src.get("given", 0))
        if task.get("steps"):
            R.steps(doc, task["steps"])
        if task.get("clicks"):
            R.clicks(doc, task["clicks"])
        if task.get("code"):
            label, lines = task["code"]
            R.p(doc, label, bold=True, after=3)
            R.code(doc, lines)
        if task.get("note"):
            R.note(doc, task["note"])
        if task.get("assessor_note"):
            R.assessor_note(doc, task["assessor_note"], mode)
        R.p(doc, "Evidence", bold=True, after=3)
        R.place_evidence(doc, [task["capture"]], mode,
                         R.evidence_images(evidence_dir, f"task-{task['n']}"))
        if notes:
            R.notes_box(doc)
        R.uoc_line(doc, task["uoc"], mode)
        R.standard_line(doc, task["standard"], mode)

    # ---- tests ----
    h1("Testing and simulation")
    R.p(doc, "These prove the design works. Run them yourself and record what actually happened — a "
             "simulation that exposed a problem you then fixed is worth more than one you skipped.",
        italic=True, size=9.5, colour=R.GREY, after=10)
    for test in TESTS_:
        R.flag(doc, f"Test {test['n']}")
        h2(test["title"])
        R.p(doc, test["job"], after=6)
        if test.get("resources"):
            R.resources_block(doc, test["resources"])
        R.steps(doc, test["steps"])
        if test.get("clicks"):
            R.clicks(doc, test["clicks"])
        if test.get("code"):
            label, lines = test["code"]
            R.p(doc, label, bold=True, after=3)
            R.code(doc, lines)
        if test.get("note"):
            R.note(doc, test["note"])
        if test.get("assessor_note"):
            R.assessor_note(doc, test["assessor_note"], mode)
        R.p(doc, "Evidence", bold=True, after=3)
        R.place_evidence(doc, [test["capture"]], mode,
                         R.evidence_images(evidence_dir, f"test-{test['n'].lower()}"))
        if notes:
            R.notes_box(doc)
        R.uoc_line(doc, test["uoc"], mode)
        R.standard_line(doc, test["standard"], mode)

    # ---- closing out ----
    h1("Closing the engagement")
    for el in CLOSEOUT_:
        _element(doc, h2, el, mode, notes=notes)

    # ---- knowledge questions ----
    if QUESTIONS_:
        h1("Knowledge questions")
        R.p(doc, "Answer each question about your own design and your own build. Refer to what you actually "
                 "decided and what actually happened.", italic=True, size=9.5, colour=R.GREY, after=10)
        for q in QUESTIONS_:
            R.flag(doc, f"Knowledge question {q['n'][1:]}")
            h2(q["q"][:70] + ("…" if len(q["q"]) > 70 else ""))
            R.p(doc, q["q"], after=6)
            if q.get("resources"):
                R.resources_block(doc, q["resources"])
            R.response_slot(doc, None, mode, points=q["points"])
            R.uoc_line(doc, q["uoc"], mode)
    # ---- reflections ----
    if REFLECTIONS_:
        h1("Reflection")
        R.p(doc, "Reflect on your own work — your judgement and your experience, not a summary of what you "
                 "built. An honest “here is what I would change” earns more credit than “everything "
                 "went perfectly”.", italic=True, size=9.5, colour=R.GREY, after=10)
        for r in REFLECTIONS_:
            R.flag(doc, f"Reflection {r['n'][1:]}")
            h2(r["title"])
            R.p(doc, r["prompt"], after=6)
            R.response_slot(doc, None, mode, points=r["points"])
            R.uoc_line(doc, ["ICTCLD401 FS Learning", "ICTCLD401 FS Self-management skills",
                             "ICTCLD502 FS Problem solving", "ICTCLD502 FS Self-management"], mode)
