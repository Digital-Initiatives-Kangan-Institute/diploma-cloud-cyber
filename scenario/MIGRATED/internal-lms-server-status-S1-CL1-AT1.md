# YAT College — LMS Server Specifications and Current Status

**Relevant to:** S1-CL1 AT1, AT2, AT3

**UoC references this document satisfies:**
- [ICTICT517 AC 5] Information on current ICT systems and practices in the organisation including operating systems, hardware, and security
- [ICTCLD502 PC 2.3] Estimate recovery objectives for multi-tier web components and for overall architecture

**Source status:** ✅ Complete — narrative description from YAT case study preserved verbatim; specific resource specs, utilisation figures, and growth rates below are Claude-proposed (plausible for an RTO LMS of YAT's stated scale and consistent with the "increase resources by at least 100%" target in the role brief) and marked **TBD** for Tim's confirmation.

---

## LMS Description (from YAT case study)

YAT is using 'Diverse Object-Orientated Dynamic Learning Environment' (DOODLE) as their custom learning and student management system (LMS). Students use the LMS to access course related resources and for assessment submission. Teachers use the LMS to record student attendance, assessment submission, unit completion, student's notes, as well as any other applicable student management tasks including support and notifications for classes. The LMS is distributed under the GNU General Public License Support.

YAT has engaged MP Tech Solutions (MTS) to provide application support and system customisation for the LMS. The college has also hired a consultant responsible for end to end delivery of the solution. You will be reporting to this consultant as your superior (supervisor).

Performance of the current system is acceptable; however, it is expected to degrade noticeably should the load increase.

## Current LMS Server — Infrastructure Summary

| Attribute | Value |
|---|---|
| Server role | LMS (DOODLE) + MySQL database (same host) |
| Operating system | Windows Server 2016 |
| Database | MySQL **TBD** version |
| Hosting | Single local on-prem server, staff network zone |
| Server age | ~5+ years — at end of life |
| Criticality | Mission critical |
| Current availability (measured, rolling 12 months) | 99.2% |
| Required new availability (per ICT Strategic Plan) | 99.9% |

## Current Hardware Specifications **TBD**

Claude-proposed plausible specs for a mid-sized RTO LMS at end of life. **TBD** confirm:

| Resource | Current | Comments |
|---|---|---|
| CPU | 4 vCPU @ 2.4 GHz | Peak utilisation ~75% during assessment-period spikes |
| Memory (RAM) | 8 GB | Peak utilisation ~85% during assessment-period spikes |
| Storage — system | 100 GB SSD | ~30% used |
| Storage — application + database | 250 GB SSD | ~70% used |
| Database storage (MySQL data files) | ~120 GB of the 250 GB above | Growing ~20 GB/year |
| Network | 1 Gbps NIC | Adequate for current load |
| IOPS (storage) | ~3,000 baseline, ~5,000 peak | |

## Migration Targets

Per the role brief (`internal-lms-migration-role-brief-S1-CL1-AT1.md`), the migrated LMS must:

- Increase CPU, memory, and storage resources by **at least 100%** over current
- Achieve **99.9%** availability (up from 99.2%)
- Retain the existing OS and application software versions (no in-flight upgrade)

Implied minimum target sizing **TBD**:

| Resource | Minimum target |
|---|---|
| CPU | 8 vCPU |
| Memory (RAM) | 16 GB |
| Storage — application + database | 500 GB |
| Network | 1 Gbps (no change required) |

These minimums leave headroom for the ~20 GB/year DB growth and the ~15% annual student-numbers growth stated in the Strategic Plan.

## Usage Patterns **TBD**

Claude-proposed plausible patterns:

- **Daily login peak:** weekday mornings (~08:00–10:00) and afternoons (~13:00–15:00) during teaching periods.
- **Assessment-period spike:** ~3x typical concurrent users during assessment submission windows (typically last 2 weeks of each term).
- **Off-hours load:** minimal — backup window 22:00–04:00 local time.
- **Annual data growth:** ~20 GB/year on the MySQL data files, driven by course materials, student submissions, and gradebook records.

---

**Still needed:**
- Replace Claude-proposed specs with real planning figures from the YAT ICT Manager (if/when sourced).
- An "LMS SERVER CURRENT STATUS" screenshot or table rendered as an image for the intranet UI.
