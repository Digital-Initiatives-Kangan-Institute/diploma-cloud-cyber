#!/usr/bin/env python3
"""Topic 3 (Building the evidence) — authored into Kangan-branded layouts.

Built from topic_03/slide_plan.md + coverage.md. Mostly bespoke (options / CBA / risk), with the
two AWS Pricing Calculator slides (ACF M02 S20 + S22, supplied in source_slides/) authored in at
their marked positions in C2 — the calculator screenshot left as a labelled placeholder to transfer.

Brand: documentaion/kangan-branding.md. Reuses helpers from build_kangan_topic_deck (brand
primitives + layouts) and build_kangan_topic1_deck (visual_slide + placeholder).

Usage:  python scripts/build_kangan_topic3_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_kangan_topic_deck as k       # noqa: E402
import build_kangan_topic1_deck as t1      # noqa: E402  visual_slide, placeholder

from pptx.util import Inches, Pt  # noqa: E402

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_03/Topic_03_Slides.pptx"

A1, A2, A3 = k.MAGENTA, k.SKY, k.GREEN   # section accents (match Topic 2)


def build(out_path):
    prs = k.Presentation()
    prs.slide_width = k.EMU_W; prs.slide_height = k.EMU_H
    n = [0]
    def pg(): n[0] += 1; return n[0]

    # ===== Title =====
    k.title_slide(prs, "03", "Building the evidence",
                  "Options, cost and risk — the case a board can act on")

    # ===== Opener =====
    t1.visual_slide(prs, pg(), "From diagnosis to evidence", "you've proved the problem — now build the answer", [
        (0, "A board doesn't fund a problem — it funds a well-evidenced answer."),
        (0, "Three moves: lay out the options → cost them over time → weigh the risks.",
            {"bold": True, "color": A1, "mark_color": A1}),
        (0, "These become the next sections of the same business case."),
        (0, "You still don't recommend yet — you assemble the evidence a recommendation rests on."),
    ], [], A1)

    # ===== C1 — Options & evaluation =====
    k.divider_slide(prs, "01", "Options & evaluation", "compare before you choose", A1)
    t1.visual_slide(prs, pg(), "You don't recommend until you've compared", "", [
        (0, "A single proposal isn't a case — it's an assertion."),
        (0, "Credible advice compares realistic options on a level field."),
        (0, "Your job here: lay the options out and evaluate them — not pick one.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], [], A1)
    t1.visual_slide(prs, pg(), "Define the workload first", "options are judged against it", [
        (0, "Before comparing options, state what any option must satisfy — from your gap analysis + the migration requirements:"),
        (1, "capacity & peaks · availability target · recovery (RPO/RTO)"),
        (1, "data residency & retention · integrations"),
        (0, "Write it down first — it's the yardstick every option is measured against.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], [], A1)
    t1.visual_slide(prs, pg(), "Identify the realistic options", "", [
        (0, "Keep the option set honest and small:"),
        (1, "Option A — renew / stay on-prem (the status-quo baseline)"),
        (1, "Option B — migrate to the cloud"),
        (0, "Name a third only if it's genuinely real."),
        (0, "Every comparison needs the status-quo option — or “moving” has nothing to beat.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], [], A1)
    t1.visual_slide(prs, pg(), "Choosing an evaluation method", "criteria, not gut feel", [
        (0, "Evaluate each option on two stated lenses:"),
        (1, "Impact against the strategic objectives — does it move the org toward its goals?"),
        (1, "Difficulty of implementing — effort, disruption, skills, dependencies"),
        (0, "Score each option on each lens and show your reasoning. (Cost comes next.)"),
    ], [], A1)
    t1.visual_slide(prs, pg(), "Impact & difficulty — a first read", "", [
        (0, "A simple matrix communicates it: each option × {impact, difficulty}."),
        (0, "High impact + low difficulty = strong candidate."),
        (0, "High impact + high difficulty = real, but plan for it."),
        (0, "This is the qualitative shortlist — the CBA and risk sections test it next.",
            {"bold": True, "color": A1, "mark_color": A1}),
    ], [], A1)
    k.activity_slide(prs, pg(), "Define the options & evaluate", [
        (0, "In your working copy of the Business Case, add the Options Considered and Evaluation section for the Accounting System (Ledgerline).", {"bold": True}),
        (0, "Remember to:"),
        (1, "State the workload/requirements an option must satisfy (from your gap table + migration reqs)."),
        (1, "Lay out Option A (renew on-prem) and Option B (migrate to cloud)."),
        (1, "Pick an evaluation method; assess each option's impact (vs objectives) and difficulty."),
        (0, "~½–1 page."),
        (0, "⚠  Evaluate, don't decide — the recommendation comes later.", {"color": A1, "mark_color": A1}),
    ], "~20 min, then we discuss", accent=A1)
    k.takeaways_slide(prs, pg(), "Section 1 · Options & evaluation", [
        "Compare realistic options on a level field — always include the status-quo.",
        "Define the workload/requirements first; options are judged against it.",
        "Evaluate on stated criteria: impact vs objectives + implementation difficulty.",
        "This is evaluation, not the decision.",
    ], accent=A1)

    # ===== C2 — Cost-Benefit Analysis =====
    k.divider_slide(prs, "02", "Cost-Benefit Analysis", "put a number on it", A2)
    t1.visual_slide(prs, pg(), "Put a number on it", "", [
        (0, "A CBA compares the options in money, over time — here, 5 years."),
        (0, "It turns “cloud feels cheaper” into evidence — or disproves it."),
        (0, "The board decides on total cost + benefit, not a monthly price.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], [], A2)
    t1.visual_slide(prs, pg(), "What a good CBA contains", "becomes §7 + Appendix 1", [
        (0, "Assumptions → per-option 5-year costs → benefits (incl. avoided downtime) → comparison → sensitivity."),
        (0, "Compare like-for-like over the same horizon."),
        (0, "State every assumption — an unstated assumption is a hole in the case.",
            {"bold": True, "color": A2, "mark_color": A2}),
        (0, "Detailed line items go in Appendix 1; the section shows the summary."),
    ], [], A2)
    t1.visual_slide(prs, pg(), "Costing the on-prem option (Option A)", "", [
        (0, "Option A = renew / keep on-prem. Cost it from the operational-costing facts:"),
        (1, "capex (server refresh) + opex (power, maintenance, licences, admin time), over 5 years"),
        (0, "Watch software licensing (Windows / SQL Server) — it rides on BOTH options; don't drop it.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], [], A2)
    # --- AWS ACF M02 S20 — Pricing Calculator (screenshot → placeholder) ---
    t1.visual_slide(prs, pg(), "AWS Pricing Calculator", "size the cloud option before you build it", [
        (0, "Use it to:"),
        (1, "estimate monthly costs and find ways to reduce them"),
        (1, "model a solution before building it"),
        (1, "find instance types & contract terms; group services into an estimate"),
        (0, "calculator.aws", {"italic": True, "color": k.GREY1}),
    ], ["AWS Pricing Calculator — screenshot"], A2)
    # --- AWS ACF M02 S22 — hands-on estimate activity ---
    k.activity_slide(prs, pg(), "Build a cost estimate", [
        (0, "In groups, use the AWS Pricing Calculator + the supplied specifications to build a cost estimate for the cloud option.", {"bold": True}),
        (0, "Remember to:"),
        (1, "Size the Accounting System's compute, storage, database and data transfer."),
        (1, "Name your estimate; group the services; capture the monthly + annual figures."),
        (1, "Be ready to report your findings back to the class."),
        (0, "This estimate feeds your CBA (Option B).", {"color": A2, "mark_color": A2}),
        (0, "🔗  calculator.aws", {"color": k.GREY1}),
    ], "~20 min, then report back", accent=A2)
    t1.visual_slide(prs, pg(), "Assembling the CBA — compare & test it", "the part the calculator doesn't do", [
        (0, "5-year comparison summary: Option A vs Option B, like-for-like."),
        (0, "Avoided-downtime benefit — value the reliability gain, don't just assert it."),
        (0, "Sensitivity: which one or two assumptions would flip the answer?"),
        (0, "A CBA with no sensitivity check reads as overconfident.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], [], A2)
    k.activity_slide(prs, pg(), "Build the 5-year CBA", [
        (0, "In your working copy of the Business Case, add the Cost-Benefit Analysis (§7) + Appendix 1 for the Accounting System.", {"bold": True}),
        (0, "Remember to:"),
        (1, "Cost Option A (renew on-prem) from the operational-costing doc."),
        (1, "Size Option B using your Pricing Calculator estimate."),
        (1, "State assumptions; build the 5-year comparison; add avoided-downtime + a sensitivity note."),
        (0, "~1 page + Appendix 1 line items."),
        (0, "⚠  Like-for-like, same horizon; every figure traceable to an assumption or source.", {"color": A2, "mark_color": A2}),
    ], "~30 min, then we compare", accent=A2)
    k.takeaways_slide(prs, pg(), "Section 2 · Cost-Benefit Analysis", [
        "A CBA compares options in money over a fixed horizon — total cost + benefit, not a monthly price.",
        "State every assumption; detail goes in Appendix 1.",
        "Size the cloud option with the Pricing Calculator; assemble the comparison yourself.",
        "Always include avoided-downtime benefit and a sensitivity check.",
    ], accent=A2)

    # ===== C3 — Risk & impact =====
    k.divider_slide(prs, "03", "Risk & impact", "what money doesn't capture", A3)
    t1.visual_slide(prs, pg(), "Money isn't the whole story", "", [
        (0, "Two options can cost the same and carry very different risk."),
        (0, "Risk & Impact is the qualitative complement to the CBA:"),
        (1, "the intangibles, and the things that could go wrong"),
    ], [], A3)
    t1.visual_slide(prs, pg(), "Intangibles comparison", "what a dollar figure misses", [
        (0, "Name the qualitative factors, per option:"),
        (1, "staff skills / learning curve · vendor lock-in · agility & scalability"),
        (1, "security posture · business continuity · disruption during change"),
        (0, "The cheaper option may carry the bigger intangible cost.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], [], A3)
    t1.visual_slide(prs, pg(), "The risk register", "", [
        (0, "For the direction you're heading, list the real risks:"),
        (1, "Risk → Likelihood → Impact → Mitigation"),
        (0, "Keep it specific to this migration: data-migration error, cutover downtime, cost overrun, skills gap."),
        (0, "A risk with no mitigation is just a worry; a mitigation makes it manageable.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], [], A3)
    k.activity_slide(prs, pg(), "Add the Risk & Impact assessment", [
        (0, "In your working copy of the Business Case, add the Risk and Impact Assessment (§8) for the Accounting System.", {"bold": True}),
        (0, "Remember to:"),
        (1, "Compare the intangibles of Option A vs Option B."),
        (1, "Build a risk register (risk → likelihood → impact → mitigation) for the cloud direction."),
        (0, "~½–1 page."),
        (0, "⚠  Specific risks with real mitigations — not generic “things might go wrong”.", {"color": A3, "mark_color": A3}),
    ], "~20 min, then we discuss", accent=A3)
    k.takeaways_slide(prs, pg(), "Section 3 · Risk & impact", [
        "Cost isn't everything — compare the intangibles too.",
        "A risk register: risk → likelihood → impact → mitigation, specific to this change.",
        "Together with the CBA, this is the full evidence base for a decision.",
    ], accent=A3)

    # ===== Close =====
    s = prs.slides.add_slide(prs.slide_layouts[6])
    k._bg(s, k.CHAR)
    k._rect(s, Inches(0), Inches(0), Inches(0.45), Inches(7.5), fill=k.GOLD)
    tb, tf = k._box(s, Inches(1.0), Inches(1.6), Inches(11.5), Inches(4.4))
    p = k._para(tf, True)
    k._run(p, "From evidence to decision", 40, k.WHITE, bold=True, font=k.FONT_BOLD)
    for txt in [
        "You've built the evidence: options laid out, costed over 5 years, risks weighed.",
        "That's the analytical core of a business case — everything a board needs to choose.",
        "You still haven't recommended — that's the next move.",
        "Next: make the call, justify it, and turn it into an action plan.",
    ]:
        pp = tf.add_paragraph(); pp.space_before = Pt(12); pp.line_spacing = 1.05
        k._run(pp, txt, 19, "E8E8E8", font=k.FONT_LT)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    prs.save(out_path)
    print(f"Wrote {out_path} ({len(prs.slides._sldIdLst)} slides)")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
