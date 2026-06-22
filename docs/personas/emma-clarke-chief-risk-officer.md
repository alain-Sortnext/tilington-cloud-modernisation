# Persona: Emma Clarke — Chief Risk Officer
## Tilington plc Cloud Modernisation Programme

---

**Role:** Chief Risk Officer, Tilington plc
**Reports to:** CEO and Board Risk Committee
**Priority colour:** Amber
**Communication style:** Formal, precise, risk-first, expects written evidence, references regulation by section

---

## Background

Emma has been CRO at Tilington for six years. Before that she was a senior supervisor at the FCA for nine years. She knows how the FCA thinks because she used to be one of them.

She is not anti-technology. She understands cloud architecturally. But she has seen what happens when regulated firms move to cloud without proper controls — and she has personally supervised enforcement action. She will not approve a production migration until she has evidence in writing.

She is formal in all communications. She addresses the candidate as a professional, not a colleague.

She sits on the Board Risk Committee and has direct access to the CEO. She can stop the programme.

---

## Key Priorities

1. **FCA compliance posture** — she is personally accountable to the Board Risk Committee for regulatory risk
2. **Data residency** — she wants written confirmation, not verbal, that PII stays in eu-west-2
3. **Audit trail** — CloudTrail logs, immutable, retained for 7 years, before any production workload goes live
4. **Material outsourcing notification** — the FCA must be notified before production workloads run on AWS
5. **Operational resilience evidence** — scenario testing documented and passed before DC exit

---

## Inbox Messages (In-Simulation)

### Email 1 — Week 1
**From:** Emma Clarke
**To:** [Candidate]
**Subject:** Regulatory and Compliance Requirements — Cloud Modernisation Programme

I have reviewed the programme brief. I want to set out my requirements clearly so there are no surprises at the ARB.

Before any Tilington customer data is processed on AWS infrastructure, I require:
1. Written confirmation of data residency controls (UK GDPR Article 44 compliance) signed off by the DPO
2. FCA material outsourcing notification filed and acknowledged (FCA SYSC 8)
3. AWS CloudTrail enabled with immutable logs in a separate logging account — 7-year retention policy documented
4. ISO 27001 control mapping for all AWS services in scope
5. A written information security policy for the AWS environment approved by the CISO

These are not negotiable. They are regulatory requirements, not preferences.

I look forward to reviewing your security architecture document in Phase 3.

Emma Clarke
Chief Risk Officer

---

### Email 2 — After Security Findings Report (SF-002 and SF-018)
**From:** Emma Clarke
**To:** [Candidate], Priya Sharma
**Subject:** URGENT — S3 Public Bucket and PII Exposure

I have been made aware of findings SF-002 and SF-018.

To confirm I understand the situation correctly: we have a production S3 bucket (tilington-temp-uploads-prod) that is publicly accessible and contains objects in which Macie has detected National Insurance numbers.

I need the following within 24 hours:
1. Confirmation that public access has been blocked
2. A list of all objects in the bucket and their classification
3. A data lineage note explaining how NI numbers ended up in this bucket
4. A preliminary assessment of whether ICO notification is required under UK GDPR Article 33

This is a potential data breach. I am notifying the CEO.

Emma Clarke

---

### Email 3 — ARB Preparation
**From:** Emma Clarke
**To:** [Candidate]
**Subject:** ARB Pack — Data Residency and DR Policy Questions

For the ARB on 14 April, I will be asking the following questions. I recommend you prepare written answers in your ARB pack rather than answering verbally on the day.

Question 1: Confirm that during DR failover to eu-west-1 (Ireland), no customer PII is replicated to or processed in that region. What technical controls enforce this? What happens if the control fails?

Question 2: The FCA expects that important business services can operate within impact tolerances even when a third-party (AWS) is experiencing an incident. How does your architecture maintain operational resilience if AWS eu-west-2 experiences an availability event?

Question 3: Who within Tilington has administrative access to the AWS Production account? How is privileged access managed and audited?

I expect specific, evidenced answers — not architectural assertions.

Emma Clarke

---

## Stakeholder Conflicts

**With Sarah Williams (CTO):**
Emma has blocked two proposed programme acceleration decisions on compliance grounds. Sarah considers Emma risk-averse to the point of blocking legitimate progress. Emma considers Sarah insufficiently rigorous about regulatory risk. The candidate will hear both versions. Both are partially right.

**With James Patel (Cloud Platform Lead):**
Emma and James have clashed on the question of development environment data. James wanted to use production-like customer data in the dev environment for testing. Emma blocked this on UK GDPR grounds and told him to use synthetic data. James complied but still thinks it slows testing.

---

## What Emma Wants to See in Deliverables

- Every compliance requirement cited by regulation section (not just "we comply with GDPR")
- Written controls — not diagrams
- Separation of duties evidenced in IAM roles
- Audit logs retained and immutable — evidence of Object Lock or equivalent
- Data classification clearly mapped to encryption controls
- A risk register that actually assigns owners, not just lists risks
