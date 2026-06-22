# Phase 3 — Networking, Security & Hybrid Cloud
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Enterprise Security & Network Architecture
**Submission types:** text_editor + file_upload
**Estimated time:** 8–12 hours

---

## Context

The Landing Zone is approved. Now you must design the network architecture that connects Tilington's two datacentres to AWS, and the security controls that satisfy Emma Clarke, Priya Sharma, and the NCSC Cloud Security Principles.

The starter Terraform in `/terraform/networking/` has the VPC and public subnets — but private subnets, NAT Gateways, route tables, security groups, and VPC Flow Logs are all marked as TODO. The security requirements in `/docs/security-requirements.md` list the AWS services required but leave the specific controls empty.

James Patel has flagged a concern: the production VPC currently has a security group (sg-0abc123) with port 22 open to 0.0.0.0/0 (finding SF-004). This must be in your architecture as a solved problem, not a known risk.

---

## Deliverables

### Deliverable 1 — Network Architecture Diagram
**File:** `/architecture/networking.drawio` + PNG

Show:
- DC1 and DC2 connectivity to AWS (Direct Connect or VPN — justify your choice in an ADR)
- VPC design: 3 tiers (public, private-app, private-data) across 3 AZs
- Transit Gateway for multi-account networking
- Route 53 private hosted zones
- VPC endpoints for AWS services (S3, DynamoDB, ECR, KMS — which ones and why)
- Egress: NAT Gateway placement (1 vs 3 — reference your ADR from Phase 2)
- On-premise CIDR ranges: DC1 10.10.0.0/16, DC2 10.20.0.0/16; AWS prod 10.30.0.0/16

---

### Deliverable 2 — Hybrid Cloud Connectivity Design
**File:** `/docs/hybrid-connectivity.md`

Make a justified recommendation: AWS Direct Connect vs Site-to-Site VPN (or both)?

Must include:
- Cost comparison (Direct Connect: ~£380/month from cost report; VPN: estimate)
- Latency requirements for Oracle Data Guard replication during migration
- Bandwidth requirements (estimate from server inventory — how much data to move?)
- Recommendation with rationale
- During-migration vs post-migration connectivity approach

---

### Deliverable 3 — Security Architecture Document
**File:** `/docs/security-architecture.md`

Complete the incomplete security-requirements.md into a full security architecture document:

**Section 1: Security Services Configuration**
For each required service in the STARTER table (CloudTrail, Config, GuardDuty, Security Hub, KMS, IAM Identity Centre, WAF, Macie, Inspector):
- Specific configuration decisions
- Which accounts it runs in
- What it alerts on and to whom
- How logs flow to the central logging account

**Section 2: KMS Key Strategy**
- How many CMKs, for what purpose
- Key rotation policy
- Key access policies (with specific IAM principals)

**Section 3: Security Group Design**
Fix finding SF-004 (SSH 0.0.0.0/0). Design security groups for:
- ALB (public-facing)
- EKS nodes
- Aurora PostgreSQL
- Internal services
Each must follow least-privilege. No SSH to 0.0.0.0/0 anywhere.

**Section 4: NCSC 14 Cloud Security Principles**
Map ALL 14 principles to specific AWS controls. Do not leave any as TODO.

---

### Deliverable 4 — Compliance Mapping
**File:** `/security/compliance-mapping.md`

Complete the starter compliance-mapping-template.md with all 14 NCSC principles mapped to specific AWS controls.

Also add:
- ISO 27001 domains A.9, A.10, A.12, A.13 mapped to AWS controls
- FCA SYSC 13 operational risk controls mapped to AWS services

---

### Deliverable 5 — Risk Register Extension
**File:** `/docs/risk-register.md`

Create a standalone risk register (extend from the discovery report). Must include:
- SF-002 and SF-018 (public S3 bucket + PII exposure) as a confirmed incident, not just a risk
- SF-006 (active SSH brute force attack) assessed and remediated
- At least 8 total risks, each with: ID, description, impact (1-5), likelihood (1-5), risk score, owner, mitigation, residual risk, status

---

### Terraform Updates
**Files:** Complete the TODOs in `/terraform/networking/main.tf`

Complete the following in Terraform:
- Private application subnets (3 AZs)
- Private data subnets (3 AZs)
- NAT Gateway(s) — justify count in a comment
- Route tables: public (→ IGW) and private (→ NAT GW)
- VPC Flow Logs with CloudWatch destination
- Security groups: ALB, EKS nodes, Aurora — all least-privilege

Push completed Terraform to your GitHub branch.

---

## Anti-Fake Validation

Required specifics:
- VPC CIDR must not conflict with DC1 (10.10.0.0/16), DC2 (10.20.0.0/16), or non-prod (10.40.0.0/16)
- NCSC principles — all 14 must be addressed with specific AWS service (not generic)
- SF-004 remediation must be specific (SSM Session Manager replaces SSH — show the SG rule removed)
- Hybrid connectivity recommendation must include a cost figure (Direct Connect £380/month from cost report)
- VPC endpoints: must name which endpoints reduce the cross-AZ cost from the January report (S3 and DynamoDB gateway endpoints are free and eliminate cross-AZ traffic)

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Network architecture diagram | 20 | VPC tiers; AZ spread; DC connectivity; VPC endpoints; Transit GW |
| Hybrid connectivity recommendation | 15 | Justified choice; cost comparison; migration vs steady-state |
| Security architecture completeness | 25 | All services configured; KMS strategy; SG least-privilege |
| NCSC 14 principles mapping | 20 | All 14 mapped to specific AWS controls — no blanks |
| Terraform networking completion | 15 | Private subnets; NAT GW; route tables; flow logs; SGs |
| Risk register quality | 5 | 8+ risks; SF-002/SF-018 captured as incident |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions on VPC design, hybrid connectivity, and AWS security architecture from UK financial services employers.
>
> Q1: "How would you design a VPC for a financial services workload that must meet FCA operational resilience requirements?" — [VERIFY SOURCE]
> Q2: "When would you use Direct Connect vs VPN for hybrid cloud connectivity?" — [VERIFY SOURCE]
> Q3: "Explain VPC endpoints — what types exist and when would you use each?" — [VERIFY SOURCE]
> Q4: "How do you implement zero-trust networking in AWS?" — [VERIFY SOURCE]
> Q5: "Walk me through how you would respond to a GuardDuty finding of SSH brute force on a production EC2 instance." — [VERIFY SOURCE]

