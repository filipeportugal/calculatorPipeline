terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "2.22.3"
    }
  }
}

provider "digitalocean" {
  token = "dop_v1_ac2a8084df532fd75d615be2691955e40d40c9843b89a21f23a44638b48e0c69" # this is where the API token is set
}

resource "digitalocean_droplet" "web1" {
  image  = "ubuntu-22-04-x64"
  name   = "droplet-1"
  region = "ams3"
  size   = "s-1vcpu-1gb"
  ssh_keys = ["0f:46:3e:e5:1d:22:3a:5a:11:13:0d:c1:86:61:4a:9b"] # ssh fingerprint!!!

}