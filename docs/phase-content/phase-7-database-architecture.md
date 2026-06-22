# Phase 7 — Database Architecture for Cloud-Native Applications
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Cloud-Native Database Architecture
**Submission types:** text_editor + file_upload
**Estimated time:** 8–12 hours

---

## Context

The microservices platform is live. Now you must design the data layer — the databases that power the four microservices and the migration path from Oracle.

The starter files in `/databases/` give you a partial Aurora design and an empty DynamoDB design with TODO markers. The Oracle situation is complex: 847 stored procedures in ORCL-01, database links in ORCL-02, and the question Sarah Williams raised about the Q2 2026 Oracle renewal decision.

Emma Clarke's email makes clear that the audit trail (DynamoDB AuditTrail table) must be FCA-compliant: append-only, no TTL, 7-year retention, separate KMS key.

---

## Deliverables

### Deliverable 1 — Database Architecture Document
**File:** `/docs/database-architecture.md`

Write the master database architecture document covering:

**Section 1: Data Architecture Overview**
- Which database serves which microservice?
- Data ownership model (each microservice owns its data — no shared databases between services)
- How do services access data they don't own? (API calls, not direct DB access)

**Section 2: Database Selection Rationale**
For each database choice (Aurora PostgreSQL, DynamoDB), document:
- Why this database for this data pattern?
- What alternatives were considered?
- What are the trade-offs?

**Section 3: Tiered Approach**
- Relational tier: Aurora PostgreSQL for Customer Service and Payments Service transactional data
- Event/document tier: DynamoDB for Payments events, Notifications, Audit
- Justify why each service uses which tier

---

### Deliverable 2 — Aurora PostgreSQL Design (Complete)
**File:** `/databases/aurora-design.md` (complete the starter)

Complete ALL TODO sections:

**Cluster design:**
- Instance class selection with sizing justification (current Oracle: SRV-006 has 32 vCPU, 256GB RAM — Aurora db.r6g.2xlarge is 8 vCPU, 64GB RAM. Is this right? Size based on actual Oracle workload, not server capacity)
- Parameter group: set `shared_preload_libraries = 'pg_stat_statements'` for query performance monitoring
- Maintenance window: avoid Tuesday 2–4am (batch window per Michael Evans)
- Backup retention: justify your choice against FCA record-keeping requirements

**Schema design:** Complete the SQL for:
- `customers` table — all columns including PII fields
- `accounts` table — with account_type constraint (ISA, SIPP, GIA, CASH)
- `transactions` table — new table (not in starter)
- Indexes: at minimum, covering index on customer email lookup; partial index on active accounts

**Oracle migration specifics:**
- List the specific PL/SQL features in ORCL-01 `customer_ledger_pkg` (hint: Michael Evans told you this is the most complex package) and how you would convert them to PostgreSQL
- DMS task configuration for ORCL-01 → Aurora
- Schema Conversion Tool: which items require manual conversion?

---

### Deliverable 3 — DynamoDB Access Pattern Design (Complete)
**File:** `/databases/dynamodb-design.md` (complete the starter)

Design all 3 tables completely:

**Table 1: PaymentEvents** (starter exists — complete it)
- Resolve the hot partition problem on status GSI for PENDING payments
  - Hint: write sharding — add a shard number (0-9) to the partition key, query all shards and merge
- Billing mode decision: PAY_PER_REQUEST vs PROVISIONED with cost calculation
  - Given: 50,000 payments/day at launch. A write = ~1 WCU at 1KB. Cost comparison required.

**Table 2: NotificationDelivery** (design from scratch per TODO in starter)
- Partition key + sort key with rationale
- GSI for "all notifications for customer X, last 90 days"
- GSI for "all failed notifications today"
- TTL: 90 days
- Item schema with all attributes

**Table 3: AuditTrail** (design from scratch — FCA critical)
- Partition key + sort key design (high write throughput + queryable by entity and timestamp)
- NO TTL — explain why (FCA requirement)
- Separate KMS key: `alias/tilington-audit`
- Access model: audit-service write-only, compliance-viewer read-only (CISO, Legal, FCA auditor)
- Capacity: 500,000 events/day — PROVISIONED or PAY_PER_REQUEST? Show calculation.

---

### Deliverable 4 — Backup & Recovery Strategy
**File:** `/docs/backup-recovery-strategy.md`

For each database:

**Aurora PostgreSQL:**
- Automated backup retention period (your justified choice)
- PITR window: what is the RPO this provides?
- Cross-region backup: yes/no? (reminder: no PII in eu-west-1 — how does this affect Aurora cross-region backup?)
- Snapshot before major schema change: procedure
- Restore procedure: step-by-step for restoring from latest automated backup

**DynamoDB:**
- PITR: enable or not? Cost: $0.20/GB/month. AuditTrail table estimate?
- On-demand backup before major changes: procedure
- DynamoDB Global Tables for DR: yes/no? (reminder: AuditTrail must not replicate to eu-west-1 — why?)

**RTO/RPO targets (from FCA PS21/3):**
- Customer Service: RTO ≤ 4h, RPO ≤ 1h — does your backup design meet this? Evidence it.
- Payments Service: RTO ≤ 2h, RPO ≤ 15min — higher bar. How do you meet this?

---

### Deliverable 5 — Data Security Controls
**File:** `/docs/data-security-controls.md`

- Encryption at rest: CMK strategy (which key for which table — reference KMS design from Phase 3)
- Encryption in transit: TLS configuration for Aurora PostgreSQL (ssl mode: require or verify-full?)
- Column-level PII encryption: evaluate `pgcrypto` vs application-layer encryption — make a recommendation
- Access model: IAM policies for each service account (least privilege — Customer Service: SELECT/INSERT/UPDATE on customers and accounts, no DELETE)
- Database audit logging: PostgreSQL audit via `pgaudit` extension — configure it
- Data masking: how do you prevent developers seeing production PII in non-production?

---

## Anti-Fake Validation

Required specifics:
- Aurora instance class must be justified against ORCL-01 workload — not just picked arbitrarily
- DynamoDB PaymentEvents hot partition: must propose write sharding or another concrete solution — not just flag the problem
- AuditTrail TTL must be explicitly set to NONE with FCA justification
- Backup retention for Aurora: must be justified against FCA COBS record-keeping (some records: 5 years; some: forever)
- Cross-region backup dilemma: must acknowledge that Aurora cross-region read replicas would put PII data in eu-west-1 and propose the solution (encrypted snapshots to S3 with no-PII tagging, or DMS to non-PII DR replica)
- RTO/RPO: Payments Service 15-minute RPO must be addressed — Aurora automated backup alone does not achieve this (PITR does)

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Aurora design completeness | 25 | Instance sizing justified; schema complete; Oracle migration specifics |
| DynamoDB — all 3 tables designed | 30 | PaymentEvents hot partition solved; NotificationDelivery designed; AuditTrail FCA-compliant |
| Backup and recovery — RTO/RPO met | 20 | Payments RPO 15min achieved via PITR; cross-region PII dilemma resolved |
| Data security controls | 15 | KMS keys; TLS; pgaudit; access model; data masking |
| Database architecture document | 10 | Data ownership; selection rationale; tiered approach |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions on Aurora, DynamoDB, database design, and cloud data architecture from UK financial services employers.
>
> Q1: "How would you approach migrating an Oracle database to Aurora PostgreSQL? What tools would you use?" — [VERIFY SOURCE]
> Q2: "When would you use DynamoDB instead of Aurora PostgreSQL? What data patterns suit each?" — [VERIFY SOURCE]
> Q3: "How do you design DynamoDB for high write throughput without hot partition issues?" — [VERIFY SOURCE]
> Q4: "How do you ensure database access follows least-privilege in a microservices architecture?" — [VERIFY SOURCE]
> Q5: "How would you achieve a 15-minute RPO for a financial services database on Aurora PostgreSQL?" — [VERIFY SOURCE]

