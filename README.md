# Container Updater
A python script that uses portainer webhooks to update containers.

![docker pulls](https://img.shields.io/docker/pulls/anthonymolinari/container-updater?style=for-the-badge)

## Supports Version Checks
- servarr applications: sonarr, radarr, prowlarr, lidarr, etc.
- coming soon plex, jellyfin, tautulli

## example configuration
` ./config/config.yml`
```yaml
schedule: "*/5 * * * *" # check for updates every 5 minutes

portainer: 
  url: "http://portainer.lan"

containers:

  - name: "sonarr"
    portainer:
      webhook: ""
    container:
      isServarr: true
      apiVer: "v3"
      url: "http://sonarr.lan"
      apiKey: "sonarrapikey"

  - name: "radarr"
    portainer:
      webhook: ""
    container:
      isServarr: true
      apiVer: "v3"
      url: "http://radarr.lan"
      apiKey: "radarrapikey"

  - name: "prowlarr"
    portainer:
      webhook: ""
    container:
      isServarr: true
      apiVer: "v1"
      url: "http://prowlarr.lan"
      apiKey: "prowlarrapikey"
      
notifications:

  discord:
    webhook: "https://discord.com/api/webhooks/"


misc:
  clean: false # use portainer api to remove 'unused images'
  
```
## Run Command
```shell
docker run -d \
  -v /path/to/config/:/app/config/ \
  -v /path/to/logs:/app/logs \
  -e "TZ=America/Los_Angeles" \
  --name container-updater \
  anthonymolinari/container-updater:latest
```

## Docker Compose
```yaml
version: '3.0'

services:
  container_updater:
    container_name: container_updater
    image: anthonymolinari/container-updater:latest
    volumes:
      - /path/on/host/config:/app/config
      - /path/on/host/logs:/app/logs
    environment:
      - TZ=America/Los_Angeles
    restart: unless-stopped
```

<hr>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)