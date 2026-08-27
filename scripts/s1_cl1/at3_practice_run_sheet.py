#!/usr/bin/env python3
"""The S1-CL1 AT3 PRACTICE HA run sheet — content.

Same shape as the AT3 assessment workbook, different everything else. A student who works
through this has rehearsed every move the assessment needs without having seen its answers:

  scenario   Ledgerline, YAT's accounting system — not the LMS
  addresses  10.20.x.x — not 10.0.x.x
  servers    Amazon Linux — not Windows
  database   PostgreSQL on 5432 — not MySQL on 3306
  monitoring one baseline alarm — not two

The starting point is `delivery/practice-lab-pack/baseline.yaml`, which replicates a correctly
completed AT2 PRACTICE build. It carries the same four single points of failure the assessment
environment does, by construction: only the first zone carries load, one NAT gateway, an Auto
Scaling group of one in one subnet, and a single-AZ database. The load balancer already spans
both public subnets — so practice task 9's "look before you design" trap rehearses too.

WHAT PRACTICE ADDS, and the whole reason it exists:

  Part A   every design task is presented exactly as the assessment presents it, then adds a
           "Things to consider" block — leading questions, pointed enough that a student who
           is paying attention cannot miss the answer, and which never state it. Practice
           teaches the thinking; it does not hand over the finding, because then the student
           arrives at the assessment having watched rather than done.
  Part B   click-by-click steps. The assessment says "extend the Auto Scaling group across
           both zones"; practice says which console, which tab, which button.

No marking criteria, no UoC tags, no institutional boilerplate — it is not an assessment.
Rendered by the shared renderer in at3_run_sheet, with these lists passed in.
"""

SITE = "https://yat.timbaird.com"

SCENARIO = [
    "Ledgerline is YAT College's accounting system. It moved to AWS in the previous practice "
    "exercise — you built the foundation yourself, or you have been given it ready-made. Finance "
    "staff use it every day, and month-end is unforgiving.",
    "It works, and it is fragile. Everything that serves Ledgerline sits in one availability zone, "
    "there is one application server, and the database has no standby. Finance have asked what "
    "happens if something breaks, and nobody has a good answer.",
    "This is practice. Nothing here is marked and nothing is submitted. It is the same work the "
    "assessment will ask for, on a different system — so do it properly, because the moves are the "
    "point.",
]

INSTRUCTIONS = [
    "Part A is the design. Work the tasks in order. Each one is presented the way the assessment "
    "presents it, and then adds a Things to consider block underneath.",
    "Those considerations are leading questions, not answers. If you work through them honestly you "
    "will arrive at the answer yourself — which is the only version of it that will still be there "
    "in the assessment.",
    "Part B is the build, and unlike the assessment it tells you exactly where to click. Use that "
    "now. In the assessment you will be told what to build and left to find your own way around the "
    "console, so pay attention to where things live.",
    "Everything you design in Part A, you build in Part B. That is how the assessment works too.",
]

CURRENT_ARCH = [
    ("Region", [("Ledgerline is destined for the Sydney region, ap-southeast-2, in production. "
                 "Use it if it is available to you. ", False),
                ("In AWS Academy Learner Lab it will not be — build in us-east-1, or whichever "
                 "region you have.", True)]),
    ("Network", "VPC ledgerline-vpc, 10.20.0.0/16"),
    ("Subnets", "zone names below follow us-east-1  ·  public-web-a  10.20.1.0/24  (us-east-1a)  ·  "
                "public-web-b  10.20.2.0/24  (us-east-1b)  ·  private-app-a  10.20.11.0/24  "
                "(us-east-1a)  ·  private-data-a  10.20.21.0/24  (us-east-1a)  ·  private-data-b  "
                "10.20.22.0/24  (us-east-1b)"),
    ("Where the load actually is", "everything serving Ledgerline runs in us-east-1a. public-web-b "
                                   "and private-data-b exist only because the load balancer and the "
                                   "database subnet group each refuse to be created with one zone. "
                                   "Nothing has been placed in them."),
    ("Internet in", "internet gateway ledgerline-igw; public-rt routes 0.0.0.0/0 to it"),
    ("Internet out", "one NAT gateway ledgerline-nat in public-web-a; private-app-rt routes "
                     "private-app-a's 0.0.0.0/0 to it"),
    ("Compute", "Auto Scaling group across private-app-a only — desired 1, minimum 1, maximum 2; "
                "launch template ledgerline-lt (Amazon Linux, web server installed at boot)"),
    ("Load balancing", "internet-facing ALB ledgerline-alb in public-web-a and public-web-b, "
                       "HTTP :80, forwarding to target group ledgerline-tg"),
    ("Database", "PostgreSQL on RDS, single-AZ with no standby, gp3 20 GB, encrypted, in subnet "
                 "group ledgerline-db-subnet-group (private-data-a + private-data-b)"),
    ("Security groups", "ledgerline-alb-sg  HTTP 80 from anywhere  ·  ledgerline-app-sg  HTTP 80 "
                        "from the ALB group  ·  ledgerline-db-sg  PostgreSQL 5432 from the app group"),
    ("Monitoring", "one alarm, ledgerline-unhealthy-hosts, on UnHealthyHostCount"),
]

# ---------------------------------------------------------------- Part A — design
# Presented as the assessment presents it, plus `consider` — the leading questions.

DESIGN = [
    dict(n=1, title="The targets this design has to meet",
         resources=[
             ("Ledgerline Cloud Migration Requirements — the availability, recovery and service-level targets. The figures you need are here",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/migration-requirements"),
             ("Ledgerline Application Specification — the workload those targets are set against",
              f"{SITE}/intranet/s1-cl1-at3/ict/accounting-application-spec-cloud"),
         ],
         prompt="Before you design anything, establish what the design is held to. Record the "
                "availability, recovery and service-level targets the HA design must achieve, and "
                "name where each figure came from.",
         given=1, blank_rows=4,
         table=(["Requirement", "Target", "Where it came from"],
                [["Availability", "", ""], ["Recovery point objective (RPO)", "", ""],
                 ["Recovery time objective (RTO)", "", ""], ["Busiest period", "", ""]]),
         consider=["A target you cannot quote a source for is a target you invented. Where would a "
                   "figure like 'the system must be available 99.9% of the time' actually be "
                   "written down?",
                   "RPO and RTO are different questions. One asks how much work you can afford to "
                   "lose; the other asks how long you can afford to be down. Which is which?",
                   "Month-end is the busiest week of Ledgerline's month. Does that change what an "
                   "outage costs, and should the targets say so?"]),

    dict(n=2, title="Review the current environment against those targets",
         resources=[
             ("Ledgerline Server Status — what is actually running, tier by tier",
              f"{SITE}/intranet/s1-cl1-at3/ict/accounting-server-status-cloud"),
         ],
         prompt="Go through the current environment tier by tier. For each, say whether it meets "
                "the targets from task 1, and if it does not, why not.",
         given=1, blank_rows=6,
         table=(["Tier", "Meets the targets?", "Why / why not"],
                [["Network", "", ""], ["Compute", "", ""], ["Load balancing", "", ""],
                 ["Database", "", ""], ["Internet out", "", ""], ["Monitoring", "", ""]]),
         consider=["Read the 'Where the load actually is' row again. How many availability zones "
                   "have anything running in them?",
                   "The load balancer is listed as being in two subnets. Is that the same thing as "
                   "the service being in two zones? Which tier is it actually protecting?",
                   "The database row says single-AZ with no standby. If that instance stopped right "
                   "now, what is the fastest way Ledgerline comes back, and how long is that?",
                   "One tier here already meets the targets without any change. Which one, and can "
                   "you say why?"]),

    dict(n=3, title="Single points of failure",
         resources=[
             ("Ledgerline Server Status — read it looking for anything there is only one of",
              f"{SITE}/intranet/s1-cl1-at3/ict/accounting-server-status-cloud"),
         ],
         prompt="Identify every single point of failure in the current environment — every "
                "component whose failure takes Ledgerline down or degrades it below the targets. "
                "For each, say what the failure looks like and what finance loses.",
         given=0, blank_rows=6,
         table=(["Component", "Failure mode", "Consequence for finance"], []),
         consider=["Go down the architecture table one row at a time and ask: is there exactly one "
                   "of these? A component that exists once, in one place, is where to look.",
                   "AWS occasionally loses a whole availability zone. If us-east-1a went dark this "
                   "afternoon, which of the things in the table above would go with it?",
                   "The Auto Scaling group has a minimum of 1. What does 'minimum 1' actually "
                   "guarantee while a replacement instance is booting?",
                   "The application servers reach the internet through something. There is one of "
                   "it. What stops working if it fails — and would you notice straight away?",
                   "You should end up with more than two rows here. If you have two, you have "
                   "missed something."]),

    dict(n=4, title="Recovery objectives the current environment actually achieves",
         resources=[
             ("Ledgerline Cloud Migration Requirements — the RPO and RTO you are measuring today's environment against",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/migration-requirements"),
         ],
         prompt="For each component, estimate what the current environment delivers today — how "
                "much data would be lost, and how long recovery would take. Put numbers on it.",
         given=1, blank_rows=3,
         table=(["Component", "Current RPO", "Current RTO", "Meets target?"],
                [["Application tier", "", "", ""], ["Database", "", "", ""],
                 ["Whole service", "", "", ""]]),
         consider=["The application tier holds no data. Does an RPO even mean anything for it?",
                   "If the database has automated backups and nothing else, how much work is lost "
                   "in the worst case — and what is the worst case?",
                   "Restoring a database backup is not instant. Think about how long it takes to "
                   "restore, point the application at it, and confirm it works.",
                   "Compare each number you write against the task 1 target on the same row. If it "
                   "does not meet it, that is the gap the rest of this design closes."]),

    dict(n=5, title="Components that have to scale vertically",
         resources=[
             ("Ledgerline Application Specification — the load each tier carries",
              f"{SITE}/intranet/s1-cl1-at3/ict/accounting-application-spec-cloud"),
         ],
         prompt="Some components can only be made bigger, not more numerous. Identify which "
                "components here are in that position, and what happens to availability while they "
                "are being resized.",
         given=0, blank_rows=4,
         table=(["Component", "Why it must scale vertically", "Availability impact while it scales"], []),
         consider=["For each tier, ask: to handle more load, do I add another one, or do I replace "
                   "it with a bigger one?",
                   "The Auto Scaling group exists precisely so one tier does not have this problem. "
                   "Which tier, and why does that make it the exception?",
                   "If a component has to be resized and there is nothing else serving while it "
                   "happens, what does the user see?"]),

    dict(n=6, title="Summarise your review",
         resources=[
             ("Ledgerline Migration Role Brief — who you are writing this summary for",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/role-brief"),
         ],
         prompt="Write a short summary of what you found: the gap between the current environment "
                "and the targets from task 1, and which components drive that gap. Write it for the "
                "YAT ICT Manager, not for another engineer. Around 200 words.",
         consider=["Your reader signs off the work and pays for it. What do they need to know that "
                   "they cannot get from a diagram?",
                   "Name the gap in the same terms as the targets — a percentage, an amount of lost "
                   "work, a number of hours. 'Not highly available' is not a gap.",
                   "If you had to cut this to two sentences, which two would you keep?"]),

    dict(n=7, title="Design — the network",
         resources=[
             ("Ledgerline Solution Design — the addressing plan and naming conventions already in use",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/solution-design"),
         ],
         prompt="Your application tier has to be able to run in two availability zones. Look at the "
                "subnets that already exist. What do you need to add, and where? Record the subnet "
                "or subnets you are designing, then sketch the network you are aiming for.",
         given=0, blank_rows=2,
         table=(["Subnet name", "CIDR", "Zone", "What it carries"], []),
         diagram="the environment you are designing — both zones, and which resources sit in each",
         consider=["List the five existing subnets and mark which zone each is in. Which layer of "
                   "the architecture has a subnet in only one zone?",
                   "There are already subnets in the second zone. Why can the application servers "
                   "not simply use one of those? What are they for?",
                   "Look at how the existing subnets are named. The name tells you what it carries "
                   "and where it is — follow that pattern.",
                   "The VPC is 10.20.0.0/16 and the app subnet in the first zone is 10.20.11.0/24. "
                   "What is the obvious next range that does not collide with anything?"]),

    dict(n=8, title="Design — the application tier",
         resources=[
             ("Ledgerline Application Specification — the concurrent load and the month-end peak your capacity numbers have to carry",
              f"{SITE}/intranet/s1-cl1-at3/ict/accounting-application-spec-cloud"),
         ],
         prompt="You now have somewhere for a second application server to run. Design the Auto "
                "Scaling group's configuration so the loss of one availability zone leaves "
                "Ledgerline serving. Give a reason for the capacity numbers you choose.",
         given=1, blank_rows=5,
         table=(["Setting", "Your design", "Why"],
                [["Subnets", "", ""], ["Minimum", "", ""], ["Desired", "", ""],
                 ["Maximum", "", ""], ["Scaling policy", "", ""]]),
         consider=["If the group can launch into two subnets but its minimum is 1, where is that "
                   "one instance? Is it guaranteed to be in the zone that survives?",
                   "Work it backwards: a zone fails, and you need at least one healthy server "
                   "still serving. What is the smallest minimum that guarantees it?",
                   "Maximum is about handling load, not surviving failure. What does month-end do "
                   "to Ledgerline, and does your maximum leave room for it?",
                   "The scaling policy was not the problem. Is there any reason to change it?"]),

    dict(n=9, title="Design — the load balancer",
         prompt="What did you decide about the load balancer, and why? Look at what is already "
                "there before you answer.",
         consider=["Which subnets is the load balancer already in? Check the architecture table "
                   "before you answer, not after.",
                   "When the Auto Scaling group launches an instance into your new subnet, who "
                   "registers it in the target group — you, or something else?",
                   "'Make it highly available' is the reflex answer. Is there anything actually "
                   "left to do here? Saying no, with a reason, is a real answer."]),

    dict(n=10, title="Design — the database",
         resources=[
             ("Ledgerline HA Database Requirements — what the database specifically has to achieve",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/ha-database-requirements"),
             ("Ledgerline Cloud Migration Requirements — the RPO and RTO the change has to deliver",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/migration-requirements"),
         ],
         prompt="The database is the component with the worst recovery numbers in task 4. Design "
                "the change that fixes it, and state what it gives you that the current "
                "configuration does not. The settings worth considering include how the deployment "
                "is spread across availability zones and how long backups are kept.",
         given=0, blank_rows=4,
         table=(["Setting", "Your design", "Why"], []),
         consider=["Your task 4 RTO for the database was measured in hours. What would have to be "
                   "true for it to be measured in minutes instead?",
                   "A standby copy in another zone can take over automatically. What does that do "
                   "to your RTO, and what does it not do to your RPO?",
                   "The application connects to the database by a name. If the standby takes over, "
                   "does that name change? What would it mean for the application if it did?",
                   "Backups solve a different problem from a standby. Which of your two numbers "
                   "does each one address?"]),

    dict(n=11, title="Design — the outbound path",
         prompt="Your application tier will now run in two zones. Think about what the servers in "
                "the new zone use to reach the internet. Design your answer, and be explicit if you "
                "are accepting a risk rather than removing it. Things you might record here: the "
                "gateway itself, and the route table that decides where a subnet's traffic goes.",
         given=0, blank_rows=4,
         table=(["Setting", "Your design", "Why"], []),
         consider=["There is one NAT gateway and it lives in public-web-a. Which zone is that?",
                   "Your new servers are in the second zone. Whose gateway are they using to reach "
                   "the internet, and what happens to them if the first zone fails?",
                   "You have just designed around a zone failure everywhere else. Would it be "
                   "consistent to leave this one depending on that zone?",
                   "A second gateway costs money and Ledgerline is a finance system with a budget. "
                   "Accepting the risk and writing down what breaks is a legitimate engineering "
                   "answer — but only if you write it down."]),

    dict(n=12, title="Design — monitoring",
         resources=[
             ("Ledgerline Cloud Migration Requirements — the service levels your monitoring reports against",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/migration-requirements"),
         ],
         prompt="The existing alarm tells you a target is unhealthy. It does not tell you a zone "
                "has gone or a database has failed over. Design the monitoring that would tell you, "
                "and say what each alarm detects. An alarm needs a metric, a threshold and a "
                "failure it would catch.",
         given=0, blank_rows=4,
         table=(["Alarm", "What it measures", "Threshold", "What it detects"], []),
         consider=["After your design, Ledgerline survives losing a zone. If that happened at 2am "
                   "on a Sunday, would anything tell you? Should it?",
                   "The existing alarm counts unhealthy hosts across the whole load balancer. If "
                   "one zone went dark and the other kept serving, would that count change enough "
                   "to fire?",
                   "A database failover is invisible to users if it works. Is 'invisible' the same "
                   "as 'nobody needs to know'?",
                   "For each alarm you design, finish this sentence: 'this fires when ___, which "
                   "means ___ has happened.' If you cannot, the threshold is guesswork."]),

    dict(n=13, title="Which single points of failure does your design remove?",
         prompt="Go back to your answer to task 3. For each single point of failure you found "
                "there, say what in your design removes it — or state plainly that it remains, and "
                "why you accepted it.",
         given=0, blank_rows=5,
         table=(["Point of failure (from task 3)", "Removed by", "Or accepted because"], []),
         consider=["Copy your task 3 list across first, before you write anything in the other "
                   "columns. Every row has to be accounted for.",
                   "If one of them is still there, that is not a failure — an accepted, documented "
                   "risk is a design position. An unmentioned one is an oversight.",
                   "Is there anything in your design that removes a point of failure you did not "
                   "list in task 3? If so, task 3 was incomplete — go back and fix it."]),

    dict(n=14, title="Recovery objectives your design achieves",
         resources=[
             ("Ledgerline Cloud Migration Requirements — the targets you are checking your design against",
              f"{SITE}/intranet/s1-cl1-at3/projects/accounting-cloud-migration/migration-requirements"),
         ],
         prompt="Redo task 4 against your design. What does each component deliver now, and does "
                "the whole service meet the targets from task 1?",
         given=1, blank_rows=3,
         table=(["Component", "Designed RPO", "Designed RTO", "Meets target?"],
                [["Application tier", "", "", ""], ["Database", "", "", ""],
                 ["Whole service", "", "", ""]]),
         consider=["Put this table next to your task 4 answer. The point is the difference between "
                   "them — can you state it in one sentence?",
                   "If a standby takes over automatically, the RTO is roughly how long the failover "
                   "takes. Is that seconds, minutes, or hours?",
                   "Does the whole service now meet the task 1 targets? If not, say so and say why "
                   "— an honest gap beats a number you cannot defend."]),

    dict(n=15, title="What still has to scale vertically?",
         prompt="Redo task 5 against your design. Which components still can only be made bigger, "
                "and what does resizing cost you in availability now? Start from the components you "
                "listed in task 5.",
         given=0, blank_rows=3,
         table=(["Component", "Still scales vertically?", "Availability impact now"], []),
         consider=["Your design did not stop the database being one database. So what changed?",
                   "If there is a standby, which one gets resized first, and what happens after "
                   "that?",
                   "Compare the availability impact you wrote in task 5 with what you would write "
                   "now. Is it the same event, costing less?"]),

    dict(n=16, title="Is your design complete?",
         prompt="Read back over tasks 7 to 15 as one document. Does it hang together — does every "
                "layer have an answer, do the answers agree with each other, and could someone "
                "build from it without asking you what you meant? Note anything you had to change "
                "on this read-through.",
         consider=["If you designed a second NAT gateway in task 11, did you also design the route "
                   "table that sends anything to it? A gateway with no route is decoration.",
                   "Does your Auto Scaling group in task 8 launch into a subnet that task 7 "
                   "actually creates?",
                   "Hand your design to the person next to you. Could they build it without asking "
                   "you a question? That is the bar.",
                   "Finding a contradiction here is a good outcome, not a bad one. Write down what "
                   "you changed."]),

    dict(n=17, title="The order you will do it in",
         resources=[
             ("Change Management Procedure — YAT's rules for changing a production system, and what a rollback plan has to contain",
              f"{SITE}/intranet/s1-cl1-at3/policies/change-management"),
         ],
         prompt="You have a maintenance window of about 3.5 hours. Plan the order you will apply "
                "your changes in. For each change give how long you expect it to take, what "
                "Ledgerline looks like to a user while it happens, how you will confirm it worked, "
                "and what you will do if it does not. State the total and the buffer you have left.",
         given=1, blank_rows=6,
         table=(["#", "Change", "Time", "Impact on Ledgerline", "How you verify it", "If it fails"],
                [["1", "", "", "", "", ""], ["2", "", "", "", "", ""], ["3", "", "", "", "", ""],
                 ["4", "", "", "", "", ""], ["5", "", "", "", "", ""],
                 ["Total", "", "", "", "", ""]]),
         consider=["Sort your changes into two piles: the ones that add something new, and the ones "
                   "that alter something already serving traffic. Which pile is safe to do first?",
                   "Creating a subnet affects nobody. Converting a database interrupts it. Does "
                   "your order reflect that?",
                   "One of your changes takes far longer than the others and runs by itself once "
                   "started. Should it be near the beginning or the end?",
                   "For each row, finish: 'if this goes wrong, I will ___.' If the answer is 'keep "
                   "going and hope', you do not have a rollback.",
                   "Add your durations up. Is there time left? If the total is 3 hours 25, you have "
                   "no plan, you have a hope."]),

    dict(n=18, title="How you will prove it works",
         prompt="A design is a claim until something tests it. Plan the simulations you will run in "
                "Part B: at least one failure simulation and at least one resize simulation. For "
                "each, say what you will do, what you expect to happen, and how you will know "
                "whether it did.",
         given=2, blank_rows=3,
         table=(["#", "Simulation", "What you will do", "What you expect", "How you will know"],
                [["F1", "Instance failure", "", "", ""], ["F2", "Database failover", "", "", ""],
                 ["R1", "Resize", "", "", ""]]),
         consider=["To prove a server failure is survivable, you have to cause one. What is the "
                   "bluntest way to remove a running instance?",
                   "Writing down what you expect BEFORE you run it is the whole point — otherwise "
                   "whatever happens looks like what you expected.",
                   "How will you actually know Ledgerline stayed up? Watching the console is not "
                   "the same as watching the service.",
                   "'It worked' is not evidence. What would you screenshot, and when?"]),
]

# ---------------------------------------------------------------- Part B — implementation
# Click-by-click. The assessment deliberately withholds all of this.

BUILD = [
    dict(n=19, title="Deploy the practice baseline",
         from_q=None,
         job="Deploy the practice lab-pack. It builds the Ledgerline environment described above, "
             "so you start from the same place as everyone else.",
         steps=["Download the practice lab-pack template from where your teacher has put it.",
                [("Set your region first — the stack builds into whichever region is selected. ", False),
                 ("In the Learner Lab choose us-east-1.", True)],
                "Open CloudFormation → Create stack → With new resources (standard).",
                "Choose Upload a template file, select the template, and choose Next.",
                "Give the stack a name. Every parameter is already filled in except one: type a "
                "database master password, at least 8 characters. Write it down — you will not "
                "be shown it again, and nothing will remind you of it.",
                "Choose Next, then Next again, then Submit.",
                "Wait for CREATE_COMPLETE — about 10 minutes. The Events tab shows progress.",
                "Open EC2 → Load Balancers, copy the DNS name of ledgerline-alb, and open it in a "
                "browser tab to confirm the page loads. Type http:// in front of it — the load balancer only listens on HTTP port 80, and a browser left to itself will try HTTPS and fail."],
         clicks=["If the stack fails, open the Events tab and scroll to the FIRST red row — that is "
                 "the cause. Everything below it is the rollback.",
                 "A stack that rolled back has to be deleted before you can try again with the same "
                 "name."],
         capture="the stack at CREATE_COMPLETE, and the page loading through the load balancer.",
         standard=None, uoc=[]),

    dict(n=20, title="Create the application subnet in the second zone",
         from_q=7,
         job="Create the subnet you designed in task 7. Copy your answer across first, then build "
             "exactly that.",
         clicks=["Open the VPC console.",
                 "In the left menu choose Subnets, then Create subnet.",
                 "VPC ID: choose ledgerline-vpc.",
                 "Subnet name: the name from your task 7 answer.",
                 "Availability Zone: the second zone — us-east-1b if you are in the Learner Lab. "
                 "Do not leave this on 'No preference'; the console will pick for you and it may "
                 "pick the wrong one.",
                 "IPv4 subnet CIDR block: the range from your task 7 answer.",
                 "Choose Create subnet.",
                 "Check the Availability Zone column in the subnet list. If it says us-east-1a, "
                 "delete it and do it again."],
         capture="the subnet list filtered to ledgerline-vpc, showing your new subnet and its zone.",
         standard=None, uoc=[]),

    dict(n=21, title="Give the new subnet a path out",
         from_q=11,
         job="Build the outbound path you designed in task 11. If you designed a second NAT "
             "gateway, create it and its route table now. If you accepted the shared gateway, "
             "associate your new subnet with the existing private route table instead.",
         clicks=["If you designed a SECOND NAT GATEWAY — VPC console → NAT gateways → Create NAT "
                 "gateway.",
                 "Name it, set Subnet to public-web-b (a NAT gateway goes in a PUBLIC subnet, not "
                 "the private one it serves), Connectivity type Public, and Allocate Elastic IP.",
                 "Choose Create NAT gateway, then wait until State reads Available. This takes a "
                 "few minutes and you cannot route to it until it does.",
                 "VPC console → Route tables → Create route table. Name it, VPC ledgerline-vpc.",
                 "Open the new route table → Routes tab → Edit routes → Add route. Destination "
                 "0.0.0.0/0, Target NAT Gateway, then pick the one you just made. Save changes.",
                 "Subnet associations tab → Edit subnet associations → tick your new subnet → Save.",
                 "If you ACCEPTED THE SHARED GATEWAY instead — open the existing private-app-rt, go "
                 "to Subnet associations, and add your new subnet to it.",
                 "Either way, check the Routes tab shows 0.0.0.0/0 pointing somewhere and the "
                 "status reads Active."],
         capture="the route table associated with your new subnet, showing its 0.0.0.0/0 route and "
                 "the target it points at.",
         standard=None, uoc=[]),

    dict(n=22, title="Extend the application tier across both zones",
         from_q=8,
         job="Edit the Auto Scaling group to match your task 8 design — the subnets it launches "
             "into, and its capacity. Then wait for the second instance to become healthy.",
         note="a new instance is not healthy the moment it launches — it has to boot and start its "
              "web server first, and until it does the target group reports it Unhealthy with "
              "Request timed out. On Linux that is quick — a minute or two. On a Windows server, which "
              "is what the assessment uses, expect about six minutes and allow up to ten. Either "
              "way the rule is the same: wait. Do "
              "not terminate it or change settings because it looks stuck.",
         clicks=["Open EC2 → Auto Scaling groups and select ledgerline-asg.",
                 "Details tab → Network → Edit. Add your new subnet so BOTH application subnets are "
                 "selected, then Update.",
                 "Details tab → Capacity overview → Edit. Set Desired capacity, and the Scaling "
                 "limits minimum and maximum, to your task 8 numbers, then Update.",
                 "Activity tab — watch for a new instance launching. It takes a few minutes.",
                 "Instance management tab — confirm you have two instances and that their "
                 "Availability Zone values are different.",
                 "EC2 → Target Groups → ledgerline-tg → Targets tab. Both instances should reach "
                 "healthy. If one stays unhealthy, check its security group and the health check "
                 "path before assuming the instance is broken."],
         capture="the Auto Scaling group's instances showing two different zones, and the target "
                 "group showing both healthy.",
         standard=None, uoc=[]),

    dict(n=23, title="Convert the database",
         from_q=10,
         job="Apply the database change you designed in task 10. Start this before the monitoring "
             "task — it runs in the background and takes the longest of anything here.",
         clicks=["Open RDS → Databases and select the Ledgerline database.",
                 "Choose Modify.",
                 "Under Availability & durability, change the deployment option to create a standby "
                 "in another availability zone.",
                 "Choose Continue.",
                 "Under Scheduling of modifications choose Apply immediately. If you leave it on "
                 "'during the next maintenance window' nothing will happen today.",
                 "Choose Modify DB instance.",
                 "The status goes to Modifying and stays there for a while — 20 minutes or more is "
                 "normal. Go and do the next task; come back to it.",
                 "When it finishes, open the Configuration tab and confirm Multi-AZ now reads Yes, "
                 "with a secondary zone listed."],
         capture="the database's Configuration tab showing the standby and the zone it is in.",
         standard=None, uoc=[]),

    dict(n=24, title="Build your HA monitoring",
         from_q=12,
         job="Create the alarms you designed in task 12. Build at least the first one; build the "
             "others if you have time.",
         clicks=["Open CloudWatch → Alarms → All alarms → Create alarm.",
                 "Choose Select metric, then find the metric from your task 12 answer. Type the "
                 "metric name into the filter box to narrow it down — for per-zone target "
                 "health that is HealthyHostCount, which appears under ApplicationELB → Per "
                 "AppELB, per AZ, per TG Metrics. The similarly-named Per AppELB, per TG "
                 "Metrics has no zone breakdown, so pick the one with AZ in the name.",
                 "If you designed something about the database instead, its metrics are under "
                 "RDS → DBInstanceIdentifier — that is the per-database grouping, named for "
                 "its dimension rather than for what it contains. DatabaseConnections and "
                 "FreeStorageSpace both live there.",
                 "One thing you cannot build here: a database failover is an RDS event, not a "
                 "CloudWatch metric. If that is what you designed, it is set up under RDS → "
                 "Event subscriptions, choosing source type Instances and the Failover "
                 "category. That is a different screen from this one and it notifies SNS "
                 "directly, without an alarm in between.",
                 "If you see more than one target group listed, pick the one your load balancer is "
                 "using now — CloudWatch keeps metrics for deleted resources, so anything you "
                 "created and removed earlier is still shown. An alarm pointed at an old one "
                 "never fires.",
                 "Pick the metric, choose Select metric.",
                 "Set Statistic and Period to suit what you are watching, then set the threshold "
                 "from your design.",
                 "Next → choose the existing notification topic, or skip notification if there "
                 "isn't one.",
                 "Next → give the alarm the name from your design → Next → Create alarm.",
                 "Wait for the state to settle. A new alarm reads INSUFFICIENT_DATA for a few "
                 "minutes; that is normal, not a fault.",
                 "If you built an alarm on database connections, expect it to go straight into "
                 "ALARM and stay there. The servers only serve a placeholder page — the "
                 "accounting application itself was never installed, so nothing ever connects "
                 "to the database. Your alarm is right; the practice environment just cannot "
                 "give it anything to measure. Note that rather than changing the alarm."],
         capture="your new alarm in the CloudWatch console, showing its metric, threshold and state.",
         standard=None, uoc=[]),
]

# ---------------------------------------------------------------- tests and simulations

TESTS = [
    dict(n="T1", title="Confirm every tier still works, in both zones",
         job="Before you break anything deliberately, confirm what you have just changed is "
             "healthy. A simulation against a broken environment tells you nothing.",
         steps=["Open the load balancer's DNS name in a browser — with http:// in front — and "
                "confirm the page loads.",
                "Open the target group and confirm both instances are healthy, in two different "
                "zones.",
                "Connect to one instance with Session Manager and run the first command below. "
                "'succeeded!' means the application tier reaches the database privately. Get the "
                "endpoint from RDS → Databases → your database → Connectivity & security.",
                "Now run the second command on your OWN computer, not on the instance. It must "
                "FAIL — that failure is the evidence. The database has no public address and its "
                "security group accepts the application tier only. Confirm it alongside RDS → "
                "Connectivity & security, where Publicly accessible reads No."],
         code=("Run these", ["# on the instance, via Session Manager - expect: succeeded!",
                             "nc -zv <YOUR-DB-ENDPOINT> 5432",
                             "",
                             "# on your own computer - expect it to time out",
                             "# Windows, in PowerShell:",
                             "Test-NetConnection <YOUR-DB-ENDPOINT> -Port 5432",
                             "# macOS or Linux, in Terminal:",
                             "nc -zv -w 10 <YOUR-DB-ENDPOINT> 5432"]),
         capture="the page loading, the target group showing two healthy targets in two zones, and "
                 "the port test succeeding.",
         standard=None, uoc=[]),

    dict(n="T2", title="Failure simulation",
         job="Run the failure simulation you planned in task 18. Watch what happens to Ledgerline "
             "while you do it — that is the evidence, not the console screen afterwards.",
         steps=["Open the load balancer address in a browser (http://, not https://) and keep "
                "reloading it.",
                "Execute the failure you planned — terminate an instance, or reboot the database "
                "with failover.",
                "Record the time, what the browser did, and how long before it was normal again.",
                "Confirm the environment recovered."],
         clicks=["To terminate an instance: EC2 → Instances → select one → Instance state → "
                 "Terminate. The Auto Scaling group will replace it — watch the ASG's Activity tab.",
                 "To fail the database over: RDS → Databases → select it → Actions → Reboot, and "
                 "tick Reboot with failover.",
                 "Do not do both at once. You want to know which one caused what."],
         capture="three things, whichever simulation you ran: the ACTION you took (the terminating instance, or the RDS event showing the failover); the SERVICE while it happened (your browser still loading the page — include a clock or timestamp if you can); and the RECOVERY (the Auto Scaling group activity showing the replacement, or the target group returning to healthy). If the service did go down, capture that honestly — a recorded outage is evidence, and you compare it against what you predicted in task 18.",
         standard=None, uoc=[]),

    dict(n="T3", title="Resize simulation",
         job="Run the resize simulation you planned in task 18, and measure what it costs in "
             "availability.",
         steps=["Keep the browser refreshing against the load balancer.",
                "Execute the resize you planned — change the desired capacity, or the database "
                "instance class.",
                "Record how long it took and whether Ledgerline was affected.",
                "Return the setting to where it was."],
         clicks=["Whichever resize you planned, keep the browser refreshing at the load balancer "
                 "address throughout — that is how you measure the impact.",
                 "IF YOU PLANNED TO RESIZE THE APPLICATION TIER — EC2 → Auto Scaling groups → your "
                 "group → Capacity overview → Edit. Raise Desired capacity by one and update. Watch "
                 "the Activity tab for the launch, then the target group until the new instance is "
                 "healthy. Nothing should go down: you are adding, not replacing.",
                 "IF YOU PLANNED TO RESIZE AN INSTANCE'S TYPE — you cannot change the type of a "
                 "running Auto Scaling instance. You change it in the LAUNCH TEMPLATE and let the "
                 "group replace instances with it: EC2 → Launch templates → your template → Actions "
                 "→ Modify template (create new version), change the instance type, then set the new "
                 "version as Default. Then EC2 → Auto Scaling groups → Instance refresh → Start "
                 "instance refresh to roll it through.",
                 "The refresh asks how to replace instances. Choose to LAUNCH BEFORE "
                 "TERMINATING, not terminate-and-launch. You are demonstrating a resize that "
                 "does not cost availability, so bringing the replacement up and waiting for "
                 "it to go healthy before killing the old one is the behaviour you want to "
                 "show. It needs room above your desired capacity to do that — if maximum "
                 "equals desired there is nowhere to launch into and it will fall back to "
                 "terminating first.",
                 "Expect the refresh to take a while: it replaces one instance at a time and "
                 "each one has to boot and install its web server before the next starts. On "
                 "Windows, budget fifteen to twenty minutes for two instances.",
                 "IF YOU PLANNED TO RESIZE THE DATABASE — RDS → Databases → select it → Modify → "
                 "change the DB instance class → Continue → Apply immediately → Modify DB instance. "
                 "On a Multi-AZ database this resizes the standby first and then fails over to it, "
                 "so the interruption is a failover rather than an outage — which is exactly the "
                 "point you are demonstrating. Expect several minutes.",
                 "Record the start and finish times and what the browser did in between. Then put "
                 "the setting back where it was."],
         capture="the resize in progress or complete, and what the service did while it happened — "
                 "the console showing the change, and your timings.",
         standard=None, uoc=[]),

    dict(n="T4", title="Measure availability across the window",
         job="Report what Ledgerline's availability actually was across the time you were working, "
             "and say how you measured it.",
         steps=["Open the target group's healthy-host metric for the period you were working.",
                "Identify every period where BOTH zones were at zero — that is the only real "
                "downtime. One zone dipping is the design working.",
                "Write one or two sentences saying what the graph shows.",
                "Note the time range on the capture, so the period it covers is unambiguous."],
         clicks=["CloudWatch → Metrics → Classic metrics (the console renamed what used to be All "
                 "metrics) → ApplicationELB → Per AppELB, per AZ, per TG "
                 "Metrics → "
                 "HealthyHostCount. Set the time range to cover your session.",
                 "Tick the row for EACH ZONE of your CURRENT target group — two rows, same load "
                 "balancer, one us-east-1a and one us-east-1b. If several load balancers are "
                 "listed, the live one is the one with your alarms shown against it in the "
                 "Alarms column; the others are deleted resources CloudWatch still remembers.",
                 "Set the graph type to STACKED AREA — the dropdown at the top right of the "
                 "graph. It is the right shape for this: the total height is the healthy "
                 "capacity serving Ledgerline, and each band is one zone's share, so losing a "
                 "zone makes the stack visibly shorter instead of hiding one line among "
                 "several.",
                 "Set the time range to cover your whole session, then read the graph.",
                 "READ IT LIKE THIS. A dip in ONE zone is not downtime — the other zone was "
                 "still serving, and that is exactly what your HA work bought. Downtime is "
                 "only when BOTH zones are at zero at the same moment. Measure those periods, "
                 "not every dip you can see.",
                 "Your resize may show a RISE rather than a dip, if you launched a replacement "
                 "before terminating the old instance. No dip at all is a result worth "
                 "recording — it means the resize cost nothing in availability.",
                 "You are NOT asked to calculate an availability percentage from this graph, and "
                 "you could not do it honestly anyway — the axis steps in tens of minutes, so a "
                 "short outage does not appear on it. The graph shows the shape: what was serving, "
                 "when, and whether anything went fully dark.",
                 "The arithmetic belongs to the knowledge questions, and it comes from YOUR OWN "
                 "TIMINGS during the simulations, not from this picture. If you noted that the "
                 "failover took 47 seconds out of a 3-hour window, that is 47 seconds out of "
                 "10,800 — about 99.6% available. Keep those timings; that is the calculation you "
                 "will be asked to show."],
         capture="the metric graph across your session, with the calculation you made from it.",
         standard=None, uoc=[]),
]

# ---------------------------------------------------------------- closing out

CLOSEOUT = [
    dict(n=25, title="What actually happened, against what you predicted",
         prompt="Go back to task 18. For each simulation, put your expected outcome next to what "
                "actually happened. Where they differ, say why.",
         given=1, blank_rows=3,
         table=(["#", "What you expected (task 18)", "What actually happened", "Why they differ"],
                [["F1", "", "", ""], ["F2", "", "", ""], ["R1", "", "", ""]]),
         consider=["If something matched exactly, say what that confirms — not just that it matched.",
                   "A failover that took 90 seconds when you predicted 'brief' is a difference. "
                   "What does 'brief' mean now that you have measured it?",
                   "Did anything surprise you? Surprises are the most useful rows in this table."]),

    dict(n=26, title="What you changed as a result",
         prompt="Did your simulations reveal anything you needed to fix? If so, say what you "
                "changed and why. If nothing needed changing, say that — and say what evidence "
                "makes you confident.",
         consider=["'Nothing broke' and 'I have evidence it works' are different claims. Which one "
                   "can you make?",
                   "If a recovery took longer than your task 1 target, that is a gap. What would "
                   "you do about it?",
                   "If an alarm you built never fired during any of this, is that because nothing "
                   "went wrong, or because the threshold is wrong?"]),
]


# ---------------------------------------------------------------- cleaning up
# Order matters and is not the reverse of the build order. The stack owns the VPC, and
# CloudFormation cannot delete a VPC that still holds a subnet it did not create — so
# everything built by hand has to go BEFORE the stack, and the instances have to go before
# the subnet they sit in. Deleting the stack first fails at the last step.

CLEANUP_INTRO = [
    "Your lab has a credit budget, and everything above keeps spending it whether you are using "
    "it or not. When you have finished, unwind it in the order below.",
    "The order is not simply the reverse of the way you built it. The CloudFormation stack owns "
    "the network everything sits in, so it has to go last — and it will refuse to delete while "
    "anything you built by hand is still inside it.",
]

CLEANUP = [
    ("Empty the Auto Scaling group",
     "EC2 → Auto Scaling groups → your group → Capacity overview → Edit. Set Desired, Minimum "
     "and Maximum all to 0 and update. Wait until the Instance management tab is empty. Do not "
     "terminate the instances directly — the group will just launch replacements."),
    ("Delete the NAT gateway you created by hand",
     "VPC → NAT gateways → select the one you made in task 21 → Actions → Delete. Wait until "
     "State reads Deleted. The stack's own NAT gateway is not yours to delete; the stack takes "
     "that one."),
    ("Release its Elastic IP",
     "VPC → Elastic IPs. The one with no Name and nothing associated is the address that NAT "
     "gateway was using — deleting the gateway does not release it, and an unattached address "
     "bills by the hour. Select it → Actions → Release Elastic IP addresses. If the release "
     "fails, the gateway has not finished deleting; wait two minutes and try again."),
    ("Delete the route table you created by hand",
     "VPC → Route tables → the one you made in task 21 → Actions → Delete route table. "
     "Deleting it removes its subnet association for you."),
    ("Delete the subnet you created by hand",
     "VPC → Subnets → the one you made in task 20 → Actions → Delete subnet. If it refuses "
     "because of a network interface, something in it has not finished terminating — wait a "
     "couple of minutes and try again."),
    ("Delete the CloudFormation stack",
     "CloudFormation → your stack → Delete. This takes everything else with it: the VPC, the "
     "remaining subnets, the load balancer, the database, the launch template, the alarms and "
     "the stack's own NAT gateway and Elastic IP. Wait for it to disappear from the list."),
    ("Check nothing survived",
     "VPC → Your VPCs should no longer list yours. Check Elastic IPs is empty — an address left "
     "allocated is the most common thing to miss, and the only one that keeps costing after "
     "everything else is gone."),
]
