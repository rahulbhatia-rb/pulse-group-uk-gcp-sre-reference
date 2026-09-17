terraform { required_version = ">= 1.6.0" }
variable "project_id" { type = string }
variable "approved_log_bucket" { type = string }
resource "google_logging_project_sink" "reliability_audit" {
 project = var.project_id
 name = "reliability-audit"
 destination = "storage.googleapis.com/${var.approved_log_bucket}"
 filter = "severity>=ERROR OR logName:(cloudaudit.googleapis.com)"
}
