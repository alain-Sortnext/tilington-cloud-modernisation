# Tilington plc — DynamoDB Design
## STATUS: STARTER — Candidate completes in Phase 7

---

## Overview

DynamoDB is used for high-volume, low-latency data that does not require relational joins:
- Payment events and transaction audit trail
- Notification delivery status and preferences
- Session tokens and temporary state
- API rate limiting counters

**Rationale:** Aurora PostgreSQL is ill-suited for high-volume append-only event data.
DynamoDB provides single-digit millisecond reads at scale without database connection overhead.

---

## Tables (STARTER — TODO: Candidate Completes All)

### Table 1: PaymentEvents

**Access pattern:** Write-heavy, read by payment ID and customer ID

| Attribute | Type | Notes |
|-----------|------|-------|
| payment_id (PK) | String (UUID) | Partition key |
| created_at (SK) | String (ISO8601) | Sort key — enables range queries |
| customer_id | String | GSI partition key |
| account_id | String | GSI |
| amount | Number | In pence to avoid decimal issues |
| currency | String | ISO 4217 (GBP, EUR, USD) |
| status | String | PENDING, PROCESSING, COMPLETED, FAILED, REVERSED |
| payment_method | String | FASTER_PAYMENTS, CHAPS, SEPA, CARD |
| metadata | Map | Provider reference, correlation IDs |
| ttl | Number | TTL timestamp — TODO: Candidate sets appropriate retention |

**Global Secondary Indexes:**
```
GSI-1: customer_id (PK) + created_at (SK)
  Query: "Get all payments for customer X in date range"
  
GSI-2: status (PK) + created_at (SK)
  Query: "Get all PENDING payments (for reconciliation)"
  Caution: status is low-cardinality — hot partition risk for PENDING
  TODO: Candidate proposes solution to the hot partition problem
```

**Billing mode:** TODO — Candidate chooses: PAY_PER_REQUEST vs PROVISIONED
Justify with expected throughput estimate.

---

### Table 2: NotificationDelivery

TODO: Candidate designs this table.

Requirements:
- Track delivery status for each notification (email, SMS, push)
- Support query: "All notifications for customer X, last 90 days"
- Support query: "All failed notifications today" (for retry)
- TTL: 90 days (notifications older than 90 days purged)

Design must include:
- [ ] Partition key and sort key selection with rationale
- [ ] At least one GSI with query pattern documented
- [ ] Attribute list with types
- [ ] TTL attribute

---

### Table 3: AuditTrail

TODO: Candidate designs this table.

Requirements:
- Append-only — never updated, never deleted (FCA audit requirement)
- Track: who did what, to which resource, when, from which IP
- Support query: "All audit events for customer X, last 12 months"
- Support query: "All events by user Y, last 7 days"
- Retention: 7 years (FCA SYSC 9.1 record-keeping)
- Must be encrypted with dedicated KMS key

**FCA Implication:** TTL must NOT be set on this table. All records retained permanently.

Design must include:
- [ ] Partition key and sort key selection
- [ ] Entity model (what entities are audited)
- [ ] Event schema
- [ ] Access controls (who can read audit data — CISO, Legal, Regulators only)

---

## Capacity Planning (TODO: Candidate Completes)

Estimated volumes:
- Payment events: ~50,000/day at launch, scaling to ~200,000/day by Year 2
- Notifications: ~180,000/day (email + SMS + push across 180,000 customers)
- Audit events: ~500,000/day (all API calls audited)

TODO:
1. Calculate required RCU/WCU for PROVISIONED mode
2. Compare cost: PROVISIONED vs PAY_PER_REQUEST at these volumes
3. Recommend billing mode with cost estimate

---

## Encryption and Security

| Table | KMS Key | Access Roles |
|-------|---------|-------------|
| PaymentEvents | alias/tilington-production-data | payments-service (write), reconciliation-lambda (read) |
| NotificationDelivery | alias/tilington-production-data | notifications-service (write/read) |
| AuditTrail | alias/tilington-audit (separate key) | audit-service (write only), compliance-viewer (read only) |

TODO: Candidate defines IAM policy for each access role — principle of least privilege

