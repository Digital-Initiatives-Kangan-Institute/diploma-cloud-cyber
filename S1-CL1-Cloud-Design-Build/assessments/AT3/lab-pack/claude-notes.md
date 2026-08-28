# Claude notes — AT3 baseline lab pack

Pack-specific notes only. The generic pattern, AWS Academy constraints, validation harness and
hard-won lessons live in the umbrella's `docs/lab-pack-standard.md` — this pack was its reference
implementation, so those findings are recorded there, not here.

`baseline.yaml` is the source of truth for what this pack builds. Where this file and the template
disagree, the template is right and this file is stale — fix it.

## What this baseline is

The post-AT2 **single-AZ, non-HA** YAT LMS environment. A student deploys it at the start of AT3 and
hardens it to multi-AZ. It reproduces the end state of the AT2 run sheet (`at2_run_sheet.py`), which
is the definition it has to track.

What that means concretely:

| | |
|---|---|
| Subnets | 5 — `public-web-a/b`, `private-app-a`, `private-data-a/b`. **No app subnet in the second zone** — creating it is AT3 task 7 |
| Load balancer | Internet-facing, **HTTP:80**, spans both public subnets |
| Compute | ASG min 1 / desired 1 / max 2, **single-AZ**. Windows Server; root `/dev/sda1` + data volume `xvdb` (the volume AT2 task 10 adds) |
| Instance profile | `LabInstanceProfile` by default; blank is allowed and skips the association |
| Database | RDS MySQL, `MultiAZ: false`, `BackupRetentionPeriod: 7`. Subnet group spans both data subnets because RDS requires two AZs |
| Instance classes | `t3.micro` / `t3.small` and `db.t3.micro` / `db.t3.small` — the exact options AT2 decisions C1 and C2 offer |
| Alarms | Exactly two: `yat-lms-unhealthy-hosts`, `yat-lms-db-storage-low` |
| Not present | No S3, no bastion, no RDP ingress, no ACM certificate, no VPC flow logs |

The compute tier is what makes this genuinely non-HA. The ALB and the DB subnet group span two zones
only because AWS refuses to create them otherwise — that is a platform floor, not a design choice, and
it is why AT3 task 9's correct answer is "no change required" for the load balancer.

## Constraints that are walls, not preferences

- **The lab is AWS Academy Learner Lab, `us-east-1`.** Design region is Sydney (`ap-southeast-2`);
  deploy is `us-east-1`, written as `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`.
- **No IAM role creation.** This is why there are no VPC flow logs — CloudWatch flow logs need a role
  the lab will not let you create.
- **HTTP:80, not HTTPS.** ACM needs a domain. It is also deliberate: students must be able to see what
  they built actually working.

## Proven live — do not re-litigate

- **Baseline reaches CREATE_COMPLETE and serves its page** in the Learner Lab `us-east-1`
  (2026-07-01).
- **The Multi-AZ hardened end state deploys** — RDS `MultiAZ: true` with a standby in a second AZ, and
  a cross-AZ ASG, both reached CREATE_COMPLETE with no capacity refusal (2026-06-26 probe).
  An earlier note claimed Multi-AZ was unsupported in the lab. **That was wrong. Do not reinstate it.**
- **The ~6-minute ELB health-check replace loop does not reproduce.** Seen once on a throwaway probe,
  clean end-to-end since. Treat it as insufficient boot time, not a defect.
