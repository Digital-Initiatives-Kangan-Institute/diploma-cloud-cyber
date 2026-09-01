#!/usr/bin/env python3
"""Build the S1-CL3 AT3 STUDENT instrument (.docx) — the blank half of the pair.

Everything comes from build_s1_cl3_at3_assessor, which holds the single definition of the
content, the front matter and the criteria. This entry point exists so the student copy has its
own script the way every other instrument does.

Usage:  python scripts/s1_cl3/build_s1_cl3_at3_student.py [output.docx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # noqa: E402
import build_s1_cl3_at3_assessor as a  # noqa: E402

if __name__ == "__main__":
    default = str(a.CLUSTER / "assessments" / "AT3" / "AT3-Implement-Student.docx")
    a.build(sys.argv[1] if len(sys.argv) > 1 else default, "student")
