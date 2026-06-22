# Phase 5 — Kubernetes, Microservices & GitOps
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Cloud-Native Microservices Platform
**Submission types:** code_panel + file_upload + text_editor
**Estimated time:** 12–18 hours

---

## Context

The IaC platform is operational. Now you must decompose Tilington's legacy Customer Platform (APP-001, APP-016, APP-005, APP-018) into four microservices and deploy them to EKS using GitOps principles.

The starter files in `/kubernetes/` and `/gitops/` are 15–20% complete. The Helm chart in `/kubernetes/helm/tilington-services/` has values defined but no templates. The ArgoCD application points at a non-existent overlay path. James Patel's code review in Phase 4 gives you the first PR comments to address.

Your EKS cluster (provisioned in Phase 4) is the target platform.

---

## The Four Microservices

| Service | Responsibility | Data Store | FCA/PCI Scope |
|---------|---------------|-----------|---------------|
| Customer Service | Customer profiles, accounts, KYC status | Aurora PostgreSQL | FCA (PII) |
| Payments Service | Payment initiation and routing | Aurora PostgreSQL + DynamoDB PaymentEvents | PCI DSS |
| Notifications Service | Email, SMS, push notifications | DynamoDB NotificationDelivery | No |
| Audit Service | Immutable audit trail for all service actions | DynamoDB AuditTrail | FCA (audit requirement) |

---

## Deliverables

### Deliverable 1 — Microservices Architecture Diagram
**File:** `/architecture/microservices.drawio` + PNG

Show:
- The four services and their boundaries
- API calls between services (synchronous)
- Event flows (asynchronous — what events does each service emit and consume?)
- External dependencies (Aurora, DynamoDB, VocaLink, World-Check)
- ALB ingress routing rules
- Which services are in PCI scope (Payments Service must be network-isolated)

---

### Deliverable 2 — Service Boundary Document
**File:** `/docs/service-boundaries.md`

For each of the four services, document:
- **Owns:** What data entities does this service own? It is the single source of truth for these.
- **Does not own:** What data does it read from other services (API call or event)?
- **Publishes events:** What domain events does it emit?
- **Subscribes to events:** What events from other services does it consume?
- **API surface:** What endpoints does it expose? (REST verb + path + description)

---

### Deliverable 3 — API Design Document
**File:** `/docs/api-design.md`

Design the REST API for the Customer Service (minimum — others optional for distinction):

For each endpoint:
- Method + Path
- Request body (JSON schema)
- Response body (JSON schema)
- HTTP status codes (success and error cases)
- Authentication mechanism (JWT bearer token validated via IAM or third-party)
- Rate limiting policy
- PII fields flagged (for GDPR data minimisation)

Minimum endpoints for Customer Service:
- GET /api/v1/customers/{customerId}
- POST /api/v1/customers
- PUT /api/v1/customers/{customerId}
- GET /api/v1/customers/{customerId}/accounts
- GET /api/v1/customers/{customerId}/kyc-status

---

### Deliverable 4 — Kubernetes Manifests (Complete)
**Files:** `/kubernetes/`

Complete the incomplete starter files and add all missing services:

For each of the 4 microservices, create:
- `deployment.yaml` — complete with: correct image URI format, resource limits, liveness/readiness probes, security context (non-root, read-only filesystem), topology spread across AZs
- `service.yaml` — ClusterIP
- `hpa.yaml` — HorizontalPodAutoscaler (minReplicas, maxReplicas, CPU target)
- `pdb.yaml` — PodDisruptionBudget (minAvailable: 2 for production services)
- `serviceaccount.yaml` — with IRSA annotation (eks.amazonaws.com/role-arn)

Complete the ingress.yaml:
- Add ACM certificate ARN (use a placeholder format: `arn:aws:acm:eu-west-2:ACCOUNT:certificate/UUID`)
- Add WAF ACL ARN
- HTTP to HTTPS redirect
- All 4 service routes

---

### Deliverable 5 — Helm Chart (Complete)
**Files:** `/kubernetes/helm/tilington-services/templates/`

Create actual Helm templates (the values.yaml is done — create the templates that use it):
- `templates/deployment.yaml` — templated deployment using `.Values.customerService.*`
- `templates/service.yaml`
- `templates/hpa.yaml`
- `templates/ingress.yaml`
- `templates/serviceaccount.yaml`
- `templates/pdb.yaml`

The Helm chart must `helm template .` without errors.

---

### Deliverable 6 — ArgoCD GitOps Configuration (Complete)
**Files:** `/gitops/`

Complete the ArgoCD setup:
- Fix `application.yaml` — set a real cluster URL format and correct overlay path
- Create `/gitops/overlays/production/kustomization.yaml` — Kustomize overlay for production
- Create `/gitops/overlays/non-production/kustomization.yaml` — Kustomize overlay for non-production (lower replica counts, smaller resource limits)
- Create an ArgoCD ApplicationSet (`/gitops/argocd/applicationset.yaml`) that templates an Application for all 4 microservices

---

### Deliverable 7 — EKS Platform Design Document
**File:** `/docs/eks-platform-design.md`

Document the EKS platform architecture:
- Cluster version and upgrade strategy
- Node group design (instance type, min/max/desired, AZ spread)
- Karpenter vs Cluster Autoscaler decision (with ADR reference)
- Storage: EBS CSI driver configuration, default storage class
- Networking: VPC CNI, Calico, or other CNI decision
- Ingress: AWS Load Balancer Controller — how it creates ALBs from Ingress objects
- Registry: ECR repository structure and image tagging strategy

---

## Anti-Fake Validation

Required specifics:
- Kubernetes manifests must have real resource limits (not `requests: cpu: 100m limits: cpu: unlimited`)
- Security context: `runAsNonRoot: true`, `readOnlyRootFilesystem: true`, `allowPrivilegeEscalation: false` — these must appear in every deployment
- Topology spread constraints must reference `topology.kubernetes.io/zone`
- PCI DSS: Payments Service must be in a separate namespace or have NetworkPolicy restricting inbound to only ALB and Customer Service
- Helm `helm template .` must produce valid YAML (test this and include evidence)
- ArgoCD ApplicationSet must iterate over actual service names from your 4 microservices
- IRSA: every serviceaccount must have the eks.amazonaws.com/role-arn annotation

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Microservices boundary design | 20 | 4 services clearly bounded; events documented; no inappropriate coupling |
| Kubernetes manifests completeness | 25 | All 4 services; correct security context; HPA; PDB; IRSA |
| Helm chart — templates produce valid YAML | 20 | All 6 template types; helm template runs without errors |
| GitOps — ArgoCD ApplicationSet | 15 | ApplicationSet covers all 4 services; overlays for prod/nonprod |
| API design quality | 10 | Customer Service API complete; PII flagged; status codes correct |
| EKS platform design document | 10 | Autoscaling; storage; networking; upgrade strategy |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions on Kubernetes, EKS, GitOps, and microservices from UK financial services or enterprise cloud employers.
>
> Q1: "How do you ensure zero-downtime deployments in Kubernetes?" — [VERIFY SOURCE]
> Q2: "Explain the difference between a Deployment and a StatefulSet. When would you use each?" — [VERIFY SOURCE]
> Q3: "How does ArgoCD implement GitOps? What happens when someone makes a manual change to the cluster?" — [VERIFY SOURCE]
> Q4: "How do you design microservice boundaries? What principles do you follow?" — [VERIFY SOURCE]
> Q5: "How would you secure a Kubernetes cluster in a PCI DSS environment?" — [VERIFY SOURCE]

