# YAT College — Current Backup and Recovery Process

**Relevant to:** S1-CL1 AT1, AT3

**UoC references this document satisfies:**
- [ICTCLD502 PC 2.3] Estimate recovery objectives for multi-tier web components and for overall architecture
- [ICTCLD502 KE 4] recoverability as measured by recovery time (RTO) and recovery point (RPO) objectives

**Source status:** ✅ Complete — adapted from Llamazonia (502 AT2 Activity 2.3) to the YAT on-prem LMS context on 2026-05-23. Steps adjusted to match YAT's single-server on-prem topology (no load balancer); RTO/RPO numbers retained because they yield the recovery-objective figures the AT1 gap analysis and AT3 HA design work against.

---

## Backup process

A complete, full backup of the YAT LMS environment runs every night, captured to tape by the System Management server. The backup covers:

- Windows Server 2016 system state (LMS server)
- The MySQL database data files (DOODLE schema and content)
- LMS application binaries and configuration
- LMS attachments and uploaded content (course materials, student submissions)

Tape backups are rotated offsite each business day per the Backup and Retention Policy.

**Backup window:** nightly, 22:00 – 04:00 local time. The LMS is fully available during this window; backups run online against the MySQL database with a brief consistency snapshot.

## Recovery process

To completely recover the YAT LMS from backups in the event of a major incident (e.g. server hardware failure, ransomware, irrecoverable database corruption), the following process is followed:

| Duration | Recovery step |
|---|---|
| 4–8 hours | Request tape from offsite location and have it delivered to the Cremorne campus |
| 1 hour | Restore Windows Server 2016 system state and LMS application binaries from tape onto replacement hardware |
| 1 hour | Restore MySQL database from the latest nightly backup and verify schema integrity |
| 1 hour | Verify LMS application connectivity to MySQL, re-authenticate against Active Directory, and confirm end-user sign-in works |

**Total RTO (worst case):** approximately 7–11 hours from incident declaration to LMS operational.

**RPO:** up to 24 hours of data loss is possible — anything written to the LMS between the last successful nightly backup and the incident is lost.

## Why this is a problem (context for the migration)

The current recovery objectives are significantly worse than the targets stated in `internal-lms-cloud-migration-requirements-S1-CL1-AT1.md` (RTO ≤ 4 hours, RPO ≤ 1 hour). Improving these is one of the explicit drivers for the LMS cloud migration, and the AT1 gap analysis should call out the gap between the current state recorded here and the target state required by the YAT ICT Strategic Plan.
