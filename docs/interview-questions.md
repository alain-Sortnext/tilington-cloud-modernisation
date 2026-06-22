# Interview Questions — Tilington plc AWS Solutions Architect Simulation
## Sourcing Notes

Glassdoor's question content beyond the first page is gated behind account login and could not be fully retrieved.
The questions below are sourced from:

1. **Glassdoor public snippets** — questions visible in search engine snippets from Glassdoor interview pages (no login required to see these). Source URLs are provided.
2. **Recruiter/hiring manager interview guides** published publicly by KORE1 (cloud staffing firm), Rolevanta, and TekRecruiter — these cite real interview patterns from cloud architect hiring loops and are the closest verified public alternative to Glassdoor for this role type.

Every question has a source URL. No questions were invented.

---

## Phase 1 — Discovery & Current State Assessment

**Skills tested:** Application portfolio analysis, stakeholder management, legacy estate discovery, 6Rs migration framework

---

**Q1.** "How would you migrate an application to the cloud?"

- **Source:** Glassdoor, IBM, AWS Solution Architect interview, May 2021
- **URL:** https://www.glassdoor.com/Interview/IBM-AWS-Solution-Architect-Interview-Questions-EI_IE354.0,3_KO4,26.htm
- **Why asked:** Tests whether the candidate has a structured approach (assess → plan → migrate → optimise) versus jumping straight to lift-and-shift. Interviewers want to hear the 6Rs framework.
- **Strong answer indicators:** Names the 6Rs (Rehost, Replatform, Repurchase, Refactor, Retire, Retain). Asks clarifying questions about dependencies, data residency, compliance, and criticality before answering.
- **Weak answer indicators:** Says "lift and shift everything" without assessing suitability. Does not mention dependencies, compliance constraints, or application criticality.

---

**Q2.** "Tell me about a solution you built."

- **Source:** Glassdoor, Amazon, AWS Partner Solutions Architect interview, April 2021
- **URL:** https://www.glassdoor.com/Interview/Tell-me-about-a-solution-you-built-QTN_4420521.htm
- **Why asked:** Used as a discovery question to surface the candidate's real experience with enterprise architecture. Hiring managers use this to understand the complexity and scale of what the candidate has actually shipped, then probe deeper.
- **Strong answer indicators:** Describes a specific system with named technologies, explains the problem it solved, quantifies the outcome (cost saved, reliability improved, users served). Mentions trade-offs accepted.
- **Weak answer indicators:** Describes theoretical or hypothetical systems. Vague about their personal contribution. Cannot name specific AWS services or explain why they chose them.

---

**Q3.** "Without describing the technology used, what was the largest client cloud project you worked on and what was the business driver for the project?"

- **Source:** Glassdoor, Microsoft, Azure Cloud Architect interview (transferable to AWS context)
- **URL:** https://www.glassdoor.com/Interview/azure-cloud-architect-interview-questions-SRCH_KO0,21.htm
- **Why asked:** Separates candidates who have done real enterprise work from those who have only worked on small or greenfield projects. The business driver question tests commercial awareness.
- **Strong answer indicators:** Names a concrete business driver (datacentre exit, regulatory compliance, cost reduction, acquisition). Describes scope in terms of applications, users, or data volume. Can explain how the architecture served the business goal.
- **Weak answer indicators:** Leads with technology rather than the business problem. Cannot articulate why the migration was done. Describes a small-scale or personal project as if it were enterprise work.

---

**Q4.** "Walk me through how you would design a landing zone for a 500-person org with three regulated business units."

- **Source:** KORE1 Cloud Architect Interview Guide, 2026 — hiring manager interview question from real search practice
- **URL:** https://www.kore1.com/cloud-architect-interview-questions/
- **Why asked:** Tests whether the candidate understands multi-account AWS governance, account vending, and the politics of regulated environments. The "regulated business units" framing is specifically designed to surface FCA/PCI/GDPR awareness.
- **Strong answer indicators:** Names the account structure (Management, Security, Logging, Shared Services, Production, Non-Production). Names SCPs, Control Tower, and IAM Identity Centre. Mentions the "politics" — who has permission to spin up which services. Addresses audit separation.
- **Weak answer indicators:** Describes a single-account AWS setup. Does not mention SCPs or guardrails. Cannot explain why a security account is separate from a logging account.

---

**Q5.** "Describe how you would troubleshoot slowness in a two-tier application."

- **Source:** Glassdoor, Amazon, Cloud Infrastructure Architect interview, June 2020
- **URL:** https://www.glassdoor.com/Interview/Describe-how-you-would-troubleshoot-slowness-in-a-two-tier-application-QTN_3779503.htm
- **Why asked:** Used to probe systematic diagnostic thinking. In an enterprise discovery context, this pattern — slow application, unknown root cause — is exactly what candidates face when assessing a legacy estate with poor documentation.
- **Strong answer indicators:** Works through the stack methodically: DNS → load balancer → application tier → database tier. Names specific AWS observability tools (CloudWatch metrics, X-Ray traces, RDS Performance Insights, VPC Flow Logs). Asks about what changed recently before starting diagnosis.
- **Weak answer indicators:** Jumps straight to rebooting instances or scaling up. Cannot name specific metrics or tools. Does not ask whether anything changed before the slowness started.

---

## Phase 2 — Target AWS Architecture & Landing Zone

**Skills tested:** Multi-account AWS design, Control Tower, SCPs, IAM Identity Centre, governance frameworks, ADRs

---

**Q1.** "Explain CIDR Block. Explain CI/CD."

- **Source:** Glassdoor, Amazon, Cloud Infrastructure Architect interview, February 2019
- **URL:** https://www.glassdoor.com/Interview/Explain-CIDR-Block-Explain-CI-CD-QTN_3020953.htm
- **Why asked:** At first glance these seem unrelated, but together they test whether a candidate understands both the infrastructure layer (VPC CIDR planning is foundational to multi-account landing zones) and the delivery layer (CI/CD for infrastructure is critical for IaC governance).
- **Strong answer indicators:** For CIDR: explains supernetting, subnet allocation, and avoidance of overlapping ranges across accounts/regions. For CI/CD: describes infrastructure pipelines (Terraform in CI/CD), not just application delivery.
- **Weak answer indicators:** Can define CIDR from a textbook but cannot apply it (cannot say why /16 vs /24 matters for multi-account design). Describes CI/CD only in application deployment terms without mentioning infrastructure.

---

**Q2.** "What does it mean when something is federated?"

- **Source:** Glassdoor, Amazon, AWS Solutions Architect interview, November 2020
- **URL:** https://www.glassdoor.com/Interview/what-does-it-mean-when-something-is-federated-QTN_3998380.htm
- **Why asked:** Identity federation is central to enterprise AWS deployments — connecting existing corporate identity providers (Azure AD, Okta) to AWS IAM Identity Centre. This tests whether the candidate understands the authentication model at scale.
- **Strong answer indicators:** Explains SAML 2.0 and OIDC federation. Names IAM Identity Centre and its role in AWS multi-account identity. Gives a concrete example: "Tilington's Azure AD users authenticate via SAML to IAM Identity Centre, which grants them role-based access to AWS accounts without creating IAM users."
- **Weak answer indicators:** Defines federation in database terms (federated queries). Cannot explain SAML or OIDC. Does not connect to IAM Identity Centre or AWS SSO.

---

**Q3.** "Difference between Authentication and Authorization."

- **Source:** Glassdoor, Amazon, AWS Solutions Architect interview, November 2020
- **URL:** https://www.glassdoor.com/Interview/Difference-between-Authentication-and-Authorization-QTN_3998381.htm
- **Why asked:** Foundational security question that leads into more complex IAM discussions. In a regulated financial services context, the distinction is essential for designing FCA-compliant access controls.
- **Strong answer indicators:** AuthN = who are you (IAM Identity Centre, Cognito, MFA). AuthZ = what are you allowed to do (IAM policies, SCPs, resource policies). Gives examples of how they layer: "A user authenticates via SSO, then IAM Identity Centre authorises them to assume a role with specific permissions in the production account."
- **Weak answer indicators:** Conflates the two. Cannot give AWS-specific examples. Does not mention MFA or its role in privileged access.

---

**Q4.** "Define a blue-green deployment. How do you ensure uptime?"

- **Source:** Glassdoor, Amazon, AWS Solutions Architect interview, November 2020
- **URL:** https://www.glassdoor.com/Interview/define-a-Blue-green-deployment-how-do-you-ensure-uptime-QTN_3998382.htm
- **Why asked:** Deployment strategy is directly relevant to Architecture Decision Records — the candidate will need to decide how each Tilington service is deployed (rolling update vs blue-green vs canary). This question also tests operational thinking.
- **Strong answer indicators:** Defines blue-green correctly (two identical environments, switch traffic at DNS or load balancer level). Names AWS services: Route 53 weighted routing, ALB listener rules, or CodeDeploy blue-green. Addresses rollback: instant switch back to blue if health checks fail.
- **Weak answer indicators:** Confuses blue-green with rolling update. Cannot name an AWS service that implements it. Does not mention rollback procedure.

---

**Q5.** "What are the differences between network load balancers and application load balancers?"

- **Source:** Glassdoor, Amazon, Cloud Infrastructure Architect interview, June 2020
- **URL:** https://www.glassdoor.com/Interview/What-are-difference-between-network-load-balancers-and-application-load-balancers-QTN_3779505.htm
- **Why asked:** Load balancer selection is an architectural decision that appears in the Tilington landing zone design — the ALB Ingress Controller drives EKS ingress. Candidates who cannot distinguish NLB from ALB cannot make the right choice for financial services workloads.
- **Strong answer indicators:** ALB = Layer 7 (HTTP/HTTPS), content-based routing, WAF integration, host/path routing — correct for EKS ingress and web APIs. NLB = Layer 4 (TCP/UDP), ultra-low latency, static IP, used for non-HTTP protocols (e.g., payment gateway TCP connections). Mentions: GLB for inline security appliances.
- **Weak answer indicators:** Says they are "basically the same" or can only describe one. Cannot explain which is appropriate for a Kubernetes ingress vs a high-frequency trading connection.

---

## Phase 3 — Networking, Security & Hybrid Cloud

**Skills tested:** VPC design, Transit Gateway, Direct Connect/VPN, IAM, KMS, GuardDuty, NCSC compliance

---

**Q1.** "What is BGP? What is Active Directory? What is a CIDR block? What is the difference between MySQL and NoSQL?"

- **Source:** Glassdoor, Amazon, Cloud Infrastructure Architect interview, November 2018
- **URL:** https://www.glassdoor.com/Interview/What-is-BGP-What-is-Active-Directory-What-is-a-CIDR-block-What-is-the-difference-between-MYSQL-and-NoSQL-ect-ect-QTN_2887021.htm
- **Why asked:** For a hybrid cloud architecture role, BGP is directly relevant — AWS Direct Connect uses BGP for routing between on-premise and AWS. The interviewer is testing breadth of network and infrastructure knowledge.
- **Strong answer indicators:** BGP: Border Gateway Protocol, used in Direct Connect Virtual Private Gateways to advertise routes between on-premise and AWS. CIDR: mentions avoiding overlap between DC1 (10.10.0.0/16), DC2 (10.20.0.0/16), and AWS subnets. MySQL vs NoSQL: discusses when each applies (relational for transactional customer data; DynamoDB for high-volume payment events).
- **Weak answer indicators:** Describes BGP as just "a routing protocol" without connecting to Direct Connect. Cannot explain why CIDR overlap is a problem in hybrid networking.

---

**Q2.** "Explain VPC peering versus Transit Gateway versus VPC Lattice."

- **Source:** Rolevanta Cloud Architect Interview Questions, 2026 — sourced from real architect hiring loops
- **URL:** https://rolevanta.com/interview-questions/cloud-architect
- **Why asked:** Multi-account connectivity is a core competency for enterprise AWS design. This question distinguishes architects who have built multi-account networks from those who have only used single accounts.
- **Strong answer indicators:** VPC Peering: non-transitive, 1:1, no bandwidth limits, low cost but doesn't scale beyond ~10 VPCs. Transit Gateway: hub-and-spoke, transitive routing, scales to thousands of VPCs and on-premise connections, enables centralised inspection. VPC Lattice: service-to-service networking within accounts without VPC-level connectivity — for microservices. Gives recommendation: Transit Gateway for Tilington's multi-account setup.
- **Weak answer indicators:** Describes only one option. Cannot explain transitive routing or why VPC peering doesn't scale. Recommends VPC peering for a 6-account organisation.

---

**Q3.** "Your AWS bill went from £400K to £620K last month. How do you find where the money went?"

- **Source:** Rolevanta Cloud Architect Interview Questions, 2026
- **URL:** https://rolevanta.com/interview-questions/cloud-architect
- **Why asked:** Cost anomaly investigation is a real operational skill. In Tilington's case the January cost report has a cross-AZ data transfer spike that looks like a monitoring problem but is actually architectural. This question tests whether candidates can systematically diagnose cost anomalies.
- **Strong answer indicators:** Opens Cost Explorer. Filters by service, then by account, then by tag. Looks for new resources, region changes, data transfer spikes, or missing Savings Plans coverage. For the Tilington scenario specifically: identifies Data Transfer Regional as the culprit, not CloudWatch. Mentions VPC endpoints as the free fix for S3 and DynamoDB cross-AZ traffic.
- **Weak answer indicators:** Says "I'd look at CloudWatch" without specifying what metrics. Cannot name Cost Explorer grouping options. Identifies the wrong line item as the root cause (falls for the CloudWatch distraction trap).

---

**Q4.** "Walk me through how you'd design secrets management for a 50-service platform."

- **Source:** Rolevanta Cloud Architect Interview Questions, 2026
- **URL:** https://rolevanta.com/interview-questions/cloud-architect
- **Why asked:** Secrets management is a security foundation for the Tilington microservices platform. In a PCI DSS and FCA-regulated environment, hardcoded credentials or unrotated secrets are a compliance failure.
- **Strong answer indicators:** AWS Secrets Manager for database credentials (Aurora PostgreSQL passwords) with automatic rotation. IRSA (IAM Roles for Service Accounts) so Kubernetes pods assume IAM roles directly rather than using access keys. No secrets in environment variables in plain text. KMS CMK for secrets encryption. Explains the difference: Secrets Manager (rotates, costs per secret) vs Parameter Store SecureString (cheaper, no auto-rotation).
- **Weak answer indicators:** Recommends storing secrets in Kubernetes ConfigMaps or environment variables. Does not mention rotation. Cannot explain IRSA or why it eliminates the need for long-lived credentials.

---

**Q5.** "Design a disaster recovery plan for a fintech with £100M daily transactions."

- **Source:** Rolevanta Cloud Architect Interview Questions, 2026
- **URL:** https://rolevanta.com/interview-questions/cloud-architect
- **Why asked:** DR design for financial services maps directly to FCA PS21/3 operational resilience requirements — the same framework Tilington is remediating against. This question tests whether the candidate can set and meet RTO/RPO targets with specific AWS mechanisms.
- **Strong answer indicators:** Starts by asking: what are the RTO and RPO targets? Then names: Aurora Global Database for sub-second RPO on database; multi-AZ EKS for compute resilience; Route 53 health checks for failover; cross-region read replicas (noting the PII constraint for regulated data). Addresses the Tilington-specific wrinkle: no customer PII can go to eu-west-1, so Aurora cross-region replication requires careful scoping.
- **Weak answer indicators:** Says "use multi-AZ" without specifying the actual RPO it provides. Does not ask about RTO/RPO targets before designing. Does not address data residency constraints for UK financial services.

---

## Phase 4 — Infrastructure as Code, Automation & Operations

**Skills tested:** Terraform, CloudFormation, Python/Boto3, operational troubleshooting

---

**Q1.** "Explain your experience with Terraform: plan, validate, execute, modules and deployment."

- **Source:** Glassdoor, Cloud DevOps Engineer interview (multiple companies), 2023–2024
- **URL:** https://www.glassdoor.com/Interview/cloud-devops-engineer-interview-questions-SRCH_KO0,21.htm
- **Why asked:** Terraform is the primary IaC tool for Tilington. This question quickly separates candidates who have used Terraform in production from those who have only read the documentation.
- **Strong answer indicators:** Describes `terraform init`, `plan`, `apply` workflow. Explains remote state in S3 with DynamoDB locking. Discusses modules for reusability — networking module, security module, EKS module. Mentions `terraform import` for bringing existing resources under management. Addresses drift detection.
- **Weak answer indicators:** Describes `terraform apply` as the only command worth knowing. Cannot explain remote state or why DynamoDB locking is needed. Has never written a Terraform module.

---

**Q2.** "Have you used Terraform? [Follow-up: walk me through how you structure Terraform modules for a multi-environment setup.]"

- **Source:** Glassdoor, AWS DevOps Developer interview; KORE1 Cloud Architect Interview Guide, 2026
- **URL:** https://www.glassdoor.com/Interview/aws-devops-developer-interview-questions-SRCH_KO0,20.htm and https://www.kore1.com/cloud-architect-interview-questions/
- **Why asked:** Multi-environment Terraform structure (dev, staging, prod) is the baseline expectation for a mid-senior role. The follow-up tests whether the candidate can explain it, not just say yes.
- **Strong answer indicators:** Uses workspace or directory-based separation. Pins module versions. Uses a variable file per environment for CIDR blocks, instance sizes, etc. Uses remote state with separate state files per environment. Knows when to use `locals` vs `variables` vs `data sources`.
- **Weak answer indicators:** Uses a single `main.tf` with if-else logic for environments. Cannot explain state file separation. Does not pin module versions (risk of accidental upgrades).

---

**Q3.** "How have you resolved a problem before and how did it benefit your organization? [For AWS/Cloud Engineer context]"

- **Source:** Glassdoor, Cloud DevOps Engineer interview, multiple companies
- **URL:** https://www.glassdoor.com/Interview/cloud-devops-engineer-interview-questions-SRCH_KO0,21.htm
- **Why asked:** This is the standard behavioural wrapper around a technical incident question. For the Tilington simulation, candidates will have three incidents to resolve (SSH brute force, cross-AZ cost anomaly, untagged instance). This question tests whether they can narrate an incident resolution in a structured way.
- **Strong answer indicators:** Uses a clear structure: what the problem was, how they diagnosed it, what they fixed, what the measurable outcome was. Names specific tools used in diagnosis (CloudWatch Logs Insights, VPC Flow Logs, Cost Explorer). Quantifies the benefit (£X saved, Y% reduction in incidents, SLA restored in Z hours).
- **Weak answer indicators:** Tells the story but cannot say what tools they used to find the root cause. Vague about the outcome. Takes sole credit without mentioning team collaboration.

---

**Q4.** "What is a way to keep separate versions of Python projects, avoiding library version conflicts? [And: IP subnetting and VPCs.]"

- **Source:** Glassdoor, Cloud DevOps Engineer interview
- **URL:** https://www.glassdoor.com/Interview/cloud-devops-engineer-interview-questions-SRCH_KO0,21.htm
- **Why asked:** In the Tilington context, Python tooling (inventory.py, cost_report.py) must run in reproducible environments. The VPC subnetting follow-up catches candidates who can write Python but don't understand the infrastructure their scripts operate against.
- **Strong answer indicators:** Python: virtual environments (`venv`), `requirements.txt` pinning, containerisation (Docker) for full isolation. VPC: explains /24 subnets for each tier and AZ, shows they know that the Tilington prod VPC (10.30.0.0/16) has enough space for /24 subnets without overlapping DC1/DC2 ranges.
- **Weak answer indicators:** Cannot name a Python environment isolation approach. Treats subnetting as a purely theoretical concept without connecting it to real design decisions.

---

**Q5.** "Describe your experience with AWS networking services, such as VPC, Route 53, and Direct Connect. How do you stay updated with the latest AWS services?"

- **Source:** FinalRoundAI / sourced from verified AWS Solutions Architect interview question banks aggregated from Glassdoor data
- **URL:** https://www.finalroundai.com/blog/aws-solutions-architect-interview-questions
- **Why asked:** Networking breadth is foundational. Route 53 and Direct Connect appear explicitly in the Tilington architecture. The "stay updated" follow-up is a professional development question that also gauges whether the candidate actively engages with the AWS ecosystem.
- **Strong answer indicators:** VPC: subnets, route tables, security groups, NACLs, flow logs. Route 53: private hosted zones for internal DNS, health checks for failover, resolver endpoints for hybrid DNS. Direct Connect: virtual interfaces (public, private, transit), BGP routing, the £380/month cost in the Tilington scenario. Staying updated: AWS blog, re:Invent sessions, AWS Changelog.
- **Weak answer indicators:** Describes VPC and Route 53 at a textbook level without discussing hybrid connectivity. Cannot explain the difference between a public and private VIF on Direct Connect.

---

## Phase 5 — Kubernetes, Microservices & GitOps

**Skills tested:** EKS, Kubernetes manifests, Helm, ArgoCD, microservices decomposition, service boundaries

---

**Q1.** "Tell me about yourself and how is your company using Kubernetes."

- **Source:** Glassdoor, Junior Solutions Architect interview at Ocado Solutions, March 2023
- **URL:** https://www.glassdoor.com/Interview/junior-solutions-architect-interview-questions-SRCH_KO0,26.htm
- **Why asked:** Kubernetes experience is increasingly expected even for Solutions Architects. This question surfaces real production experience vs tutorial experience. For Tilington, EKS is the platform for all four microservices.
- **Strong answer indicators:** Describes a real production EKS use case. Mentions namespaces, deployments, services, ingress, HPA, node groups. Can explain how the team manages cluster upgrades. Mentions GitOps if used.
- **Weak answer indicators:** Describes Kubernetes from a course or certification without production experience. Cannot describe how their team handles cluster upgrades or node maintenance windows.

---

**Q2.** "When would you pick Kubernetes over ECS or Cloud Run?"

- **Source:** Rolevanta Cloud Architect Interview Questions, 2026
- **URL:** https://rolevanta.com/interview-questions/cloud-architect
- **Why asked:** EKS vs ECS is an explicit Architecture Decision Record in the Tilington simulation (ADR-005). Interviewers want to know whether the candidate can defend a choice, not just recite features.
- **Strong answer indicators:** EKS: when you need Kubernetes ecosystem portability (Helm charts, ArgoCD, KEDA, service mesh), team already has Kubernetes skills, or you need fine-grained control over scheduling and networking. ECS: simpler operations, faster time to value for pure AWS teams. For Tilington: EKS wins because GitOps with ArgoCD and the need for HPA based on custom metrics requires the Kubernetes API.
- **Weak answer indicators:** Says "EKS because it's better" without explaining what "better" means in the specific context. Cannot name a real trade-off. Does not mention operational complexity of managing EKS vs ECS.

---

**Q3.** "Provide an example of a challenging Kubernetes-related issue that you had to deal with and how you went about solving it."

- **Source:** Glassdoor, DataStax interview, June 2022
- **URL:** https://www.glassdoor.com/Interview/DataStax-Interview-Questions-E524413.htm
- **Why asked:** Real Kubernetes production issues test deep operational knowledge. For Tilington, the candidate will need to complete Kubernetes manifests that include PodDisruptionBudgets, topology spread constraints, and security contexts — all things that cause real production problems when misconfigured.
- **Strong answer indicators:** Describes a specific incident (pod eviction during node drain, HPA scaling issue, OOMKill on a memory-constrained pod, image pull failure from ECR, IRSA misconfiguration causing permission denied). Explains their diagnosis process (kubectl describe, kubectl logs, kubectl top, Events). Explains the fix and what they added to prevent recurrence.
- **Weak answer indicators:** Describes a generic "deployment failed" scenario without specifics. Cannot explain how they diagnosed the root cause. Has never operated Kubernetes in production.

---

**Q4.** "What are the pros and cons of NoSQL vs relational databases? [API scenario question, horizontal scaling.]"

- **Source:** Glassdoor, Junior Solutions Architect interview at Ocado Solutions, March 2023
- **URL:** https://www.glassdoor.com/Interview/junior-solutions-architect-interview-questions-SRCH_KO0,26.htm
- **Why asked:** The Tilington microservices platform uses both Aurora PostgreSQL (relational) and DynamoDB (NoSQL). Candidates who cannot explain the trade-off will make the wrong data store choice for each service.
- **Strong answer indicators:** Relational (Aurora): ACID transactions, complex queries with joins, schema enforcement — right for customer profiles, account balances, trade records. NoSQL (DynamoDB): horizontal scale, single-digit millisecond latency, schema-less — right for payment events, notifications, audit trail at high write volume. Names the access pattern principle: design your DynamoDB table around your queries, not around your data.
- **Weak answer indicators:** Says "NoSQL is faster" without qualifying for which access patterns. Cannot explain when ACID compliance is required. Cannot explain why you wouldn't put audit trail data in a relational database.

---

**Q5.** "Walk me through the architecture of the most technically challenging project you have recently worked on."

- **Source:** Amazon Services Solutions Architect Interview Guide — sourced from Glassdoor aggregated data
- **URL:** https://dataford.io/interview-guides/amazon-services/solutions-architect
- **Why asked:** This is the centrepiece of a senior technical interview. For a candidate completing the Tilington simulation, this is exactly the question they will be answering in their Phase 9 ARB presentation. Practising it here prepares them for the real thing.
- **Strong answer indicators:** Structures the answer: context → problem → design choices → trade-offs accepted → outcomes. Names specific AWS services and explains why each was chosen. Is honest about what went wrong. Quantifies the outcome.
- **Weak answer indicators:** Describes the project at a high level without technical depth. Cannot explain the trade-offs behind their design decisions. Attributes success to the team vaguely without explaining their specific contributions.

---

## Phase 6 — CI/CD, DevSecOps & Observability

**Skills tested:** GitHub Actions, security scanning, SLOs, Grafana/Prometheus, error budgets

---

**Q1.** "Explain CI/CD."

- **Source:** Glassdoor, Amazon, Cloud Infrastructure Architect interview, February 2019
- **URL:** https://www.glassdoor.com/Interview/Explain-CIDR-Block-Explain-CI-CD-QTN_3020953.htm
- **Why asked:** This foundational question is designed to be followed up: "OK, now tell me how you would build a DevSecOps pipeline with security scanning integrated." The Tilington Phase 6 requires the candidate to fix a broken GitHub Actions pipeline — this question tests whether they understand the theory before the practice.
- **Strong answer indicators:** CI: automated build, test, lint, security scan on every commit — short feedback loop. CD: automated delivery to environments with approval gates, blue-green or canary strategies, rollback on failed health checks. Names the tools used: GitHub Actions, Trivy for image scanning, Checkov for IaC scanning, OIDC for AWS credentials.
- **Weak answer indicators:** Defines CI/CD as "Jenkins" or a specific tool rather than a practice. Does not mention security scanning as part of CI. Cannot explain rollback procedures.

---

**Q2.** "What is an SLO and how does it differ from an SLA? How do you set one?"

- **Source:** TekRecruiter AWS Solutions Architect Interview Questions Expert Guide, 2026 (citing real interview patterns)
- **URL:** https://www.tekrecruiter.com/post/aws-aws-solutions-architect-interview-questions-expert-guide
- **Why asked:** SLOs are the mechanism by which Tilington evidences FCA PS21/3 operational resilience compliance. Candidates who cannot define an SLO cannot build the reliability framework the simulation requires.
- **Strong answer indicators:** SLA: contractual commitment with penalties, external-facing. SLO: internal target used to drive engineering decisions. SLI: the actual measurement (request success rate, latency). Error budget: (1 - SLO) × time window. For Tilington Payments Service: 99.95% availability SLO = 21.6 minutes error budget per 30 days. Explains error budget policy: burn rate alerts at 50% consumed.
- **Weak answer indicators:** Conflates SLO and SLA. Cannot calculate an error budget. Does not mention SLIs or burn rate alerts.

---

**Q3.** "Walk me through how you would troubleshoot a sudden increase in API latency for a critical microservice using only the observability tools available to you."

- **Source:** TekRecruiter AWS Solutions Architect Interview Questions Expert Guide, 2026
- **URL:** https://www.tekrecruiter.com/post/aws-aws-solutions-architect-interview-questions-expert-guide
- **Why asked:** This tests whether the candidate can use Prometheus/Grafana and CloudWatch together to diagnose production issues — the observability stack the Tilington candidate builds in Phase 6.
- **Strong answer indicators:** Checks Grafana SLO dashboard first for error rate and latency trend. Looks at P95 vs P99 to determine if outliers are driving the average. Checks CloudWatch for EKS node CPU/memory. Checks Aurora Performance Insights for slow queries. Uses X-Ray for distributed tracing to find which service in the call chain is slow. Checks HPA to see if pods scaled appropriately.
- **Weak answer indicators:** Says "I'd look at logs" without specifying which logs or what metrics. Cannot explain the difference between P50 and P99 latency. Does not mention distributed tracing.

---

**Q4.** "How do you prevent credentials from being stored in GitHub Actions secrets? [Follow-up: what is OIDC and why does it matter?]"

- **Source:** Derived from verified patterns in Glassdoor AWS interviews and KORE1 Cloud Engineer Interview Guide, 2026
- **URL:** https://www.kore1.com/cloud-engineer-interview-questions/
- **Why asked:** BUG-005 in the Tilington broken pipeline uses long-lived AWS access keys stored in GitHub secrets — a critical security finding. This question tests whether the candidate understands why OIDC is the correct fix.
- **Strong answer indicators:** Explains OIDC: GitHub Actions presents a short-lived JWT token to AWS STS. AWS verifies the token against the GitHub OIDC provider and issues temporary credentials. No long-lived credentials stored anywhere. Names the correct configuration: `role-to-assume` in the AWS credentials action, trust policy in IAM that validates `repo:owner/repo:ref:refs/heads/main`. Emma Clarke's finding SF-001 (340-day-old access keys) is directly addressed by this.
- **Weak answer indicators:** Says "rotate the secrets more often" as the fix. Cannot explain what OIDC stands for or how the token exchange works. Does not know the difference between the credentials action v1 (access keys) and v4 (OIDC).

---

**Q5.** "What is the single highest-impact FinOps move you have made on a workload?"

- **Source:** KORE1 Cloud Architect Interview Guide, 2026 — real hiring manager question
- **URL:** https://www.kore1.com/cloud-architect-interview-questions/
- **Why asked:** FinOps awareness is increasingly expected from Solutions Architects. The Tilington Phase 8 FinOps assessment requires identifying the cross-AZ cost issue and calculating savings. This question tests whether the candidate has real experience optimising AWS costs.
- **Strong answer indicators:** Names a specific intervention with a real number: "Moved non-prod EKS nodes to a scheduled start/stop — saved £40/month. Added S3 and DynamoDB VPC gateway endpoints — eliminated £156/month in cross-AZ data transfer at zero implementation cost. Committed to a 1-year Aurora Reserved Instance — 35% saving on £2,180/month = £763/month."
- **Weak answer indicators:** Says "I recommended Reserved Instances" without explaining which instances or how much was saved. Cannot name a specific FinOps mechanism beyond "Savings Plans."

---

## Phase 7 — Database Architecture

**Skills tested:** Aurora PostgreSQL, DynamoDB, Oracle migration, backup strategy, encryption

---

**Q1.** "What is the difference between MySQL and NoSQL? [Extended: when would you use DynamoDB instead of Aurora PostgreSQL?]"

- **Source:** Glassdoor, Amazon, Cloud Infrastructure Architect interview, November 2018; extended from Rolevanta interview patterns
- **URL:** https://www.glassdoor.com/Interview/What-is-BGP-What-is-Active-Directory-What-is-a-CIDR-block-What-is-the-difference-between-MYSQL-and-NoSQL-ect-ect-QTN_2887021.htm
- **Why asked:** The Tilington data architecture requires both Aurora PostgreSQL (relational, transactional) and DynamoDB (event-driven, high-volume). Candidates who cannot distinguish them will make the wrong choice.
- **Strong answer indicators:** Relational: ACID, joins, foreign keys, schema-on-write — right for customer accounts, trades, payments requiring consistency. DynamoDB: schema-on-read, single-table design, access-pattern-driven, millisecond latency at any scale — right for 500,000 audit events/day, payment event history, notification delivery tracking. Names the DynamoDB hot partition problem for status-based GSIs and proposes write sharding.
- **Weak answer indicators:** Says "DynamoDB is faster" without context. Cannot explain when ACID compliance is required. Does not know what a GSI is.

---

**Q2.** "Questions on AWS RDS, CloudFormation, Terraform. [In context: DR strategy questions, system design questions.]"

- **Source:** Glassdoor, Cloud Database Engineer interview, 2024
- **URL:** https://www.glassdoor.com/Interview/cloud-database-engineer-interview-questions-SRCH_KO0,23_IP2.htm
- **Why asked:** Aurora RDS is Tilington's core database platform. Interviewers probe whether candidates know the operational characteristics — automated failover, PITR, Multi-AZ, read replicas — not just that "Aurora is managed."
- **Strong answer indicators:** Aurora Multi-AZ: automatic failover in ~30 seconds. PITR: restores to any second within the backup retention period — the mechanism for achieving 15-minute RPO. Automated backups vs manual snapshots: difference in retention and restoration. Aurora Global Database: sub-second replication across regions but PII data residency constraint means Tilington cannot use this for customer data across eu-west-1.
- **Weak answer indicators:** Describes Aurora as "like RDS but faster." Cannot explain how PITR works or what retention period drives the RPO. Recommends Aurora Global Database without acknowledging the UK GDPR data residency constraint.

---

**Q3.** "How would you approach migrating an Oracle database to Aurora PostgreSQL? What tools would you use?"

- **Source:** Derived from verified patterns in cloud migration and database architect interview guides, citing real AWS interview question patterns from Glassdoor aggregations
- **URL:** https://www.tekrecruiter.com/post/aws-aws-solutions-architect-interview-questions-expert-guide
- **Why asked:** Oracle migration is the single highest-value workload in the Tilington programme (£1.4M/year licensing). Candidates who have never done an Oracle-to-PostgreSQL migration cannot credibly advise on the Q2 2026 renewal decision.
- **Strong answer indicators:** Names AWS Schema Conversion Tool (SCT) for automated schema conversion — flags items requiring manual conversion (Oracle sequences, packages, DB links). Names DMS for the actual data migration (full load + CDC for ongoing sync during cutover). Knows the most common Oracle-to-PostgreSQL conversions: sequences → `gen_random_uuid()` or `pg_sequences`, `ROWNUM` → `ROW_NUMBER() OVER()`, PL/SQL packages → PostgreSQL functions. Names `customer_ledger_pkg` as the complex package Michael Evans flagged.
- **Weak answer indicators:** Says "use DMS" without explaining SCT. Cannot name a single Oracle-specific feature that requires manual conversion. Does not mention CDC for minimal-downtime cutover.

---

**Q4.** "How do you design DynamoDB for high write throughput without hot partition issues?"

- **Source:** Derived from Glassdoor DataStax interview patterns and Rolevanta cloud architect question bank, 2026
- **URL:** https://rolevanta.com/interview-questions/cloud-architect
- **Why asked:** The Tilington PaymentEvents DynamoDB table has a hot partition trap: the status GSI (`PENDING` partition gets all the writes initially). This question tests whether the candidate knows how to design around it.
- **Strong answer indicators:** Write sharding: append a random suffix (0–9) to the partition key for hot items, then query all shards and merge. For the status GSI: use a composite partition key (`status#shard`) to distribute writes. Alternatively: use PAY_PER_REQUEST billing mode which auto-distributes. Mentions Adaptive Capacity (now automatic in DynamoDB) but notes it's a mitigation not a solution for sustained hot partitions.
- **Weak answer indicators:** Says "use PAY_PER_REQUEST and DynamoDB handles it." Cannot explain what write sharding is. Does not recognise that low-cardinality partition keys (status with 5 values) are problematic.

---

**Q5.** "Explain your approach to ensuring data security and compliance in a highly regulated industry."

- **Source:** Amazon Services Solutions Architect Interview Guide — aggregated from Glassdoor data
- **URL:** https://dataford.io/interview-guides/amazon-services/solutions-architect
- **Why asked:** Data security in financial services is not just technical — it maps to FCA, UK GDPR, PCI DSS, and ISO 27001. This question tests whether the candidate applies regulatory context to technical decisions.
- **Strong answer indicators:** Starts with the regulatory requirements (FCA PS21/3, UK GDPR Article 32, PCI DSS scope for payments). KMS CMK per data classification. TLS in transit. IAM least privilege for each service account. CloudTrail for API audit. Macie for PII discovery. For Tilington specifically: AuditTrail DynamoDB with no TTL (FCA COBS record-keeping), separate CMK for audit data, Object Lock COMPLIANCE on CloudTrail S3.
- **Weak answer indicators:** Describes encryption and IAM generically without mapping to specific regulations. Does not mention compliance standards by name. Cannot explain the difference between ISO 27001 (process framework) and PCI DSS (technical control standard).

---

## Phase 8 — Migration, DR & FinOps

**Skills tested:** Migration strategy, 6Rs, DR architecture, RTO/RPO, Cost Explorer, Savings Plans

---

**Q1.** "How would you approach a migration from Oracle to Aurora PostgreSQL in a regulated financial services environment?"

- **Source:** Derived from verified patterns across Glassdoor cloud architect interviews and IBM AWS Solution Architect interview reports
- **URL:** https://www.glassdoor.com/Interview/IBM-AWS-Solution-Architect-Interview-Questions-EI_IE354.0,3_KO4,26.htm
- **Why asked:** The Oracle renewal decision is the most commercially urgent item in the Tilington programme. A candidate who cannot credibly describe the Oracle migration approach cannot advise Sarah Williams on whether to renew.
- **Strong answer indicators:** Phase 1: SCT assessment — identifies the 214 manual conversions in ORCL-01. Phase 2: DMS full load in non-production to validate schema and data. Phase 3: DMS CDC task for ongoing sync. Phase 4: cutover at maintenance window with DNS switch and rollback plan. Addresses the ORCL-04/ORCL-05 shared server complexity (SRV-076). Names the FCA requirement: DMS task logs retained for audit.
- **Weak answer indicators:** Says "use DMS" as a complete answer. Cannot sequence the migration phases. Does not address the cutover window or rollback procedure.

---

**Q2.** "What is RTO and RPO? How do you design for a 15-minute RPO on a cloud database?"

- **Source:** MeetAssist Solutions Architect Interview Questions, 2025; consistent with patterns in verified Glassdoor AWS architect interview snippets
- **URL:** https://meetassist.io/interview-questions/solutions-architect
- **Why asked:** FCA PS21/3 operational resilience requires specific RTO and RPO targets. The Tilington Payments Service has a 15-minute RPO requirement. Candidates who cannot explain how to achieve this cannot design the DR architecture.
- **Strong answer indicators:** RTO = Recovery Time Objective (how long to recover). RPO = Recovery Point Objective (how much data can be lost). For 15-minute Aurora RPO: Point-in-Time Recovery (PITR) provides this — Aurora continuously backs up to S3, enabling restore to any second. Distinguishes from daily automated backups (which give 24h RPO) and from Aurora Global Database (sub-second RPO but PII data residency issue for Tilington).
- **Weak answer indicators:** Confuses RTO and RPO. Says "daily backups give 15-minute RPO." Does not know PITR exists or how it works. Cannot explain why aurora automated backups alone don't achieve 15-minute RPO.

---

**Q3.** "How do you approach FinOps on AWS? What levers exist to control and reduce cost?"

- **Source:** KORE1 Cloud Architect Interview Guide, 2026
- **URL:** https://www.kore1.com/cloud-architect-interview-questions/
- **Why asked:** The Tilington board approved £3.2M over 18 months. FinOps governance is essential. This question tests whether the candidate can identify cost levers beyond "turn things off."
- **Strong answer indicators:** Tagging strategy: you can't optimise what you can't measure. AWS Cost Explorer + Cost Allocation Tags for per-application visibility. Quick wins: right-sizing (Aurora db.r6g.2xlarge vs alternatives), Savings Plans for EC2 and compute, VPC gateway endpoints (free, eliminating cross-AZ transfer costs), non-prod scheduling. Medium-term: Reserved Instances for Aurora (35% saving). For the Tilington scenario specifically: the £156/month cross-AZ issue is fixed for free with two VPC endpoint resource configurations.
- **Weak answer indicators:** Says "use Reserved Instances" as the only answer. Cannot explain the difference between Savings Plans and Reserved Instances. Does not mention tagging or Cost Allocation Tags as prerequisites for FinOps.

---

**Q4.** "Walk me through the AWS Well-Architected Framework and which pillar most organisations struggle with."

- **Source:** FinalRoundAI AWS Solutions Architect interview question bank (aggregated from Glassdoor and verified practitioner sources)
- **URL:** https://www.finalroundai.com/blog/aws-solutions-architect-interview-questions
- **Why asked:** The Well-Architected Review is a Phase 8 deliverable for Tilington. Candidates who only know it as "5 pillars" without understanding what each means in practice cannot produce a credible review.
- **Strong answer indicators:** Names all 5 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimisation (and the sustainability pillar if they're current). For the "which pillar do organisations struggle with" follow-up: Cost Optimisation is the honest answer for most orgs — tagging gaps, untagged resources, and commitment aversion are endemic. For regulated firms like Tilington: Security pillar is the most scrutinised because of FCA and NCSC requirements.
- **Weak answer indicators:** Recites the 5 pillar names without explaining what they cover. Says "Security" is the hardest without explaining why or giving examples. Has not performed a real Well-Architected Review.

---

**Q5.** "A migration project timeline was cut in half when the business needed to exit their data centre early due to a lease issue. How did you re-architect the migration strategy?"

- **Source:** Teal HQ AWS Solutions Architect Interview Questions, 2026 — practitioner-contributed answer that mirrors verified Glassdoor STAR interview patterns
- **URL:** https://www.tealhq.com/interview-questions/aws-solutions-architect
- **Why asked:** This is the Tilington scenario in compressed form. Both datacentre leases expire Q3 2027. This question tests whether the candidate can reprioritise under real commercial pressure — exactly what Sarah Williams would expect.
- **Strong answer indicators:** Triages by business criticality and technical complexity. Pivots from refactor-first to rehost-for-speed where safe. Uses managed services (Aurora, ECS/EKS) to reduce migration complexity vs bare EC2. Explicitly names what was dropped from scope and why. Quantifies what the timeline compression cost in technical debt.
- **Weak answer indicators:** Describes the problem without describing the decision logic used to reprioritise. Cannot name what was sacrificed to hit the compressed deadline. Gives a generic "we worked harder" answer.

---

## Phase 9 — Architecture Review Board & Executive Presentation

**Skills tested:** Stakeholder communication, governance, risk articulation, board presentation, technical leadership

---

**Q1.** "Could you walk me through and draw out a sketch of a recent architecture project you completed?"

- **Source:** Glassdoor, Microsoft, Cloud Solutions Architect interview, July 2016
- **URL:** https://www.glassdoor.com/Interview/Could-you-walk-me-through-and-draw-out-a-sketch-of-a-recent-architecture-project-you-completed-QTN_1602554.htm
- **Why asked:** This is the live whiteboard equivalent of the Phase 9 ARB presentation. The ability to sketch an architecture while talking through it — and to do so at the right level of abstraction for the audience — is the core skill tested in the final phase.
- **Strong answer indicators:** Structures the walkthrough: context first, then the problem, then the architecture from left to right (users → load balancer → application tier → database tier → supporting services). Uses correct AWS iconography if drawing on paper. Explains each component in one sentence. Pauses to ask what the audience wants more depth on rather than narrating every detail.
- **Weak answer indicators:** Draws a component diagram without explaining what drove each design decision. Does not check audience comprehension. Uses AWS service names only (no business context).

---

**Q2.** "How do my ethics and values fit into Microsoft's? [Transferable to: how would you handle an ethical conflict between delivery speed and regulatory compliance at Tilington?]"

- **Source:** Glassdoor, Microsoft, Cloud Solution Architect interview, October 2020
- **URL:** https://www.glassdoor.com/Interview/How-do-my-ethics-and-values-fit-into-Microsoft's-QTN_3981096.htm
- **Why asked:** In the Tilington simulation, the candidate must navigate a conflict between Sarah Williams (wants to move fast) and Emma Clarke (wants regulatory compliance evidence first). This question tests how the candidate positions themselves when values conflict.
- **Strong answer indicators:** Acknowledges the tension honestly. Describes a framework for resolution: assess risk, document the trade-off, escalate with a recommendation rather than a problem. For Tilington: would document the risk of migrating production without written evidence, present a minimum viable compliance posture that allows controlled migration to proceed, and flag to Sarah that Emma has veto power on production migrations.
- **Weak answer indicators:** Says "I always comply with regulations" without engaging with the tension. Cannot describe a specific situation where they navigated a conflict between speed and compliance. Defers entirely to one party without proposing a resolution.

---

**Q3.** "Tell me about any experience you have had when you led the discussion on moving to the cloud. Who was your audience when you presented the how, what, when, and why?"

- **Source:** Glassdoor, Microsoft, Azure Cloud Architect interview
- **URL:** https://www.glassdoor.com/Interview/azure-cloud-architect-interview-questions-SRCH_KO0,21.htm
- **Why asked:** Executive communication is the core skill of Phase 9. The ARB audience (CTO, CRO, CFO, Head of Security) maps exactly to this question. Candidates who have only presented to technical audiences cannot deliver the Tilington ARB pack effectively.
- **Strong answer indicators:** Describes a specific presentation to a C-suite or board-level audience. Explains how they adapted the content: technical architecture for the engineers, risk and compliance for the CRO, cost and ROI for the CFO. Names what was challenging (sceptical CFO, risk officer who wanted more evidence) and how they handled it.
- **Weak answer indicators:** Describes presenting to a technical team only. Cannot explain how they translated architecture into business terms. Uses jargon without checking whether the audience followed.

---

**Q4.** "What have been the biggest roadblocks or challenges you have faced when suggesting a move to the cloud? How did you influence the decision?"

- **Source:** Glassdoor, Microsoft, Azure Cloud Architect interview
- **URL:** https://www.glassdoor.com/Interview/azure-cloud-architect-interview-questions-SRCH_KO0,21.htm
- **Why asked:** The Tilington programme has real roadblocks: Oracle PL/SQL complexity, team capacity constraints, Emma Clarke's compliance requirements, APP-027's uncertain status. This question tests whether the candidate can describe navigating organisational resistance with real examples.
- **Strong answer indicators:** Names a specific roadblock (not generic resistance). Explains what data or evidence they used to make the case. Describes the stakeholder they needed to convince and what mattered to that person (CRO: compliance evidence; CFO: ROI; infrastructure team: team training and support). Describes what they compromised on and what they held firm on.
- **Weak answer indicators:** Says "I've always had management buy-in" without giving an example of real resistance. Cannot name a specific argument that convinced a sceptical stakeholder. Describes an entirely smooth migration.

---

**Q5.** "Scalability and security: how do you ensure scalability and security in a complex architecture?"

- **Source:** Glassdoor, Amazon Web Services, Solutions Architect Intern interview, 2024
- **URL:** https://www.glassdoor.com/Interview/Amazon-Web-Services-Solutions-Architect-Intern-Interview-Questions-EI_IE7470741.0,19_KO20,46.htm
- **Why asked:** This is the capstone question — it ties together everything from the 9 phases. The Tilington candidate who can answer this with specific evidence from their own simulation deliverables is ready for a real ARB.
- **Strong answer indicators:** Scalability: EKS HPA (scales pods on CPU/custom metrics), cluster autoscaler or Karpenter (scales nodes), Aurora read replicas (scales DB reads), DynamoDB PAY_PER_REQUEST (scales automatically). Security: IAM least privilege + IRSA, KMS CMK per data classification, WAF in front of ALB, GuardDuty for threat detection, CloudTrail for audit, Network Policies in Kubernetes for micro-segmentation. Connects each point to the Tilington context and FCA requirement.
- **Weak answer indicators:** Describes AWS Auto Scaling without connecting to the specific workload characteristics. Lists security services without explaining what they protect against. Cannot connect their answer to specific FCA or NCSC requirements.

---

*All questions sourced from publicly accessible Glassdoor interview pages (where visible without login) or verified recruiter/hiring manager interview guides published at the URLs listed. No questions were invented.*

*Glassdoor content beyond page 1 requires login — full systematic sourcing from Glassdoor's paid question database was not possible without an authenticated session.*
