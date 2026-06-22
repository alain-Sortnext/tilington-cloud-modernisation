# Tilington plc — Migration Objectives
## Cloud Modernisation Programme | STARTER — v0.1

> **Status: STARTER — Candidate extends in Phase 8**

---

## Programme Objectives

### Objective 1 — Datacentre Exit by Q3 2027
**Definition of Done:**
- All workloads migrated or decommissioned
- DC1 (London) lease handed back by 30 June 2027
- DC2 (Manchester) lease handed back by 30 September 2027
- All hardware disposal records documented for ISO 27001

### Objective 2 — FCA Operational Resilience Compliance
**Definition of Done:**
- Important Business Services (IBS) defined and documented
- Impact tolerances set and approved by Board
- AWS architecture demonstrates RTO ≤ 4h, RPO ≤ 1h for IBS
- First operational resilience scenario test passed and evidenced

### Objective 3 — Oracle Licensing Elimination
**Target:** Q2 2026 renewal decision — migrate 3 of 5 Oracle instances to Aurora PostgreSQL before renewal
**Definition of Done:**
- Customer accounts DB migrated to Aurora PostgreSQL
- Trade processing DB migrated to Aurora PostgreSQL
- Reference data DB migrated to Aurora PostgreSQL
- Oracle contract not renewed — saving: £1.4M/year

### Objective 4 — Cloud-Native Platform Operational
**Definition of Done:**
- EKS cluster operational in eu-west-2
- 4 microservices deployed (Customer, Payments, Notifications, Audit)
- CI/CD pipeline live with security scanning
- Observability stack operational (metrics, logs, traces)

---

## Migration Approach — 6Rs Classification (TODO: Candidate Completes)

| R-Strategy | Description | Tilington Candidate Apps |
|-----------|-------------|------------------------|
| Rehost (Lift & Shift) | Migrate as-is to EC2 | TODO — identify from inventory |
| Replatform | Minor optimisation, managed service | TODO |
| Repurchase | Replace with SaaS | TODO |
| Refactor / Re-architect | Significant redesign | Customer platform → microservices |
| Retire | Decommission | TODO — identify from inventory |
| Retain | Keep on-premise temporarily | TODO |

---

## Migration Waves (STARTER — TODO: Candidate defines in Phase 8)

### Wave 1 — Foundation (Month 1-3)
- AWS Landing Zone deployed
- Network connectivity established (Direct Connect or VPN)
- Identity federation configured
- Logging and monitoring baseline
- TODO: Add specific apps

### Wave 2 — Non-Production (Month 4-6)
- Dev and test environments migrated
- CI/CD pipeline operational
- TODO: Add specific apps

### Wave 3 — Non-Critical Production (Month 7-9)
- Internal back-office applications
- Reporting and batch processing
- TODO: Add specific apps

### Wave 4 — Business-Critical (Month 10-14)
- Customer-facing applications
- Core financial processing
- Oracle to Aurora migration
- TODO: Add specific apps

### Wave 5 — Final Migration & DC Exit (Month 15-18)
- Remaining workloads
- DR validation
- Datacentre decommission
- TODO: Add specific apps

---

## Success Metrics (TODO: Candidate Adds Targets)

| Metric | Current | Target | By When |
|--------|---------|--------|---------|
| Applications migrated | 0/28 | 28/28 | Q2 2027 |
| Oracle instances migrated | 0/5 | 3/5 | Q2 2026 |
| AWS monthly spend | £0 | ≤ £56,667 avg | Month 12 |
| RTO for critical services | Unknown | ≤ 4 hours | Q1 2027 |
| RPO for critical services | Unknown | ≤ 1 hour | Q1 2027 |
| Security findings (HIGH/CRITICAL) | Unknown | 0 | Ongoing |

