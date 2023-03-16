import sys
import anyio
import dagger 

async def buildImage():
     async with dagger.Connection(dagger.Config(log_out=sys.stderr)) as client:
          src = client.host().directory(".")
          python = (
               client.container().from_("python:3.10-slim-buster")
               .with_mounted_directory("/src", src)
               .with_workdir("/src")
               .with_exec(["pip", "install", "-r", "requirements.txt"])
               .with_exec(["ls"])
          )
          await python.exit_code()
     print("Test Finished")


if __name__ == "__main__":
     anyio.run(buildImage)
