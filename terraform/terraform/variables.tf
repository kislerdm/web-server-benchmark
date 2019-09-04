variable "project" {
  type    = "string"
  default = "web-server-benchmark-1"
}

variable "region" {
  type    = "string"
  default = "europe-west4"
}

variable "ssh_key" {
  type = "map"
  default = {
    user      = "dkisler"
    file      = "/Users/dkisler/.ssh/google_compute_engine.pub"
    file_priv = "/Users/dkisler/.ssh/google_compute_engine"
  }
}

variable "startupscript_path" {
  type    = "string"
  default = "./startupscripts"
}

variable "instance" {
  type    = "list"
  default = ["node"]
}
