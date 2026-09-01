#!/usr/bin/env python3
"""Build the S1-CL3 AT3 instruments (.docx) — assessor and student — from the Kangan template.

AT3 = Cloud Infrastructure Improvement: Implement. ICTCLD504 elements 3–4: deploy the approved
improvement onto the baseline, demonstrate it against the metrics set in AT1, refine it from the
test results, document the as-deployed state and obtain final sign-off.

NO DEPLOYMENT REPORT TEMPLATE. ICTCLD504's assessment conditions name no document format, so
`[ICTCLD504 PC 4.1]` and `[ICTCLD504 PE 5]` are met by tasks 10 and 11 of the worksheet.

Usage:  python scripts/s1_cl3/build_s1_cl3_at3_assessor.py [assessor|student] [output.docx]
"""
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parents[2] / "kangan-templates"
CLUSTER = Path(__file__).resolve().parents[2] / "S1-CL3-Cloud-Infrastructure-Improvement"

sys.path.insert(0, str(Path(__file__).resolve().parent))  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # noqa: E402
sys.path.insert(0, str(next(d / "scripts" for d in Path(__file__).resolve().parents
                            if (d / "scripts" / "helpers" / "__init__.py").exists())))  # noqa: E402
from helpers.workbook_instrument import (assemble, benchmark_sections,  # noqa: E402
                                         collect_elements, marking_guide, reverse_map_body,
                                         unevidenced_items)
import s1_cl3_at3_run_sheet as content  # noqa: E402

DETAILS = {
    "qualification": "ICT50220 Diploma of Information Technology",
    "units": ["ICTCLD504 Improve cloud infrastructure"],
    "task_title": "AT3 — Cloud Infrastructure Improvement: Implement",
    "task_number": "3 of 3",
}

TIME_ALLOWED = [
    "A 12-hour deployment and testing window across sessions, plus the handover session.",
    "Deployments fail and get fixed — that is the work, not lost time. Time is indicative.",
]

OVERVIEW = [
    "Students are assessed on deploying the approved Ledgerline improvement, demonstrating it "
    "against the metrics and business goals they set in AT1, refining it from their own test "
    "results, documenting the as-deployed environment and obtaining final sign-off. AT3 is the "
    "third and final assessment task in the S1-CL3 Cloud Infrastructure Improvement cluster.",
    "The assessment is one guided workbook of thirteen tasks and two knowledge questions, "
    "submitted as a single document. The student deploys the assessor-provided baseline, records "
    "the scope their AT1 sign-off actually approved, applies the improvement as an update to the "
    "running environment, measures against their own metrics, demonstrates reliability, security, "
    "scalability and cost optimisation one at a time, applies refinements traced to test results, "
    "documents the as-deployed result and a long-term strategy, obtains sign-off, and tears the "
    "environment down.",
    "EACH STUDENT DEPLOYS THEIR OWN APPROVED SCOPE. AT1 produced each student's own improvement "
    "design and its sign-off, so what is deployed here differs between students. Task 2 records "
    "that scope and is the reference for task 10's 'changes from the approved design'. A student "
    "who deploys something they were not approved to build has not met [ICTCLD504 PC 3.1].",
    "THE TESTS ARE THE ASSESSMENT. [ICTCLD504 PC 3.3] requires the student to test AND DEMONSTRATE "
    "all four concerns. Tasks 5–8 are one per concern and each asks for something to be made to "
    "happen and something observed. 'The design is reliable because it spans two zones' has "
    "demonstrated nothing; terminating an instance and showing the service continuing has.",
    "AN ASSESSOR REFERENCE TEMPLATE IS THE FALLBACK. Where a team's integrated template from AT2 "
    "is not usable, provide the reference improvement template so an individual's evidence here "
    "is not blocked by someone else's work.",
    "WHAT IS BEING MARKED. Each element carries two assessor-only lines: 'Evidences', naming the "
    "UoC items, and 'Satisfactory when', naming what has to be true for them to be met. Mark the "
    "second. Because each student's approved improvement differs, most standards are about "
    "whether the demonstration actually tests the thing that student designed.",
    "This is an open-book practical assessment. Students may use the YAT intranet, AWS "
    "documentation, course materials and external research (which must be cited). They may not "
    "use another student.",
    "Reasonable adjustment may include extending the deployment window, providing one-on-one "
    "verbal explanation of the baseline, allowing alternative evidence formats where assistive "
    "technology requires it, or splitting the work across more sittings.",
    "Teacher/assessor support level: the assessor may clarify what a task is asking and explain "
    "the baseline, but must not diagnose deployment failures for the student, design the tests, "
    "or decide the refinements.",
    "The assessment will not proceed if for any reason it is not safe to do so. You must advise "
    "the student of the reason for suspending the assessment, and what safety action should be "
    "taken. Advise the student of revised arrangements when it is safe to do so.",
    "There is a zero tolerance for plagiarism, cheating and collusion. Students will be expected "
    "to make a declaration that all work is their own prior to submission. Refer to the Training "
    "and Assessment Policy for further information.",
]

STUDENT_OVERVIEW = [
    OVERVIEW[0], OVERVIEW[1],
    "YOU DEPLOY WHAT WAS APPROVED. Your AT1 sign-off recorded which improvements YAT approved — "
    "that list is your scope here, not everything you proposed and not everything the team wrote.",
    "TASKS 5 TO 8 ASK YOU TO DEMONSTRATE, NOT ASSERT. Make something happen and record what you "
    "observed. A test with no observation is not a test.",
    OVERVIEW[6], OVERVIEW[9], OVERVIEW[10],
]

TASKS = [
    "The improvement design was approved and the team has encoded it as infrastructure as code. "
    "This is the deployment phase: the student stands the environment up, applies the approved "
    "improvement, proves it does what they said it would, and hands it over.",
    "Tasks 1–3 deploy the baseline, record the approved scope, and apply the improvement as an "
    "update to the running environment rather than a rebuild.",
    "Tasks 4–8 measure and demonstrate: the metrics and business goals set in AT1, then "
    "reliability (by inducing a real failure), security (by testing a control rather than listing "
    "it), scalability (by causing a scaling event), and cost optimisation (against the AT1 "
    "estimate, with a cost measure shown working).",
    "Tasks 9–13 close the engagement: refinements traced to specific test results, documentation "
    "of the as-deployed architecture and test results with every difference from the approved "
    "design highlighted, a prioritised long-term improvement strategy, handover and final "
    "sign-off, and teardown through the tooling.",
    "Lab environment: AWS Academy Learner Lab. The scenario places Ledgerline in Sydney — "
    "[scenario: ap-southeast-2 | deploy: us-east-1].",
    "MTS scope: cloud infrastructure only. The Ledgerline application and its financial data are "
    "out of scope, and no financial data may be lost.",
]

RESOURCES = [
    "Teacher/assessor supplied resources",
    "AWS Academy Learner Lab access — providing the cloud vendor service provider, the managed "
    "database service, console / CLI / SDK tooling, an SSH or RDP client, and internet and web "
    "browser access",
    "The baseline lab-pack — the infrastructure-as-code template that builds the current "
    "single-AZ Ledgerline environment. THE ASSESSOR MUST PROVIDE THIS at the start of task 1",
    "The assessor reference improvement template, as a fallback where a team's integrated "
    "template from AT2 is not usable",
    "Access to the YAT scenario site / intranet — the improvement requirements, the operational "
    "costing, the change management procedure and the records management policy",
    "A person to role-play Sam Walker, YAT ICT Manager, for the handover and final sign-off — "
    "normally the assessor",
    "The worked workbook later in this document — model answers, per-element UoC mapping, and the "
    "standard each element is marked against",
    "Student supplied resources",
    "Computer with web browser",
    "A screenshot tool",
]

STUDENT_RESOURCES = [
    "AWS Academy Learner Lab access",
    "The baseline lab-pack from your assessor — you deploy it as task 1",
    "Your team's integrated template from AT2, or the assessor's reference template",
    "Your own AT1 workbook — you need the approved scope, the goals and the metrics from it",
    "Access to the YAT scenario site / intranet",
    "Computer with web browser, and a screenshot tool",
]

CRITERIA = [
    "To receive a Satisfactory outcome for this assessment the student must:",
    "Achieve Satisfactory on every criterion in the Marking Guide below",
    "Submit the completed workbook (.docx) with every task and question answered and every "
    "evidence box populated",
    "Obtain final sign-off at task 12",
]

CONDITIONS = [
    "These are conditions the assessor verifies as present before marking begins. They are not "
    "student-performance criteria — they are the conditions under which the assessment can "
    "validly be conducted.",
    "C1 Lab environment is accessible to the student throughout the assessment — AWS Academy "
    "Learner Lab — providing cloud vendor service provider access, a cloud managed database "
    "service, console / CLI / SDK tooling, an SSH or RDP client, and internet and web browser "
    "access",
    "C2 The baseline lab-pack has been made available to the student before task 1",
    "C3 An integrated improvement template is available to the student — their team's, or the "
    "assessor's reference template",
    "C4 The YAT scenario site / intranet is accessible to the student throughout the assessment",
    "C5 A person is available to role-play Sam Walker, YAT ICT Manager, for the handover and "
    "final sign-off",
]

CRITERIA_MAP = [
    dict(code="I1", tasks=["1", "2"],
         text="Baseline deployed and approved scope recorded (tasks 1–2) — the student deploys "
              "the baseline with the infrastructure-as-code tooling and confirms it before "
              "changing anything, and records what their own AT1 sign-off actually approved, "
              "including anything proposed but not approved"),
    dict(code="I2", tasks=["3"],
         text="Approved architecture deployed (task 3) — the improvement is applied to the "
              "running baseline as an update rather than a rebuild, and the student records what "
              "the update did to existing resources"),
    dict(code="I3", tasks=["4"],
         text="Measured against the metrics (task 4) — the student's own AT1 metrics, each with "
              "an observed value against its target; a metric recorded as met with no observed "
              "value has not met the item"),
    dict(code="I4", tasks=["5", "6", "7", "8"],
         text="All four concerns tested and demonstrated (tasks 5–8) — a real failure induced and "
              "the service behaviour observed; a security control tested rather than listed; a "
              "scaling event caused and timed; and the cost position compared against the AT1 "
              "estimate with a cost measure shown working"),
    dict(code="I5", tasks=["9"],
         text="Short-term refinements applied (task 9) — at least one refinement, each traced to "
              "a specific observation from the tests, with the chain from observation to change "
              "visible"),
    dict(code="I6", tasks=["10"],
         text="As-deployed architecture and test results documented (task 10) — the environment "
              "as it actually stands, the deployment and testing steps in enough detail to "
              "repeat, the test results, and every difference from the approved design "
              "highlighted with its reason"),
    dict(code="I7", tasks=["11"],
         text="Long-term improvement strategy described (task 11) — prioritised, specific to "
              "Ledgerline's position after this deployment, each with a benefit"),
    dict(code="I8", tasks=["12"],
         text="Handover and final sign-off (task 12) — the documentation filed per YAT's Records "
              "Management Policy and final sign-off obtained, recorded with a decision, a name "
              "and a date"),
    dict(code="I9", tasks=["13"],
         text="Environment removed (task 13) — torn down through the infrastructure-as-code "
              "tooling and confirmed gone"),
    dict(code="I10", tasks=["Q1", "Q2"],
         text="Knowledge (questions 1–2) — the testing and debugging techniques actually used and "
              "the techniques for avoiding single points of failure in their own environment, and "
              "the metrics they would leave in place for YAT to run it day to day"),
]

AC_CONDITIONS = {
    "ICTCLD504 AC 1": "C1", "ICTCLD504 AC 2": "C1", "ICTCLD504 AC 3": "C1",
    "ICTCLD504 AC 4": "C1", "ICTCLD504 AC 5": "C4", "ICTCLD504 AC 6": "C1",
    "ICTCLD504 AC 7": "C1",
}

EXPECTED = (
    [f"ICTCLD504 PC {n}" for n in "3.1 3.2 3.3 3.4 4.1 4.2 4.3".split()]
    + [f"ICTCLD504 PE {n}" for n in "2 4 5".split()]
    + [f"ICTCLD504 KE {n}" for n in "7 10".split()]
    + [f"ICTCLD504 FS {s}" for s in ["Problem solving", "Self-management", "Writing"]]
)


def _elements():
    return collect_elements(content.TASKS, (content.QUESTIONS, "Q"))


# The mapping engine reads this: the same per-criterion tag lists the marking guide
# uses, inverted per unit to produce the Assessment Mapping documents.
BENCHMARK = benchmark_sections(CRITERIA_MAP, _elements(), "AT3 — Cloud Infrastructure Improvement: Implement")


def build(path, mode="assessor"):
    elements = _elements()
    gaps = unevidenced_items(CRITERIA_MAP, elements, None, EXPECTED)
    if gaps:
        raise SystemExit("No criterion evidences: " + ", ".join(gaps))

    spec = dict(details=DETAILS, overview=OVERVIEW, student_overview=STUDENT_OVERVIEW,
                tasks=TASKS, time_allowed=TIME_ALLOWED, resources=RESOURCES,
                student_resources=STUDENT_RESOURCES, criteria=CRITERIA, conditions=CONDITIONS,
                criteria_map=CRITERIA_MAP,
                marking_rows=marking_guide(CRITERIA_MAP, elements))

    def render_body(doc, mode):
        def h1(t):
            return doc.add_paragraph(t, style="Heading 1")

        def h2(t):
            return content.R.heading2(doc, t)

        content.render_front_matter(doc, h1)
        content.render(doc, h1, h2, mode=mode)

    tmpl = TEMPLATES / (f"Project Assessment - "
                        f"{'Assessor' if mode == 'assessor' else 'Student'}.docx")
    benchmark = reverse_map_body(
        CRITERIA_MAP, elements, CLUSTER / "consolidated_uoc.md",
        [("ICTCLD504", "ICTCLD504 — Improve cloud infrastructure (AT3-evidenced items; "
                       "elements 1–2 are evidenced in AT1)")], AC_CONDITIONS)
    doc = assemble(str(tmpl), spec, mode, render_body, benchmark)

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    print(f"Wrote {path}  ({mode})")


if __name__ == "__main__":
    args = list(sys.argv[1:])
    mode = args.pop(0) if args and args[0] in ("assessor", "student") else "assessor"
    name = f"AT3-Implement-{'Assessor' if mode == 'assessor' else 'Student'}.docx"
    build(args[0] if args else str(CLUSTER / "assessments" / "AT3" / name), mode)
