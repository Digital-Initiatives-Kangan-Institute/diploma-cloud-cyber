#!/usr/bin/env python3
"""The S1-CL1 AT2 PRACTICE build run sheet — content.

Same shape as the assessment run sheet, different everything else. A student who works
through this has rehearsed every skill the assessment needs without having seen its answers:

  scenario   Ledgerline, YAT's accounting system — not the LMS
  addresses  10.20.x.x — not 10.0.x.x
  servers    Amazon Linux — not Windows
  database   PostgreSQL on 5432 — not MySQL on 3306
  detail     every task carries click-by-click steps. The assessment deliberately does not.

This is a practice exercise, not an assessment: no marking criteria, no UoC tags, no
institutional boilerplate. Rendered by the shared renderer in at2_run_sheet.
"""

SCENARIO = [
    "YAT College runs its finance function on Ledgerline, an accounting system that has lived on a "
    "server under a desk in the finance office for eleven years. Finance staff reach it from campus "
    "and, increasingly, from home. It is being moved to AWS.",
    "You are an MTS Consultant on the Ledgerline migration. Senior Architecture has produced the "
    "design and an implementation lead has turned it into the run sheet below. Your job is to build "
    "it.",
    "This is practice. Nothing here is marked, and nothing you build here is submitted. It is the "
    "same shape of work as your assessment, on a different system with different settings, so that "
    "working through it teaches you the moves without handing you the answers.",
]

INSTRUCTIONS = [
    "Work the tasks in order. Each one tells you what to build, the settings to build it to, and "
    "the clicks to get there.",
    "Take a screenshot at the end of each task even though nobody is marking them. In the "
    "assessment you will need one per task, and building the habit here is the point.",
    "When something does not work, read the error before changing anything. Most of what goes "
    "wrong in this build is a setting in the wrong place rather than something broken.",
    "Delete everything when you finish a session. The lab charges for the NAT gateway and the load "
    "balancer whether you are using them or not.",
]

REGION_NOTE = ("Build in us-east-1. Ledgerline is destined for ap-southeast-2 in production, but the "
               "lab environment runs in us-east-1 and that is where you will work.")

TASKS = [
    dict(n=1, title="Sign in and confirm your working region",
         job="Sign in to the AWS console and check which region you are in.",
         settings=[("Region", "us-east-1")],
         clicks=["Start the lab and open the AWS console.",
                 "Look at the region selector in the top-right of the black bar.",
                 "If it does not read N. Virginia (us-east-1), click it and choose that region."],
         capture="the console with the region selector visible."),

    dict(n=2, title="Create the VPC",
         job="Create the private network everything else sits inside.",
         settings=[("Name", "ledgerline-vpc"), ("IPv4 CIDR", "10.20.0.0/16"),
                   ("DNS hostnames", "Enabled"), ("DNS resolution", "Enabled")],
         clicks=["Search VPC in the top search bar and open it.",
                 "Choose Your VPCs in the left menu, then Create VPC.",
                 "Choose VPC only, not VPC and more. The wizard creates subnets for you and you "
                 "want to create them yourself.",
                 "Enter the name and the CIDR, leave the rest as it is, and Create VPC.",
                 "On the VPC page, Actions, Edit VPC settings, and tick both DNS options."],
         evidence_note="No screenshot needed. Creating the VPC is a prerequisite step — "
                       "everything that follows is built inside it."),

    dict(n=3, title="Create the subnets",
         job="Create five subnets: three for the workload, two more that exist only because two "
             "AWS services refuse to be created with subnets in a single zone.",
         settings=[("ledgerline-public-a", "10.20.1.0/24  —  zone  us-east-1a"),
                   ("ledgerline-public-b", "10.20.2.0/24  —  zone  us-east-1b"),
                   ("ledgerline-app-a", "10.20.11.0/24  —  zone  us-east-1a"),
                   ("ledgerline-data-a", "10.20.21.0/24  —  zone  us-east-1a"),
                   ("ledgerline-data-b", "10.20.22.0/24  —  zone  us-east-1b")],
         clicks=["In the VPC console choose Subnets, then Create subnet.",
                 "Select ledgerline-vpc at the top.",
                 "For each subnet: type the name, CHOOSE THE ZONE from the dropdown, type the "
                 "CIDR, then Add new subnet for the next one.",
                 "Do not leave the zone on No preference. If two subnets that should be in "
                 "different zones land in the same one, the load balancer and the database will "
                 "both refuse to create later and the error will not mention subnets.",
                 "Create subnet once all five are filled in."],
         capture="the subnet list showing all five, with the Availability Zone column visible."),

    dict(n=4, title="Create the internet gateway",
         job="Create the gateway that gives the public subnets a path to the internet.",
         settings=[("Name", "ledgerline-igw"), ("Attach to", "ledgerline-vpc")],
         clicks=["VPC console, Internet gateways, Create internet gateway.",
                 "Name it and Create.",
                 "It appears as Detached. Choose Actions, Attach to VPC, pick ledgerline-vpc, "
                 "and Attach."],
         capture="the internet gateway showing State: Attached."),

    dict(n=5, title="Create the NAT gateway",
         job="Create the gateway that lets the application servers reach out to the internet "
             "without anything being able to reach in.",
         settings=[("Name", "ledgerline-nat"), ("Subnet", "ledgerline-public-a"),
                   ("Connectivity type", "Public"), ("Elastic IP", "allocate a new one")],
         clicks=["VPC console, NAT gateways, Create NAT gateway.",
                 "Name it, choose ledgerline-public-a as the subnet, leave Connectivity type as "
                 "Public.",
                 "Click Allocate Elastic IP.",
                 "Create NAT gateway, then wait. It takes a few minutes to leave Pending, and you "
                 "cannot route to it until it reads Available."],
         capture="the NAT gateway showing State: Available with its Elastic IP."),

    dict(n=6, title="Create the route tables",
         job="Create two route tables. The data subnets get neither — they stay on the VPC "
             "default, which has no route out, which is what a database tier should have.",
         settings=[("ledgerline-public-rt", "associated with both public subnets; 0.0.0.0/0 → the "
                                            "internet gateway"),
                   ("ledgerline-app-rt", "associated with ledgerline-app-a; 0.0.0.0/0 → the NAT "
                                         "gateway"),
                   ("The data subnets", "leave them alone")],
         clicks=["VPC console, Route tables, Create route table. Name it, choose ledgerline-vpc, "
                 "Create. Repeat for the second one.",
                 "Open the public route table, Routes tab, Edit routes, Add route.",
                 "Destination 0.0.0.0/0, Target Internet Gateway, pick ledgerline-igw, Save.",
                 "Subnet associations tab, Edit subnet associations, tick BOTH public subnets, Save.",
                 "Open the app route table and do the same, but choose NAT Gateway as the target "
                 "and associate only ledgerline-app-a."],
         capture="both route tables showing their routes and their subnet associations."),

    dict(n=7, title="Create the three security groups",
         job="Create the firewall rules that let each tier talk only to the tier next to it.",
         settings=[("ledgerline-alb-sg", "inbound HTTP 80 from 0.0.0.0/0"),
                   ("ledgerline-app-sg", "inbound HTTP 80 from ledgerline-alb-sg"),
                   ("ledgerline-db-sg", "inbound PostgreSQL 5432 from ledgerline-app-sg"),
                   ("Outbound", "leave the default on all three")],
         clicks=["VPC console, Security groups, Create security group.",
                 "Create all three with names and descriptions first and no inbound rules at all. "
                 "Two of them need to name another as a source, which you cannot do until it "
                 "exists.",
                 "Do not start a name with sg- : AWS reserves that prefix for the IDs it generates "
                 "and will reject the name.",
                 "Now open ledgerline-alb-sg, Edit inbound rules, Add rule: type HTTP, source "
                 "Anywhere-IPv4. Save.",
                 "Open ledgerline-app-sg, Add rule: type HTTP, source Custom, and start typing "
                 "ledgerline-alb-sg — pick it from the list. Save.",
                 "Open ledgerline-db-sg, Add rule: type PostgreSQL, source Custom, "
                 "ledgerline-app-sg. Save."],
         capture="all three security groups with their inbound rules expanded."),

    dict(n=8, title="Configure the access model",
         job="Create the group that will run Ledgerline after the migration, and an account in it. "
             "Fill in each form with the values below, submit it, and capture what comes back.",
         note="the lab environment does not let you create groups or users. You will be refused. "
              "That is the environment, not your work — and the refusal is what you capture. Do "
              "the task properly anyway: filling the form correctly is the part worth practising.",
         settings=[("Group name", "YAT-Finance-Ops"),
                   ("Policy on the group", "ReadOnlyAccess — filter for it and pick the policy "
                                           "named exactly that, not a service-specific one"),
                   ("User name", "ledgerline-ops"),
                   ("Policy on the user", "CloudWatchFullAccess"),
                   ("Expected result", "both submissions refused with a permissions error")],
         clicks=["Search IAM in the top search bar and open it.",
                 "Choose User groups, then Create group. Enter the group name.",
                 "Under Attach permissions policies, filter for ReadOnlyAccess and tick the one "
                 "named exactly that. Create group. Capture the error.",
                 "Now choose Users, then Create user. Enter the user name.",
                 "On the permissions page choose Attach policies directly, filter for "
                 "CloudWatchFullAccess and tick it. Work through to Create user, and capture the "
                 "error."],
         captures=["the completed group form — YAT-Finance-Ops with ReadOnlyAccess attached — and "
                   "the error returned.",
                   "the completed user form — ledgerline-ops with CloudWatchFullAccess attached — "
                   "and the error returned."],
         decision=("This group can see everything but cannot change anyone's permissions — "
                   "including its own. Why not simply let the team that runs Ledgerline manage "
                   "its own access?",
                   "Because a group that can rewrite its own permissions has no limit at all — it "
                   "can grant itself anything, so the boundary is only as strong as everyone's "
                   "restraint. Keeping identity with whoever governs the account means the "
                   "finance team can operate the system fully without being able to widen their "
                   "own access.")),

    dict(n=9, title="Look at the role your servers will use",
         job="Find the role the lab provides for instances and read what it allows. You cannot "
             "create your own here, so this is a look rather than a build.",
         settings=[("Where", "IAM → Roles"), ("Open", "LabRole"),
                   ("Write down", "the name, for task 9")],
         clicks=["Search IAM and open it, then choose Roles.",
                 "Find LabRole in the list and open it.",
                 "Look at the Permissions tab and read which services it grants access to."],
         capture="the LabRole page with its permissions visible."),

    dict(n=10, title="Create the launch template",
         job="Create the template that defines how every application server is built. The Auto "
             "Scaling group builds servers from it, so nothing is configured by hand.",
         settings=[("Name", "ledgerline-lt"),
                   ("AMI", "Amazon Linux 2023"),
                   ("Instance type", "your choice — see the decision below"),
                   ("Key pair", "do not include"),
                   ("Subnet", "do not include"),
                   ("Security group", "ledgerline-app-sg"),
                   ("Root volume", "gp3, 8 GB"),
                   ("Advanced details → IAM instance profile", "LabInstanceProfile"),
                   ("Advanced details → User data", "the script below")],
         code=("User data", [
             "#!/bin/bash",
             "dnf install -y nginx",
             "echo '<h1>Ledgerline</h1><p>Infrastructure ready.</p>' \\",
             "     > /usr/share/nginx/html/index.html",
             "systemctl enable --now nginx",
         ]),
         clicks=["EC2 console, Launch templates, Create launch template.",
                 "Name it. Tick Provide guidance to help me set up a template.",
                 "Application and OS Images: choose Amazon Linux 2023.",
                 "Instance type: whichever of the two you chose below.",
                 "Key pair: choose Don't include in launch template.",
                 "Network settings: leave the subnet blank. Under Security groups pick "
                 "ledgerline-app-sg. Getting this wrong is the most common reason the servers "
                 "later come up unreachable.",
                 "Storage: set the root volume to 8 GB, gp3.",
                 "Expand Advanced details. Find IAM instance profile and choose "
                 "LabInstanceProfile.",
                 "Scroll to the bottom of Advanced details to User data and paste the script "
                 "exactly as written, including the first line.",
                 "Create launch template."],
         capture="the launch template summary showing the AMI, instance type, security group and "
                 "instance profile.",
         decision=("Choose the instance type for the application tier: t3.micro or t3.small. Name "
                   "the one you did not choose, say which you chose, and explain why against what "
                   "Ledgerline actually has to do — a finance system used by a small team, all of "
                   "them on campus or at home, never by students.",
                   "t3.micro has 1 GiB of memory and t3.small has 2 GiB. Amazon Linux and nginx "
                   "together use a small fraction of 1 GiB, and Ledgerline serves a finance team "
                   "rather than a whole college, so t3.micro carries this workload comfortably "
                   "and t3.small would be paying for headroom nothing uses. I chose t3.micro. If "
                   "the user count grew, the Auto Scaling group adds servers before the instance "
                   "type needs revisiting.")),

    dict(n=11, title="Create the target group",
         job="Create the list of servers the load balancer will send traffic to, and the health "
             "check that decides which of them are fit to receive it.",
         settings=[("Name", "ledgerline-tg"), ("Target type", "Instances"),
                   ("Protocol and port", "HTTP, 80"), ("VPC", "ledgerline-vpc"),
                   ("Health check path", "/"), ("Register targets", "skip")],
         clicks=["EC2 console, Target groups, Create target group.",
                 "Choose Instances as the target type.",
                 "Name it, leave protocol HTTP and port 80, choose ledgerline-vpc.",
                 "Leave the health check as HTTP with path /.",
                 "Next. On the register targets page, register nothing and choose Create target "
                 "group. The Auto Scaling group will add servers for you."],
         evidence_note="No screenshot needed. Creating the target group is a prerequisite step — "
                       "the load balancer sends traffic to it, and the Auto Scaling group fills "
                       "it with servers."),

    dict(n=12, title="Create the load balancer",
         job="Create the load balancer that takes traffic from the internet and passes it to "
             "whichever servers are healthy.",
         settings=[("Type", "Application Load Balancer"), ("Name", "ledgerline-alb"),
                   ("Scheme", "Internet-facing"), ("VPC", "ledgerline-vpc"),
                   ("Subnets", "both public subnets"),
                   ("Security group", "ledgerline-alb-sg"),
                   ("Listener", "HTTP 80 → ledgerline-tg")],
         clicks=["EC2 console, Load balancers, Create load balancer.",
                 "Choose Application Load Balancer.",
                 "Name it and leave the scheme as Internet-facing.",
                 "Choose ledgerline-vpc, then tick BOTH availability zones and choose the matching "
                 "public subnet under each. It will not let you continue with only one.",
                 "Under Security groups, remove the default group and add ledgerline-alb-sg.",
                 "Under Listeners and routing, leave HTTP:80 and choose ledgerline-tg as the "
                 "default action.",
                 "Create load balancer, then wait for it to leave Provisioning."],
         capture="the load balancer summary showing its scheme, DNS name and security group."),

    dict(n=13, title="Create the Auto Scaling group",
         job="Create the group that launches and removes servers on its own.",
         settings=[("Launch template", "ledgerline-lt"), ("VPC", "ledgerline-vpc"),
                   ("Subnet", "ledgerline-app-a only"),
                   ("Load balancing", "attach to ledgerline-tg"),
                   ("Health checks", "turn on Elastic Load Balancing health checks"),
                   ("Group size", "desired 1, minimum 1, maximum 2"),
                   ("Scaling policy", "target tracking, Average CPU utilization, 70")],
         clicks=["EC2 console, Auto Scaling groups, Create Auto Scaling group.",
                 "Name it, choose ledgerline-lt as the launch template, Next.",
                 "Choose ledgerline-vpc and tick ledgerline-app-a only. Next.",
                 "This page defaults to No load balancer and is the easiest step to skip. Choose "
                 "Attach to an existing load balancer, then Choose from your load balancer target "
                 "groups, and pick ledgerline-tg.",
                 "Tick Turn on Elastic Load Balancing health checks. Next.",
                 "Set desired 1, minimum 1, maximum 2.",
                 "Choose Target tracking scaling policy, metric Average CPU utilization, target "
                 "70. Next through the remaining pages and Create.",
                 "Watch the Activity tab. A server should launch within a minute or two."],
         capture="the Auto Scaling group showing its size, target group and scaling policy."),

    dict(n=14, title="Create the database subnet group",
         job="Create the group that tells the database service which subnets it may use.",
         settings=[("Name", "ledgerline-db-subnet-group"), ("VPC", "ledgerline-vpc"),
                   ("Zones", "us-east-1a and us-east-1b"),
                   ("Subnets", "ledgerline-data-a and ledgerline-data-b")],
         clicks=["Search RDS and open it. Choose Subnet groups in the left menu — not the VPC "
                 "console, which is where most people go looking.",
                 "Create DB subnet group. Name it, choose ledgerline-vpc.",
                 "Tick both availability zones, then choose the matching data subnet under each.",
                 "Create."],
         evidence_note="No screenshot needed. Creating the subnet group is a prerequisite step — "
                       "the database cannot be created without one."),

    dict(n=15, title="Create the database",
         job="Create the database, empty. Loading data is somebody else's job.",
         settings=[("Creation method", "Standard create"), ("Engine", "PostgreSQL"),
                   ("Template", "Free tier"),
                   ("Instance class", "your choice — see the decision below"),
                   ("Storage", "gp3, 20 GB"), ("VPC", "ledgerline-vpc"),
                   ("Subnet group", "ledgerline-db-subnet-group"),
                   ("Public access", "No"), ("Security group", "ledgerline-db-sg"),
                   ("Encryption", "enabled")],
         clicks=["RDS console, Databases, Create database.",
                 "Choose Standard create. Easy create picks the network and security settings for "
                 "you and will not let you change them.",
                 "Choose PostgreSQL, then the Free tier template.",
                 "Give it a name and set a master username and password. Write the password down.",
                 "Instance class: whichever of the two you chose below. Storage 20 GB gp3.",
                 "Under Connectivity choose ledgerline-vpc and your subnet group, set Public "
                 "access to No, remove the default security group and add ledgerline-db-sg.",
                 "Under Additional configuration confirm encryption is enabled.",
                 "Create database, then wait. It takes several minutes to reach Available."],
         capture="the database summary showing Available, Public access No, and encryption on.",
         decision=("Choose the database instance class: db.t3.micro or db.t3.small. Name the one "
                   "you did not choose, say which you chose, and explain why against the "
                   "workload.",
                   "db.t3.micro has 1 GiB of memory and db.t3.small has 2 GiB. Ledgerline's "
                   "working set is small — a single finance team's ledgers, not a college's worth "
                   "of student records — so db.t3.micro holds what is frequently read in memory "
                   "without difficulty. I chose db.t3.micro. The reasoning would change if month-"
                   "end reporting turned out to read far more than day-to-day use does.")),

    dict(n=16, title="Create the two monitoring alarms",
         job="Create two alarms — one that tells you when the application tier stops serving, one "
             "that tells you when the database is running out of room.",
         settings=[("Notification topic", "create an SNS topic named ledgerline-alerts with your "
                                          "own email address and use it for both alarms. You do "
                                          "not need to confirm the subscription email"),
                   ("─ Alarm 1 ─", "the application tier is not serving"),
                   ("Metric", "Application ELB → Per AppELB, per TG Metrics → UnHealthyHostCount"),
                   ("Statistic", "Maximum"), ("Period", "1 minute"),
                   ("Condition", "Greater/Equal than 1"),
                   ("Datapoints to alarm", "1 out of 1"),
                   ("Name", "ledgerline-unhealthy-hosts"),
                   ("─ Alarm 2 ─", "the database is running out of room"),
                   ("Metric", "RDS → DBInstanceIdentifier, then filter for FreeStorageSpace "
                              "and tick the row for your database"),
                   ("Statistic", "Minimum"), ("Period", "5 minutes"),
                   ("Condition", "Lower than 20% of the 20 GiB you allocated"),
                   ("Working that out", "the field takes bytes, not gigabytes. 20 GiB is "
                                        "21474836480 bytes, so 20% of it is 4294967296. Type the "
                                        "raw digits — no commas, no units. The graph above the "
                                        "field is drawn in GB, which makes it easy to type a "
                                        "number a thousand times too small"),
                   ("Datapoints to alarm", "2 out of 2"),
                   ("Name", "ledgerline-db-storage-low")],
         clicks=["Search CloudWatch and open it. Choose Alarms, then Create alarm.",
                 "Select metric. Choose Application ELB, then Per AppELB, per TG Metrics.",
                 "Filter the list for UnHealthyHostCount and tick the row for your load balancer "
                 "and target group. Select metric.",
                 "Set Statistic to Maximum and Period to 1 minute.",
                 "Under Conditions choose Greater/equal and enter 1. Next.",
                 "Create an SNS topic named ledgerline-alerts with your email. Next, name the "
                 "alarm, and finish.",
                 "Create alarm again for the second one. Select metric, choose RDS, then "
                 "DBInstanceIdentifier.",
                 "Filter for FreeStorageSpace, tick the row for your database, Select metric.",
                 "Set Statistic to Minimum and Period to 5 minutes.",
                 "Under Conditions choose Lower and type the byte figure you worked out above.",
                 "Under Additional configuration set Datapoints to alarm to 2 out of 2.",
                 "Choose the ledgerline-alerts topic you already made, name the alarm, finish."],
         capture="the alarm list showing both alarms with their metrics, thresholds and current "
                 "state."),
]

TESTS = [
    dict(n="T1", title="Connect to a server",
         job="Connect to one of your application servers and confirm you are on it.",
         steps=["EC2, Instances, select the running instance.",
                "Choose Connect, then the Session Manager tab, then Connect.",
                "Run the command below."],
         code=("Run this", ["hostname"]),
         note="Session Manager needs no key pair and no open port, which is why your servers can "
              "sit in a private subnet with nothing exposed.",
         capture="the session showing the hostname."),

    dict(n="T2", title="Reach the internet from the server",
         job="Confirm the server can reach out through the NAT gateway.",
         steps=["In the same session, run the command below.",
                "You should get a page of HTML back."],
         code=("Run this", ["curl -I https://aws.amazon.com"]),
         capture="the command and the response headers."),

    dict(n="T3", title="Reach the database from the server",
         job="Confirm the application tier can reach the database privately.",
         steps=["RDS, your database, Connectivity & security. Copy the endpoint.",
                "In the session, run the command below with your endpoint in place of the "
                "placeholder.",
                "A blank response with no error means the port is open. Connection refused or a "
                "timeout means the security groups are wrong."],
         code=("Run this", ["nc -zv <YOUR-DB-ENDPOINT> 5432"]),
         capture="the command and its result."),

    dict(n="T4", title="Reach the application from a browser",
         job="Open your load balancer in a browser and see the page your servers are serving.",
         steps=["EC2, Load balancers, select ledgerline-alb and copy its DNS name.",
                "Paste it into a browser tab with http:// in front.",
                "You should see the Ledgerline placeholder page.",
                "If you get a 503, the target group has no healthy server yet — check the Targets "
                "tab and give it a minute."],
         note="your servers have no public address. What the browser is reaching is the load "
              "balancer, which is the only thing allowed to talk to them.",
         capture="the browser showing the page with the load balancer address in the bar."),

    dict(n="T5", title="Watch it scale",
         job="Make the Auto Scaling group add a server on its own, then take it away again.",
         steps=["EC2, Instances, select your instance, Monitoring tab. Read the CPU figure — it "
                "will be low.",
                "Open your Auto Scaling group, Automatic scaling tab, edit the policy.",
                "Set the target value BELOW the CPU figure you just read. If it is very low, use "
                "1. Save.",
                "Watch the Activity tab until a second server launches.",
                "Edit the policy again, set the target to 90, and save.",
                "Watch until the group drops back to one server, then set the target back to 70."],
         note="scaling in is much slower than scaling out. Give it several minutes.",
         capture="the Activity tab showing both the scale-out and the scale-in."),
]
