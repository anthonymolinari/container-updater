import sys
import anyio
import dagger 

async def buildImage():
     async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
          src = client.host().directory(".")
          python = (
               client.container()
               .with_mounted_directory("/app", src)
               .with_workdir("/app")
               .build(src)
               .publish("docker.io/anthonymolinari/container-updater:latest")
          )
          await python

     print("Pipeline Done")


if __name__ == "__main__":
     anyio.run(buildImage)
