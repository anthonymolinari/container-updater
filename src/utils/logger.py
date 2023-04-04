from datetime import datetime
import logging

def log(msg: str):
    now = datetime.now()
    logging.info(msg)
    print(f'[{now.strftime("%H:%M:%S")}]: {msg}', flush=True)


def error(msg: str):
    now = datetime.now()
    logging.error(msg)
    print(f'[{now.strftime("%H:%M:%S")}][ERROR]: {msg}', flush=True)