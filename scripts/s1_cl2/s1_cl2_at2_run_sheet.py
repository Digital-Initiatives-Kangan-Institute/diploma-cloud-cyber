#!/usr/bin/env python3
"""The S1-CL2 AT2 microservice-and-IaC build workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), through the shared workbook engine in
the umbrella (`helpers/run_sheet.py`).

WHY THERE IS NO DEPLOYMENT REPORT TEMPLATE. ICTCLD505's assessment conditions (AC 1–9) are all
environment conditions — a vendor, an infrastructure-as-code service, an IDE, a browser, an
SSH/RDP client, console/CLI tooling. Like ICTCLD503's, none names a document format or a
reporting standard, and there is no equivalent of `[ICTCLD501 AC 3]` anywhere in this unit. So
`[ICTCLD505 PC 4.1]` "Create user documentation including cloud infrastructure as code
templates" and `[ICTCLD505 PE 4]` are met by task 20 of this worksheet, which asks for real
user documentation with a real audience — whoever operates this stack after the student leaves.
The worksheet is the deliverable.

WHAT IS PROVIDED AND WHAT IS AUTHORED — the seam this whole AT turns on:

  provided   the data-store template (`datastore.yaml`). The student OPERATES it: reads it,
             deploys it, fixes it when it fails, updates it, and eventually removes it. This is
             ICTCLD505 element 2, which is explicitly about PRE-DEFINED templates.
  provided   the microservice application code (`handler.py`) and the webhook contract. The
             student does not write application code — ICTCLD503 element 3 is about deploying
             and configuring, not developing.
  authored   the student's OWN template that provisions the API, the queue, the function and
             the permissions, and wires them to the provided data store. This is ICTCLD505
             element 3 and `[ICTCLD505 PE 2]`.

THE PLANTED FAULT. The provided template does not deploy as supplied: its AttributeDefinitions
declares an attribute named `id` while its KeySchema uses `event_id`, so CloudFormation rejects
it. This is deliberate and it is the evidence for `[ICTCLD505 PC 2.6]` and `[ICTCLD505 KE 7]` —
a student who never sees a template fail has never troubleshot one. Task 7 is where they find
it. Do not fix it in the supplied file.

THE MARKING MODEL. Values here are ours, invented so the student has a concrete task. Each
element carries the `uoc` items it evidences and a `standard` naming what must be true for them
to be met. An assessor marks the standard, never the table.

REGION. The design places the audit store in India; the Learner Lab does not offer that region.
The notation `[scenario: ap-south-1 | deploy: us-east-1]` is used throughout per the umbrella's
region-substitution standard — the design stays multi-region, the deploy is single-region.
"""

from helpers import run_sheet as R  # noqa: E402  (the shared workbook engine, in the umbrella)

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at2"
PROJECT = f"{SITE}/intranet/{STATE}/projects/website-global-expansion"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"
REFERENCE = f"{SITE}/intranet/{STATE}/reference"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "The Website Global Expansion engagement has been approved. The design and the disaster "
    "recovery plan were produced in the previous phase and signed off by Sam Walker (YAT ICT "
    "Manager), and this is the implementation phase.",
    "You remain an MTS Consultant reporting to Pat Lin (MTS Senior Consultant), with Sam Walker "
    "as the person who accepts the build. Your job is to stand up the audit-log microservice that "
    "the approved design calls for, and to do it as code so YAT can reproduce it.",
    "You are building the design that was approved — not a fresh one. Where this run sheet gives "
    "you settings, they come from that design.",
]

RESOURCES = [
    ("Website Global Expansion — Functional & Non-Functional Requirements — the requirement the "
     "microservice exists to satisfy", f"{PROJECT}/requirements"),
    ("Data Residency & Sovereignty Requirements — why the store is in India and why it is "
     "parameterised", f"{PROJECT}/data-residency-requirements"),
    ("Industry Standards — the standards and practices YAT works to",
     f"{REFERENCE}/industry-standards"),
    ("Change Management Procedure — the governance a production-affecting change sits under",
     f"{POLICY}/change-management"),
]

ASSESSOR_PROVIDES = ("Your assessor will tell you the current address of the YAT site, and will "
                     "give you the two provided files reproduced below as downloads so you do not "
                     "have to retype them.")

INSTRUCTIONS = [
    "This is an open-book assessment. You may use the YAT intranet, AWS documentation, and "
    "anything you have from class. What you may not use is another student.",
    "Work the tasks in order. Tasks 1 to 4 are the thinking you do before touching anything; "
    "tasks 5 to 10 operate a template someone else wrote; tasks 11 to 19 build your own.",
    "Take each screenshot as you finish the task, not at the end. Recreating a screen after you "
    "have moved on is painful and sometimes impossible. A task you cannot evidence cannot be "
    "assessed as satisfactory.",
    "Things will fail. That is not a problem with the assessment — troubleshooting is one of the "
    "things being assessed, and there is a task that exists specifically to capture it. Record "
    "what broke and what you did about it rather than quietly fixing it.",
    "Answer the knowledge questions about your own build. Generic answers about infrastructure as "
    "code will not pass.",
]

REGION_NOTE = ("The approved design places the audit store in India — "
               "[scenario: ap-south-1 | deploy: us-east-1]. Build everything in us-east-1 in the "
               "AWS Academy Learner Lab, which does not offer the Indian regions. Where a task "
               "asks you to name the region the design calls for, name ap-south-1; where it asks "
               "what you deployed to, that is us-east-1. The work is identical either way, and "
               "the parameterisation in task 17 is exactly what makes the difference a parameter.")

# ---------------------------------------------------------------- the supplied material

SUPPLIED_INTRO = [
    "Two files are provided to you and are reproduced here in full. You do not write either of "
    "them. Read them both before you start — task 5 and task 11 depend on you having done so.",
]

DATASTORE_YAML = [
    "AWSTemplateFormatVersion: '2010-09-09'",
    "Description: >-",
    "  YAT audit-log data store (PROVIDED - you operate this, you do not author it).",
    "  A single DynamoDB table that holds the append-only access-log records your",
    "  microservice writes. Operate it: review, deploy, update a parameter, and delete.",
    "  It may not deploy as supplied - if so, diagnose the error, fix it, and redeploy.",
    "",
    "Parameters:",
    "  EnvName:",
    "    Type: String",
    "    Default: dev",
    "    AllowedValues: [dev, prod]",
    "    Description: Environment suffix used in the table name.",
    "",
    "Resources:",
    "  AuditTable:",
    "    Type: AWS::DynamoDB::Table",
    "    Properties:",
    "      TableName: !Sub 'yat-audit-${EnvName}'",
    "      BillingMode: PAY_PER_REQUEST",
    "      AttributeDefinitions:",
    "        - { AttributeName: id, AttributeType: S }",
    "      KeySchema:",
    "        - { AttributeName: event_id, KeyType: HASH }",
    "      Tags:",
    "        - { Key: Project, Value: YAT-Website }",
    "        - { Key: Environment, Value: !Ref EnvName }",
    "        - { Key: DataClassification, Value: audit-log }",
    "",
    "Outputs:",
    "  AuditTableName:",
    "    Description: The audit table name - your microservice stack reads this.",
    "    Value: !Ref AuditTable",
    "    Export:",
    "      Name: !Sub 'yat-audit-table-${EnvName}'",
]

WEBHOOK_CONTRACT = [
    "POST  {ApiEndpoint}              # an Output of your deployed stack",
    "Content-Type: application/json",
    "",
    "{",
    '  "event_id":    "3f9a1c2e-...",          # unique id (UUID) - the idempotency key',
    '  "occurred_at": "2026-06-07T01:23:45Z",  # ISO-8601 UTC timestamp',
    '  "user_ref":    "u-48217",               # opaque user reference, not a name',
    '  "cohort":      "IN",                    # "AU" or "IN"  (IN = the India cohort)',
    '  "event_type":  "login",                 # login | course_access | assessment_view',
    '  "source_ip":   "203.0.113.7"            # the client IP the event came from',
    "}",
    "",
    "Responses:   200 = accepted and queued for writing      400 = malformed request",
]

HANDLER_SUMMARY = [
    ("What it is", "handler.py — an SQS-triggered Lambda written in Python 3.12. Provided to you "
                   "in full as a download; you deploy it, you do not write it."),
    ("What it does", "reads access-event messages from the queue, validates each one, and writes "
                     "it to the DynamoDB table as an immutable audit record"),
    ("Data flow", "HTTP API  →  SQS queue  →  this Lambda  →  DynamoDB table"),
    ("Idempotency", "event_id is the partition key and the write is conditional, so a "
                    "re-delivered message is skipped rather than duplicated"),
    ("What it needs from you", "an environment variable AUDIT_TABLE holding the table name, and "
                               "permission to write to that table"),
    ("Runtime note", "boto3 is provided by the Lambda runtime — there are no dependencies to "
                     "package"),
]

# ---------------------------------------------------------------- the tasks

TASKS = [
    # ---------------------------------------- 505 element 1 — before you build
    dict(n=1, title="Why infrastructure as code for this job",
         resources=[
             ("Website Global Expansion — Functional & Non-Functional Requirements — the "
              "requirement that the changes be provisioned as code", f"{PROJECT}/requirements"),
             ("Data Residency & Sovereignty Requirements — DR-R4, keeping the Indian footprint "
              "extensible", f"{PROJECT}/data-residency-requirements"),
         ],
         prompt="Before you build anything, establish why this is being built as code at all. "
                "Identify the benefits infrastructure as code brings to THIS engagement — not in "
                "general — and tie each one to a business need you can point at in the "
                "requirements.",
         uoc=["ICTCLD505 PC 1.1", "ICTCLD505 KE 3", "ICTCLD505 FS Reading"],
         standard="the benefits are tied to this engagement's stated needs rather than listed "
                  "generically. The residency requirement DR-R4 (keep localisation extensible) and "
                  "the requirement to stand the environment up in another region by changing "
                  "configuration are both in the supplied documents and both are answers. A list of "
                  "generic IaC benefits with no business need beside it has not met PC 1.1, which "
                  "says 'according to business needs'.",
         given=1, blank_rows=5,
         table=(["Benefit", "What it gives YAT here", "The business need it answers"],
                [["Reproducible in another region",
                  "the Indian footprint can be stood up elsewhere by changing a parameter",
                  "DR-R4 — keep localisation extensible without re-architecture"],
                 ["Repeatable disaster recovery",
                  "the second region is deployed from the same template during a recovery",
                  "the 4-hour RTO in the approved DR plan"],
                 ["Consistency between environments",
                  "dev and prod are the same definition with a different parameter",
                  "the requirement that the environment be reproduced consistently"],
                 ["Reviewable change",
                  "an infrastructure change is a file change someone can read before it happens",
                  "the Change Management Procedure"],
                 ["No undocumented drift",
                  "what is deployed is what is in the template",
                  "YAT ICT has to operate this after MTS leaves"]])),

    dict(n=2, title="What automation gives the platform",
         prompt="Infrastructure as code is one kind of automation. Determine what else about this "
                "build is automated rather than done by hand, and what YAT gets from each. Think "
                "about what happens without anyone present — at 2am, or when a message fails.",
         uoc=["ICTCLD505 PC 1.2"],
         standard="the student identifies automation beyond template deployment — the queue "
                  "retrying a failed write, the function scaling with the event rate, the alarm "
                  "raising itself — and says what each removes the need for a human to do. PC 1.2 "
                  "is about how automation LEVERAGES the platform, so the answer should be about "
                  "capability the platform supplies rather than scripts the student wrote.",
         given=1, blank_rows=5,
         table=(["What is automated", "How the platform does it", "What YAT no longer does by hand"],
                [["Provisioning", "the IaC service creates and orders the resources",
                  "clicking through the console and remembering the order"],
                 ["Retry on failure", "the queue redelivers a message the function did not process",
                  "noticing and replaying lost events"],
                 ["Scaling the processor", "the function runs per message, concurrently",
                  "sizing a server for peak event rate"],
                 ["Capacity for the store", "on-demand billing scales with the write rate",
                  "provisioning throughput ahead of demand"],
                 ["Detection", "the alarm evaluates the metric and notifies",
                  "watching a dashboard"]])),

    dict(n=3, title="What can go wrong with infrastructure as code",
         prompt="Determine and assess what can go wrong when infrastructure is deployed this way. "
                "You are about to find at least one of these for real, so think about it now: what "
                "kinds of error does this approach produce, and how serious is each?",
         uoc=["ICTCLD505 PC 1.3", "ICTCLD505 KE 7"],
         standard="the student names error classes rather than one example — syntax errors, "
                  "invalid resource properties, dependency and ordering failures, permission "
                  "failures, and the destructive-update risk where a change replaces a resource "
                  "rather than modifying it — and assesses severity. The last one is the mark of a "
                  "student who has thought about it rather than listed.",
         given=1, blank_rows=6,
         table=(["What can go wrong", "What it looks like", "How serious"],
                [["Template syntax error", "the service rejects the file before doing anything",
                  "low — fast to find, nothing was created"],
                 ["Invalid or mismatched resource properties",
                  "the stack fails during creation and rolls back",
                  "low to moderate — the error names the resource"],
                 ["Missing dependency or wrong ordering",
                  "a resource is created before the thing it needs",
                  "moderate — the message can be indirect"],
                 ["Insufficient permissions",
                  "creation fails on one resource with an access error",
                  "moderate — easy to misread as a template fault"],
                 ["A change that replaces rather than updates",
                  "the update succeeds and the data is gone",
                  "high — this is the one that hurts in production"],
                 ["Drift from manual console changes",
                  "the template no longer describes what is deployed",
                  "high over time — the template stops being the truth"]])),

    dict(n=4, title="Select the infrastructure-as-code service",
         prompt="Evaluate the infrastructure-as-code services available for this platform and select "
                "one. Say what you compared it against and why your choice suits this engagement. A "
                "choice with no alternative beside it is not an evaluation.",
         uoc=["ICTCLD505 PC 1.4", "ICTCLD505 KE 4"],
         standard="at least two genuine alternatives are compared — CloudFormation, Terraform and "
                  "the CDK are the recognised set and naming them satisfies KE 4 — and the selection "
                  "is argued against this engagement's constraints (a single cloud platform, the "
                  "Learner Lab environment, and YAT ICT operating it afterwards). Any of them is an "
                  "acceptable choice if the reasoning holds.",
         given=1, blank_rows=4,
         table=(["Service", "What it is", "Suitability here"],
                [["AWS CloudFormation", "the vendor's own declarative service, native to the "
                                        "platform",
                  "no extra tooling, available in the lab, and the provided template is already "
                  "written in it"],
                 ["Terraform", "a third-party tool that works across multiple cloud platforms",
                  "strong, but its multi-cloud benefit is not one YAT needs here"],
                 ["AWS CDK", "infrastructure defined in a general-purpose programming language",
                  "powerful, but adds a build step and a language YAT ICT may not maintain"],
                 ["Your selection", "CloudFormation",
                  "matches the provided artefact, needs no extra tooling, and YAT ICT can read it"]])),

    # ---------------------------------------- 505 element 2 — operate the provided template
    dict(n=5, title="Review the provided data-store template",
         prompt="Read the provided template above, closely. Work out what it creates, what each "
                "part of it does, and what depends on what. Do not deploy it yet — the point of "
                "this task is that you can read a template someone else wrote before you run it.",
         uoc=["ICTCLD505 PC 2.1", "ICTCLD505 PC 2.2", "ICTCLD505 KE 5", "ICTCLD505 FS Reading"],
         standard="the student identifies the single DynamoDB table, the parameter that names it, "
                  "the export that other stacks consume, and the section structure of the template "
                  "itself (Parameters, Resources, Outputs). Recognising that the Export is the "
                  "dependency their own stack will consume is what PC 2.2's 'any dependencies' is "
                  "asking for.",
         given=1, blank_rows=6,
         table=(["Part of the template", "What it does", "What depends on it"],
                [["Parameters — EnvName",
                  "supplies the environment suffix, constrained to dev or prod",
                  "the table name and the export name are both built from it"],
                 ["Resources — AuditTable",
                  "creates one DynamoDB table, billed per request",
                  "the microservice writes to it"],
                 ["TableName — !Sub", "builds the name from the parameter",
                  "how the two environments stay separate"],
                 ["Tags", "project, environment and data classification",
                  "YAT's records and cost reporting"],
                 ["Outputs — AuditTableName with Export",
                  "publishes the table name for other stacks",
                  "your own template imports this in task 12"],
                 ["What it does NOT create",
                  "no API, no queue, no function — those are yours",
                  "nothing; it is the boundary of the provided work"]])),

    dict(n=6, title="Deploy the provided template",
         prompt="Deploy the provided template using the infrastructure-as-code service's tooling. "
                "Use the console or the command line — your choice, but say which you used and why. "
                "It will not succeed. Capture what happens.",
         uoc=["ICTCLD505 PC 2.3", "ICTCLD505 PE 1", "ICTCLD505 PE 3", "ICTCLD505 KE 6",
              "ICTCLD503 PE 4"],
         standard="the student runs a real deployment with the service's own tooling and captures "
                  "the failure rather than pre-emptively fixing the template. Naming the tool used "
                  "(console, CLI, or SDK) satisfies KE 6 and the PE 3 items in both units. A student "
                  "who fixed the fault before deploying has skipped the evidence for task 7 and "
                  "should be sent back to deploy it as supplied.",
         given=1, blank_rows=4,
         table=(["Step", "What you did", "What happened"],
                [["Tooling used", "console or CLI — name it, and why you chose it", ""],
                 ["Stack name", "yat-audit-store", ""],
                 ["Parameter", "EnvName=dev", ""],
                 ["Result", "the stack did not reach CREATE_COMPLETE", ""]]),
         evidence=["the failed stack showing its status and the failure reason"]),

    dict(n=7, title="Diagnose and fix the failure",
         prompt="The template does not deploy as supplied. Read the error before changing anything. "
                "Work out what is actually wrong, fix it, and redeploy. Record the error you saw, "
                "what you worked out, and the change you made — this task is about the diagnosis, "
                "not the fix.",
         uoc=["ICTCLD505 PC 2.6", "ICTCLD505 KE 7", "ICTCLD505 FS Problem solving",
              "ICTCLD503 KE 5"],
         standard="the student identifies the real fault: the table declares an attribute named "
                  "`id` in AttributeDefinitions but uses `event_id` as the key in KeySchema, and "
                  "every attribute in the key schema must be defined. Either correction is "
                  "acceptable — renaming the definition to `event_id` is the one that matches the "
                  "webhook contract and the provided handler, and a student who notices that has "
                  "read further than the error message. Guessing changes until it works, with no "
                  "diagnosis recorded, has not met PC 2.6.",
         given=1, blank_rows=4,
         table=(["Diagnosis", "Your answer"],
                [["The error message you saw",
                  "the key schema references an attribute not present in the attribute definitions"],
                 ["What you worked out it meant",
                  "AttributeDefinitions declares `id`; KeySchema uses `event_id`; they must agree"],
                 ["The change you made",
                  "renamed the attribute definition to `event_id`"],
                 ["Why that fix and not the other one",
                  "the provided handler and the webhook contract both use event_id, so the key must "
                  "be event_id"]]),
         evidence=["the stack reaching CREATE_COMPLETE after your fix"]),

    dict(n=8, title="Confirm the deployment",
         prompt="Confirm the resources actually exist and are configured the way the template said. "
                "Do not take the stack's success message as proof — go and look at the resource "
                "itself, using the console or the command line.",
         uoc=["ICTCLD505 PC 2.4", "ICTCLD505 PE 3", "ICTCLD503 PE 4"],
         standard="the student inspects the created table itself rather than only the stack, and "
                  "confirms the name, the key and the tags against the template. PC 2.4 says "
                  "'confirm deployments … using cloud platform console or command line tools', so "
                  "the evidence must show the resource, not the stack event list.",
         given=1, blank_rows=4,
         table=(["What you confirmed", "How you confirmed it", "What you saw"],
                [["The table exists with the expected name", "console or CLI", "yat-audit-dev"],
                 ["The partition key", "the table's key schema", "event_id"],
                 ["The tags applied", "the table's tags", "Project, Environment, "
                                                          "DataClassification"],
                 ["The stack output and export", "the stack's Outputs tab", "the exported table "
                                                                           "name"]]),
         evidence=["the deployed table showing its name, key schema and tags"]),

    dict(n=9, title="Update the provided template and redeploy",
         prompt="Change the parameter and redeploy the same template, so the stack modifies what is "
                "already there rather than creating something new. Record what changed and — more "
                "importantly — what happened to the resource that already existed.",
         uoc=["ICTCLD505 PC 2.3", "ICTCLD505 PE 1", "ICTCLD505 KE 10"],
         standard="the student redeploys with EnvName=prod and observes what the platform does. The "
                  "table name is part of the resource's identity, so this update REPLACES the table "
                  "rather than renaming it — a student who notices that, and connects it to the "
                  "destructive-update risk they identified in task 3, has understood something the "
                  "task is really testing. Noticing is what is marked, not predicting it in advance.",
         given=1, blank_rows=4,
         table=(["Step", "What you did", "What happened"],
                [["The change", "redeployed with EnvName=prod", ""],
                 ["What the service did",
                  "created a new table and removed the old one — the name is part of its identity",
                  ""],
                 ["What that means for real data",
                  "an update like this in production would destroy the audit records", ""],
                 ["Which task warned you", "task 3 — the replace-rather-than-update risk", ""]]),
         evidence=["the stack update, and the resulting table"]),

    dict(n=10, title="Return the store to a known state",
         prompt="You need the data store running with EnvName=dev for the rest of this build. Put it "
                "back there, and confirm it. Say what you did — whether you updated again or "
                "removed and redeployed — and why that was the right way round.",
         uoc=["ICTCLD505 PC 2.3", "ICTCLD505 PC 2.4"],
         standard="the store ends this task deployed at EnvName=dev and confirmed. Either route is "
                  "acceptable; what is marked is that the student knew the state they needed and "
                  "verified they had it, rather than assuming.",
         given=1, blank_rows=3,
         table=(["Step", "What you did", "Confirmed how"],
                [["Returned the store to EnvName=dev", "", ""],
                 ["Confirmed the table name and key", "", ""],
                 ["Confirmed the export is available for your own stack", "", ""]])),

    # ---------------------------------------- 503 element 3 + 505 element 3 — your own build
    dict(n=11, title="Review the microservice code and contract",
         prompt="Read the provided handler and the webhook contract above. Work out what the code "
                "expects from the infrastructure you are about to build — what it reads, what it "
                "writes, what it needs to be told, and what permissions it will need. Everything "
                "your template has to provide is discoverable from these two things.",
         uoc=["ICTCLD503 PC 3.1", "ICTCLD505 FS Reading"],
         standard="the student extracts the infrastructure requirements from the code rather than "
                  "guessing: the function is triggered by the queue, it reads the table name from an "
                  "AUDIT_TABLE environment variable, and it needs write permission on that table. "
                  "PC 3.1 is 'review microservice design and code components' — a student who starts "
                  "authoring without this task has nothing to build against.",
         given=1, blank_rows=5,
         table=(["What the code needs", "Where you found it", "What your template must provide"],
                [["To be triggered by queue messages", "the handler reads event['Records']",
                  "an event source mapping from the queue to the function"],
                 ["The table name", "os.environ.get('AUDIT_TABLE')",
                  "an environment variable set from the provided stack's export"],
                 ["Permission to write to the table", "table.put_item(...)",
                  "a role allowing write access to that table"],
                 ["A Python 3.12 runtime", "the module docstring; boto3 is supplied by the runtime",
                  "the runtime setting — no dependency packaging"],
                 ["Something to receive the HTTP call", "the webhook contract — POST to an endpoint",
                  "an HTTP API that puts the body on the queue"]])),

    dict(n=12, title="Author your template",
         prompt="Write the infrastructure-as-code template that deploys the microservice. It "
                "provisions the API, the queue and the function, sets the function's environment "
                "variable from the provided stack's export, and grants the permissions the function "
                "needs. Record the structure of what you wrote — the actual file is submitted with "
                "this worksheet.",
         uoc=["ICTCLD505 PC 3.1", "ICTCLD505 PC 3.2", "ICTCLD505 KE 5", "ICTCLD505 KE 9"],
         standard="the template provisions a set of RELATED resources — API, queue, function, "
                  "permissions — rather than one resource, and connects to the provided store "
                  "through its export or an equivalent parameter. KE 9 (industry standard practices) "
                  "is evidenced by the template being structured and readable: named parameters, "
                  "sensible logical IDs, described outputs. A template that hard-codes the table "
                  "name has not connected to the provided stack the way task 11 established.",
         given=1, blank_rows=6,
         table=(["Section of your template", "What you put in it", "Why"],
                [["Parameters", "EnvName, matching the provided stack",
                  "the two stacks have to agree on which environment they are"],
                 ["The HTTP API", "an endpoint that accepts POST and puts the body on the queue",
                  "the single integration point the contract defines"],
                 ["The queue", "a standard queue between the API and the function",
                  "decoupling — the website is not waiting on the write"],
                 ["The function", "Python 3.12, running the provided handler",
                  "the processor; the code is provided, the infrastructure is yours"],
                 ["Environment variable", "AUDIT_TABLE, from the provided stack's export",
                  "how the function finds the table without it being hard-coded"],
                 ["Permissions", "write access to the table, and read from the queue",
                  "least privilege — only what the handler actually does"]])),

    dict(n=13, title="Deploy your template",
         prompt="Deploy your own template. Expect it to take more than one attempt — that is normal "
                "for a first template and it is not a mark against you. Record the attempts.",
         uoc=["ICTCLD505 PC 3.2", "ICTCLD505 PE 2", "ICTCLD503 PC 3.2", "ICTCLD503 PE 3"],
         standard="the student's own template reaches a successful deployment and the stack creates "
                  "the API, the queue and the function. PE 2 requires the student to create and run "
                  "at least one template of their own — this task is where that is evidenced, and it "
                  "must be the student's own file, not the provided one modified.",
         given=1, blank_rows=4,
         table=(["Attempt", "What happened", "What you changed"],
                [["1", "", ""],
                 ["2", "", ""],
                 ["3", "", ""],
                 ["Final", "the stack reached CREATE_COMPLETE", "—"]]),
         evidence=["your stack showing CREATE_COMPLETE and the resources it created"]),

    dict(n=14, title="Confirm your deployment",
         prompt="Confirm the resources your template created, using the console or the command line. "
                "Check the wiring, not just the existence — the function has to be connected to the "
                "queue, and it has to know the table name.",
         uoc=["ICTCLD505 PC 3.4", "ICTCLD505 PE 3", "ICTCLD503 PE 4"],
         standard="the student confirms the API endpoint, the queue, the function, the event source "
                  "mapping between queue and function, and the AUDIT_TABLE environment variable "
                  "holding the real table name. Checking the environment variable is the one that "
                  "separates a student who confirmed from one who glanced.",
         given=1, blank_rows=5,
         table=(["Resource", "What you checked", "What you saw"],
                [["HTTP API", "the endpoint URL exists and is an output of your stack", ""],
                 ["Queue", "created, and named as your template said", ""],
                 ["Function", "created, Python 3.12, running the provided handler", ""],
                 ["Trigger", "the queue is an event source for the function", ""],
                 ["Environment variable", "AUDIT_TABLE holds the real table name", ""]]),
         evidence=["the function's configuration showing its trigger and environment variable"]),

    dict(n=15, title="Test the microservice end to end",
         prompt="Send a real event through the contract and confirm it arrives in the store. Use the "
                "payload shape from the webhook contract above. Then send one that breaks the "
                "contract — a missing field or an invalid cohort — and record what happens to it.",
         uoc=["ICTCLD503 PC 3.3", "ICTCLD503 PE 3", "ICTCLD505 PE 3"],
         standard="a valid event is posted and the resulting record is shown in the table; an "
                  "invalid event is posted and the student can say what became of it (the handler "
                  "rejects it and logs the reason — it is not written). Testing only the happy path "
                  "has half-met PC 3.3, which asks the student to confirm the application is "
                  "functioning.",
         given=1, blank_rows=4,
         table=(["Test", "What you sent", "What you expected", "What happened"],
                [["Valid event", "a complete payload per the contract",
                  "200 accepted, and one record in the table", ""],
                 ["The record itself", "—", "all six fields present and correct", ""],
                 ["Duplicate event", "the same payload again, same event_id",
                  "no second record — the write is conditional", ""],
                 ["Invalid event", "a payload missing a required field",
                  "rejected and logged; nothing written", ""]]),
         evidence=["the request and its response",
                   "the record in the table",
                   "the function log showing the rejection of the invalid event"]),

    dict(n=16, title="Troubleshoot what went wrong",
         prompt="Record what actually broke during tasks 12 to 15 and what you did about it. Every "
                "real build has these. An empty table here is not a sign of a perfect build — it is "
                "a sign you did not write them down as you went.",
         uoc=["ICTCLD505 PC 3.7", "ICTCLD503 PC 3.4", "ICTCLD505 KE 7", "ICTCLD503 KE 5",
              "ICTCLD505 FS Problem solving"],
         standard="at least two genuine problems are recorded with the symptom, the diagnosis and "
                  "the fix, and the diagnosis shows a method — reading the log, checking the "
                  "permission, testing the piece in isolation. Common real ones: the function lacks "
                  "write permission, the event source mapping is missing so nothing is consumed, or "
                  "the import name does not match the provided stack's export.",
         given=1, blank_rows=5,
         table=(["Symptom", "How you diagnosed it", "The fix"],
                [["Events accepted by the API but no record appears",
                  "checked the function log — an access-denied error on the write",
                  "added write permission on the table to the function's role"],
                 ["Nothing invokes the function at all",
                  "the queue has messages; the function has no invocations",
                  "the event source mapping between queue and function was missing"],
                 ["The stack fails on the import",
                  "the export name does not match what the provided stack published",
                  "corrected the import to the exact exported name"],
                 ["", "", ""],
                 ["", "", ""]])),

    dict(n=17, title="Parameterise for a second environment",
         prompt="Redeploy your template as a second, separate environment by changing configuration "
                "only — not by editing resource definitions. This is the thing that makes the India "
                "region a parameter rather than a rebuild, which is what the residency requirement "
                "asked for. Confirm the two environments are genuinely separate.",
         uoc=["ICTCLD505 PC 3.5", "ICTCLD505 KE 8"],
         standard="the student deploys a second stack from the same template with a different "
                  "parameter, and both exist independently with distinct resource names. KE 8 "
                  "(parameterisation to support configuration and code reuse) is evidenced by the "
                  "template being reused unchanged — a student who copied the file and edited it has "
                  "not parameterised anything.",
         given=1, blank_rows=4,
         table=(["Step", "What you did", "Result"],
                [["Second deployment", "same template, different EnvName", ""],
                 ["What you did NOT change", "the template file itself", ""],
                 ["Confirmed separate", "distinct API endpoints, queues, functions", ""],
                 ["What this proves for the design",
                  "the region would be a parameter too — DR-R4 stays open", ""]]),
         evidence=["both stacks existing side by side"]),

    dict(n=18, title="Update your template to add a resource",
         prompt="Modify your template to add a new resource, and redeploy so the existing stack is "
                "updated rather than replaced. A dead-letter queue for messages the function could "
                "not process is the sensible addition — it is what the DR plan's retention argument "
                "assumed. Record what the update did to what was already there.",
         uoc=["ICTCLD505 PC 3.3", "ICTCLD505 KE 10"],
         standard="a new resource is added by updating the existing stack, and the student can say "
                  "which existing resources were modified and which were left alone. PC 3.3 is "
                  "specifically 'update and redeploy … to modify previously deployed resources AND "
                  "add new resources', so both halves must appear.",
         given=1, blank_rows=4,
         table=(["Change", "What you added or modified", "What the update did"],
                [["New resource", "a dead-letter queue", ""],
                 ["Modified resource", "the main queue, to redrive to it after N failures", ""],
                 ["Unchanged", "the API and the function", ""],
                 ["Why this addition", "failed events are retained rather than lost", ""]]),
         evidence=["the updated stack showing the new resource"]),

    dict(n=19, title="Set up a metric and an alarm",
         prompt="Set up monitoring for the service you have built: a metric that tells you it is "
                "healthy, and an alarm that fires when it is not. Say what the alarm means in "
                "business terms — what has actually gone wrong for YAT when it fires.",
         uoc=["ICTCLD503 PC 4.1"],
         standard="a metric and a working alarm are configured, and the student can say what "
                  "condition it detects and why that condition matters. Sensible answers: queue "
                  "depth or message age rising (events are not being written), function errors, or "
                  "dead-letter queue depth above zero. An alarm on something that does not indicate "
                  "a problem has not met the item.",
         given=1, blank_rows=4,
         table=(["Metric", "Alarm condition", "What it means has gone wrong"],
                [["Age of the oldest message on the queue", "older than a threshold you set",
                  "events are arriving but not being written — the residency obligation is at risk"],
                 ["Function errors", "any errors in a period",
                  "the writer is failing; messages will end up in the dead-letter queue"],
                 ["Dead-letter queue depth", "greater than zero",
                  "events have been abandoned after retries and need manual attention"],
                 ["Who is notified", "the on-call YAT ICT address", "—"]]),
         evidence=["the alarm you created, showing its condition and its state"]),

    # ---------------------------------------- 505 element 4 + 503 element 4 — hand it over
    dict(n=20, title="Write the user documentation",
         prompt="Write the user documentation for what you have built. Its reader is the YAT ICT "
                "person who has to operate this after you leave and who was not here while you built "
                "it. Include your templates — documentation for infrastructure as code that does not "
                "contain the code is not documentation. Write it in the box below; attach your "
                "template files with this worksheet.",
         uoc=["ICTCLD505 PC 4.1", "ICTCLD505 PE 4", "ICTCLD505 FS Writing", "ICTCLD503 FS Writing"],
         standard="the documentation is written FOR AN OPERATOR, not for the assessor: it says what "
                  "the service is, how to deploy it, what the parameters mean, how to update it, how "
                  "to tear it down, and what to do when the alarm fires — and the templates are "
                  "included. PC 4.1 says 'including cloud infrastructure as code templates', so "
                  "documentation without them has not met the item. Prose that narrates what the "
                  "student did during the assessment is a build log, not user documentation.",
         points=[
             "what the service is and what it is for, in two or three sentences an operator can use",
             "the two stacks, which order they deploy in, and why the store goes first",
             "every parameter, its allowed values, and what changing it does — including the warning "
             "from task 9 that changing EnvName replaces the table",
             "how to deploy, how to update, and how to remove, with the actual commands",
             "the templates themselves, included or attached",
             "what the alarm means when it fires, and the first thing to check",
             "known limitations — what this does not do",
         ]),

    dict(n=21, title="Remove what you deployed",
         prompt="Tear down everything you created, using the infrastructure-as-code tooling rather "
                "than deleting resources by hand. Confirm it is gone. This is part of the lifecycle, "
                "not housekeeping — and doing it by hand would leave the templates describing "
                "resources that no longer exist.",
         uoc=["ICTCLD505 PC 2.5", "ICTCLD505 PC 3.6", "ICTCLD505 PE 1"],
         standard="both the student's stacks and the provided stack are removed through the service, "
                  "and the student confirms the resources are gone rather than trusting the delete "
                  "command. Removing resources by hand in the console has not met the item, which "
                  "specifies removal using the infrastructure-as-code tools.",
         given=1, blank_rows=4,
         table=(["What you removed", "How", "Confirmed gone"],
                [["Your second environment stack", "via the IaC service", ""],
                 ["Your microservice stack", "via the IaC service", ""],
                 ["The provided data-store stack", "via the IaC service", ""],
                 ["Anything left behind", "checked for orphaned resources", ""]]),
         evidence=["the stacks removed, and the resource list showing nothing left behind"]),

    dict(n=22, title="Confirm the build and obtain sign-off",
         prompt="Walk Sam Walker (role-played by your assessor) through what you built, confirm it "
                "meets what was approved in AT1, ask for feedback, respond to it, and obtain "
                "sign-off. Record the conversation and the decision.",
         uoc=["ICTCLD503 PC 4.2", "ICTCLD503 PC 4.3", "ICTCLD505 PC 4.2",
              "ICTCLD505 FS Oral communication"],
         standard="the student confirms the build against the approved design, actively seeks "
                  "feedback and responds to it with a decision, and obtains recorded sign-off from "
                  "the required person. PC 4.2 in 503 has three verbs — confirm, seek, respond — and "
                  "all three must appear. A record showing only 'signed off' has not evidenced the "
                  "feedback half.",
         given=1, blank_rows=5,
         table=(["Record", "Your entry"],
                [["What you confirmed against the approved design",
                  "the microservice matches the AT1 Part A design: API, queue, function, in-region "
                  "store"],
                 ["Feedback you sought and were given", ""],
                 ["How you responded", ""],
                 ["Decision", "Approved / Approved with conditions / Not approved"],
                 ["Signed by, and date", "Sam Walker, YAT ICT Manager"]])),
]

# ---------------------------------------------------------------- knowledge questions

QUESTIONS = [
    dict(n=1, title="Which industry standards and standard products does your build rely on?",
         prompt="Name the industry technology standards your build uses, and the standard products "
                "you deployed — including the storage technology. For each, say what it is and why "
                "it was the right sort of thing for this job.",
         uoc=["ICTCLD505 KE 1", "ICTCLD505 KE 2", "ICTCLD503 KE 1", "ICTCLD503 KE 2"],
         standard="the student names real standards (HTTP and REST, JSON, YAML, TLS, ISO-8601 "
                  "timestamps, UUIDs) and real product categories (managed NoSQL storage, managed "
                  "queuing, serverless compute), and explains the storage choice specifically — "
                  "KE 2 in both units names storage technology explicitly. This question carries "
                  "four KE items across two units, so all of standards, products and storage must "
                  "be addressed.",
         points=[
             "HTTP and REST for the webhook, and JSON as the payload format — the contract is built "
             "on both",
             "YAML for the templates; ISO-8601 for timestamps; UUIDs as the idempotency key",
             "TLS on the API endpoint — the events carry an opaque user reference and a source IP",
             "managed NoSQL storage: key-accessed, append-only, scales with write rate without "
             "provisioning",
             "managed queuing and serverless compute as the standard products for event-driven work",
             "why NoSQL and not the website's relational database — different access pattern, and "
             "it must sit in a different region",
         ]),

    dict(n=2, title="How did you test and debug your work?",
         prompt="Describe the techniques you actually used to test and debug both the templates and "
                "the microservice. Point at specific things you found with each technique.",
         uoc=["ICTCLD505 KE 7", "ICTCLD503 KE 5", "ICTCLD505 FS Self-management"],
         standard="the student describes real techniques — reading stack events and failure "
                  "reasons, linting or validating the template before deploying, checking function "
                  "logs, testing components in isolation, sending a deliberately invalid payload — "
                  "and ties each to something they actually found in tasks 7, 15 or 16. A list of "
                  "techniques with no findings attached has not met the contextual bar.",
         points=[
             "read the stack's failure reason first — that is what found the key-schema fault in "
             "task 7",
             "validating or linting the template before deploying, to catch syntax before it costs "
             "a deployment cycle",
             "function logs to see what the code did with a message",
             "testing pieces in isolation — put a message on the queue directly, without the API",
             "a deliberately invalid payload to prove the rejection path works, not just the happy "
             "path",
         ]),

    dict(n=3, title="How would you manage these templates over time?",
         prompt="You are handing this to YAT ICT. Explain how templates like these are managed, "
                "provisioned and updated over their life, and what signals or measures would tell "
                "YAT whether it is going well.",
         uoc=["ICTCLD505 KE 10", "ICTCLD505 KE 11"],
         standard="the student addresses the template lifecycle — version control, review before "
                  "deployment, change sets or plans to preview an update, environment promotion — "
                  "and names measures that indicate health (deployment success rate, time to "
                  "deploy, drift between template and deployed state, failed-change rate). KE 11 "
                  "asks for industry standard metrics, so at least one real measure must appear.",
         points=[
             "the templates live in version control; a change is a reviewed change",
             "preview the effect of an update before applying it, so a replace-not-update is caught "
             "before it destroys data",
             "promote the same template between environments by parameter, never by editing",
             "measures: deployment success rate, how long a deployment takes, how often a change "
             "fails and has to roll back",
             "drift detection — whether what is deployed still matches the template",
             "the alarm from task 19 is the operational signal; these are the delivery signals",
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
    R.note(doc, REGION_NOTE)


def render_supplied(doc, h1, h2):
    h1("What you are given")
    for para in SUPPLIED_INTRO:
        R.p(doc, para, after=8)
    h2("The data-store template — datastore.yaml")
    R.p(doc, "PROVIDED. You operate this template; you do not author it. It may not deploy as "
             "supplied.", italic=True, size=9.5, colour=R.GREY, after=6)
    R.code(doc, DATASTORE_YAML)
    h2("The microservice code — handler.py")
    R.p(doc, "PROVIDED in full as a download. You deploy this code; you do not write it. What it "
             "needs from your infrastructure is summarised here and confirmed in task 11.",
        italic=True, size=9.5, colour=R.GREY, after=6)
    R.settings_table(doc, HANDLER_SUMMARY)
    h2("The webhook contract")
    R.p(doc, "The single integration point between the website and your service.",
        italic=True, size=9.5, colour=R.GREY, after=6)
    R.code(doc, WEBHOOK_CONTRACT)


def render(doc, h1, h2, mode="student", tasks=None, questions=None, notes=False,
           evidence_dir=None):
    """Render AT2 into `doc`. mode = student | assessor."""
    TASKS_ = TASKS if tasks is None else tasks
    QUESTIONS_ = QUESTIONS if questions is None else questions

    h1("The build")
    for task in TASKS_:
        R.element(doc, h2, task, mode, notes=notes)
        if task.get("evidence"):
            R.p(doc, "Evidence", bold=True, size=9.5, after=3)
            images = R.evidence_images(evidence_dir, f"task-{task['n']:02d}")
            R.place_evidence(doc, task["evidence"], mode, images)

    h1("Knowledge questions")
    R.p(doc, "Answer these about your own build. Generic answers about infrastructure as code will "
             "not pass.", italic=True, size=9.5, colour=R.GREY, after=10)
    for q in QUESTIONS_:
        R.element(doc, h2, q, mode, label="Question", notes=notes)
