import yaml
import threading
from time import sleep
from utils import webhooks, logger


def validate(config) -> bool:
    # validate configuration
    return True


def loadConfig() -> any:
    logger.log("loading config")
    try:
        with open('../config/config.yml', 'r') as config_file:
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


def main(): 
    # load configuration
    config = loadConfig()
    if not validate(config):
        exit(2)
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
        

if __name__ == '__main__':
    main()
