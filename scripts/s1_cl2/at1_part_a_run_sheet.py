#!/usr/bin/env python3
"""The S1-CL2 AT1 Part A design workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), through the shared workbook engine in
the umbrella (`helpers/run_sheet.py`). Same form as S1-CL1 AT3 Part A: the workbook supplies
the environment and the ORDER of the tasks; every finding and every design decision is the
student's.

WHY THERE IS NO SOLUTION DESIGN TEMPLATE. ICTCLD503's assessment conditions (AC 1–9) are all
environment and input conditions — a cloud vendor, a managed database service, a serverless
environment, an IDE, a browser, data sources. None names a document format or a reporting
standard. So `[ICTCLD503 PC 1.7]` "Document and justify architecture changes" and
`[ICTCLD503 PC 2.4]` "Document and justify architecture design" are satisfied by this
worksheet: the tasks are the documenting, and tasks 14 and 19 are the justifying. Contrast
`[ICTCLD501 AC 3]` — "reporting standards for documenting and communicating disaster recovery
plan" — which is why AT1 Part B keeps a real DR Plan document.

THE MARKING MODEL. Values in this document are ours, invented so the student has a concrete
task; the unit's wording is vague by design. Each element carries the `uoc` items it evidences
and a `standard` naming what must be true for them to be met. An assessor marks the standard,
never the table. A student who puts the edge cache in front of the whole site where we put it
in front of static content only has still met `[ICTCLD503 PC 1.5]`; one who leaves the India
audience served from Sydney over the open internet has not — not because it differs from ours,
but because it does not answer the latency requirement they recorded in task 1.

THE TWO STRANDS mirror the unit's own elements: tasks 1–14 are element 1 (web-scale design,
PC 1.1–1.7), tasks 15–19 are element 2 (microservice design, PC 2.1–2.4). Each strand closes
with its own justification task, because that is where its final PC sits.

STARTING STATE. The website arrives HA-hardened — Multi-AZ, single-region, in ap-southeast-2.
That is the end state of the CL1 work and it is supplied, not designed. This assessment adds
global serving and the India-resident audit-log microservice on top of it. Cross-region
disaster recovery is Part B's DR plan, not this part.
"""

from helpers import run_sheet as R  # noqa: E402  (the shared workbook engine, in the umbrella)

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/website-global-expansion"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "YAT College has entered an offshore partnership in India, and the public website is now the "
    "enrolment front door for that campus. You are an MTS Consultant on this engagement, reporting "
    "to Pat Lin (MTS Senior Consultant). Sam Walker (YAT ICT Manager) is your primary YAT-side "
    "stakeholder; Dana Mercer (Marketing & Admissions Manager) owns the website itself.",
    "The website already runs on AWS in Sydney and has been hardened to Multi-AZ high availability. "
    "It works, and it is resilient inside its region. What it was never built for is an audience on "
    "the other side of the Indian Ocean, or the log-residency obligations that come with operating "
    "in India.",
    "The board has approved the expansion. In this part you design the extended architecture: how "
    "the website serves a global audience, and the audit-log service that keeps India's access logs "
    "in India. You are designing changes to a working system, not replacing it.",
]

RESOURCES = [
    ("Website Global Expansion — Functional & Non-Functional Requirements — the targets this design "
     "is held to", f"{PROJECT}/requirements"),
    ("Data Residency & Sovereignty Requirements — the India obligations the design must satisfy",
     f"{PROJECT}/data-residency-requirements"),
    ("Website Infrastructure Specifications — the HA-hardened environment you are extending",
     f"{ICT}/website-server-status-ha"),
    ("Website Specification — the workload itself: what the site does, who uses it, and how much",
     f"{ICT}/website-application-spec"),
    ("Engagement Role Brief — your role on this engagement and what is in scope for MTS",
     f"{PROJECT}/role-brief"),
]

INSTRUCTIONS = [
    "This is an open-book assessment. You may use the YAT intranet, AWS documentation, and anything "
    "you have from class — including your own notes and any practice work you have done. What you "
    "may not use is another student.",
    "Work the tasks in order — each one builds on the answer before it. They tell you what to "
    "decide; they do not tell you what to decide it to.",
    "Tasks 1 to 14 are the web-scale design. Tasks 15 to 19 are the audit-log microservice. Each "
    "strand finishes with a written justification of the design you produced in it — those two "
    "tasks are where your reasoning is assessed, so give them the time they need.",
    "This part is design only. You are not building anything here, and nothing is deployed. Where a "
    "task asks for a region, name the region the design calls for.",
    "Recovery from the loss of the whole Sydney region is the subject of Part B's disaster recovery "
    "plan. Design for it here only where a scaling decision also affects it, and say so.",
]

ASSESSOR_PROVIDES = ("Everything this part needs is on the YAT intranet. Your assessor will tell you "
                     "the current address of the site.")

# ---------------------------------------------------------------- the supplied current state

NETWORK_DIAGRAM = ("Network Diagram (HA-hardened) — the environment drawn out, including where the "
                   "website sits relative to the campus",
                   f"{ICT}/network-diagram-ha-hardened")

CURRENT_ARCH_INTRO = [
    "This is the environment you are extending. It is what the previous phase built and handed over "
    "— Multi-AZ, in one region, and working. Read it before you answer anything: several tasks "
    "below turn on noticing what is already there and not redesigning it.",
]

CURRENT_ARCH = [
    ("Region", "ap-southeast-2 (Sydney). This part is a design exercise — no build, so the region "
               "is the one the design calls for, not a lab substitute."),
    ("Workload", "YAT's public website — marketing pages, course catalogue, and the online enquiry / "
                 "application intake. Open-source PHP / MySQL CMS on a LAMP stack. Public and "
                 "unauthenticated: its visitors are anonymous, arriving from the open internet and "
                 "from search engines."),
    ("Network", "a website VPC across two availability zones  ·  public-web-a / -b (load balancer + "
                "NAT)  ·  private-app-a / -b (web tier)  ·  private-data-a / -b (database)"),
    ("Load balancing", "internet-facing Application Load Balancer across both public subnets, "
                       "HTTPS :443, TLS terminating at the load balancer on an ACM certificate"),
    ("Compute", "Auto Scaling group across private-app-a and -b, minimum 2 (one per zone), scaling "
                "on CPU and request count; general-purpose small instances running the LAMP stack"),
    ("Database", "Amazon RDS for MySQL, Multi-AZ — primary in private-data-a, synchronous standby in "
                 "private-data-b, automatic failover typically under two minutes, encrypted, 7-day "
                 "backup retention"),
    ("Storage", "uploaded media (images, brochures, course PDFs) served from an S3 bucket rather "
                "than instance disk, so every instance serves the same media; a second private "
                "bucket holds nightly database and media backups"),
    ("Internet", "an internet gateway, and a NAT gateway in each zone for the private subnets' "
                 "outbound traffic"),
    ("Security groups", "sg-alb  HTTPS 443 from the internet  ·  sg-app  from sg-alb only  ·  "
                        "sg-db  MySQL 3306 from sg-app only"),
    ("Availability posture", "tolerates an instance failure and a single-zone failure with no manual "
                             "intervention. Availability is already at or above 99.9%, and the "
                             "expansion must not degrade it."),
    ("What is NOT in place", "anything outside this one region. There is no edge delivery, no "
                             "presence in India, no cross-region recovery, and no audit-log service."),
]

SCOPE_NOTE = ("Your work is the AWS infrastructure. The CMS, the website content and the application "
              "stack are not yours to change — the requirements are explicit that no operating "
              "system, CMS or application version changes as part of this engagement.")

# ---------------------------------------------------------------- Part A — the design tasks
# n        — task number, referenced by later tasks that build on this answer
# title    — the heading
# prompt   — what the student is asked
# uoc      — items this task evidences
# standard — what must be true for those items to be met (assessor-only)
# table    — (columns, model_rows) for a capture table; or
# points   — key points for a written response
# diagram  — optional caption for a drawing slot

DESIGN = [
    # ------------------------------------------------ element 1: web-scale design
    dict(n=1, title="The scaling needs this design has to meet",
         resources=[
             ("Website Global Expansion — Functional & Non-Functional Requirements — the targets YAT "
              "signed off on. The figures you need are here",
              f"{PROJECT}/requirements"),
             ("Website Specification — the workload those targets are set against: who visits, how "
              "many, and when", f"{ICT}/website-application-spec"),
         ],
         prompt="Before you design anything, establish what the design is held to. Read the "
                "requirements and the website specification, and record the scaling and performance "
                "needs this expansion must meet. Name the document each one came from — a target you "
                "cannot attribute is one you have assumed.",
         uoc=["ICTCLD503 PC 1.1", "ICTCLD503 FS Reading"],
         standard="the student records the global-audience latency need, the seasonal scaling "
                  "behaviour, the availability floor and the read-heavy traffic profile, and "
                  "attributes each to a source document rather than inventing it. The figures are in "
                  "the supplied documents; a student who transcribes them correctly has met the "
                  "item. Additional rows are welcome, not required.",
         given=1, blank_rows=6,
         table=(["Need", "What the requirement says", "Where it came from"],
                [["Global audience served with acceptable latency",
                  "the India prospective-student audience must receive acceptable response times; "
                  "content delivered from the edge, close to users",
                  "Functional & Non-Functional Requirements"],
                 ["Scale up and down with demand automatically",
                  "load varies across the academic calendar with a pronounced Jan–Feb enrolment peak; "
                  "the new cohort adds to it",
                  "Functional & Non-Functional Requirements"],
                 ["Availability must not be degraded",
                  "already Multi-AZ at 99.9% or better; the expansion builds on top and must not "
                  "reduce it", "Functional & Non-Functional Requirements"],
                 ["Read-heavy traffic profile",
                  "marketing pages and course catalogue dominate; enquiry / application submissions "
                  "are comparatively light writes",
                  "Functional & Non-Functional Requirements"],
                 ["Remain discoverable by search engines",
                  "the catalogue and marketing pages are a primary acquisition channel for the new "
                  "market", "Functional & Non-Functional Requirements"],
                 ["Public attack surface must be protected",
                  "internet-facing and unauthenticated — exposed to bots, scraping, denial of "
                  "service and abuse of the public form",
                  "Functional & Non-Functional Requirements"]])),

    dict(n=2, title="Review the current architecture against those needs",
         resources=[
             ("Website Infrastructure Specifications — the HA-hardened environment as it stands "
              "today, tier by tier", f"{ICT}/website-server-status-ha"),
             ("Network Diagram (HA-hardened) — the same environment drawn out",
              f"{ICT}/network-diagram-ha-hardened"),
         ],
         prompt="Go through the current architecture layer by layer. For each, say whether it meets "
                "the needs you recorded in task 1, and if it does not, why not. Work from what is "
                "described above and in the infrastructure specifications — not from what you would "
                "expect a cloud website to look like.",
         uoc=["ICTCLD503 PC 1.2", "ICTCLD503 FS Reading"],
         standard="every layer is reviewed and each judgement is tied to a task 1 need rather than "
                  "to a general sense that something is 'not best practice'. The student must "
                  "recognise that compute, database and in-region availability already meet their "
                  "needs — a review that recommends rebuilding what is already adequate has not met "
                  "the item. The gaps that matter are edge delivery and the absence of any India "
                  "presence.",
         given=1, blank_rows=7,
         table=(["Layer", "Meets the needs?", "Why / why not"],
                [["Load balancing", "Yes",
                  "cross-AZ ALB with TLS at the edge of the VPC; scales with the tier behind it"],
                 ["Compute", "Yes",
                  "Auto Scaling group across two zones already scales on CPU and request count, and "
                  "absorbs the Jan–Feb peak"],
                 ["Database", "Partly",
                  "Multi-AZ MySQL is available and durable, but every read for every visitor still "
                  "crosses the Indian Ocean to Sydney"],
                 ["Storage", "Yes",
                  "media already served from S3 rather than instance disk, so it is not tied to a "
                  "single instance"],
                 ["Content delivery", "No",
                  "there is no edge caching — an India visitor fetches every page and image from "
                  "Sydney over the open internet"],
                 ["India presence", "No",
                  "nothing exists in an Indian region, so the log-residency obligation cannot be met "
                  "as things stand"],
                 ["Public exposure", "Partly",
                  "security groups control network reach but nothing inspects or filters malicious "
                  "web traffic at the edge"]])),

    dict(n=3, title="The residency obligation, as a design input",
         resources=[
             ("Data Residency & Sovereignty Requirements — the India obligations, and what they do "
              "and do not require", f"{PROJECT}/data-residency-requirements"),
         ],
         prompt="Read the Data Residency & Sovereignty Requirements and record what they oblige this "
                "design to do. Be precise about the boundary: note what must be held in India and "
                "what may remain in Australia. This is an input that shapes your design — you are "
                "not writing a compliance plan, and you are not interpreting the law.",
         uoc=["ICTCLD503 PC 1.5", "ICTCLD503 FS Reading"],
         standard="the student separates the log-residency obligation (DR-R1: access and activity "
                  "logs in an Indian region, 180 days) from what is NOT required (DR-R3: the main "
                  "data store may stay in Australia; full localisation is not required). A student "
                  "who concludes the whole website must move to India has misread the input and "
                  "will over-build in every task after this one.",
         given=1, blank_rows=5,
         table=(["Reference", "What the design must do", "What it does not require"],
                [["DR-R1",
                  "access and activity logs for the India cohort written to and retained in an "
                  "Indian AWS region for at least 180 days",
                  "it does not require the website itself to run in India"],
                 ["DR-R2",
                  "those logs readily retrievable, so an incident can be reported within 6 hours",
                  "no continuous reporting pipeline is asked for"],
                 ["DR-R3",
                  "nothing — content and enquiry records may remain in the Australian region",
                  "full localisation of the website is explicitly not required"],
                 ["DR-R4",
                  "keep the option open to place more data categories in India later without "
                  "re-architecting — provision the Indian footprint as reusable, "
                  "region-parameterised infrastructure",
                  "it does not require those categories to be moved now"],
                 ["DR-R5",
                  "handling of India-cohort personal data stays consistent with YAT's Privacy and "
                  "Security policies",
                  "no separate compliance deliverable is required"]])),

    dict(n=4, title="The cloud services this design needs",
         resources=[
             ("Reference Architectures — the service patterns YAT's architects work from",
              f"{SITE}/intranet/{STATE}/reference/reference-architectures"),
         ],
         prompt="Name the cloud services you will use to close the gaps you found in task 2, and say "
                "what each one does for you. One row per service. You are identifying the toolkit "
                "here; the design decisions come in the tasks after this one.",
         uoc=["ICTCLD503 PC 1.3"],
         standard="the services named actually address the gaps identified in task 2 — at minimum a "
                  "content delivery network for edge delivery and something in an Indian region for "
                  "the logs. A service list that repeats what is already deployed, or that names "
                  "services with no stated purpose, has not met the item. Specific product names are "
                  "not required; the function each service performs is.",
         given=1, blank_rows=6,
         table=(["Gap it closes", "Service", "What it does here"],
                [["Edge delivery / latency", "Content delivery network (CloudFront)",
                  "caches pages and media at edge locations near the visitor, so India traffic is "
                  "served locally instead of from Sydney"],
                 ["Global entry point", "DNS with latency or geolocation routing (Route 53)",
                  "resolves visitors to the nearest entry point and is the seam a second region "
                  "would later plug into"],
                 ["Public attack surface", "Web application firewall at the edge",
                  "filters common web exploits, bots and abusive traffic before it reaches the "
                  "origin"],
                 ["Log residency", "Managed NoSQL data store in an Indian region (DynamoDB)",
                  "holds the India-cohort access records in-region, retained 180 days"],
                 ["Log ingestion", "HTTP API + queue + serverless function",
                  "receives access events, buffers them, and writes them to the store without the "
                  "website waiting on it"],
                 ["Repeatable Indian footprint", "Infrastructure as code (CloudFormation)",
                  "lets the India-side resources be stood up by parameter, which is what keeps "
                  "DR-R4 open"]])),

    dict(n=5, title="Design — the network and entry point",
         prompt="Design how a visitor's request reaches the website once the expansion is in place. "
                "Say what sits in front of the load balancer, how a visitor in India is routed, and "
                "what changes inside the VPC. Remember the load balancer, subnets and security "
                "groups already exist — say where you leave them alone.",
         uoc=["ICTCLD503 PC 1.4"],
         standard="the design puts an edge layer in front of the existing load balancer rather than "
                  "replacing it, and the student is explicit that the VPC layout is unchanged. A "
                  "design that rebuilds the network has not met the item — PC 1.4 is about designing "
                  "architecture CHANGES, and the change here is in front of the origin, not inside "
                  "it.",
         given=1, blank_rows=5,
         table=(["Element", "Your design", "Why"],
                [["Public entry point", "CDN distribution in front of the ALB",
                  "the visitor reaches an edge location, not Sydney; the ALB becomes the origin"],
                 ["DNS", "the public domain resolves to the CDN distribution",
                  "one global name, routed to the nearest edge"],
                 ["Load balancer", "unchanged — still internet-facing, still across both zones",
                  "it already works and the CDN needs a reachable origin"],
                 ["Subnets and routing", "unchanged",
                  "nothing about global serving requires a different VPC layout"],
                 ["Origin protection",
                  "restrict the ALB so it only accepts traffic from the CDN",
                  "otherwise the edge can be bypassed and the firewall with it"]])),

    dict(n=6, title="Design — the compute tier",
         prompt="Say what happens to the web tier under the expansion. Consider the Jan–Feb peak "
                "with the new cohort added to it, and what the edge layer does to the volume of "
                "requests that actually reach an instance.",
         uoc=["ICTCLD503 PC 1.4"],
         standard="the student recognises that caching at the edge REDUCES origin load, so the "
                  "compute tier does not need to grow in proportion to the new audience, and states "
                  "what the scaling policy is measured on. A design that simply raises the instance "
                  "count without reference to the edge has not engaged with the change it just made "
                  "in task 5.",
         given=1, blank_rows=4,
         table=(["Element", "Your design", "Why"],
                [["Auto Scaling group", "retained across both zones; minimum stays 2",
                  "one instance per zone is what holds the availability floor"],
                 ["Maximum capacity", "raised to absorb the enlarged Jan–Feb peak",
                  "the new cohort adds to an already-peaky profile"],
                 ["Scaling signal", "request count per target, or CPU",
                  "the tier scales on what actually reaches it, which is now cache misses and form "
                  "submissions"],
                 ["Effect of the edge", "cached pages and media never reach an instance",
                  "a read-heavy public site offloads most of its traffic to the CDN"]])),

    dict(n=7, title="Design — the database and storage tier",
         prompt="Say what happens to the database and to media storage. Both already exist and both "
                "already work — the question is what the global audience and the read-heavy profile "
                "change about them, if anything.",
         uoc=["ICTCLD503 PC 1.4"],
         standard="the student addresses read scaling for a read-heavy workload (a read replica or "
                  "caching layer is the expected answer, and either is acceptable if justified) and "
                  "recognises that media is already in object storage and is therefore served "
                  "through the CDN without change. Keeping the writable primary in Sydney is "
                  "correct, not a gap — DR-R3 permits it.",
         given=1, blank_rows=5,
         table=(["Element", "Your design", "Why"],
                [["Primary database", "stays Multi-AZ MySQL in Sydney",
                  "residency permits it, and the write volume is light"],
                 ["Read scaling", "read replica, or an in-memory cache for hot queries",
                  "the catalogue is read constantly and changes rarely"],
                 ["Media", "unchanged in S3, delivered via the CDN",
                  "already decoupled from the instances; the edge does the rest"],
                 ["Backups", "unchanged",
                  "in scope for Part B's recovery plan, not for scaling"],
                 ["Enquiry submissions", "continue to write to the Sydney primary",
                  "light write traffic, and DR-R3 allows the records to stay in Australia"]])),

    dict(n=8, title="Design — serving a global audience",
         resources=[
             ("Website Global Expansion — Functional & Non-Functional Requirements — the global "
              "serving and search-discoverability requirements", f"{PROJECT}/requirements"),
         ],
         prompt="This is the task the whole expansion turns on. Set out how the architecture serves "
                "the India audience: what is cached, where, for how long, and what cannot be cached. "
                "Say how the site stays discoverable by search engines, and how a visitor in "
                "Australia and a visitor in India each reach content.",
         uoc=["ICTCLD503 PC 1.5", "ICTCLD503 PE 5"],
         standard="the student distinguishes cacheable content (marketing pages, catalogue, media) "
                  "from what must reach the origin (the enquiry form submission, CMS authoring), and "
                  "sets a cache policy for each rather than caching everything or nothing. Naming "
                  "edge locations near the India audience, and keeping one canonical domain for "
                  "search, are the substance of PC 1.5 here.",
         given=1, blank_rows=6,
         table=(["Content", "Cached where", "Policy", "Why"],
                [["Marketing pages", "CDN edge", "cached, medium TTL",
                  "changes rarely, read constantly, identical for every visitor"],
                 ["Course catalogue", "CDN edge", "cached, medium TTL",
                  "the primary acquisition channel and the heaviest read path"],
                 ["Media (images, brochures, PDFs)", "CDN edge", "cached, long TTL",
                  "large, static, and the biggest share of bytes transferred"],
                 ["Enquiry / application form POST", "not cached", "pass through to origin",
                  "a write; caching it would break the submission"],
                 ["CMS authoring", "not cached", "pass through to origin",
                  "authenticated and must always be live for Marketing"],
                 ["Search discoverability", "one canonical public domain on the CDN",
                  "no split hostnames per region",
                  "regionally divergent URLs fragment search ranking for the new market"]])),

    dict(n=9, title="Design — the caching decision",
         prompt="Task 8 put content at the edge. There is a second, different caching question "
                "inside the architecture: repeated database reads. Choose between a content delivery "
                "network and an in-memory data store for this problem — or say where you use each — "
                "and explain the choice against your workload. Name the option you did not choose as "
                "well as the one you did.",
         uoc=["ICTCLD503 KE 3", "ICTCLD503 PE 5", "ICTCLD503 FS Problem solving"],
         standard="the student shows they understand these solve different problems — the CDN caches "
                  "whole responses at the network edge for anonymous visitors, an in-memory store "
                  "caches query results next to the application. The strongest answer uses both, in "
                  "the right places. An answer that treats them as interchangeable has not met "
                  "KE 3's content-delivery-network / in-memory-data-store bullet.",
         given=1, blank_rows=3,
         table=(["Option", "Where you would use it", "What it does not solve"],
                [["Content delivery network",
                  "in front of the whole site, for anonymous read traffic and media",
                  "does not help a dynamic page whose query still runs on every miss"],
                 ["In-memory data store",
                  "in front of the database, for hot catalogue queries",
                  "does nothing about the distance between India and Sydney"],
                 ["Your decision", "both, at their own layer",
                  "the edge removes the distance; the in-memory cache removes repeated query cost"]])),

    dict(n=10, title="Check the design scales as utilisation increases",
         prompt="Walk your design through a load increase. Take the Jan–Feb enrolment peak with the "
                "India cohort added, and say what each layer does as demand rises — and what would "
                "run out first. A design that only works at today's volume has not met the "
                "requirement.",
         uoc=["ICTCLD503 PC 1.4", "ICTCLD503 FS Problem solving"],
         standard="each of network, compute and storage is addressed, and the student identifies at "
                  "least one genuine limit — the Auto Scaling maximum, the database's single writer, "
                  "or the read replica's capacity. Naming the constraint is the evidence; the item "
                  "asks the student to CHECK the design scales, which means finding where it stops.",
         given=1, blank_rows=4,
         table=(["Layer", "What happens as load rises", "What runs out first"],
                [["Network / edge", "the CDN absorbs it — edge capacity is elastic",
                  "nothing practical at this scale"],
                 ["Compute", "the Auto Scaling group adds instances on request count",
                  "the group's configured maximum"],
                 ["Database — reads", "served by the replica or the in-memory cache",
                  "replica capacity, if the catalogue cache is cold"],
                 ["Database — writes", "enquiry submissions go to the single primary",
                  "the single writer — vertical scaling only"]])),

    dict(n=11, title="Check availability and security are maintained",
         resources=[
             ("Privacy / Data Handling Policy — YAT's obligations for the personal information the "
              "enquiry form collects", f"{POLICY}/privacy"),
         ],
         prompt="Your changes must not cost the website the availability it already has, and they "
                "must not open it up. Go through what you have added and say, for each, what it does "
                "to availability and what it does to the attack surface.",
         uoc=["ICTCLD503 PC 1.6"],
         standard="the student recognises that adding an edge layer creates a new dependency in "
                  "front of a previously self-contained system, and addresses the public attack "
                  "surface explicitly (a web application firewall, TLS to the origin, and origin "
                  "access restriction are the expected answers). Asserting that availability is "
                  "'maintained because it is Multi-AZ' without examining the new components has not "
                  "met the item.",
         given=1, blank_rows=5,
         table=(["What you added", "Effect on availability", "Effect on security"],
                [["CDN distribution",
                  "improves it — the edge serves cached content even under origin stress; but it is "
                  "now in the request path",
                  "improves it — the origin is no longer directly addressable"],
                 ["Web application firewall", "negligible",
                  "the main gain — filters exploits, bots and form abuse at the edge"],
                 ["Origin access restriction", "no change",
                  "closes the bypass that would defeat the firewall"],
                 ["Read replica / cache", "improves read availability",
                  "one more component holding website data — same encryption and access rules apply"],
                 ["Audit-log microservice", "none — decoupled from the website by design",
                  "holds India-cohort access records; scoped write permissions only"]])),

    dict(n=12, title="Review your design and revise it",
         prompt="Go back over tasks 5 to 11 as a whole. Does the design meet every need you recorded "
                "in task 1? Where it does not, or where two decisions you made pull against each "
                "other, say what you would change. If you change nothing, say what you checked and "
                "why you are satisfied — 'no changes' is an acceptable answer only if it is an "
                "argued one.",
         uoc=["ICTCLD503 PC 1.6", "ICTCLD503 FS Self-management"],
         standard="the student revisits their own design against task 1 rather than describing it "
                  "again, and the review is specific. PC 1.6's 'review design as required' is met by "
                  "a genuine second pass — a candidate who identifies a tension (cache TTL against "
                  "content freshness for Marketing, or cost against replica capacity) and resolves "
                  "it has met the item well.",
         given=1, blank_rows=4,
         table=(["Need from task 1", "Met?", "Change you would make"],
                [["Global audience served with acceptable latency", "Yes",
                  "none — the edge layer answers it directly"],
                 ["Scale up and down with demand", "Yes",
                  "none, provided the Auto Scaling maximum is raised as designed"],
                 ["Availability not degraded", "Yes",
                  "none, but the CDN is a new dependency and belongs in Part B's recovery plan"],
                 ["Remain discoverable by search engines", "Partly",
                  "cache TTLs need to be short enough that catalogue updates publish within the "
                  "intake cycle Marketing works to"]])),

    dict(n=13, title="Draw the web-scale architecture",
         prompt="Draw the extended architecture as a diagram: the path a visitor's request takes "
                "from India and from Australia, everything you added, and everything you kept. Label "
                "the regions. A reader who has not seen your tables should be able to follow how the "
                "website now serves a global audience.",
         uoc=["ICTCLD503 PE 1"],
         standard="the diagram shows a multi-tier web application whose networking, compute and "
                  "storage all scale — the edge layer, the load balancer, the auto-scaling tier, and "
                  "the database with its read path — and it is consistent with the tables in tasks 5 "
                  "to 8. This is where PE 1 is demonstrated: the tables carry the reasoning, the "
                  "diagram is the architecture.",
         diagram="the extended website architecture — edge, region, tiers, and the request path from "
                 "both audiences"),

    dict(n=14, title="Justify the web-scale design",
         prompt="Justify the architecture you have documented in tasks 5 to 13. For each significant "
                "choice, say which of the scaling needs from task 1 it answers, and why you chose it "
                "over the alternative you considered. This is a written answer, not a table — and it "
                "is where your design reasoning is assessed, not your design.",
         uoc=["ICTCLD503 PC 1.7", "ICTCLD503 FS Writing"],
         standard="the justification ties specific design choices to specific needs recorded in "
                  "task 1, and names alternatives that were considered and rejected. A restatement "
                  "of the design, or generic praise for the services chosen ('CloudFront is fast and "
                  "scalable'), has not met PC 1.7 — the item asks the student to JUSTIFY, which "
                  "means giving reasons an assessor could disagree with.",
         points=[
             "the edge layer is justified by the latency need, not by convention — India traffic is "
             "the reason it exists",
             "keeping the existing VPC, load balancer and Multi-AZ database is itself a justified "
             "choice: the requirements say build on the HA platform, not replace it",
             "the read-scaling choice is argued against the read-heavy profile from task 1",
             "cache policy is justified per content type, including what is deliberately not cached",
             "at least one rejected alternative appears with the reason it was rejected — a "
             "second full region, full localisation in India, or caching everything at one TTL",
             "cost-effectiveness is addressed: the requirements ask for the simplest arrangement "
             "that meets them",
         ]),

    # ------------------------------------------------ element 2: microservice design
    dict(n=15, title="The microservice and the data it handles",
         resources=[
             ("Website Global Expansion — Functional & Non-Functional Requirements — the audit / "
              "access log requirement and why it is a separate service",
              f"{PROJECT}/requirements"),
             ("Data Residency & Sovereignty Requirements — what has to be captured and held in "
              "India", f"{PROJECT}/data-residency-requirements"),
         ],
         prompt="The residency obligation you recorded in task 3 is met by a dedicated service, not "
                "by changing the website. Identify what that service does: the events it receives, "
                "the data each event carries, and where the data comes to rest. One row per data "
                "transaction.",
         uoc=["ICTCLD503 PC 2.1"],
         standard="the student identifies the access/activity event as the transaction, names the "
                  "fields an access log needs to be useful to CERT-In (who, what, when, from where), "
                  "and places the store in an Indian region. A design that logs into the existing "
                  "MySQL database in Sydney has not met the requirement it exists to satisfy.",
         given=1, blank_rows=4,
         table=(["Transaction", "What it carries", "Where it comes to rest"],
                [["Access / activity event from the website",
                  "an event identifier, timestamp, an opaque user reference, the cohort, the event "
                  "type, and the source address",
                  "the India-region log store"],
                 ["Enquiry / application submission event",
                  "the same access-event shape — that a submission occurred, not its contents",
                  "the India-region log store; the submission itself stays in Sydney"],
                 ["Retrieval for incident reporting",
                  "a query over the retained records for a time window",
                  "read from the India-region store, within the 6-hour obligation"]])),

    dict(n=16, title="The cloud services that support it",
         prompt="Name the services your microservice is built from, and say what each contributes. "
                "The service has to receive events from the website, hold them safely if it is busy "
                "or briefly unavailable, process them, and store them — say which service does each "
                "of those, and why that kind of service suits the job.",
         uoc=["ICTCLD503 PC 2.2", "ICTCLD503 KE 4"],
         standard="the student names an API or endpoint to receive events, a queue or messaging "
                  "service to decouple, a compute element to process, and a persistent store — and "
                  "explains the queue's purpose specifically. KE 4's 'API, messaging and queuing "
                  "services' and 'database and storage services for persistent data storage' are "
                  "both evidenced here; a design with no queue has not evidenced the messaging "
                  "bullet and has also lost the decoupling the requirement asks for.",
         given=1, blank_rows=5,
         table=(["Role", "Service", "Why this kind of service"],
                [["Receive events", "HTTP API endpoint",
                  "a single, simple integration point the website can call"],
                 ["Decouple and buffer", "Queue",
                  "the website hands the event over and moves on; if the writer is slow or down, "
                  "events wait in the queue instead of being lost"],
                 ["Process", "Serverless function",
                  "runs only when there are events, which suits bursty, low-volume traffic and costs "
                  "nothing at idle"],
                 ["Store", "Managed NoSQL table in an Indian region",
                  "append-only records with a simple key, retained 180 days, in-region by "
                  "construction"],
                 ["Provision", "Infrastructure as code, parameterised by region",
                  "keeps DR-R4 open — another region is a parameter, not a rebuild"]])),

    dict(n=17, title="Draw the microservice architecture",
         prompt="Draw the microservice: the website as the event producer, each component of your "
                "service, the direction events travel, and the region boundary between Australia and "
                "India. Show where the website's responsibility ends and the service's begins.",
         uoc=["ICTCLD503 PC 2.3", "ICTCLD503 PE 2"],
         standard="the diagram shows a decoupled flow — producer, endpoint, queue, processor, store "
                  "— with the region boundary marked, and it agrees with task 16. PE 2 is "
                  "demonstrated here: a microservice architecture for a simple web application. A "
                  "diagram showing the website writing directly to the store has designed the "
                  "coupling out of existence and has not met the item.",
         diagram="the audit-log microservice — producer, endpoint, queue, processor, store, and the "
                 "Australia / India region boundary"),

    dict(n=18, title="The interface contract",
         prompt="Define the contract between the website and your service — the one place they touch. "
                "Say what the website sends, what it gets back, and what happens if the same event "
                "arrives twice. Someone building either side from your contract alone should not have "
                "to ask you a question.",
         uoc=["ICTCLD503 PC 2.3", "ICTCLD503 KE 4"],
         standard="the contract specifies the request (method, payload fields, types), the responses "
                  "including a failure response, and how duplicates are handled. Cohesion and loose "
                  "coupling — KE 4's first bullet — are evidenced by the contract being the ONLY "
                  "coupling: the website knows the endpoint and nothing about the queue, the "
                  "function or the store.",
         given=1, blank_rows=6,
         table=(["Element of the contract", "Your definition", "Why"],
                [["Direction", "website → service, one way",
                  "the website does not read its own audit log"],
                 ["Call", "HTTP POST to a single endpoint, JSON body",
                  "the simplest integration a CMS can make"],
                 ["Payload", "event id, timestamp, opaque user reference, cohort, event type, "
                             "source address",
                  "enough for CERT-In retrieval without carrying personal content"],
                 ["Success response", "accepted, queued for writing",
                  "the website is told it was received, not that it was stored — that is the "
                  "decoupling"],
                 ["Failure response", "malformed request rejected with a clear error",
                  "the producer can log and move on"],
                 ["Duplicates", "the event id is the idempotency key; a repeat is ignored",
                  "a re-delivered message must not create a second audit record"]])),

    dict(n=19, title="Justify the microservice design",
         prompt="Justify the microservice you have documented in tasks 15 to 18. Say why a separate "
                "service rather than a change to the website, why each component is there, and what "
                "your design would cost you if the service were unavailable for an hour. As with "
                "task 14, this is a written answer and it is where your reasoning is assessed.",
         uoc=["ICTCLD503 PC 2.4", "ICTCLD503 FS Writing"],
         standard="the justification argues the separation (availability of the website must not "
                  "depend on the logger — the requirement says so explicitly), argues the queue "
                  "specifically, and answers the unavailability question honestly. A student who "
                  "says the service is 'best practice' or 'more scalable' without tying it to the "
                  "requirement or to the residency obligation has not met PC 2.4.",
         points=[
             "separation is justified by the requirement that the log service not affect website "
             "availability — not by a general preference for microservices",
             "the India region is justified by DR-R1, and the choice NOT to move the rest is "
             "justified by DR-R3",
             "the queue is justified by what it protects against: a slow or failed writer losing "
             "events the obligation requires be retained",
             "the store choice is argued for an append-only, key-accessed, high-write-rate record "
             "set — which is what KE 3's SQL-versus-NoSQL bullet is really asking",
             "an honest answer to the outage question: events queue and are written when the service "
             "recovers; events lost entirely only if the queue's retention is exceeded",
             "parameterising by region is justified by DR-R4, not by tidiness",
         ]),
]

# ---------------------------------------------------------------- knowledge questions

QUESTIONS = [
    dict(n=1, title="Your design makes four component choices. Explain each one.",
         prompt="For each pair below, say which you used in your design, where, and why it suited "
                "that job better than the alternative. Answer about YOUR design — a general "
                "comparison of the two technologies will not pass.",
         uoc=["ICTCLD503 KE 3"],
         standard="all four pairs are addressed against the student's own design: SQL for the "
                  "website's relational content and NoSQL for the append-only log store; the "
                  "monolithic CMS retained while the new function is a microservice; the compute "
                  "models (instances for the CMS, serverless for the logger); and the two caching "
                  "technologies from task 9. This question is the whole of KE 3 and each bullet must "
                  "be evidenced.",
         points=[
             "SQL vs NoSQL — relational CMS content stays on MySQL; the audit log is key-accessed, "
             "append-only and high-write, which suits NoSQL",
             "monolithic vs microservice — the CMS stays monolithic because the engagement forbids "
             "changing it; the new capability is a microservice because it must not affect website "
             "availability",
             "virtual, container and serverless compute — instances run the LAMP stack; the logger "
             "is serverless because it is event-driven and idle most of the time",
             "CDN vs in-memory data store — the edge removes distance, the in-memory cache removes "
             "repeated query cost; they solve different problems",
         ]),

    dict(n=2, title="What makes your microservice highly cohesive and loosely coupled?",
         prompt="Point at the specific parts of your own design that make it so, and say what would "
                "have to change for that to stop being true.",
         uoc=["ICTCLD503 KE 4"],
         standard="the student explains cohesion as the service doing one job (recording access "
                  "events) and coupling as the single contract from task 18, and can name what would "
                  "break it — the website reading the store directly, or the service taking on a "
                  "second responsibility. Definitions with no reference to their own design have not "
                  "met the contextual-knowledge bar.",
         points=[
             "cohesion: the service records access events and does nothing else",
             "coupling: the website knows one endpoint and one payload shape — not the queue, the "
             "function, or the store",
             "the store can be changed without the website knowing",
             "it would stop being true if the website read the log store directly, or if the service "
             "took on a second job",
         ]),

    dict(n=3, title="Which web-scaling principles does your design apply?",
         prompt="Name the web-scaling principles and technologies your design uses, and for each one "
                "point to where it appears in your architecture and what it does for the global, "
                "anonymous, read-heavy audience this website serves.",
         uoc=["ICTCLD503 KE 6", "ICTCLD503 PE 5"],
         standard="the student names principles rather than only products — caching close to the "
                  "user, horizontal scaling, statelessness, decoupling, offloading static content — "
                  "and locates each in their own design. Listing AWS services with no principle "
                  "behind them has not met KE 6.",
         points=[
             "cache close to the user — the edge layer, justified by the India audience",
             "scale horizontally, not vertically — the Auto Scaling group; and where that is not "
             "possible, the single database writer",
             "keep the tier stateless — media in object storage rather than instance disk, which is "
             "what lets any instance serve any request",
             "decouple work that does not have to be synchronous — the queue in the microservice",
             "offload static content from the application — media served from the edge, never "
             "touching an instance",
         ]),

    dict(n=4, title="How does your design keep the residency option open?",
         prompt="DR-R4 asks that additional data categories could be located in India later without "
                "re-architecting. Explain how your design keeps that open, and what it would take to "
                "act on it.",
         uoc=["ICTCLD503 KE 4", "ICTCLD503 FS Self-management"],
         standard="the student connects the parameterised, infrastructure-as-code Indian footprint "
                  "to the future obligation, and gives a concrete answer about what changing it "
                  "would involve. This is the design-for-change question; an answer that only "
                  "restates DR-R4 has not engaged with it.",
         points=[
             "the Indian footprint is defined as code and parameterised by region, so a second "
             "category is a deployment, not a redesign",
             "the microservice pattern generalises — another event type is another producer calling "
             "the same contract",
             "what it would take: a new store and writer for the category, and a decision about "
             "whether the Sydney copy is retained or moved",
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


def render(doc, h1, h2, mode="student", design=None, questions=None,
           current_arch=None, network_diagram=None, notes=False):
    """Render Part A into `doc`. mode = student | assessor.

    The content lists default to AT1 Part A's own. A practice sheet passes its own — same
    renderer, same shapes, a different system — so the two cannot drift structurally even
    though every value in them differs.
    """
    DESIGN_ = DESIGN if design is None else design
    QUESTIONS_ = QUESTIONS if questions is None else questions

    h1("Part A — Design")
    h2("The environment you are extending")
    for para in CURRENT_ARCH_INTRO:
        R.p(doc, para, after=6)
    R.settings_table(doc, current_arch or CURRENT_ARCH)
    label, url = network_diagram or NETWORK_DIAGRAM
    par = doc.add_paragraph()
    par.paragraph_format.space_after = R.Pt(4)
    par.add_run("•  ").font.size = R.Pt(R.BODY_PT)
    R.add_hyperlink(par, label, url, size_pt=R.BODY_PT)
    R.p(doc, SCOPE_NOTE, italic=True, size=9.5, colour=R.GREY, after=10)

    for el in DESIGN_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Knowledge questions")
    R.p(doc, "Answer these about your own design. Generic answers about cloud architecture will not "
             "pass.", italic=True, size=9.5, colour=R.GREY, after=10)
    for q in QUESTIONS_:
        R.element(doc, h2, q, mode, label="Question", notes=notes)
