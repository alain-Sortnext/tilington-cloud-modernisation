# Tilington plc — Aurora PostgreSQL Design
## STATUS: STARTER — Candidate completes in Phase 7

---

## Overview

Aurora PostgreSQL replaces Oracle Database 19c for transactional customer and account data.

**Migration target:** £1.4M/year Oracle licensing eliminated before Q2 2026 contract renewal.

Oracle instances in scope:
| Instance | Purpose | Size | Migration Strategy |
|----------|---------|------|--------------------|
| ORCL-01 | Customer accounts and profiles | 2TB | Refactor to Aurora PostgreSQL |
| ORCL-02 | Trade processing and order book | 800GB | Refactor to Aurora PostgreSQL |
| ORCL-03 | Reference data (instruments, FX rates) | 400GB | Refactor to Aurora PostgreSQL |
| ORCL-04 | Batch reporting and regulatory returns | 1.2TB | TODO: Candidate evaluates strategy |
| ORCL-05 | Legacy risk calculations | 600GB | TODO: Candidate evaluates strategy |

---

## Proposed Aurora Cluster Design (STARTER — TODO: Candidate Reviews and Completes)

### Cluster: tilington-customers-aurora

**Purpose:** Customer profiles, accounts, KYC status
**Engine:** Aurora PostgreSQL 15.4
**Instance class:** db.r6g.2xlarge (TODO: Candidate validates with sizing exercise)

```
              ┌──────────────────────────────────┐
              │   Aurora Global Cluster          │
              │   tilington-customers-aurora     │
              └──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────┴─────┐      ┌─────┴────┐      ┌──────┴───┐
   │ Writer   │      │ Reader 1 │      │ Reader 2 │
   │ AZ-A     │      │ AZ-B     │      │ AZ-C     │
   └──────────┘      └──────────┘      └──────────┘
   Primary write     Read scaling      Read scaling
```

**TODO: Candidate completes:**
- Instance class selection with sizing justification
- Parameter group configuration
- Subnet group (must use private-data subnets only)
- Security group (allow access from EKS customer-service pods only)
- Backup retention period (FCA record keeping: 7 years minimum for some data)
- Maintenance window selection

---

## Schema Design (STARTER — TODO: Candidate Extends)

### Schema: customers

```sql
-- STARTER: Core customer table
-- TODO: Candidate adds all missing columns and constraints

CREATE TABLE customers (
    customer_id     UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    -- TODO: Add: first_name, last_name, date_of_birth, national_insurance_number
    -- TODO: Add: email, phone, address fields
    -- TODO: Consider: PII encryption at column level? Or rely on KMS at-rest?
    kyc_status      VARCHAR(20) NOT NULL CHECK (kyc_status IN (???)), -- TODO: Define valid statuses
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    -- TODO: Add: soft delete? audit trail? version column?
);

-- STARTER: Account table
CREATE TABLE accounts (
    account_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id     UUID NOT NULL REFERENCES customers(customer_id),
    account_type    VARCHAR(20) NOT NULL, -- TODO: Define valid types (ISA, SIPP, GIA, etc.)
    -- TODO: Add: balance, currency, status, opened_date, closed_date
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
);

-- TODO: Candidate adds:
-- CREATE TABLE transactions (...)
-- CREATE TABLE kyc_documents (...)
-- CREATE TABLE audit_log (...)

-- TODO: Candidate adds indexes:
-- Covering index for customer lookup by email
-- Partial index for active accounts only
-- Index for kyc_status (low cardinality — consider if worth it)
```

---

## Encryption Strategy

| Layer | Mechanism | Key |
|-------|-----------|-----|
| At-rest (cluster) | AWS KMS CMK | alias/tilington-production-data |
| In-transit (app to DB) | TLS 1.2+ via SSL mode | ACM-managed |
| Column-level PII | TODO: Candidate evaluates pgcrypto vs application-layer encryption | TBD |

---

## Backup Strategy (TODO: Candidate Completes)

| Item | Current Oracle | Target Aurora | Rationale |
|------|---------------|--------------|-----------|
| Automated backup retention | 7 days | TODO | FCA requirement |
| Point-in-time recovery | Manual | Automatic (Aurora) | RTO target |
| Cross-region backup | No | TODO | FCA DR requirement |
| Snapshot before major change | Manual | TODO | Change control |
| Backup encryption | No | TODO | ISO 27001 |

---

## Access Model (TODO: Candidate Defines)

| Role | Access Level | Used By | Notes |
|------|-------------|---------|-------|
| customer_service_app | SELECT, INSERT, UPDATE on customers, accounts | customer-service pod (IRSA) | No DELETE |
| migration_admin | TODO | DMS migration task | Time-limited |
| readonly_analyst | SELECT only | Reporting | No PII columns |
| dba_admin | ALL | Break-glass only | MFA required |

---

## Oracle Migration Approach (TODO: Candidate Completes)

Migration tool recommendation: AWS Database Migration Service (DMS)

Migration phases for ORCL-01:
1. Schema conversion: AWS Schema Conversion Tool (SCT)
   - TODO: Candidate identifies Oracle-specific features to convert
   - Common issues: sequences → pg_sequences, ROWNUM → ROW_NUMBER(), packages → functions
2. Full load: DMS full load task
3. Change data capture: DMS CDC task for ongoing sync during cutover
4. Validation: Row count and checksum validation
5. Cutover: Blue/green DNS switch at maintenance window

TODO: Candidate documents specific Oracle incompatibilities found in ORCL-01 schema

