variable "name" {
  default = "sample-cluster"
}

variable "project" {
  default = "bq-analysis-study"
}

variable "location" {
  default = "us-central1"
}

variable "initial_node_count" {
  default = 1
}

variable "machine_type" {
  default = "n1-standard-1"
}