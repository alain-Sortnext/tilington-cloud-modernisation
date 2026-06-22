# Persona: Michael Evans — Head of Infrastructure
## Tilington plc Cloud Modernisation Programme

---

**Role:** Head of Infrastructure, Tilington plc
**Reports to:** CTO (Sarah Williams)
**Priority colour:** Teal
**Communication style:** Honest, cautious, technical, sometimes defensive about the legacy estate

---

## Background

Michael has been at Tilington for eleven years. He built DC1 from the ground up in 2014 and DC2 in 2016. He knows every server in the estate personally — or at least he thought he did until SRV-086 and SRV-087 turned up in your audit.

He is not anti-cloud. He attended AWS re:Invent in 2023 and came back enthusiastic. But he is genuinely worried about migrating 90 servers and 28 applications in 18 months with a team of six infrastructure engineers who have never worked on AWS at scale.

He has AWS Solutions Architect Associate certification but has never used Terraform in production.

He is your closest day-to-day ally but he will push back if he thinks something is unsafe.

---

## Key Priorities

1. **Nothing breaks in production during migration** — his team gets called at 3am if it does
2. **His team's wellbeing** — he is worried about burnout; the team is already stretched
3. **Honest timeline** — he thinks 18 months is tight and will say so privately
4. **The Oracle migration** — he has deep knowledge of ORCL-01 and ORCL-02 and is concerned about the PL/SQL complexity
5. **The two mystery servers** — he is embarrassed about SRV-086 and SRV-087 and wants to resolve this quickly

---

## Inbox Messages (In-Simulation)

### Slack Message 1 — Day 1
**From:** Michael Evans
**To:** [Candidate]
**Channel:** #cloud-programme

Hey — welcome. I've pushed the server inventory to the repo but fair warning: it's not complete. We found two servers in DC1 Rack 21 during the audit last week that aren't in the CMDB. SRV-086 and SRV-087. Nobody knows what they are. I've asked around and nobody's owning them. Could be test boxes from 2022 or could be something important. I need your help figuring this out.

Also — APP-027 (Legacy Fund Accounting). Finance say they stopped using it 18 months ago. But I'm still seeing database sessions on ORCL-05 that look like it's still connecting. Can you help me nail down whether this is active or not?

Michael

---

### Slack Message 2 — Week 2
**From:** Michael Evans
**To:** [Candidate]
**Channel:** #cloud-programme

One thing you need to know about APP-006 (Document Management System) — it's listed as connecting to MSSQL-03 but I cannot find MSSQL-03 anywhere in the inventory. SRV-030 references it. It might be a SQL Server instance that lives on the same box as something else. Or it might be a ghost entry from when we consolidated servers in 2021. Either way the dependency map is wrong somewhere. FYI for your discovery report.

---

### Email 1 — Oracle Migration Concern
**From:** Michael Evans
**To:** [Candidate]
**Subject:** Oracle — We Need to Talk

I need to flag something before it becomes a problem.

ORCL-01 has 847 stored procedures. I've done a rough pass with the Oracle Schema Conversion Tool and it's flagging 214 of them as requiring manual conversion. Some of them are PL/SQL packages that took our DBA six months to write.

ORCL-02 is even more complex — it has custom scheduler jobs and 3 database links to external systems (SWIFT, Refinitiv, a legacy FTP gateway).

I'm not saying we can't do it. I'm saying Sarah's timeline assumes this is straightforward and it isn't. Can you factor this into your Phase 8 migration planning and give me an honest view of the risk?

Michael

---

### Email 2 — Team Capacity
**From:** Michael Evans
**To:** [Candidate]
**Subject:** Resource constraint you should know about

Sarah asked me not to raise this in the programme call but I think you need to know.

I have six engineers. Two of them are 80% dedicated to keeping the current estate running — patching, incidents, BAU. That leaves me with effectively four people for the migration. Of those four, only James Patel has real AWS experience.

I've flagged this with Sarah. She's told me to use contractors. But getting contractors onboarded takes 6-8 weeks with our security clearance process and we've not started.

This is a real risk to the timeline. Please document it.

Michael

---

## Stakeholder Conflicts

**With Sarah Williams (CTO):**
Michael thinks the timeline was set without fully understanding the Oracle complexity or the team capacity constraint. He raises this in 1:1s with Sarah but softens it in programme calls. He will be honest with the candidate about his concerns if asked directly.

**With James Patel (Cloud Platform Lead):**
Occasional tension about approach. James wants to build everything cloud-native from the start. Michael wants to rehost some workloads first and refactor later. They respect each other but disagree on pace.

---

## Technical Knowledge the Candidate Can Use

Michael can provide context on:
- Which Oracle stored procedures are most complex (ORCL-01 package: `customer_ledger_pkg` is the most critical and complex)
- Why ORCL-04 and ORCL-05 share SRV-076 (it was a cost-saving measure in 2020 — he had two databases left over after a consolidation project and one server with spare capacity)
- The DC1 to DC2 network topology — MPLS with 10Gbps dark fibre, latency ~8ms
- The 3am batch window — ORCL-04 batch runs 2am-5am nightly; any migration activity must avoid this window
