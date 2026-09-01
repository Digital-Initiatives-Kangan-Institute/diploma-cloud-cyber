#!/usr/bin/env python3
"""The S1-CL3 AT3 implementation workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), through the shared workbook engine in
the umbrella (`helpers/run_sheet.py`).

WHY THERE IS NO DEPLOYMENT REPORT TEMPLATE. ICTCLD504's assessment conditions (AC 1–8) are all
environment and input conditions and name no document format, so `[ICTCLD504 PC 4.1]` "Document
as-deployed architecture and test results" and `[ICTCLD504 PE 5]` "create documentation of
deployment and testing steps" are met by tasks 10 and 11 of this worksheet. The only unit in
this course requiring a separate document is ICTCLD501, via `[ICTCLD501 AC 3]`.

WHAT THE STUDENT IS DEPLOYING, AND WHOSE DESIGN IT IS. AT1 produced each student's own
improvement design and obtained sign-off for it. AT2 encoded an agreed design as infrastructure
as code, as a team. AT3 is individual again: the student deploys the baseline, applies the
approved improvement to it, and demonstrates it against the metrics AT1 set. An assessor
reference template is available as a fallback so that a team integration failure in AT2 cannot
block an individual's evidence here.

THE TESTS ARE THE ASSESSMENT. `[ICTCLD504 PC 3.3]` requires the student to test AND DEMONSTRATE
security, reliability, scalability and cost optimisation — all four. Tasks 5 to 8 are one per
concern, and each asks for a demonstration rather than an assertion: something was made to
happen, and something was observed. A student who says the design is reliable because it spans
two zones has not demonstrated anything; one who terminates an instance and shows the service
continuing has.

THE MARKING MODEL. Values here are ours, invented so the student has a concrete task. Each
element carries the `uoc` items it evidences and a `standard` naming what must be true for them
to be met. An assessor marks the standard, never the table. Because each student's approved
improvement differs, most standards here are about whether the demonstration actually tests the
thing the student themselves designed.
"""

from helpers import run_sheet as R  # noqa: E402  (the shared workbook engine, in the umbrella)

SITE = "https://yat.timbaird.com"
STATE = "s1-cl3-at3"
PROJECT = f"{SITE}/intranet/{STATE}/projects/ledgerline-improvement"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "Your improvement design was approved and the team has encoded it as infrastructure as code. "
    "This is the deployment phase: you stand the environment up, apply the approved improvement, "
    "prove it does what you said it would, and hand it over.",
    "You are an MTS Consultant reporting to Pat Lin (MTS Senior Consultant). Sam Walker (YAT ICT "
    "Manager) accepts the completed work. YAT Finance depend on Ledgerline during business hours, "
    "so your work happens inside a maintenance window and outside the Restricted Period.",
    "You deploy what was approved — not a new design, and not everything the team wrote. If your "
    "sign-off in AT1 approved some improvements and not others, that approved list is your scope.",
]

RESOURCES = [
    ("Improvement Requirements — the outcomes IR-1 to IR-7 the deployed result is judged against",
     f"{PROJECT}/improvement-requirements"),
    ("Accounting System Infrastructure Specifications — the baseline you are deploying and improving",
     f"{ICT}/accounting-server-status-cloud"),
    ("Change Management Procedure — the governance a production-affecting change sits under, and "
     "the Restricted Period", f"{POLICY}/change-management"),
    ("Records Management Policy — where completed engagement documentation is filed",
     f"{POLICY}/records-management"),
]

ASSESSOR_PROVIDES = ("Your assessor will provide the baseline lab-pack — the infrastructure-as-code "
                     "template that builds the current single-AZ environment — and, if your team's "
                     "integrated template is not usable, a reference improvement template so you "
                     "are not blocked by someone else's work. Ask your assessor for both.")

INSTRUCTIONS = [
    "This is an open-book assessment. You may use the YAT intranet, AWS documentation, and "
    "anything you have from class. What you may not use is another student.",
    "Work the tasks in order. Task 1 deploys the baseline; everything after it improves and proves "
    "that environment.",
    "Take each screenshot as you finish the task, not at the end. Recreating a screen after you "
    "have moved on is painful and sometimes impossible. A task you cannot evidence cannot be "
    "assessed as satisfactory.",
    "Tasks 5 to 8 ask you to demonstrate, not to assert. Make something happen and record what you "
    "observed. A test with no observation is not a test.",
    "Things will fail. Record what broke and what you did about it — there is a task for exactly "
    "that, and troubleshooting is part of what is assessed.",
]

REGION_NOTE = ("The scenario places Ledgerline in Sydney — [scenario: ap-southeast-2 | deploy: "
               "us-east-1]. Build in us-east-1 in the AWS Academy Learner Lab. Where a task refers "
               "to availability zones, read the first two zones of whichever region you are in.")

# ---------------------------------------------------------------- the tasks

TASKS = [
    dict(n=1, title="Deploy the baseline environment",
         prompt="Deploy the assessor-provided baseline template. This builds the current single-AZ "
                "Ledgerline environment — the state your AT1 analysis was written against. Confirm "
                "it came up before you change anything, because everything after this is measured "
                "against it.",
         uoc=["ICTCLD504 PE 4"],
         standard="the baseline is deployed using the infrastructure-as-code tooling and the "
                  "student confirms the environment is running before improving it. PE 4 (use cloud "
                  "management consoles, SDKs or command line tools) is evidenced from here onward; "
                  "this task establishes the before state that tasks 4 to 8 compare against.",
         given=1, blank_rows=4,
         table=(["Step", "What you did", "Result"],
                [["Deployed the baseline template", "", ""],
                 ["Tooling used", "console or CLI — name it", ""],
                 ["Confirmed the application responds", "", ""],
                 ["Recorded the before state", "what the environment looks like pre-improvement",
                  ""]]),
         evidence=["the baseline stack deployed, and the application responding"]),

    dict(n=2, title="Record your approved scope",
         prompt="Before you deploy anything else, write down what you are actually authorised to "
                "build. Copy the approved improvements from your AT1 sign-off. If something you "
                "proposed was not approved, it does not get deployed here — record it as out of "
                "scope so the difference is deliberate rather than forgotten.",
         uoc=["ICTCLD504 FS Self-management"],
         standard="the approved list matches the student's own AT1 sign-off record, and anything "
                  "proposed but not approved is listed as out of scope. This task exists so that "
                  "task 10's 'changes from the approved design' has a baseline to be measured "
                  "against.",
         given=1, blank_rows=6,
         table=(["Improvement", "Approved?", "In scope for this deployment"],
                [["", "", ""], ["", "", ""], ["", "", ""],
                 ["", "", ""], ["", "", ""], ["", "", ""]])),

    dict(n=3, title="Apply the approved improvement",
         prompt="Apply your approved improvement to the running baseline as an update — not by "
                "tearing it down and rebuilding. Updating a live environment is what YAT would "
                "actually experience, and it is where the interesting problems are. Record each "
                "attempt.",
         uoc=["ICTCLD504 PC 3.1", "ICTCLD504 PE 2"],
         standard="the approved architecture is deployed onto the running baseline through the "
                  "infrastructure-as-code service, and the student records what the update did to "
                  "existing resources. PC 3.1 is 'deploy approved architecture' — deploying "
                  "something other than what was approved in AT1, or rebuilding from scratch rather "
                  "than updating, has not met it.",
         given=1, blank_rows=5,
         table=(["Attempt", "What you applied", "What happened", "What you changed"],
                [["1", "", "", ""],
                 ["2", "", "", ""],
                 ["3", "", "", ""],
                 ["Final", "the approved improvement", "applied successfully", "—"],
                 ["What the update did to existing resources",
                  "which were modified, which were replaced, which were untouched", "", ""]]),
         evidence=["the update completing, and the resources it changed"]),

    dict(n=4, title="Monitor and measure against your metrics",
         prompt="Measure the improved environment against the performance metrics and business "
                "goals you set in AT1. For each metric, record what you measured, what the target "
                "was, and whether it is met. Where a metric cannot be measured yet, say what would "
                "be needed — that is a finding, not a failure.",
         uoc=["ICTCLD504 PC 3.2", "ICTCLD504 KE 10"],
         standard="the metrics measured are the student's own from AT1, each with an observed value "
                  "against its target. KE 10 (techniques, methods and industry standard metrics to "
                  "monitor performance) is evidenced by the student using real platform "
                  "measurements rather than impressions. A metric recorded as 'met' with no observed "
                  "value has not met PC 3.2.",
         given=1, blank_rows=6,
         table=(["Metric (from your AT1 design)", "Target", "What you measured", "Met?"],
                [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]),
         evidence=["your monitoring showing the measurements you recorded"]),

    dict(n=5, title="Test and demonstrate reliability",
         prompt="Demonstrate that the environment is more reliable than the baseline was. Make a "
                "failure happen — terminate an instance, or fail over whatever you improved — and "
                "record what the service did while it was happening. If your approved improvement "
                "did not touch reliability, test the reliability you have and say so.",
         uoc=["ICTCLD504 PC 3.3", "ICTCLD504 KE 7"],
         standard="a real failure is induced and the service behaviour is observed and recorded, "
                  "not predicted. KE 7 (testing and debugging techniques, including techniques to "
                  "avoid single point failures) is evidenced by the student testing the specific "
                  "single point of failure their AT1 analysis identified. A description of what "
                  "would happen has not demonstrated anything.",
         given=1, blank_rows=5,
         table=(["Test", "What you did", "What you expected", "What actually happened"],
                [["Instance failure", "terminated a running application instance", "", ""],
                 ["Service during the failure", "requested the application throughout", "", ""],
                 ["Recovery", "observed the group replacing the instance", "", ""],
                 ["Zone-level behaviour", "if your design spans zones, what the other zone did",
                  "", ""],
                 ["Database behaviour", "per your approved design", "", ""]]),
         evidence=["the failure you induced",
                   "the service continuing during it",
                   "the environment after recovery"]),

    dict(n=6, title="Test and demonstrate security",
         resources=[
             ("Security & Incident Response Policy — the obligations the environment is held to",
              f"{POLICY}/security-incident"),
         ],
         prompt="Demonstrate the security position of the deployed environment. Show the controls "
                "working rather than listing them — that the paths you intended to be closed are "
                "closed, and that anything you improved is actually in effect.",
         uoc=["ICTCLD504 PC 3.3"],
         standard="the student demonstrates at least one control by testing it — attempting a "
                  "connection that should be refused and showing it refused is the clearest form — "
                  "and confirms any security improvement from AT1 is in effect. Screenshots of "
                  "security group rules alone show configuration, not behaviour, and are a weaker "
                  "form of the same evidence.",
         given=1, blank_rows=5,
         table=(["Control", "How you tested it", "What you observed"],
                [["Database reachable only from the application tier",
                  "attempted a connection from outside it", ""],
                 ["No public ingress to the application tier", "", ""],
                 ["Administrative access without an open management port", "", ""],
                 ["Transport encryption, if you improved it", "", ""],
                 ["Storage encryption", "", ""]]),
         evidence=["a connection attempt being refused where it should be",
                   "the security improvement you deployed, in effect"]),

    dict(n=7, title="Test and demonstrate scalability",
         prompt="Demonstrate that the environment scales. Ledgerline's real scaling event is "
                "month-end close, so make the tier scale — generate load, or change the desired "
                "capacity — and record what happened and how long it took.",
         uoc=["ICTCLD504 PC 3.3"],
         standard="the student causes a scaling event and observes it, recording the trigger, the "
                  "response and the time taken. Either route is acceptable — generated load is the "
                  "more realistic, a capacity change is the more reliable in a lab. Asserting that "
                  "the Auto Scaling group will scale has not demonstrated scalability.",
         given=1, blank_rows=4,
         table=(["Test", "What you did", "What happened", "How long it took"],
                [["Scale out", "", "", ""],
                 ["Service during scale-out", "requested the application throughout", "", ""],
                 ["Scale in", "", "", ""],
                 ["Behaviour against the month-end profile",
                  "what this means for the close period", "", ""]]),
         evidence=["the scaling event, showing the group before and after"]),

    dict(n=8, title="Test and demonstrate cost optimisation",
         resources=[
             ("Accounting System Operational Costing — the cost basis you compared against in AT1",
              f"{ICT}/accounting-operational-costing-cloud"),
         ],
         prompt="Demonstrate the cost position of what you deployed. Show what the improvement "
                "actually costs to run against what you estimated in AT1, and show any cost measure "
                "you designed working — a scheduled scale-down, right-sizing, or a budget alert.",
         uoc=["ICTCLD504 PC 3.3"],
         standard="the student compares the deployed cost position against their AT1 estimate and "
                  "demonstrates at least one cost measure in effect. An honest 'this costs more than "
                  "I estimated, and here is why' is a satisfactory answer — PC 3.3 asks for "
                  "demonstration of cost optimisation, not for the estimate to have been right.",
         given=1, blank_rows=5,
         table=(["Item", "AT1 estimate", "What you deployed", "Observed position"],
                [["Additional compute", "", "", ""],
                 ["Additional networking", "", "", ""],
                 ["Database", "", "", ""],
                 ["Cost measure in effect", "e.g. scheduled scale-down or a budget alert", "", ""],
                 ["Net position against your cost goal", "", "", ""]]),
         evidence=["the cost measure you designed, working"]),

    dict(n=9, title="Apply short-term refinements",
         prompt="Your tests will have found something — a threshold set too tight, a missing alarm, "
                "a health check that is slower than it needs to be, capacity that is wrong. Apply "
                "the refinements your own test results point to, and record what drove each one. A "
                "refinement with no test result behind it is a change, not a refinement.",
         uoc=["ICTCLD504 PC 3.4", "ICTCLD504 FS Problem solving"],
         standard="at least one refinement is applied and each traces to a specific observation "
                  "from tasks 4 to 8. PC 3.4 says 'according to test results', so the chain from "
                  "observation to change must be visible. A student whose tests genuinely found "
                  "nothing must say what they checked and why they are satisfied — but that is rare "
                  "and should be probed.",
         given=1, blank_rows=5,
         table=(["What the test showed", "The refinement you applied", "What it changed"],
                [["", "", ""], ["", "", ""], ["", "", ""],
                 ["", "", ""], ["", "", ""]]),
         evidence=["a refinement applied, and its effect"]),

    dict(n=10, title="Document the as-deployed architecture and test results",
         prompt="Document what is actually deployed, and how it differs from what was approved. "
                "Write it for the YAT ICT person who inherits this environment and was not here. "
                "Include the test results — the as-deployed state without the evidence it works is "
                "half a handover. Highlight every change from the approved design, with the reason.",
         uoc=["ICTCLD504 PC 4.1", "ICTCLD504 PE 5", "ICTCLD504 FS Writing"],
         standard="the documentation describes the as-deployed environment (not the approved "
                  "design), records the test results, and explicitly highlights the differences "
                  "between the two with reasons — including the refinements from task 9. PC 4.1 "
                  "names all three: as-deployed, test results, and changes highlighted. PE 5 "
                  "requires the deployment and testing STEPS to be documented, so someone must be "
                  "able to repeat what the student did.",
         points=[
             "the as-deployed architecture, tier by tier, as it actually stands",
             "the deployment steps in enough detail that someone else could repeat them",
             "the test results from tasks 4 to 8, with what was observed",
             "every difference from the approved design, with the reason — including the task 9 "
             "refinements",
             "anything approved but not deployed, and why",
             "known limitations of the deployed result",
         ]),

    dict(n=11, title="Describe the long-term improvement strategy",
         prompt="You have deployed what was approved. Describe what YAT should do next and over the "
                "longer term, and what each thing would buy them. This is not a list of everything "
                "possible — it is what you would advise a client you have just spent a project "
                "with, in the order you would advise it.",
         uoc=["ICTCLD504 PC 4.2"],
         standard="the strategies are specific to Ledgerline's actual position after this "
                  "deployment, prioritised, and each carries a benefit. Sensible content: whatever "
                  "was proposed but not approved, recovery testing on a schedule, extending "
                  "infrastructure as code coverage, and the point at which the application itself "
                  "becomes the constraint. Generic cloud advice has not met PC 4.2, which asks for "
                  "strategies 'as applied to deployed resources'.",
         given=1, blank_rows=5,
         table=(["Strategy", "Why, and when", "The benefit to YAT"],
                [["", "", ""], ["", "", ""], ["", "", ""],
                 ["", "", ""], ["", "", ""]])),

    dict(n=12, title="Hand over and obtain final sign-off",
         prompt="Walk Sam Walker through what you deployed, what your tests showed, and what you "
                "are recommending next. Answer questions, respond to feedback, and obtain final "
                "sign-off. File your documentation per the Records Management Policy.",
         resources=[
             ("Records Management Policy — where completed engagement documentation is filed",
              f"{POLICY}/records-management"),
         ],
         uoc=["ICTCLD504 PC 4.3", "ICTCLD504 FS Oral communication"],
         standard="final sign-off is obtained from the required person and recorded with a "
                  "decision, a name and a date, and the documentation is filed per YAT's policy. "
                  "PC 4.3 is the terminal gate of the engagement — a student who demonstrated well "
                  "but never closed the loop has not met it.",
         given=1, blank_rows=5,
         table=(["Record", "Your entry"],
                [["What you handed over", "the as-deployed documentation and the test results"],
                 ["Where you filed it", "per the Records Management Policy"],
                 ["Feedback given, and your response", ""],
                 ["Decision", "Approved / Approved with conditions / Not approved"],
                 ["Signed by, and date", "Sam Walker, YAT ICT Manager"]])),

    dict(n=13, title="Remove what you deployed",
         prompt="Tear the environment down through the infrastructure-as-code tooling and confirm "
                "it is gone. Lab environments are not free and an environment left running is a "
                "cost YAT did not agree to.",
         uoc=["ICTCLD504 PE 4"],
         standard="the environment is removed through the tooling rather than by hand, and the "
                  "student confirms nothing is left behind. This also closes the loop on the cost "
                  "argument the whole cluster has been making.",
         given=1, blank_rows=3,
         table=(["What you removed", "How", "Confirmed gone"],
                [["The improved environment", "via the IaC service", ""],
                 ["The baseline stack", "via the IaC service", ""],
                 ["Anything left behind", "checked for orphaned resources", ""]])),
]

# ---------------------------------------------------------------- knowledge questions

QUESTIONS = [
    dict(n=1, title="How did you test this environment, and how do you avoid single points of "
                    "failure?",
         prompt="Describe the testing and debugging techniques you used, and explain the techniques "
                "available for avoiding single points of failure — pointing at where each one "
                "appears, or deliberately does not appear, in what you deployed.",
         uoc=["ICTCLD504 KE 7", "ICTCLD504 FS Problem solving"],
         standard="real techniques are described and tied to what the student actually did — "
                  "inducing a failure and observing, testing a control by attempting what should be "
                  "refused, reading logs and stack events, comparing against a baseline measurement. "
                  "The single-point-of-failure half must reference the student's own environment, "
                  "including any point they deliberately accepted.",
         points=[
             "induce the failure rather than reason about it — that is what task 5 was for",
             "test the negative case: attempt what should be refused and show it refused",
             "read the platform's own events and logs before changing anything",
             "measure against a recorded baseline, or the comparison means nothing",
             "avoiding single points of failure: redundancy across zones, managed failover, "
             "automated replacement — and where you accepted one, the reason",
         ]),

    dict(n=2, title="What would you monitor to know this environment is healthy?",
         prompt="Explain the techniques, methods and industry standard metrics used to monitor cloud "
                "resources, and say which of them you would leave in place for YAT to run this "
                "environment day to day.",
         uoc=["ICTCLD504 KE 10", "ICTCLD504 FS Self-management"],
         standard="the student distinguishes categories of measurement — availability, "
                  "performance/latency, utilisation, error rate, cost — names real platform metrics "
                  "for each, and selects a proportionate set for an internal business-hours system. "
                  "Proposing exhaustive monitoring for Ledgerline repeats the gold-plating IR-2 "
                  "warns against.",
         points=[
             "availability: healthy target count, per zone",
             "performance: response time and request rate at the load balancer",
             "utilisation: CPU and database connections, as the scaling signals",
             "errors: application and database error rates",
             "cost: a budget alert on the tagged resources",
             "what to leave out for a business-hours internal system, and why",
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


def render(doc, h1, h2, mode="student", tasks=None, questions=None, notes=False,
           evidence_dir=None):
    """Render AT3 into `doc`. mode = student | assessor."""
    TASKS_ = TASKS if tasks is None else tasks
    QUESTIONS_ = QUESTIONS if questions is None else questions

    h1("The deployment")
    for task in TASKS_:
        R.element(doc, h2, task, mode, notes=notes)
        if task.get("evidence"):
            R.p(doc, "Evidence", bold=True, size=9.5, after=3)
            images = R.evidence_images(evidence_dir, f"task-{task['n']:02d}")
            R.place_evidence(doc, task["evidence"], mode, images)

    h1("Knowledge questions")
    R.p(doc, "Answer these about your own deployment. Generic answers about cloud infrastructure "
             "will not pass.", italic=True, size=9.5, colour=R.GREY, after=10)
    for q in QUESTIONS_:
        R.element(doc, h2, q, mode, label="Question", notes=notes)
