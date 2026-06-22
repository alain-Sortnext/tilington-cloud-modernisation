# Persona: James Patel — Cloud Platform Lead
## Tilington plc Cloud Modernisation Programme

---

**Role:** Cloud Platform Lead, Tilington plc
**Reports to:** Head of Infrastructure (Michael Evans)
**Priority colour:** Coral
**Communication style:** Collaborative, technical, enthusiastic about cloud-native, prefers Slack to email

---

## Background

James joined Tilington two years ago specifically to lead the cloud journey. He has AWS Solutions Architect Professional certification and has previously worked at a fintech where he ran EKS in production for three years. He is the most cloud-experienced person on the team.

He is 31, enthusiastic, and occasionally needs reining in — he wants to build everything cloud-native immediately and sometimes skips documentation steps that Emma Clarke later requires.

He set up the initial AWS accounts and pushed the starter GitHub repo. He is your primary technical contact and the person most likely to review your pull requests.

He has strong opinions on GitOps and thinks IaC discipline is non-negotiable. He will push back on anything he considers "ClickOps."

---

## Key Priorities

1. **EKS platform quality** — he wants a platform the dev teams can actually use
2. **GitOps discipline** — everything through ArgoCD, no manual kubectl in production
3. **CI/CD security** — he was stung by a CVE incident at his last job and is serious about security scanning
4. **Terraform standards** — modules, remote state, no manual changes
5. **Cost visibility** — he checks Cost Explorer every Monday and Slacks the team if something looks wrong

---

## Inbox Messages (In-Simulation)

### Slack Message 1 — Day 1
**From:** James Patel
**To:** [Candidate]
**Channel:** #cloud-platform

Hey! Welcome. I've set you up with read access to the AWS accounts. Repo is at github.com/alain-Sortnext/tilington-cloud-modernisation.

Quick heads up on the current state:
- Terraform networking module is about 20% done. Main VPC resource is there, private subnets and NAT GWs are commented out TODOs. 
- The GitHub Actions pipeline has some bugs I deliberately left in for you to find and fix :) there are 10 of them
- The ArgoCD application.yaml is pointing at a cluster URL that doesn't exist yet — you'll need to update it once EKS is provisioned
- The cost report from January is in migration/aws_cost_report.csv — have a look. There's something in there that looks like a monitoring cost problem but I think is actually an architectural problem. See if you spot it.

Let me know if you need anything.

James

---

### Slack Message 2 — After Phase 4 Terraform
**From:** James Patel
**To:** [Candidate]
**Channel:** #cloud-platform

Quick code review notes on your Terraform PR:

✅ VPC and subnet structure looks right
✅ NAT GW HA decision — agree with your ADR reasoning
⚠️ The KMS key policy on the production data key — you're allowing the root account wildcard. For financial services this should be tighter. Let's discuss.
⚠️ The EKS security group is missing an ingress rule for the Kubernetes API from the VPN CIDR — once we have Direct Connect this will be the problem
❌ Missing outputs for private_app_subnet_ids — the EKS module needs these. Please add.

Good work overall. Merge after fixing the ❌ and discussing the ⚠️.

---

### Slack Message 3 — Phase 6, Pipeline Bug Hunt
**From:** James Patel
**To:** [Candidate]
**Channel:** #cloud-platform

Did you find all 10 bugs in the pipeline? I'll give you a hint: BUG-004 is subtle — it's not a typo. The job technically runs but produces a false-negative result. You need to understand how GitHub Actions matrix jobs and `needs:` dependencies interact to see it.

Also — the OIDC fix for BUG-005 is important. I've already had Emma's team ask why we have AWS access keys stored in GitHub secrets. That has to go before production.

---

### Email 1 — Cost Anomaly
**From:** James Patel
**To:** [Candidate]
**Subject:** January Cost Report — Something Looks Wrong

I was reviewing the January cost report and something caught my eye.

CloudWatch DataProcessing is £89.40 for the month. At first I thought it was a monitoring verbosity issue — maybe we're ingesting too many logs.

But then I noticed AWS Data Transfer Regional is £156.30. That's cross-AZ data transfer. For a cluster the size of ours that seems high.

My theory: we have something making a lot of cross-AZ calls that should be using VPC endpoints or staying within an AZ. It's architectural, not just a monitoring config problem.

Can you investigate and give me your analysis? If I'm right, fixing the architecture (VPC endpoints for S3 and DynamoDB) should bring both costs down.

James

---

### Meeting Notes — EKS Platform Design Review
**Date:** 15 February 2026
**Attendees:** James Patel, [Candidate], Michael Evans

Key points:
- Agreed: EKS 1.29 as target Kubernetes version (James: "always N-1 from latest — gives us 12 months before forced upgrade")
- Agreed: Managed node groups not self-managed — reduces ops overhead
- Agreed: Karpenter for node autoscaling (preferred over Cluster Autoscaler)
- **DISAGREEMENT**: Michael wants worker nodes in t3.xlarge (cost), James wants m5.2xlarge (performance margin). Agreed: m5.xlarge as compromise pending load test results
- Agreed: Private API server endpoint only — no public kubectl access
- Agreed: IRSA for all service accounts — no instance profiles
- Action: [Candidate] to document this decision in an ADR

---

## Stakeholder Conflicts

**With Emma Clarke (CRO):**
James thinks Emma's requirements slow down development unnecessarily. Emma thinks James skips controls. Both have legitimate points. The candidate should ensure security controls are built in — not bolted on — so this tension doesn't derail delivery.

**With Michael Evans (Head of Infrastructure):**
Generally good relationship but disagree on pace (see above) and on rehost vs refactor strategy. James's view: "Lift and shift creates more work in the long run. Better to refactor now." Michael's view: "We don't have time to refactor everything in 18 months."

---

## Technical Opinions the Candidate Should Know

- James prefers Karpenter over Cluster Autoscaler for EKS
- James uses Renovate Bot for dependency management — expects it in the pipeline
- James thinks DynamoDB PAY_PER_REQUEST is almost always right for variable-load workloads
- James has strong opinions on Helm chart structure — flat values.yaml per service, not nested
- James will ask why you made any design choice that deviates from AWS Well-Architected Framework
