# Persona: Sarah Williams — Chief Technology Officer
## Tilington plc Cloud Modernisation Programme

---

**Role:** CTO, Tilington plc
**Reports to:** CEO and Board
**Priority colour:** Purple
**Communication style:** Direct, board-level language, low technical tolerance, focused on outcomes and risk

---

## Background

Sarah joined Tilington four years ago from a tier-1 UK bank where she led a cloud transformation programme. She holds a Computer Science degree from UCL and an MBA from London Business School. She is commercially sharp and has strong FCA relationships — she has already had one informal conversation with the FCA supervisor about the operational resilience remediation programme.

Sarah approved the £3.2M budget personally and presented the programme to the Board in January 2026. She is accountable for delivery and has political capital invested in this programme succeeding on time.

She is not a hands-on architect. She will not review your Terraform. She will read your one-page executive summary and ask three pointed questions.

---

## Key Priorities

1. **Programme delivery on time** — DC lease exits Q2/Q3 2027 are non-negotiable
2. **FCA relationship** — she wants to tell the regulator in Q4 2026 that remediation is complete
3. **Oracle cost** — she has already told the CFO the Oracle contract will not be renewed in Q2 2026
4. **Board confidence** — the Board gets a quarterly update; she needs architecture news to be good news

---

## Inbox Messages (In-Simulation)

### Email 1 — Kick-off, Week 1
**From:** Sarah Williams
**To:** [Candidate]
**Subject:** Welcome to the Tilington Cloud Programme

Welcome aboard. I'll be direct: this programme has a hard deadline and I need it to succeed.

Your first priority is discovery. I need to understand what we're dealing with before I commit publicly to the Oracle renewal decision in Q2. Michael will brief you on the estate — but I warn you, the documentation is patchy. Don't trust the CMDB without verifying it.

I'd like to see your initial findings by the end of Phase 1. Please structure your report so I can hand the executive summary to the Board without editing it.

One request: if you find anything that changes the programme timeline or budget, tell me immediately. I'd rather know early than be surprised in front of the Board.

Sarah

---

### Email 2 — After Phase 1 Discovery
**From:** Sarah Williams
**To:** [Candidate]
**Subject:** RE: Discovery Findings — Two Questions

Thank you for the discovery report. Two things I need clarity on:

1. The two servers you found that aren't in the CMDB — SRV-086 and SRV-087. Emma Clarke is asking whether these represent a data protection risk. Can you give me a one-paragraph risk assessment I can share with her?

2. APP-027 (Legacy Fund Accounting) — your report flags this as "unclear if still used." I need a definitive answer before we finalise the wave plan. Michael thinks it's still running. Finance says they stopped using it 18 months ago. Please investigate and confirm.

Sarah

---

### Email 3 — After Phase 3 Architecture
**From:** Sarah Williams
**To:** [Candidate]
**Subject:** ARB Date — 14 April

The Architecture Review Board is confirmed for 14 April. You will need to present your target architecture and answer questions from Emma Clarke (risk), Priya Sharma (security), and David Okafor (retail technology).

Emma is particularly focused on the data residency question — she wants written confirmation that no customer PII will leave eu-west-2 under any scenario, including the DR failover to eu-west-1. Please prepare a clear one-page answer to this question for the ARB pack.

The Board CFO will also be in the room. He will ask about cost. Have your numbers ready.

Sarah

---

### Email 4 — Phase 8, Pre-Oracle Decision
**From:** Sarah Williams
**To:** [Candidate]
**Subject:** Oracle Renewal — Decision Needed This Week

Our Oracle renewal window closes 30 April. I need your recommendation: do we renew or not renew?

The CFO wants a business case. If we don't renew, what's the risk? If we do renew, what does that cost us and what does it signal to the programme?

I need a clear recommendation with numbers by Thursday.

Sarah

---

## Stakeholder Conflicts

**With Emma Clarke (CRO):**
Sarah wants to move fast. Emma wants every control evidenced before any production workload migrates. They have had at least one heated exchange about what "production-ready" means. The candidate will need to navigate this — Emma can veto production migrations without Sarah's explicit override.

**With Michael Evans (Head of Infra):**
Sarah pushed for a faster migration timeline than Michael thinks is safe. Michael has quietly told his team the timeline is "ambitious." Sarah is aware of this and will mention it to the candidate. She wants the candidate to give her an honest view of whether the timeline is achievable.

**With the CFO (background):**
The CFO wanted AWS costs to stay below £45,000/month in Year 1. Sarah agreed to this without fully pressure-testing it. The candidate's FinOps work in Phase 8 will likely surface tension here.

---

## Meeting Notes

### Programme Kick-off — 3 February 2026
Attendees: Sarah Williams, Michael Evans, Emma Clarke, James Patel, [Candidate]

Key points:
- Sarah confirmed budget: £3.2M over 18 months
- DC lease dates confirmed: DC1 exit Q2 2027, DC2 exit Q3 2027
- Oracle renewal decision deadline: Q2 2026
- FCA remediation — Sarah confirmed they are under informal monitoring
- Sarah asked candidate to prioritise discovery and architecture in the first 8 weeks
- Emma raised concern about data residency — Sarah committed to a written policy before architecture sign-off
- James Patel confirmed EKS is the agreed container platform — no debate

Action items:
- [Candidate]: Discovery report by end of March 2026
- Michael Evans: Provide server inventory by 10 February
- Emma Clarke: Provide FCA correspondence file by 15 February
- James Patel: Set up GitHub repo access by 7 February
