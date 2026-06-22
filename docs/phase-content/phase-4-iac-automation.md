# Phase 4 — Infrastructure as Code, Automation & Operations
## Tilington plc Cloud Modernisation Programme

**Portfolio output:** Infrastructure Automation Platform
**Submission types:** code_panel + file_upload + text_editor
**Estimated time:** 10–15 hours

---

## Context

The architecture is approved. Now it must be built. James Patel has reviewed the starter Terraform and left you code review comments in his inbox message. The Python tools need completing. There is also a simulated operational incident for you to diagnose and resolve.

This is the most hands-on technical phase. Every deliverable requires working code pushed to GitHub.

---

## Deliverables

### Deliverable 1 — Terraform Repository (Complete)
**Files:** `/terraform/networking/`, `/terraform/security/`, `/terraform/eks/`

Complete all TODOs in the Terraform modules:

**Networking module** (building on Phase 3 work):
- Must `terraform plan` and show 0 errors (you can use `terraform plan -var="environment=non-production"`)
- Remote state backend configured in S3 (document the bucket name and DynamoDB table)
- All outputs populated (private_app_subnet_ids, private_data_subnet_ids, nat_gateway_ids)

**Security/IAM module:**
- KMS key policy must be tightened from root wildcard to specific principals
- CloudTrail S3 bucket must have Object Lock in COMPLIANCE mode (7-year retention)
- Add an S3 bucket policy that denies all puts except from CloudTrail service
- GuardDuty detector complete and enabled

**EKS module:**
- OIDC provider for IRSA
- At minimum one managed node group
- EKS addons: VPC CNI, CoreDNS, kube-proxy, aws-load-balancer-controller

Push all Terraform to GitHub. Include a `terraform plan` output screenshot as evidence.

---

### Deliverable 2 — CloudFormation Template
**File:** `/cloudformation/vpc.yaml` (complete the incomplete starter)
**File:** `/cloudformation/security.yaml` (new file)

Complete the non-production VPC CloudFormation template — all TODO sections resolved.

Create `security.yaml` to configure the Security Hub baseline for a new AWS account:
- Enable Security Hub
- Enable AWS Foundational Security Best Practices standard
- Enable CIS AWS Foundations Benchmark
- Enable GuardDuty and create a detector
- Outputs: GuardDuty detector ID, Security Hub ARN

---

### Deliverable 3 — Python AWS Inventory Tool (Complete)
**File:** `/python/inventory-tool/inventory.py`

Complete all the TODO functions:
- `get_rds_inventory()` — must identify Oracle instances (engine: oracle-ee or oracle-se2)
- `get_s3_inventory()` — must flag unencrypted buckets and public buckets as HIGH severity
- `get_eks_inventory()` — must flag public API server endpoints

Your completed tool must produce an actual CSV output when run against the Tilington AWS non-production account (or a personal free-tier account with a few test resources).

**Required submission evidence:** A screenshot of the tool running and producing output, OR the actual output CSV committed to `/python/inventory-tool/sample-output.csv`.

---

### Deliverable 4 — Python Cost Reporting Tool (Complete)
**File:** `/python/cost-reporting-tool/cost_report.py`

Complete:
- `get_cost_by_service()` — implemented and producing output
- `get_cost_by_tag()` — implemented for "Application" and "Environment" tags
- `get_savings_recommendations()` — retrieves Savings Plans recommendation

**The cross-AZ mystery:** James Patel flagged in his email that the January cost report shows CloudWatch DataProcessing at $89.40 (looks like monitoring) but AWS Data Transfer Regional at $156.30 (actually architectural). Your cost analysis must identify this and recommend VPC gateway endpoints for S3 and DynamoDB as the fix.

Include your analysis in a comment in the code and in the incident resolution report.

---

### Deliverable 5 — Incident Resolution Report
**File:** `/docs/incident-resolution-report.md`

You have been given three incidents to diagnose and resolve. Document each:

**Incident 1 — SSH Brute Force (SF-006)**
- Root cause
- Immediate containment action taken
- Long-term remediation (SF-004 fix)
- Evidence: before/after Security Hub finding status

**Incident 2 — Cross-AZ Cost Anomaly**
- Root cause (CloudWatch log data vs actual architectural issue)
- Which VPC endpoints resolve it (S3 gateway endpoint, DynamoDB gateway endpoint — both free)
- Estimated monthly saving from fix
- Evidence: architecture change documented

**Incident 3 — Untagged EC2 Instance (SF-007)**
- Instance: i-0nonprod003, cost: $98.40/month, no tags, unknown owner
- Investigation steps taken
- Resolution: identified owner (or confirmed orphaned and terminated)
- Governance fix: which SCP or AWS Config rule prevents recurrence

---

### Deliverable 6 — Operations Runbook
**File:** `/docs/operations-runbook.md`

Write an operations runbook covering:
- EKS: how to safely drain a node, roll a node group update, check cluster health
- Aurora: how to perform a manual failover, check replication lag, restore from snapshot
- Terraform: how to safely apply, how to handle state drift, what to do if `terraform destroy` is run accidentally in production
- Incident escalation: who to call at Tilington, what AWS support tier to use

---

## Anti-Fake Validation

Required evidence:
- `terraform plan` output (screenshot or text output) showing 0 errors
- Actual Python tool output (CSV or screenshot) — not mocked output
- Cost report must reference the specific January figures from the CSV (Aurora writer: $2,180.16/month; Direct Connect: $380/month; cross-AZ: $156.30/month)
- CloudTrail S3 Object Lock must be set to COMPLIANCE mode — not GOVERNANCE (explain the difference)
- The MSSQL-03 mystery from Phase 1 should appear in the inventory findings if you query the correct account

---

## Rubric

| Criterion | Marks | Indicators |
|-----------|-------|-----------|
| Terraform completeness — plans with 0 errors | 25 | All modules complete; remote state; outputs populated |
| Python inventory tool — working output | 20 | RDS/S3/EKS implemented; Oracle instances identified; flags unencrypted |
| Python cost tool — working output | 15 | Per-service breakdown; cross-AZ finding identified; savings recommendation |
| CloudFormation template completion | 15 | VPC complete; security.yaml new; valid YAML |
| Incident resolution report | 15 | All 3 incidents; root cause; fix; evidence |
| Operations runbook quality | 10 | EKS; Aurora; Terraform; escalation process |
| Total | 100 | |

---

## Interview Questions (Research Required)

> RESEARCH REQUIRED: 5 real interview questions on Terraform, IaC, Python/Boto3, and AWS operations from UK financial services or enterprise cloud employers.
>
> Q1: "How do you manage Terraform state across multiple AWS accounts?" — [VERIFY SOURCE]
> Q2: "What is the difference between Terraform import and Terraform refresh? When would you use each?" — [VERIFY SOURCE]
> Q3: "How would you write a Python script using Boto3 to identify unencrypted S3 buckets across all accounts in an AWS Organization?" — [VERIFY SOURCE]
> Q4: "Describe a time you had to troubleshoot an AWS cost spike. What was your investigation process?" — [VERIFY SOURCE]
> Q5: "How do you handle Terraform state drift — when someone makes a manual change to an AWS resource that Terraform manages?" — [VERIFY SOURCE]

