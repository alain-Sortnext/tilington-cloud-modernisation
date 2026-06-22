# Tilington plc — Cloud Modernisation Programme

> **Project Lab Simulation** | AWS Solutions Architect | Mid–Senior | UK Financial Services

---

## ⚠️ Candidate Instructions

This repository is **15–20% complete by design**. Your job across 9 phases is to complete it.

Files marked `# TODO:` or `# INCOMPLETE` need your work.  
Files marked `# STARTER` show you the pattern — extend them.  
Files with `???` placeholders require your architectural decisions.

**Do not delete starter files.** Build on them.

---

## Repository Structure

```
tilington-cloud-modernisation/
├── docs/                    # Architecture docs, ADRs, runbooks
├── architecture/            # Draw.io diagrams (upload exports here)
├── terraform/               # IaC — networking, security, IAM, EKS modules
├── cloudformation/          # CFN templates — VPC, security baseline
├── networking/              # Network design reference docs
├── security/                # Security controls, compliance mapping
├── kubernetes/              # K8s manifests — deployments, services, ingress
├── gitops/                  # ArgoCD application configs
├── ci-cd/                   # GitHub Actions pipelines
├── python/                  # Automation tools — inventory, cost reporting
├── databases/               # Aurora + DynamoDB design docs
├── migration/               # Migration strategy, wave plans, runbooks
├── observability/           # Grafana dashboards, Prometheus config
├── finops/                  # Cost dashboards, savings analysis
├── presentations/           # ARB deck, exec slides
└── submissions/             # Your phase submission evidence
```

---

## The Scenario

**Tilington plc** is a UK financial services company (asset management + retail banking services) migrating from two legacy on-premise datacentres to AWS.

- **90 servers** across London (primary) and Manchester (DR) datacentres
- **28 applications** — 6 customer-facing, 22 internal
- **Datacentre leases expire** Q3 2027 — hard deadline
- **FCA PS21/3 operational resilience** — impact tolerances enforcement in flight
- **Oracle licensing** running £1.4M/year — renewal decision due Q2 2026
- **Budget:** £3.2M over 18 months approved by Board

You are the **Lead AWS Solutions Architect** on the Cloud Modernisation Programme.

---

## Phase Overview

| Phase | Title | Key Deliverable |
|-------|-------|----------------|
| 1 | Discovery & Current State | Enterprise Discovery Pack |
| 2 | Target AWS Architecture & Landing Zone | Landing Zone Design + HLD/LLD |
| 3 | Networking, Security & Hybrid Cloud | Security & Network Architecture |
| 4 | Infrastructure as Code & Automation | Terraform + Python Toolkit |
| 5 | Kubernetes, Microservices & GitOps | Cloud-Native Microservices Platform |
| 6 | CI/CD, DevSecOps & Observability | Delivery & Reliability Platform |
| 7 | Database Architecture | Cloud-Native Database Architecture |
| 8 | Migration, DR & FinOps | Migration & FinOps Programme |
| 9 | Architecture Review Board & Exec Presentation | Executive AWS Portfolio |

---

## Getting Started

1. Clone this repo: `git clone https://github.com/alain-Sortnext/tilington-cloud-modernisation`
2. Read `/docs/company-brief.md` — understand the business context
3. Read `/docs/architecture-principles.md` — understand the design constraints
4. Open Phase 1 in Project Lab and begin your Discovery Assessment

---

*Tilington plc is a fictional company created for Project Lab. All data is simulated.*
