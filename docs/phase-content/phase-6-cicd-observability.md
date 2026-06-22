# Phase 6 — CI/CD, DevSecOps & Observability
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Enterprise Delivery & Reliability Platform
**Submission types:** code_panel + file_upload + text_editor
**Estimated time:** 10–15 hours

---

## Context

The microservices platform is deployed. Now you must build the delivery pipeline and the observability stack that lets Tilington operate it with confidence.

The broken GitHub Actions pipeline in `/.github/workflows/deploy.yml` has 10 documented bugs (BUG-001 through BUG-010). Find and fix all of them. James Patel has given you one hint in his inbox message — BUG-004 is subtle and requires understanding of how GitHub Actions `needs:` dependencies work.

The observability starters in `/observability/` give you a Prometheus scrape config and a Grafana dashboard spec — but no actual dashboards yet.

---

## Pipeline Bug Hunt

Before building anything new, fix the broken pipeline. Here are the 10 bugs — find the root cause and fix each:

| Bug ID | Description | Hint |
|--------|-------------|------|
| BUG-001 | ECR_REGISTRY env var is empty | What format is an ECR registry URI? |
| BUG-002 | docker build uses wrong context path | Where does the Dockerfile actually live? |
| BUG-003 | No Trivy image scan on built image | Where in the job order should this run? |
| BUG-004 | security-scan job never runs — find the root cause | It's not a typo. Read how `needs:` + `if:` interact. |
| BUG-005 | AWS credentials via access keys not OIDC | What is the correct actions/configure-aws-credentials@v4 for OIDC? |
| BUG-006 | IMAGE_TAG variable never defined | Where should it be set and what value should it take? |
| BUG-007 | deploy-production has no AWS credentials | Missing entire step |
| BUG-008 | No rollback step on failed deployment | kubectl rollout undo — when and how? |
| BUG-009 | No smoke test after deployment | What should a basic smoke test check? |
| BUG-010 | No notification on pipeline failure | Slack or GitHub issue — pick one and implement |

---

## Deliverables

### Deliverable 1 — Fixed GitHub Actions Pipeline
**File:** `/.github/workflows/deploy.yml` (replace the broken one)

Fixed pipeline must:
- Build Docker image with correct context path
- Run Trivy scan on built image — fail pipeline on CRITICAL CVEs
- Run Checkov scan on Terraform and Kubernetes manifests
- Push to ECR using OIDC (no long-lived credentials in secrets)
- Deploy to non-production EKS
- Require manual approval gate before production deployment
- Deploy to production EKS with rollback on failure
- Run smoke test (HTTP GET to /health/ready endpoint)
- Notify on failure (Slack webhook or GitHub issue creation)

---

### Deliverable 2 — DevSecOps Pipeline Design Document
**File:** `/docs/devsecops-pipeline.md`

Document the full pipeline design:
- Pipeline stages: what runs at each stage and why
- Security scanning strategy: what Trivy catches vs Checkov catches
- OIDC vs access keys: explain the security improvement
- Environment promotion: how code moves from commit → non-production → production
- Approval gates: who must approve production deployments at Tilington?
- Rollback procedure: at what point does automatic rollback trigger vs manual decision?

---

### Deliverable 3 — Security Scanning Evidence
**File:** `/ci-cd/security-scan-results/` (directory)

Run Trivy against a real Docker image (any Alpine or Ubuntu-based image) and commit the output:
- `trivy-scan-output.json` — full JSON output
- `trivy-scan-summary.md` — your summary: total CVEs by severity, what you would fix vs accept

Run Checkov against the Kubernetes manifests:
- `checkov-k8s-scan.txt` — Checkov output
- `checkov-remediation.md` — for each FAILED check, document: what Checkov flagged, why it matters, what you changed to fix it

---

### Deliverable 4 — Monitoring Dashboards
**Files:** `/observability/grafana/dashboards/`

Create the three required Grafana Cloud dashboards (export each as JSON):
- `service-health-overview.json` — request rate, error rate, P95 latency for all 4 services
- `reliability-slo-dashboard.json` — SLO compliance, error budget remaining, burn rate
- `eks-infrastructure-dashboard.json` — node CPU/memory, pod scheduling, HPA events

**Evidence:** Include a screenshot of at least one dashboard with real or synthetic data. Grafana Cloud free tier: https://grafana.com/products/cloud/

---

### Deliverable 5 — SLO/SLA Runbook
**File:** `/docs/reliability-runbook.md`

Define the SLO framework:

**SLO definitions** (use the specs from `/observability/grafana/dashboards/README.md`):
- For each of the 4 services: availability SLO, latency SLO (P99), error rate SLO
- Error budget calculation: if availability SLO is 99.9% on a 30-day window, how many minutes of downtime are allowed?
- Error budget policy: what happens when 50% of error budget is consumed? 100%?

**Alerting runbook:**
- Fast burn alert: what threshold triggers a page? (e.g. consuming 5% of 30-day budget in 1 hour)
- Slow burn alert: what threshold triggers a ticket? (e.g. consuming 10% of budget in 6 hours)
- Escalation: from alert → on-call engineer → Michael Evans → Sarah Williams

**FCA relevance:**
- How does this SLO framework provide evidence for FCA PS21/3 operational resilience?
- Which SLO breach would trigger a FCA notification requirement? (consult Emma Clarke's emails)

---

## Anti-Fake Validation

Required evidence:
- Show the diff between broken `deploy.yml` and fixed version — list each BUG ID fixed with the specific line(s) changed
- BUG-004 explanation: must correctly identify the root cause (hint: it involves `if: github.ref == 'refs/heads/main'` on the `security-scan` job — understand why this causes the problem)
- OIDC configuration: must show the correct `role-to-assume` format: `arn:aws:iam::ACCOUNT:role/tilington-github-actions-role`
- Trivy scan output must be a real file, not mocked
- Error budget for Payments Service (99.95% SLO over 30 days): candidates must calculate this correctly — 30 × 24 × 60 × 0.0005 = 21.6 minutes per month

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Pipeline — all 10 bugs fixed with explanations | 30 | Each bug identified with root cause; fixed code shown |
| Security scanning — Trivy and Checkov evidence | 20 | Real scan output; remediation documented |
| Grafana dashboards — created and exported | 20 | 3 dashboards with correct panels; JSON exported |
| SLO framework — calculations and policy | 20 | All 4 services; error budget calculated correctly; alert thresholds |
| DevSecOps pipeline design document | 10 | Stages; OIDC; approval gates; rollback policy |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions on GitHub Actions, DevSecOps, SLOs, and observability from UK financial services or enterprise employers.
>
> Q1: "How do you implement a DevSecOps pipeline? What security tools would you integrate and at which stages?" — [VERIFY SOURCE]
> Q2: "What is an SLO and how does it differ from an SLA? How do you set one?" — [VERIFY SOURCE]
> Q3: "Walk me through how you would investigate a spike in P99 latency in a microservices architecture." — [VERIFY SOURCE]
> Q4: "How do you prevent credentials from being stored in GitHub Actions secrets?" — [VERIFY SOURCE]
> Q5: "What is an error budget and how does it influence deployment decisions?" — [VERIFY SOURCE]

