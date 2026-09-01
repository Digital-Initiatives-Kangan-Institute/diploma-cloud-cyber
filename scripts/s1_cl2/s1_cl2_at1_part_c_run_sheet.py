#!/usr/bin/env python3
"""The S1-CL2 AT1 Part C approval workbook — content, and the renderer that places it.

ONE definition, rendered two ways (student | assessor), through the shared workbook engine.

WHAT THIS PART IS, AND WHAT IT IS NOT. Part C is a live event: the student walks Sam Walker
(role-played by the assessor) through the Part A design and the Part B plan, answers questions,
responds to feedback, lodges the plan and obtains sign-off. `[ICTCLD501 PC 5.1]` says "Conduct
VERBAL walkthrough" and `[ICTCLD501 FS Oral communication]` is only demonstrable in the room.
**Completing this worksheet is not the assessment — presenting is.** The front matter says so
to the student, in those words.

WHY THERE IS NO PRESENTATION DECK. PC 5.1 requires a verbal walkthrough of the plan, not a
slide deck. A deck is a delivery convention, not a unit requirement, so under the standing rule
(worksheet unless a UoC requirement explicitly demands a separate artefact) none is asked for.
The student walks through the two documents they have already produced. A student who wants to
build slides may, and nothing marks them.

THE TWO KINDS OF ELEMENT HERE. Preparation tasks carry no `uoc` and no `standard` — they are
scaffolding, they are not marking criteria, and their prompts say so, so neither student nor
assessor mistakes them for assessed work. The record tasks that follow ARE the criteria, one
per PC in element 5.
"""

from helpers import run_sheet as R  # noqa: E402  (the shared workbook engine, in the umbrella)

SITE = "https://yat.timbaird.com"
STATE = "s1-cl2-at1"
PROJECT = f"{SITE}/intranet/{STATE}/projects/website-global-expansion"
POLICY = f"{SITE}/intranet/{STATE}/policies"

# ---------------------------------------------------------------- front matter

INTRO = [
    "This is the approval gate. You walk Sam Walker (YAT ICT Manager, role-played by your "
    "assessor) through the design you produced in Part A and the disaster recovery plan you "
    "produced in Part B, answer questions on both, respond to the feedback you are given, lodge "
    "the plan and obtain sign-off.",
    "Completing this worksheet is not the assessment. Presenting is. The first two tasks are "
    "your preparation and nothing in them is marked — they exist so you walk in ready. "
    "Everything from task 3 onward is a record of what actually happened in the room.",
    "There is no slide deck to build. You are walking your reader through two documents you have "
    "already written, which is what a consultant does. Bring them, printed or on screen, and know "
    "your way around them.",
]

EVENT = [
    ("Format", "in person on campus, or by video conference — confirm which with your assessor"),
    ("Duration", "10–15 minutes walking through, then about 5 minutes of questions, feedback and "
                 "sign-off"),
    ("Bring", "your completed Part A worksheet and your completed Disaster Recovery Plan"),
    ("Submit beforehand", "both documents, at least 48 hours before the session, so Sam Walker "
                          "has read them"),
    ("Who is in the room", "you and Sam Walker (your assessor). Sam has read the documents but "
                           "will ask you to explain the reasoning behind them"),
]

RESOURCES = [
    ("Records Management Policy — the lodgement protocol a completed engagement document follows",
     f"{POLICY}/records-management"),
    ("Engagement Role Brief — who signs off what on this engagement",
     f"{PROJECT}/role-brief"),
]

# ---------------------------------------------------------------- the tasks

APPROVAL = [
    # ---- preparation: deliberately not assessed, and the prompts say so ----
    dict(n=38, title="Plan your walkthrough",
         prompt="Preparation — not assessed. Nobody marks this table; it exists so you are not "
                "improvising in front of your client. Plan the order you will take Sam through the "
                "two documents, and for each part write down the ONE point you want Sam to "
                "understand. You have 10 to 15 minutes, which is not long enough to read your work "
                "out — so decide what matters.",
         given=1, blank_rows=7,
         table=(["What you cover", "The one point Sam should take away", "Roughly how long"],
                [["Why the engagement exists",
                  "the India campus makes the website the enrolment front door — that is why any of "
                  "this is worth doing", "1 min"],
                 ["The web-scale design",
                  "the edge layer answers the latency requirement; the existing platform is kept",
                  "3 min"],
                 ["The microservice",
                  "the log obligation is met by a separate service so it cannot affect the website",
                  "2 min"],
                 ["The risks you assessed",
                  "these are the three events worth planning for, and why", "2 min"],
                 ["The recovery strategy",
                  "pilot light meets the 4-hour target without paying for idle capacity", "3 min"],
                 ["What you are asking for", "approval to proceed to implementation", "1 min"],
                 ["What you deliberately did not do",
                  "the exclusions, so Sam is not surprised later", "1 min"]])),

    dict(n=39, title="Anticipate the questions",
         prompt="Preparation — not assessed. Write down the questions you would ask if you were Sam, "
                "and your answer to each. The ones worth preparing are the ones where you made a "
                "choice someone could reasonably disagree with — that is exactly where you will be "
                "asked.",
         given=1, blank_rows=6,
         table=(["Question you expect", "Your answer"],
                [["Why not just back up to another region — it is cheaper?",
                  "backup and restore cannot make a 4-hour recovery time; the requirement decides it"],
                 ["Why not run two regions all the time?",
                  "it doubles the cost to beat a target we already meet; the requirements ask for "
                  "the simplest arrangement that works"],
                 ["Do we have to move the whole website to India?",
                  "no — the obligation is on logs; the residency document is explicit that the main "
                  "data store may stay in Australia"],
                 ["What does this cost us to run?",
                  "the edge layer and the replication; the second region costs almost nothing until "
                  "it is invoked"],
                 ["What happens if the log service goes down?",
                  "events queue and are written when it recovers; the website is unaffected, which "
                  "is why it is a separate service"],
                 ["How do we know the plan works?",
                  "it is not proven until it is tested — and that is a recommendation, not something "
                  "this engagement delivered"]])),

    # ---- the assessed record: one element per PC in 501 element 5 ----
    dict(n=40, title="The walkthrough",
         prompt="Record the session: when it happened, who was there, and what you actually covered. "
                "Fill this in immediately afterwards, while you remember it.",
         uoc=["ICTCLD501 PC 5.1", "ICTCLD501 FS Oral communication"],
         standard="the student conducted a verbal walkthrough of the DR plan with the required "
                  "person — this is observed live by the assessor, and the table is the record, not "
                  "the evidence. PC 5.1 is met by the student explaining their own plan in their own "
                  "words and answering questions on it using appropriate industry language. Reading "
                  "the document aloud, or being unable to explain a decision recorded in their own "
                  "plan, has not met it.",
         given=1, blank_rows=5,
         table=(["Record", "Your entry"],
                [["Date and time of the session", "—"],
                 ["Attendees and their roles", "Sam Walker (YAT ICT Manager); the student (MTS)"],
                 ["Documents walked through",
                  "the Part A design worksheet and the Disaster Recovery Plan"],
                 ["What you covered", "per your task 38 plan, noting anything you changed on the day"],
                 ["Questions you were asked", "the substance of them, and how you answered"]])),

    dict(n=41, title="Feedback sought, and your response",
         prompt="Record the feedback Sam gave you and what you did about it. Sam will give you at "
                "least one thing to change — that is the point of an approval gate. For each item, "
                "say what you were told, what you decided to do, and if you disagreed, say that and "
                "why. Agreeing with everything is not the same as responding to feedback.",
         uoc=["ICTCLD501 PC 5.2"],
         standard="the student both SOUGHT feedback (asked for it, rather than waiting to be "
                  "corrected) and RESPONDED to it with a decision and a reason. A record showing "
                  "feedback received and no response, or 'agreed' against every item with no change "
                  "made, has not met PC 5.2. A reasoned disagreement, recorded, is a satisfactory "
                  "response.",
         given=1, blank_rows=5,
         table=(["Feedback from Sam Walker", "Your response", "Change made?"],
                [["e.g. the recovery steps do not say who repoints DNS",
                  "accepted — assigned to YAT ICT in step 6", "Yes"],
                 ["e.g. consider whether 24 hours is acceptable for media recovery",
                  "considered and retained — media changes rarely and a day-old copy is materially "
                  "the same site", "No, with reason"],
                 ["", "", ""],
                 ["", "", ""],
                 ["", "", ""]])),

    dict(n=42, title="Lodge the plan",
         resources=[
             ("Records Management Policy — where a completed engagement document is lodged, and "
              "how it is retained", f"{POLICY}/records-management"),
         ],
         prompt="Lodge the approved Disaster Recovery Plan the way YAT requires. Read the Records "
                "Management Policy and follow it — record where you lodged it, under what "
                "classification, and who can retrieve it. Remember what you wrote in Part B task 32: "
                "a plan nobody can reach during an outage is not a plan.",
         uoc=["ICTCLD501 PC 5.3"],
         standard="the plan is lodged according to YAT's Records Management Policy rather than "
                  "wherever the student found convenient, and the record names the location, the "
                  "classification and the retention. PC 5.3 says 'according to organisation and "
                  "legislative protocol' — a student who attaches the file to an email has not met "
                  "it. A strong answer also notes that a copy must be reachable when the primary "
                  "region is not.",
         given=1, blank_rows=4,
         table=(["Lodgement record", "Your entry"],
                [["Where it is lodged", "per the Records Management Policy"],
                 ["Classification applied", "Internal — ICT, and engaged consultants under the MSA"],
                 ["Retention period", "per the policy"],
                 ["Who can retrieve it, and how, during an outage",
                  "named roles, and a copy held outside the primary region"]])),

    dict(n=43, title="Obtain sign-off",
         prompt="Obtain Sam Walker's sign-off. This is the gate: without it the engagement does not "
                "proceed to implementation. Record the decision — including if it is approval with "
                "conditions, which is a real outcome and not a failure.",
         uoc=["ICTCLD501 PC 5.4"],
         standard="sign-off is obtained from the required person and recorded with a decision, a "
                  "name and a date. PC 5.4 is met by the student ASKING for and OBTAINING it — a "
                  "student who presents well but never closes the loop has not met the item. "
                  "'Approved with conditions' is a satisfactory outcome where the conditions are "
                  "recorded.",
         given=1, blank_rows=4,
         table=(["Sign-off record", "Your entry"],
                [["Decision", "Approved / Approved with conditions / Not approved"],
                 ["Any conditions attached", "—"],
                 ["Signed by", "Sam Walker, YAT ICT Manager"],
                 ["Date", "—"]])),
]

# ---------------------------------------------------------------- rendering


def render(doc, h1, h2, mode="student", approval=None, notes=False):
    """Render Part C into `doc`. mode = student | assessor."""
    APPROVAL_ = APPROVAL if approval is None else approval

    h1("Part C — Presentation and approval")
    for para in INTRO:
        R.p(doc, para, after=8)
    R.p(doc, "The session", bold=True, size=9.5, after=3)
    R.settings_table(doc, EVENT)
    R.resources_block(doc, RESOURCES)

    for el in APPROVAL_:
        R.element(doc, h2, el, mode, notes=notes)
