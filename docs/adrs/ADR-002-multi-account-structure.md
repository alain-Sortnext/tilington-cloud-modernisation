# ADR-002: Multi-Account AWS Organisation Structure

**Date:** 2026-02-15
**Status:** Accepted
**Deciders:** Sarah Williams (CTO), Priya Sharma (Head of InfoSec), James Patel (Cloud Platform Lead)

---

## Context

AWS accounts must be structured to support security isolation, cost allocation, compliance, and operational governance. A single-account approach was considered but rejected.

FCA expects separation of production from non-production environments. PRA expects controls on account-level blast radius.

## Decision

**Tilington will use a multi-account AWS organisation via AWS Organizations and AWS Control Tower.**

Minimum account structure:
- Management account (root — billing and governance only, no workloads)
- Security account (GuardDuty master, Security Hub master, CloudTrail aggregation)
- Logging account (centralised CloudTrail, Config, VPC Flow Logs — immutable)
- Shared Services account (Transit Gateway, Route 53 Resolver, shared tooling)
- Production account (production workloads, customer data)
- Non-Production account (dev, test, staging)

## Rationale

- Blast radius: a compromised non-production account cannot access production data
- Cost allocation: per-account billing enables accurate cost tracking
- SCP enforcement: Service Control Policies applied at OU level
- FCA audit: separate audit log account provides tamper-resistant evidence
- AWS Well-Architected: multi-account is the recommended pattern for enterprise

## Consequences

**Positive:**
- Strong security isolation between environments
- Clear cost allocation per account
- SCP guardrails enforced at organisation level
- Audit logs isolated and protected

**Negative:**
- Additional complexity in cross-account IAM and networking
- VPC sharing or Transit Gateway required for cross-account connectivity
- More accounts to manage — mitigated by Control Tower automation

## Alternatives Considered

- **Single account with environment tags:** Rejected — no blast radius containment, FCA audit separation not achievable.
- **Two accounts (prod/non-prod):** Rejected — insufficient security/logging isolation.

