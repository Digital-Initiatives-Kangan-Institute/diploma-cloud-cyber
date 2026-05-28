# YAT College — High-Availability Database Requirements

**Relevant to:** S1-CL1 AT3

**UoC references this document satisfies:**
- [ICTCLD502 PE 1] design and implement at least one fault tolerant cloud infrastructure on a cloud platform resilient to networking, compute, storage, database and data centre failures
- [ICTCLD502 AC 5] business and functionality requirements

**Source status:** ✅ Complete — rebranded from Llamazonia (502 AT2 Activity 5) to YAT LMS context on 2026-05-23.

---

## Context

As the LMS cloud migration enters its high-availability hardening phase (S1-CL1 AT3), YAT requires the LMS's MySQL database service to be re-deployed as a fault-tolerant, multi-AZ managed database. The single-instance MySQL deployed during AT2 (the cloud foundation build) must be replaced with — or upgraded to — a service that meets the high-availability requirements stated below.

## Requirements

The HA database service for the migrated YAT LMS must:

- **Be MySQL-compatible.** The LMS uses MySQL (per the YAT case study and the LMS application specification). The HA database service must run MySQL or a fully-compatible managed equivalent so that the DOODLE LMS application continues to operate without code or schema changes.
- **Replicate data across availability zones.** Data must be replicated to a standby instance in a different availability zone within the same AWS region.
- **Provide automatic failover under two minutes.** If the primary instance fails, the database must automatically switch to the standby instance and resume service in under 2 minutes.
- **Run on the same cloud vendor as the rest of the migrated environment.** The HA database service must use AWS (consistent with the cloud foundation built in S1-CL1 AT2) so that networking, IAM, and operational tooling remain coherent.
- **Be a managed service.** To minimise management and maintenance effort required by YAT's ICT staff — who have limited cloud expertise per the YAT case study — the LMS must use a managed database service offered by the cloud vendor (e.g. Amazon RDS Multi-AZ for MySQL) rather than self-hosted MySQL on an EC2 instance.
