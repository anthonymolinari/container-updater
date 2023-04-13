terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {
  host = var.docker_host
  ssh_opts = ["-o", "StrictHostKeyChecking=no"]
}

resource "docker_image" "container_updater" {
  name = "anthonymolinari/container-updater:latest"
  keep_locally = false
}

resource "docker_container" "container_updater" {
    name = "container-updater"
    image = docker_image.container_updater.image_id

    volumes {
      container_path = "/app/config"
      host_path = var.config_path
    }
    volumes {
      container_path = "/app/logs"
      host_path = var.logs_path
    }

    env = [ "TZ=America/Los_Angeles" ]

    restart = "unless-stopped"
}