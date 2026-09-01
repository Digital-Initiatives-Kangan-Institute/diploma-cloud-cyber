#!/usr/bin/env python3
"""The S1-CL2 AT1 Part B disaster-recovery workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), through the shared workbook engine in
the umbrella (`helpers/run_sheet.py`). Same form as Part A.

WHY THIS PART KEEPS A TEMPLATE, WHEN PART A DOES NOT. `[ICTCLD501 AC 3]` is explicit —
"reporting standards for documenting and communicating disaster recovery plan" — and
`[ICTCLD501 PE 3]` requires the student to "document disaster recovery plan". A DR plan is an
artefact YAT keeps and uses; it is lodged as a record and read by someone in an incident. So
the plan survives as a real document. What the worksheet takes over is the THINKING: the
student works every analysis and decision here, task by task, and the closing task copies the
answers into the YAT Disaster Recovery Plan template. Both are submitted.

THE TASK ORDER IS THE TEMPLATE'S SECTION ORDER. That is deliberate and it is what makes the
copy-out mechanical rather than a translation job at the end. Task N maps to one template
section; the closing task carries the map. If the template's sections are ever re-ordered,
re-order these tasks with them.

WHAT THIS PART IS RECOVERING. The system designed in Part A — the globally-served website with
its India audit-log service. A DR plan is written for a designed system, which is why Part A
comes first. Several tasks copy forward from Part A the way AT3's Part B copies forward from
its Part A.

THE MARKING MODEL. Values here are ours, invented so the student has a concrete task. Each
element carries the `uoc` items it evidences and a `standard` naming what must be true for them
to be met. An assessor marks the standard, never the table. A student whose recovery strategy
is warm standby where we modelled pilot light has still met `[ICTCLD501 PC 3.1]` if the choice
is argued against their own RTO; one who names a strategy that cannot reach the RTO they set
has not.
"""

from helpers import run_sheet as R  # noqa: E402  (the shared workbook engine, in the umbrella)

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/website-global-expansion"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"
REFERENCE = f"{SITE}/intranet/{STATE}/reference"

# ---------------------------------------------------------------- front matter

INTRO = [
    "Part A designed the extended website. This part plans its recovery: what could take it "
    "down, what that would cost YAT, how you would get it back, and how long that would take.",
    "You are writing for two readers. One is Sam Walker, who approves the plan. The other is "
    "whoever is on call at 3am when the Sydney region is unavailable and this is the document "
    "they open. Write for the second one.",
    "Work the tasks in order. They follow the sections of the YAT Disaster Recovery Plan "
    "template, so when you reach the last task the plan assembles from what you have already "
    "written. Nothing you do here is wasted effort or gets written twice.",
]

RESOURCES = [
    ("Website Global Expansion — Functional & Non-Functional Requirements — the recovery "
     "objectives YAT signed off on", f"{PROJECT}/requirements"),
    ("Website Infrastructure Specifications — the environment, and the backup arrangements "
     "currently in place", f"{ICT}/website-server-status-ha"),
    ("Deprecated on-premises DR Plan — superseded by the move to the cloud. Context for what an "
     "organisational plan looks like, not a model to copy", f"{ICT}/lms-dr-plan-onprem-deprecated"),
    ("Backup & Retention Policy — YAT's standing backup and retention obligations",
     f"{POLICY}/backup-retention"),
    ("Industry Standards — the information-security and continuity standards YAT works to",
     f"{REFERENCE}/industry-standards"),
    ("Records Management Policy — where a completed engagement document has to be lodged",
     f"{POLICY}/records-management"),
]

TEMPLATE_NOTE = ("You will need the YAT Disaster Recovery Plan template — download it from the "
                 "intranet's Templates section. You do not need it until the last task, but read "
                 "its section headings before you start so you can see where your answers land.")

# ---------------------------------------------------------------- the plan tasks
# Task order follows the DR Plan template's section order. The map is in the closing task.

PLAN = [
    dict(n=20, title="The recovery requirements this plan has to meet",
         resources=[
             ("Website Global Expansion — Functional & Non-Functional Requirements — the recovery "
              "objectives and the availability floor", f"{PROJECT}/requirements"),
             ("Engagement Role Brief — what MTS is engaged to deliver and what is out of scope",
              f"{PROJECT}/role-brief"),
         ],
         prompt="Establish what the plan is held to before you write any of it. Record the recovery "
                "requirements YAT has set, what business need each one comes from, and where you "
                "read it. A requirement you cannot attribute is one you have assumed.",
         uoc=["ICTCLD501 PC 1.1", "ICTCLD501 FS Reading"],
         standard="the student records the RTO and RPO targets, the availability floor, and the "
                  "business reason the website now warrants them (it is the enrolment front door for "
                  "the India campus), each attributed to a source document. PC 1.1 is about "
                  "identifying requirements according to BUSINESS needs — a list of technical "
                  "targets with no business driver beside them has not met it.",
         given=1, blank_rows=5,
         table=(["Requirement", "What it is", "The business need behind it"],
                [["Recovery time objective", "≤ 4 hours to operational service",
                  "a prospective student who cannot reach the site during intake goes elsewhere"],
                 ["Recovery point objective", "≤ 1 hour of data loss",
                  "enquiry and application submissions are the acquisition pipeline"],
                 ["Availability floor", "≥ 99.9%, not to be degraded",
                  "already achieved Multi-AZ; the expansion must not cost YAT what it has"],
                 ["Recovery independent of the primary region",
                  "recovery must not depend on Sydney being available",
                  "a regional event is exactly the case the plan exists for"],
                 ["Scope", "cloud infrastructure only — CMS and content unchanged",
                  "YAT Marketing owns the content; MTS is engaged for the infrastructure"]])),

    dict(n=21, title="Existing recovery arrangements",
         resources=[
             ("Website Infrastructure Specifications — the backup arrangements in place today",
              f"{ICT}/website-server-status-ha"),
             ("Backup & Retention Policy — YAT's standing obligations",
              f"{POLICY}/backup-retention"),
             ("Deprecated on-premises DR Plan — the plan the cloud migration superseded. Context "
              "only — do not copy it", f"{ICT}/lms-dr-plan-onprem-deprecated"),
         ],
         prompt="Determine what recovery arrangements already exist. Go through what is actually in "
                "place today and say what each one would and would not get you back. Be honest about "
                "the difference between a backup and a recovery plan.",
         uoc=["ICTCLD501 PC 1.2", "ICTCLD501 FS Reading"],
         standard="the student identifies the automated database backups, the nightly snapshots to "
                  "object storage, and Multi-AZ failover — and recognises that none of these survive "
                  "the loss of the region, because they all live in it. Recognising that the "
                  "deprecated on-prem plan is superseded and does not cover the cloud environment is "
                  "the other half of PC 1.2.",
         given=1, blank_rows=5,
         table=(["Existing arrangement", "What it protects against", "What it does not cover"],
                [["Multi-AZ database with automatic failover",
                  "loss of one availability zone, an instance, or the primary database",
                  "loss of the whole region — the standby is in it"],
                 ["Automated database backups, 7-day retention",
                  "data corruption or accidental deletion",
                  "the backups are held in the same region as the database"],
                 ["Nightly database and media snapshots to object storage",
                  "rebuilding content after a data loss",
                  "same region again; and nothing automates the rebuild"],
                 ["Auto Scaling across two zones",
                  "instance failure, replaced without intervention",
                  "nothing outside the region"],
                 ["Deprecated on-premises DR plan",
                  "nothing current — it was written for the on-premises estate",
                  "superseded by the cloud migration; no cloud environment is in scope of it"]])),

    dict(n=22, title="Vendor provisions and service level agreements",
         resources=[
             ("Master Services Agreement — the engagement's contractual frame",
              f"{PROJECT}/master-services-agreement"),
             ("Industry Standards — the provider commitments YAT works to",
              f"{REFERENCE}/industry-standards"),
         ],
         prompt="Identify what your cloud provider commits to, and what it does not. Record the "
                "service commitments that matter to this plan, and be clear about where the "
                "provider's responsibility ends and YAT's begins — that boundary is where your plan "
                "has to do the work.",
         uoc=["ICTCLD501 PC 1.3"],
         standard="the student identifies the shared-responsibility boundary: the provider commits "
                  "to service availability and to the durability of stored objects, but recovery of "
                  "YAT's workload into another region is YAT's job. A student who treats the "
                  "provider's availability figure as YAT's recovery plan has not met PC 1.3.",
         given=1, blank_rows=5,
         table=(["Provision", "What the provider commits to", "What remains YAT's responsibility"],
                [["Compute service level", "service availability within a region",
                  "the application running on it, and its recovery elsewhere"],
                 ["Managed database", "automated backup, patching, Multi-AZ failover",
                  "choosing the retention, and copying backups out of the region"],
                 ["Object storage durability", "very high durability of stored objects",
                  "replicating the bucket to another region if that is what recovery needs"],
                 ["Regional isolation", "regions fail independently",
                  "having anything at all in a second region beforehand"],
                 ["Incident communication", "status reporting during a service event",
                  "detecting the impact on YAT and deciding to invoke the plan"]])),

    dict(n=23, title="Recovery objectives",
         prompt="State the recovery objectives this plan commits to, per component of the system you "
                "designed in Part A. Take the targets from task 20 as the requirement, then say what "
                "each component's objective is and why. Not everything needs the same objective — "
                "say where you differentiate, and why that is defensible.",
         uoc=["ICTCLD501 PC 2.1", "ICTCLD501 KE 5"],
         standard="the student states an RTO and RPO per component rather than one figure for the "
                  "whole system, and the figures are within the targets from task 20. Differentiating "
                  "(the marketing pages can come back before the enquiry history) is the mark of a "
                  "strong answer; KE 5 is evidenced by the student using the terms correctly — RPO "
                  "is data loss, RTO is time to service.",
         given=1, blank_rows=6,
         table=(["Component", "RTO", "RPO", "Why this objective"],
                [["Public website (pages, catalogue)", "≤ 4 hours", "≤ 1 hour",
                  "the front door; the whole target exists for this"],
                 ["Enquiry / application submissions", "≤ 4 hours", "≤ 1 hour",
                  "the acquisition pipeline — lost submissions are lost students"],
                 ["Media (images, brochures, PDFs)", "≤ 4 hours", "≤ 24 hours",
                  "changes rarely; a day-old copy is materially the same site"],
                 ["CMS authoring", "≤ 24 hours", "≤ 1 hour",
                  "internal, and Marketing can wait a day to publish"],
                 ["India audit-log store", "≤ 4 hours", "≤ 1 hour",
                  "the residency obligation does not pause during a Sydney outage"]])),

    dict(n=24, title="The data you are protecting",
         resources=[
             ("Website Specification — the data the website holds, its volume and its sensitivity",
              f"{ICT}/website-application-spec"),
             ("Privacy / Data Handling Policy — the classification and handling obligations",
              f"{POLICY}/privacy"),
         ],
         prompt="Estimate what data this system holds, how much of it there is, and how sensitive "
                "each kind is. Volume drives how long a recovery takes; sensitivity drives how "
                "carefully it has to be handled while you are recovering it.",
         uoc=["ICTCLD501 PC 2.3"],
         standard="the student estimates volumes and assigns a sensitivity or classification to "
                  "each data category, and identifies the enquiry / application submissions as the "
                  "personal information that carries the heaviest obligation. PC 2.3 asks for the "
                  "amount AND the security level — an answer with volumes but no classification has "
                  "met half the item.",
         given=1, blank_rows=6,
         table=(["Data", "Approximate volume", "Sensitivity", "What that means for recovery"],
                [["Page content and course catalogue", "~0.3 GB", "Public once published",
                  "small, and no handling constraint — recover it first"],
                 ["Uploaded media", "~5 GB, growing ~1 GB/year",
                  "Public", "the bulk of the volume; drives transfer time"],
                 ["Enquiry / application submissions", "~0.5 GB",
                  "Personal information — Privacy Act and APPs",
                  "must stay encrypted and in an approved region throughout recovery"],
                 ["India audit / access logs", "grows with India traffic",
                  "Regulated — CERT-In, 180-day retention",
                  "must be recovered into an Indian region, not into the DR region"],
                 ["Web and access logs", "~1 GB rolling", "Operational",
                  "useful for diagnosis; not required to restore service"]])),

    dict(n=25, title="Risk assessment — the major risk events",
         resources=[
             ("Security & Incident Response Policy — how YAT classifies and responds to incidents",
              f"{POLICY}/security-incident"),
         ],
         prompt="Identify the major risk events this plan is written for. You need at least three. "
                "For each, say how likely it is, what the impact on YAT would be, and how you rated "
                "it — name the method you used, because a rating with no method behind it is an "
                "opinion.",
         uoc=["ICTCLD501 PC 2.4", "ICTCLD501 PE 2", "ICTCLD501 KE 1", "ICTCLD501 KE 2",
              "ICTCLD501 FS Planning and organising"],
         standard="at least three major risk events, each with a likelihood, an impact stated in "
                  "terms of YAT's business rather than in generic risk language, and a stated rating "
                  "method (a likelihood × consequence matrix is the expected answer and satisfies "
                  "KE 2). PE 1 depends on this task producing three — fewer than three fails the "
                  "performance evidence for the whole AT, so it is worth checking here.",
         given=1, blank_rows=6,
         table=(["Risk event", "Likelihood", "Impact on YAT", "Rating"],
                [["Loss of the Sydney region", "Rare",
                  "the enrolment front door is down; every prospective student sees nothing; "
                  "submissions stop", "High"],
                 ["Data corruption or destructive change to the database", "Unlikely",
                  "catalogue and submission history damaged; recovery from backup with data loss "
                  "up to the retention point", "High"],
                 ["Sustained denial-of-service or hostile traffic against the public site",
                  "Possible",
                  "site slow or unreachable during the period it matters most; a public, "
                  "unauthenticated site is exposed by design", "Medium"],
                 ["Loss of the India log store or its region", "Rare",
                  "the residency obligation is breached and CERT-In reporting cannot be met",
                  "Medium"],
                 ["Accidental deletion of infrastructure by a change", "Possible",
                  "partial or total outage; recoverable but only as fast as it can be rebuilt",
                  "Medium"]])),

    dict(n=26, title="Plan exclusions",
         prompt="Say what this plan does not cover, and why each exclusion is defensible against the "
                "business requirements. An exclusion is a decision you are accountable for — it is "
                "not the same as something you forgot.",
         uoc=["ICTCLD501 PC 2.2"],
         standard="the student names exclusions and justifies each against a business requirement — "
                  "typically the CMS application and content (out of engagement scope), the campus "
                  "network (not connected to the website), and anything the requirements place "
                  "outside cloud infrastructure. An empty or unjustified exclusions list has not met "
                  "PC 2.2, which asks the student to ASSESS exclusions.",
         given=1, blank_rows=5,
         table=(["Excluded from this plan", "Why", "Who does own it"],
                [["The CMS application and website content",
                  "the engagement is cloud infrastructure only; no application change is permitted",
                  "YAT Marketing & Admissions, with YAT ICT"],
                 ["The campus network", "the website is public-facing and not connected to it",
                  "YAT ICT"],
                 ["Recovery of individual user devices", "not part of the website service",
                  "YAT ICT service desk"],
                 ["Legal interpretation of the India obligations",
                  "owned by the YAT compliance area; MTS designs to the determination",
                  "YAT Compliance"],
                 ["Recovery of the LMS and Ledgerline",
                  "separate systems with their own arrangements", "YAT ICT"]])),

    dict(n=27, title="Record the outcomes of the impact analysis",
         resources=[
             ("Records Management Policy — how analysis outcomes are recorded and retained",
              f"{POLICY}/records-management"),
             ("Change Management Procedure — the governance a production-affecting plan sits under",
              f"{POLICY}/change-management"),
         ],
         prompt="Your analysis in tasks 4 to 7 has to be recorded in a way YAT can act on and audit "
                "later. Say what gets recorded, where it is held, who owns it, and when it is "
                "reviewed — according to YAT's policies, not your preference.",
         uoc=["ICTCLD501 PC 2.5"],
         standard="the student ties the recording of the analysis to YAT's actual policies — the "
                  "Records Management Policy for lodgement and retention, and a review trigger. "
                  "PC 2.5 says 'according to organisational policies and procedures', so an answer "
                  "that describes good practice without reference to YAT's policies has not met it.",
         given=1, blank_rows=4,
         table=(["What is recorded", "Where it is held", "Owner", "Reviewed when"],
                [["Risk register and ratings", "with the lodged DR plan", "Sam Walker, ICT Manager",
                  "annually, and after any incident"],
                 ["Recovery objectives per component", "in the DR plan itself",
                  "Sam Walker, ICT Manager", "annually, or on material change to the website"],
                 ["Plan exclusions and their justification", "in the DR plan itself",
                  "Sam Walker, ICT Manager", "annually"],
                 ["Data volumes and classifications", "with the lodged DR plan",
                  "YAT ICT", "annually, or when the data profile changes"]])),

    dict(n=28, title="Recovery options evaluated",
         resources=[
             ("Reference Architectures — the recovery patterns YAT's architects work from",
              f"{REFERENCE}/reference-architectures"),
         ],
         prompt="Develop a range of recovery solutions — not one. For each, say what it would cost "
                "YAT to run, what recovery time it would actually achieve, and what it would not do. "
                "You are building the comparison your recommendation in the next task rests on.",
         uoc=["ICTCLD501 PC 3.1", "ICTCLD501 KE 3", "ICTCLD501 FS Problem solving"],
         standard="at least three genuine cloud recovery techniques are evaluated — backup and "
                  "restore, pilot light, warm standby and multi-site active/active are the "
                  "recognised set, and naming them satisfies KE 3. Each must carry a realistic "
                  "recovery time and a cost posture. PC 3.1 says 'develop RANGE of solutions': a "
                  "single proposal with no alternatives has not met it.",
         given=1, blank_rows=5,
         table=(["Option", "How it works", "Realistic RTO", "Cost posture"],
                [["Backup and restore",
                  "backups copied to a second region; everything rebuilt on demand",
                  "many hours to a day — misses the 4-hour target", "lowest"],
                 ["Pilot light",
                  "database replicated to the second region, core infrastructure defined as code and "
                  "deployed on invocation", "2 to 4 hours — meets the target",
                  "low: storage and replication only"],
                 ["Warm standby",
                  "a scaled-down but running copy in the second region, scaled up on failover",
                  "under an hour", "moderate: always-on capacity"],
                 ["Multi-site active/active",
                  "both regions serving traffic all the time", "near zero",
                  "highest — roughly double"]])),

    dict(n=29, title="The recommended approach",
         prompt="Recommend one of the options from task 28 and align it to the business requirement. "
                "Say why it is the right level of protection for this system — not the most "
                "protection available. Name the option you would choose if the requirements changed, "
                "and what change would make you switch.",
         uoc=["ICTCLD501 PC 3.1", "ICTCLD501 PC 4.1", "ICTCLD501 FS Problem solving"],
         standard="the recommendation meets the RTO and RPO from task 23 and is justified as "
                  "proportionate — PC 4.1 is about ALIGNING the recovery to business requirements, "
                  "which cuts both ways: under-protecting misses the target, over-protecting spends "
                  "YAT's money on protection it did not ask for. A student who recommends "
                  "active/active for a 4-hour RTO has not aligned anything.",
         given=1, blank_rows=4,
         table=(["Decision", "Your answer", "Why"],
                [["Recommended strategy", "pilot light in a second region",
                  "meets a 4-hour RTO and a 1-hour RPO without paying for idle capacity"],
                 ["Why not the cheaper option",
                  "backup and restore cannot make 4 hours", "it fails the requirement"],
                 ["Why not the stronger option",
                  "warm standby and active/active both exceed the requirement",
                  "the requirements ask for the simplest arrangement that meets them"],
                 ["What would change the recommendation",
                  "an RTO under an hour, or the website becoming transactional",
                  "then warm standby becomes the proportionate answer"]])),

    dict(n=30, title="Vendor protections and risk prioritisation",
         prompt="Come back to the provider protections you identified in task 22, now that you have a "
                "strategy. For each risk event from task 25, say what the provider already covers, "
                "what your plan has to cover, and in what order you would deal with them.",
         uoc=["ICTCLD501 PC 3.2"],
         standard="the student prioritises the risks rather than treating them as equal, and the "
                  "priority order is defensible against the ratings from task 25. The pairing of "
                  "provider protection against plan responsibility is the substance of PC 3.2.",
         given=1, blank_rows=5,
         table=(["Risk event", "Provider protection", "What your plan must add", "Priority"],
                [["Loss of the Sydney region", "regions fail independently",
                  "everything — a second region does not exist until you create it", "1"],
                 ["Data corruption", "automated backups and point-in-time restore",
                  "a copy outside the region, and a decision about restore point", "2"],
                 ["Denial of service", "platform-level absorption at the edge",
                  "the web application firewall and rate limiting from Part A", "3"],
                 ["Loss of the India log store", "regional durability of stored objects",
                  "the recovery path that keeps the logs in an Indian region", "4"],
                 ["Accidental deletion by change",
                  "none — this is a YAT action, not a provider event",
                  "change discipline, and infrastructure defined as code to rebuild from", "5"]])),

    dict(n=31, title="Insurance",
         prompt="Assess whether external insurance protection is appropriate here, and at what level. "
                "This is a real question with a real answer either way — say what you would "
                "recommend to YAT and on what basis. If your answer is that it sits outside your "
                "scope, say who it belongs to and what you would tell them.",
         uoc=["ICTCLD501 PC 3.3"],
         standard="the student engages with the question rather than skipping it, and reaches a "
                  "position: what cyber or business-interruption cover would and would not do for "
                  "this system, and the recommendation to YAT. PC 3.3 asks the student to ASSESS "
                  "suitability — 'not applicable' with no reasoning has not met it, but a reasoned "
                  "'this is YAT's commercial decision, and here is what they need to know' has.",
         given=1, blank_rows=4,
         table=(["Cover type", "What it would protect", "Suitability here"],
                [["Cyber liability",
                  "costs of a breach of the personal information in enquiry submissions",
                  "relevant — the site holds personal information under the Privacy Act"],
                 ["Business interruption",
                  "revenue lost while the site is unavailable",
                  "limited — YAT's revenue is enrolment, not transactions on the site"],
                 ["Provider service credits",
                  "a partial refund of service charges for a breached service level",
                  "not insurance; does not restore service or cover YAT's loss"],
                 ["Recommendation to YAT",
                  "cyber liability warrants review; the rest is a commercial decision",
                  "MTS advises the technical exposure; YAT's business area decides cover"]])),

    dict(n=32, title="Other recovery components",
         prompt="A recovery plan is more than infrastructure. Identify the other components this plan "
                "needs to work at 3am — the people, the access, the contacts, the communications, and "
                "anything else without which the technical steps cannot be carried out.",
         uoc=["ICTCLD501 PC 3.4"],
         standard="the student identifies non-technical components — who has authority to invoke, "
                  "who holds the credentials, how stakeholders are told, and where the plan itself "
                  "can be read when the environment is down. The last one is the test of whether "
                  "they have thought about it: a plan stored only in the failed region is not a "
                  "plan.",
         given=1, blank_rows=6,
         table=(["Component", "What it is", "Why the plan fails without it"],
                [["Invocation authority", "who decides this is a disaster and declares it",
                  "without it the team waits, and the clock is running"],
                 ["Access to the second region",
                  "credentials and permissions that work when the primary is gone",
                  "recovery cannot start"],
                 ["Contact list", "on-call ICT, Sam Walker, MTS, the provider",
                  "nobody can be reached out of hours"],
                 ["Stakeholder communications",
                  "what Marketing tells prospective students while the site is down",
                  "reputational damage compounds the outage"],
                 ["An off-region copy of this plan",
                  "the document itself, readable when Sydney is unavailable",
                  "the plan is inaccessible exactly when it is needed"],
                 ["DNS control", "the ability to repoint the public domain",
                  "the second region can be running and still unreachable"]])),

    dict(n=33, title="Detection and alerting",
         prompt="A recovery plan starts when someone finds out. Say how a region-level disaster "
                "affecting this website would be detected, what would alert whom, and how long you "
                "would expect detection to take. Remember detection has to work from outside the "
                "region that has failed.",
         uoc=["ICTCLD501 KE 6", "ICTCLD501 PC 4.2"],
         standard="the student proposes detection that does not depend on the failed region — an "
                  "external health check or a monitor in the second region — and names who is "
                  "alerted. Detection time counts against the RTO, and a strong answer says so. "
                  "Monitoring configured only inside the primary region has not met the item.",
         given=1, blank_rows=5,
         table=(["Signal", "What raises it", "Who is alerted", "Expected detection time"],
                [["External endpoint health check",
                  "the public URL stops responding from outside the region", "on-call YAT ICT",
                  "within minutes"],
                 ["Edge origin errors",
                  "the content delivery network cannot reach its origin", "on-call YAT ICT",
                  "within minutes"],
                 ["Provider service health notification", "a declared regional service event",
                  "YAT ICT and Sam Walker", "variable — not relied on as the trigger"],
                 ["Audit-log write failures",
                  "events stop being written to the India store", "on-call YAT ICT",
                  "within the hour"],
                 ["Detection counts against RTO",
                  "the 4-hour clock starts at the event, not at the alert", "—",
                  "budget it explicitly"]])),

    dict(n=34, title="The recovery steps",
         prompt="Write the recovery steps for your recommended strategy — what is actually done, in "
                "order, by whom, and how long each step takes. This is the section someone follows "
                "under pressure. Number the steps, give each a duration, and make the total add up "
                "to less than your RTO.",
         uoc=["ICTCLD501 PC 4.2", "ICTCLD501 FS Planning and organising"],
         standard="the steps are sequenced, assigned to a role, and carry timings that sum to within "
                  "the RTO from task 23. PC 4.2 names timelines, key features and service providers "
                  "explicitly — all three must appear. Steps with no durations cannot be checked "
                  "against the objective and have not met the item.",
         given=1, blank_rows=8,
         table=(["#", "Step", "Who", "Duration"],
                [["1", "Confirm the event and declare a disaster", "on-call ICT → Sam Walker",
                  "15 min"],
                 ["2", "Notify stakeholders; Marketing publishes the holding message",
                  "Sam Walker / Marketing", "15 min"],
                 ["3", "Deploy the infrastructure-as-code stack into the second region",
                  "YAT ICT with MTS", "45 min"],
                 ["4", "Promote the replicated database in the second region", "YAT ICT", "30 min"],
                 ["5", "Restore media from the replicated bucket", "YAT ICT", "30 min"],
                 ["6", "Repoint DNS and the content delivery network origin to the second region",
                  "YAT ICT", "30 min"],
                 ["7", "Verify the site, the enquiry form and the audit-log path", "YAT ICT + MTS",
                  "30 min"],
                 ["8", "Confirm recovery and stand down; begin the incident record",
                  "Sam Walker", "15 min"]])),

    dict(n=35, title="How the plan meets the recovery objectives",
         prompt="Show that your plan actually achieves the objectives you set in task 23. Add up your "
                "recovery steps against the RTO, and explain what mechanism delivers the RPO. If the "
                "numbers do not work, change the plan — do not change the objective.",
         uoc=["ICTCLD501 PE 3", "ICTCLD501 KE 5"],
         standard="the student demonstrates the arithmetic — the summed step durations plus a "
                  "detection allowance against the RTO — and names the specific mechanism that "
                  "delivers the RPO (continuous or near-continuous database replication, not nightly "
                  "backups). PE 3 requires the plan to show the WAYS it reaches the targets; an "
                  "assertion that it meets them has not met the item.",
         given=1, blank_rows=4,
         table=(["Objective", "Target", "What the plan achieves", "The mechanism"],
                [["RTO", "≤ 4 hours",
                  "≈ 3 hours 30 min of steps plus detection — inside the target with margin",
                  "infrastructure as code deploys the second region rather than rebuilding by hand"],
                 ["RPO", "≤ 1 hour",
                  "minutes, not hours",
                  "cross-region replication of the database, running continuously"],
                 ["Media RPO", "≤ 24 hours", "within a day",
                  "cross-region replication of the media bucket"],
                 ["India log residency during recovery", "maintained",
                  "logs recover into an Indian region, never into the DR region",
                  "the log store is separately deployed and region-parameterised"]])),

    dict(n=36, title="The standards this plan reflects",
         resources=[
             ("Industry Standards — the information-security and continuity standards YAT works to",
              f"{REFERENCE}/industry-standards"),
         ],
         prompt="Name the information-security and business-continuity standards that informed this "
                "plan, and for each say where it shows up in what you have written. A standard you "
                "cannot point to in your own plan is one you have listed rather than applied.",
         uoc=["ICTCLD501 KE 4"],
         standard="ISO 27001, ISO 27002 and ISO 27031 are all named — that trio is the whole of "
                  "KE 4 — and each is tied to a specific section of the student's own plan. A "
                  "definition of each standard with no link to the plan has not met the contextual "
                  "bar this cluster applies to knowledge evidence.",
         given=1, blank_rows=4,
         table=(["Standard", "What it covers", "Where it shows up in your plan"],
                [["ISO/IEC 27001",
                  "the information security management system — risk-based control selection",
                  "the risk assessment in task 25 and the ratings method behind it"],
                 ["ISO/IEC 27002",
                  "the control set itself — the practices an organisation implements",
                  "backup, access control and the handling of personal information during recovery"],
                 ["ISO/IEC 27031",
                  "ICT readiness for business continuity — the standard closest to this document",
                  "the recovery objectives, strategy and step-by-step plan in tasks 4 to 16"]])),

    dict(n=37, title="Assemble the Disaster Recovery Plan",
         prompt="Now build the document. Open the YAT Disaster Recovery Plan template and copy your "
                "answers across using the map below — your work is done, this is transcription. "
                "Write the Executive Summary last, once you can see the whole plan. Submit both this "
                "worksheet and the completed plan. You will walk Sam Walker through the plan in "
                "Part C, and lodge it formally once it is approved — so this is the version you "
                "present, not yet the lodged record.",
         uoc=["ICTCLD501 PC 4.3", "ICTCLD501 PE 1", "ICTCLD501 FS Self-management"],
         standard="the completed plan is a coherent document containing at least three major risk "
                  "events (PE 1) and is documented to the YAT reporting standard the template sets "
                  "(PC 4.3, and the reason `[ICTCLD501 AC 3]` requires a template at all). The "
                  "assessor marks the SUBMITTED PLAN for this item; the worksheet is the evidence "
                  "that the thinking behind it is the student's own. A plan whose content differs "
                  "materially from the worksheet is worth a conversation before it is marked.",
         given=2, blank_rows=18,
         table=(["Template section", "Comes from", "Done"],
                [["1. Executive Summary", "written last, from the whole plan", ""],
                 ["2. Engagement Context and Scope", "task 20, and Part A's engagement framing", ""],
                 ["3.1 Existing recovery arrangements", "task 21", ""],
                 ["3.2 Vendor provisions and SLAs", "task 22", ""],
                 ["4.1 Recovery objectives (RTO / RPO)", "task 23", ""],
                 ["4.2 Data managed", "task 24", ""],
                 ["4.3 Risk assessment", "task 25", ""],
                 ["4.4 Plan exclusions", "task 26", ""],
                 ["4.5 Recording the analysis", "task 27", ""],
                 ["5.1 Options evaluated", "task 28", ""],
                 ["5.2 Recommended approach", "task 29", ""],
                 ["5.3 Vendor protections and risk prioritisation", "task 30", ""],
                 ["5.4 Insurance", "task 31", ""],
                 ["5.5 Other recovery components", "task 32", ""],
                 ["6.1 Detection and alerting", "task 33", ""],
                 ["6.2 Recovery steps", "task 34", ""],
                 ["6.3 Meeting the recovery objectives", "task 35", ""],
                 ["7. Plan Validation and Approval", "completed at your Part C presentation", ""]])),
]

# ---------------------------------------------------------------- knowledge questions

QUESTIONS = [
    dict(n=5, title="What is distinctive about the risk environment of a public, cloud-hosted "
                    "website?",
         prompt="Explain what makes this system's risk environment different from an internal, "
                "authenticated system like the LMS — and say how your three major risk events in "
                "task 25 reflect that difference.",
         uoc=["ICTCLD501 KE 1"],
         standard="the student identifies public, unauthenticated internet exposure as the "
                  "distinguishing feature — anyone can reach it, hostile traffic is constant, and "
                  "the attack surface is not bounded by an identity system — and connects that to "
                  "their own risk events. A generic list of cloud risks has not met the contextual "
                  "bar.",
         points=[
             "anyone on the internet can reach it; there is no login to keep anyone out",
             "hostile and automated traffic is continuous rather than exceptional",
             "reputational exposure is immediate and public — an outage is visible to the market "
             "YAT is trying to win",
             "the shared-responsibility model puts the region and the workload's recovery on YAT, "
             "not the provider",
             "the India obligations add a regulatory risk an Australian-only system does not carry",
         ]),

    dict(n=6, title="What method did you use to identify and rate the risks, and why does it suit "
                    "this job?",
         prompt="Name the method behind your task 25 ratings and explain why it is appropriate here "
                "rather than something more or less formal.",
         uoc=["ICTCLD501 KE 2"],
         standard="a named method — a likelihood × consequence matrix is the expected answer — with "
                  "reasoning about why that level of formality suits an engagement of this size. "
                  "KE 2 is about data analysis methodologies to determine the risk environment; the "
                  "student must be able to say what they did, not just what they concluded.",
         points=[
             "a likelihood × consequence matrix, with the scales stated",
             "inputs: the infrastructure specification, the consultation notes, and the incident "
             "history YAT has",
             "why it suits: proportionate, repeatable by someone else, and defensible to Sam Walker",
             "its limit: likelihood for rare regional events is a judgement, not a measurement",
         ]),

    dict(n=7, title="Explain the cloud disaster recovery techniques available, and why yours fits "
                    "this website.",
         prompt="Set out the recovery techniques cloud environments make available, and explain why "
                "the one you recommended in task 29 fits this website's objectives better than the "
                "others.",
         uoc=["ICTCLD501 KE 3", "ICTCLD501 KE 5"],
         standard="the recognised set is described — backup and restore, pilot light, warm standby, "
                  "multi-site — with the RTO/RPO trade-off understood, and the student's own choice "
                  "argued against their objectives. This is KE 3 and KE 5 together: the techniques, "
                  "and the objectives they are selected against.",
         points=[
             "the four techniques and where each sits on the cost-versus-recovery-time curve",
             "RTO and RPO are what select between them, not preference",
             "why pilot light fits a 4-hour RTO on a read-heavy public site",
             "what would move the answer: a tighter RTO, or the site becoming transactional",
         ]),
]

# ---------------------------------------------------------------- rendering


def render(doc, h1, h2, mode="student", plan=None, questions=None, notes=False):
    """Render Part B into `doc`. mode = student | assessor."""
    PLAN_ = PLAN if plan is None else plan
    QUESTIONS_ = QUESTIONS if questions is None else questions

    h1("Part B — Disaster Recovery Plan")
    for para in INTRO:
        R.p(doc, para, after=8)
    R.resources_block(doc, RESOURCES)
    R.p(doc, TEMPLATE_NOTE, italic=True, size=9.5, colour=R.GREY, after=10)

    for el in PLAN_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Knowledge questions")
    R.p(doc, "Answer these about your own plan. Generic answers about disaster recovery will not "
             "pass.", italic=True, size=9.5, colour=R.GREY, after=10)
    for q in QUESTIONS_:
        R.element(doc, h2, q, mode, label="Question", notes=notes)
