import sys
import anyio
import dagger 
import argparse

from utils.dockerlogin import dockerLogin, dockerLogout


parser = argparse.ArgumentParser()
parser.add_argument("--tag", help="docker image tag", default="unstable")
parser.add_argument("--no-login", help="do not handle registry login w/ this script", action='store_true')

args = parser.parse_args()

async def buildImage():
     async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
          repo = client.host().directory(".")

          # gather files for container build
          dockerfile = repo.file("Dockerfile")
          ignore = repo.file(".dockerignore")
          src = repo.directory("./src")
          config = repo.directory("./config")

          # setup build env
          build = (
               client.container()
                    .with_directory("/build/src", src)
                    .with_directory("/build/config", config)
                    .with_file("/build/Dockerfile", dockerfile)
                    .with_file("/build/.dockerignore", ignore)
                    .with_workdir("/build")
          )

          build_dir = build.directory("/build")

          push = (
               build
                    .build(build_dir)
                    .publish(f"docker.io/anthonymolinari/container-updater:{args.tag}")
          )
          await push
     print("Pipeline Done")


if __name__ == "__main__":
     print("running...")

     try:
          if not args.no_login:
               dockerLogin()
          anyio.run(buildImage)
          if not args.no_login:
               dockerLogout()
     except:
          print('Error Running Pipeline')
          sys.exit(3)
          
