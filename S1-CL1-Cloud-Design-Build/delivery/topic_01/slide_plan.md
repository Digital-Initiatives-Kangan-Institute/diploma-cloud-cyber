# Topic 01 Intro to Cloud — Slide plan
> **Covers:** Topic 01 — see coverage.md
> **Subtitle:** Speak ‘cloud’ well enough to write a business case

## Slides

### C1 — Cloud fundamentals & deployment models
- Teaches: [ICTCLD401 KE 11]
- [BESPOKE] Cloud literacy
  - Goal: speak “cloud” well enough to write a business case.
  - Where this fits: you're an MTS cloud consultant — before advising “renew on-prem vs move to cloud,” you need to speak cloud fluently.
  - What you'll be able to do: name the building blocks, classify service & deployment models, point to the right standards, and reason about cost.
  - Where the edges are: recognise, explain, classify — not build. Building comes in a later engagement.
  - How you'll practise: on a real YAT system — the Accounting System (Ledgerline).
  kicker: the consultant's starting kit
  image: none
  notes:
    Frame this as the map for the whole Topic — set expectations, don't teach content yet.
    • Goal: read it out — by the end they can "speak cloud well enough to write a business case."
    That business case IS AT1; everything today feeds it.
    • Where this fits: they are MTS consultants advising YAT. Literacy comes before advice — you
    can't recommend "renew on-prem vs move to cloud" if you can't name the pieces.
    • What they'll do: preview the four verbs — name building blocks, classify models, point to
    standards, reason about cost. Each maps to a section today.
    • Stress the edge (the bolded line): recognise/explain/classify, NOT build. Building is AT2,
    later. Manage the keen student who wants to launch an EC2 instance today.
    • How they practise: on YAT's Accounting System (Ledgerline) — a real client system, all term.
    Misconception to pre-empt: "cloud = one thing you switch on." No — it's a vocabulary and a set
    of choices; today builds that vocabulary.
    Question to pose: "Before you can advise a client to move to the cloud, what do you need to
    understand first?" — draws out that literacy precedes recommendation.
    UoC/AT1 tie: this Topic develops the KE that AT1 Appendix 2 Q1–Q5 evidence.
- [BESPOKE] Our scenario: the Accounting System (Ledgerline)
  - YAT runs Ledgerline — its accounting and office-admin system. Your engagement: look at moving it to the cloud.
  - A cloud version would take a familiar shape:
    - Internet → ALB → EC2 / Auto Scaling Group  (Ledgerline app, Windows Server)
    - → RDS for SQL Server
    - (+ S3 for scanned invoices/POs · CloudWatch monitoring)
  - Don't worry about the names yet — you'll learn each piece this Topic.
  - Every exercise from here uses this system, so the picture builds as you go.
  kicker: the engagement on your desk
  image: none
  notes:
    Introduce the vehicle that carries every activity today — Ledgerline, YAT's accounting/office-admin
    system. The engagement on their desk: look at moving it to the cloud.
    • Walk the shape slowly but tell them NOT to memorise names yet (the bolded line) — you're
    planting a picture the rest of the Topic fills in.
    • Trace the flow: Internet → ALB (front door) → EC2/Auto Scaling Group (the app on Windows Server)
    → RDS for SQL Server (the database), with S3 for scanned invoices/POs and CloudWatch watching.
    • The point: this exact sketch reappears in Section 3 ("How the pieces fit") — the picture builds
    as they go, so every service they meet has a home.
    Misconception to pre-empt: that this diagram is the answer they must reproduce. It's a familiar
    SHAPE, not a mandated design — you're giving them a mental model, not a solution.
    Question to pose: "What does an accounting system need that makes 'always available' matter?" —
    gets them thinking about business expectations (feeds the next activity).
    UoC/AT1 tie: naming these components is KE 2 (industry-standard products); this same web-app
    pattern is what AT1's options/cost sections get priced against.
- [EX] Get to know your client — YAT
  - Open the YAT website & intranet and look around — this is where your client's information lives all term.
  - Find answers to:
    - What kind of organisation is YAT — what does it do, and roughly how big is it?
    - What does YAT already use in the cloud today?
    - What is Ledgerline used for, and who relies on it?
    - Where does Ledgerline run today, and on what kind of infrastructure?
    - What does the business expect of it — e.g. when must it be available?
  timer: ~10 min, then we'll share what we found
  image: none
  notes:
    Facilitation — a client-discovery task, not a lecture. This is their first contact with the
    scenario site; get them navigating it independently.
    Tell students: "You've just been assigned to the YAT engagement. Before any consultant advises a
    client, they learn the business. Open the YAT website and intranet and find the answers — this is
    where your client's information lives all term."
    Steps (put on the board):
    1. What kind of organisation is YAT — what it does, roughly how big.
    2. What YAT already uses in the cloud today.
    3. What Ledgerline is used for, and who relies on it.
    4. Where Ledgerline runs today, and on what infrastructure.
    5. What the business expects of it — e.g. when must it be available.
    Must produce: short written answers to the five questions (their first scenario notes).
    Timing: ~10 min then share. Where they get stuck: they try to Google generic answers instead of
    reading YAT's actual intranet — circulate and point them back to the site.
    Share-back prompt: "What surprised you about how YAT runs Ledgerline today?"
    No-leakage note: YAT/Ledgerline is the PRACTICE client — the assessed system (LMS) is different;
    keep them anchored to the scenario site here.
- [BESPOKE] What is cloud computing?
  image: reuse gen-7cdc0110.png
  notes:
    Section-opener visual (image only) — use it to pivot from the client to the concept. Don't over-run
    it; it's a springboard for the definition slide next.
    • Ask the room for their own one-line definition of "the cloud" BEFORE revealing anything — surface
    the vague answers ("it's the internet", "someone else's computer") so the formal definition next
    slide lands as a correction.
    • Keep the visual to a talking point: it's a picture of the idea, the precise words come next.
    Misconception to pre-empt: "cloud = the internet" or "cloud = storage (Dropbox)." Flag that these
    are partial; the real definition is broader (compute, database, storage, apps — on demand).
    Question to pose: "If I say 'we moved to the cloud', what actually changed about where the software
    runs and how we pay for it?"
    UoC/AT1 tie: sets up KE 3 (principles/functions of cloud computing) — the foundation for AT1's
    whole premise.
    [Thin slide — image only; noted as a discussion springboard.]
- [BESPOKE] Cloud computing defined
  - Cloud computing is the on-demand delivery of compute power, database, storage, applications and other IT resources via the internet, with pay-as-you-go pricing.
  - Those resources run on servers in large data centres around the world.
  - You provision what you need, when you need it, and pay only for what you use.
  image: reuse gen-5637d754.png
  notes:
    This is the anchor definition of the Topic — teach it deliberately; students should be able to
    paraphrase it in AT1.
    • Read the bolded definition, then unpack each clause: "on-demand" (you ask, you get, no waiting),
    "delivery … via the internet", the resource list (compute, database, storage, apps), and
    "pay-as-you-go pricing."
    • Second bullet: those resources run on real servers in large data centres — cloud isn't magic,
    it's someone else's data centre at global scale.
    • Third bullet: provision what you need WHEN you need it, pay only for use — this is the economic
    hinge that Section 5 (cost) builds on.
    Misconception to pre-empt: "on-demand" means free or unlimited. No — it means you can get it
    instantly, but you pay for what you use; the meter is always running.
    Question to pose: "Which word in this definition is the biggest change from buying a server for
    YAT's comms room?" (on-demand / pay-as-you-go — no upfront capex, no guessing capacity).
    UoC/AT1 tie: KE 3. This definition is exactly the kind of knowledge AT1 Appendix 2 tests and the
    business case's premise rests on.
- [BESPOKE] Infrastructure as software
  - Cloud computing lets you stop thinking of infrastructure as hardware — and instead think of (and use) it as software.
  image: reuse gen-fc3c904b.png
  notes:
    Short, high-leverage conceptual slide — the single mindset shift the whole Topic turns on. Give it
    weight despite the one bullet.
    • The idea: stop thinking of infrastructure as hardware you buy, rack and cable; think of it — and
    USE it — as software you define, request and change with a few clicks or lines of config.
    • Make it concrete: "need another server? In the old world you buy and install a box. In the cloud
    you request one and it exists in minutes — and you can delete it just as fast."
    • This frames the very next two slides (traditional vs cloud model) as the before/after of this
    shift.
    Misconception to pre-empt: "software" here doesn't mean the cloud has no hardware — the hardware is
    still there (last slide), it's just abstracted so YOU interact with it as software.
    Question to pose: "If a server is now 'software', what can you do with it that you never could with
    a physical box?" (clone it, script it, delete it, scale it up/down on demand).
    UoC/AT1 tie: KE 3 — this abstraction is the principle underlying every cloud benefit AT1 argues.
- [BESPOKE] Traditional computing model
  - Hardware solutions:
    - require space, staff, physical security, planning, capital expenditure
    - have a long hardware procurement cycle
    - make you provision capacity by guessing the theoretical maximum peak
  kicker: infrastructure as hardware
  image: diagram traditional-computing-model
  notes:
    The "before" picture — teach it so the cloud model next slide has something to beat. Lean on the
    accompanying diagram.
    • Walk the three pains: hardware needs space, staff, physical security, planning and CAPITAL
    expenditure (money up front); the procurement cycle is LONG (weeks/months to get a server); and
    you must size for the theoretical PEAK — guessing the maximum you'll ever need.
    • Drive the peak point home: you buy for the busiest hour of the busiest day, then that capacity
    sits idle the rest of the time — money spent on "just in case."
    Misconception to pre-empt: that on-prem is simply "worse." It isn't always — it's predictable and
    fully under your control; the problem is capex, lead time and over-provisioning. Keep it fair so
    their AT1 comparison is balanced.
    Question to pose: "YAT's Ledgerline server was sized years ago — how would they have guessed how
    big to make it, and what does that cost them?"
    UoC/AT1 tie: this is the on-prem baseline AT1's cost-benefit analysis (§6) argues against — you're
    arming the "before" side of their comparison.
- [BESPOKE] Cloud computing model
  - Software solutions:
    - are flexible
    - change more quickly, easily and cost-effectively than hardware
    - eliminate the undifferentiated heavy lifting
  kicker: infrastructure as software
  image: diagram cloud-computing-model
  notes:
    The "after" picture — deliberately mirror the previous slide point-for-point so the contrast is
    clean. Use the diagram.
    • Software solutions are FLEXIBLE; they change quickly, easily and cost-effectively (versus buying
    hardware); and they eliminate the "undifferentiated heavy lifting."
    • Define undifferentiated heavy lifting plainly: the racking, patching, power, cooling — work every
    company does identically and that adds no value to YOUR business. AWS does it so YAT's IT can
    focus on YAT's work.
    Misconception to pre-empt: "flexible and cheap means always cheaper." Not necessarily — an
    always-on workload can cost more than owned hardware. The win is flexibility and no upfront capex;
    cost depends on the workload shape (Section 5).
    Question to pose: "Which of Ledgerline's headaches does 'infrastructure as software' remove — and
    which does it NOT?"
    UoC/AT1 tie: the "after" side of AT1's cost-benefit; also feeds §2 strategic alignment (why moving
    aligns with the business).
- [BESPOKE] Cloud computing deployment models
  kicker: where an application runs
  image: diagram deployment-models
  notes:
    Diagram-only slide introducing the deployment-model concept — use the visual to name the models
    before the YAT-specific slide applies them.
    • Name the four off the diagram: public (shared, provider-run), private (dedicated to one org),
    hybrid (a mix of on-prem and cloud), community (shared by orgs with common needs). Define WHERE
    the application runs in each — that's the deciding axis.
    • Keep it crisp; the real work is the next slide where they see which fits YAT.
    Misconception to pre-empt: "public cloud = public/visible to everyone." No — "public" means shared,
    multi-tenant infrastructure; your data is still private and isolated. This trips students up every
    year.
    Question to pose: "Office 365 is already cloud and the comms-room servers are on-prem — so what
    deployment model is YAT running RIGHT NOW?" (hybrid — leads straight into the next slide).
    UoC/AT1 tie: KE 11 (cloud models: on-premises/private/hybrid/public) — directly tested by AT1
    Appendix 2 Q2.
    [Thin slide — diagram only; notes drive the naming/definition off the visual.]
- [BESPOKE] Deployment models — YAT's situation
  - YAT today is hybrid: on-prem servers in the comms room + Office 365 (SaaS) already in the cloud.
  - The engagement on your desk is a straight one: move an on-prem system into the public cloud.
  - So public cloud is the model that matters here — know private and hybrid as context, not as the choice.
  - The real question isn't “which of four models” — it's “keep this system on-prem, or move it to public cloud?”
  image: none
  notes:
    Apply the models to the actual client — this is where abstract becomes decision-relevant.
    • YAT today is HYBRID: on-prem servers in the comms room + Office 365 (SaaS) already in the cloud.
    Point out they're not starting from zero.
    • The engagement is a straight one: move an on-prem system INTO public cloud. So (bolded line)
    public cloud is the model that matters here — know private and hybrid as context, not as the
    choice on the table.
    • The real question (last bullet) isn't "which of four models" — it's binary: keep Ledgerline
    on-prem, or move it to public cloud. This reframing is what keeps AT1 focused.
    Misconception to pre-empt: that they must evaluate all four models exhaustively in AT1. No — name
    them to show literacy, but the genuine decision is on-prem vs public cloud.
    Question to pose: "Why would a small RTO like YAT choose PUBLIC cloud over building its own PRIVATE
    cloud?" (scale, cost, no data centre to run).
    UoC/AT1 tie: KE 11; and this binary framing IS the spine of AT1's §5 Options Considered.
- [EX] Which deployment model?
  - YAT is considering moving Ledgerline off its on-prem server.
  - Which deployment model fits a cloud version of Ledgerline — and why is that the right fit for YAT?
  - Write one short paragraph: name the model, then justify it (think about who YAT is, what it already runs, and how much it wants to manage).
  timer: ~5 min, then we compare
  image: none
  notes:
    Facilitation — a short written reasoning task, their first "consultant recommendation" in miniature.
    Tell students: "YAT is considering moving Ledgerline off its on-prem server. As the MTS consultant,
    pick the deployment model for a cloud version — and justify it for THIS client."
    Steps:
    1. Name the model (they should land on public cloud).
    2. Justify it in one short paragraph — WHO YAT is, what it already runs (Office 365 = comfortable
    with SaaS/public cloud), and how much it wants to manage.
    Must produce: one short written paragraph — a named model plus a client-specific justification (not
    a generic textbook reason).
    Timing: ~5 min then compare. Where they get stuck: they name "hybrid" because YAT is hybrid today —
    push them to answer for the Ledgerline SYSTEM specifically, which is moving TO public cloud.
    Share-back prompt: take two contrasting answers and ask the room which justification is more
    client-specific.
    No-leakage note: this is practice reasoning on Ledgerline; the same skill is assessed later on the
    LMS in AT1 — comparable, not identical.
    UoC/AT1 tie: rehearses AT1 Appendix 2 Q2 and §5 in contextual form.
- [TAKEAWAYS] Section 1 · Cloud literacy
  - Cloud computing = on-demand IT resources over the internet, pay-as-you-go.
  - It lets you treat infrastructure as software, not hardware.
  - Three deployment models: cloud · hybrid · on-premises (private cloud).
  - For YAT the real choice is binary: keep on-prem, or move to public cloud.
  image: none

### C2 — Service models
- Teaches: [ICTCLD401 KE 3]
- Kicker: who manages what
- [BESPOKE] Cloud service models
  - IaaS — infrastructure as a service
  - PaaS — platform as a service
  - SaaS — software as a service
  - IaaS → SaaS = more control / more work  →  less control / less work.
  kicker: a spectrum of control
  image: diagram service-model-spectrum
  notes:
    Open Section 2 — the IaaS/PaaS/SaaS spectrum. Use the spectrum diagram; this is one of the two
    highest-value concepts in the Topic.
    • Name the three (bolded): IaaS = infrastructure, PaaS = platform, SaaS = software as a service.
    • The key line (accent bold): moving IaaS → SaaS trades MORE control/more work for LESS control/less
    work. Everything else on this topic hangs off that one axis.
    • Don't classify real services yet — that's the next slide. Here, just install the spectrum and the
    trade-off direction.
    Misconception to pre-empt: that the models are ranked "SaaS is best / most advanced." They are NOT
    a quality ladder — they're a control-vs-effort trade-off; the right one depends on the client.
    Question to pose: "If you want maximum control over the operating system, which end do you sit at —
    and what do you give up for it?" (IaaS; you take on all the ops work).
    UoC/AT1 tie: KE 3; directly evidenced by AT1 Appendix 2 Q1.
- [BESPOKE] Service models — who manages what
  - IaaS (e.g. EC2) — you manage the OS and the app; the provider handles the hardware → most control, most work. Preserve an existing stack.
  - PaaS (e.g. RDS, ALB) — the provider runs the platform; you run your app/data → less control, far less ops. Offload work when cloud skills are thin.
  - SaaS (e.g. Office 365) — the provider runs everything; you just use it → least control, least work.
  - Choosing = control vs operational burden. Classify each part, then say why that level fits the client.
  image: none
  notes:
    The workhorse slide of Section 2 — teach the "who manages what" split with concrete AWS examples so
    it stops being an acronym.
    • IaaS (EC2): YOU manage OS + app, provider does hardware → most control, most work. Use when you
    must preserve an existing stack (like a lift-and-shift of Ledgerline's app).
    • PaaS (RDS, ALB): provider runs the platform; you run app/data → far less ops. Use to offload work
    when cloud skills are thin (very relevant to a small RTO).
    • SaaS (Office 365): provider runs everything, you just use it → least control, least work.
    • The decision (accent bold): control vs operational burden — classify each part, then SAY WHY that
    level fits the client. The "why" is what earns AT1 marks, not the label.
    Misconception to pre-empt: students think a whole solution is "a SaaS" or "an IaaS." Real
    architectures MIX models — Ledgerline could be IaaS app + PaaS database + SaaS email at once.
    Question to pose: "In our Ledgerline sketch, which piece is IaaS and which is PaaS — and why did
    the designer choose PaaS for the database?" (RDS = offload patching/backups/DR).
    UoC/AT1 tie: KE 3 → AT1 Appendix 2 Q1 and §5 (articulating the cloud option).
- [EX] Classify the service models
  - For each, name the service model and say why:
    - Office 365
    - A VPS that comes with an OS installed, which you then configure and run your software on
    - A service that lets you rent compute & memory and install your own OS and software
    - A managed database service where the provider runs, patches and backs up the engine, and you just connect and store data
  timer: ~8 min, then we compare
  image: none
  notes:
    Facilitation — the Section 2 practice; mirrors AT1 Appendix 2 Q1 in contextual form.
    Tell students: "For each of these four, name the service model — IaaS, PaaS or SaaS — and give me
    the one-line WHY. The label alone earns nothing; the reasoning does."
    The four (read/put up):
    1. Office 365 → SaaS (provider runs everything, you just use it).
    2. A VPS with an OS installed that you configure and run your software on → IaaS.
    3. A service that rents compute & memory where you install your own OS and software → IaaS.
    4. A managed database the provider runs/patches/backs up, you just connect and store → PaaS.
    Must produce: four labelled answers, each with a one-line justification tied to "who manages what."
    Timing: ~8 min then compare. Where they get stuck: items 2 and 3 both being IaaS feels wrong to
    them (they hunt for variety) — reassure them the distinction is about who manages the OS, and both
    leave the OS to you.
    Share-back prompt: "Which one was hardest to place, and what tipped it?"
    No-leakage note: practice items here; AT1 asks the same skill on the assessed system.
- [TAKEAWAYS] Section 2 · Service models
  - Three models: IaaS → PaaS → SaaS — handing over more control for less effort.
  - IaaS = you manage the OS up · PaaS = provider runs the platform · SaaS = you just use it.
  - The deciding question is always “who manages the OS / the platform?”
  - Choosing isn't “best” — it's control vs operational burden for this client.
  image: none

### C3 — Core AWS services
- Teaches: [ICTCLD401 KE 2] · [ICTCLD502 KE 2]
- Kicker: the building blocks
- [BESPOKE] What is AWS?
  - A secure cloud platform offering a broad set of global cloud-based products.
  - On-demand access to compute, storage, network, database and other IT resources — plus the tools to manage them.
  - You pay only for the services you use, for as long as you use them.
  - AWS services work together like building blocks.
  image: none
  notes:
    Open Section 3 — anchor what AWS actually IS before drowning them in service names.
    • Walk the bullets: a secure cloud PLATFORM with a broad set of global products; on-demand access
    to compute, storage, network, database and more, plus the tools to manage them; pay only for
    what you use, for as long as you use it.
    • The accent-bold line is the mental model for the whole section: AWS services work together like
    BUILDING BLOCKS. Everything that follows (compute, storage, database, networking) is a box of
    blocks; the web-app pattern slide clicks them together.
    Misconception to pre-empt: "AWS = servers in the cloud." It's far broader — 200+ services across
    many categories; today they meet only the handful needed for a web app.
    Question to pose: "Why would AWS build small single-purpose services instead of one big product?"
    (compose only what you need; pay only for what you use).
    UoC/AT1 tie: KE 2 (industry-standard hardware/software products) → AT1 Appendix 2 Q4.
- [BESPOKE] Selecting a Region
  - Choose a Region based on:
    - data governance & legal requirements
    - proximity to users (latency)
    - which services are available in the Region
    - cost (varies by Region)
  kicker: where your services and data live
  image: none
  notes:
    Teach Region as a real, consequential first decision — not trivia. It returns hard in AT2 (residency).
    • Walk the four drivers: data governance & LEGAL requirements (where data is allowed to live),
    proximity to users (latency), service AVAILABILITY (not every service is in every Region), and
    cost (prices vary by Region).
    • Lead with governance/legal for this client: YAT holds financial records and PII — that's the
    driver that dominates, and it's why the AT2 design later mandates a Sydney Region.
    Misconception to pre-empt: "pick the closest Region for speed." Latency matters, but for YAT DATA
    RESIDENCY (legal) outranks it — closest isn't automatically correct.
    Question to pose: "YAT stores Australians' financial and personal data — which of these four drivers
    decides the Region, and why?" (governance/legal → onshore).
    UoC/AT1 tie: KE 2. Region choice-for-residency is developed here and BUILT in AT2 (Topic 6) — flag
    the through-line.
- [BESPOKE] Availability Zones
  - Each Region has multiple Availability Zones.
  - Each AZ is a fully isolated partition of the AWS infrastructure:
    - discrete data centres, designed for fault isolation
    - interconnected by high-speed private networking
    - you choose your AZs; replicate across them for resiliency
  kicker: isolated, within a Region
  image: diagram availability-zones
  notes:
    Teach AZs as the resilience building block — pair with the diagram; students routinely confuse AZ
    with Region.
    • Each Region has MULTIPLE Availability Zones. Each AZ is a fully isolated partition: discrete data
    centres designed for fault ISOLATION, interconnected by high-speed private networking.
    • The consequence (last bullet): YOU choose your AZs and replicate across them for resiliency — one
    AZ can fail without taking your app down. This is why the Ledgerline sketch has an Auto Scaling
    Group spanning AZs.
    Misconception to pre-empt: "an AZ is a single data centre" or "AZ = Region." An AZ is one or more
    discrete data centres; a Region CONTAINS several AZs. Draw the Region-as-box, AZs-inside picture.
    Question to pose: "If an accounting system must stay up when one data centre fails, what does that
    force you to do with AZs?" (spread across at least two).
    UoC/AT1 tie: KE 2; sets up the Region/AZ hierarchy the console activity has them verify hands-on.
- [BESPOKE] AWS categories of services
  image: reuse 01-aws-service-categories.png
  notes:
    Diagram-only overview slide — use it as the section's map, not a slide to read out.
    • Point to the grid: AWS groups its 200+ services into CATEGORIES (compute, storage, database,
    networking, security, etc.). Tell them we'll walk the four categories a web app needs over the
    next slides — they don't need the whole grid.
    • Reassure: nobody memorises this; consultants recognise the category and know where to look.
    Misconception to pre-empt: that they must learn every service shown. No — literacy is knowing the
    CATEGORIES and the handful of core services in each; breadth over depth today.
    Question to pose: "For our Ledgerline web app, which categories will we definitely touch?" (compute,
    storage, database, networking — previews the next four slides).
    UoC/AT1 tie: KE 2 → AT1 Appendix 2 Q4 (naming industry-standard products by category).
    [Thin slide — image only; used as a navigational map for the section.]
- [BESPOKE] Compute
  - Amazon EC2 · EC2 Auto Scaling
  - Amazon ECS · EKS · ECR · Fargate
  - AWS Elastic Beanstalk · AWS Lambda
  kicker: service category
  image: reuse gen-34a664bb.png
  notes:
    First of four service-category slides — keep the pace up; the goal is recognition, not depth.
    • Name the headline service and its role: Amazon EC2 = virtual servers (the core), EC2 Auto Scaling
    = add/remove instances with demand. Mention the container/serverless family exists — ECS, EKS,
    ECR, Fargate, Elastic Beanstalk, Lambda — without going deep.
    • Tie to the sketch: EC2 + Auto Scaling Group is the APP TIER of Ledgerline. That's the one they
    must be able to name and place.
    Misconception to pre-empt: that they need all of these. For the web-app pattern only EC2 + Auto
    Scaling matter; the rest are "recognise the name" only at this level.
    Question to pose: "Which compute service runs the Ledgerline application itself?" (EC2, scaled by an
    Auto Scaling Group).
    UoC/AT1 tie: KE 2 → AT1 Appendix 2 Q4; EC2 is IaaS, tying back to Section 2's spectrum.
- [BESPOKE] Storage
  - Amazon EBS — block storage for EC2
  - Amazon EFS — managed file system
  - Amazon S3 — object storage
  - Amazon S3 Glacier — archive / long-term backup
  kicker: service category
  image: reuse gen-a635ad7f.png
  notes:
    Second service-category slide — differentiate the storage TYPES, which is the examinable point.
    • EBS = block storage attached to EC2 (like a disk on the server). EFS = a managed shared file
    system. S3 = OBJECT storage (files/blobs by key — where Ledgerline's scanned invoices and POs
    live). S3 Glacier = cheap archive / long-term backup.
    • For the sketch, the two that matter: EBS (disks on the EC2 servers) and S3 (scanned documents).
    Misconception to pre-empt: "S3 is a hard drive / a file system." It isn't — S3 is object storage
    (no OS mounts it like a drive); EBS is the block "disk" for a server. This block-vs-object
    distinction is the whole slide.
    Question to pose: "Where should YAT keep scanned invoices — EBS or S3, and why?" (S3 — cheap,
    durable object storage for documents; EBS is for the server's OS/app disk).
    UoC/AT1 tie: KE 2 → AT1 Appendix 2 Q4.
- [BESPOKE] Database
  - Amazon RDS — managed relational database
  - Amazon Aurora — MySQL/PostgreSQL-compatible
  - Amazon DynamoDB — key-value / document
  - Amazon Redshift — analytics / data warehouse
  kicker: service category
  image: reuse gen-90cedd2d.png
  notes:
    Third service-category slide — anchor on RDS since that's Ledgerline's database tier.
    • RDS = managed RELATIONAL database (in the sketch, SQL Server) — provider patches/backs up/handles
    DR. Aurora = AWS's MySQL/PostgreSQL-compatible engine. DynamoDB = key-value/document (NoSQL).
    Redshift = analytics/data warehouse.
    • Tie to the sketch: RDS for SQL Server is Ledgerline's database — and it's PaaS (callback to
    Section 2: the provider runs the engine, YAT just stores data).
    Misconception to pre-empt: "a database is a database." No — relational (RDS/Aurora) vs NoSQL
    (DynamoDB) vs warehouse (Redshift) serve different jobs; picking wrong is a design error.
    Question to pose: "Ledgerline is an accounting system with structured, related records — which
    database service fits, and is it IaaS or PaaS?" (RDS; PaaS).
    UoC/AT1 tie: KE 2 → AT1 Appendix 2 Q4; reinforces the service-model classification skill.
- [BESPOKE] Networking & content delivery
  - Amazon VPC — isolated virtual network
  - Elastic Load Balancing · Route 53 (DNS)
  - Amazon CloudFront — content delivery
  - AWS Direct Connect · Transit Gateway · VPN
  kicker: service category
  image: reuse gen-0312fdbb.png
  notes:
    Fourth service-category slide — the plumbing that ties the tiers together. Keep VPC and ELB central;
    the rest is recognition.
    • VPC = your isolated virtual network (the private space everything lives in). Elastic Load Balancing
    = spreads traffic across servers (the ALB in the sketch). Route 53 = DNS. CloudFront = content
    delivery/caching. Direct Connect / Transit Gateway / VPN = enterprise connectivity — name-only.
    • For the sketch: VPC (the network) and the ALB (load balancer) are the two that matter.
    Misconception to pre-empt: "the load balancer is a server that does the work." No — it DISTRIBUTES
    incoming requests across the EC2 servers; it doesn't run the app itself.
    Question to pose: "In the Ledgerline sketch, what sits between the internet and the EC2 servers, and
    what job does it do?" (the ALB — spreads traffic; enables scaling and resilience).
    UoC/AT1 tie: KE 2 → AT1 Appendix 2 Q4; VPC/subnets return hands-on in the console activity and in AT2.
- [BESPOKE] How the pieces fit — the web-app pattern
  - Internet → ALB → EC2 / Auto Scaling Group → RDS  (+ S3, CloudWatch)
  - ALB — spreads incoming traffic across servers · PaaS
  - EC2 + Auto Scaling Group — the app tier; runs the app, scales with demand · IaaS
  - RDS — managed database (here, SQL Server) · PaaS
  - S3 — object storage (scanned invoices/POs) · EBS — disks on the EC2 servers
  - CloudWatch — monitors all of the above
  kicker: the Ledgerline sketch wasn't random
  image: none
  notes:
    The payoff slide of Section 3 — this is where the Ledgerline sketch from the start of class snaps
    together. Slow down and assemble it live.
    • Read the flow (accent-bold): Internet → ALB → EC2/Auto Scaling Group → RDS (+ S3, CloudWatch).
    Then attach each service to its role AND its service model:
    - ALB spreads traffic across servers · PaaS
    - EC2 + Auto Scaling Group = app tier, runs the app and scales with demand · IaaS
    - RDS = managed database (SQL Server) · PaaS
    - S3 = object storage for scanned invoices/POs; EBS = the disks on the EC2 servers
    - CloudWatch = monitors all of it.
    • Callback hard: "the Ledgerline sketch wasn't random" — this is the standard multi-tier web-app
    pattern; recognising it is a core consultant skill.
    Misconception to pre-empt: that this is the only correct architecture. It's the COMMON pattern, not
    a law — but it's the one they should recognise and reason about.
    Question to pose: "Point at each box and tell me: IaaS or PaaS — and why did the designer pick that?"
    UoC/AT1 tie: KE 2 + KE 3 together; this integrated picture underpins AT1's §5 options and the
    services that get priced in §6.
- [BESPOKE] Activity: AWS Management Console
  - We'll log in to the AWS Management Console together.
  - You'll answer five questions as we navigate; we discuss and reveal each answer.
  kicker: educator-led clickthrough
  image: reuse 01-aws-console.png
  notes:
    Set-up/framing slide for the educator-led console walk-through — brief, then move to the live tour.
    • Explain the format: you'll all log in to the AWS Management Console together; as you navigate,
    they answer five questions; you discuss and reveal each answer. This is guided literacy — no
    building, just seeing the console is real and navigable.
    • Manage expectations: they'll get lost in the console at first; that's fine — the goal is to see
    how services are organised and where Region/AZ live, not to master it.
    Misconception to pre-empt: "we're building today." No — this is a look-and-find tour; building is
    AT2. Keep them from launching resources.
    Question to pose (warm-up): "When you open the console, how do you think 200+ services are organised
    so you can find anything?" (by category — which they'll confirm live).
    UoC/AT1 tie: makes KE 2 concrete — recognising real industry-standard products in the actual tool.
- [BESPOKE] Hands-on: Console clickthrough
  - Launch the AWS Academy Learner Lab and connect to the AWS Management Console.
  - Open the Services menu — notice services are grouped into categories (EC2 → Compute).
    - Q1: which category is the IAM service under?
    - Q2: which category is Amazon VPC under?
  - Open VPC; switch the Region menu (e.g. to EU (London)); open Subnets, select one.
    - Q3: does a subnet exist at Region level or Availability-Zone level?
    - Q4: does a VPC exist at Region level or AZ level?
    - Q5: which are global, not Regional — EC2, IAM, Lambda, Route 53?
  image: none
  notes:
    Facilitation — run this as the live, educator-led tour with the five questions. You drive; they
    follow and answer. Pause on each Q, take answers, then reveal (answer key is the next slide).
    Sequence to demonstrate:
    1. Launch the AWS Academy Learner Lab, connect to the Console.
    2. Open the Services menu — show services grouped by category (EC2 → Compute).
    Q1: which category is IAM under?  Q2: which category is Amazon VPC under?
    3. Open VPC; switch the Region menu (e.g. to EU (London)); open Subnets, select one.
    Q3: does a subnet exist at Region or AZ level?  Q4: does a VPC exist at Region or AZ level?
    Q5: which of EC2, IAM, Lambda, Route 53 are global, not Regional?
    Timing: ~15 min. Where they get stuck: Learner Lab login/console handoff (have the lab-launch steps
    ready), and the Region switch confusing them — go slowly and have everyone switch together.
    Share-back: take a show of hands on each Q before revealing; the disagreements are the teaching
    moment (esp. Q3/Q4 Region-vs-AZ and Q5 global-vs-Regional).
    Note: Learner Lab deploys to us-east-1 — [scenario region | deploy: us-east-1]; if you switch
    Regions to demo, switch back before anyone builds.
    UoC/AT1 tie: KE 2; cements the Region/AZ hierarchy from the AZ slide by having them SEE it.
- [BESPOKE] Activity answer key
  - Q1 — IAM → Security, Identity & Compliance.
  - Q2 — Amazon VPC → Networking & Content Delivery.
  - Q3 — subnets exist at the Availability-Zone level.
  - Q4 — VPCs exist at the Region level.
  - Q5 — IAM and Route 53 are global; EC2 and Lambda are Regional.
  image: none
  notes:
    Reveal + consolidate — don't just read answers; explain WHY each is what it is, because the
    Region-vs-global distinction is the sticky one.
    • Q1 — IAM → Security, Identity & Compliance.
    • Q2 — Amazon VPC → Networking & Content Delivery.
    • Q3 — subnets exist at the AVAILABILITY-ZONE level (a subnet lives in one AZ).
    • Q4 — VPCs exist at the REGION level (a VPC spans the AZs in its Region).
    • Q5 (accent-bold) — IAM and Route 53 are GLOBAL; EC2 and Lambda are REGIONAL.
    Draw the hierarchy on the board: global services sit above Regions; a VPC is Region-scoped; subnets
    sit inside AZs inside the Region.
    Misconception to pre-empt: "everything belongs to a Region." Some services (IAM, Route 53) are
    global — get this wrong in AT2 and screenshots won't match the expected scope.
    Question to pose: "Why does it make sense that IAM is global but EC2 is Regional?" (identity applies
    account-wide; servers physically live in a Region).
    UoC/AT1 tie: KE 2; this Region/AZ/global model is assumed knowledge when they build in AT2.
- [TAKEAWAYS] Section 3 · Core AWS services
  - AWS groups services into categories — compute, storage, database, networking…
  - Web-app building blocks: EC2 (compute) · S3/EBS (storage) · RDS (database) · ALB/VPC (networking).
  - Regions and Availability Zones decide where services run — for residency and resilience.
  - They assemble into one shape: Internet → ALB → EC2/ASG → RDS (+ S3, CloudWatch).
  - At this stage: name each service and its role — not build it.
  image: none

### C4 — Industry technology standards
- Teaches: [ICTCLD401 KE 1] · [ICTCLD502 KE 1]
- Kicker: standards that inform a migration
- [BESPOKE] The AWS Well-Architected Framework
  - A guide for designing infrastructure that is:
    - secure · high-performing · resilient · efficient
  - A consistent way to evaluate and improve cloud architectures.
  - Best practices drawn from reviewing thousands of customer architectures.
  image: reuse 01-well-architected-pillars.png
  notes:
    Open Section 4 — the one standard worth teaching in a little depth, because its Reliability pillar
    returns in the design work. Use the pillars image.
    • What it is: a GUIDE for designing infrastructure that is secure, high-performing, resilient and
    efficient — a consistent way to EVALUATE and IMPROVE cloud architectures, built from AWS reviewing
    thousands of real customer architectures.
    • Frame it as the "how do I know my design is any good?" standard — the yardstick, not a product.
    Misconception to pre-empt: that Well-Architected is a tool you install or a certification. It's a
    framework/checklist of design principles you assess a design against.
    Question to pose: "If you had to argue YAT's proposed cloud design is 'well designed', what would you
    measure it against?" (the pillars — security, reliability, performance, cost, etc.).
    UoC/AT1 tie: KE 1 (industry technology standards) → AT1 Appendix 2 Q3; its Reliability pillar comes
    back when they design for real in AT2, so flag the through-line.
- [TABLE] Standards that inform a migration
  kicker: each guides a different decision
  | Standard | What it is | Informs… |
  |---|---|---|
  | NIST SP 800-145 | The definition of IaaS / PaaS / SaaS | service-model choices |
  | AWS Well-Architected | Six design pillars (incl. Reliability) | design quality + how you improve it |
  | ISO/IEC 27017 | Cloud-specific security controls | security decisions |
  | ACSC Essential Eight | Australian baseline cyber mitigations | security controls / compliance |
  | ITIL 4 | Service-management practices | change-management alignment |
  note: You're not implementing these — you're naming the right standard for a given decision.
  image: none
- [EX] Which standard informs the decision?
  - For each decision, name the standard and give a one-line why:
    - Deciding whether each part of a solution is IaaS, PaaS or SaaS
    - Choosing the cloud security controls for a system
    - Meeting an Australian baseline of cyber mitigations
    - Judging whether an architecture is well-designed and reliable
    - Planning the change-management around a migration
  timer: ~8 min, then we compare
  image: none
  notes:
    Facilitation — the Section 4 practice; matching standards to decisions (AT1 Appendix 2 Q3 in
    contextual form).
    Tell students: "You don't implement these standards yet — you name the RIGHT one for a given
    decision and say why in one line. That's the consultant skill: knowing which rulebook to reach for."
    The five decisions (put up):
    1. Deciding whether each part is IaaS/PaaS/SaaS → NIST SP 800-145.
    2. Choosing cloud security controls → ISO/IEC 27017.
    3. Meeting an Australian baseline of cyber mitigations → ACSC Essential Eight.
    4. Judging whether an architecture is well-designed and reliable → AWS Well-Architected.
    5. Planning change-management around a migration → ITIL 4.
    Must produce: five matched standard→decision pairs, each with a one-line why.
    Timing: ~8 min then compare. Where they get stuck: conflating ISO 27017 (cloud security controls)
    with Essential Eight (AU baseline mitigations) — clarify 27017 is the international control set,
    Essential Eight is the Australian government baseline.
    Share-back: read a decision, take the standard from the room, confirm the reasoning.
    No-leakage note: practice mapping here; AT1 tests the same recognition on the assessed context.
- [TAKEAWAYS] Section 4 · Industry standards
  - A migration is informed by several standards — each guides a different decision.
  - NIST → service models · Well-Architected → design quality · ISO 27017 → cloud security · Essential Eight → AU baseline · ITIL 4 → change management.
  - Well-Architected's Reliability pillar comes back when you design for real.
  - The skill now is recognising the right standard for a decision, not implementing it.
  image: none

### C5 — Cloud cost models & economics
- Teaches: [ICTCLD401 KE 4] · [ICTCLD502 KE 3]
- Kicker: why a migration is a cost conversation
- [BESPOKE] AWS pricing model
  - Compute — charged per hour/second, varies by instance type.
  - Storage — charged typically per GB.
  - Data transfer — outbound is aggregated and charged; inbound is mostly free.
  kicker: three fundamental cost drivers
  image: none
  notes:
    Open Section 5 — the three fundamental cost drivers. This section arms AT1's cost-benefit analysis,
    so keep it concrete and money-focused.
    • Three drivers (all bolded): COMPUTE — charged per hour/second, varies by instance type; STORAGE —
    typically per GB; DATA TRANSFER — outbound is aggregated and charged, inbound is mostly free.
    • Hammer the data-transfer asymmetry: getting data IN is usually free, getting it OUT costs — a
    classic surprise on cloud bills.
    Misconception to pre-empt: "cloud is billed as one flat monthly fee." No — it's the sum of many
    metered drivers; you must model each. And "data transfer is free" — only inbound.
    Question to pose: "For Ledgerline, which of these three drivers is likely the biggest, and which
    could surprise YAT on the bill?" (compute for an always-on app; egress data transfer as the
    surprise).
    UoC/AT1 tie: KE 4 / KE 3 (cost models & scalability) → AT1 Appendix 2 Q5 and §6 cost-benefit.
- [BESPOKE] How do you pay for AWS?
  - Pay for what you use.
  - Pay less when you reserve.
  - Pay less when you use more, and as AWS grows.
  image: reuse 01-aws-pricing-philosophy.png
  notes:
    Teach the three-part AWS pricing PHILOSOPHY — the logic behind every discount they'll meet next.
    Use the pricing-philosophy image.
    • Pay for what you use (the pay-as-you-go default). Pay LESS when you RESERVE (commit ahead → the
    next slide, RIs). Pay LESS when you use MORE, and as AWS grows (volume discounts + AWS passing on
    its own economies of scale).
    • Frame it as: AWS rewards predictability (commit) and scale — the opposite of paying full retail
    for everything on demand.
    Misconception to pre-empt: "pay-as-you-go is always cheapest." Not for a steady always-on workload —
    reserving is cheaper there (the whole point of the next slide). On-demand's value is flexibility,
    not lowest price.
    Question to pose: "Ledgerline runs every business day, all year — does pay-as-you-go or reserving
    suit it better, and why?" (reserved — predictable baseline).
    UoC/AT1 tie: KE 4 → AT1 Appendix 2 Q5; underpins justifying the pricing choice in the cost-benefit.
- [BESPOKE] Pay less when you reserve
  - Invest in Reserved Instances — save up to 75%.
  - Options (more upfront = bigger discount):
    - All Upfront (AURI) — largest discount
    - Partial Upfront (PURI) — lower discount
    - No Upfront (NURI) — smallest discount
  kicker: Reserved Instances (RIs)
  image: reuse 01-reserved-instance-options.png
  notes:
    Teach Reserved Instances concretely — this is the highest-leverage cost lever for YAT's steady
    workload. Use the RI-options image.
    • The headline: commit to Reserved Instances and save up to ~75% versus on-demand — a big number,
    make sure it lands.
    • The trade (more upfront = bigger discount): All Upfront (AURI) = largest discount; Partial Upfront
    (PURI) = middle; No Upfront (NURI) = smallest. It's a cash-flow-vs-savings choice.
    Misconception to pre-empt: "reserved = a physically different, better server." No — same instance;
    you're pre-COMMITTING to pay for it, so AWS discounts it. Also, RIs suit steady baselines, NOT
    variable/peaky workloads (that's on-demand).
    Question to pose: "YAT could pay more upfront for a bigger discount, or nothing upfront for less —
    what would you advise a small RTO watching cash flow?" (weigh discount vs cash flow — a real
    consulting judgement).
    UoC/AT1 tie: KE 4 → AT1 Appendix 2 Q5; the RI-discount rationale is explicitly examinable.
- [BESPOKE] AWS Pricing Calculator
  - Estimate monthly costs and find ways to reduce them.
  - Model solutions before building them; explore the calculations behind an estimate.
  - Find instance types & contract terms; group services to organise an estimate.
  kicker: model the cost before you build
  image: reuse 01-pricing-calculator.png
  notes:
    Introduce the tool that turns cost knowledge into a real AT1 number. Use the calculator image.
    • What it does: estimate monthly costs and find ways to reduce them; MODEL solutions before building
    them and explore the calculations behind an estimate; find instance types & contract terms; group
    services to organise an estimate.
    • Frame it as the consultant's estimating instrument — this is literally how they'll produce the
    AWS pricing figures in AT1's cost-benefit appendix.
    Misconception to pre-empt: "the calculator's number is the exact bill." It's an ESTIMATE based on
    your assumptions (usage, hours, region) — change the assumptions and the number changes; document
    your assumptions.
    Question to pose: "Before you can price Ledgerline in the calculator, what do you need to know about
    how it runs?" (which services, instance size, hours, storage, data transfer).
    UoC/AT1 tie: KE 4 → directly enables AT1 §6 + Appendix 1 (Cost-Benefit Analysis) — the tool they'll
    actually use.
- [BESPOKE] Reading an estimate
  - An estimate is broken into three figures:
    - First 12 months total
    - Total upfront
    - Total monthly
  image: none
  notes:
    Short but practical — teach students to READ a calculator estimate, because they'll paste one into
    AT1 and must interpret it.
    • An estimate breaks into three figures: FIRST 12 MONTHS total, TOTAL UPFRONT, and TOTAL MONTHLY.
    Explain what each answers: monthly = ongoing run rate; upfront = any reserved commitment paid now;
    12-month = the headline annual figure that combines them.
    • Tie back: if they chose Reserved Instances (last slides), the upfront figure is where that shows up.
    Misconception to pre-empt: "the monthly figure is the whole cost." No — upfront commitments sit
    outside the monthly run rate; the 12-month total is what reconciles them. Reading only one figure
    misleads the business case.
    Question to pose: "If YAT's board asks 'what will this cost us?', which of the three figures do you
    lead with, and which do you NOT hide?" (lead with 12-month/annual; don't hide upfront).
    UoC/AT1 tie: KE 4 → AT1 cost-benefit — interpreting the estimate correctly is what makes the §6
    argument credible.
- [TABLE] Match the pricing model to the workload
  kicker: cost follows the shape of demand
  | Workload profile | Best-fit pricing |
  |---|---|
  | Predictable, always-on baseline | Reserved Instances (commit, pay less) |
  | Variable / peaky | On-demand or autoscaling |
  | Interruptible, can be retried | Spot (cheapest — not for production baseline) |
  | Storage & data | Pay-as-you-go (scales with usage) |
  note: Watch licensing: a Windows + SQL Server system carries software-licence cost on top of infrastructure — easy to miss.
  image: none
- [BESPOKE] Additional benefit considerations
  - Hard benefits:
    - lower spend on compute, storage, networking, security
    - fewer hardware/software purchases (capex); lower ops, backup & DR costs
  - Soft benefits:
    - reuse of services; higher developer productivity
    - improved customer satisfaction; agility; greater reach
  kicker: hard and soft benefits
  image: none
  notes:
    Close the cost section by widening it from cost to VALUE — AT1's business case argues benefits, not
    just a cheaper bill.
    • Hard benefits (quantifiable): lower spend on compute/storage/networking/security; fewer
    hardware/software purchases (less capex); lower ops, backup and DR costs.
    • Soft benefits (harder to price but real): reuse of services; higher developer productivity;
    improved customer satisfaction; agility; greater reach.
    • The teaching point: a strong business case pairs the hard numbers with the soft benefits — cost
    alone rarely wins the argument.
    Misconception to pre-empt: "the business case is just 'cloud is cheaper'." Often it ISN'T strictly
    cheaper — the case is built on agility, capex avoidance and capability, not price alone. Guard
    against a purely-cost argument in AT1.
    Question to pose: "Which soft benefit would matter most to YAT specifically, and how would you
    evidence something you can't put a dollar on?"
    UoC/AT1 tie: KE 4 → AT1 §6 cost-benefit AND §2 strategic alignment — the benefits case, not just
    the price tag.
- [TAKEAWAYS] Section 5 · Cost models
  - Three cost drivers: compute · storage · data transfer.
  - Three ways to pay: pay-as-you-go · reserve (commit for less) · pay-less-as-you-grow.
  - Match pricing to the workload — baseline→reserved, peaky→on-demand, storage→pay-as-you-go.
  - Don't forget software licensing (e.g. Windows / SQL Server) on top of infrastructure.
  - Cost grows roughly with demand — that's why moving a system is a cost conversation.
  image: none

### Close
- [BESPOKE] From literacy to the job
  - You can now classify deployment and service models, name the building blocks, point to the right standard, and reason about cost.
  - That's the literacy a consultant needs before recommending whether to move a system to the cloud.
  - Next, you'll put it to work — weighing the options and making the case for a real migration.
  - You practised on the Accounting System; the same skills carry to whatever engagement lands on your desk.
  image: none
