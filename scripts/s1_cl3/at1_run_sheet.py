#!/usr/bin/env python3
"""The S1-CL3 AT1 improvement-design workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), through the shared workbook engine in
the umbrella (`helpers/run_sheet.py`).

WHY THERE IS NO SOLUTION DESIGN TEMPLATE. ICTCLD504's assessment conditions (AC 1–8) are all
environment and input conditions — a vendor, a managed database service, console/CLI tooling, an
IDE, requirements and standards, a browser, an SSH/RDP client. None names a document format or a
reporting standard, so `[ICTCLD504 PC 2.4]` "Document and present proposed architecture for
review to required personnel" is satisfied by this worksheet (the documenting) plus Part B (the
presenting). Same finding as ICTCLD503 and ICTCLD505; the only unit in this course that does
require a document is ICTCLD501, via `[ICTCLD501 AC 3]`.

THE IMPROVEMENT IS OPEN. This is the thing that separates CL3 from CL1's AT3. There is no
target architecture and no planted set of faults to find. The Improvement Requirements are
framed as outcomes — stable, reliable, fit for purpose, compliant — and IR-2 asks for sound
engineering proportionate to an internal, business-hours finance system, explicitly not
gold-plating. So a student who proposes every available improvement has not done better than one
who proposes three and justifies each; they have done worse, because IR-2 and IR-6 both ask for
justification against business need. The `standard` lines below are written to mark that.

STARTING STATE. Ledgerline sits at the single-AZ cloud baseline it reached during the migration:
one application instance in one availability zone, a single-AZ database, one NAT gateway. It
runs on Amazon Linux with a managed PostgreSQL database, and the vendor supports a
high-availability deployment with an automatic-failover standby — so database-tier resilience is
available to the student's design if they judge it warranted. Whether it IS warranted for an
internal business-hours system is exactly the proportionality judgement the cluster is testing.

THE MARKING MODEL. Values here are ours, invented so the student has a concrete task. Each
element carries the `uoc` items it evidences and a `standard` naming what must be true for them
to be met. An assessor marks the standard, never the table. Because the improvement is open,
most standards here are about the REASONING rather than the answer: a student who leaves the
database single-AZ and argues it against the recovery need and the cost has met the item, and so
has one who converts it and argues that.
"""

from helpers import run_sheet as R  # noqa: E402  (the shared workbook engine, in the umbrella)

SITE = "https://yat.timbaird.com"
STATE = "s1-cl3-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/ledgerline-improvement"
MIGRATION = f"{SITE}/intranet/{STATE}/projects/accounting-cloud-migration"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"
REFERENCE = f"{SITE}/intranet/{STATE}/reference"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "YAT College's offshore partnership in India has put a spotlight on the systems that support "
    "it. Ledgerline — YAT's finance and office-administration system — was migrated to AWS in an "
    "earlier engagement and has run there since, but it was migrated as-is: everything sits in one "
    "availability zone, and nothing has been revisited since the cutover.",
    "You are an MTS Consultant on this engagement, reporting to Pat Lin (MTS Senior Consultant). "
    "Sam Walker (YAT ICT Manager) is your primary stakeholder, with YAT Finance as the business "
    "owner of the system.",
    "MTS has been engaged to confirm Ledgerline is stable, reliable, fit for purpose and compliant "
    "with the Indian regulatory requirements that now apply — and to improve it where it is not. "
    "What that improvement consists of is your analysis to make.",
]

RESOURCES = [
    ("Improvement Requirements — the outcomes IR-1 to IR-7 this engagement is held to",
     f"{PROJECT}/improvement-requirements"),
    ("Indian Regulatory Requirements — the obligations the infrastructure is assessed against",
     f"{PROJECT}/indian-regulatory-requirements"),
    ("Accounting System Infrastructure Specifications — the current as-built environment",
     f"{ICT}/accounting-server-status-cloud"),
    ("Accounting System Application Specification — the workload, its users and its patterns",
     f"{ICT}/accounting-application-spec-cloud"),
    ("Accounting System Operational Costing — what the environment costs to run today",
     f"{ICT}/accounting-operational-costing-cloud"),
    ("Engagement Role Brief — your role, and what is in and out of scope for MTS",
     f"{PROJECT}/role-brief"),
]

ASSESSOR_PROVIDES = ("Everything this part needs is on the YAT intranet. Your assessor will tell "
                     "you the current address of the site.")

INSTRUCTIONS = [
    "This is an open-book assessment. You may use the YAT intranet, AWS documentation, and "
    "anything you have from class. What you may not use is another student.",
    "Work the tasks in order — each builds on the answer before it. They tell you what to decide; "
    "they do not tell you what to decide it to.",
    "There is no right answer waiting to be found. The Improvement Requirements are outcomes, not "
    "solutions, and IR-2 asks for improvements proportionate to an internal, business-hours "
    "finance system. Proposing every improvement available is not a better answer than proposing "
    "three you can justify — it is a worse one.",
    "Every improvement you propose must carry a cost-versus-benefit justification (IR-6). An "
    "improvement with no cost stated is not a proposal, it is a wish.",
    "This part is analysis and design only. You are not deploying anything — AT3 deploys the "
    "improvement YAT approves.",
]

# ---------------------------------------------------------------- the supplied current state

NETWORK_DIAGRAM = ("Network Diagram — the environment drawn out, including the campus it connects "
                   "back to", f"{ICT}/network-diagram-cl3")

CURRENT_ARCH_INTRO = [
    "This is the environment you are improving. It is what the migration built and handed over. "
    "Read it before you answer anything — several tasks below turn on noticing what is already "
    "there, and on not proposing to rebuild what already works.",
]

CURRENT_ARCH = [
    ("Region", "ap-southeast-2 (Sydney), with the whole workload in a single availability zone"),
    ("Workload", "Ledgerline Finance & Office Suite — general ledger, accounts payable and "
                 "receivable, student fee billing, procurement and asset management. Internal "
                 "back-office system; payroll is outsourced and does not run here."),
    ("Access path", "internal only — staff reach it from campus over the Site-to-Site VPN. No "
                    "public ingress."),
    ("Application tier", "Amazon Linux on general-purpose burstable instances, in an Auto Scaling "
                         "group with min 1 / desired 1 / max 2, in ledgerline-app-a only; target "
                         "tracking on CPU at 70%"),
    ("Load balancing", "Application Load Balancer across ledgerline-public-a and -b (a load "
                       "balancer requires two zones), HTTP :80 to ledgerline-tg"),
    ("Database", "Amazon RDS for PostgreSQL, single-AZ with no standby, gp3 20 GB, encrypted, "
                 "7-day backup retention, in ledgerline-data-a"),
    ("Storage", "block storage only — the instance root volume and the database storage. No object "
                "storage is in use."),
    ("Network", "ledgerline-vpc 10.20.0.0/16; public-a/-b, app-a, data-a/-b; a single NAT gateway "
                "in ledgerline-public-a"),
    ("Security groups", "ledgerline-alb-sg  HTTP 80 from anywhere  ·  ledgerline-app-sg  from the "
                        "load balancer group  ·  ledgerline-db-sg  PostgreSQL 5432 from the app "
                        "group only"),
    ("Monitoring", "two alarms — ledgerline-unhealthy-hosts (any unhealthy target) and "
                   "ledgerline-db-storage-low (free storage below 15%)"),
    ("Usage", "business hours only, Monday to Friday, roughly 07:30–18:00; effectively idle "
              "overnight and at weekends. Month-end close is the monthly peak at 45–55 concurrent "
              "users; end of financial year is the annual peak."),
    ("Target availability", "99.5% business-hours service"),
    ("Administrative access", "Systems Manager Session Manager — no key pair, no open management "
                              "port, no bastion host"),
]

SCOPE_NOTE = ("Your work is the cloud infrastructure. The Ledgerline application and its financial "
              "data are out of scope (IR-4) — the application continues to run unchanged, and no "
              "financial data may be lost.")

SIZING_NOTE = ("Instance and database classes throughout this environment are sized to what will "
               "actually launch in an AWS Academy Learner Lab, which caps what is available. "
               "Ledgerline's real finance workload would warrant considerably larger. Reason about "
               "sizing as you would at full scale — the reasoning is what is assessed, not the "
               "vCPU count.")

# ---------------------------------------------------------------- Part A — analyse and design

DESIGN = [
    # ---- element 1: analyse ----
    dict(n=1, title="Review the current architecture",
         resources=[
             ("Accounting System Infrastructure Specifications — the environment tier by tier",
              f"{ICT}/accounting-server-status-cloud"),
             ("Accounting System Cloud Architecture — Baseline Design — how it was designed at "
              "migration, and why", f"{MIGRATION}/solution-design"),
             ("Network Diagram — the environment drawn out", f"{ICT}/network-diagram-cl3"),
         ],
         prompt="Identify and review the architecture as it stands. Go tier by tier and record what "
                "is there, how it is configured, and what design decision it represents. You are "
                "not judging it yet — this task is establishing what you are looking at.",
         uoc=["ICTCLD504 PC 1.1", "ICTCLD504 FS Reading"],
         standard="every tier is identified from the supplied records rather than assumed, and the "
                  "student notes the deliberate decisions as decisions — single-AZ, internal-only "
                  "access, no object storage, burstable instance families. PC 1.1 is review, not "
                  "critique; a task 1 answer full of recommendations has jumped ahead and usually "
                  "means the student did not read the baseline design.",
         given=1, blank_rows=7,
         table=(["Tier", "What is there", "The design decision it represents"],
                [["Application", "one instance in an ASG (min 1, max 2), one availability zone",
                  "capacity was the concern at migration; resilience was deferred"],
                 ["Load balancing", "ALB across two public subnets, HTTP only",
                  "a load balancer needs two zones even when the workload uses one"],
                 ["Database", "RDS PostgreSQL, single-AZ, no standby, 7-day backups",
                  "migrated as-is; the standby was deferred with the rest"],
                 ["Network", "one VPC, five subnets, a single NAT gateway",
                  "sized for a single-zone workload"],
                 ["Access", "internal only, over the site-to-site VPN, Session Manager for admin",
                  "a deliberate and strong security posture — no public ingress, no bastion"],
                 ["Storage", "block storage only", "no static content, so none was needed"],
                 ["Monitoring", "two alarms — unhealthy hosts and low database storage",
                  "a baseline, covering availability and capacity but little else"]])),

    dict(n=2, title="Evaluate the architecture and identify the business impact",
         resources=[
             ("Accounting System Application Specification — who uses it, when, and how heavily",
              f"{ICT}/accounting-application-spec-cloud"),
             ("Improvement Requirements — the outcomes the current state is judged against",
              f"{PROJECT}/improvement-requirements"),
         ],
         prompt="Now evaluate it. For each design decision from task 1, say what it means for the "
                "business — not what it means technically. 'Single availability zone' is a fact; "
                "'a zone failure stops month-end close and finance cannot pay suppliers' is a "
                "business impact.",
         uoc=["ICTCLD504 PC 1.2", "ICTCLD504 FS Problem solving"],
         standard="impacts are expressed in business terms and are proportionate to what Ledgerline "
                  "actually is — an internal, business-hours system with outsourced payroll and a "
                  "99.5% target. A student who describes a zone outage as catastrophic for a system "
                  "that is idle overnight and at weekends has not evaluated it against the business; "
                  "neither has one who dismisses it because the system is 'only internal'. PC 1.2 is "
                  "about the impact of DESIGN DECISIONS, so each row must trace to one.",
         given=1, blank_rows=6,
         table=(["Design decision", "Business impact if it fails or falls short", "How serious"],
                [["Single availability zone",
                  "a zone failure takes finance offline until it is rebuilt elsewhere; during "
                  "month-end close that stops supplier payments and billing",
                  "significant, but bounded by business hours"],
                 ["Single application instance",
                  "an instance failure takes the system down until the ASG replaces it — minutes, "
                  "not hours", "moderate; the ASG already limits it"],
                 ["Single-AZ database with 7-day backups",
                  "a database failure means restoring from backup, with data loss back to the "
                  "restore point and hours of downtime",
                  "the most significant single exposure"],
                 ["Single NAT gateway",
                  "loss of outbound access — patching and external integrations stop; the system "
                  "itself keeps serving users", "low"],
                 ["HTTP only, no TLS",
                  "finance data crosses the campus network unencrypted", "significant for a finance "
                                                                        "system"],
                 ["Two alarms only",
                  "problems that are not an unhealthy host or low storage are found by users "
                  "reporting them", "moderate"]])),

    dict(n=3, title="Assess compliance against the Indian regulatory requirements",
         resources=[
             ("Indian Regulatory Requirements — the applicable instruments and what they oblige",
              f"{PROJECT}/indian-regulatory-requirements"),
             ("Privacy / Data Handling Policy — YAT's own obligations for the data held here",
              f"{POLICY}/privacy"),
         ],
         prompt="Assess the current infrastructure against the Indian Regulatory Requirements that "
                "now apply to the India-campus operation. Identify any gaps, and say what "
                "infrastructure change would close each one. You are designing to the compliance "
                "area's determination — you are not interpreting the law.",
         uoc=["ICTCLD504 AC 5", "ICTCLD504 FS Reading"],
         standard="the student works from the supplied determination rather than reasoning about "
                  "the law themselves, identifies the gaps that actually apply to an internal "
                  "finance system, and proposes infrastructure changes rather than policy. A student "
                  "who advises on the legal position has stepped outside the engagement's scope, "
                  "which the Role Brief and IR-3 both set explicitly.",
         given=1, blank_rows=5,
         table=(["Requirement", "Current position", "Gap", "Infrastructure change that closes it"],
                [["Log retention in-jurisdiction", "", "", ""],
                 ["Retrievability for incident reporting", "", "", ""],
                 ["Data handling and security safeguards", "", "", ""],
                 ["", "", "", ""],
                 ["", "", "", ""]])),

    dict(n=4, title="Identify design patterns and architectural options",
         resources=[
             ("Reference Architectures — the patterns YAT's architects work from",
              f"{REFERENCE}/reference-architectures"),
         ],
         prompt="Identify the design patterns and architectural options available to address what "
                "you found in tasks 2 and 3. You are building the menu here, not choosing from it — "
                "include options you will later reject, because rejecting an option with a reason is "
                "part of the design.",
         uoc=["ICTCLD504 PC 1.3", "ICTCLD504 KE 4"],
         standard="a genuine range of patterns is identified, with what each addresses — multi-AZ "
                  "deployment, managed-service failover, automated backup and restore, "
                  "infrastructure as code, edge or caching patterns where relevant, and monitoring "
                  "patterns. KE 4 (design principles for cloud applications) is evidenced by the "
                  "student framing these as principles — remove single points of failure, prefer "
                  "managed services, automate recovery — rather than as a product list.",
         given=1, blank_rows=7,
         table=(["Pattern or option", "What it addresses", "Where it would apply here"],
                [["Multi-AZ application tier",
                  "removes the single-zone and single-instance exposure",
                  "the Auto Scaling group, spread across two zones"],
                 ["Managed database failover standby",
                  "removes the database as a single point of failure, with automatic failover",
                  "the RDS instance — available on this engine and supported by the vendor"],
                 ["Automated backup and tested restore",
                  "recovery without a standby, at lower cost and higher recovery time",
                  "the alternative to a standby, if the cost is not justified"],
                 ["Redundant outbound path",
                  "removes the single NAT gateway exposure", "a NAT gateway per zone"],
                 ["Transport encryption",
                  "protects finance data in transit", "TLS terminating at the load balancer"],
                 ["Infrastructure as code",
                  "reproducibility, and the ability to rebuild elsewhere", "the whole environment; "
                                                                          "IR-5 asks for it"],
                 ["Broader monitoring and alerting",
                  "detection of the failure modes the two current alarms do not cover",
                  "the metrics you set in task 8"]])),

    dict(n=5, title="Assess the benefits against the current business model",
         resources=[
             ("Accounting System Operational Costing — what this environment costs today",
              f"{ICT}/accounting-operational-costing-cloud"),
         ],
         prompt="Determine and assess what the options from task 4 actually give YAT, against the "
                "way this business runs. Ledgerline is used by finance staff during business hours "
                "and is idle the rest of the time — that shapes what an improvement is worth. Say "
                "what each option costs and what it buys.",
         uoc=["ICTCLD504 PC 1.4", "ICTCLD504 KE 3", "ICTCLD504 KE 5"],
         standard="each option carries a cost posture and a benefit stated against Ledgerline's "
                  "actual operating profile. The strongest answers notice that an idle-overnight, "
                  "business-hours system changes the value of always-on redundancy, and that some "
                  "cloud benefits (elasticity) matter less here than others (managed recovery). "
                  "KE 3 and KE 5 are evidenced by the student reasoning about what cloud adoption "
                  "and migration bring to THIS system rather than in general.",
         given=1, blank_rows=6,
         table=(["Option", "What it costs", "What it buys, for this business"],
                [["Multi-AZ application tier",
                  "a second running instance — roughly doubles application compute",
                  "removes the zone and instance exposure; matters most during month-end close"],
                 ["Database standby",
                  "roughly doubles database cost, running continuously",
                  "automatic failover instead of a restore measured in hours"],
                 ["Automated backup and tested restore",
                  "near nothing beyond what is already retained",
                  "much of the protection at a fraction of the cost, at a slower recovery"],
                 ["NAT gateway per zone", "a second gateway, hourly",
                  "outbound survives a zone failure; low value if the tier does not"],
                 ["TLS at the load balancer", "a certificate — effectively nothing",
                  "finance data encrypted in transit; the cheapest improvement on this list"],
                 ["Infrastructure as code", "effort now, not run cost",
                  "reproducibility, reviewable change, and a rebuild path"]])),

    dict(n=6, title="Set the business goals",
         resources=[
             ("Improvement Requirements — IR-1 to IR-7, the outcomes these goals must serve",
              f"{PROJECT}/improvement-requirements"),
         ],
         prompt="Set the business goals this improvement is aiming at, across security, reliability, "
                "performance and cost. These are yours to determine — the Improvement Requirements "
                "give outcomes, not numbers. Make each one measurable, because in AT3 someone has to "
                "demonstrate whether it was met.",
         uoc=["ICTCLD504 PC 1.6", "ICTCLD504 PE 3"],
         standard="a goal is set in each of the four areas, each measurable and each defensible "
                  "against Ledgerline's profile. 'Improve reliability' is not a goal; 'business-hours "
                  "availability of 99.9%, up from 99.5%' is. PE 3 requires the student to determine "
                  "metrics AND business goals, so the pairing must be visible. Goals wildly beyond "
                  "the system's need (99.99% for a business-hours finance system) fail IR-2 and "
                  "should be marked as not proportionate.",
         given=1, blank_rows=5,
         table=(["Area", "Business goal", "Why this level, for this system"],
                [["Reliability", "raise business-hours availability from 99.5% to 99.9%",
                  "a zone or instance failure should not stop finance; overnight outages cost "
                  "nothing"],
                 ["Recovery", "restore service within 4 hours, losing no more than 1 hour of "
                              "financial data",
                  "a business day is the unit that matters; financial records cannot be lost"],
                 ["Security", "no finance data in transit unencrypted",
                  "cheap to fix and indefensible to leave"],
                 ["Cost", "no more than a modest increase in monthly run cost",
                  "IR-2 and IR-6 — proportionate to an internal system"],
                 ["Performance", "month-end close performance no worse than today",
                  "the peak that matters; nothing suggests it is currently a problem"]])),

    dict(n=7, title="Confirm your design decisions against business needs",
         prompt="Before you design in detail, confirm the direction. State the improvements you are "
                "going to propose, and for each name the business need from task 6 it serves and the "
                "option from task 4 you chose. Just as importantly, state what you are NOT proposing "
                "and why — that is where IR-2 is actually assessed.",
         uoc=["ICTCLD504 PC 1.5", "ICTCLD504 FS Self-management"],
         standard="the student commits to a proportionate set and can defend the exclusions. There "
                  "is no correct set: converting the database to a standby is defensible on the "
                  "recovery goal, and so is leaving it single-AZ with a tested restore if the cost "
                  "is argued against a business-hours system. What fails PC 1.5 is a proposal set "
                  "with no rejected options beside it, or one whose items do not trace to a task 6 "
                  "goal.",
         given=1, blank_rows=7,
         table=(["Proposing / not proposing", "Improvement", "The business need it serves"],
                [["Proposing", "spread the application tier across two availability zones",
                  "the reliability goal — removes the zone and instance exposure"],
                 ["Proposing", "TLS terminating at the load balancer",
                  "the security goal — finance data encrypted in transit"],
                 ["Proposing", "broader monitoring against the metrics set in task 8",
                  "reliability, and AT3 has to demonstrate the goals were met"],
                 ["Proposing", "define the environment as infrastructure as code",
                  "IR-5 — operable and reproducible by YAT ICT"],
                 ["Decide and justify", "the database — standby, or backup and tested restore",
                  "the recovery goal, weighed against cost; either is defensible if argued"],
                 ["Not proposing", "a second region",
                  "far beyond an internal business-hours system; fails IR-2"],
                 ["Not proposing", "larger instance classes",
                  "capacity is not the constraint — the specifications say so"]])),

    # ---- element 2: design ----
    dict(n=8, title="Evaluate and confirm the performance metrics",
         prompt="Confirm the metrics that will show whether the goals in task 6 were achieved. For "
                "each, say what is measured, where the measurement comes from, and what value counts "
                "as meeting the goal. In AT3 someone deploys this and has to demonstrate it against "
                "these metrics — write them so that is possible.",
         uoc=["ICTCLD504 PC 2.1", "ICTCLD504 PE 3"],
         standard="each metric names a real measurable source and a target value, and pairs with a "
                  "goal from task 6. A metric with no threshold cannot be demonstrated against, "
                  "which is what PC 2.1's 'evaluate and confirm' is asking for and what AT3 will "
                  "depend on.",
         given=1, blank_rows=6,
         table=(["Goal", "Metric", "Where it is measured", "Target value"],
                [["Availability", "healthy target count behind the load balancer",
                  "load balancer target health", "at least one healthy target in each zone"],
                 ["Availability", "successful request rate",
                  "load balancer request and error counts", "errors below a stated threshold"],
                 ["Recovery", "time to restore service in a test",
                  "a timed recovery exercise", "within 4 hours"],
                 ["Recovery", "recovery point achievable",
                  "backup frequency and retention", "no more than 1 hour of data"],
                 ["Security", "proportion of traffic encrypted in transit",
                  "the load balancer listener configuration", "all of it"],
                 ["Cost", "monthly run cost", "cost reporting for the tagged resources",
                  "within the increase agreed in task 6"]])),

    dict(n=9, title="Design — compute, storage, database and network",
         prompt="Select and design the improvements to the resources themselves. Go tier by tier and "
                "say what changes, what stays, and why. Where you are leaving something alone, say "
                "so explicitly — an unmentioned tier reads as an oversight rather than a decision.",
         uoc=["ICTCLD504 PC 2.2", "ICTCLD504 KE 9"],
         standard="all four resource types are addressed with a decision and a reason, including "
                  "explicit no-change decisions. KE 9 (features of cloud services and techniques to "
                  "improve security, reliability, scalability and cost) is evidenced by the student "
                  "naming the platform capability that delivers each improvement rather than "
                  "describing an outcome.",
         given=1, blank_rows=6,
         table=(["Resource", "Your design", "Why"],
                [["Compute", "Auto Scaling group across two zones, minimum 2",
                  "one instance per zone is what makes the tier survive a zone failure"],
                 ["Load balancer", "unchanged in placement; a TLS listener added",
                  "it already spans two zones — only the listener changes"],
                 ["Database", "your decision from task 7, designed out here", ""],
                 ["Storage", "unchanged — block storage on the instances and the database",
                  "no static content to move; adding object storage would evidence nothing"],
                 ["Network", "a NAT gateway in the second zone",
                  "otherwise the new zone's outbound path depends on the original zone"],
                 ["Subnets", "an application subnet in the second zone",
                  "the tier cannot spread into a zone with no subnet"]])),

    dict(n=10, title="Design — security improvements",
         resources=[
             ("Security & Incident Response Policy — YAT's security obligations",
              f"{POLICY}/security-incident"),
             ("User Access Policy — access control requirements",
              f"{POLICY}/user-access"),
         ],
         prompt="Review the security of the environment and design the improvements you judge "
                "necessary. Note what is already strong — this environment has some genuinely good "
                "decisions in it — and improve what is not.",
         uoc=["ICTCLD504 PC 2.3", "ICTCLD504 KE 8"],
         standard="the student recognises the existing strengths (no public ingress, Session "
                  "Manager rather than a bastion or key pairs, encrypted database storage, tight "
                  "security-group chaining) and does not propose replacing them. The real gap is "
                  "transport encryption. KE 8 (tools and uses of security layers) is evidenced by "
                  "the student describing security in layers — network, transport, identity, data — "
                  "rather than as a single control.",
         given=1, blank_rows=6,
         table=(["Layer", "Current position", "Your design"],
                [["Network", "no public ingress; access over the site-to-site VPN",
                  "unchanged — this is already the strongest thing about the environment"],
                 ["Transport", "HTTP only inside the VPC",
                  "TLS terminating at the load balancer"],
                 ["Identity and admin access", "Session Manager; no key pairs, no bastion",
                  "unchanged"],
                 ["Data at rest", "database storage encrypted", "unchanged; confirm for any new "
                                                                "storage"],
                 ["Security groups", "chained: load balancer → app → database",
                  "unchanged in shape; extend to the second zone's resources"],
                 ["Detection", "two alarms", "extended in task 12"]])),

    dict(n=11, title="Design — reliability and scalability improvements",
         prompt="Design the reliability and scalability improvements in detail. This is where your "
                "database decision from task 7 gets designed out properly — say exactly what you are "
                "doing and what recovery behaviour it produces. Be specific about what happens when "
                "each component fails.",
         uoc=["ICTCLD504 PC 2.3", "ICTCLD504 PE 1"],
         standard="each single point of failure identified in task 2 is either removed or "
                  "explicitly accepted with a reason, and the student can state the failure "
                  "behaviour of the improved design — what happens when an instance, a zone, or the "
                  "database fails. PE 1 (assess, identify and improve cloud architecture according "
                  "to design decisions) is evidenced across tasks 9 to 11 and lands here.",
         given=1, blank_rows=6,
         table=(["Component", "Your design", "What now happens when it fails"],
                [["Application instance", "minimum 2, one per zone",
                  "the load balancer stops sending to it; the group replaces it; service continues"],
                 ["Availability zone", "application tier spread across two",
                  "the surviving zone serves; capacity is reduced, not lost"],
                 ["Database", "your decision from task 7", ""],
                 ["NAT gateway", "one per zone", "outbound continues from the surviving zone"],
                 ["Load balancer", "unchanged — already spans two zones",
                  "the service handles this itself"],
                 ["Scalability at month-end", "existing target tracking, maximum raised",
                  "the group scales to absorb the close; unchanged in mechanism"]])),

    dict(n=12, title="Design — cost optimisation and monitoring",
         prompt="Two things that pull in opposite directions. Say how you are keeping the cost of "
                "your improvements proportionate, and design the monitoring that will let AT3 "
                "demonstrate the goals from task 6 were actually met. A goal nobody can measure is "
                "not a goal.",
         uoc=["ICTCLD504 PC 2.3", "ICTCLD504 KE 9"],
         standard="the student proposes at least one genuine cost measure that suits a "
                  "business-hours system (right-sizing, scheduled scale-down outside business "
                  "hours, or accepting a slower recovery instead of a standby) and designs "
                  "monitoring that maps onto the task 8 metrics. Monitoring that does not measure "
                  "the stated goals has not met the item.",
         given=1, blank_rows=6,
         table=(["Item", "Your design", "Why"],
                [["Cost — scaling profile",
                  "the tier scales down outside business hours; the system is idle overnight",
                  "the largest available saving, and it costs nothing in service"],
                 ["Cost — right-sizing",
                  "keep the current instance families; capacity is not the constraint",
                  "IR-6 — no cost without benefit"],
                 ["Cost — the database decision", "carried from task 7",
                  "the single biggest cost lever in this design"],
                 ["Monitoring — availability", "alarm on healthy targets per zone",
                  "the existing alarm does not distinguish zones"],
                 ["Monitoring — recovery readiness", "alarm on backup age or failure",
                  "a backup nobody checks is not a recovery plan"],
                 ["Monitoring — cost", "a budget alert on the tagged resources",
                  "IR-6 — the ongoing cost impact must stay visible"]])),

    dict(n=13, title="Cost-benefit justification",
         resources=[
             ("Accounting System Operational Costing — the current run cost, and the basis for "
              "your comparison", f"{ICT}/accounting-operational-costing-cloud"),
         ],
         prompt="IR-6 requires every improvement to be justified on cost versus benefit, with its "
                "ongoing operating-cost impact made explicit. Do that for each improvement you are "
                "proposing. Order does not matter, but nothing may be missing — an improvement "
                "without a line here is one YAT cannot approve.",
         uoc=["ICTCLD504 PC 1.4", "ICTCLD504 PC 2.3"],
         standard="every proposed improvement from task 7 appears with a cost direction and a "
                  "benefit, and the total is characterised against the cost goal from task 6. Exact "
                  "dollar figures are not required — the costing document supports estimates, and "
                  "the reasoning is what is assessed. A cost-benefit table that omits an improvement "
                  "the student proposed has not met IR-6.",
         given=1, blank_rows=7,
         table=(["Improvement", "Ongoing cost impact", "Benefit", "Justified because"],
                [["Second application instance", "increase — a second instance running",
                  "removes the zone and instance exposure",
                  "the reliability goal; the largest single reliability gain available"],
                 ["Second NAT gateway", "increase — hourly per gateway",
                  "outbound survives a zone failure",
                  "small, and pointless to spread the tier without it"],
                 ["TLS listener", "negligible", "finance data encrypted in transit",
                  "cheapest improvement on the list; indefensible to skip"],
                 ["The database decision", "carried from task 7", "", ""],
                 ["Scheduled scale-down", "decrease", "offsets part of the above",
                  "the system is genuinely idle overnight and at weekends"],
                 ["Infrastructure as code", "no run cost; effort now",
                  "reproducibility and reviewable change", "IR-5 asks for it"],
                 ["Extended monitoring", "small increase",
                  "the goals become demonstrable", "AT3 cannot demonstrate what is not measured"]])),

    dict(n=14, title="Draw the improved architecture",
         prompt="Draw the improved architecture: both availability zones, every tier, what you "
                "added, and what you kept. Mark clearly what is new. A reader who has not seen your "
                "tables should be able to see what changes and what does not.",
         uoc=["ICTCLD504 PE 1"],
         standard="the diagram shows the improved architecture consistently with tasks 9 to 12, "
                  "with both zones and the changed components identifiable. This is where the design "
                  "is demonstrated as an architecture rather than as a set of decisions.",
         diagram="the improved Ledgerline architecture — both zones, every tier, and what is new"),

    dict(n=15, title="Document and justify the proposed architecture",
         prompt="Justify the architecture you have documented in tasks 9 to 14. For each significant "
                "improvement, say which business goal from task 6 it serves and why you chose it "
                "over the alternative you considered in task 4. Say plainly what you decided not to "
                "do and why. This is a written answer, and it is where your reasoning is assessed "
                "rather than your design.",
         uoc=["ICTCLD504 PC 2.4", "ICTCLD504 FS Writing"],
         standard="the justification ties improvements to the goals set in task 6 and names "
                  "rejected alternatives with reasons. The database decision must be argued "
                  "explicitly — it is the largest cost and the largest reliability lever, and either "
                  "answer is acceptable if the reasoning is. Restating the design, or justifying "
                  "improvements on the grounds that they are best practice, has not met PC 2.4.",
         points=[
             "each improvement is tied to a specific business goal from task 6, not to convention",
             "the database decision is argued at length — cost against recovery time, for a "
             "business-hours system with outsourced payroll",
             "the improvements NOT proposed appear with their reasons; IR-2 is assessed here as "
             "much as anywhere",
             "the existing strengths are named as deliberately retained, not overlooked",
             "the ongoing cost impact is stated and set against the cost goal",
             "the design is presented as changes to a working system, not as a rebuild",
         ]),
]

# ---------------------------------------------------------------- Part B — review and approval

APPROVAL = [
    dict(n=16, title="Prepare your presentation",
         prompt="Preparation — not assessed. Nobody marks this table. Plan how you will take Sam "
                "Walker through your proposal in the time you have, and for each part write the one "
                "point Sam must take away. You are asking for approval to spend YAT's money, so "
                "lead with what it buys, not with what it is.",
         given=1, blank_rows=6,
         table=(["What you cover", "The one point Sam should take away", "Roughly how long"],
                [["What you found", "the environment works; its exposure is resilience, not "
                                    "capacity", "2 min"],
                 ["The goals you set", "these are the numbers we are aiming at, and why those",
                  "2 min"],
                 ["What you propose", "a short, justified list — not everything possible", "4 min"],
                 ["The database decision", "the one genuinely arguable call, and your reasoning",
                  "3 min"],
                 ["What it costs", "the ongoing impact, against the benefit", "2 min"],
                 ["What you are asking for", "approval to proceed to deployment", "1 min"]])),

    dict(n=17, title="Present the proposed architecture for review",
         prompt="Present your proposed architecture to Sam Walker (YAT ICT Manager, role-played by "
                "your assessor) for review. Walk through the design and the reasoning, and answer "
                "questions on both. Record the session immediately afterwards.",
         uoc=["ICTCLD504 PC 2.4", "ICTCLD504 FS Oral communication"],
         standard="the student presents their own proposal and can explain and defend the reasoning "
                  "behind it in appropriate industry language — this is observed live by the "
                  "assessor, and the table is the record, not the evidence. PC 2.4 pairs documenting "
                  "with presenting; a student who cannot explain a decision recorded in their own "
                  "worksheet has not met the presenting half.",
         given=1, blank_rows=5,
         table=(["Record", "Your entry"],
                [["Date and time", "—"],
                 ["Attendees and roles", "Sam Walker (YAT ICT Manager); the student (MTS)"],
                 ["What you presented", "per your task 16 plan, noting anything you changed"],
                 ["Questions you were asked", "the substance, and how you answered"],
                 ["Feedback given, and your response", ""]])),

    dict(n=18, title="Obtain sign-off to proceed to deployment",
         prompt="Obtain Sam Walker's sign-off to proceed to deployment, and record which "
                "improvements were approved. Approval with conditions, or approval of only some of "
                "your proposals, are real outcomes — record exactly what was agreed, because AT3 "
                "deploys what was approved and nothing else.",
         uoc=["ICTCLD504 PC 2.5"],
         standard="sign-off is obtained and recorded with a decision, a name and a date, and the "
                  "approved scope is unambiguous. PC 2.5 is 'obtain sign off to PROCEED TO "
                  "DEPLOYMENT', so the record must make clear what is approved to be built — this "
                  "is the input AT3 works from.",
         given=1, blank_rows=5,
         table=(["Sign-off record", "Your entry"],
                [["Decision", "Approved / Approved with conditions / Not approved"],
                 ["Improvements approved", "list them — this is AT3's scope"],
                 ["Improvements not approved, and why", ""],
                 ["Conditions attached", ""],
                 ["Signed by, and date", "Sam Walker, YAT ICT Manager"]])),
]

# ---------------------------------------------------------------- knowledge questions

QUESTIONS = [
    dict(n=1, title="Which industry standards and standard products does your design rely on?",
         prompt="Name the industry technology standards and the standard hardware and software "
                "products your design uses, and for each say what it contributes here.",
         uoc=["ICTCLD504 KE 1", "ICTCLD504 KE 2"],
         standard="real standards (TLS, HTTP, SQL, the availability-zone model) and real product "
                  "categories (managed relational database, load balancer, auto scaling, block "
                  "storage) are named and tied to the student's own design. A list with no "
                  "connection to their architecture has not met the contextual bar.",
         points=[
             "TLS for transport, and why it matters for a finance system on an internal network",
             "the managed relational database — what YAT gets by not running PostgreSQL themselves",
             "the load balancer and auto scaling group as the standard availability pattern",
             "block storage versus object storage, and why this system uses only the first",
             "the availability-zone model as the platform primitive the whole design rests on",
         ]),

    dict(n=2, title="Where would object storage be the right answer, and why not here?",
         prompt="Ledgerline uses no object storage. Contrast it with a system that depends on object "
                "storage for static content — the YAT public website is the obvious example — and "
                "explain how you would provision that storage and serve content from it if this "
                "system needed it.",
         uoc=["ICTCLD504 KE 6"],
         standard="the student explains object storage for static content — durable, served "
                  "independently of any instance, cheap per gigabyte, able to serve a static site "
                  "directly or through a content delivery network — and correctly identifies that "
                  "Ledgerline has no static public content and would gain nothing. Proposing object "
                  "storage for Ledgerline anyway would fail IR-2 and should be marked accordingly.",
         points=[
             "static assets served straight from the store, with no server in the path",
             "every instance sees the same content — the store is not tied to an instance",
             "durability and cost per gigabyte compared with block storage",
             "fronting it with a content delivery network for a geographically spread audience",
             "why Ledgerline gains nothing: an internal, dynamic, form-driven finance application "
             "with no static public content",
         ]),

    dict(n=3, title="What did cloud adoption change for Ledgerline, and what would migrating "
                    "further change?",
         prompt="Ledgerline moved from a server under a desk to a managed cloud environment. Explain "
                "what that change actually gave YAT, what it did not, and what principles would "
                "apply if YAT migrated more of this system — for instance to a fully managed or "
                "serverless model.",
         uoc=["ICTCLD504 KE 3", "ICTCLD504 KE 5"],
         standard="the student distinguishes what the migration delivered (managed database "
                  "operations, elastic capacity, no hardware refresh) from what it did not (the "
                  "single-zone exposure came across unchanged), and can name migration principles — "
                  "assess suitability first, migrate in stages, keep the application unchanged where "
                  "the vendor constrains it, prove recovery before decommissioning.",
         points=[
             "what was gained: managed database operations, elasticity for month-end, no hardware "
             "refresh cycle",
             "what was not: the single-zone design came across with it — a lift and shift moves the "
             "architecture too",
             "IR-4 constrains further change: the application runs unchanged",
             "migration principles — assess first, stage the work, prove recovery before you rely "
             "on it",
             "where a further move would and would not pay for an internal business-hours system",
         ]),
]

# ---------------------------------------------------------------- rendering


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


def render(doc, h1, h2, mode="student", design=None, approval=None, questions=None,
           current_arch=None, network_diagram=None, notes=False):
    """Render AT1 into `doc`. mode = student | assessor."""
    DESIGN_ = DESIGN if design is None else design
    APPROVAL_ = APPROVAL if approval is None else approval
    QUESTIONS_ = QUESTIONS if questions is None else questions

    h1("Part A — Analysis and design")
    h2("The environment you are improving")
    for para in CURRENT_ARCH_INTRO:
        R.p(doc, para, after=6)
    R.settings_table(doc, current_arch or CURRENT_ARCH)
    label, url = network_diagram or NETWORK_DIAGRAM
    par = doc.add_paragraph()
    par.paragraph_format.space_after = R.Pt(4)
    par.add_run("•  ").font.size = R.Pt(R.BODY_PT)
    R.add_hyperlink(par, label, url, size_pt=R.BODY_PT)
    R.p(doc, SCOPE_NOTE, italic=True, size=9.5, colour=R.GREY, after=6)
    R.note(doc, SIZING_NOTE)

    for el in DESIGN_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Part B — Review and approval")
    R.p(doc, "You present your proposal to YAT for review and approval to proceed. Completing the "
             "records below is not the assessment — presenting is.",
        italic=True, size=9.5, colour=R.GREY, after=10)
    for el in APPROVAL_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Knowledge questions")
    R.p(doc, "Answer these about your own design. Generic answers about cloud architecture will not "
             "pass.", italic=True, size=9.5, colour=R.GREY, after=10)
    for q in QUESTIONS_:
        R.element(doc, h2, q, mode, label="Question", notes=notes)
