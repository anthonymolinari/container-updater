# Container Updater
A python script that uses portainer webhooks to update containers

> See the [Github](https://github.com/anthonymolinari/container-updater) form more information

## Usage

### Docker Command
```shell
docker run -d \
  -v /path/to/config/:/app/config/ \
  -v /path/to/logs:/app/logs \
  -e "TZ=America/Los_Angeles" \
  --name container-updater \
  anthonymolinari/container-updater:latest
```

### Docker Compose
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
