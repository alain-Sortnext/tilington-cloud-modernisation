# Phase 8 — Migration, Disaster Recovery & FinOps
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Cloud Migration, DR & FinOps Programme
**Submission types:** text_editor + file_upload
**Estimated time:** 10–15 hours

---

## Context

The platform is built and the databases are designed. Now you must plan the migration and validate cost and resilience.

Sarah Williams is waiting for your Oracle renewal recommendation — the Q2 2026 deadline is approaching. The January cost report shows the programme is on budget but James Patel has spotted the cross-AZ architectural issue. Michael Evans has warned you about Oracle PL/SQL complexity and team capacity constraints.

The migration-wave-candidates.csv gives you the sequencing logic — but you must validate it, extend it, and present it in a format the Board can understand.

---

## Deliverables

### Deliverable 1 — Migration Strategy (Complete)
**File:** `/migration/migration-strategy.md` (extend the starter)

Complete ALL TODO sections:

**6Rs application:** For every app that still has "???" in the wave candidates CSV, make a definitive recommendation. Justify each one.

**Wave plan:** Fully define all 5 waves with:
- Specific applications assigned to each wave
- Rationale for sequencing (dependencies — APP-012 authentication must move before ALL customer-facing apps)
- Entry criteria for each wave
- Exit criteria for each wave (what must be true before the next wave starts)

**Oracle renewal recommendation for Sarah Williams:**
This is a board-level decision. Structure it as a one-page recommendation:
- Renew (£1.4M/year × 3 years = £4.2M): what risk does this accept?
- Do not renew (migrate 3 of 5 Oracle instances before Q2 2026): is this technically achievable given Michael Evans's PL/SQL complexity warning?
- Your recommendation with explicit risk acknowledgement
- Decision must reference the actual Oracle instances (ORCL-01, -02, -03 for renewal deadline; ORCL-04, -05 possible later)

---

### Deliverable 2 — Migration Wave Plan
**File:** `/migration/migration-waves.xlsx` (or .csv)

Create a detailed migration wave plan spreadsheet with:
- Wave number, app ID, app name, 6R strategy, complexity, owner
- Estimated start date, estimated cutover date
- Pre-migration tasks (minimum 3 per app)
- Cutover window (hours)
- Rollback procedure
- Success criteria
- Status: Not Started / In Progress / Complete

The plan must show the full 18-month programme from March 2026 to Q3 2027.

---

### Deliverable 3 — Disaster Recovery Architecture
**File:** `/architecture/dr.drawio` + PNG

Design and diagram the DR architecture:
- Primary: eu-west-2 (London) — production
- DR: eu-west-1 (Ireland) — no customer PII

Show:
- Aurora: active/standby replica strategy (remembering the PII constraint in eu-west-1)
- DynamoDB: AuditTrail must NOT replicate to eu-west-1 (FCA audit data must stay in UK)
- EKS: what runs in eu-west-1? Is it a warm standby or cold standby?
- Route 53 health checks and failover routing
- RTO/RPO by service tier

---

### Deliverable 4 — RTO/RPO Matrix
**File:** `/docs/rto-rpo-matrix.md`

| Service | FCA RTO Requirement | Achieved RTO | FCA RPO Requirement | Achieved RPO | Architecture Mechanism | Gap? |
|---------|--------------------|-----------| -------------------|--------------|------------------------|------|
| Customer Service | ≤ 4h | ? | ≤ 1h | ? | ? | ? |
| Payments Service | ≤ 2h | ? | ≤ 15min | ? | ? | ? |
| Notifications Service | ≤ 8h | ? | ≤ 4h | ? | ? | ? |
| Audit Service | ≤ 4h | ? | ≤ 1h | ? | ? | ? |

Fill in each cell and evidence each claim with the specific AWS mechanism. If you cannot meet the FCA requirement, document the gap and proposed remediation.

---

### Deliverable 5 — FinOps Assessment
**File:** `/finops/finops-assessment.md`

Analyse the January 2026 cost report (`/migration/aws_cost_report.csv`) and produce:

**Section 1: Current Spend Analysis**
- Total January AWS spend: calculate from the CSV (sum all blended_cost_usd)
- Spend by service: top 5 services by cost
- Spend by account: Production vs Non-Production vs Security vs Logging
- Spend by tag: by Application tag (flag untagged spend)
- Monthly run rate vs £56,667/month budget (convert at current GBP/USD)

**Section 2: Key Findings**
You must identify these specific findings from the data:
1. Aurora writer db.r6g.2xlarge at $2,180.16/month — is this right-sized? (Compare to SRV-006: 32 vCPU, 256GB RAM; db.r6g.2xlarge is 8 vCPU, 64GB. Downsizing risk vs cost. Make a recommendation.)
2. Direct Connect at $380/month — cost justified? (Compare to: business case assumed £680k/year AWS infra. Direct Connect is ~£300/month = £3,600/year — small %)
3. Non-prod EKS nodes running 24/7 — two nodes at $28.08/month each. Saving if turned off nights/weekends: $28.08 × 2 × (5/7) = ~$40/month. Document the recommendation.
4. Untagged instance (i-0nonprod003) at $98.40/month — governance issue and cost visibility gap
5. Cross-AZ data transfer $156.30/month — root cause: S3 and DynamoDB API calls crossing AZs. Fix: VPC gateway endpoints (free). Annual saving: $156.30 × 12 = $1,875.60

**Section 3: Savings Recommendations**
- Quick wins (implementable in <1 week): VPC endpoints, non-prod scheduling, tagging enforcement
- Medium-term (1-3 months): Savings Plans evaluation (EC2 and EKS on-demand patterns)
- Long-term: Reserved Instances for Aurora (1-year commitment saves ~35%)

---

### Deliverable 6 — AWS Well-Architected Assessment
**File:** `/docs/well-architected-review.md`

Conduct a self-assessment against the 5 pillars:

| Pillar | Key Risks Found | Severity | Remediation |
|--------|----------------|---------|-------------|
| Operational Excellence | ? | ? | ? |
| Security | ? | ? | ? |
| Reliability | ? | ? | ? |
| Performance Efficiency | ? | ? | ? |
| Cost Optimisation | ? | ? | ? |

Minimum 2 risks per pillar. Use evidence from the security findings CSV and cost report.

---

## Anti-Fake Validation

Required specifics:
- January total spend must be calculated from the CSV (sum of blended_cost_usd — do not estimate)
- Non-prod scheduling saving must use the actual node costs from the CSV ($28.08/month each)
- Cross-AZ saving must cite the $156.30/month figure and identify S3/DynamoDB gateway endpoints as the free fix
- Aurora sizing discussion must reference SRV-006 (32 vCPU, 256GB) vs db.r6g.2xlarge (8 vCPU, 64GB)
- Oracle renewal recommendation must name ORCL-01, ORCL-02, ORCL-03 as the Q2 2026 candidates
- AuditTrail DynamoDB must not be in DR replication plan — FCA audit data UK residency
- RTO/RPO: Payments Service 15min RPO mechanism must be specifically named (Aurora PITR, not just "backups")

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Migration strategy completeness — all 28 apps | 20 | All waves defined; sequencing justified; Oracle recommendation present |
| FinOps analysis — CSV-driven findings | 25 | All 5 specific findings identified; savings quantified; budget vs actual |
| DR architecture | 20 | eu-west-1 design; PII constraint addressed; RTO/RPO by tier |
| RTO/RPO matrix — all 4 services evidenced | 15 | FCA requirements met or gap documented; mechanisms named |
| Well-Architected review | 10 | 5 pillars; 2+ risks each; evidence-based |
| Wave plan spreadsheet completeness | 10 | All apps; dates; pre-migration tasks; rollback |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions on cloud migration, FinOps, DR design, and Well-Architected from UK financial services employers.
>
> Q1: "How would you approach a migration from Oracle to Aurora PostgreSQL in a regulated financial services environment?" — [VERIFY SOURCE]
> Q2: "What is RTO and RPO? How do you design for a 15-minute RPO on a cloud database?" — [VERIFY SOURCE]
> Q3: "How do you approach FinOps on AWS? What levers exist to control and reduce cost?" — [VERIFY SOURCE]
> Q4: "Walk me through the AWS Well-Architected Framework. Which pillar do you find most organisations struggle with?" — [VERIFY SOURCE]
> Q5: "How would you present a cloud migration business case to a CFO?" — [VERIFY SOURCE]

