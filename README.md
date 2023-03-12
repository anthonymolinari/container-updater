# Container Updater
A simple python script that uses portainer webhooks to update containers.

## Supports Version Checks
- servarr applications: sonarr, radarr, prowlarr, lidarr
- coming soon plex, jellyfin


## example configuration
` ./config/config.yml`
```
portainer: 
  url: "http://portainer.lan"
  interval: 60 # polling interval 

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
