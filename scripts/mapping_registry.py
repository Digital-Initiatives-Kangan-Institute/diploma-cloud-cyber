"""Course mapping registry — the course/semester-specific data the generic mapping engine consumes.

Lives in the content repo; the generic engine (`mapping/generate_mapping_doc.py`) imports it, so the
same engine builds any course's Assessment Mapping docs. Swap this file per course — everything here is
this course's data, nothing is engine logic. See docs/mapping-document-standard.md.

Three things the engine needs from a course:
  QUALIFICATION  — the qualification code + title stamped on every mapping doc.
  UNIT_PREFIXES  — the unit-code prefixes this course's units use (drives tag parsing).
  CLUSTERS       — the per-cluster registry: which builder packages hold the assessor benchmarks +
                   FS/AC maps, the cluster dirs, AT counts, and the FS/AC source policy.
"""

QUALIFICATION = dict(code="ICT50220", title="Diploma of Information Technology")

# Unit-code prefixes used by this course's units (S1 Cloud: ICTCLD/ICTICT/BSBXTW). A future course
# supplies its own (e.g. S2 Cyber adds ICTCYS/ICTSAS).
UNIT_PREFIXES = ["ICTCLD", "ICTICT", "BSBXTW"]

# Per-cluster registry. Data (benchmarks, FS_MAP, AC_MAP, UNITS, titles, paths) is sourced from the
# per-cluster builder modules; only policy lives here.
CLUSTERS = {
    "cl1": dict(
        # Legacy cluster: no invertible assessor benchmark — the mapping comes from the hand-authored
        # DATA_* dicts (synthesised into a direct inversion). Titles are reproduced from the committed
        # docs so regeneration only fixes the structural artefacts (401 AC block-row; 517 PE split).
        pkg="s1_cl1", cluster_dir="S1-CL1-Cloud-Design-Build", n_ats=3,
        build_mod="build_s1_cl1_mapping_docs", source="data",
        fs_source="benchmark_then_map", ac_source="benchmark_then_map",
        at_titles=["AT1 – Business Case", "AT2 - Deployment", "AT3 – High Availability"],
        unit_titles={
            "ICTCLD401": "Configure cloud services",
            "ICTCLD502": "Design and implement highly-available cloud infrastructure",
            "ICTICT517": "Match ICT needs with the strategic direction of the organisation",
        },
    ),
    "cl2": dict(
        pkg="s1_cl2", cluster_dir="S1-CL2-Cloud-Disaster-Recovery", n_ats=2,
        assessors=["build_s1_cl2_at1_assessor", "build_s1_cl2_at2_assessor"],
        build_mod="build_s1_cl2_mapping_docs",
        # FS comes from the benchmarks, which tag foundation skills on the tasks that exercise
        # them, and falls back to FS_MAP only where they don't. AC stays map-only: the
        # benchmarks don't tag assessment conditions — those are instrument Conditions (C1…Cn).
        fs_source="benchmark_then_map", ac_source="map_only",
    ),
    "cl3": dict(
        pkg="s1_cl3", cluster_dir="S1-CL3-Cloud-Infrastructure-Improvement", n_ats=3,
        assessors=["build_s1_cl3_at1_assessor", "build_s1_cl3_at2_assessor",
                   "build_s1_cl3_at3_assessor"],
        build_mod="build_s1_cl3_mapping_docs",
        fs_source="benchmark_then_map", ac_source="benchmark_then_map",
    ),
}
