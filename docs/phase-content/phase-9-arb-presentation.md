# Phase 9 — Architecture Review Board & Executive Presentation
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Executive AWS Architecture Portfolio
**Submission types:** text_editor + file_upload
**Estimated time:** 8–12 hours

---

## Context

You have completed the full technical programme. Now you must synthesise everything into board-level governance deliverables and defend your architecture at the Architecture Review Board.

Sarah Williams has scheduled the ARB for 14 April. The panel: Emma Clarke (CRO), Priya Sharma (Head of InfoSec), David Okafor (Head of Retail Technology), and the CFO. Emma has already told you she will ask three specific questions — they are in her inbox message in the personas file.

This phase tests whether you can translate deep technical architecture into clear governance language. Your audience will not read your Terraform. They will read your one-page risk summary and ask pointed questions.

---

## Deliverables

### Deliverable 1 — Final Architecture Review Board Pack
**File:** `/presentations/arb-presentation.pptx`

Create a PowerPoint/Google Slides ARB pack (12–16 slides maximum):

**Slide 1:** Programme title, date, presented by
**Slide 2:** Executive summary — what we built, why, outcomes achieved
**Slide 3:** AWS architecture overview diagram (current-to-target)
**Slide 4:** Multi-account structure and governance model
**Slide 5:** Security posture — key controls, Security Hub findings closed, NCSC compliance status
**Slide 6:** Data residency confirmation — PII stays in eu-west-2 (Emma Clarke's question 1)
**Slide 7:** Operational resilience — RTO/RPO matrix, DR design, FCA PS21/3 compliance evidence
**Slide 8:** Migration progress — wave plan status (if Phase 8 complete, show % migrated)
**Slide 9:** FinOps — January spend, budget vs actual, savings achieved/planned
**Slide 10:** Oracle renewal recommendation (for CFO and Sarah Williams)
**Slide 11:** Outstanding risks — honest risk register summary for the Board
**Slide 12:** Next steps and timeline to DC exit
**Slide 13 (optional):** Technical appendix — detailed architecture for Priya Sharma's questions
**Slide 14 (optional):** DR test results (if tested)

---

### Deliverable 2 — Architecture Decision Log
**File:** `/docs/architecture-decision-log.md`

Compile every ADR from all phases into a single decision log:

| ADR # | Title | Status | Date | Decided By | Summary |
|-------|-------|--------|------|-----------|---------|
| ADR-001 | AWS as primary cloud | Accepted | 2026-02-01 | CTO, CRO | ... |
| ADR-002 | Multi-account structure | Accepted | ... | ... | ... |
| ADR-003 through ADR-NNN | ... | ... | ... | ... | ... |

For any ADR that was accepted and then revised or superseded during the programme, document what changed and why. This is the governance audit trail.

---

### Deliverable 3 — Risk & Trade-Off Summary
**File:** `/docs/final-risk-summary.md`

**Section 1: Accepted Risks**
Risks that the programme has accepted and why. Each must be signed off by a named stakeholder.

Example format:
| Risk | Accepted by | Rationale | Residual controls |
|------|-------------|-----------|------------------|
| ORCL-04 and ORCL-05 migration deferred to Wave 5 | Sarah Williams | Team capacity constraint; priority on customer-facing Oracle instances | Existing Oracle contract covers until Wave 5 completion |

**Section 2: Key Trade-offs Made**
Architectural decisions where you chose between competing options. For each:
- What was the trade-off?
- What did you choose?
- What did you give up?
- Who approved the trade-off?

Required trade-offs to document (from the programme):
- NAT Gateway: 1 per VPC (cost) vs 3 per VPC (HA) — document your decision
- Aurora instance class: right-sized vs over-provisioned for Oracle parity
- Direct Connect vs VPN for hybrid connectivity
- Rehost vs Refactor for APP-002 Trade Processing Engine timing
- Public vs private EKS API server endpoint

**Section 3: Open Risks**
Risks that remain open at ARB. Each needs an owner and a resolution date.

---

### Deliverable 4 — Final Portfolio Summary
**File:** `/docs/final-portfolio-summary.md`

A one-page professional summary of what you built, suitable for:
- Including in a CV portfolio
- Sharing with a recruitment agency
- LinkedIn project description

Must cover:
- Programme scope (what it was)
- Your role and responsibilities
- Key deliverables and technical achievements
- Business outcomes achieved (Oracle cost saving, FCA compliance, DC exit enablement)
- Technologies used (with specifics — not just "AWS" but specific services)
- Skills demonstrated (mapped back to the skills blueprint)

---

## ARB Questions You Must Prepare For

Based on Emma Clarke's email (in her persona file), prepare written answers for:

**Question 1 (Emma Clarke):** "Confirm that during DR failover to eu-west-1, no customer PII is replicated to or processed in that region. What technical controls enforce this? What happens if the control fails?"

Your answer must name:
- The specific S3 bucket replication policy (or absence of it)
- The Aurora cross-region strategy (snapshot only, no live replica in eu-west-1 for PII data)
- The DynamoDB Global Tables exclusion for AuditTrail
- The SCP that prevents eu-west-1 from being used for PII data
- Failure mode: if SCP is bypassed, what detective control catches it? (CloudTrail + Config rule)

**Question 2 (Emma Clarke):** "How does your architecture maintain operational resilience if AWS eu-west-2 experiences an availability event?"

Your answer must cover:
- Multi-AZ within eu-west-2 (immediate AZ failure handled)
- eu-west-1 warm standby (eu-west-2 region failure — RTO/RPO targets)
- Route 53 health check failover mechanism
- What happens to in-flight payments during failover (PCI DSS data integrity)

**Question 3 (Emma Clarke):** "Who within Tilington has administrative access to the AWS Production account? How is privileged access managed and audited?"

Your answer must name:
- Specific IAM Identity Centre roles with Production account access
- Break-glass procedure (what is it, who initiates, what is logged)
- CloudTrail coverage of all privileged actions
- Review cadence (monthly access review by Priya Sharma)

---

## Anti-Fake Validation

Required specifics:
- ARB deck must reference actual January spend total from the CSV (candidates must have calculated this)
- Emma Clarke's three questions must be answered with specific technical mechanisms, not prose assertions
- Architecture decision log must contain all ADRs created during the programme (minimum ADR-001 through ADR-007 plus candidate additions)
- Trade-off on NAT Gateway (1 vs 3) must reference the actual cost figure (~£90/month per additional NAT GW)
- Oracle renewal recommendation must give a specific recommendation (renew or don't renew) — not "it depends"
- Portfolio summary must name real AWS services with specificity

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| ARB presentation quality and completeness | 30 | All 12 slides; board-level language; specific data referenced |
| Emma Clarke's 3 questions answered specifically | 25 | Technical mechanisms named; not prose; DR PII constraint addressed |
| Architecture decision log | 15 | All ADRs from programme; format correct; superseded ADRs noted |
| Risk and trade-off summary | 20 | Accepted risks with stakeholder sign-off; trade-offs with rationale |
| Portfolio summary — professional quality | 10 | Specific; CV-ready; outcomes quantified |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions on architecture governance, ARB, executive communication, and technical leadership from UK financial services employers.
>
> Q1: "How do you present a complex technical architecture to a non-technical executive audience?" — [VERIFY SOURCE]
> Q2: "Describe a time you had to defend an architectural decision to senior stakeholders who pushed back. What happened?" — [VERIFY SOURCE]
> Q3: "What is an Architecture Review Board and what makes one effective?" — [VERIFY SOURCE]
> Q4: "How do you balance technical perfectionism with delivery deadlines in a regulated environment?" — [VERIFY SOURCE]
> Q5: "Walk me through the biggest architectural risk you have accepted on a project and how you managed it." — [VERIFY SOURCE]

