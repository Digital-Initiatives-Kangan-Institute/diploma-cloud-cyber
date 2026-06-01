#!/usr/bin/env python3
"""Topic 1 (Intro to Cloud) — authored into Kangan-branded layouts, like the Topic 2 build.

Topic 1 mixes bespoke text with AWS slides carrying images/diagrams. Rather than re-skin the
old deck (which mis-sized text and dropped rasters), this AUTHORS Topic 1 fresh into the clean
Kangan layouts and drops a labelled PLACEHOLDER box wherever a visual belongs — raster image or
native vector diagram alike. Images are transferred in manually afterwards.

Content faithful to Topic_01_Slides.pptx (titles, bullets, tables, section structure).
Brand: documentaion/kangan-branding.md. Reuses helpers from build_kangan_topic_deck.

Usage:  python scripts/build_kangan_topic1_deck.py [output.pptx]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_kangan_topic_deck as k   # noqa: E402

from pptx.util import Inches, Pt, Emu  # noqa: E402
from pptx.dml.color import RGBColor  # noqa: E402
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR  # noqa: E402
from pptx.enum.shapes import MSO_SHAPE  # noqa: E402
from pptx.oxml.ns import qn  # noqa: E402

OUT_DEFAULT = "S1-CL1-Cloud-Design-Build/delivery/topic_01/Topic_01_Kangan_experiment.pptx"

# section accents (Topic 2 convention extended to 5 sections)
A1, A2, A3, A4, A5 = k.MAGENTA, k.SKY, k.GREEN, k.NAVY, k.GOLD_DK


def placeholder(slide, l, t, w, h, label, accent=k.GOLD_DK):
    box = k._rect(slide, l, t, w, h, fill="FBF6E6", line=accent,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    ln = box.line._get_or_add_ln()
    ln.append(ln.makeelement(qn('a:prstDash'), {'val': 'dash'}))
    tb, tf = k._box(slide, l, t, w, h, anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    k._run(p, "🖼", 30, accent, font=k.FONT_BOLD)
    p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER; p2.space_before = Pt(4)
    k._run(p2, "IMAGE", 12, accent, bold=True, font=k.FONT_BOLD)
    p3 = tf.add_paragraph(); p3.alignment = PP_ALIGN.CENTER; p3.space_before = Pt(2)
    k._run(p3, label, 12, k.GREY1, italic=True, font=k.FONT_LT)


def _title_block(prs, title, kicker, accent):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    k._bg(s, k.WHITE)
    tb, tf = k._box(s, Inches(0.7), Inches(0.5), Inches(11.9), Inches(1.05))
    p = k._para(tf, True)
    k._run(p, title, 28, k.CHAR, bold=True, font=k.FONT_BOLD)
    if kicker:
        pk = tf.add_paragraph(); pk.space_before = Pt(2)
        k._run(pk, kicker, 17, k.GOLD_DK, italic=True, font=k.FONT_LT)
    k._rect(s, Inches(0.72), Inches(1.5), Inches(1.6), Pt(4), fill=accent)
    return s


def visual_slide(prs, pageno, title, kicker, bullets, images, accent):
    """Content slide with 0..3 labelled image placeholders + bullets."""
    s = _title_block(prs, title, kicker, accent)
    n = len(images)
    if n == 0:
        tb, tf = k._box(s, Inches(0.72), Inches(1.85), Inches(11.9), Inches(4.9))
        k._bullets(tf, bullets, base_size=18)
    elif n == 1:
        if bullets:
            tb, tf = k._box(s, Inches(0.72), Inches(1.9), Inches(6.0), Inches(4.7))
            k._bullets(tf, bullets, base_size=17)
            placeholder(s, Inches(7.0), Inches(1.95), Inches(5.6), Inches(4.4), images[0], accent)
        else:
            placeholder(s, Inches(2.7), Inches(1.95), Inches(7.9), Inches(4.5), images[0], accent)
    elif n == 2:
        if bullets:
            tb, tf = k._box(s, Inches(0.72), Inches(1.85), Inches(11.9), Inches(1.3))
            k._bullets(tf, bullets, base_size=16)
            ytop = Inches(3.35)
        else:
            ytop = Inches(2.1)
        placeholder(s, Inches(0.9), ytop, Inches(5.5), Inches(3.3), images[0], accent)
        placeholder(s, Inches(6.9), ytop, Inches(5.5), Inches(3.3), images[1], accent)
    else:  # 3 across
        if bullets:
            tb, tf = k._box(s, Inches(0.72), Inches(1.85), Inches(11.9), Inches(1.0))
            k._bullets(tf, bullets, base_size=16)
            ytop = Inches(3.0)
        else:
            ytop = Inches(2.2)
        xs = [Inches(0.72), Inches(4.42), Inches(8.12)]
        for x, lab in zip(xs, images):
            placeholder(s, x, ytop, Inches(3.6), Inches(3.4), lab, accent)
    k._footer(s, pageno, accent=accent)
    return s


def build(out_path):
    prs = k.Presentation()
    prs.slide_width = k.EMU_W; prs.slide_height = k.EMU_H
    n = [0]
    def pg(): n[0] += 1; return n[0]

    # ===== Title =====
    k.title_slide(prs, "01", "Intro to Cloud", "Speak ‘cloud’ well enough to write a business case")

    # ===== Section 1 — Cloud literacy (accent A1) =====
    visual_slide(prs, pg(), "Cloud literacy", "the consultant's starting kit", [
        (0, "Goal: speak “cloud” well enough to write a business case."),
        (0, "Where this fits: you're an MTS cloud consultant — before advising “renew on-prem vs move to cloud,” you need to speak cloud fluently."),
        (0, "What you'll be able to do: name the building blocks, classify service & deployment models, point to the right standards, and reason about cost."),
        (0, "Where the edges are: recognise, explain, classify — not build. Building comes in a later engagement.", {"bold": True, "color": A1, "mark_color": A1}),
        (0, "How you'll practise: on a real YAT system — the Accounting System (Ledgerline)."),
    ], [], A1)

    visual_slide(prs, pg(), "Our scenario: the Accounting System (Ledgerline)", "the engagement on your desk", [
        (0, "YAT runs Ledgerline — its accounting and office-admin system. Your engagement: look at moving it to the cloud."),
        (0, "A cloud version would take a familiar shape:"),
        (1, "Internet → ALB → EC2 / Auto Scaling Group  (Ledgerline app, Windows Server)"),
        (1, "→ RDS for SQL Server"),
        (1, "(+ S3 for scanned invoices/POs · CloudWatch monitoring)"),
        (0, "Don't worry about the names yet — you'll learn each piece this Topic.", {"bold": True, "color": A1, "mark_color": A1}),
        (0, "Every exercise from here uses this system, so the picture builds as you go."),
    ], [], A1)

    k.activity_slide(prs, pg(), "Get to know your client — YAT", [
        (0, "Open the YAT website & intranet and look around — this is where your client's information lives all term.", {"bold": True}),
        (0, "Find answers to:"),
        (1, "What kind of organisation is YAT — what does it do, and roughly how big is it?"),
        (1, "What does YAT already use in the cloud today?"),
        (1, "What is Ledgerline used for, and who relies on it?"),
        (1, "Where does Ledgerline run today, and on what kind of infrastructure?"),
        (1, "What does the business expect of it — e.g. when must it be available?"),
    ], "~10 min, then we'll share what we found", accent=A1)

    visual_slide(prs, pg(), "What is cloud computing?", "", [], ["opening illustration — what does ‘cloud’ mean to you?"], A1)

    visual_slide(prs, pg(), "Cloud computing defined", "", [
        (0, "Cloud computing is the on-demand delivery of compute power, database, storage, applications and other IT resources via the internet, with pay-as-you-go pricing.", {"bold": True}),
        (0, "Those resources run on servers in large data centres around the world."),
        (0, "You provision what you need, when you need it, and pay only for what you use."),
    ], ["cloud / data-centre illustration"], A1)

    visual_slide(prs, pg(), "Infrastructure as software", "", [
        (0, "Cloud computing lets you stop thinking of infrastructure as hardware — and instead think of (and use) it as software."),
    ], ["infrastructure AS HARDWARE", "infrastructure AS SOFTWARE"], A1)

    visual_slide(prs, pg(), "Traditional computing model", "infrastructure as hardware", [
        (0, "Hardware solutions:"),
        (1, "require space, staff, physical security, planning, capital expenditure"),
        (1, "have a long hardware procurement cycle"),
        (1, "make you provision capacity by guessing the theoretical maximum peak"),
    ], ["traditional (on-prem hardware) model diagram"], A1)

    visual_slide(prs, pg(), "Cloud computing model", "infrastructure as software", [
        (0, "Software solutions:"),
        (1, "are flexible"),
        (1, "change more quickly, easily and cost-effectively than hardware"),
        (1, "eliminate the undifferentiated heavy lifting"),
    ], ["cloud computing model diagram"], A1)

    visual_slide(prs, pg(), "Cloud computing deployment models", "where an application runs", [],
                 ["Cloud", "Hybrid", "On-premises (private cloud)"], A1)

    visual_slide(prs, pg(), "Deployment models — YAT's situation", "", [
        (0, "YAT today is hybrid: on-prem servers in the comms room + Office 365 (SaaS) already in the cloud."),
        (0, "The engagement on your desk is a straight one: move an on-prem system into the public cloud."),
        (0, "So public cloud is the model that matters here — know private and hybrid as context, not as the choice.", {"bold": True, "color": A1, "mark_color": A1}),
        (0, "The real question isn't “which of four models” — it's “keep this system on-prem, or move it to public cloud?”"),
    ], [], A1)

    k.activity_slide(prs, pg(), "Which deployment model?", [
        (0, "YAT is considering moving Ledgerline off its on-prem server.", {"bold": True}),
        (0, "Which deployment model fits a cloud version of Ledgerline — and why is that the right fit for YAT?"),
        (0, "Write one short paragraph: name the model, then justify it (think about who YAT is, what it already runs, and how much it wants to manage)."),
    ], "~5 min, then we compare", accent=A1)

    k.takeaways_slide(prs, pg(), "Section 1 · Cloud literacy", [
        "Cloud computing = on-demand IT resources over the internet, pay-as-you-go.",
        "It lets you treat infrastructure as software, not hardware.",
        "Three deployment models: cloud · hybrid · on-premises (private cloud).",
        "For YAT the real choice is binary: keep on-prem, or move to public cloud.",
    ], accent=A1)

    # ===== Section 2 — Service Models (A2) =====
    k.divider_slide(prs, "02", "Service models", "who manages what", A2)
    visual_slide(prs, pg(), "Cloud service models", "a spectrum of control", [
        (0, "IaaS — infrastructure as a service", {"bold": True}),
        (0, "PaaS — platform as a service", {"bold": True}),
        (0, "SaaS — software as a service", {"bold": True}),
        (0, "IaaS → SaaS = more control / more work  →  less control / less work.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], ["service-model spectrum (control vs effort)"], A2)
    visual_slide(prs, pg(), "Service models — who manages what", "", [
        (0, "IaaS (e.g. EC2) — you manage the OS and the app; the provider handles the hardware → most control, most work. Preserve an existing stack."),
        (0, "PaaS (e.g. RDS, ALB) — the provider runs the platform; you run your app/data → less control, far less ops. Offload work when cloud skills are thin."),
        (0, "SaaS (e.g. Office 365) — the provider runs everything; you just use it → least control, least work."),
        (0, "Choosing = control vs operational burden. Classify each part, then say why that level fits the client.",
            {"bold": True, "color": A2, "mark_color": A2}),
    ], [], A2)
    k.activity_slide(prs, pg(), "Classify the service models", [
        (0, "For each, name the service model and say why:", {"bold": True}),
        (1, "Office 365"),
        (1, "A VPS that comes with an OS installed, which you then configure and run your software on"),
        (1, "A service that lets you rent compute & memory and install your own OS and software"),
        (1, "A managed database service where the provider runs, patches and backs up the engine, and you just connect and store data"),
    ], "~8 min, then we compare", accent=A2)
    k.takeaways_slide(prs, pg(), "Section 2 · Service models", [
        "Three models: IaaS → PaaS → SaaS — handing over more control for less effort.",
        "IaaS = you manage the OS up · PaaS = provider runs the platform · SaaS = you just use it.",
        "The deciding question is always “who manages the OS / the platform?”",
        "Choosing isn't “best” — it's control vs operational burden for this client.",
    ], accent=A2)

    # ===== Section 3 — Core AWS Services (A3) =====
    k.divider_slide(prs, "03", "Core AWS services", "the building blocks", A3)
    visual_slide(prs, pg(), "What is AWS?", "", [
        (0, "A secure cloud platform offering a broad set of global cloud-based products."),
        (0, "On-demand access to compute, storage, network, database and other IT resources — plus the tools to manage them."),
        (0, "You pay only for the services you use, for as long as you use them."),
        (0, "AWS services work together like building blocks.", {"bold": True, "color": A3, "mark_color": A3}),
    ], [], A3)
    visual_slide(prs, pg(), "Selecting a Region", "where your services and data live", [
        (0, "Choose a Region based on:"),
        (1, "data governance & legal requirements"),
        (1, "proximity to users (latency)"),
        (1, "which services are available in the Region"),
        (1, "cost (varies by Region)"),
    ], [], A3)
    visual_slide(prs, pg(), "Availability Zones", "isolated, within a Region", [
        (0, "Each Region has multiple Availability Zones."),
        (0, "Each AZ is a fully isolated partition of the AWS infrastructure:"),
        (1, "discrete data centres, designed for fault isolation"),
        (1, "interconnected by high-speed private networking"),
        (1, "you choose your AZs; replicate across them for resiliency"),
    ], ["Availability Zones diagram (AWS)"], A3)
    visual_slide(prs, pg(), "AWS categories of services", "", [], ["AWS service categories graphic (AWS)"], A3)
    visual_slide(prs, pg(), "Compute", "service category", [
        (0, "Amazon EC2 · EC2 Auto Scaling"),
        (0, "Amazon ECS · EKS · ECR · Fargate"),
        (0, "AWS Elastic Beanstalk · AWS Lambda"),
    ], ["compute illustration / icon"], A3)
    visual_slide(prs, pg(), "Storage", "service category", [
        (0, "Amazon EBS — block storage for EC2"),
        (0, "Amazon EFS — managed file system"),
        (0, "Amazon S3 — object storage"),
        (0, "Amazon S3 Glacier — archive / long-term backup"),
    ], ["storage illustration / icon"], A3)
    visual_slide(prs, pg(), "Database", "service category", [
        (0, "Amazon RDS — managed relational database"),
        (0, "Amazon Aurora — MySQL/PostgreSQL-compatible"),
        (0, "Amazon DynamoDB — key-value / document"),
        (0, "Amazon Redshift — analytics / data warehouse"),
    ], ["database illustration / icon"], A3)
    visual_slide(prs, pg(), "Networking & content delivery", "service category", [
        (0, "Amazon VPC — isolated virtual network"),
        (0, "Elastic Load Balancing · Route 53 (DNS)"),
        (0, "Amazon CloudFront — content delivery"),
        (0, "AWS Direct Connect · Transit Gateway · VPN"),
    ], ["networking illustration / icon"], A3)
    visual_slide(prs, pg(), "How the pieces fit — the web-app pattern", "the Ledgerline sketch wasn't random", [
        (0, "Internet → ALB → EC2 / Auto Scaling Group → RDS  (+ S3, CloudWatch)",
            {"bold": True, "color": A3, "mark_color": A3}),
        (0, "ALB — spreads incoming traffic across servers · PaaS"),
        (0, "EC2 + Auto Scaling Group — the app tier; runs the app, scales with demand · IaaS"),
        (0, "RDS — managed database (here, SQL Server) · PaaS"),
        (0, "S3 — object storage (scanned invoices/POs) · EBS — disks on the EC2 servers"),
        (0, "CloudWatch — monitors all of the above"),
    ], [], A3)
    visual_slide(prs, pg(), "Activity: AWS Management Console", "educator-led clickthrough", [
        (0, "We'll log in to the AWS Management Console together."),
        (0, "You'll answer five questions as we navigate; we discuss and reveal each answer."),
    ], ["AWS Management Console illustration"], A3)
    visual_slide(prs, pg(), "Hands-on: Console clickthrough", "", [
        (0, "Launch the Sandbox environment and connect to the AWS Management Console."),
        (0, "Open the Services menu — notice services are grouped into categories (EC2 → Compute)."),
        (1, "Q1: which category is the IAM service under?"),
        (1, "Q2: which category is Amazon VPC under?"),
        (0, "Open VPC; switch the Region menu (e.g. to EU (London)); open Subnets, select one."),
        (1, "Q3: does a subnet exist at Region level or Availability-Zone level?"),
        (1, "Q4: does a VPC exist at Region level or AZ level?"),
        (1, "Q5: which are global, not Regional — EC2, IAM, Lambda, Route 53?"),
    ], [], A3)
    visual_slide(prs, pg(), "Activity answer key", "", [
        (0, "Q1 — IAM → Security, Identity & Compliance."),
        (0, "Q2 — Amazon VPC → Networking & Content Delivery."),
        (0, "Q3 — subnets exist at the Availability-Zone level."),
        (0, "Q4 — VPCs exist at the Region level."),
        (0, "Q5 — IAM and Route 53 are global; EC2 and Lambda are Regional.",
            {"bold": True, "color": A3, "mark_color": A3}),
    ], [], A3)
    k.takeaways_slide(prs, pg(), "Section 3 · Core AWS services", [
        "AWS groups services into categories — compute, storage, database, networking…",
        "Web-app building blocks: EC2 (compute) · S3/EBS (storage) · RDS (database) · ALB/VPC (networking).",
        "Regions and Availability Zones decide where services run — for residency and resilience.",
        "They assemble into one shape: Internet → ALB → EC2/ASG → RDS (+ S3, CloudWatch).",
        "At this stage: name each service and its role — not build it.",
    ], accent=A3)

    # ===== Section 4 — Industry standards (A4) =====
    k.divider_slide(prs, "04", "Industry technology standards", "standards that inform a migration", A4)
    visual_slide(prs, pg(), "The AWS Well-Architected Framework", "", [
        (0, "A guide for designing infrastructure that is:"),
        (1, "secure · high-performing · resilient · efficient"),
        (0, "A consistent way to evaluate and improve cloud architectures."),
        (0, "Best practices drawn from reviewing thousands of customer architectures."),
    ], ["Well-Architected — the six pillars (AWS)"], A4)
    k.table_slide(prs, pg(), "Standards that inform a migration", "each guides a different decision",
                  ["Standard", "What it is", "Informs…"],
                  [["NIST SP 800-145", "The definition of IaaS / PaaS / SaaS", "service-model choices"],
                   ["AWS Well-Architected", "Six design pillars (incl. Reliability)", "design quality + how you improve it"],
                   ["ISO/IEC 27017", "Cloud-specific security controls", "security decisions"],
                   ["ACSC Essential Eight", "Australian baseline cyber mitigations", "security controls / compliance"],
                   ["ITIL 4", "Service-management practices", "change-management alignment"]],
                  accent=A4, col_widths=[3.0, 5.2, 3.7],
                  note="You're not implementing these — you're naming the right standard for a given decision.")
    k.activity_slide(prs, pg(), "Which standard informs the decision?", [
        (0, "For each decision, name the standard and give a one-line why:", {"bold": True}),
        (1, "Deciding whether each part of a solution is IaaS, PaaS or SaaS"),
        (1, "Choosing the cloud security controls for a system"),
        (1, "Meeting an Australian baseline of cyber mitigations"),
        (1, "Judging whether an architecture is well-designed and reliable"),
        (1, "Planning the change-management around a migration"),
    ], "~8 min, then we compare", accent=A4)
    k.takeaways_slide(prs, pg(), "Section 4 · Industry standards", [
        "A migration is informed by several standards — each guides a different decision.",
        "NIST → service models · Well-Architected → design quality · ISO 27017 → cloud security · Essential Eight → AU baseline · ITIL 4 → change management.",
        "Well-Architected's Reliability pillar comes back when you design for real.",
        "The skill now is recognising the right standard for a decision, not implementing it.",
    ], accent=A4)

    # ===== Section 5 — Cost models (A5) =====
    k.divider_slide(prs, "05", "Cloud cost models & economics", "why a migration is a cost conversation", A5)
    visual_slide(prs, pg(), "AWS pricing model", "three fundamental cost drivers", [
        (0, "Compute — charged per hour/second, varies by instance type.", {"bold": True}),
        (0, "Storage — charged typically per GB.", {"bold": True}),
        (0, "Data transfer — outbound is aggregated and charged; inbound is mostly free.", {"bold": True}),
    ], [], A5)
    visual_slide(prs, pg(), "How do you pay for AWS?", "", [
        (0, "Pay for what you use."),
        (0, "Pay less when you reserve."),
        (0, "Pay less when you use more, and as AWS grows."),
    ], ["AWS pricing philosophy graphic (AWS)"], A5)
    visual_slide(prs, pg(), "Pay less when you reserve", "Reserved Instances (RIs)", [
        (0, "Invest in Reserved Instances — save up to 75%."),
        (0, "Options (more upfront = bigger discount):"),
        (1, "All Upfront (AURI) — largest discount"),
        (1, "Partial Upfront (PURI) — lower discount"),
        (1, "No Upfront (NURI) — smallest discount"),
    ], ["Reserved Instance options graphic (AWS)"], A5)
    visual_slide(prs, pg(), "AWS Pricing Calculator", "model the cost before you build", [
        (0, "Estimate monthly costs and find ways to reduce them."),
        (0, "Model solutions before building them; explore the calculations behind an estimate."),
        (0, "Find instance types & contract terms; group services to organise an estimate."),
    ], ["AWS Pricing Calculator — screenshot"], A5)
    visual_slide(prs, pg(), "Reading an estimate", "", [
        (0, "An estimate is broken into three figures:"),
        (1, "First 12 months total"),
        (1, "Total upfront"),
        (1, "Total monthly"),
    ], [], A5)
    k.table_slide(prs, pg(), "Match the pricing model to the workload", "cost follows the shape of demand",
                  ["Workload profile", "Best-fit pricing"],
                  [["Predictable, always-on baseline", "Reserved Instances (commit, pay less)"],
                   ["Variable / peaky", "On-demand or autoscaling"],
                   ["Interruptible, can be retried", "Spot (cheapest — not for production baseline)"],
                   ["Storage & data", "Pay-as-you-go (scales with usage)"]],
                  accent=A5, col_widths=[5.9, 6.0],
                  note="Watch licensing: a Windows + SQL Server system carries software-licence cost on top of infrastructure — easy to miss.")
    visual_slide(prs, pg(), "Additional benefit considerations", "hard and soft benefits", [
        (0, "Hard benefits:", {"bold": True}),
        (1, "lower spend on compute, storage, networking, security"),
        (1, "fewer hardware/software purchases (capex); lower ops, backup & DR costs"),
        (0, "Soft benefits:", {"bold": True}),
        (1, "reuse of services; higher developer productivity"),
        (1, "improved customer satisfaction; agility; greater reach"),
    ], [], A5)
    k.takeaways_slide(prs, pg(), "Section 5 · Cost models", [
        "Three cost drivers: compute · storage · data transfer.",
        "Three ways to pay: pay-as-you-go · reserve (commit for less) · pay-less-as-you-grow.",
        "Match pricing to the workload — baseline→reserved, peaky→on-demand, storage→pay-as-you-go.",
        "Don't forget software licensing (e.g. Windows / SQL Server) on top of infrastructure.",
        "Cost grows roughly with demand — that's why moving a system is a cost conversation.",
    ], accent=A5)

    # ===== Close =====
    s = prs.slides.add_slide(prs.slide_layouts[6])
    k._bg(s, k.CHAR)
    k._rect(s, Inches(0), Inches(0), Inches(0.45), Inches(7.5), fill=k.GOLD)
    tb, tf = k._box(s, Inches(1.0), Inches(1.6), Inches(11.5), Inches(4.4))
    p = k._para(tf, True)
    k._run(p, "From literacy to the job", 40, k.WHITE, bold=True, font=k.FONT_BOLD)
    for txt in [
        "You can now classify deployment and service models, name the building blocks, point to the right standard, and reason about cost.",
        "That's the literacy a consultant needs before recommending whether to move a system to the cloud.",
        "Next, you'll put it to work — weighing the options and making the case for a real migration.",
        "You practised on the Accounting System; the same skills carry to whatever engagement lands on your desk.",
    ]:
        pp = tf.add_paragraph(); pp.space_before = Pt(12); pp.line_spacing = 1.05
        k._run(pp, txt, 18, "E8E8E8", font=k.FONT_LT)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    prs.save(out_path)
    print(f"Wrote {out_path} ({len(prs.slides._sldIdLst)} slides)")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT_DEFAULT
    build(out)
