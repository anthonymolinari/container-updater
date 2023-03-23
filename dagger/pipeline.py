import sys
import anyio
import dagger 
import os
from decouple import config

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


def dockerLogin():
     USERNAME = os.getenv('DOCKERHUB_USERNAME')
     TOKEN = os.getenv('DOCKERHUB_TOKEN')

     if USERNAME is None or TOKEN is None:
          # use local .env
          USERNAME = config('DOCKERHUB_USERNAME')
          TOKEN = config('DOCKERHUB_TOKEN')

     if os.system(f'docker login -u {USERNAME} -p {TOKEN}') != 0:
          print(f'Error login failed')
          sys.exit(1)
     

def dockerLogout():
     if os.system('docker logout') != 0:
          print(f'Error logout failed')
          sys.exit(1)
     

if __name__ == "__main__":
     dockerLogin()
     anyio.run(buildImage)
     dockerLogout()
          
