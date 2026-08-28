"""S1-CL1 Assessment Mapping docs — THIN WRAPPER (cluster data + delegation only).

================================================================================
⚠  NOT the canonical generator. The docx-building mechanics live in the shared engine
   ┖─ <umbrella>/scripts/mapping/generate_mapping_doc.py  ← the single generator for ALL clusters.
   CL1 has no single BENCHMARK constant to invert, so the engine drives it from the DATA_* dicts
   below (CLUSTERS "cl1", source:"data"). This module keeps only that data + UNIT_DATA; the
   docx-building mechanics (formerly an in-place edit of a pre-populated docx) are the engine's.
   DATA_* is the generator's INPUT, never the gate's oracle — validate-mapping-doc checks the built
   docx against the three assessors' reverse-map tables instead, so drift here is caught.
   • To (re)generate, from the umbrella root:
       scripts/.venv/bin/python scripts/mapping/generate_mapping_doc.py \
           --registry diploma-cloud-cyber-content-s1/scripts/ --build cl1
   • Contract + pipeline + CL1 conformance status: docs/mapping-document-standard.md
   Full conformance (real machine-readable, UoC-tagged benchmarks in CL1's assessors) is a separate
   retrofit; the CL2/CL3 engine entries are the worked examples of the intended implementation.
================================================================================

DATA_401/502/517 map each PC/PE/KE/FS/AC item to its AT1/AT2/AT3 criterion code(s).

These cells are DERIVED, not authored: each one is the "Evidenced by criterion(ia)" value from the
matching row of the relevant assessor's own reverse-map table (the "UoC coverage verification" tables
in build_s1_cl1_at{1,2,3}_assessor.py). AT1 marks against A1-A14/B1-B8, AT2 against A1-A10, AT3 against
A1-A18; C-codes are assessment-conditions pre-conditions, not marking criteria. When an assessor's
reverse map changes, re-derive these cells from it rather than editing them by hand — the assessor is
the source of truth, and a cell that disagrees with it is a fabricated traceability claim.

USAGE:
    python scripts/s1_cl1/build_s1_cl1_mapping_docs.py {401|502|517|all}   # delegates to the engine
"""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]  # scripts/s1_cl1/ -> content repo root
MAPPINGS = REPO / "S1-CL1-Cloud-Design-Build" / "mappings"

# Column indices in the mapping tables (0-indexed)
# Table 3 (AC): col 0 = description; cols 1,2,3,4,5 = AT1..AT5
# Table 4 (PC): col 0 = element; col 1 = PC; cols 2,3,4,5,6 = AT1..AT5
# Table 5 (PE): col 0 = PE description; cols 1,2,3,4,5 = AT1..AT5
# Table 6 (KE): col 0 = KE description; cols 1,2,3,4,5 = AT1..AT5
# Table 7 (FS): col 0 = skill; col 1 = PC (often empty); col 2 = description;
#                cols 3,4,5,6,7 = AT1..AT5

# -----------------------------------------------------------------------------
# Mapping data: UoC item → {AT1, AT2, AT3} criterion code(s)
# Empty string means "no criterion evidences this in that AT" (cell stays blank).
# -----------------------------------------------------------------------------

DATA_401 = {
    # PC text starts with "X.Y" — match by leading prefix
    "pcs": {
        "1.1": {"AT1": "", "AT2": "A7", "AT3": ""},
        "1.2": {"AT1": "", "AT2": "A6", "AT3": ""},
        "1.3": {"AT1": "", "AT2": "A7", "AT3": ""},
        "1.4": {"AT1": "", "AT2": "A2", "AT3": ""},
        "1.5": {"AT1": "", "AT2": "A2", "AT3": ""},
        "1.6": {"AT1": "", "AT2": "A2", "AT3": ""},
        "1.7": {"AT1": "", "AT2": "A1", "AT3": ""},
        "1.8": {"AT1": "A4", "AT2": "", "AT3": ""},
        "2.1": {"AT1": "", "AT2": "A2", "AT3": ""},
        "2.2": {"AT1": "", "AT2": "A1", "AT3": ""},
        "2.3": {"AT1": "", "AT2": "A3", "AT3": ""},
        "2.4": {"AT1": "", "AT2": "A3", "AT3": ""},
        "2.5": {"AT1": "", "AT2": "A4", "AT3": ""},
        "2.6": {"AT1": "", "AT2": "A8", "AT3": ""},
        "3.1": {"AT1": "", "AT2": "A3", "AT3": ""},
        "3.2": {"AT1": "", "AT2": "A8", "AT3": ""},
        "4.1": {"AT1": "A13, B4", "AT2": "", "AT3": ""},
        "4.2": {"AT1": "B5", "AT2": "", "AT3": ""},
        "4.3": {"AT1": "", "AT2": "A10", "AT3": "A16"},
    },
    # PEs in source order
    "pes": [
        # PE 1 — build at least one simple virtual network
        {"AT1": "", "AT2": "A1", "AT3": ""},
        # PE 2 — configure compute, storage, database, autoscaling
        {"AT1": "", "AT2": "A3, A4", "AT3": ""},
        # PE 3 — conduct simple tests to confirm access
        {"AT1": "", "AT2": "A8", "AT3": ""},
    ],
    # KEs in source order
    "kes": [
        # KE 1 — industry technology standards
        {"AT1": "A5, A11", "AT2": "", "AT3": ""},
        # KE 2 — industry standard hardware/software products
        {"AT1": "A11", "AT2": "", "AT3": ""},
        # KE 3 — IaaS/PaaS/SaaS
        {"AT1": "A11", "AT2": "", "AT3": ""},
        # KE 4 — cost models
        {"AT1": "A5, A11", "AT2": "", "AT3": ""},
        # KE 5 — VM/networking/scaling features
        {"AT1": "", "AT2": "A9", "AT3": ""},
        # KE 6 — vertical/horizontal scaling, db types, storage options
        {"AT1": "", "AT2": "A9", "AT3": ""},
        # KE 7 — shared security responsibility
        {"AT1": "", "AT2": "A9", "AT3": ""},
        # KE 8 — user access protocols
        {"AT1": "", "AT2": "A9", "AT3": ""},
        # KE 9 — security policies and protocols
        {"AT1": "", "AT2": "A9", "AT3": ""},
        # KE 10 — DNS
        {"AT1": "", "AT2": "A9", "AT3": ""},
        # KE 11 — cloud models (on-prem/private/hybrid/public)
        {"AT1": "A11", "AT2": "", "AT3": ""},
    ],
    # FSs keyed by skill name (matches col 0 of Table 7)
    "fss": {
        "Reading": {"AT1": "", "AT2": "A9", "AT3": "A1"},
        "Writing": {"AT1": "", "AT2": "A9", "AT3": "A17"},
        "Learning": {"AT1": "", "AT2": "", "AT3": "A18"},
        "Planning and organising": {"AT1": "", "AT2": "", "AT3": "A7"},
        "Self-management skills": {"AT1": "", "AT2": "", "AT3": "A18"},
    },
    # ACs in source order — short label + per-AT codes; rows inserted into Table 3
    "acs": [
        ("cloud vendor service provider",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("cloud managed database service",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("internet and web browser",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("data to gather information from to determine output and user requirements, including user access and business protocols",
         {"AT1": "C1", "AT2": "C2", "AT3": "C2"}),
        ("Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards",
         {"AT1": "✓", "AT2": "✓", "AT3": "✓"}),
    ],
}

DATA_502 = {
    "pcs": {
        "1.1": {"AT1": "", "AT2": "", "AT3": "A1"},
        "1.2": {"AT1": "A4", "AT2": "", "AT3": ""},
        "1.3": {"AT1": "", "AT2": "A1", "AT3": ""},
        "2.1": {"AT1": "", "AT2": "", "AT3": "A1"},
        "2.2": {"AT1": "", "AT2": "", "AT3": "A2"},
        "2.3": {"AT1": "", "AT2": "", "AT3": "A2"},
        "2.4": {"AT1": "", "AT2": "", "AT3": "A2"},
        "2.5": {"AT1": "", "AT2": "", "AT3": "A3"},
        "3.1": {"AT1": "", "AT2": "", "AT3": "A4"},
        "3.2": {"AT1": "", "AT2": "", "AT3": "A5"},
        "3.3": {"AT1": "", "AT2": "", "AT3": "A5"},
        "3.4": {"AT1": "", "AT2": "", "AT3": "A5"},
        "3.5": {"AT1": "", "AT2": "", "AT3": "A6"},
        "4.1": {"AT1": "", "AT2": "A3", "AT3": "A9"},
        "4.2": {"AT1": "", "AT2": "A8", "AT3": "A11"},
        "4.3": {"AT1": "", "AT2": "A5", "AT3": "A10"},
        "4.4": {"AT1": "", "AT2": "", "AT3": "A12"},
        "4.5": {"AT1": "", "AT2": "", "AT3": "A13"},
        "4.6": {"AT1": "", "AT2": "", "AT3": "A8"},
        "5.1": {"AT1": "", "AT2": "", "AT3": "A14"},
        "5.2": {"AT1": "B6", "AT2": "", "AT3": "A15"},
        "5.3": {"AT1": "A13", "AT2": "", "AT3": ""},
    },
    "pes": [
        # PE 1 — design + implement at least one fault tolerant cloud infra
        {"AT1": "", "AT2": "", "AT3": "A4, A9"},
        # PE 2 — design + deploy automated infrastructure scaling
        {"AT1": "", "AT2": "", "AT3": "A4, A9"},
        # PE 3 — simulate failures + demonstrate fault tolerance
        {"AT1": "", "AT2": "", "AT3": "A12"},
        # PE 4 — use cloud management console / SDK / CLI
        {"AT1": "", "AT2": "", "AT3": "A9"},
        # PE 5 — define, monitor and record resource availability
        {"AT1": "", "AT2": "", "AT3": "A4, A10"},
    ],
    "kes": [
        # KE 1 — industry technology standards
        {"AT1": "A11", "AT2": "", "AT3": ""},
        # KE 2 — industry hardware/software products
        {"AT1": "A11", "AT2": "", "AT3": ""},
        # KE 3 — cloud cost models re scalability
        {"AT1": "A5, A11", "AT2": "", "AT3": ""},
        # KE 4 — HA cloud infra concepts (FT, SPOFs, MTTF/MTTR/MTBF, RTO/RPO, SLAs, scalability)
        {"AT1": "", "AT2": "", "AT3": "A17"},
        # KE 5 — testing and debugging techniques
        {"AT1": "", "AT2": "", "AT3": "A17"},
        # KE 6 — tools and techniques to measure availability impact
        {"AT1": "", "AT2": "", "AT3": "A17"},
        # KE 7 — built-in vs designed fault tolerance
        {"AT1": "", "AT2": "", "AT3": "A17"},
        # KE 8 — load balancing + autoscaling for availability
        {"AT1": "", "AT2": "", "AT3": "A17"},
        # KE 9 — performance monitoring techniques and metrics
        {"AT1": "", "AT2": "", "AT3": "A17"},
    ],
    "fss": {
        "Oral communication": {"AT1": "B8", "AT2": "", "AT3": ""},
        "Reading": {"AT1": "", "AT2": "A1", "AT3": "A1"},
        "Problem solving": {"AT1": "", "AT2": "", "AT3": "A18"},
        "Self-management": {"AT1": "", "AT2": "", "AT3": "A18"},
    },
    "acs": [
        ("cloud vendor service provider",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("cloud managed database service",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("information and data sources required to design and implement cloud infrastructure",
         {"AT1": "C1", "AT2": "C2", "AT3": "C2"}),
        ("integrated development environment (IDE)",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("specific requirements and industry standards, organisational procedures and legislative requirements, including business and functionality requirements, as required",
         {"AT1": "C1", "AT2": "C2", "AT3": "C2"}),
        ("internet and web browser",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("secure shell (SSH) or remote desktop protocol (RDP) client to connect to cloud-hosted instances",
         {"AT1": "", "AT2": "C1", "AT3": "C1"}),
        ("data to gather information from to determine output and user requirements, including user access and business protocols",
         {"AT1": "C1", "AT2": "C2", "AT3": "C2"}),
        ("Assessors of this unit must satisfy the requirements for assessors in applicable vocational education and training legislation, frameworks and/or standards",
         {"AT1": "✓", "AT2": "✓", "AT3": "✓"}),
    ],
}

DATA_517 = {
    "pcs": {
        "1.1": {"AT1": "A1", "AT2": "", "AT3": ""},
        "1.2": {"AT1": "A2", "AT2": "", "AT3": ""},
        "1.3": {"AT1": "A3", "AT2": "", "AT3": ""},
        "1.4": {"AT1": "A10, B1", "AT2": "", "AT3": ""},
        "2.1": {"AT1": "A4, A5, A6", "AT2": "", "AT3": ""},
        "2.2": {"AT1": "A4, A6", "AT2": "", "AT3": ""},
        "2.3": {"AT1": "A7", "AT2": "", "AT3": ""},
        "2.4": {"AT1": "A12, B2", "AT2": "", "AT3": ""},
        "3.1": {"AT1": "A8", "AT2": "", "AT3": ""},
        "3.2": {"AT1": "A8", "AT2": "", "AT3": ""},
        "3.3": {"AT1": "A9, A13, B3", "AT2": "", "AT3": ""},
    },
    # NOTE: 517 PE table is structurally different — the source UoC has one
    # top-level bullet "For one organisation:" with 6 nested sub-bullets,
    # and the mapping docx has a single row containing all 6 sub-bullets
    # joined together. We need to split that single row into 6 per-PE rows
    # (like the AC table). Use the (label, codes) tuple format so the splitter
    # can populate col 0 with the PE text.
    "pes_split": [
        ("interpret a strategic plan and objectives of the organisation",
         {"AT1": "A1", "AT2": "", "AT3": ""}),
        ("evaluate the current state of ICT in the organisation",
         {"AT1": "A2", "AT2": "", "AT3": ""}),
        ("identify possible gaps and opportunities in ICT and evaluate organisational impact with reference to the strategic plan and the objectives",
         {"AT1": "A3", "AT2": "", "AT3": ""}),
        ("determine and prioritise proposed changes to meet organisational needs",
         {"AT1": "A7", "AT2": "", "AT3": ""}),
        ("evaluate the difficulty of implementing proposed changes",
         {"AT1": "A6", "AT2": "", "AT3": ""}),
        ("develop an action plan for implementation",
         {"AT1": "A8", "AT2": "", "AT3": ""}),
    ],
    "kes": [
        # KE 1 — Key sections of an action plan
        {"AT1": "A8, A11", "AT2": "", "AT3": ""},
        # KE 2 — Methods of evaluation and planning approaches
        {"AT1": "A5, A11", "AT2": "", "AT3": ""},
        # KE 3 — Methods of evaluation of competing ICT systems and products
        {"AT1": "A4, A5, A11", "AT2": "", "AT3": ""},
        # KE 4 — Current and emerging trends
        {"AT1": "A11", "AT2": "", "AT3": ""},
    ],
    "fss": {
        "Reading": {"AT1": "A3", "AT2": "", "AT3": ""},
        "Writing": {"AT1": "A14", "AT2": "", "AT3": ""},
        "Oral Communication": {"AT1": "B7", "AT2": "", "AT3": ""},
        "Numeracy": {"AT1": "A5", "AT2": "", "AT3": ""},
        # FSs below were originally unmapped in the AT1 marking guide; mapped to
        # closest-fit AT1 criteria 2026-05-26 per Tim's "avoid changing the
        # assessments at this stage if we can manage it". The AT1 assessor docx
        # criterion UoC columns are NOT updated to claim these — known
        # inconsistency to address in a later pass if needed for audit.
        "Navigate the world of work": {"AT1": "A8", "AT2": "", "AT3": ""},
        "Interact with others": {"AT1": "B5, B6", "AT2": "", "AT3": ""},
        "Get the work done": {"AT1": "A4, A8, A12", "AT2": "", "AT3": ""},
    },
    "acs": [
        ("A site where ICT needs and strategic directions of the organisation are coordinated",
         {"AT1": "C1", "AT2": "", "AT3": ""}),
        ("Detailed information relating to a strategic organisation plan, objectives, and direction",
         {"AT1": "C1", "AT2": "", "AT3": ""}),
        ("Organisational policies and procedures relating to the implementation of ICT changes",
         {"AT1": "C1", "AT2": "", "AT3": ""}),
        ("Individual superior in the organisation",
         {"AT1": "C2", "AT2": "", "AT3": ""}),
        ("Information on current ICT systems and practices in the organisation including operating systems, hardware, and security",
         {"AT1": "C1", "AT2": "", "AT3": ""}),
        ("Assessors of this unit must satisfy the assessor requirements in applicable vocational education and training legislation, frameworks and/or standards",
         {"AT1": "✓", "AT2": "✓", "AT3": "✓"}),
    ],
}

UNIT_DATA = {
    "401": ("ICTCLD401_Assessment_Mapping.docx", DATA_401),
    "502": ("ICTCLD502_Assessment_Mapping.docx", DATA_502),
    "517": ("ICTICT517_Assessment_Mapping.docx", DATA_517),
}
# ----------------------------------------------------------------------------
# docx generation — delegated to the shared engine (scripts/mapping/generate_mapping_doc.py).
# CL1 has no invertible assessor benchmark, so the engine drives it from the DATA_* dicts above
# (synthesised into a direct inversion via the CLUSTERS "cl1" source:"data" path). This module now
# keeps only that data + UNIT_DATA — which the validate-mapping-doc skill reads as CL1's oracle;
# the docx-building mechanics are the engine's, one code path for all clusters.
# ----------------------------------------------------------------------------


def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("401", "502", "517", "all"):
        # The engine moved to the umbrella in the 2026-07-08 restructure; the content repo is
        # cloned inside it, so the umbrella root is the content repo's parent.
        engine_dir = REPO.parent / "scripts" / "mapping"
        if not (engine_dir / "generate_mapping_doc.py").exists():
            sys.exit(f"Shared mapping engine not found at {engine_dir} — run this repo from "
                     f"inside the umbrella, or invoke the engine directly with --registry.")
        sys.path.insert(0, str(engine_dir))
        sys.path.insert(0, str(REPO / "scripts"))  # mapping_registry.py
        import generate_mapping_doc as engine  # noqa: E402
        only = None if sys.argv[1] == "all" else [UNIT_DATA[sys.argv[1]][0].split("_Assessment_Mapping")[0]]
        for out in engine.build_cluster("cl1", only=only):
            print(f"Wrote {out}")
    else:
        print("Usage: build_s1_cl1_mapping_docs.py {401|502|517|all}")
        sys.exit(2)


if __name__ == "__main__":
    main()
