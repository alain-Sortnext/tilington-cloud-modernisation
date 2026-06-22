# Phase 2 — Target AWS Architecture & Landing Zone
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Enterprise AWS Landing Zone Design
**Submission types:** text_editor + file_upload
**Estimated time:** 8–12 hours

---

## Context

Discovery is complete. Sarah Williams has approved your findings and given you the green light to design the target AWS architecture. The Architecture Review Board is scheduled for 14 April. You have until then to produce an architecture that Emma Clarke, Priya Sharma, and David Okafor can scrutinise.

Your starting point: the starter files in `/docs/` and `/docs/adrs/` — ADR-001 (AWS selected) and ADR-002 (multi-account structure) are already accepted. You are building on them.

The architecture must support: 6 AWS accounts minimum, SCPs, governance guardrails, identity federation with Tilington's existing Azure AD, and the FCA compliance requirements documented in `/docs/security-requirements.md`.

---

## Deliverables

### Deliverable 1 — High-Level Design (HLD)
**File:** `/docs/hld.md`

Write the HLD document covering:

**Section 1: Solution Overview**
- Target state in one page
- Architecture principles applied (from `/docs/architecture-principles.md`)
- Key design decisions summary

**Section 2: AWS Account Structure**
- Diagram or table showing all 6+ accounts and their purpose
- Organisational Unit (OU) structure
- SCP strategy: what is blocked at which OU level? (At minimum: deny eu-west-2 exit for PII, deny root account usage, deny public S3 buckets)

**Section 3: Identity and Access Model**
- IAM Identity Centre configuration
- Azure AD federation approach
- Role hierarchy (6 roles minimum: Admin, PlatformEngineer, Developer, ReadOnly, SecurityAuditor, FinOpsViewer)
- Permission boundary strategy for developer-created roles

**Section 4: Governance Controls**
- Control Tower guardrails selected and why
- AWS Config rules required
- Tagging strategy and mandatory tags
- Budget alerts configuration

---

### Deliverable 2 — Low-Level Design (LLD)
**File:** `/docs/lld.md`

The LLD must contain specific, implementable detail:

**Account-level details:** For each of the 6 accounts — account name, OU, purpose, SCPs applied, key services
**IAM role specifications:** For each of the 6 roles — service or person, specific AWS policies attached, conditions
**SCP content:** At least 3 SCPs written in JSON (not described — actually written):
  - Deny leaving AWS region eu-west-2 for services that handle PII
  - Deny creating S3 buckets with public access
  - Deny disabling CloudTrail

---

### Deliverable 3 — Landing Zone Architecture Diagram
**File:** `/architecture/target-state.drawio` + PNG export

Show:
- AWS Organization root → OUs → Accounts
- Control Tower in management account
- Each account with its primary services
- Cross-account trust relationships
- Connectivity to on-premise (placeholder — detailed in Phase 3)

---

### Deliverable 4 — Governance Framework
**File:** `/docs/governance-framework.md`

- Change management process for AWS infrastructure (who approves what)
- IaC only policy — what constitutes a ClickOps violation and what happens
- Security exception process
- Cost governance: who approves new spend above what threshold
- How compliance is monitored continuously (AWS Config + Security Hub)

---

### Deliverable 5 — Architecture Decision Records
Add at least 3 new ADRs to `/docs/adrs/`:

Required ADRs:
- **ADR-003:** Primary AWS region choice (eu-west-2)
- **ADR-004:** Terraform as primary IaC tool
- **ADR-005:** EKS for container orchestration (EKS vs ECS — document why EKS)

Optional extra ADRs for distinction-level work:
- NAT Gateway HA vs cost trade-off
- IAM Identity Centre vs legacy IAM federation
- Control Tower vs manual account vending

---

## Anti-Fake Validation

Your submission must include:
- At least 3 SCPs written in actual JSON — not described in prose
- Specific AWS account names (not just "production account")
- IAM role trust policies for at least one cross-account role
- Emma Clarke's data residency requirement addressed specifically in the LLD
- Reference to Tilington's Azure AD in the identity design
- The EKS vs ECS ADR must include specific trade-offs relevant to Tilington, not generic

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Account structure design | 20 | 6+ accounts; OU hierarchy; rationale for separation |
| SCP content — written in JSON | 20 | 3+ SCPs; correct JSON syntax; appropriate deny scope |
| Identity and access model | 20 | IAM Identity Centre; Azure AD federation; role hierarchy |
| ADRs — quality and completeness | 20 | 3+ new ADRs; context/decision/consequences format; Tilington-specific |
| Architecture diagram quality | 10 | Shows org structure; accounts; services; readable |
| Governance framework quality | 10 | Change process; IaC policy; cost governance |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions for "AWS multi-account design, Control Tower, landing zone" from UK financial services or enterprise employers. Suggested sources: Glassdoor (AWS, Accenture, Deloitte Cloud practice, HSBC Technology), LinkedIn interview prep posts.
>
> Q1: "How would you design an AWS multi-account structure for a regulated financial services firm?" — [VERIFY SOURCE]
> Q2: "What is AWS Control Tower and when would you use it over a custom account vending machine?" — [VERIFY SOURCE]
> Q3: "Explain the difference between an SCP and an IAM policy. When would each be applied?" — [VERIFY SOURCE]
> Q4: "How do you handle identity federation between on-premise Active Directory and AWS?" — [VERIFY SOURCE]
> Q5: "What governance controls would you put in place from Day 1 on a new AWS organisation?" — [VERIFY SOURCE]

