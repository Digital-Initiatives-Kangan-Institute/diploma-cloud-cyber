# Claude notes — CL3 AT3 lab pack (Ledgerline)

Pack-specific notes only. The generic pattern, AWS Academy constraints, validation harness and
hard-won lessons live in the canonical standard — `docs/lab-pack-standard.md` (umbrella). Below is
only what is specific to THIS pack. See also `assessments/assessment_plan.md` §6.8.

> **Lab = AWS Academy Learner Lab, `us-east-1`** (course-wide single product; see the region-substitution
> standard). Design regions stay real — Sydney `ap-southeast-2`, India `ap-south-1`, Melbourne DR
> `ap-southeast-4` — but everything **deploys to `us-east-1`**, and **residency/DR are design-only** (not
> deployed).
>
> ⚠️ **NOT currently proven live — the templates were materially rebuilt and need a fresh proving run.**
> The pack now deploys **Amazon Linux 2023 + RDS for PostgreSQL** (was Windows Server 2016 + SQL Server
> Express) and the improvement **converts the database to Multi-AZ**. Earlier runs (Sandbox 2026-06-21,
> Learner Lab 2026-07-01) proved the *previous* templates and no longer certify these. Local validation is
> green (cfn-lint clean, 14/14 pytest). See "Proving run" below for the one thing to watch.

## What this pack is

The AT3 environment for **Ledgerline** (the YAT Accounting System). AT3 follows an **apply-as-update**
model:

- **`baseline.yaml`** — the existing single-AZ state the student deploys first.
- **`improved.yaml`** — the **approved improvement** applied as a CloudFormation **change-set / stack
  update** to the *same* stack (same logical IDs, so every change is in-place/additive — no replacement).
  The database is **modified**, not rebuilt: `MultiAZ` is an in-place update property, so the instance and
  its data survive the change-set.
  Doubles as the AT2 model answer and the AT3 assessor reference/fallback if a team's AT2 write is unusable.

## Design decisions specific to this pack

1. **The improvement takes BOTH tiers to Multi-AZ.** The baseline is single-AZ at compute and database;
   `improved.yaml` spreads the ASG across two AZs and converts the RDS instance to a Multi-AZ deployment
   with a synchronous standby and automatic failover. Backup, point-in-time restore and the cross-Region
   DR copy stay behind it — failover covers AZ and instance failure, not data loss, corruption or a
   Region-level event. The pytest enforces baseline `MultiAZ: false` / improved `MultiAZ: true`, and that
   **MultiAZ is the only DB property that differs** — anything else would trigger a replacement and
   destroy the data.

   *History: this pack previously asserted the opposite, on the basis that Ledgerline could not run on a
   Multi-AZ database. That restriction was lifted across the scenario (Ledgerline is the practice vehicle
   for HA database work, and the restriction was giving students grounds to decline the practice).*

2. **Internal ALB (faithful) → console-based verification.** Unlike CL1 AT3 (internet-facing ALB you could
   curl), Ledgerline is internal-only (VPN), so the ALB is `Scheme: internal` and is **not browser-reachable
   in the lab** (no VPN). Verification is via the console: stack status, Target Group health, RDS status,
   ASG instance AZs. The README says so explicitly. This is a deliberate divergence from the CL1 pattern,
   driven by the scenario.

3. **Engine is PostgreSQL, and both templates must agree.** The scenario's cloud Ledgerline runs on
   **Amazon RDS for PostgreSQL** (Accounting System Infrastructure Specifications); the templates now match
   it, on `db.t3.micro`. `Engine` is a **replacement** property — if the two templates ever disagree, the
   change-set destroys and rebuilds the database instead of updating it. The pytest asserts both default to
   `postgres`. No `LicenseModel` (that is a SQL Server property; setting it fails the create).

   This also removes the old edition problem outright: SQL Server Standard would not deploy on the lab's
   permitted instance classes, and Express does not support Multi-AZ at all. PostgreSQL does Multi-AZ on
   `db.t3.micro`, so there is no substitution left to disclose to students.

4. **Cross-Region DR backup copy is a documented CLI step, not in the template.** RDS automated-backup
   replication to a second Region (Melbourne, `ap-southeast-4`, to keep financial data in Australia) is set
   via `aws rds start-db-instance-automated-backups-replication`, not a CloudFormation property. The exemplar
   design names it; the lab treats it as an out-of-band step. Do not expect it in `improved.yaml`.

5. **2-AZ network, single-AZ compute baseline.** An internal ALB needs >= 2 subnets in 2 AZs and an RDS
   subnet group needs >= 2 AZs, so a 2nd app subnet and 2nd data subnet are present in the baseline; the
   ASG is kept single-AZ (one subnet) so the baseline is genuinely non-HA at the compute tier. `improved.yaml`
   adds the 2nd app-subnet route-table association and spreads the ASG across both app subnets.

## Proving run — REQUIRED, not yet done for these templates

The templates were rebuilt (Amazon Linux 2023 + PostgreSQL; database converted to Multi-AZ by the
change-set). Nothing below has been demonstrated on the current pack. **Do the run before treating this
pack as delivered** — the lab-pack standard makes one live run part of the definition of done.

**The one thing to watch: can CloudFormation modify the RDS instance in the Learner Lab?**

This is the only step that could fail on permissions rather than configuration, and the evidence is
genuinely mixed:

- *Against:* on 2026-06-21, in the **Cloud Architecting Sandbox**, a change-set raising
  `BackupRetentionPeriod` 7->14 hit `AccessDenied` on `rds:ModifyDBInstance`. That is where the old
  "the DB must stay untouched" rule came from. It was never retested in the Learner Lab, because the
  change-set was rewritten to avoid the DB entirely, which made the question moot rather than answered.
- *For:* the **CL1 AT3 pack** has students convert a running RDS instance to Multi-AZ **in the Learner
  Lab, via the console**, and its notes record it as proven live with an explicit instruction not to
  reinstate the claim that Multi-AZ is unsupported there.

So: create is certainly permitted; console modify is proven on CL1; **CFN modify in the Learner Lab is
unproven**. Deploy `baseline.yaml`, apply `improved.yaml` as a stack update, and watch the `Database`
resource in the change-set.

**If it is denied,** the fallback is a straight swap of model, not a redesign: make `improved.yaml` a
standalone stack that *creates* the improved state (Multi-AZ included) rather than updating the
baseline, and change the README to deploy it directly. `CreateDBInstance` is not in question.

Also still not demonstrated live on any version of this pack: the failure simulation
(terminate-an-instance), the scale-out demo, and a PITR restore. Restore permissions remain unverified.

## Local validation (done)

- **cfn-lint:** clean (exit 0) on both templates via the `.cfnlintrc.yaml` template list (W1011 suppressed
  and justified — NoEcho DB password supplied at deploy, not Secrets Manager, to avoid IAM in the lab).
- **pytest:** 14/14. Asserts baseline single-AZ -> improved Multi-AZ, that `MultiAZ` is the ONLY database
  property differing between the templates (anything else would force a replacement), `postgres` on both,
  single-AZ->2-AZ compute, internal ALB, encrypted+empty DB, no IAM created, the lab instance profile, SSM
  AMI, locked buckets, and **pure ASCII** (a non-ASCII char in an RDS description fails the live deploy and
  cfn-lint does not catch it).
- Run: `python -m venv .venv && .venv/bin/python -m pip install -r requirements.txt`, then
  `.venv/bin/cfn-lint` and `.venv/bin/python -m pytest -q`.
