# YAT College — Hardware / Software Inventory Summary

**Relevant to:** S1-CL1 AT1, AT2, AT3

**UoC references this document satisfies:**
- [ICTICT517 AC 5] Information on current ICT systems and practices in the organisation including operating systems, hardware, and security
- [ICTCLD502 AC 5] specific requirements and industry standards (the products align to)

**Source status:** ✅ Complete — products and platforms collated from YAT case study (verbatim where named in source); quantities, vendor placeholders, and licence-renewal placeholders below are Claude-proposed plausible values marked **TBD** for confirmation. Vendor/model placeholders left as **TBD** rather than invented to avoid implying a specific real-world supplier.

---

## Server inventory

| Server role | Quantity | OS | Vendor / Model | Notes |
|---|---:|---|---|---|
| Domain Controllers (AD / DHCP / DNS) | 2 | Windows Server 2016 | **TBD** | Load-shared across both zones; no single-system outage causes service outage |
| System Management & Backups | 1 | Windows Server 2016 | **TBD** | Single instance; explicitly not HA. Runs daily backups for both zones |
| Application Services (Accounting / Office Admin) | 1 | Windows Server 2016 | **TBD** | Single instance; critical functions (e.g. pay runs) outsourced |
| **LMS (DOODLE + MySQL)** | **1** | **Windows Server 2016** | **TBD** | **Single, end of life, mission critical — migration target** |
| VPN | 1 | **TBD** | **TBD** | Staff-only remote access; single instance — SPOF |

## Storage inventory

| Device | Quantity | Zone | Vendor / Model | Configuration |
|---|---:|---|---|---|
| NAS — staff zone | 1 | Staff | **TBD** | RAID-5, hot-swap disks |
| NAS — student zone | 1 | Student | **TBD** | RAID-5, hot-swap disks |

## Endpoint inventory **TBD quantities**

| Endpoint | Approx quantity | OS / Edition | Notes |
|---|---:|---|---|
| Staff desktops (offices) | ~25 | Windows 10 Enterprise | AD-joined |
| Student desktops (classrooms + labs) | ~80 | Windows 10 Enterprise + Office 365 Education | AD-joined; lab machines have additional memory/storage as required |
| Multifunction printers | ~5 | n/a | High-performance; staff-only locations |
| Classroom printers | ~15 | n/a | One per classroom |

## Network equipment **TBD**

| Item | Quantity | Vendor / Model | Notes |
|---|---:|---|---|
| Edge router/firewall | 2 (redundant) | **TBD** | No SPOF at network plumbing layer per source |
| LAN distribution switches (staff zone) | **TBD** | **TBD** | |
| LAN distribution switches (student zone) | **TBD** | **TBD** | |
| Wireless access points | **TBD** | **TBD** | Not explicitly mentioned in YAT source — confirm whether YAT has wifi |

## Software / licensing inventory

| Product | Vendor | Licence type | Quantity / coverage | Renewal **TBD** |
|---|---|---|---|---|
| Windows Server 2016 | Microsoft | Per-server licensing | 5 servers (DC x2, SysMgmt, AppSvc, LMS) | **TBD** |
| Windows 10 Enterprise | Microsoft | Per-device licensing | ~105 desktops | **TBD** |
| Active Directory 2016 | Microsoft | Included with Server 2016 | n/a | n/a |
| Office 365 Education edition | Microsoft | Per-student site licence | All students (~800) | **TBD** |
| Office 365 (Email, staff + students) | Microsoft | Mailbox-licensed SaaS (Azure-hosted) | ~860 mailboxes (staff + students) | **TBD** |
| DOODLE (Diverse Object-Orientated Dynamic Learning Environment) | Open source — GNU GPL | Free / no licence cost | 1 deployment | n/a — open source |
| MySQL | Oracle (Community Edition assumed) | **TBD** Community Edition / Standard / Enterprise | 1 deployment | **TBD** |

## Facilities

| Item | Notes |
|---|---|
| Server room | Physically secured, air-conditioned, UPS-protected against power loss and electrical surges |
| Network plumbing | Redundant (no SPOF) — see `internal-on-prem-network-diagram-S1-CL1-AT1.md` |

---

**Still needed:**
- Replace **TBD** vendor/model placeholders with real values if/when sourced (or with realistic-but-clearly-fictional vendor names to keep the simulation consistent).
- Confirm wifi presence/absence with Tim — not mentioned in YAT source.
- Confirm endpoint quantities scale with the headcount assumptions in `public-org-structure.md` (~60 staff + ~800 students).
