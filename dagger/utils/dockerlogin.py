import os
import sys
from decouple import config

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
          sys.exit(2)
     