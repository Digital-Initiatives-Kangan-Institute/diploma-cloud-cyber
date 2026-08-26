#!/usr/bin/env python3
"""Build the YAT Business Case board-presentation TEMPLATE (.pptx).

A branded, fillable board-presentation deck mirroring the Business Case document:
title → agenda → context → current state → gap → options → recommendation →
cost → benefits → risks → plan → decision → close. Each content slide carries
greyed guidance the presenter replaces. Branding via pptx_brand (brand-pack §3/§4.3).

Usage:  python scripts/build_bc_deck_template.py [output.pptx]
Default: ../diploma-cloud-cyber-website-s1/public/templates/YAT-Business-Case-Deck-Template.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # content-repo scripts/ (brand + registry)  # noqa: E402
sys.path.insert(0, str(next(d / "scripts" for d in Path(__file__).resolve().parents if (d / "scripts" / "helpers" / "__init__.py").exists())))  # umbrella scripts/ (engine)  # noqa: E402
from helpers import pptx_brand as b  # noqa: E402


def build(path):
    prs = b.new_deck()

    b.add_title_slide(
        prs, "Business Case", "[ Project / initiative name ]",
        ["[ Presenter name, role ]", "[ Date ]   ·   [ Audience — e.g. YAT Board ]"])

    b.add_content_slide(prs, "Agenda", [
        ("Why this matters — strategic context", 0),
        ("Where we are today — current state", 0),
        ("The gap", 0),
        ("Options considered", 0),
        ("Recommendation", 0),
        ("Cost summary", 0),
        ("Risks and mitigation", 0),
        ("Implementation plan", 0),
        ("The decision we're asking for", 0),
    ])

    b.add_content_slide(prs, "Strategic context & alignment", [
        ("State the organisational objectives this initiative serves — cite the strategic plan.", 0),
        ("Note the relevant industry direction, and where the plan aligns or diverges.", 0),
        ("Land the “why this, why now”.", 0),
    ], guidance=True)

    b.add_content_slide(prs, "Current state", [
        ("The system today: platform, condition, availability, recovery.", 0),
        ("The key dependencies and integrations.", 0),
        ("The limitations that motivate the change.", 0),
    ], guidance=True)

    b.add_content_slide(prs, "The gap", [
        ("The handful of gaps between where the organisation wants to be and where it is.", 0),
        ("Keep to the material ones — the board needs the headline, not the full table.", 0),
    ], guidance=True)

    b.add_content_slide(prs, "Options considered", [
        ("Option A — [ one-line description ]", 0),
        ("Option B — [ one-line description ]", 0),
        ("Note any other options considered and why they were set aside.", 0),
    ], guidance=True)

    b.add_statement_slide(
        prs, "Recommendation",
        "[ Your recommendation, in one clear sentence ]",
        "[ The one-line reason the board should back it ]")

    b.add_table_slide(prs, "Cost summary", ["", "Option A", "Option B"],
                      [["5-year cost", "$_____", "$_____"],
                       ["Key quantified benefit", "—", "$_____"],
                       ["Net position", "$_____", "$_____"]],
                      col_widths=[4.5, 3.6, 3.6])

    b.add_content_slide(prs, "Benefits & value", [
        ("The decisive non-cost benefits of the recommended option.", 0),
        ("Tie each one back to an organisational objective.", 0),
    ], guidance=True)

    b.add_content_slide(prs, "Risks & mitigation", [
        ("The top two or three risks of the recommended option.", 0),
        ("For each, the mitigation that makes it acceptable.", 0),
    ], guidance=True)

    b.add_content_slide(prs, "Implementation plan", [
        ("The phases at a glance, with the indicative timeline.", 0),
        ("Flag the key dependency or constraint (e.g. the cutover window).", 0),
    ], guidance=True)

    b.add_statement_slide(
        prs, "The decision we're asking for",
        "[ The decision you are asking the board to approve today ]",
        "[ e.g. approve the option, the action plan, and the Year-1 budget ]")

    b.add_closing_slide(prs, "Questions", "[ Presenter name ]  ·  [ contact ]")

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    prs.save(path)
    print(f"Wrote {path} ({len(prs.slides)} slides)")


if __name__ == "__main__":
    default = "../diploma-cloud-cyber-website-s1/public/templates/YAT-Business-Case-Deck-Template.pptx"
    out = sys.argv[1] if len(sys.argv) > 1 else default
    build(out)
