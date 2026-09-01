#!/usr/bin/env python3
"""The S1-CL3 AT2 team-implementation workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), through the shared workbook engine in
the umbrella (`helpers/run_sheet.py`).

THE ONE GROUP ASSESSMENT IN S1, AND HOW IT STILL WORKS AS A WORKSHEET. The work is done by a
team; the assessment is of each individual. Every BSBXTW401 performance criterion describes what
ONE PERSON does in relation to the team — allocates, instructs, facilitates, coaches, measures,
gives feedback, manages conflict. So each student gets their own copy of this worksheet and
fills it in from their own seat. The team produces one plan and one integrated template; each
student records that plan in their own sheet and evidences their own leadership around it.

THE WORKSHEET IS THE MEETING AGENDA. Part A's tasks are written to be worked through with the
team in the room — "agree this with your team, then record it below". Four students sitting
around a table with the same worksheet have a planning agenda, which is a better artefact than a
blank team-plan template and produces the same evidence.

WHAT IS NOT IN THE WORKSHEET. The CloudFormation the team writes is real work with a real
output, and it is submitted as itself — a repository, the template files, whatever the team
actually produced. Task 7 captures where it is and what the student's own contribution was; it
does not try to reproduce the work inside a worksheet. The technical write is BSBXTW401's
vehicle, not what BSBXTW401 assesses.

THE OBSERVED MEETING, AND WHY THE RECORDS EXIST TOO. `[BSBXTW401 PC 3.4]` and `[BSBXTW401 PE 5]`
need a challenge or conflict to have actually happened, and `[BSBXTW401 PC 3.1]` needs someone to
have needed coaching. A well-run twenty-minute stand-up where nothing goes wrong gives a student
nowhere to demonstrate any of them. So this workbook routes that evidence twice: the student
keeps running records across the project (tasks 10 to 12), and the observed meeting confirms what
those records claim. A student is then evidenced on what they did over weeks, not on whether
something usefully went wrong while the assessor was watching.

THE ASSESSOR'S SIGNATURE. Task 9 carries a signature block the assessor completes in the room.
The worksheet records that the observation happened; the assessor's own judgement of it is theirs
to record wherever the institution requires. The student's job is to arrange it and capture it.

THE MARKING MODEL. Values here are ours, invented so the student has a concrete task. Each
element carries the `uoc` items it evidences and a `standard` naming what must be true for them
to be met. An assessor marks the standard, never the table.
"""

from helpers import run_sheet as R  # noqa: E402  (the shared workbook engine, in the umbrella)

SITE = "https://yat.timbaird.com"
STATE = "s1-cl3-at2"
PROJECT = f"{SITE}/intranet/{STATE}/projects/ledgerline-improvement"
ICT = f"{SITE}/intranet/{STATE}/ict"
POLICY = f"{SITE}/intranet/{STATE}/policies"

# ---------------------------------------------------------------- front matter

SCENARIO = [
    "YAT College has approved the improvement design for the Ledgerline cloud infrastructure. "
    "Your MP Tech Solutions team now implements it. The team is four members, each owning one "
    "cloud component — network, compute, database, or storage — and together you produce one "
    "integrated, deployable template.",
    "You are an MTS Consultant reporting to Pat Lin (MTS Senior Consultant). Sam Walker (YAT ICT "
    "Manager) is the client. The approved design and the baseline are on the intranet: you "
    "implement the agreed design, you do not redesign it.",
    "What is assessed here is not the code. It is how you work as part of the team — how you help "
    "plan it, how you lead when it is your turn, how you support the people around you, and how "
    "you review how it went.",
]

RESOURCES = [
    ("Improvement Requirements — the outcomes the implementation serves",
     f"{PROJECT}/improvement-requirements"),
    ("Accounting System Infrastructure Specifications — the baseline you are improving",
     f"{ICT}/accounting-server-status-cloud"),
    ("Acceptable Use Policy — the code of conduct your team works under",
     f"{POLICY}/acceptable-use"),
    ("Work Health & Safety Policy — the safety obligations that apply to how the team works",
     f"{POLICY}/whs"),
    ("Change Management Procedure — the governance the team's work sits under",
     f"{POLICY}/change-management"),
]

ASSESSOR_PROVIDES = ("Your assessor will tell you the current address of the YAT site, confirm "
                     "your team and your allocated component, and arrange to observe you leading "
                     "one of your team's meetings.")

INSTRUCTIONS = [
    "This worksheet is yours. Everyone in your team has one, and each of you fills in your own — "
    "including where you are recording something the team agreed together. You are assessed as an "
    "individual on how you work within the team.",
    "Part A is a meeting agenda. Work through it with your team in the room: talk about each item, "
    "agree it, then write it down. The order is the order to discuss things in.",
    "Part B is the actual build. That work is submitted as itself — your code, in whatever form "
    "your team keeps it. The worksheet only records where it is and what you contributed.",
    "Part C is you leading a meeting with your assessor watching. Arrange it early; do not leave "
    "it to the last week.",
    "Parts D and E run across the whole project. Fill them in as things happen — a conflict you "
    "handled three weeks ago is very hard to write up honestly at the end.",
]

HOW_ASSESSED = [
    ("What is assessed", "your teamwork and leadership — planning, allocating, facilitating, "
                         "coaching, supporting, monitoring and reviewing"),
    ("What is not assessed", "the quality of the CloudFormation. The technical work is what the "
                             "team does together; it is the vehicle, not the subject"),
    ("Your team", "four members, one cloud component each — network, compute, database, storage"),
    ("What the team submits", "the team plan (recorded in each member's worksheet) and the "
                              "integrated, validated template"),
    ("What you submit", "this worksheet, complete, plus a link or reference to your own "
                        "contribution to the build"),
    ("The observed meeting", "one team meeting that you lead, with your assessor present. Arrange "
                             "it with them — see task 9"),
]

# ---------------------------------------------------------------- Part A — the planning meeting

PLAN = [
    dict(n=1, title="Agree what the team is here to do",
         resources=[
             ("Improvement Requirements — the outcomes the client has asked for",
              f"{PROJECT}/improvement-requirements"),
             ("Engagement Role Brief — what MTS is engaged to deliver",
              f"{PROJECT}/role-brief"),
         ],
         prompt="With your team: agree what you are collectively here to achieve, what each of you "
                "is responsible for, and what has to exist at the end for the engagement to be "
                "done. Talk about it first, then record what the team agreed. Write it in your own "
                "words — four identical worksheets suggest one person talked.",
         uoc=["BSBXTW401 PC 1.1", "BSBXTW401 FS Get the work done"],
         standard="the objectives are the team's own and are specific to this engagement, "
                  "responsibilities are assigned by name, and the required outcomes are things "
                  "someone could check for. PC 1.1 asks for objectives, responsibilities AND "
                  "required outcomes — all three must be present. Objectives copied verbatim from "
                  "the Improvement Requirements have restated the client's ask rather than agreed "
                  "the team's job.",
         given=1, blank_rows=6,
         table=(["", "What the team agreed"],
                [["Our common objective", ""],
                 ["Required outcome — the deliverable", ""],
                 ["Required outcome — how we know it is good enough", ""],
                 ["Responsibilities — network", ""],
                 ["Responsibilities — compute", ""],
                 ["Responsibilities — database", ""],
                 ["Responsibilities — storage", ""]])),

    dict(n=2, title="Set what is expected of each member",
         prompt="With your team: agree what each member is expected to produce, by when, and how "
                "you expect each other to behave while doing it. Behaviours matter as much as "
                "deliverables — most teams that struggle do not struggle over the work.",
         uoc=["BSBXTW401 PC 1.2", "BSBXTW401 KE 1"],
         standard="each member has an expected outcome, a goal that can be measured, and agreed "
                  "behaviours — and the behaviours reference the organisational standards the team "
                  "works under (the Acceptable Use Policy and code of conduct). PC 1.2 says "
                  "performance plans 'in accordance with team objective and relevant policies', so "
                  "the policy link is part of the item, and KE 1 (workplace policies, codes of "
                  "conduct, organisational reputation and culture) is evidenced here.",
         given=1, blank_rows=5,
         table=(["Member", "Expected outcome", "Goal we can measure", "Behaviours we agreed"],
                [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["Where these behaviours come from",
                  "the YAT Acceptable Use Policy and code of conduct", "", ""]])),

    dict(n=3, title="Agree how you will hold each other accountable",
         prompt="With your team: agree how you will know whether people are on track, and what you "
                "will do when someone is not. Decide this now, while everyone is comfortable — the "
                "point of agreeing it in advance is that nobody has to invent it in the moment.",
         uoc=["BSBXTW401 PC 1.3"],
         standard="the strategies are concrete and the team could actually follow them — a stated "
                  "check-in rhythm, a visible way of tracking who has what, an agreed first "
                  "response when something slips, and who raises it. 'We will communicate well' is "
                  "not a strategy. PC 1.3 asks for strategies that ensure accountability for roles "
                  "and responsibilities, so each row should tie to how the team will know.",
         given=1, blank_rows=5,
         table=(["Strategy", "How it works", "Who does it"],
                [["How we check progress", "", ""],
                 ["How we make work visible", "", ""],
                 ["What we do when someone falls behind", "", ""],
                 ["How we raise a problem with each other", "", ""],
                 ["When we escalate outside the team", "", ""]])),

    dict(n=4, title="Plan for what could go wrong",
         prompt="With your team: work out what could disrupt you, and agree what you would do about "
                "each one. Think about people, not just technology — the most common disruption to "
                "a four-person team is one of the four not being there.",
         uoc=["BSBXTW401 PC 1.4", "BSBXTW401 KE 9"],
         standard="the contingencies cover the people-side risks KE 9 names — unplanned absence, "
                  "re-allocating work, and who could cover an important role — as well as any "
                  "technical ones. A contingency plan listing only technical risks has missed what "
                  "the item is about; the response to each must be an action, not a hope.",
         given=1, blank_rows=6,
         table=(["What could happen", "How likely", "What we would do"],
                [["A member is away unexpectedly", "", ""],
                 ["A member's component turns out to be much bigger than expected", "", ""],
                 ["Someone's work has to be re-allocated", "", ""],
                 ["The person who understands one component is unavailable at integration", "", ""],
                 ["The components do not integrate cleanly", "", ""],
                 ["", "", ""]])),

    dict(n=5, title="Allocate the work",
         prompt="With your team: allocate the four components, and give each other real instruction "
                "— what the component covers, where it touches someone else's, and what done looks "
                "like. Allocate on the basis of what people are good at or want to develop, and "
                "record which of those it was.",
         uoc=["BSBXTW401 PC 2.2", "BSBXTW401 PE 1"],
         standard="each component is allocated to a named member with instruction specific enough "
                  "to start from, the basis for the allocation is stated (expertise or development "
                  "potential — PC 2.2 names both), and contingencies from task 4 are reflected. "
                  "PE 1 requires tasks assigned with appropriate instruction AND with contingencies "
                  "considered, so a bare allocation list has not met it.",
         given=1, blank_rows=5,
         table=(["Component", "Who", "Why them", "The instruction they were given",
                 "Done looks like"],
                [["Network", "", "", "", ""],
                 ["Compute", "", "", "", ""],
                 ["Database", "", "", "", ""],
                 ["Storage", "", "", "", ""],
                 ["Integration — who owns it", "", "", "", ""]])),

    dict(n=6, title="Agree how you will work with people outside the team",
         prompt="With your team: identify who outside the team you will need, and what for. That "
                "includes your assessor and anyone else whose input you depend on. Note where "
                "another team or another person could help you — a team that only ever talks to "
                "itself misses things.",
         uoc=["BSBXTW401 PC 2.1", "BSBXTW401 PC 2.4"],
         standard="the student identifies genuine collaboration opportunities beyond the four "
                  "members, and can say how the team's objectives were communicated to those "
                  "people. PC 2.4 is about identifying opportunities for cross collaboration with "
                  "external AND internal individuals, so a row naming only the assessor is thin.",
         given=1, blank_rows=5,
         table=(["Who", "What we need from them", "How we will communicate our objectives to them"],
                [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]])),
]

# ---------------------------------------------------------------- Part B — the work itself

WORK = [
    dict(n=7, title="Do your allocated work, and record where it is",
         prompt="Build your component of the approved design, and keep your work where the team can "
                "see it. Your code is submitted as itself, not copied into this worksheet — record "
                "here where it lives and what part of it is yours. If you are not sure what form "
                "your team should keep the work in, agree it with your team and ask your assessor.",
         uoc=["BSBXTW401 FS Get the work done"],
         standard="the student's own contribution is identifiable and reachable — a repository "
                  "link, a named file, or whatever form the team agreed — and the student can say "
                  "what part of the integrated result is theirs. This task is the vehicle, not the "
                  "assessment: the CloudFormation's technical quality is not marked here. What is "
                  "marked is that the student did the work they were allocated and kept it visible "
                  "to their team.",
         given=1, blank_rows=5,
         table=(["", "Your entry"],
                [["My allocated component", ""],
                 ["Where the team's work is kept", "repository, shared folder, or as agreed"],
                 ["Where my own contribution is, specifically", ""],
                 ["What state it is in", ""],
                 ["Anything I handed to, or took from, another member", ""]])),

    dict(n=8, title="Integrate and confirm the team's build",
         prompt="With your team: bring the four components into one deployable template, validate "
                "it, and agree together that it is ready. Record what integration actually took — "
                "components rarely fit together first time, and how the team handled that is worth "
                "more here than a clean result.",
         uoc=["BSBXTW401 PC 3.3", "BSBXTW401 FS Get the work done"],
         standard="the student describes their own part in integrating and in resolving what "
                  "integration surfaced. PC 3.3 (facilitate the team to identify, brainstorm, "
                  "report and resolve task-related issues and inefficiencies) is evidenced here "
                  "when the student can name an issue the team found and their role in resolving "
                  "it. 'It integrated fine' with no further detail evidences nothing.",
         given=1, blank_rows=5,
         table=(["", "Your entry"],
                [["Who owned the integration", ""],
                 ["What did not fit first time", ""],
                 ["How the team worked out what to do", ""],
                 ["My part in resolving it", ""],
                 ["How the team agreed it was ready", ""]])),
]

# ---------------------------------------------------------------- Part C — the observed meeting

MEETING = [
    dict(n=9, title="Lead a team meeting, with your assessor observing",
         prompt="Lead one of your team's meetings while your assessor watches. A daily stand-up is "
                "the easiest to run, but pick one where there is something to actually coordinate — "
                "allocating work, working through a problem, or getting the integration agreed — "
                "because that gives you something to lead. Arrange the time with your assessor "
                "early. Record the meeting below and ask your assessor to sign it off at the end.",
         uoc=["BSBXTW401 PC 2.1", "BSBXTW401 PC 2.3", "BSBXTW401 FS Interact with others"],
         standard="the student chairs a real working meeting of their own team and the assessor "
                  "observes it. What is being marked live: that the objectives and the purpose were "
                  "communicated, that tasks were allocated or confirmed with instruction, and that "
                  "everyone in the room was drawn in rather than the loudest two talking. The "
                  "coaching, issue-resolution and conflict criteria are evidenced by the records in "
                  "tasks 10 to 12 as well as here, so a quiet meeting does not cost the student "
                  "those items.",
         given=1, blank_rows=7,
         table=(["Meeting record", "Your entry"],
                [["Date and time", ""],
                 ["Type of meeting", "stand-up, working session, integration review, other"],
                 ["Who attended", ""],
                 ["What the meeting was for", ""],
                 ["What you did to open it — the objectives you communicated", ""],
                 ["What was allocated or confirmed, and to whom", ""],
                 ["How you made sure everyone contributed", ""]])),

    dict(n=10, title="Assessor observation record",
         prompt="Your assessor completes this at the end of the meeting you led. Bring your "
                "worksheet to the meeting so it can be signed on the spot — chasing a signature "
                "afterwards is your problem to avoid, not theirs to solve.",
         uoc=["BSBXTW401 PC 2.3", "BSBXTW401 FS Interact with others"],
         standard="the assessor observed the student leading and records which behaviours were "
                  "demonstrated. What this observation must establish is that the student can hold "
                  "a room: communicate purpose, allocate with instruction, and bring the whole team "
                  "into the conversation. The coaching, issue-resolution and conflict criteria are "
                  "NOT carried by this observation — the unit does not tie them to a meeting, and "
                  "they are evidenced by the reflections in tasks 11 to 13. Behaviours that did "
                  "arise here are worth noting as corroboration, but a quiet meeting costs the "
                  "student nothing.",
         given=2, blank_rows=9,
         table=(["Observed", "Demonstrated?", "Assessor note"],
                [["Communicated the team's objectives and the meeting's purpose", "", ""],
                 ["Allocated or confirmed tasks and gave appropriate instruction", "", ""],
                 ["Facilitated open, respectful collaboration, including diverse perspectives",
                  "", ""],
                 ["Coached or supported a member toward the team goals", "", ""],
                 ["Facilitated the team to identify and resolve a task-related issue", "", ""],
                 ["Managed a conflict or challenge constructively", "", ""],
                 ["Monitored progress against the plan and gave constructive feedback", "", ""],
                 ["Assessor name", "", ""],
                 ["Assessor signature and date", "", ""]])),
]

# ---------------------------------------------------------------- Part D — across the project

RUNNING = [
    dict(n=11, title="Describe a conflict or challenge you dealt with during the project",
         prompt="Describe a conflict or challenge you personally dealt with — a disagreement about "
                "the work, someone not delivering, a difficult conversation, or work that had to be "
                "taken off someone. Say what happened, what you did about it, and how it turned "
                "out. Write about the parts that did not go well too: an honest account of "
                "something you handled imperfectly evidences more than a tidy one. If you dealt "
                "with more than one, describe the two that taught you most.",
         uoc=["BSBXTW401 PE 5", "BSBXTW401 KE 5", "BSBXTW401 KE 10",
              "BSBXTW401 FS Interact with others"],
         standard="a genuine challenge of the kinds KE 10 names — difficulty performing tasks, "
                  "conflict with a team member or the client, a risk or safety concern, or "
                  "inappropriate behaviour — with what the student actually did and what came of "
                  "it. PE 5 requires conflicts managed according to organisational requirements, so "
                  "the response should connect to the behaviours the team agreed in task 2 or to "
                  "YAT's policies. A student who reports no challenge at all has either not been "
                  "involved or is not being frank, and is worth asking about directly.",
         points=[
             "what actually happened, in enough detail that the situation is clear",
             "what they did — the specific action, not 'I communicated'",
             "why they chose that approach over the alternative",
             "how it turned out, including if it did not fully resolve",
             "the connection to the agreed team behaviours or YAT's code of conduct",
             "what they would do differently",
         ]),

    dict(n=12, title="Describe a time you coached or helped a team member",
         prompt="Describe a situation during the project where you helped or coached someone on "
                "your team — explaining something they were stuck on, working through a problem "
                "with them, or supporting them to get back on track. Say what they needed, what you "
                "did, and what changed as a result. Helping someone solve their own problem counts "
                "for more here than solving it for them.",
         uoc=["BSBXTW401 PC 3.1", "BSBXTW401 PC 3.2", "BSBXTW401 PE 2"],
         standard="a real instance with a named need, a specific action, and an outcome. PC 3.1 "
                  "(coaching to enhance workplace culture) and PC 3.2 (support individuals to work "
                  "towards common team goals) are both evidenced when the student adapted to what "
                  "the person actually needed. A student who describes doing the other member's "
                  "work for them has helped the deliverable, not the person, and should be probed "
                  "on what the member could do afterwards that they could not before.",
         points=[
             "who needed help and what with — the specific difficulty",
             "how the student noticed, or how it was raised with them",
             "what they actually did: explained, paired, asked questions, took something off them",
             "why that approach suited that person and that problem",
             "what changed — what the member could do afterwards",
             "the effect on the team, not just on the task",
         ]),

    dict(n=13, title="Describe an issue the team hit, and your part in resolving it",
         prompt="Describe a task-related problem or inefficiency your team ran into, and your part "
                "in sorting it out. The interesting ones are usually nobody's fault — a dependency "
                "nobody spotted, two people building the same thing, a decision that nobody "
                "actually made. Say how the team found it and what you did to help the team resolve "
                "it, rather than what you resolved alone.",
         uoc=["BSBXTW401 PC 3.3", "BSBXTW401 PC 3.4"],
         standard="a real task-related issue, how it surfaced, and the student's own contribution "
                  "to the team resolving it. PC 3.3 names identify, brainstorm, report AND resolve, "
                  "and it is about facilitating the TEAM — so an account of the student fixing it "
                  "single-handedly evidences PC 3.4's problem solving but not PC 3.3's "
                  "facilitation, and should be marked accordingly.",
         points=[
             "the issue, and how it came to light",
             "how the team worked out what to do — who was involved and how it was discussed",
             "the student's own part: raising it, running the discussion, proposing the option, "
             "getting the decision made",
             "what was decided and whether it worked",
             "anything the team changed in how it worked so it would not recur",
         ]),
]

# ---------------------------------------------------------------- Part E — review and close out

REVIEW = [
    dict(n=14, title="Measure the team against the plan",
         prompt="Go back to the expectations you agreed in task 2 and measure what actually "
                "happened against them, member by member — including yourself. Be fair and be "
                "specific. This is a professional judgement, not a popularity contest.",
         uoc=["BSBXTW401 PC 4.1", "BSBXTW401 PE 3"],
         standard="every member including the student is measured against the task 2 expectations, "
                  "with evidence rather than impression. PC 4.1 says 'against agreed work plans', "
                  "so the measurement must trace back to what was actually agreed. PE 3 (collate "
                  "feedback on individual and team performance) is evidenced by the student "
                  "gathering input rather than judging alone — say where the assessment came from.",
         given=1, blank_rows=5,
         table=(["Member", "What was expected", "What happened", "Met?"],
                [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["Where your assessment came from",
                  "your own observation, the team's input, the work itself", "", ""]])),

    dict(n=15, title="The feedback you gave",
         prompt="Record the performance feedback you gave each member, and when. Feedback given at "
                "the end of a project is a report card; feedback given during it is useful. Note "
                "which of yours was which — and if some of it was late, say so.",
         uoc=["BSBXTW401 PC 4.2", "BSBXTW401 PE 2"],
         standard="feedback is recorded per member with what was said and roughly when, and it is "
                  "constructive and specific. PC 4.2 requires it timely and constructive and "
                  "according to expected organisational standards, so feedback delivered only at "
                  "the end, or feedback that is only praise, partially meets the item at best. A "
                  "student who notes their own feedback was late has met the reflective bar the "
                  "unit expects.",
         given=1, blank_rows=5,
         table=(["Member", "What you told them", "When", "How they responded"],
                [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["", "", "", ""]])),

    dict(n=16, title="Development opportunities and what you did about them",
         prompt="Identify what would make each member — and the team as a whole — better next time, "
                "and say what was actually done about it during this project. An identified "
                "opportunity that nobody acted on is a note; the unit asks for action plans that "
                "were implemented.",
         uoc=["BSBXTW401 PC 4.3", "BSBXTW401 PC 4.4", "BSBXTW401 PE 4"],
         standard="development needs are identified for individuals and for the team, and each "
                  "carries an action that was actually taken or started during the project. PC 4.4 "
                  "(implement action plans) and PE 4 (identify AND implement development "
                  "opportunities for others) both require implementation, so a table of "
                  "recommendations with nothing done has met PC 4.3 only.",
         given=1, blank_rows=5,
         table=(["Who", "Development need", "The action plan", "What was actually done"],
                [["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                 ["The team as a whole", "", "", ""],
                 ["Yourself", "", "", ""]])),

    dict(n=17, title="Reflect on how you led",
         prompt="Look back over the project at your own leadership. What did you do well, what did "
                "you do badly, and what would you do differently with the same team tomorrow? Write "
                "this properly — it is the one place in the whole assessment where the honest answer "
                "is worth more than the impressive one.",
         uoc=["BSBXTW401 KE 8", "BSBXTW401 FS Interact with others"],
         standard="the reflection is specific to what the student actually did and shows awareness "
                  "of the professional behaviours a leader models (KE 8) — reliability, fairness, "
                  "following through, how they behaved when under pressure. Generic self-praise, or "
                  "a reflection that identifies no weakness, has not met the bar.",
         points=[
             "something specific they did well, with the evidence for it",
             "something they did badly or late, named plainly",
             "how they behaved when the team was under pressure — that is where the professional "
             "behaviours in KE 8 are actually tested",
             "what they would do differently with the same team tomorrow",
             "what they now know about leading that they did not at task 1",
         ]),
]

# ---------------------------------------------------------------- knowledge questions

QUESTIONS = [
    dict(n=1, title="What organisational and legislative requirements applied to your team?",
         prompt="Explain the organisational requirements your team worked under and the legislative "
                "requirements that applied — and for each, point at where it actually affected how "
                "your team worked, not just that it existed.",
         uoc=["BSBXTW401 KE 1", "BSBXTW401 KE 2", "BSBXTW401 FS Navigate the world of work"],
         standard="the student names YAT's workplace policies and code of conduct and connects them "
                  "to the behaviours agreed in task 2, addresses organisational reputation and "
                  "culture (both named in KE 1), and identifies real legislative requirements — work "
                  "health and safety, privacy over the client data the team touches, and "
                  "anti-discrimination in how the team treats each other. A list of legislation with "
                  "no connection to the team's actual work has not met the contextual bar.",
         points=[
             "the workplace policies the team worked under, and where they shaped the agreed "
             "behaviours",
             "the code of conduct — what it required of the team in practice",
             "organisational reputation and culture: the team represents MTS in front of a client",
             "work health and safety obligations as they apply to how the team worked",
             "privacy obligations over the client information the team had access to",
             "the requirement to treat each other without discrimination, and what that meant for "
             "how meetings ran",
         ]),

    dict(n=2, title="What facilitation, coaching and communication techniques did you use?",
         prompt="Describe the techniques you used to keep the team working together — how you ran "
                "meetings, how you coached, and how you adapted the way you communicated to "
                "different people. Point at where you used each.",
         uoc=["BSBXTW401 KE 3", "BSBXTW401 KE 4", "BSBXTW401 KE 6", "BSBXTW401 KE 7"],
         standard="the student names real techniques and locates them in their own project: "
                  "facilitation (going round the room, timeboxing, making work visible), coaching "
                  "(asking rather than telling, pairing, modelling), and communication choices "
                  "(when to use a message and when to have a conversation). KE 7 requires "
                  "cross-cultural communication and communicating with people with special needs or "
                  "disabilities to be addressed specifically — a student who skips that half has "
                  "not met the item.",
         points=[
             "facilitation: how you got the quiet member to contribute, and how you kept the "
             "meeting to time",
             "coaching: asking questions rather than giving answers, pairing, modelling the work",
             "different communication methods and when each suited — written for a decision "
             "record, spoken for a disagreement",
             "cross-cultural communication: not assuming shared context, checking understanding "
             "rather than assuming agreement, allowing for directness meaning different things to "
             "different people",
             "adapting for a team member with a disability or a specific need — what you would do, "
             "or did",
         ]),

    dict(n=3, title="How do you resolve conflict, and what challenges should a team expect?",
         prompt="Explain the strategies available for resolving conflict and negotiating a way "
                "through disagreement, and describe the challenges a team like yours should expect "
                "to meet. Connect them to what actually happened in your team.",
         uoc=["BSBXTW401 KE 5", "BSBXTW401 KE 10"],
         standard="real strategies are named — addressing it early and privately, separating the "
                  "person from the problem, finding the shared interest, escalating when it is "
                  "beyond the team — and tied to the conflicts recorded in task 13. KE 10's four "
                  "categories (difficulties performing tasks, conflicts with clients or team "
                  "members, risks or safety hazards, unethical or inappropriate behaviour) should "
                  "all be recognised as things a team can expect, even where the student's own team "
                  "only met some.",
         points=[
             "deal with it early and in private before it becomes the team's problem",
             "separate the person from the problem; argue about the work, not the character",
             "find what both people actually want — usually the same thing, differently expressed",
             "know when it is beyond you and has to be escalated",
             "the challenges to expect: difficulty performing tasks, conflict with team members or "
             "the client, risks and safety hazards, and unethical or inappropriate behaviour",
             "which of those your team actually met, and which you were fortunate to avoid",
         ]),
]

# ---------------------------------------------------------------- rendering


def render_front_matter(doc, h1):
    h1("Scenario")
    for para in SCENARIO:
        R.p(doc, para, after=8)
    h1("How this assessment works")
    R.settings_table(doc, HOW_ASSESSED)
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


def render(doc, h1, h2, mode="student", plan=None, work=None, meeting=None, running=None,
           review=None, questions=None, notes=False):
    """Render AT2 into `doc`. mode = student | assessor."""
    PLAN_ = PLAN if plan is None else plan
    WORK_ = WORK if work is None else work
    MEETING_ = MEETING if meeting is None else meeting
    RUNNING_ = RUNNING if running is None else running
    REVIEW_ = REVIEW if review is None else review
    QUESTIONS_ = QUESTIONS if questions is None else questions

    h1("Part A — The planning meeting")
    R.p(doc, "Work through these with your team in the room. Talk about each one, agree it, then "
             "write down what was agreed. This is your agenda for the first meeting.",
        italic=True, size=9.5, colour=R.GREY, after=10)
    for el in PLAN_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Part B — The build")
    R.p(doc, "The build is submitted as itself. These two tasks record where your work is and what "
             "you contributed — they do not ask you to copy your code in here.",
        italic=True, size=9.5, colour=R.GREY, after=10)
    for el in WORK_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Part C — Leading a meeting")
    R.p(doc, "Arrange this with your assessor early in the project. Bring this worksheet to the "
             "meeting so it can be signed at the end.",
        italic=True, size=9.5, colour=R.GREY, after=10)
    for el in MEETING_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Part D — What happened, and what you did")
    R.p(doc, "Three things that happen in every team project. Write about your own experience of "
             "them, in your own words. These carry more of your evidence than the observed meeting "
             "does — make notes as the project runs so you are not reconstructing it weeks later.",
        italic=True, size=9.5, colour=R.GREY, after=10)
    for el in RUNNING_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Part E — Review and reflection")
    for el in REVIEW_:
        R.element(doc, h2, el, mode, notes=notes)

    h1("Knowledge questions")
    R.p(doc, "Answer these about your own team and your own leadership. Generic answers about "
             "teamwork will not pass.", italic=True, size=9.5, colour=R.GREY, after=10)
    for q in QUESTIONS_:
        R.element(doc, h2, q, mode, label="Question", notes=notes)
