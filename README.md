# GCP Site Reliability Engineering Reference — Pulse Group application

A small, testable SRE reference for a cloud-transformation environment: service-level indicators, burn-rate response, deployment safety and a GCP-oriented observability boundary. Prepared by Rahul H Bhatia for the Senior SRE fixed-term opportunity shared by Pulse Group. This is a portfolio project, not a Pulse/client production system.

## Reviewer guide

| Role theme | Evidence | Scope |
| --- | --- | --- |
| SLIs, SLOs and reliability standards | `app/burn.py` evaluates multi-window error-budget burn and fails invalid data closed | Reference calculation; no live telemetry/SLO target claim |
| Kubernetes and CI/CD | `app/deploy.py` rejects mutable images and unready deployments; CI runs tests | Not a cluster admission controller or client pipeline |
| GCP infrastructure | `terraform/observability.tf` declares GCP project input and a log-sink pattern | Design adaptation, not a deployed GCP environment |
| Observability / incident response | `docs/sre-operating-model.md` covers alert quality, triage, post-incident work and toil reduction | No Datadog/Grafana/Prometheus ownership is claimed |

## Run

```bash
python -m unittest discover -s tests -v
terraform -chdir=terraform init
terraform -chdir=terraform validate
```

Tests have no cloud dependency and CI does not apply Terraform. Production work requires organisation-owned SLO targets, authentication, telemetry queries, alert routing, GCP IAM/network/state design, Kubernetes policy enforcement, load tests and change control.

## Candidate alignment and eligibility

Rahul’s production background includes AWS cloud/platform engineering, Terraform/CloudFormation, Kubernetes/EKS, CI/CD/GitOps, observability, incident response, cost optimization and AWS GenAI/RAG deployment. This project does not claim production GCP experience, UK work eligibility, a Pulse/client deployment, or a specific number of years. Rahul is based in Chennai, India; eligibility for this UK-based FTC must be confirmed by the hiring organisation.

## Contact

Rahul H Bhatia · +91 9884541449 · rahulbhatia1998@gmail.com  
[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
