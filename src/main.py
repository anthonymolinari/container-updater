import threading
import asyncio
import aiocron

from utils import logger, config as con, updater
from providers.servarr import servarrUpdate
from providers.portainer import portainerWebhook


def main(config): 
    threads = list()

    # create threads for each container
    for container in config['containers']:
        logger.log(f'spawning worker for: {container["name"]}')
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
    logger.log('awaiting next scheduled job...')
    await aiocron.crontab(config['schedule']).next()
    main(config)


if __name__ == '__main__':
    config = con.loadConfig("./config/config.yml")
    if not con.validate(config):
        exit(2)
    
    loop = asyncio.get_event_loop_policy().get_event_loop()
    
    while True:
        loop.run_until_complete(runner(config))
    