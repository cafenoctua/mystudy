provider "google" {
    credentials = file("cred.json")
    project = "bq-analysis-study"
    region = "us-central1"
}

resource "google_container_cluster" "default" {
  name     = var.name
  project = var.project
  description = "Sample GKE Cluster"
  location = var.location

  # We can't create a cluster with no node pool defined, but we want to only use
  # separately managed node pools. So we create the smallest possible default
  # node pool and immediately delete it.
  remove_default_node_pool = true
  initial_node_count       = var.initial_node_count

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }
}

resource "google_container_node_pool" "default_preemptible_nodes" {
  name       = "${var.name}-node-pool"
  project = var.project
  location   = var.location
  cluster    = google_container_cluster.default.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = var.machine_type

    metadata = {
      disable-legacy-endpoints = "true"
    }

    oauth_scopes    = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}

# resource "google_compute_firewall" "default" {
#   name = var.name
#   network = google_compute_network.default.name

#   allow {
#     protocol = "icmp"
#   }

#   allow {
#     protocol = "tcp"
#     ports = [""]
#   }

#   source_tags = ["web"]
# }

# resource "google_compute_network" "default" {
#   name = var.name
# }