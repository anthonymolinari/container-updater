variable "docker_host" {
    type = string
    description = "remote host id, ssh://user@host:port"
    sensitive = true
}

variable "config_path" {
    type = string
    description = "absolute path to directory to bind"
    sensitive = false
}

variable "logs_path" {
    type = string
    description = "absolute path to directory to bind"
    sensitive = false
}   