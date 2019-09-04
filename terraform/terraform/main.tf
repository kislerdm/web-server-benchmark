provider "google" {
  region              = "europe-west4"
  version             = "~> 2.13"
}

resource "google_compute_address" "ip" {
  project = "${var.project}"
  region  = "${var.region}"

  count = length(var.instance)
  name  = "ip-${var.instance[count.index]}"

  address_type = "EXTERNAL"
}

resource "google_compute_instance" "vm" {
  project = "${var.project}"
  zone    = "${var.region}-a"

  count = length(var.instance)
  name  = "vm-small-${var.instance[count.index]}"

  machine_type = "g1-small"

  boot_disk {
    auto_delete = true
    initialize_params {
      image = "debian-cloud/debian-9-stretch-v20190813"
      type  = "pd-ssd"
      size  = 10
    }
  }

  network_interface {
    network = "default"
    access_config {
      nat_ip = "${google_compute_address.ip[count.index].address}"
    }
  }

  metadata = {
    sshKeys = "${var.ssh_key.user}:${file(var.ssh_key.file)}"
  }

  provisioner "remote-exec" {
      
      connection {
        type        = "ssh"
        host        = "${google_compute_address.ip[count.index].address}"
        user        = "${var.ssh_key.user}"
        private_key = "${file(var.ssh_key.file_priv)}"
      }

      inline = [
        "sudo apt-get update",
        "sudo apt-get install -y git build-essential libssl-dev",
        # "sudo apt-get install -y libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev checkinstall libreadline-gplv2-dev libncursesw5-dev",
        "git clone https://github.com/wg/wrk.git wrk",
        "cd wrk",
        "make -j4",
        "sudo cp wrk /usr/local/bin",
        "cd ../",
        "rm -rf wrk",
        "git clone https://github.com/kislerdm/web-server-benchmark.git web-server-benchmark",
        "cd web-server-benchmark",
        "git config --global user.name Dmitry Kisler",
        "git config --global user.email admin@dkisler.com",
        "git checkout -b result-gcp-small-${var.instance[count.index]}",
      ]
  }
}

output "ip-out" {
  value = "${google_compute_address.ip[0].address}"
}

resource "google_compute_address" "ip-go" {
  project = "${var.project}"
  region  = "${var.region}"

  name  = "ip-go"

  address_type = "EXTERNAL"
}

resource "google_compute_instance" "vm-go" {
  project = "${var.project}"
  zone    = "${var.region}-a"

  name  = "vm-small-gp"

  machine_type = "g1-small"

  boot_disk {
    auto_delete = true
    initialize_params {
      image = "debian-cloud/debian-9-stretch-v20190813"
      type  = "pd-ssd"
      size  = 10
    }
  }

  network_interface {
    network = "default"
    access_config {
      nat_ip = "${google_compute_address.ip-go.address}"
    }
  }

  metadata = {
    sshKeys = "${var.ssh_key.user}:${file(var.ssh_key.file)}"
  }

  provisioner "remote-exec" {
      
      connection {
        type        = "ssh"
        host        = "${google_compute_address.ip-go.address}"
        user        = "${var.ssh_key.user}"
        private_key = "${file(var.ssh_key.file_priv)}"
      }

      inline = [
        "sudo echo 'deb http://ftp.de.debian.org/debian sid main' >> /etc/apt/sources.list",
        "sudo apt-get update && sudo apt-get -y upgrade",
        "sudo apt-get install -y git build-essential libssl-dev",
        "git clone https://github.com/wg/wrk.git wrk",
        "cd wrk",
        "make -j4",
        "sudo cp wrk /usr/local/bin",
        "cd ../",
        "rm -rf wrk",
        "git clone https://github.com/kislerdm/web-server-benchmark.git web-server-benchmark",
        "cd web-server-benchmark",
        "git config --global user.name Dmitry Kisler",
        "git config --global user.email admin@dkisler.com",
        "git checkout -b result-gcp-small-go}",
        "cd ../",
        "wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz",
        "tar -xvf go1.12.7.linux-amd64.tar.gz",
        "sudo mv go /usr/local",
        "echo 'PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> ~/.profile"
      ]
  }
}

output "ip-out-go" {
  value = "${google_compute_address.ip-go.address}"
}



