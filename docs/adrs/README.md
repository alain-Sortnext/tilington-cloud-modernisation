# Architecture Decision Records (ADRs)
## Tilington plc Cloud Modernisation Programme

---

ADRs document significant architectural decisions, the context in which they were made, and the trade-offs accepted.

**Format:** [Nygard ADR format](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

**Status values:** Proposed | Accepted | Deprecated | Superseded

---

## ADR Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| ADR-001 | AWS as primary cloud provider | Accepted | 2026-02-01 |
| ADR-002 | Multi-account AWS organisation structure | Accepted | 2026-02-15 |
| ADR-003 | eu-west-2 as primary region | Accepted | 2026-02-15 |
| ADR-004 | Terraform as primary IaC tool | Accepted | 2026-03-01 |
| ADR-005 | EKS for container orchestration | Accepted | 2026-03-01 |
| ADR-006 | Aurora PostgreSQL to replace Oracle | Proposed | 2026-03-01 |
| ADR-007 | GitOps via ArgoCD | Proposed | 2026-03-01 |
| ADR-008 | TODO — Candidate adds in Phase 2 | | |
| ADR-009 | TODO — Candidate adds in Phase 2 | | |

---

## TODO

> Candidate: Add at minimum 3 ADRs in Phase 2. Each must follow the template below.

ADR Template:
```markdown
# ADR-NNN: [Title]

**Date:** YYYY-MM-DD  
**Status:** Proposed | Accepted | Deprecated | Superseded  
**Deciders:** [Names/roles]  

## Context
[What is the issue we are deciding about? What is the situation?]

## Decision
[What is the change we are making? What did we decide?]

## Consequences
[What becomes easier or harder? What are the trade-offs?]

## Alternatives Considered
[What else was considered and why was it rejected?]
```

