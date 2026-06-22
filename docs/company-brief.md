# Tilington plc — Company Brief
## Cloud Modernisation Programme | Version 0.1 — STARTER DOCUMENT

---

## 1. Company Overview

**Tilington plc** is a UK-regulated financial services firm headquartered in London EC2.

Business lines:
- **Tilington Asset Management** — institutional asset management, £4.2bn AUM
- **Tilington Retail Financial Services** — retail savings, ISAs, and investment products, ~180,000 individual customers

Offices: London (head office), Manchester (operations), Edinburgh (fund management). 1,200 employees.

Regulated by: **Financial Conduct Authority (FCA)** and **Prudential Regulation Authority (PRA)**

---

## 2. Current Technology Estate

### Datacentres

| Site | Location | Role | Lease Expiry |
|------|----------|------|-------------|
| DC1 Primary | Canary Wharf, London | Production workloads | Q3 2027 |
| DC2 Secondary | Salford, Manchester | DR + batch processing | Q3 2027 |

### Infrastructure

- **90 servers total** — 58 in DC1, 32 in DC2
- OS: Windows Server 2012 R2 (34), Windows Server 2019 (18), RHEL 7 (28), RHEL 8 (10)
- Virtualisation: VMware vSphere 6.7 (EOL October 2022)
- Primary DB: Oracle Database 19c — 5 instances — £1.4M/year licensing
- Secondary: SQL Server 2016 (3 instances), MySQL 5.7 (4 instances)
- Storage: NetApp FAS 8200 (DC1), Dell EMC Unity (DC2)
- Network: MPLS between DC1/DC2, 10Gbps dark fibre, BT internet breakout

### Application Portfolio

- 28 applications total — 6 customer-facing, 22 internal
- Average application age: 11.4 years
- Documentation coverage: ~30%
- Single points of failure identified: 14

---

## 3. Business Drivers

**Driver 1 — Datacentre Lease Expiry (HARD DEADLINE)**
Both leases expire Q3 2027. No renewal. All workloads must migrate or decommission.

**Driver 2 — FCA Operational Resilience (PS21/3)**
Impact tolerances deadline was 31 March 2025. Tilington is in active FCA remediation. Cloud migration is the primary remediation path.

**Driver 3 — Oracle Licensing**
£1.4M/year. 3-year renewal due Q2 2026. Migration to Aurora PostgreSQL eliminates this. Target saving: £4.2M over 3 years.

**Driver 4 — Technology Debt**
VMware EOL, Windows 2012 EOL. ISO 27001 and FCA compliance at risk.

---

## 4. CTO Mandate

> "We will migrate all production workloads to AWS by Q2 2027, decommission both datacentres by Q3 2027, achieve FCA operational resilience compliance through cloud architecture, and eliminate our Oracle licensing cost before the Q2 2026 renewal decision."
>
> — Sarah Williams, CTO, February 2026

Board-approved budget: **£3,200,000 over 18 months**

---

## 5. Budget Breakdown

| Category | Budget |
|----------|--------|
| AWS infrastructure Year 1 | £680,000 |
| AWS infrastructure Year 2 | £520,000 |
| Professional services / architecture | £480,000 |
| Migration tooling and licences | £180,000 |
| Training and enablement | £95,000 |
| Contingency (15%) | £367,500 |
| Reserved / unallocated | £877,500 |
| **Total** | **£3,200,000** |

---

## 6. Regulatory Requirements

| Regulation | Key Requirement |
|------------|----------------|
| FCA PS21/3 | Operational resilience — RTO ≤ 4h, RPO ≤ 1h for critical services |
| FCA SYSC | AWS = material outsourcing — FCA notification required |
| UK GDPR | Customer PII must remain in eu-west-2 (London) only |
| ISO 27001 | Full controls mapping across AWS services |
| NCSC Cloud Security Principles | All 14 principles must be addressed |
| PCI DSS v4 | Payments service in PCI scope |
| PRA SS2/21 | Cloud resilience stress testing required |

---

## 7. Programme Timeline

| Milestone | Target Date |
|-----------|------------|
| Discovery complete | March 2026 |
| Architecture approved at ARB | April 2026 |
| IaC platform ready | May 2026 |
| Kubernetes platform + CI/CD live | June 2026 |
| Migration waves 1-3 complete | October 2026 |
| DR test passed | November 2026 |
| ARB sign-off and board presentation | December 2026 |
| DC1 decommission | Q2 2027 |
| DC2 decommission | Q3 2027 |

---

## 8. Stakeholders

| Name | Role | Key Concern |
|------|------|-------------|
| Sarah Williams | CTO | On-time delivery, board confidence |
| Michael Evans | Head of Infrastructure | Stability during migration, team capacity |
| Emma Clarke | Chief Risk Officer | FCA compliance, data residency, audit trail |
| James Patel | Cloud Platform Lead | IaC quality, Kubernetes, GitOps |
| David Okafor | Head of Retail Technology | Customer app stability |
| Priya Sharma | Head of Information Security | Zero-trust, IAM, NCSC compliance |

---

## 9. AWS Region Strategy

| Region | Purpose |
|--------|---------|
| eu-west-2 London | Primary production — all customer data |
| eu-west-1 Ireland | DR replica — no PII |

Multi-AZ required for all production workloads.

---

## 10. Known Risks (STARTER — TODO: Candidate extends this in Phase 1)

| # | Risk | Impact | Likelihood | Owner | Status |
|---|------|--------|-----------|-------|--------|
| R-001 | Oracle migration complexity underestimated | HIGH | HIGH | Michael Evans | Open |
| R-002 | DC1/DC2 network dependencies undocumented | HIGH | HIGH | Michael Evans | Open |
| R-003 | FCA material outsourcing notification not filed | HIGH | MED | Emma Clarke | Open |
| R-004 | VMware EOL security exposure during migration | MED | HIGH | Priya Sharma | Open |
| R-005 | Team AWS skills gap | MED | HIGH | James Patel | Open |
| R-006 | ??? | ??? | ??? | ??? | TODO |
| R-007 | ??? | ??? | ??? | ??? | TODO |

---

*Version 0.1 — STARTER DOCUMENT — Candidate extends all sections in Phase 1*
