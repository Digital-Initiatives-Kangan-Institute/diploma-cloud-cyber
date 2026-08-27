#!/usr/bin/env python3
"""Shared rendering primitives for the S1-CL1 workbook instruments.

A workbook instrument is ONE definition rendered two ways:

  student   the blank sheet the student works through — the job, empty capture tables,
            empty screenshot boxes, empty response boxes. No UoC tags.
  assessor  the worked copy: every screenshot box replaced by a terracotta description of
            what should be in it, every response box filled with a teal model answer, each
            element tagged with the UoC items it evidences, and each carrying the standard
            it is actually marked against.

These are the pieces both AT2 and AT3 draw on. They were lifted verbatim from
`at2_run_sheet.py`, which keeps its own copies until the session working on it lands; when
it does, it imports from here and the duplicates go. Everything AT3 needed on top —
`design_table`, `diagram_slot`, `standard_line` — is new here.

The marking model these support: a settings table is context, not the standard. The tags on
`Evidences:` say which UoC items an element carries; the `Satisfactory when:` line says what
has to be true for them to be met. An assessor marks the second, never the table.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # noqa: E402
sys.path.insert(0, str(next(d / "scripts" for d in Path(__file__).resolve().parents if (d / "scripts" / "helpers" / "__init__.py").exists())))  # noqa: E402
from helpers.docx_styling import set_cell_borders, shade_cell  # noqa: E402
from helpers.instrument_layout import add_hyperlink  # noqa: E402
from brand import CREAM, GREY, TEAL, TERRACOTTA  # noqa: E402

from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Pt, Cm, RGBColor  # noqa: E402

BODY_PT = 10.5
UOC = "6B6660"          # muted — the assessor-only traceability line
CAPTURE = TERRACOTTA    # exemplar: what the screenshot should have shown
MODEL = TEAL            # exemplar: the model written answer

__all__ = [
    "BODY_PT", "UOC", "CAPTURE", "MODEL", "GREY", "TEAL", "CREAM", "add_hyperlink",
    "p", "settings_table", "design_table", "box", "screenshot_slot", "diagram_slot",
    "response_slot", "flag", "code", "note", "clicks", "assessor_note", "steps",
    "uoc_line", "standard_line",
]


def p(doc, text, size=BODY_PT, bold=False, italic=False, colour=None, indent=None, after=None):
    par = doc.add_paragraph()
    if indent:
        par.paragraph_format.left_indent = Cm(indent)
    if after is not None:
        par.paragraph_format.space_after = Pt(after)
    r = par.add_run(text)
    r.font.size = Pt(size); r.bold = bold; r.italic = italic
    if colour:
        r.font.color.rgb = RGBColor.from_string(colour)
    return par


def settings_table(doc, settings):
    """A given (label, value) table — what the student builds to. Values are supplied."""
    t = doc.add_table(rows=0, cols=2)
    for label, value in settings:
        cells = t.add_row().cells
        set_cell_borders(cells[0]); set_cell_borders(cells[1]); shade_cell(cells[0], CREAM)
        lr = cells[0].paragraphs[0].add_run(label); lr.bold = True; lr.font.size = Pt(9.5)
        cells[1].paragraphs[0].add_run(value).font.size = Pt(9.5)
        cells[0].width = Cm(4.2); cells[1].width = Cm(11.6)
    doc.add_paragraph()


def design_table(doc, columns, rows, mode, blank_rows=3):
    """A capture table the STUDENT fills in — the inverse of settings_table.

    `rows` are the model answers, shown teal in the assessor copy. The student copy shows
    the same grid with empty cells, `blank_rows` of them (or as many as the model has,
    whichever is greater), so there is visibly room to answer.
    """
    n = max(blank_rows, len(rows)) if mode != "assessor" else len(rows)
    t = doc.add_table(rows=0, cols=len(columns))
    hdr = t.add_row().cells
    for i, col in enumerate(columns):
        set_cell_borders(hdr[i]); shade_cell(hdr[i], CREAM)
        r = hdr[i].paragraphs[0].add_run(col); r.bold = True; r.font.size = Pt(9)
    body = rows if mode == "assessor" else [[""] * len(columns)] * n
    for row in body:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            set_cell_borders(cells[i])
            r = cells[i].paragraphs[0].add_run(str(val)); r.font.size = Pt(9)
            if mode == "assessor":
                r.font.color.rgb = RGBColor.from_string(MODEL)
    doc.add_paragraph()


def box(doc, lines):
    """A bordered drop-zone. `lines` is a list of (text, colour_or_None, bold, italic)."""
    t = doc.add_table(rows=1, cols=1)
    cell = t.rows[0].cells[0]
    set_cell_borders(cell); shade_cell(cell, CREAM); cell.width = Cm(16.6)
    for i, (text, colour, bold, italic) in enumerate(lines):
        par = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER if colour is None else WD_ALIGN_PARAGRAPH.LEFT
        r = par.add_run(text)
        r.font.size = Pt(9.5 if colour else 10); r.bold = bold; r.italic = italic
        if colour:
            r.font.color.rgb = RGBColor.from_string(colour)
    doc.add_paragraph()


def screenshot_slot(doc, capture, mode):
    if mode == "assessor":
        box(doc, [(f"SCREENSHOT — {capture}", CAPTURE, False, True)])
    else:
        box(doc, [("[ PASTE YOUR SCREENSHOT HERE ]", None, True, False),
                  (capture, GREY, False, True)])


def diagram_slot(doc, what, mode):
    """A drawing area. Works on paper or on screen — sketch it or paste it."""
    if mode == "assessor":
        box(doc, [(f"DIAGRAM — {what}", CAPTURE, False, True)])
    else:
        box(doc, [("[ SKETCH OR PASTE YOUR DIAGRAM HERE ]", None, True, False),
                  (what, GREY, False, True)])


def response_slot(doc, model, mode, points=None):
    """Blank box for the student; for the assessor either a model answer or key points."""
    if mode != "assessor":
        box(doc, [("[ WRITE YOUR ANSWER HERE ]", None, True, False)])
        return
    if points:
        lines = [("Key points the answer should touch on:", MODEL, True, False)]
        lines += [(f"•  {pt}", MODEL, False, False) for pt in points]
        box(doc, lines)
    else:
        box(doc, [(model, MODEL, False, False)])


def flag(doc, text):
    """A small teal label above a heading — the thing a student quotes when they are stuck."""
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(10)
    par.paragraph_format.space_after = Pt(0)
    r = par.add_run(text.upper())
    r.bold = True; r.font.size = Pt(8)
    r.font.color.rgb = RGBColor.from_string(TEAL)


def code(doc, lines):
    """A verbatim block — monospace, shaded, for anything the student must copy exactly."""
    t = doc.add_table(rows=1, cols=1)
    cell = t.rows[0].cells[0]
    set_cell_borders(cell); shade_cell(cell, CREAM); cell.width = Cm(16.6)
    for i, line in enumerate(lines):
        par = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        par.paragraph_format.space_after = Pt(0)
        r = par.add_run(line)
        r.font.name = "Consolas"; r.font.size = Pt(9)
    doc.add_paragraph()


def note(doc, text):
    """An environment-constraint note — set apart from the task, in the accent colour."""
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(0.4)
    par.paragraph_format.space_before = Pt(4)
    par.paragraph_format.space_after = Pt(8)
    lead = par.add_run("Environment constraint ")
    lead.bold = True; lead.font.size = Pt(9.5)
    lead.font.color.rgb = RGBColor.from_string(TERRACOTTA)
    r = par.add_run(text)
    r.italic = True; r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor.from_string(TERRACOTTA)


def clicks(doc, items):
    """Click-by-click detail. The practice sheet has this; the assessment deliberately does not."""
    p(doc, "How to do it", bold=True, after=3)
    for i, step in enumerate(items, 1):
        par = doc.add_paragraph()
        par.paragraph_format.left_indent = Cm(0.6)
        par.paragraph_format.space_after = Pt(2)
        lead = par.add_run(f"{i}.  "); lead.bold = True; lead.font.size = Pt(10)
        par.add_run(step).font.size = Pt(10)
    doc.add_paragraph()


def assessor_note(doc, text, mode):
    """Guidance for the assessor only — never rendered in the student copy."""
    if mode != "assessor":
        return
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(0.4)
    par.paragraph_format.space_before = Pt(4)
    par.paragraph_format.space_after = Pt(8)
    lead = par.add_run("Assessor note ")
    lead.bold = True; lead.font.size = Pt(9.5)
    lead.font.color.rgb = RGBColor.from_string(MODEL)
    r = par.add_run(text)
    r.italic = True; r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor.from_string(MODEL)


def steps(doc, items):
    for i, step in enumerate(items, 1):
        par = doc.add_paragraph()
        par.paragraph_format.left_indent = Cm(0.6)
        par.paragraph_format.space_after = Pt(3)
        lead = par.add_run(f"{i}.  "); lead.bold = True; lead.font.size = Pt(BODY_PT)
        par.add_run(step).font.size = Pt(BODY_PT)
    doc.add_paragraph()


def uoc_line(doc, items, mode):
    """The assessor-only traceability line under an element's heading."""
    if mode != "assessor":
        return
    p(doc, "Evidences: " + " · ".join(f"[{u}]" for u in items),
      size=9, italic=True, colour=UOC, after=2)


def standard_line(doc, text, mode):
    """What the element is actually marked against — the UoC intent, not the supplied values.

    Every settings table in this instrument contains values we invented so the student has a
    concrete task. This line names which of them are load-bearing. An assessor marks this,
    never the table.
    """
    if mode != "assessor":
        return
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(6)
    lead = par.add_run("Satisfactory when ")
    lead.bold = True; lead.font.size = Pt(9)
    lead.font.color.rgb = RGBColor.from_string(UOC)
    r = par.add_run(text)
    r.italic = True; r.font.size = Pt(9)
    r.font.color.rgb = RGBColor.from_string(UOC)
