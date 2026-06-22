# ADR-001: AWS as Primary Cloud Provider

**Date:** 2026-02-01
**Status:** Accepted
**Deciders:** Sarah Williams (CTO), Emma Clarke (CRO), James Patel (Cloud Platform Lead)

---

## Context

Tilington plc must exit two on-premise datacentres by Q3 2027. The Board has approved a cloud-first strategy. A cloud provider must be selected.

Three providers were evaluated: AWS, Microsoft Azure, Google Cloud Platform.

Key constraints:
- UK data residency required (UK GDPR)
- Financial services regulatory compliance (FCA, PRA)
- Team has existing AWS familiarity (2 AWS-certified engineers)
- Integration with AWS financial services partners preferred

## Decision

**AWS is the primary cloud provider for the Tilington Cloud Modernisation Programme.**

## Rationale

- AWS eu-west-2 (London) provides UK data residency
- AWS has the most mature financial services compliance programme (ISO 27001, PCI DSS, SOC 2)
- AWS Well-Architected Framework financial services lens available
- Existing AWS skills in team reduces training cost
- AWS Partner Network includes Tilington's core banking software vendor
- Board-level familiarity with AWS pricing model

## Consequences

**Positive:**
- Single cloud strategy reduces operational complexity
- AWS Professional Services available for FCA operational resilience advisory
- AWS managed services reduce team operational burden

**Negative:**
- Vendor lock-in risk — mitigated by using open standards (Kubernetes, PostgreSQL, Terraform)
- AWS cost model requires FinOps discipline to control
- Azure AD integration requires federation setup (Tilington uses Microsoft 365)

## Alternatives Considered

- **Azure:** Rejected — strong contender but team skills gap is wider. Azure Financial Services Cloud does not yet have the same partner ecosystem as AWS in UK.
- **GCP:** Rejected — limited financial services customer evidence in UK, smaller partner network.
- **Multi-cloud:** Rejected — programme timeline and budget do not support multi-cloud complexity.

