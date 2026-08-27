# AT3 — Set up your baseline environment

Before you start the AT3 assessment you need to build the **starting environment** in AWS.
This guide walks you through it, step by step. You only do this once, at the start of AT3.

**What you are building:** the YAT LMS infrastructure exactly as it stands at the end of AT2 —
the same VPC, subnets, security groups, load balancer, Auto Scaling group and database, built to
the same settings, under the same names. It is a working system, but it is not yet highly
available. During AT3 you will improve it into a highly available design.

You get this whether or not your own AT2 build finished cleanly. Everyone starts AT3 from the
same known-good state.

**You will need:**
- Your AWS Academy login.
- The file **`baseline.yaml`** (download it from your AT3 assessment page and save it somewhere
  easy to find, like your Downloads folder).
- About **20 minutes** (the environment takes ~15 minutes to build itself once you start it).

---

## Part 1 — Open the AWS Academy Learner Lab

1. Log in to **AWS Academy** (the Canvas site your teacher gave you the link to).
2. On your **Dashboard**, click the tile named **AWS Academy Learner Lab**.
3. On the left-hand menu, click **Modules**.
4. Open the **Learner Lab**.
5. A lab page opens. Near the top you will see a row with **Start Lab**, **End Lab**, and a
   small circle next to the word **AWS**. Click **Start Lab**.
6. Wait. The circle next to **AWS** turns **yellow** (starting), then **green** (ready). This
   takes a minute or two. **Wait for green.**
7. Click the green circle next to **AWS**. The **AWS Management Console** opens in a new browser
   tab. (If nothing opens, your browser may have blocked the pop-up — allow pop-ups for this
   site and click it again.)

You are now in the AWS console.

---

## Part 2 — Choose your region

8. Look at the **top-right** of the console and click the region selector to see what is offered.
9. If **Asia Pacific (Sydney)** — `ap-southeast-2` — is in the list, choose it. If it is not, use
   whichever region you do have; in the Learner Lab that is **US East (N. Virginia)**, `us-east-1`.
   Whatever you choose, stay in it for the whole of AT3.

> **Which region?** The scenario runs this in Sydney, `ap-southeast-2` — use that region if it is
> available to you. If you are working in the AWS Academy Learner Lab or a similar restricted
> environment, Sydney will not be offered: build in `us-east-1`, or whichever region you do have.
> The template builds the same thing in any region — it asks AWS which availability zones exist
> wherever it is running, so no part of it is tied to a location.
>
> Where the course materials use this notation, the left side is the design region and the right
> side is where you actually build:
>
> `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`

---

## Part 3 — Build the environment

10. In the **search bar** at the top, type **CloudFormation** and click it in the results.
11. Click the orange **Create stack** button (choose **With new resources** if it asks).
12. Under **Prepare template**, leave **Choose an existing template** selected.
13. Under **Template source**, choose **Upload a template file**.
14. Click **Choose file** and select the **`baseline.yaml`** file you saved earlier. Click **Next**.
15. On the next page:
    - **Stack name:** type `yat-lms-baseline`
    - Find the box labelled **DBMasterPassword** and type a password (at least 8 characters).
      **Write this password down** — it's the database admin password.
    - Leave every other box as it is.
    - Click **Next**.
16. On the **Configure stack options** page, don't change anything. Scroll to the bottom and
    click **Next**.
17. On the **Review** page, scroll to the bottom and click **Submit**.

The environment now starts building. You'll see a list of items turning from
**CREATE_IN_PROGRESS** (blue) to **CREATE_COMPLETE** (green).

18. **Wait about 15 minutes.** The database is the slowest part. When the stack name shows
    **CREATE_COMPLETE** (green) at the top, it's ready.

---

## Part 4 — Check it worked

19. Click the **Outputs** tab (near the top, next to Events/Resources).
20. Find the row **AlbDnsName** and copy its value (it looks like
    `yat-lms-alb-1234567890.us-east-1.elb.amazonaws.com`).
21. Open a new browser tab, type `http://` then paste that value, and press Enter.
22. You should see the heading **YAT LMS** and the text **"Infrastructure ready - awaiting
    application deployment."** — the same page your AT2 build served.
    (If it doesn't load straight away, wait 2–3 minutes and try again — the server takes a
    moment after building.)

If you see that page, your baseline environment is up and you're ready to begin AT3.

---

## Part 5 — When you finish (clean up)

Always do this at the end of your session so you don't waste your lab budget.

23. Go back to **CloudFormation**, click your **`yat-lms-baseline`** stack, and click **Delete**
    (confirm **Delete** when asked). Wait until it disappears from the list.
24. Go back to the lab tab and click **End Lab** at the top, then **Yes**.

---

## If something goes wrong

- **The stack says ROLLBACK or FAILED:** click the **Events** tab and look for the first red
  **CREATE_FAILED** row — its **Status reason** says what happened. Tell your teacher what it says.
- **The web page (Part 4) won't load:** give it a few more minutes; if it still won't load after
  ~10 minutes, delete the stack (Part 5) and start again from Part 3.
- **You ran out of time / the lab stopped:** you can click **Start Lab** again to get more time.
