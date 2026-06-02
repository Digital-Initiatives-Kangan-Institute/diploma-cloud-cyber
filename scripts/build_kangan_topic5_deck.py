#!/usr/bin/env python3
"""Topic 5 (Making the case) — Kangan-branded teaching deck. All bespoke (AT1 Part B / presentation).

Content only; brand + layouts live in kangan_deck.py.
Usage:  python scripts/build_kangan_topic5_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kangan_deck import *  # noqa: F401,F403  (brand palette + layouts)

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_05/Topic_05_Slides.pptx"

A1, A2, A3 = MAGENTA, SKY, GREEN   # section accents (match Topics 2–4)


def build(path):
    prs = new_deck()
    n = [0]
    def pg(): n[0] += 1; return n[0]

    # Title
    title_slide(prs, "05", "Making the case",
                "Present the business case to the board — and win the decision")

    # Opener
    content_slide(prs, pg(), "From the written case to the room", "a great case still has to be sold", [
        (0, "The written case is done (Topics 2–4) — this Topic is about communicating and defending it."),
        (0, "Three moves: prepare & rehearse → deliver → handle the room.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "This is the presentation event — an observed assessment: how you present is assessed, not just what you built."),
    ])

    # ===== C1 — Prepare & rehearse =====
    divider_slide(prs, "01", "Prepare & rehearse", "from document to pitch", A1)
    content_slide(prs, pg(), "The pitch is a distillation, not a read-through", "", [
        (0, "A board deck isn't your business case with slide borders — the board already read the document."),
        (0, "The deck carries the spine — the ask, the money, the risk, the plan; you fill the rest verbally."),
        (0, "8–10 slides, one section each, with speaker notes — on the YAT Board Presentation Deck template.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "The board arc", "order it the way a board decides", [
        (0, "Agenda → strategic context → current state → the gap → options → recommendation"),
        (0, "cost summary → benefits → risks → implementation plan → the decision → Q&A"),
        (0, "One section per slide: headline + a few points. The recommendation and the plan get the airtime.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "What makes the cut", "", [
        (0, "KEEP — the ask · the cost comparison · key risks + mitigations · the plan · the strategic fit.", {"bold": True}),
        (0, "CUT — line-item detail · method explanations · anything that lives in the appendices.", {"bold": True}),
        (0, "If a slide doesn't help the decision, it's a handout — not a pitch slide.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    content_slide(prs, pg(), "Rehearse — this is where pitches are won", "", [
        (0, "Preparation isn't done when the deck is built. Rehearse:"),
        (1, "run it aloud — walk the board through each slide, don't read it"),
        (1, "time it (target 10–15 min); if you run long, cut"),
        (1, "anticipate the board's questions and prepare your answers"),
        (1, "practise stating the ask and asking for sign-off — the bit most often fumbled"),
        (0, "A rehearsed pitch sounds confident; an unrehearsed one reads off the slides.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], accent=A1)
    activity_slide(prs, pg(), "Build & rehearse your board deck", [
        (0, "Build an 8–10 slide board deck for your practice Business Case (Accounting System / Ledgerline) on the YAT Board Presentation Deck template, with speaker notes.", {"bold": True}),
        (0, "Then rehearse it:"),
        (1, "run it aloud and time it (target 10–15 min)"),
        (1, "in your notes, write the three questions you'd least like to be asked — and your answers"),
        (0, "Lead with the section spine; slides = headline + a few points; end on the decision."),
        (0, "⚠  Rehearsal isn't optional — a pitch you haven't said aloud isn't ready.", {"color": A1, "mark_color": A1}),
    ], "~30 min build + rehearse, then we present", accent=A1)
    takeaways_slide(prs, pg(), "Section 1 · Prepare & rehearse", [
        "The deck is a distillation — the spine, not the whole document.",
        "Board arc: context → gap → options → recommendation → cost/risk → plan → the ask.",
        "Preparation includes rehearsal: run it aloud, time it, prepare for the questions.",
    ], accent=A1)

    # ===== C2 — Deliver the case =====
    divider_slide(prs, "02", "Deliver the case", "present to the board", A2)
    content_slide(prs, pg(), "Lead with the ask", "", [
        (0, "A board listens better when it knows what you want."),
        (0, "Open by naming the decision you're seeking — then walk them through the case that justifies it."),
        (0, "Don't hide the ask on the last slide.", {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Walk the board through it", "", [
        (0, "Report the situation and the gap."),
        (0, "Walk through how you evaluated the options — the CBA + risk."),
        (0, "Put the action plan — explicitly seeking the board's feedback and approval."),
        (0, "You're reporting to a superior and asking for a decision, not lecturing.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    content_slide(prs, pg(), "Speak the board's language", "", [
        (0, "The board is not technical."),
        (0, "Plain English; translate each technical term as you use it — “RDS: a managed database the vendor runs for us”."),
        (0, "Pitch ideas in business terms — cost, risk, availability, continuity."),
        (0, "Jargon loses the room.", {"bold": True, "color": A2, "mark_color": A2}),
    ], accent=A2)
    activity_slide(prs, pg(), "Deliver your pitch", [
        (0, "Present your board deck to a mock board (peers + trainer as Sam Walker / Pat Lin), 10–15 minutes.", {"bold": True}),
        (0, "Remember to:"),
        (1, "open with the ask"),
        (1, "walk context → gap → options → recommendation → cost/risk → plan"),
        (1, "translate technical terms as you go; eyes on the room, not the slides"),
        (0, "⚠  You're seeking a decision — present to persuade, not to inform.", {"color": A2, "mark_color": A2}),
    ], "10–15 min each, then feedback", accent=A2)
    takeaways_slide(prs, pg(), "Section 2 · Deliver the case", [
        "Lead with the ask, then justify it.",
        "Report → evaluate → put the plan and seek approval.",
        "Plain English, technical terms translated, pitched to a non-technical board.",
    ], accent=A2)

    # ===== C3 — Handle the room =====
    divider_slide(prs, "03", "Handle the room", "Q&A, feedback & sign-off", A3)
    content_slide(prs, pg(), "Q&A is assessed", "", [
        (0, "The board's questions aren't a formality — they probe whether you understand your own analysis and the principles behind it."),
        (0, "Defend your case from your evidence; don't bluff.", {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Listen, then answer", "", [
        (0, "Let the question land; clarify if unsure — “Do you mean cost or risk?”"),
        (0, "Answer directly, pointing to your evidence (your CBA, your risk register)."),
        (0, "Check it landed before moving on."),
        (0, "A crisp “good question — here's the data” beats a long ramble.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Be ready for these", "the dimensions the board probes", [
        (0, "Cost assumptions — what if pricing changes?"),
        (0, "Risk — the single biggest reason to say no?"),
        (0, "Prioritisation — which change carries the most risk?"),
        (0, "Strategic fit — what if YAT opens a second campus in Year 3?"),
        (0, "Service models & standards — why IaaS/PaaS here? which standards informed it?"),
        (0, "These come from your own Topics 1–4 work — defend, don't re-derive.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    content_slide(prs, pg(), "Seek feedback & get sign-off", "", [
        (0, "Explicitly seek and respond to the board's feedback — confirm you've understood it."),
        (0, "Capture the feedback in the Feedback Record."),
        (0, "Obtain the board's sign-off on the action plan."),
        (0, "The decision is the point of the whole exercise — ask for it.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], accent=A3)
    activity_slide(prs, pg(), "Run the Q&A, feedback & sign-off", [
        (0, "After each pitch, the mock board asks 3–5 questions, gives feedback, and signs off.", {"bold": True}),
        (1, "Presenter: clarify → answer from your evidence → seek/respond to feedback → capture it → get the sign-off."),
        (1, "Board: probe across the dimensions above."),
        (0, "⚠  Always close by asking for the decision.", {"color": A3, "mark_color": A3}),
    ], "~5 min each, then debrief", accent=A3)
    takeaways_slide(prs, pg(), "Section 3 · Handle the room", [
        "Q&A tests your grasp of your own case — defend it from your evidence.",
        "Listen, clarify, answer directly, check it landed.",
        "Seek and respond to feedback, capture it, and obtain sign-off — always ask for the decision.",
    ], accent=A3)

    # ===== Close =====
    close_slide(prs, "From the practice room to the real thing", [
        "You can now build a board deck, deliver it, and handle the room — the whole communication skill.",
        "That completes the case for the migration: analyse it, plan it, and sell it.",
        "You practised on the Accounting System; next you do it for real.",
        "Next: produce and present your real Business Case for the YAT LMS migration.",
    ])

    save(prs, path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
