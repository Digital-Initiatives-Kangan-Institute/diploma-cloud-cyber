# YAT College — LMS Migration Role Brief

**Relevant to:** S1-CL1 AT1, AT2, AT3

**UoC references this document satisfies:**
- [ICTICT517 AC 4] Individual superior in the organisation
- [ICTICT517 PC 1.4] Report on proposed changes, gaps and improvement opportunities to superior

**Source status:** ✅ Verbatim from YAT case study (originally in 517 AT2 source)

---

## Your role

You work in the ICT department at MP Tech Solutions (MTS). Your role is to assess current systems against the strategic plan, propose changes (if appropriate) and evaluate the effect of these changes. You will then put together an action plan to implement these changes.

## LMS server — senior team recommendations

Senior members of the ICT team have made the following recommendations for the LMS server:

- On a new server the CPU, memory and storage resources need to increase by at least 100%.
- The availability of the system needs to increase from 99.2% to 99.9%.
- There is no intention to change the OS and/or application software versions as part of the transition.

---

## Scope of the MTS consulting engagement

> *This section extends the verbatim role description above. It defines the boundary between work performed by MTS (the consulting firm) and work performed by YAT's in-house IT department. Both AT1 (Business Case), AT2 (Foundation Build), and AT3 (HA Hardening) operate within this scope.*

### In scope for MTS

The MTS consulting engagement covers **the cloud infrastructure** for the YAT LMS migration. Specifically:

- **Strategic recommendation and business case** — analysis of YAT's strategic plan against the industry environment, evaluation of options (in-house renewal vs cloud migration), 5-year cost-benefit analysis, risk and impact assessment, recommendation, and action plan. *Delivered by MTS in AT1.*
- **Foundation cloud infrastructure design and build** — design and deployment of the AWS-based foundation environment for the LMS (AWS account access, IAM, network, compute, managed database, autoscaling, storage, monitoring baseline). *Delivered by MTS in AT2 against a baseline design produced by MTS Senior Architecture in consultation with YAT IT.*
- **High-availability hardening, simulation testing, and final handover** — review of the AT2 foundation for HA gaps, design of HA improvements (Multi-AZ, fault tolerance, recovery objectives), implementation of HA hardening, failure-simulation testing, and final handover to YAT IT. *Delivered by MTS in AT3.*
- **All consulting documentation produced by MTS** — business case, deployment reports, HA design document, simulation outcomes, handover documentation, knowledge-evidence responses.

### Out of scope for MTS (handled by YAT in-house IT)

The following activities are required to complete the LMS migration as a whole project, but are **YAT IT's responsibility**, not MTS's. They are explicitly excluded from the MTS deliverables across AT1, AT2, and AT3:

- **LMS application installation** — installation of the DOODLE LMS application binaries onto the cloud infrastructure provided by MTS
- **Application configuration** — configuration of the LMS application (course shells, user groups, accessibility settings, integrations to Office 365 SMTP, ASQA reporting exports, etc.)
- **Database migration** — extraction of the MySQL database from the on-premises LMS server and load into the AWS RDS instance, including any data transformation, schema validation, and post-migration verification
- **Cutover** — the switch from the legacy on-premises LMS to the new AWS-hosted LMS, including DNS changes, parallel running of old and new during the transition window, user redirection, and decommissioning of the on-premises infrastructure
- **Organisational change management** — change advisory board (CAB) process for the cutover, end-user communications, staff and student training, post-cutover support ramp-up, and management of the change through YAT's documented Change Management Procedure
- **Post-handover application support** — ongoing application-level support, patching, and incident response for the LMS application after MTS handover (ongoing AWS infrastructure support remains contracted to MTS separately, on terms outside this engagement)

### What this means for the Business Case (AT1)

The Business Case must reflect the **total cost of the recommended option** — including both MTS-priced work *and* the YAT-internal cost of the out-of-scope activities listed above. Reason: the YAT board is approving the whole project, not just the MTS share. A CBA that omits YAT-internal cost categories gives the board an unrealistic basis for decision-making.

The **Action Plan (§10 of the Business Case)** makes the responsibility split explicit by assigning ownership to MTS or YAT IT for each phase of work.

See `internal-cba-cost-inputs-S1-CL1-AT1.md` for the cost categories and indicative inputs the Business Case needs to include from both sides.
