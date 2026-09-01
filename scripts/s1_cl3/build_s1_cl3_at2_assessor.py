#!/usr/bin/env python3
"""Build the S1-CL3 AT2 instruments (.docx) — assessor and student — from the Kangan template.

AT2 = Team Implementation. BSBXTW401 in full: each student is assessed individually on how they
work within, and lead, the team that encodes the approved improvement as infrastructure as code.

THE ONLY GROUP ASSESSMENT IN S1. The work is done by a team; the assessment is of the individual.
Every BSBXTW401 criterion describes what ONE PERSON does in relation to the team, so each student
completes their own copy of the workbook — including where they are recording something the team
agreed together.

WHAT IS NOT IN THE WORKBOOK. The CloudFormation the team writes is submitted as itself. Task 7
records where it lives and what the student contributed; the technical quality is not marked
here, because BSBXTW401 assesses the teamwork and the write is only its vehicle.

Usage:  python scripts/s1_cl3/build_s1_cl3_at2_assessor.py [assessor|student] [output.docx]
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
import s1_cl3_at2_run_sheet as content  # noqa: E402

DETAILS = {
    "qualification": "ICT50220 Diploma of Information Technology",
    "units": ["BSBXTW401 Lead and facilitate a team"],
    "task_title": "AT2 — Team Implementation",
    "task_number": "2 of 3",
}

TIME_ALLOWED = [
    "This assessment runs across the whole project rather than in one sitting.",
    "The planning meeting is early; the reflections are written as things happen; the observed "
    "meeting is arranged with the assessor; the review is completed at the end.",
]

OVERVIEW = [
    "Students are assessed individually, within a team, on leading and facilitating the team that "
    "implements the approved Ledgerline improvement as infrastructure as code. AT2 is the second "
    "of three assessment tasks in the S1-CL3 Cloud Infrastructure Improvement cluster and the "
    "only group assessment in the semester.",
    "The team is four members, each owning one cloud component — network, compute, database or "
    "storage — and together they produce one integrated, deployable template. Each student "
    "completes their own copy of the workbook: the team's plan, their own allocated work, one "
    "team meeting they lead with the assessor observing, written reflections on the conflict, "
    "coaching and issue-resolution they were personally involved in, and a review of the team's "
    "performance against the plan.",
    "THE WORK IS THE TEAM'S; THE ASSESSMENT IS THE INDIVIDUAL'S. Every criterion below describes "
    "what one person did. Four students will submit four different workbooks recording the same "
    "team plan — that is expected. Four identical workbooks are not, and suggest one person "
    "talked while three wrote it down.",
    "THE CLOUDFORMATION IS NOT MARKED HERE. BSBXTW401 assesses teamwork and leadership; the "
    "technical write is its vehicle. Task 7 records where the student's contribution lives so it "
    "can be seen; its quality is ICTCLD504's business, in AT1 and AT3.",
    "THE OBSERVED MEETING IS NOT THE ONLY EVIDENCE, AND MUST NOT BE TREATED AS IT. BSBXTW401 does "
    "not tie coaching, issue resolution or conflict management to a meeting, and its assessment "
    "conditions require only a safe working or simulated environment. A well-run twenty-minute "
    "stand-up where nothing goes wrong gives a student nowhere to demonstrate [BSBXTW401 PC 3.4] "
    "or [BSBXTW401 PE 5]. Those criteria are carried by the written reflections in tasks 11–13; "
    "the observation confirms the student can hold a room. Do not fail a student for a quiet "
    "meeting.",
    "WHAT IS BEING MARKED. Each element carries two assessor-only lines: 'Evidences', naming the "
    "UoC items, and 'Satisfactory when', naming what has to be true for them to be met. Mark the "
    "second.",
    "This is an open-book assessment. Students may use the YAT intranet, course materials and "
    "external research (which must be cited). Collaboration within the team is the point; "
    "collaboration on the individual reflections is not.",
    "Reasonable adjustment may include scheduling the observed meeting at a time that suits the "
    "student, allowing the reflections to be given verbally and transcribed, or adjusting the "
    "team composition where a student's circumstances require it.",
    "Teacher/assessor support level: the assessor may clarify what a task is asking and may "
    "intervene where a team dynamic becomes genuinely harmful, but must not run the team's "
    "meetings, allocate its work, or resolve its conflicts for it.",
    "The assessment will not proceed if for any reason it is not safe to do so. You must advise "
    "the student of the reason for suspending the assessment, and what safety action should be "
    "taken. Advise the student of revised arrangements when it is safe to do so.",
    "There is a zero tolerance for plagiarism, cheating and collusion. Students will be expected "
    "to make a declaration that all work is their own prior to submission. Refer to the Training "
    "and Assessment Policy for further information.",
]

STUDENT_OVERVIEW = [
    OVERVIEW[0], OVERVIEW[1],
    "THIS WORKBOOK IS YOURS. Everyone in your team has one and each of you fills in your own, "
    "including where you are recording something the team agreed together. You are assessed as an "
    "individual on how you work within the team.",
    "WHAT IS NOT MARKED HERE. The quality of the CloudFormation. This assessment is about how you "
    "plan, coordinate, support and review the team — the code is what the team works on together.",
    OVERVIEW[6], OVERVIEW[9], OVERVIEW[10],
]

TASKS = [
    "YAT College has approved the improvement design for the Ledgerline cloud infrastructure. The "
    "MTS improvement team implements it: four members, one cloud component each, one integrated "
    "deployable template.",
    "Part A — The planning meeting. Six tasks worked through with the team in the room, as an "
    "agenda: agree the common objectives, responsibilities and required outcomes; set each "
    "member's expected outcomes, measurable goals and agreed behaviours against YAT's code of "
    "conduct; agree accountability strategies; plan for contingencies including unplanned "
    "absence and re-allocation; allocate the four components with real instruction and a stated "
    "basis; and identify who outside the team the work depends on.",
    "Part B — The build. Two tasks recording where the student's own contribution lives and their "
    "part in integrating the four components, including what did not fit first time.",
    "Part C — Leading a meeting. The student leads one team meeting with the assessor observing, "
    "records it, and has the assessor complete the observation table at the end.",
    "Part D — What happened, and what you did. Three written reflections: a conflict or challenge "
    "the student dealt with, a time they coached or helped a team member, and an issue the team "
    "hit and their part in resolving it.",
    "Part E — Review and reflection. Measure each member including themselves against the plan, "
    "record the feedback given and when, identify development opportunities and what was actually "
    "done about them, and reflect on their own leadership.",
    "Three knowledge questions cover the organisational and legislative requirements that applied, "
    "the facilitation, coaching and communication techniques used, and conflict resolution.",
]

RESOURCES = [
    "Teacher/assessor supplied resources",
    "A team of four students per improvement team, with one cloud component allocated to each",
    "The approved improvement design and the baseline, from AT1",
    "Access to the YAT scenario site / intranet — supplying the improvement requirements, the "
    "acceptable use and work health and safety policies, and the change management procedure",
    "Assessor availability to observe one meeting led by each student, scheduled across the "
    "project rather than in one block",
    "A safe working or simulated environment in which the team can meet and work",
    "The worked workbook later in this document — model answers, per-element UoC mapping, and the "
    "standard each element is marked against",
    "Student supplied resources",
    "Computer with web browser",
    "Word-processing software (e.g. Microsoft Word or equivalent)",
    "A code editor, and wherever the team agrees to keep its work",
]

STUDENT_RESOURCES = [
    "Your team of four, with one cloud component each",
    "The approved improvement design and the baseline, from AT1",
    "Access to the YAT scenario site / intranet — every document you need is linked from the task "
    "it belongs to",
    "Your assessor, who will observe one meeting that you lead — arrange it with them early",
    "Computer with web browser, word-processing software, a code editor, and wherever your team "
    "agrees to keep its work",
]

CRITERIA = [
    "To receive a Satisfactory outcome for this assessment the student must:",
    "Achieve Satisfactory on every criterion in the Marking Guide below",
    "Submit their own completed workbook with every task and reflection answered",
    "Lead one team meeting with the assessor observing, and have the observation record signed",
    "Provide a link or reference to their own contribution to the team's build",
]

CONDITIONS = [
    "These are conditions the assessor verifies as present before marking begins. They are not "
    "student-performance criteria — they are the conditions under which the assessment can "
    "validly be conducted.",
    "C1 A safe working or simulated environment is provided in which the team can meet and work",
    "[BSBXTW401 AC 1]",
    "C2 The student is a member of a team of four, with one cloud component allocated to them",
    "C3 The approved improvement design and the baseline environment are available to the team",
    "C4 The assessor has observed one meeting led by this student and completed the observation "
    "record at task 10",
]

CRITERIA_MAP = [
    dict(code="T1", tasks=["1", "2", "3", "4"],
         text="The team plan (tasks 1–4) — the student contributes to and records the team's "
              "objectives, responsibilities and required outcomes; per-member expectations, "
              "measurable goals and agreed behaviours tied to YAT's policies and code of conduct; "
              "concrete accountability strategies; and contingency plans covering the people-side "
              "risks, not only the technical ones"),
    dict(code="T2", tasks=["5", "6"],
         text="Allocation and collaboration (tasks 5–6) — each component allocated to a named "
              "member with instruction specific enough to start from and a stated basis "
              "(expertise or development potential), and genuine collaboration opportunities "
              "identified beyond the four members"),
    dict(code="T3", tasks=["7", "8"],
         text="The student's own work and the integration (tasks 7–8) — the student's "
              "contribution is identifiable and reachable, and they can name an issue integration "
              "surfaced and their part in the team resolving it"),
    dict(code="T4", tasks=["9", "10"],
         text="Leading a team meeting (tasks 9–10, observed) — the student chairs a real working "
              "meeting of their own team: communicates the objectives and purpose, allocates or "
              "confirms tasks with instruction, and draws the whole team into the conversation "
              "rather than the loudest two"),
    dict(code="T5", tasks=["11"],
         text="Conflict or challenge managed (task 11) — a genuine challenge with what the "
              "student actually did and how it turned out, connected to the team's agreed "
              "behaviours or YAT's code of conduct"),
    dict(code="T6", tasks=["12"],
         text="Coaching and support (task 12) — a real instance with a named need, a specific "
              "action and an outcome, showing the student adapted to what the person needed "
              "rather than doing their work for them"),
    dict(code="T7", tasks=["13"],
         text="Team issue resolved (task 13) — a real task-related issue, how it surfaced, and "
              "the student's own contribution to the TEAM resolving it"),
    dict(code="T8", tasks=["14"],
         text="Performance measured (task 14) — every member including the student measured "
              "against the expectations agreed in task 2, with evidence rather than impression, "
              "and the source of that assessment stated"),
    dict(code="T9", tasks=["15"],
         text="Feedback given (task 15) — recorded per member with what was said and roughly "
              "when, constructive and specific; feedback delivered only at the end partially "
              "meets the item at best"),
    dict(code="T10", tasks=["16"],
         text="Development opportunities identified and acted on (task 16) — needs identified for "
              "individuals and the team, each with an action that was actually taken or started "
              "during the project"),
    dict(code="T11", tasks=["17"],
         text="Reflection on their own leadership (task 17) — specific to what the student did, "
              "identifying something done well and something done badly, and showing awareness of "
              "the professional behaviours a leader models"),
    dict(code="T12", tasks=["Q1", "Q2", "Q3"],
         text="Knowledge (questions 1–3) — the organisational and legislative requirements that "
              "applied and where they shaped the team's work; the facilitation, coaching and "
              "communication techniques used, including cross-cultural communication and "
              "communicating with people with special needs or disabilities; and conflict "
              "resolution strategies with the challenges a team should expect"),
]

AC_CONDITIONS = {"BSBXTW401 AC 1": "C1"}

EXPECTED = (
    [f"BSBXTW401 PC {n}" for n in
     "1.1 1.2 1.3 1.4 2.1 2.2 2.3 2.4 3.1 3.2 3.3 3.4 4.1 4.2 4.3 4.4".split()]
    + [f"BSBXTW401 PE {n}" for n in "1 2 3 4 5".split()]
    + [f"BSBXTW401 KE {n}" for n in range(1, 11)]
    + [f"BSBXTW401 FS {s}" for s in
       ["Get the work done", "Interact with others", "Navigate the world of work"]]
)


def _elements():
    return collect_elements(content.PLAN, content.WORK, content.MEETING, content.RUNNING,
                            content.REVIEW, (content.QUESTIONS, "Q"))


# The mapping engine reads this: the same per-criterion tag lists the marking guide
# uses, inverted per unit to produce the Assessment Mapping documents.
BENCHMARK = benchmark_sections(CRITERIA_MAP, _elements(), "AT2 — Team Implementation")


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
        [("BSBXTW401", "BSBXTW401 — Lead and facilitate a team")], AC_CONDITIONS)
    doc = assemble(str(tmpl), spec, mode, render_body, benchmark)

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    print(f"Wrote {path}  ({mode})")


if __name__ == "__main__":
    args = list(sys.argv[1:])
    mode = args.pop(0) if args and args[0] in ("assessor", "student") else "assessor"
    name = f"AT2-Team-Implementation-{'Assessor' if mode == 'assessor' else 'Student'}.docx"
    build(args[0] if args else str(CLUSTER / "assessments" / "AT2" / name), mode)
