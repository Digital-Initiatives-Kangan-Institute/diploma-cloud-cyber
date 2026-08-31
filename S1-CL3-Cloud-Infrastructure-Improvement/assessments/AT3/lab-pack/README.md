# AT3 — Deploy the Ledgerline environment and apply the improvement

This guide walks you, step by step, through building the **starting environment** for AT3 and then
**applying the approved improvement** to it. You do this in your own AWS Academy lab.

**What you are doing:**
1. Deploy the **existing-state** Ledgerline infrastructure (`baseline.yaml`) — a single-AZ environment.
2. Apply the **approved improvement** (`improved.yaml`) to that same environment as a change-set.

**You will need:**
- Your AWS Academy login.
- The files **`baseline.yaml`** and **`improved.yaml`** (download them from your AT3 assessment page).
- A database password you choose (at least 8 characters) — **write it down**.
- About **20 minutes** (the database is the slow part to build).

> **Note about reaching the system.** Ledgerline is an **internal** system — in real life staff reach
> it over a private VPN, not the public internet. In the lab there is no VPN, so you will **not** open
> the application in a browser. Instead you confirm everything is working from the **AWS console**
> (stack status, healthy targets, database status). That is normal and expected for this system.

---

## Part 1 — Open the AWS Academy Learner Lab

1. Log in to **AWS Academy** (the Canvas site your teacher gave you).
2. On your **Dashboard**, open the **AWS Academy Learner Lab** course.
3. On the left menu click **Modules**, then open the **Learner Lab**.
4. On the lab page, click **Start Lab**. Wait for the dot next to **AWS** to turn **green**.
5. Click the green **AWS** dot — the AWS Management Console opens in a new tab.

## Part 2 — Check the region

6. At the **top-right** of the console, confirm the region is **US East (N. Virginia)** — `us-east-1`.
   The Learner Lab runs only in this region, so it should already be selected; if not, choose it.

> **Region substitution.** Ledgerline is designed to run in Sydney, but the Learner Lab only offers
> `us-east-1`, so that is where you deploy. Wherever you see this notation, the left side is the real
> design region and the right side is where you actually deploy:
>
> `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`
>
> Deploying to `us-east-1` is identical to deploying anywhere else — only the location label changes.

## Part 3 — Build the baseline (existing state)

7. In the search bar type **CloudFormation** and open it.
8. Click **Create stack** → **With new resources**.
9. **Template source** → **Upload a template file** → **Choose file** → select **`baseline.yaml`** → **Next**.
10. On the next page:
    - **Stack name:** `ledgerline-baseline`
    - **DBMasterPassword:** type a password (8+ characters) and **write it down**.
    - Leave everything else as it is → **Next**.
11. **Configure stack options** → leave as is → **Next**.
12. **Review** → scroll down → **Submit**.
13. **Wait about 15 minutes.** When the stack shows **CREATE_COMPLETE** (green), it is ready.

## Part 4 — Check the baseline worked (from the console)

14. **Stack built?** The `ledgerline-baseline` stack shows **CREATE_COMPLETE**.
15. **App tier healthy?** Search **EC2** → **Target Groups** → click `ledgerline-...` → **Targets** tab.
    You should see the instance with status **healthy** (give it a few minutes after the stack finishes).
16. **Database up?** Search **RDS** → **Databases** → `ledgerline-prod` shows status **Available**, and
    (importantly) **Multi-AZ = No** — the baseline runs a single instance with no standby. That is the
    starting state you are about to improve.

If those three are good, your baseline is up.

## Part 5 — Apply the approved improvement (change-set)

You now apply the approved improvement **to the same stack**, so nothing is rebuilt from scratch.

17. Go back to **CloudFormation** → click the **`ledgerline-baseline`** stack → **Update** (top right).
18. Choose **Replace existing template** → **Upload a template file** → select **`improved.yaml`** → **Next**.
19. Keep the **same parameter values** as before (including the **same DBMasterPassword**) → **Next** → **Next**.
20. On the **Review** page, scroll to the bottom and look at the **Change set preview**. You should see
    **Modify** actions (no **Replace**) — the improvement is applied in place. Click **Submit**.
21. **Wait** for **UPDATE_COMPLETE** (green). This is quicker than the first build.

## Part 6 — Check the improvement applied

22. **App tier now Multi-AZ?** EC2 → **Auto Scaling groups** → `ledgerline-app-prod` → **Instance management**.
    You should now see **two** instances, in **two different Availability Zones** (e.g. `us-east-1a`
    and `us-east-1b`). The application tier can now survive an AZ failure.
23. **Database now Multi-AZ?** RDS → `ledgerline-prod` → **Configuration** tab. **Multi-AZ** now reads
    **Yes**, with a standby in a second Availability Zone. AWS builds and syncs the standby in the
    background, so the database may sit in **Modifying** for a while before it settles on **Available** —
    that is normal, and the database stays reachable throughout. The database can now fail over
    automatically instead of being restored from a backup.

    The instance is **modified in place**, not rebuilt — same endpoint name, same data.

## Part 7 — Clean up (always do this at the end)

24. **CloudFormation** (`us-east-1`) → select **`ledgerline-baseline`** → **Delete** → confirm. Wait for it to disappear.
25. Back on the lab tab, click **End Lab**.

---

## If something goes wrong

- **Stack says ROLLBACK or FAILED:** open the **Events** tab, find the first red **CREATE_FAILED** /
  **UPDATE_FAILED** row — its **Status reason** says what happened. Tell your teacher what it says.
- **The change-set preview shows "Replace" instead of "Modify":** stop and check you used the **same**
  parameter values (especially the password and the database settings) as the baseline. A changed
  database setting can force a replacement.
- **Target shows unhealthy:** wait a few minutes after the stack finishes — the web server takes a
  moment to start. If it stays unhealthy, delete the stack (Part 8) and redeploy.
