#!/usr/bin/env python3
"""Build the YAT / MTS Deployment Report template for the LMS foundation build (.docx).

A deployment-report template scoped to ONE deployment — the YAT LMS foundation build — holding
exactly and only the sections that deployment requires. Split from the generic superset template
(build_deployment_report_template.py), which stays in place for other deployments.

What a foundation build does not have, and so is not in here: a maintenance window (§3.1),
cross-Region backup (§4.9), failure/resize simulation, availability measurement and the findings
and adjustments that follow from them (§6.5-§6.9), a stakeholder feedback record, a sign-off
block, and an appendix of configuration exports. The feedback record and sign-off go because no AT2
marking criterion looks at them; the exports go because the Appendix A screenshots already evidence
the same performance item. Nothing carries an "Applicability / mark Not applicable" note — every
section in this template is a section the report needs.

[TBD - needs discussion: the Appendix A / B / C evidence lists. The AT2 marking criteria name
counts (17 screenshots, 7 exports, 6 test-evidence items) that no artefact enumerates and that no
version of this template has ever carried. The lists are to be derived from the review of what the
assessment actually asks the student to do, once that review is complete; until then the
appendices carry the generic examples inherited from the superset template.]

Usage:  python scripts/templates/build_at2_deployment_report_template.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # content-repo scripts/ (brand + registry)  # noqa: E402
sys.path.insert(0, str(next(d / "scripts" for d in Path(__file__).resolve().parents if (d / "scripts" / "helpers" / "__init__.py").exists())))  # umbrella scripts/ (engine)  # noqa: E402
from helpers.docx_body_text import add_guidance_text, add_response_placeholder  # noqa: E402
from helpers.docx_callouts import add_convention_box  # noqa: E402
from helpers.docx_styling import add_field, paragraph_bottom_rule, set_cell_borders, shade_cell  # noqa: E402
from helpers.docx_tables import add_template_table  # noqa: E402
from brand import ADDRESS, CREAM, GREY, TEAL  # noqa: E402
from helpers.scenario_document import build_header_footer, configure_styles, wordmark  # noqa: E402

from build_deployment_report_template import KE_AT2, REFLECT_AT2  # noqa: E402

from docx import Document  # noqa: E402
from docx.enum.section import WD_SECTION  # noqa: E402
from docx.enum.table import WD_TABLE_ALIGNMENT  # noqa: E402
from docx.shared import Pt, Cm, RGBColor  # noqa: E402

# Course-side note styling — the same violet convention the Business Case template uses for
# anything addressed to the student rather than to the reader of the finished report.
NOTE = "6A3EA1"
NOTE_PT = 9.0

SUPPLIED_NOTE = ("Supplied — this section is already written for you. It is part of your report: "
                 "leave the text below as it is. Delete this note before you submit.")

# §2 and §3 are the same for every consultant on this engagement — the engagement, the
# stakeholders, the predecessor work and the scope all come from the approved design. They are
# supplied rather than written, so nothing here is student work.
ENGAGEMENT_CONTEXT = [
    "This deployment is the foundation-build phase of the YAT College Learning Management System "
    "(LMS) migration to AWS, carried out by MTS under the engagement agreed following the LMS "
    "Replacement Business Case. The board approved the action plan set out in that business case, "
    "and this phase implements the first stage of it.",
    "MTS Senior Architecture and YAT IT subsequently produced the YAT LMS Cloud Architecture — "
    "Baseline Design, approved by Pat Lin (MTS Senior Consultant) and Sam Walker (YAT IT Manager). "
    "That design is the specification this deployment implements; where it leaves a decision to the "
    "implementer, the decision and its rationale are recorded in §5.",
    "On completion the infrastructure is handed to YAT in-house IT, who are responsible for "
    "installing the LMS application, migrating the database, and running the cutover. Hardening the "
    "environment for high availability is a separate, later phase.",
]

SCOPE_IN = [
    "Identity and access management — groups, users, MFA enforcement and instance roles",
    "Network topology — the VPC, its subnets, gateways and route tables",
    "Compute — the launch template, EC2 instances and the Auto Scaling group",
    "Load balancing — the application load balancer, its target group and listener",
    "Database — the managed relational database instance",
    "Storage — the EBS volumes and S3 buckets, with encryption and public-access settings",
    "Security — the tiered security-group model and encryption in transit and at rest",
    "Monitoring — the baseline alarm set",
]

SCOPE_DEFERRED = [
    "Multi-availability-zone database deployment",
    "Resilience across availability zones",
    "Failure and resize simulation, and the availability measurement that goes with it",
    "Cross-Region backup and replication",
    "Disaster-recovery runbooks",
    "The high-availability-tuned monitoring set",
]

SCOPE_EXCLUDED = [
    "LMS application installation on the infrastructure built here",
    "Migration of the existing database content",
    "Cutover from the legacy environment, and the change management around it",
    "Ongoing application support after handover",
]


def add_supplied_note(doc):
    """The violet course-side marker that heads a supplied (pre-written) section."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(SUPPLIED_NOTE)
    r.italic = True
    r.font.size = Pt(NOTE_PT)
    r.font.color.rgb = RGBColor.from_string(NOTE)


def add_supplied_body(doc, text):
    """A paragraph of supplied report content — normal body styling, not guidance styling."""
    p = doc.add_paragraph()
    p.add_run(text).font.size = Pt(10.5)
    return p


def add_supplied_bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(item).font.size = Pt(10.5)


def build(path):
    doc = Document()
    configure_styles(doc)

    sec = doc.sections[0]
    sec.page_height = Cm(29.7); sec.page_width = Cm(21.0)
    sec.top_margin = Cm(2.6); sec.bottom_margin = Cm(2.2)
    sec.left_margin = Cm(2.2); sec.right_margin = Cm(2.2)
    sec.header_distance = Cm(1.0); sec.footer_distance = Cm(1.0)
    build_header_footer(sec)

    # ---- COVER ----
    wordmark(doc.add_paragraph())
    ar = doc.add_paragraph().add_run(ADDRESS)
    ar.font.size = Pt(9); ar.font.color.rgb = RGBColor.from_string(GREY)
    paragraph_bottom_rule(doc.add_paragraph(), TEAL, sz=12)
    for _ in range(3):
        doc.add_paragraph()
    doc.add_paragraph(style="Title").add_run("Deployment Report")
    sub = doc.add_paragraph().add_run("[ Deployment / engagement name ]")
    sub.font.size = Pt(15); sub.italic = True; sub.font.color.rgb = RGBColor.from_string(GREY)
    doc.add_paragraph()

    cover_rows = [
        ("Engagement", "[ Engagement name ]"),
        ("Engagement reference", "[ Reference ]"),
        ("Report version", "[ e.g. v1.0 ]"),
        ("Prepared by", "[ Consultant name ]"),
        ("Consultant role", "[ Role, e.g. MTS Consultant ]"),
        ("Date submitted", "[ DD/MM/YYYY ]"),
        ("Submitted to", "[ Acceptance authority / sponsor ]"),
        ("Related documents", "[ e.g. the approved design this report implements ]"),
        ("Classification", "Commercial-in-confidence"),
    ]
    ct = doc.add_table(rows=0, cols=2)
    ct.alignment = WD_TABLE_ALIGNMENT.LEFT
    for k, v in cover_rows:
        cells = ct.add_row().cells
        set_cell_borders(cells[0]); set_cell_borders(cells[1]); shade_cell(cells[0], CREAM)
        kr = cells[0].paragraphs[0].add_run(k); kr.bold = True; kr.font.size = Pt(10)
        vr = cells[1].paragraphs[0].add_run(v); vr.font.size = Pt(10); vr.italic = True
        vr.font.color.rgb = RGBColor.from_string(GREY)
        cells[0].width = Cm(4.5); cells[1].width = Cm(12.0)

    # ---- CONTENTS + convention ----
    doc.add_section(WD_SECTION.NEW_PAGE); build_header_footer(doc.sections[-1])
    doc.add_paragraph("How to use this template", style="Heading 1")
    add_convention_box(doc, [
        ("Complete every section that asks you for a response.", "Every section in this template "
         "is one the report needs — there is nothing here to skip."),
        ("Two sections are supplied.", "§2 and §3 are already written for you and are part of your "
         "report. Leave them as they are, and delete the violet note above each before you submit."),
        ("Cross-reference your evidence.", "The build narrative and testing sections reference the "
         "screenshots and test evidence captured in the appendices."),
    ])
    doc.add_paragraph("Contents", style="Heading 1")
    add_field(doc.add_paragraph(), 'TOC \\o "1-3" \\h \\z \\u',
              placeholder="Right-click and choose “Update Field” to build the table of contents.")

    # ---- BODY ----
    doc.add_section(WD_SECTION.NEW_PAGE); build_header_footer(doc.sections[-1])
    h1 = lambda t: doc.add_paragraph(t, style="Heading 1")
    h3 = lambda t: doc.add_paragraph(t, style="Heading 3")

    h1("2. Engagement Context")
    add_supplied_note(doc)
    for para in ENGAGEMENT_CONTEXT:
        add_supplied_body(doc, para)

    h1("3. Scope of Deployment")
    add_supplied_note(doc)
    add_supplied_body(doc, "In scope of this deployment:")
    add_supplied_bullets(doc, SCOPE_IN)
    add_supplied_body(doc, "Deferred to the follow-on high-availability phase:")
    add_supplied_bullets(doc, SCOPE_DEFERRED)
    add_supplied_body(doc, "Outside the MTS engagement entirely — YAT in-house IT's responsibility:")
    add_supplied_bullets(doc, SCOPE_EXCLUDED)

    h1("4. Build Narrative")
    add_guidance_text(doc, "A layer-by-layer account of what was built. For each layer, write a short narrative of "
                     "what you stood up, and cross-reference the Appendix A screenshots.")
    for n, title, hint in [
        ("4.1", "Identity and access management (IAM)", "account access, groups/users/roles, MFA, instance profiles"),
        ("4.2", "Network topology", "VPC, subnets, gateways, route tables"),
        ("4.3", "Compute (EC2 + Auto Scaling)", "launch template, instance type + why, ASG min/desired/max + scaling policy"),
        ("4.4", "Load balancing (ALB)", "the load balancer, target group, listener, health check"),
        ("4.5", "Database (RDS)", "instance class + why, engine version, storage, encryption, backups"),
        ("4.6", "Storage (EBS + S3)", "EBS volumes, S3 buckets, encryption, public-access settings"),
        ("4.7", "Security (security groups + encryption)", "the tiered security-group model, encryption in transit + at rest"),
        ("4.8", "Monitoring", "the baseline CloudWatch alarms and thresholds"),
    ]:
        h3(f"{n} {title}")
        add_guidance_text(doc, f"Cover: {hint}. Cross-reference the relevant Appendix A screenshots.")
        add_response_placeholder(doc)

    h1("5. Configuration Decisions")
    add_guidance_text(doc, "The approved design leaves eight decisions to the implementer (design §14). For each, "
                     "state your choice and justify it against the YAT LMS workload described in the LMS "
                     "Application Specification.")
    add_template_table(doc, ["#", "Decision point", "Your decision", "Rationale"],
             [["C1", "EC2 instance type", "[ … ]", "[ concurrent-user load + cost envelope ]"],
              ["C2", "RDS instance class", "[ … ]", "[ database workload characteristics ]"],
              ["C3", "EBS data volume + RDS storage sizing", "[ show the calc ]", "[ current footprint + growth ]"],
              ["C4", "ASG scaling threshold", "[ … ]", "[ expected CPU profile at peak ]"],
              ["C5", "Permission boundary for MTS-Consultants", "[ … ]", "[ … ]"],
              ["C6", "Bastion / RDP design", "[ … ]", "[ security trade-off ]"],
              ["C7", "MySQL engine version", "[ … ]", "[ application compatibility ]"],
              ["C8", "DNS strategy + ACM certificate", "[ … ]", "[ … ]"]],
             widths=[1.0, 6.0, 4.0, 4.5])

    h1("6. Testing and Validation")
    add_guidance_text(doc, "Document the tests run to verify the deployment. For each test, state the test, the "
                     "result, and reference the supporting evidence in Appendix C.")
    h3("6.1 Connectivity tests")
    add_template_table(doc, ["Test", "Outcome (Pass/Fail)", "Notes"],
             [["ALB → EC2 health check", "[ ]", "[ ]"],
              ["EC2 → RDS connection (private)", "[ ]", "[ ]"],
              ["EC2 → internet via NAT", "[ ]", "[ ]"],
              ["RDS not publicly reachable (negative test)", "[ ]", "[ ]"]],
             widths=[7.0, 4.0, 4.5])
    h3("6.2 Autoscaling test")
    add_guidance_text(doc, "Trigger a scaling event (e.g. load against the ALB) and confirm the ASG scales out and "
                     "back in. Cross-reference Appendix C.")
    add_response_placeholder(doc)
    h3("6.3 Database connectivity and basic operations")
    add_guidance_text(doc, "Confirm the database tier is reachable from the app tier over the private network, the "
                     "engine version meets the application requirement, and encryption-in-transit is in place.")
    add_response_placeholder(doc)
    h3("6.4 Infrastructure end-to-end smoke test")
    add_guidance_text(doc, "Confirm the infrastructure is ready to serve traffic (e.g. a placeholder page via the "
                     "ALB DNS returns HTTP 200/302 from a backend instance that can reach the database).")
    add_response_placeholder(doc)

    h1("7. Operational Handover")
    add_guidance_text(doc, "Hand-over information for the team taking over the infrastructure.")
    h3("7.1 Access")
    add_guidance_text(doc, "Who has what access post-handover, MFA enforcement, any IAM group changes.")
    add_response_placeholder(doc)
    h3("7.2 Runbook references")
    add_guidance_text(doc, "Pointers to the design document, naming/tagging conventions, backup arrangements, and "
                     "the alarms list + notification destinations.")
    add_response_placeholder(doc)
    h3("7.3 Known limitations and what's next")
    add_guidance_text(doc, "Be explicit about what is not covered today and what a later phase would add.")
    add_response_placeholder(doc)
    h3("7.4 Documentation filing")
    add_template_table(doc, ["Item", "Filed in", "Reference"],
             [["This Deployment Report", "[ YAT ICT shared documentation ]", "[ ref ]"],
              ["Test evidence (Appendix C)", "[ … ]", "[ ref ]"]],
             widths=[6.5, 5.0, 4.0])
    h1("8. Knowledge Evidence Responses")
    for text, placeholder in KE_AT2:
        add_guidance_text(doc, text)
        add_response_placeholder(doc, placeholder or "[ Write your response here ]")

    # ---- APPENDICES ----
    doc.add_section(WD_SECTION.NEW_PAGE); build_header_footer(doc.sections[-1])
    h1("Appendix A — Build evidence (screenshots)")
    add_guidance_text(doc, "Capture a console screenshot evidencing each component you built, with the region "
                     "indicator visible. List each below and cross-reference it from §4 / §6. Examples:")
    add_template_table(doc, ["#", "Screenshot", "What must be visible"],
             [["A1", "IAM groups / MFA", "[ created groups; MFA enabled ]"],
              ["A2", "VPC subnets", "[ subnets + AZs ]"],
              ["A3", "EC2 instances + ASG", "[ running instances; ASG min/desired/max ]"],
              ["A4", "ALB target group health", "[ healthy targets ]"],
              ["A5", "RDS database", "[ available; encryption ]"],
              ["A6", "CloudWatch alarms / dashboard", "[ the baseline alarms ]"],
              ["…", "[ add as your deployment requires ]", "[ … ]"]],
             widths=[1.0, 5.5, 9.0])
    h1("Appendix C — Test evidence")
    add_guidance_text(doc, "Attach the evidence supporting the results in §6 — screenshots, terminal/log excerpts "
                     "and metric graphs.")
    add_response_placeholder(doc, "[ Test evidence ]")

    reflect_intro, reflect_items = REFLECT_AT2
    h1("Appendix D — Reflections")
    add_guidance_text(doc, reflect_intro)
    for heading, prompt in reflect_items:
        h3(heading)
        add_guidance_text(doc, prompt)
        add_response_placeholder(doc)

    h1("Document control")
    add_template_table(doc, ["Field", "Value"],
             [["Document version", "[ v1.0 ]"],
              ["Author", "[ Name, role ]"],
              ["Engagement", "[ Engagement name ]"],
              ["Date submitted", "[ DD/MM/YYYY ]"],
              ["Distribution", "[ … ]"],
              ["Related documents", "[ the design implemented; predecessor/successor reports ]"]],
             widths=[5.0, 10.5])

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    print(f"Wrote {path}")


if __name__ == "__main__":
    out = Path("../diploma-cloud-cyber-website-s1/public/templates/AT2-Deployment-Report-Template.docx")
    build(out)
