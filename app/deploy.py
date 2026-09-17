def assess(manifest):
 containers=manifest.get("spec",{}).get("containers",[])
 if not containers: raise ValueError("containers missing")
 for c in containers:
  if not c.get("image","") or c["image"].endswith(":latest"): return "reject_mutable_image"
  if not c.get("readinessProbe"): return "reject_missing_readiness_probe"
 return "admit_progressive_rollout"
