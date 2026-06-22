# Tilington plc — Migration Strategy
## STATUS: STARTER — Candidate completes in Phase 8

---

## 1. Migration Approach

The Tilington Cloud Modernisation Programme uses a phased migration approach based on the AWS 6Rs framework.

### 6Rs Application (TODO: Candidate Completes for All 28 Apps)

| R-Strategy | Definition | Example in Tilington Context |
|-----------|-----------|------------------------------|
| Rehost (Lift & Shift) | Migrate to EC2 without changes | Legacy batch reporting jobs |
| Replatform | Move to managed service with minor changes | Oracle → Aurora PostgreSQL |
| Repurchase | Replace with SaaS equivalent | TODO: Identify candidates |
| Refactor / Re-architect | Redesign as cloud-native | Legacy customer platform → microservices |
| Retire | Decommission — no longer needed | TODO: Identify candidates |
| Retain | Keep on-premise temporarily | TODO: Identify — and define exit criteria |

---

## 2. Application Classification (STARTER — 5 of 28 shown)

| App ID | Application | Current Platform | 6R Strategy | Wave | Priority | Owner |
|--------|-------------|-----------------|-------------|------|----------|-------|
| APP-001 | Customer Portal (web) | RHEL 7 + Tomcat | Refactor → microservices | Wave 4 | Critical | David Okafor |
| APP-002 | Trade Processing Engine | Windows 2012 + Oracle | Replatform → Aurora PostgreSQL | Wave 3 | Critical | Michael Evans |
| APP-003 | Risk Calculation Engine | RHEL 8 + Oracle | TODO: Candidate classifies | TODO | High | Michael Evans |
| APP-004 | Internal Reporting Portal | Windows 2019 + SQL Server | TODO: Candidate classifies | TODO | Medium | David Okafor |
| APP-005 | Email Notification Service | RHEL 7 + MySQL | Refactor → Notifications microservice | Wave 2 | Medium | James Patel |
| APP-006 | ??? | ??? | TODO | TODO | TODO | TODO |
| ... | 23 more apps | TODO: Candidate completes from inventory | | | | |

---

## 3. Migration Wave Plan (STARTER)

### Wave 0 — Foundation (Months 1-2)
**Goal:** AWS Landing Zone deployed, network connected, identity federated

Workloads: NONE (infrastructure only)

Activities:
- [ ] AWS Organizations and Control Tower deployed
- [ ] All 6 accounts provisioned
- [ ] Direct Connect or VPN to DC1 and DC2 established
- [ ] IAM Identity Centre configured with Azure AD federation
- [ ] CloudTrail, GuardDuty, Security Hub enabled in all accounts
- [ ] Terraform state bucket and DynamoDB lock table created
- [ ] First Well-Architected Review completed

Exit criteria:
- EKS cluster healthy with 0 HIGH/CRITICAL Security Hub findings
- VPN/Direct Connect connectivity tested with DC1 and DC2

---

### Wave 1 — Non-Production (Months 3-4)
**Goal:** Dev and test environments migrated, CI/CD operational

Workloads:
- APP-005 (Email Notification Service) — dev and test only
- TODO: Candidate identifies 3-5 more low-risk applications

Exit criteria:
- CI/CD pipeline deploying to non-production EKS
- All non-prod Oracle connections using Aurora PostgreSQL equivalent

---

### Wave 2 — Non-Critical Internal (Months 5-7)
TODO: Candidate defines

---

### Wave 3 — Business-Critical Internal (Months 8-11)
TODO: Candidate defines — must include APP-002 (Trade Processing Engine)

---

### Wave 4 — Customer-Facing (Months 12-15)
TODO: Candidate defines — must include APP-001 (Customer Portal)
Note: This wave requires FCA operational resilience testing before cutover

---

### Wave 5 — Final Cleanup and DC Exit (Months 16-18)
TODO: Candidate defines

---

## 4. Cutover Plan Template (STARTER — Candidate Applies to Each App)

For each application cutover:

| Step | Action | Owner | Duration | Rollback |
|------|--------|-------|----------|---------|
| T-7 days | Final DR test in AWS | James Patel | 4 hours | N/A |
| T-2 days | Communication to users | David Okafor | 1 hour | N/A |
| T-0 Day | Maintenance window starts | Michael Evans | | Rollback plan |
| T+0:00 | Application stopped on DC | Michael Evans | 5 min | Restart on DC |
| T+0:05 | Final DMS sync completed | James Patel | 30 min | Restart DMS |
| T+0:35 | DNS switched to AWS | James Patel | 5 min | DNS revert |
| T+0:40 | Smoke tests on AWS | All | 20 min | DNS revert if fail |
| T+1:00 | Go/No-Go decision | Sarah Williams | | Rollback if No-Go |
| T+1:00+ | Monitoring for 24 hours | James Patel | 24 hours | Rollback available |
| T+24h | DC instance decommissioned | Michael Evans | 1 hour | N/A (archived) |

---

## 5. AWS Migration Tools

| Tool | Purpose | Used For |
|------|---------|---------|
| AWS Application Discovery Service | Dependency mapping | Wave planning |
| AWS Database Migration Service (DMS) | Database migration | Oracle → Aurora |
| AWS Schema Conversion Tool (SCT) | Schema conversion | Oracle → PostgreSQL |
| AWS Server Migration Service (SMS) | VM migration | Rehost workloads |
| AWS DataSync | Data transfer | Large dataset migration |
| CloudEndure / MGN | Rehost at scale | Multiple EC2 migrations |

