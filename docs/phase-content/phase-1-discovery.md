# Phase 1 — Discovery & Current State Assessment
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Enterprise Discovery Pack
**Submission types:** text_editor + file_upload
**Estimated time:** 6–10 hours

---

## Context

You are the newly appointed Lead AWS Solutions Architect on Tilington's Cloud Modernisation Programme. Your first task is to make sense of what Tilington actually has before designing anything.

The estate is messier than anyone admits:
- 90 servers documented in the inventory — but Michael Evans has told you two were discovered during a physical audit and are not in the CMDB (SRV-086 and SRV-087)
- 28 applications — but at least one (APP-027) has unclear operational status. Finance says it was decommissioned 18 months ago. Michael sees database activity that suggests otherwise.
- APP-006 (Document Management System) references MSSQL-03 in its dependencies, but MSSQL-03 does not appear in the server inventory
- The documentation coverage is approximately 30% — most systems are undocumented

Read the company brief, the server inventory, the application inventory, and the dependency map in `/migration/`. Read James Patel's and Michael Evans's inbox messages. Then complete the deliverables below.

---

## Deliverables

### Deliverable 1 — Discovery Assessment Report
**File:** `/docs/discovery-report.md`

Write a structured discovery report covering:

**Section 1: Executive Summary (1 page)**
- Current state in 3-4 bullet points
- Top 3 risks requiring immediate attention
- Recommendation: is the 18-month timeline achievable? Be honest.

**Section 2: Infrastructure Assessment**
- Summary table of 90 servers by OS, EOL status, and patch health
- How many servers are on EOL OS? List them by server ID.
- How many servers have CRITICAL patch status?
- What is the VMware EOL risk?
- The two undocumented servers (SRV-086, SRV-087) — what is your risk assessment?

**Section 3: Application Portfolio Assessment**
- Classify all 28 applications using the 6Rs (you may use the CSV as a reference)
- Applications with unclear status — specifically APP-027: what is your recommendation?
- Single points of failure identified

**Section 4: Dependency Analysis**
- Which applications have undocumented dependencies?
- Critical path applications (those with the most incoming dependencies)
- The MSSQL-03 mystery: what is your finding and what action do you recommend?

**Section 5: Compliance Gap Analysis**
- EOL OS servers and their regulatory implications (ISO 27001, FCA)
- CMDB accuracy risk
- Documentation coverage risk

**Section 6: Risks and Issues**
- Extend the risk register in company-brief.md with at least 5 additional risks you have identified
- Each risk must have: description, impact, likelihood, owner, mitigation

---

### Deliverable 2: Current State Architecture Diagram
**File:** `/architecture/current-state.drawio` (export a .png copy too)

Draw the current on-premise architecture showing:
- DC1 (Canary Wharf) and DC2 (Salford) as separate domains
- Key server tiers: DMZ, App, Data, Infra
- MPLS connectivity between DCs
- External connections (internet, counterparties, regulators)
- Oracle database instances and their relationships
- The 5 Oracle instances and which servers host them

Use Draw.io (free: app.diagrams.net). Export as .drawio and .png.

---

### Deliverable 3: Application Inventory Assessment
**File:** `/migration/application-inventory.xlsx` (or .csv)

Complete the application inventory with:
- Your 6R classification for all 28 applications (the template has 5 pre-classified)
- Migration wave assignment
- Dependency count
- Complexity rating (LOW / MEDIUM / HIGH / VERY HIGH)
- Your confidence in the classification (HIGH / MEDIUM / LOW — flag where you need more information)

---

### Deliverable 4: Stakeholder Register
**File:** `/docs/stakeholder-register.md`

Create a stakeholder register with all 6 named stakeholders. For each:
- Name, role, interest level (HIGH/MEDIUM/LOW), influence level
- Key concern for this programme
- Communication preference
- Potential conflict or blocker risk

---

## Anti-Fake Validation

Your submission must reference specific data from the CSV files. Generic answers that could apply to any cloud migration will score zero on evidence criteria.

Required specifics your submission must include:
- Exact count of EOL OS servers (with server IDs)
- Exact count of CRITICAL patch status servers  
- The specific finding about MSSQL-03 and your recommendation
- Your APP-027 recommendation with reasoning
- The SRV-086/SRV-087 risk classification with reasoning
- At least one specific dependency chain from dependency-map.csv (e.g. APP-001 → APP-012 → External:AzureAD)
- Reference to the specific ORCL-04/ORCL-05 shared server finding (SRV-076)

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Infrastructure analysis completeness | 20 | All 90 servers addressed; EOL count correct; CRITICAL count correct |
| Application portfolio — 6R classification | 20 | All 28 apps classified; reasoning given; confidence flagged |
| Dependency analysis — messy reality | 20 | MSSQL-03 finding; SRV-086/087 risk assessment; ORCL-04/05 shared server noted |
| Risk register quality | 15 | 5+ new risks identified; each has impact/likelihood/owner/mitigation |
| Current state architecture diagram | 15 | Shows DC1/DC2 separation; Oracle instances; external connections; tiers |
| Executive summary quality | 10 | Board-readable; honest about timeline; specific risk calls |
| Total | 100 | |

---

## Interview Questions (Real — Research Required)

> Per simulation design rules: interview questions must be sourced from verified Glassdoor, Indeed, or employer interview reports. If sourcing cannot be confirmed, the question is flagged as research required.
>
> RESEARCH REQUIRED: Provide 5 real interview questions for "AWS Solutions Architect discovery and assessment" from UK financial services employers. Sources to check: Glassdoor (Lloyds Banking Group, HSBC, Barclays AWS Solutions Architect interview reviews), LinkedIn interview questions, Indeed company reviews.
>
> Placeholder format (to be replaced with verified sources):
>
> Q1: "How would you approach discovering dependencies in a legacy estate where documentation is poor?" — [Source: Glassdoor, Lloyds Banking Group, Solutions Architect, 2024 — VERIFY]
> Q2: "What is the 6Rs framework and how do you decide between rehost and replatform?" — [Source: Indeed, HSBC Technology, Cloud Architect, 2025 — VERIFY]
> Q3: "How do you handle stakeholder resistance to cloud migration from an infrastructure team that owns the legacy estate?" — [Source: Glassdoor, NatWest, Cloud Architect, 2024 — VERIFY]
> Q4: "Walk me through how you would classify an application portfolio for migration prioritisation." — [Source: Glassdoor, Barclays, Solutions Architect, 2024 — VERIFY]
> Q5: "What are the FCA's operational resilience requirements and how do they affect your migration approach?" — [Source: Indeed, Standard Chartered, Cloud Solutions Architect, 2025 — VERIFY]

