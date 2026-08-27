# Practice — set up the finished Ledgerline environment

This builds the **finished** Ledgerline environment in one go — the same thing you would have at
the end of the practice build run sheet, if you had worked through all fifteen tasks by hand.

**Use it when** you want to practise the *next* stage of the work without spending an hour
rebuilding the stage before it. If you have not done the practice build run sheet yet, do that
first — building it by hand is the point of it.

**You will need:**
- Your AWS Academy login.
- The file **`baseline.yaml`** from this folder.
- About **15 minutes** (the database is the slow part).

---

## Part 1 — Open the AWS Academy Learner Lab

1. Log in to **AWS Academy** and open the **AWS Academy Learner Lab** tile.
2. Click **Modules**, then open the **Learner Lab**.
3. Click **Start Lab** and wait for the circle next to **AWS** to turn **green**.
4. Click the green circle. The **AWS Management Console** opens in a new tab.

## Part 2 — Check the region

5. Top-right of the console should read *United States (N. Virginia)* — `us-east-1`. If not,
   click it and choose that region.

## Part 3 — Build it

6. Search for **CloudFormation** in the top search bar and open it.
7. **Create stack** → **With new resources**.
8. **Template source** → **Upload a template file** → **Choose file** → pick `baseline.yaml`.
   **Next**.
9. **Stack name:** `ledgerline-practice`.
10. **DBMasterPassword:** type a password of at least 8 characters and write it down.
11. **AlertEmail:** leave blank, or put your own address in if you want the alarm to email you.
12. Leave everything else as it is. **Next**, **Next**, then **Submit**.
13. Wait about 15 minutes, until the stack reads **CREATE_COMPLETE**.

## Part 4 — Check it worked

14. Open the **Outputs** tab and copy the **AlbDnsName** value.
15. Paste it into a browser with `http://` in front.
16. You should see **Ledgerline — Infrastructure ready.**

If the page loads, the environment is up.

## Part 5 — When you finish

17. CloudFormation → your **`ledgerline-practice`** stack → **Delete**. Wait until it is gone.
18. Back in the lab tab, click **End Lab**.

The NAT gateway and the load balancer both cost money by the hour, so delete the stack at the
end of every session.

---

## What this is not

It is **not** the assessment environment. Ledgerline runs on a different address range
(`10.20.0.0/16`), a different operating system (Amazon Linux), and a different database engine
(PostgreSQL), and everything is named `ledgerline-`. The shape is the same on purpose so the
moves transfer; the values are different on purpose so they cannot be copied across.

One deliberate difference from Ledgerline's real design: the load balancer here is
**internet-facing**, so you can reach the page from your own browser and see the thing you built.
The real Ledgerline would sit behind the corporate network.

## If something goes wrong

- **ROLLBACK or FAILED:** open the **Events** tab and find the first red **CREATE_FAILED** row.
  Its **Status reason** says what happened.
- **The page won't load:** give it 2–3 more minutes. The server needs a moment after the stack
  finishes. If it still won't load after ~10 minutes, delete the stack and start again.
- **`LabInstanceProfile` does not exist:** clear the **InstanceProfileName** box to blank and
  deploy again. The site will still work; you just won't be able to open a shell on the server.
