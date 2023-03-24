import threading
import asyncio
import aiocron
import logging

from utils.logger import log, error
from utils.config import load_config, validate_config
from utils.updater import updater
from providers.servarr import servarrUpdate
from providers.portainer import portainerWebhook


def main(config): 
    threads = list()

    # create threads for each container
    for container in config['containers']:
        log(f'spawning worker for: {container["name"]}')
        threads.append(
            threading.Thread(
                target=updater, 
                args=(container, config['notifications']['discord']['webhook'],)
            )
        )
        threads[-1].start() # start last thread pushed to list

    for thread in threads:
        thread.join() 
        logger.log(f'thread closed...')


async def runner(config: any):
    log('awaiting next scheduled job...')
    await aiocron.crontab(config['schedule']).next()
    main(config)


if __name__ == '__main__':
    logger = logging.basicConfig(
        filename="./logs/container-updater.logs",
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG           
    )

    config = load_config("./config/config.yml")
    if not validate_config(config):
        exit(2)
    
    log("config is valid...")

    loop = asyncio.get_event_loop_policy().get_event_loop()
    
    while True:
        loop.run_until_complete(runner(config))
    