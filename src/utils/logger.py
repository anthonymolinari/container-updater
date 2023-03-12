from datetime import datetime


def log(msg: str):
    now = datetime.now()
    print(f'[{now.strftime("%H:%M:%S")}]: {msg}')


def error(msg: str):
    now = datetime.now()
    print(f'[{now.strftime("%H:%M:%S")}][ERROR]: {msg}')