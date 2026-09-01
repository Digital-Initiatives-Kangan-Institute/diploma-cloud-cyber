#!/usr/bin/env python3
"""Build the S1-CL2 AT2 STUDENT instrument (.docx) — the blank half of the pair.

Everything comes from build_s1_cl2_at2_assessor, which holds the single definition of the
content, the front matter and the criteria. This entry point exists so the student copy has its
own script the way every other instrument does.

Usage:  python scripts/s1_cl2/build_s1_cl2_at2_student.py [output.docx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # noqa: E402
import build_s1_cl2_at2_assessor as a  # noqa: E402

if __name__ == "__main__":
    default = str(a.CLUSTER / "assessments" / "AT2" /
                  "AT2-Microservice-IaC-Implementation-Student.docx")
    a.build(sys.argv[1] if len(sys.argv) > 1 else default, "student")
