// Configure the Google Cloud provider
provider "google" {
  credentials = file("CREDENTIALS_FILE.json")
  project = "bq-analysis-study"
  region = "us-central1"
}

// Terraform plogin for creating random ids
resource "random_id" "instance_id" {
  byte_length = 8
}

// A single Compute Engine instance
resource "google_compute_instance" "name" {
  name = "flack-vm-${random_id.instance_id.hex}"
  machine_type = "f1-micro"
  zone = "us-west1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  // Make sure flask is installed on all new instances for later steps
  metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python-pip rsync; pip install flask"
  network_interface {
    network = "default"

    access_config {
      // Include this session to give the VM an external ip address
    }
  }

  metadata = {
    ssh-keys = "ldlwbru0218@gmail.com:${file("~/.ssh/gcp_ssh.pub")}"
  }

}
// A variable for extracting the external IP address of the instance
output "ip" {
  value = google_compute_instance.name.network_interface.0.access_config.0.nat_ip
}

resource "google_compute_firewall" "name" {
 name    = "flask-app-firewall"
 network = "default"

 allow {
   protocol = "tcp"
   ports    = ["5000"]
 }
}