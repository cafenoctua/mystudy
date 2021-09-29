provider "google" {
  credentials = file("./gcp-cred.json")
  project = "bq-analysis-study"
  region = "us-central1"
}

locals {
  onprem = var.ip_list
}

resource "google_sql_database_instance" "postgres" {
  name = "digdag"
  database_version = "POSTGRES_13"
  region = "us-central1"

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      dynamic "authorized_networks" {
          for_each = local.onprem
          iterator = onprem

          content {
              name = "onprem-${onprem.key}"
              value = onprem.value
          }
      }
    }
  }
}