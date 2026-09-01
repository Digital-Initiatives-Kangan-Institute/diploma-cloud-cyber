#!/usr/bin/env python3
"""Build the S1-CL3 AT1 instruments (.docx) — assessor and student — from the Kangan template.

AT1 = Cloud Infrastructure Improvement: Design. ICTCLD504 elements 1–2: analyse the Ledgerline
cloud baseline, design a proportionate improvement, present it and obtain sign-off to proceed.

ONE DEFINITION, TWO INSTRUMENTS — content in s1_cl3_at1_run_sheet.py, rendered worked for the assessor
and blank for the student. The marking guide's traceability lines and the reverse map are
derived from the workbook's own tags (helpers.workbook_instrument), and the Kangan wiring is the
shared `assemble`.

NO SOLUTION DESIGN TEMPLATE. ICTCLD504's assessment conditions (AC 1–8) are environment and
input conditions and name no document format, so `[ICTCLD504 PC 2.4]` "document and present" is
met by the worksheet (documenting) plus Part B (presenting).

Usage:  python scripts/s1_cl3/build_s1_cl3_at1_assessor.py [assessor|student] [output.docx]
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
import s1_cl3_at1_run_sheet as content  # noqa: E402

DETAILS = {
    "qualification": "ICT50220 Diploma of Information Technology",
    "units": ["ICTCLD504 Improve cloud infrastructure"],
    "task_title": "AT1 — Cloud Infrastructure Improvement: Design",
    "task_number": "1 of 3",
}

TIME_ALLOWED = [
    "Part A — Analysis and design: 6 hours",
    "Part B — Presentation and approval: a 20-minute session, scheduled with the assessor",
    "Time is indicative. A student who needs longer continues in the next session rather than "
    "submitting incomplete work.",
]

OVERVIEW = [
    "Students are assessed on analysing the cloud infrastructure of YAT's Ledgerline accounting "
    "system, designing a proportionate improvement to it, and obtaining sign-off to proceed to "
    "deployment. AT1 is the first of three assessment tasks in the S1-CL3 Cloud Infrastructure "
    "Improvement cluster.",
    "The assessment is one guided workbook of fifteen design tasks, three approval tasks and "
    "three knowledge questions, submitted as a single document. Part A leads the student through "
    "reviewing the current architecture, evaluating its business impact, assessing compliance "
    "against the Indian regulatory requirements, identifying architectural options, setting "
    "measurable business goals and metrics, designing the improvement across the four concerns, "
    "justifying each on cost versus benefit, and drawing the result. Part B is a live session in "
    "which the student presents the proposal and obtains sign-off.",
    "THE IMPROVEMENT IS OPEN — THIS IS THE POINT OF THE CLUSTER. There is no target architecture "
    "and no planted set of faults. The Improvement Requirements are outcomes, and IR-2 asks for "
    "sound engineering proportionate to an internal, business-hours finance system, explicitly "
    "not gold-plating. A student who proposes every improvement available has not done better "
    "than one who proposes four and justifies each — they have done worse. Mark the reasoning, "
    "not the ambition.",
    "WHAT IS BEING MARKED. Every table and worked answer contains values we chose so there is a "
    "concrete task. Each element carries two assessor-only lines: 'Evidences', naming the UoC "
    "items, and 'Satisfactory when', naming what has to be true for them to be met. Mark the "
    "second. Because the improvement is open, most standards here are about whether the student's "
    "reasoning holds, not whether they reached our answer — converting the database to a standby "
    "is defensible on a recovery goal, and so is leaving it single-instance with a tested restore "
    "if the cost is argued.",
    "This is an open-book assessment. Students may use the YAT intranet, AWS documentation, "
    "course materials and external research (which must be cited). They may not use another "
    "student.",
    "Reasonable adjustment may include extending the design time, providing one-on-one verbal "
    "explanation of the supplied environment, allowing the Part B session by video conference, or "
    "splitting the work across more sittings.",
    "Teacher/assessor support level: the assessor may clarify what a task is asking and explain "
    "the supplied records, but must not identify improvements for the student, set their goals or "
    "metrics, or confirm whether a design decision is correct.",
    "The assessment will not proceed if for any reason it is not safe to do so. You must advise "
    "the student of the reason for suspending the assessment, and what safety action should be "
    "taken. Advise the student of revised arrangements when it is safe to do so.",
    "There is a zero tolerance for plagiarism, cheating and collusion. Students will be expected "
    "to make a declaration that all work is their own prior to submission. Refer to the Training "
    "and Assessment Policy for further information.",
]

STUDENT_OVERVIEW = [
    OVERVIEW[0], OVERVIEW[1],
    "THE IMPROVEMENT IS OPEN. There is no right answer waiting to be found. The Improvement "
    "Requirements are outcomes, not solutions, and IR-2 asks for improvements proportionate to an "
    "internal, business-hours finance system. Proposing everything available is not a better "
    "answer than proposing four you can justify — it is a worse one.",
    "WHAT YOU SUBMIT. The completed workbook, with every task and question answered and the "
    "approval records from Part B filled in.",
    OVERVIEW[4], OVERVIEW[7], OVERVIEW[8],
]

TASKS = [
    "YAT College's offshore partnership in India has put a spotlight on the systems supporting "
    "it. Ledgerline — the finance and office-administration system — was migrated to AWS in an "
    "earlier engagement and has run there since, but it was migrated as-is: the whole workload "
    "sits in one availability zone and nothing has been revisited since cutover.",
    "MTS is engaged to confirm Ledgerline is stable, reliable, fit for purpose and compliant with "
    "the Indian regulatory requirements that now apply, and to improve it where it is not. What "
    "that improvement consists of is the student's analysis to make.",
    "Part A — Analysis and design. Fifteen tasks: review the architecture and the decisions it "
    "represents, evaluate the business impact of those decisions, assess compliance against the "
    "Indian Regulatory Requirements, identify the design patterns and options available, assess "
    "their benefits against how this business actually runs, set measurable business goals across "
    "security, reliability, performance and cost, confirm the direction including what is NOT "
    "being proposed, confirm the metrics, design the improvements to compute, storage, database, "
    "network, security, reliability, scalability, cost and monitoring, justify each on cost "
    "versus benefit, draw the result, and write the justification.",
    "Part B — Review and approval. The student presents the proposal to the role-played YAT ICT "
    "Manager, answers questions, and obtains sign-off recording exactly which improvements are "
    "approved — that approved list is AT3's scope. The first task of Part B is the student's own "
    "preparation and is not marked.",
    "MTS scope: cloud infrastructure only. The Ledgerline application and its financial data are "
    "out of scope (IR-4), as is legal interpretation of the India obligations — the student "
    "designs to the compliance area's determination.",
]

RESOURCES = [
    "Teacher/assessor supplied resources",
    "Access to the YAT scenario site / intranet — supplying the Improvement Requirements, the "
    "Indian Regulatory Requirements, the Accounting System Infrastructure Specifications, "
    "Application Specification and Operational Costing, the baseline design, the network diagram, "
    "the reference architectures and the YAT policies. Those documents are linked from the "
    "Instructions to Student below",
    "A person to role-play Sam Walker, YAT ICT Manager, for the Part B presentation and sign-off "
    "— normally the assessor",
    "The worked workbook later in this document — model answers, per-element UoC mapping, and the "
    "standard each element is marked against",
    "Student supplied resources",
    "Computer with web browser",
    "Word-processing software (e.g. Microsoft Word or equivalent)",
]

STUDENT_RESOURCES = [
    "Access to the YAT scenario site / intranet — every document you need is linked from the task "
    "it belongs to",
    "Your assessor will role-play Sam Walker, YAT ICT Manager, for the Part B session",
    "Computer with web browser",
    "Word-processing software (e.g. Microsoft Word or equivalent)",
]

CRITERIA = [
    "To receive a Satisfactory outcome for this assessment the student must:",
    "Achieve Satisfactory on every criterion in the Marking Guide below",
    "Submit the completed workbook (.docx) with every task and question answered",
    "Attend the Part B session and obtain sign-off",
]

CONDITIONS = [
    "These are conditions the assessor verifies as present before marking begins. They are not "
    "student-performance criteria — they are the conditions under which the assessment can "
    "validly be conducted.",
    "C1 The YAT scenario site / intranet is accessible to the student throughout the assessment — "
    "supplying the improvement requirements, the regulatory determination, the infrastructure, "
    "application and costing records, the baseline design and the organisational policies",
    "C2 Cloud platform reference access is available for the student to research services and "
    "their capabilities — a cloud vendor service provider, its managed database documentation, an "
    "internet connection and a web browser. AT1 is analysis and design: nothing is deployed, so "
    "no lab session is required",
    "C3 A person is available to role-play Sam Walker, YAT ICT Manager, for the Part B "
    "presentation and sign-off",
]

CRITERIA_MAP = [
    dict(code="D1", tasks=["1", "2"],
         text="Architecture reviewed and its business impact evaluated (tasks 1–2) — the student "
              "identifies every tier from the supplied records and the deliberate decision each "
              "represents, then states the business consequence of each in terms proportionate to "
              "an internal, business-hours system rather than as generic risk"),
    dict(code="D2", tasks=["3"],
         text="Compliance assessed (task 3) — the student assesses the infrastructure against the "
              "supplied regulatory determination, identifies the gaps that actually apply, and "
              "proposes infrastructure changes rather than advising on the law"),
    dict(code="D3", tasks=["4", "5"],
         text="Options identified and assessed (tasks 4–5) — a genuine range of design patterns "
              "with what each addresses, then assessed against how this business actually runs, "
              "including that an idle-overnight system changes the value of always-on redundancy"),
    dict(code="D4", tasks=["6", "7"],
         text="Business goals set and direction confirmed (tasks 6–7) — a measurable goal in each "
              "of the four areas, defensible for this system, and a committed proposal set with "
              "its exclusions stated and justified"),
    dict(code="D5", tasks=["8"],
         text="Performance metrics confirmed (task 8) — each metric names a real measurable "
              "source and a target value, and pairs with a goal, so AT3 can demonstrate against "
              "them"),
    dict(code="D6", tasks=["9", "10", "11", "12"],
         text="The improvement designed (tasks 9–12) — compute, storage, database and network "
              "addressed with decisions and reasons including explicit no-change decisions; "
              "security designed in layers, recognising what is already strong; reliability and "
              "scalability designed with the failure behaviour stated; and cost and monitoring "
              "designed together"),
    dict(code="D7", tasks=["13"],
         text="Cost-benefit justification (task 13) — every proposed improvement carries a cost "
              "direction and a benefit, and the total is set against the cost goal"),
    dict(code="D8", tasks=["14"],
         text="Improved architecture drawn (task 14) — a diagram consistent with the design "
              "tables, with both zones and the changed components identifiable"),
    dict(code="D9", tasks=["15"],
         text="Design documented and justified (task 15) — a written justification tying each "
              "improvement to a business goal, naming rejected alternatives, and arguing the "
              "database decision explicitly"),
    dict(code="D10", tasks=["17"],
         text="Proposal presented for review (task 17, observed) — the student presents their own "
              "proposal to the required person and can explain and defend the reasoning behind it "
              "in appropriate industry language"),
    dict(code="D11", tasks=["18"],
         text="Sign-off to proceed obtained (task 18) — sign-off recorded with a decision, a name "
              "and a date, and the approved scope unambiguous, since it is AT3's input"),
    dict(code="D12", tasks=["Q1", "Q2", "Q3"],
         text="Knowledge (questions 1–3) — industry standards and standard products in the "
              "student's own design, where object storage is and is not the right answer, and "
              "what cloud adoption changed for Ledgerline"),
]

AC_CONDITIONS = {
    "ICTCLD504 AC 1": "C2", "ICTCLD504 AC 2": "C2", "ICTCLD504 AC 3": "C2",
    "ICTCLD504 AC 4": "C2", "ICTCLD504 AC 6": "C2", "ICTCLD504 AC 7": "C2",
}

EXPECTED = (
    [f"ICTCLD504 PC {n}" for n in "1.1 1.2 1.3 1.4 1.5 1.6 2.1 2.2 2.3 2.4 2.5".split()]
    + ["ICTCLD504 PE 1", "ICTCLD504 PE 3"]
    + [f"ICTCLD504 KE {n}" for n in "1 2 3 4 5 6 8 9".split()]
    + [f"ICTCLD504 FS {s}" for s in ["Oral communication", "Reading", "Writing"]]
    + ["ICTCLD504 AC 5"]
)


def _elements():
    return collect_elements(content.DESIGN, content.APPROVAL, (content.QUESTIONS, "Q"))


# The mapping engine reads this: the same per-criterion tag lists the marking guide
# uses, inverted per unit to produce the Assessment Mapping documents.
BENCHMARK = benchmark_sections(CRITERIA_MAP, _elements(), "AT1 — Cloud Infrastructure Improvement: Design")


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
        [("ICTCLD504", "ICTCLD504 — Improve cloud infrastructure (AT1-evidenced items; "
                       "elements 3–4 are evidenced in AT3)")], AC_CONDITIONS)
    doc = assemble(str(tmpl), spec, mode, render_body, benchmark)

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    print(f"Wrote {path}  ({mode})")


if __name__ == "__main__":
    args = list(sys.argv[1:])
    mode = args.pop(0) if args and args[0] in ("assessor", "student") else "assessor"
    name = f"AT1-Design-{'Assessor' if mode == 'assessor' else 'Student'}.docx"
    build(args[0] if args else str(CLUSTER / "assessments" / "AT1" / name), mode)
