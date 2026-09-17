# SRE operating model

Alert on actionable symptoms of user impact, not every infrastructure event. Define an owner, indicator, target, window, escalation path and runbook for every paging alert. Use the short/long burn example as a starting point only; calibrate values to the service and error budget.

During an incident, assign an incident lead, establish impact and a timeline, halt changes that worsen impact, and communicate an update cadence. Resolve safely before conducting a blameless review. The review should result in owned engineering work: automation, better detection, safer defaults, dependency protection or removed toil—not individual blame.

Use immutable artifacts, readiness signals and progressive rollout. Test rollback, recovery and capacity assumptions. Keep secrets and customer payloads out of logs and traces; enforce retention/access controls in the actual GCP project.
