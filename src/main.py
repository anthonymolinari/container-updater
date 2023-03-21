import yaml
import threading
import asyncio
import aiocron
from time import sleep
from utils import webhooks, logger



def validate(config) -> bool:
    # validate configuration

    # has been scheduled
    if 'schedule' not in config:
        return False

    # has portainer key
    if 'portainer' not in config:
        return False
    # has containers 
    if 'containers' not in config:
        print('Configuration missing "containers" key')
        return False

    return True


def loadConfig() -> any:
    logger.log("loading config")
    try:
        with open('./config/config.yml', 'r') as config_file:
            config = yaml.safe_load(config_file)
    except:
        logger.log("failed to open configuration file, you may need to create one.")
        logger.log("terminating...")
        exit(1)

    return config


def updater(container, discord_webhook):
    if container['container']['isServarr']:
        if webhooks.servarrUpdate(
            container['container']['url'], 
            container['container']['apiKey'], 
            container['name'],
            container['container']['apiVer'],
            discord_webhook
        ):
            stat = webhooks.portainerWebhook(container['portainer']['webhook'])
            logger.log(f'portainer reponse: {stat}')



def main(config): 
    threads = list()

    # create threads for each container
    for container in config['containers']:
        logger.log(f'spawning worker for: {container["name"]}')
        threads.append(
            threading.Thread(target=updater, args=(container, config['notifications']['discord']['webhook'],))
        )
        threads[-1].start() # start last thread pushed to list

    for thread in threads:
        thread.join() 
        logger.log(f'thread closed...')


async def runner(config: any):
    logger.log('awaiting next scheduled job...')
    await aiocron.crontab(config['schedule']).next()
    main(config=config)



if __name__ == '__main__':
    config = loadConfig()
    if not validate(config):
        exit(2)
    
    loop = asyncio.get_event_loop_policy().get_event_loop()
    
    while True:
        loop.run_until_complete(runner(config))
    
    
    
    
