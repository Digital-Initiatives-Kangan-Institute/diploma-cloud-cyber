#!/usr/bin/env python3
"""S1-CL2 Assessment Mapping docs — THIN WRAPPER (cluster data + delegation only).

================================================================================
⚠  NOT the canonical generator. The docx-building mechanics live in the shared engine
   ┖─ scripts/mapping/generate_mapping_doc.py  ← the single generator for ALL clusters.
   This module now keeps only S1-CL2's *data* (UNITS, FS_MAP, AC_MAP, AT titles) and the
   benchmark *inversion* the validator reads; build_unit() just calls engine.build_cluster("cl2").
   • To (re)generate:   python scripts/mapping/generate_mapping_doc.py --build cl2
   • To add a NEW cluster: add a CLUSTERS entry in the engine — do NOT copy this script's shape.
   • Contract + pipeline: docs/mapping-document-standard.md
   invert_benchmarks() returns the inversion already split by AT, the same shape the CL3 module
   uses and the shape the engine and the mapping-doc validator both consume.
================================================================================

Build the S1-CL2 per-UoC Assessment Mapping docx files (ICTCLD501/503/505).

Mirrors the CL1 mapping docs: the institutional "Assessment Mapping Tool" template,
filled with each unit's items (Details, AT descriptions, and the AC/PC/PE/KE/FS rows in
the description columns) and the AT1/AT2 columns carrying the criterion code(s) that
evidence each item.

Two data sources, both already in the repo (no hand-typed UoC text):
  * item text + order  — parsed from units_of_competency/<UNIT>_Complete_R1.md
  * item -> AT/criterion — inverted from the AT1 + AT2 assessor benchmarks
    (build_s1_cl2_at1_assessor.BENCHMARK, build_s1_cl2_at2_assessor.BENCHMARK), with FS/AC
    handled with judgement (the benchmarks don't tag AC, and FS coverage is partial).

Staged: `--dump <unit>` prints the parsed items + the inverted mapping for review;
generation of the docx is layered on once the data checks out.

USAGE:
    python scripts/s1_cl2/build_s1_cl2_mapping_docs.py --dump 501
    python scripts/s1_cl2/build_s1_cl2_mapping_docs.py --dump all
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_s1_cl2_at1_assessor as a1   # noqa: E402
import build_s1_cl2_at2_assessor as a2   # noqa: E402

REPO = Path(__file__).resolve().parents[2]  # scripts/s1_cl2/ -> content repo root
UOC = REPO / "S1-CL2-Cloud-Disaster-Recovery" / "units_of_competency"
MAPPINGS = REPO / "S1-CL2-Cloud-Disaster-Recovery" / "mappings"
TEMPLATE = REPO / "kangan-templates" / "Assessment Mapping Tool.docx"

AT1_TITLE = "Cloud Expansion: Design & DR Plan"
AT2_TITLE = "Cloud Microservice & IaC Implementation"

# FS closest-fit map (CL1 precedent: map to where the skill is genuinely exercised;
# the assessor instruments are NOT updated to claim these — noted inconsistency).
# Reading/Writing -> document/review criteria; Oral comm -> presentation/sign-off;
# Self-management/Planning/Problem solving -> the design/analysis/troubleshoot criteria.
FS_MAP = {
    "ICTCLD501": {
        "Reading": {"AT1": "B1"},
        "Oral communication": {"AT1": "C6"},
        "Self-management": {"AT1": "B8"},
        "Planning and organising": {"AT1": "B12"},
        "Problem solving": {"AT1": "B5"},
    },
    "ICTCLD503": {
        "Reading": {"AT1": "A3", "AT2": "D2"},
        "Writing": {"AT1": "A11, A13", "AT2": "D13"},
        "Problem solving": {"AT1": "A8", "AT2": "D5"},
        "Self-management": {"AT1": "A7", "AT2": "D8"},
    },
    "ICTCLD505": {
        "Oral communication": {"AT2": "D11"},
        "Reading": {"AT2": "D2"},
        "Writing": {"AT2": "D10, D13"},
        "Problem solving": {"AT2": "D5"},
        "Self-management": {"AT2": "D8"},
    },
}

# AC -> assessment Conditions map (ACs map to the instrument Conditions / scenario
# access, not the marking criteria). One entry per AC in source order. The final
# assessor-requirement AC is the tick row.
AC_MAP = {
    "ICTCLD501": [
        {"AT1": "C1"},          # data to assess risk events (scenario)
        {"AT1": "C1"},          # legislation applicable (scenario / residency reqs)
        {"AT1": "C2"},          # reporting standards for the DR plan (templates)
        {"AT1": "✓"},      # assessor requirement
    ],
    "ICTCLD503": [
        {"AT1": "C3", "AT2": "C2"},   # cloud vendor service provider (lab)
        {"AT1": "C3", "AT2": "C2"},   # cloud managed database service (lab)
        {"AT2": "C2"},                # cloud serverless environment (lab; build = AT2)
        {"AT2": "C3"},                # pre-prepared code elements (provided artefacts)
        {"AT1": "C1", "AT2": "C1"},   # information and data sources (scenario)
        {"AT1": "C3", "AT2": "C2"},   # IDE (lab)
        {"AT1": "C1", "AT2": "C1"},   # specific requirements / standards (scenario)
        {"AT1": "C3", "AT2": "C2"},   # internet and web browser (lab)
        {"AT1": "C1", "AT2": "C1"},   # data re user requirements (scenario)
        {"AT1": "✓", "AT2": "✓"},  # assessor requirement
    ],
    "ICTCLD505": [
        {"AT2": "C2"},          # cloud vendor service provider (lab)
        {"AT2": "C2"},          # IaC service (lab)
        {"AT2": "C1"},          # specific requirements / standards (scenario)
        {"AT2": "C1"},          # information and data sources (scenario)
        {"AT2": "C2"},          # IDE (lab)
        {"AT2": "C2"},          # internet and web browser (lab)
        {"AT2": "C2"},          # SSH / RDP client (lab)
        {"AT2": "C2"},          # cloud console / SDK / CLI (lab)
        {"AT2": "✓"},      # assessor requirement
    ],
}

UNITS = {
    "501": ("ICTCLD501", "Develop cloud disaster recovery plans"),
    "503": ("ICTCLD503", "Implement web-scale cloud infrastructure"),
    "505": ("ICTCLD505", "Implement cloud infrastructure with code"),
}


# ----------------------------------------------------------------------------
# Source .md parser
# ----------------------------------------------------------------------------

def _sections(text):
    """Split the markdown into {heading: body} by top-level '# ' headings."""
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^#\s+(.*)", line)
        if m:
            if cur is not None:
                out.setdefault(cur, "\n".join(buf))
            cur, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if cur is not None:
        out.setdefault(cur, "\n".join(buf))
    return out


def _bullets(body):
    """Return top-level '- ...' items in order. Indented sub-bullets are folded
    into their parent item (parent + children), matching the consolidated-UoC
    discipline of quoting a nested KE as a single item under the parent's tag."""
    items = []
    for ln in body.splitlines():
        stripped = ln.strip()
        if not stripped.startswith("- "):
            continue
        text = re.sub(r"^-\s+", "", stripped).strip()
        indented = len(ln) - len(ln.lstrip()) > 0
        if indented and items:
            items[-1] = items[-1] + "\n  - " + text
        else:
            items.append(text)
    return items


def parse_source_unit(unit_code):
    text = (UOC / f"{unit_code}_Complete_R1.md").read_text(encoding="utf-8")
    secs = _sections(text)

    # --- PCs: Elements & Performance Criteria table ---
    pcs = []          # [(pc_num, pc_text, element_text)]
    epc = secs.get("Elements and Performance Criteria", "")
    for ln in epc.splitlines():
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        elem, pc_cell = cells[0], cells[1]
        if elem.upper().startswith("ELEMENTS") or elem.startswith("Elements describe"):
            continue
        if not re.match(r"^\d+\.", elem):
            continue
        for piece in pc_cell.split("<br>"):
            piece = piece.strip()
            m = re.match(r"^(\d+\.\d+)\s+(.*)", piece)
            if m:
                pcs.append((m.group(1), m.group(2).strip(), elem))

    # --- FS: Foundation Skills table ---
    fss = []          # [(skill, description)]
    fsec = secs.get("Foundation Skills", "")
    for ln in fsec.splitlines():
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        skill, desc = cells[0], cells[1]
        if skill.upper() == "SKILL" or not skill or skill.startswith("---"):
            continue
        fss.append((skill, desc.replace("<br>", " ")))

    # --- PE / KE: bullets ---
    pes = _bullets(secs.get("Performance Evidence", ""))
    kes = _bullets(secs.get("Knowledge Evidence", ""))

    # --- AC: access bullets + the assessor-requirements statement ---
    acsec = secs.get("Assessment Conditions", "")
    acs = _bullets(acsec)
    for ln in acsec.splitlines():
        if ln.strip().lower().startswith("assessors of this unit must satisfy"):
            acs.append(ln.strip())
    return {"pcs": pcs, "fss": fss, "pes": pes, "kes": kes, "acs": acs}


# ----------------------------------------------------------------------------
# Benchmark inverter: (unit, section, item) -> set of criterion codes
# ----------------------------------------------------------------------------

def _expand(section, numbering):
    """Expand a numbering fragment into individual item ids."""
    out = []
    for part in numbering.split(","):
        part = part.strip().replace("–", "-").replace("—", "-")
        if not part:
            continue
        if "-" in part and section != "FS":
            a, b = (x.strip() for x in part.split("-", 1))
            if section == "PC" and "." in a and "." in b:
                ea, ia = a.split("."); eb, ib = b.split(".")
                if ea == eb:
                    out += [f"{ea}.{i}" for i in range(int(ia), int(ib) + 1)]
                else:
                    out += [a, b]
            else:
                try:
                    out += [str(i) for i in range(int(a), int(b) + 1)]
                except ValueError:
                    out += [a, b]
        else:
            out.append(part)
    return out


def _parse_tags(s):
    """Yield (unit, section, item) from a benchmark UoC string (inherits unit prefix)."""
    cur_unit = None
    for m in re.finditer(r"\[([^\]]+)\]", s):
        inner = m.group(1).strip()
        um = re.match(r"(ICTCLD\d{3})\s+(.*)", inner)
        if um:
            cur_unit, rest = um.group(1), um.group(2)
        else:
            rest = inner
        sm = re.match(r"(PC|PE|KE|AC|FS)\s+(.*)", rest)
        if not sm or cur_unit is None:
            continue
        section, numbering = sm.group(1), sm.group(2).strip()
        if section == "FS":
            yield (cur_unit, "FS", numbering)
        else:
            for item in _expand(section, numbering):
                yield (cur_unit, section, item)


AT_BENCHMARKS = [("AT1", a1), ("AT2", a2)]


def invert_benchmarks():
    """Return {(unit, section, item): {'AT1': [criteria...], 'AT2': [...]}}.

    Split by AT at the source, from which assessor's benchmark a criterion came out of. This
    used to return one flat list per item and leave the split to `_split_codes()`, which
    inferred the AT from the criterion code's first letter (A/B/C meant AT1, D meant AT2). That
    made a criterion code carry hidden meaning: renaming AT2's criteria silently emptied its
    column in every mapping document, and the mapping-doc validator reported the documents as
    wrong when they were right. The AT is knowable here, so it is recorded rather than encoded.

    Same shape as the CL3 module's, which is the model to follow for new clusters.
    """
    out = {}
    for at, mod in AT_BENCHMARKS:
        for _part_title, rows in mod.BENCHMARK:
            for cid, uoc in rows:
                for tag in _parse_tags(uoc):
                    d = out.setdefault(tag, {"AT1": [], "AT2": []})
                    if cid not in d[at]:
                        d[at].append(cid)
    return out


# ----------------------------------------------------------------------------
# Dump (verification)
# ----------------------------------------------------------------------------

def dump(unit_key):
    code, title = UNITS[unit_key]
    items = parse_source_unit(code)
    inv = invert_benchmarks()
    print(f"\n================  {code}  {title}  ================")
    print(f"counts: PC={len(items['pcs'])} FS={len(items['fss'])} "
          f"PE={len(items['pes'])} KE={len(items['kes'])} AC={len(items['acs'])}")

    def codes_for(section, item):
        by_at = inv.get((code, section, item), {})
        both = [f"{at}:{', '.join(c)}" for at in ("AT1", "AT2") if (c := by_at.get(at))]
        return "  ".join(both) or "-- (unmapped)"

    print("\n-- PCs --")
    for num, txt, _elem in items["pcs"]:
        print(f"  {num:<5} [{codes_for('PC', num):<12}] {txt[:70]}")
    print("\n-- PEs --")
    for i, txt in enumerate(items["pes"], 1):
        print(f"  PE{i}  [{codes_for('PE', str(i)):<12}] {txt[:70]}")
    print("\n-- KEs --")
    for i, txt in enumerate(items["kes"], 1):
        print(f"  KE{i}  [{codes_for('KE', str(i)):<12}] {txt[:70]}")
    print("\n-- FSs --")
    for skill, _desc in items["fss"]:
        print(f"  [{codes_for('FS', skill):<12}] {skill}")
    print("\n-- ACs --")
    for i, txt in enumerate(items["acs"], 1):
        print(f"  AC{i}  {txt[:80]}")


# ----------------------------------------------------------------------------
# docx generation — delegated to the shared engine (scripts/mapping/generate_mapping_doc.py).
# This module supplies the data (UNITS, FS_MAP, AC_MAP, titles) + the inversion the engine and the
# validator read. The docx-building mechanics are the engine's, one code path for all clusters.
# ----------------------------------------------------------------------------


def build_unit(unit_key):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mapping"))
    import generate_mapping_doc as engine  # noqa: E402
    code = UNITS[unit_key][0]
    for out in engine.build_cluster("cl2", only=[code]):
        print(f"Wrote {out}")


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--build":
        targets = ["501", "503", "505"] if sys.argv[2] == "all" else [sys.argv[2]]
        for t in targets:
            build_unit(t)
        return
    if len(sys.argv) >= 3 and sys.argv[1] == "--dump":
        targets = ["501", "503", "505"] if sys.argv[2] == "all" else [sys.argv[2]]
        for t in targets:
            dump(t)
    else:
        print("Usage: build_cl2_mapping_docs.py --dump {501|503|505|all}")
        sys.exit(2)


if __name__ == "__main__":
    main()
