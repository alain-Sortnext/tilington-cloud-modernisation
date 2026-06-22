# Tilington plc — Grafana Dashboards
## STATUS: STARTER — Candidate creates dashboards in Phase 6

---

## Required Dashboards

Candidate must create the following dashboards in Grafana Cloud (free tier).
Export each dashboard as JSON and save here.

### Dashboard 1 — Service Health Overview
**Purpose:** Single-pane view of all 4 microservices health

Must include:
- [ ] Request rate per service (req/sec)
- [ ] Error rate per service (%) — RED line at 1%
- [ ] P50, P95, P99 latency per service
- [ ] Pod count per service (should match desired replicas)
- [ ] Overall health status traffic light (Green/Amber/Red)

File: `service-health-overview.json`

### Dashboard 2 — Reliability & SLO Dashboard
**Purpose:** Track SLO compliance for FCA operational resilience evidence

Must include:
- [ ] Customer Service availability SLO (target: 99.9%)
- [ ] Payments Service availability SLO (target: 99.95% — PCI in scope)
- [ ] Current error budget remaining (%)
- [ ] Error budget burn rate (fast burn alert threshold)
- [ ] Latency SLO compliance

File: `reliability-slo-dashboard.json`

### Dashboard 3 — Infrastructure & EKS Dashboard
**Purpose:** EKS cluster and node health

Must include:
- [ ] Node CPU and memory utilisation
- [ ] Pod scheduling status
- [ ] HPA scaling events
- [ ] PVC storage utilisation
- [ ] Network I/O per node

File: `eks-infrastructure-dashboard.json`

---

## SLO Definitions (Candidate Implements)

| Service | Availability SLO | Latency SLO (P99) | Error Rate SLO | Window |
|---------|----------------|-------------------|----------------|--------|
| Customer Service | 99.9% | < 500ms | < 0.1% | 30-day rolling |
| Payments Service | 99.95% | < 250ms | < 0.05% | 30-day rolling |
| Notifications Service | 99.5% | < 2000ms | < 0.5% | 30-day rolling |
| Audit Service | 99.9% | < 1000ms | < 0.1% | 30-day rolling |

---

## TODO

1. Sign up for Grafana Cloud free tier: https://grafana.com/products/cloud/
2. Connect your Prometheus data source
3. Import the starter dashboard (link below)
4. Complete the required panels
5. Export dashboard JSON and save to this directory
6. Share your dashboard URL in your Phase 6 submission

Grafana Cloud free tier: https://grafana.com/products/cloud/
Prometheus remote_write config for Grafana Cloud: Add to observability/prometheus/prometheus.yml

