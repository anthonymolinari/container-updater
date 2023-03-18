import sys
import anyio
import dagger 

async def buildImage():
     async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
          src = client.host().directory(".")
          # username = client.host().env_variable("DOCKER_HUB_USERNAME")
          token = client.host().env_variable("DOCKER_HUB_TOKEN")

          python = (
               client.container()
               .with_mounted_directory("/app", src)
               .with_workdir("/app")
               .build(src)
               .with_registry_auth(
                    "docker.io",
                    "anthonymolinari",
                    token.secret()
               )
               .publish("docker.io/anthonymolinari/container-updater:latest")
          )
          await python

     print("Finished build")


if __name__ == "__main__":
     anyio.run(buildImage)
