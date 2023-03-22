from utils import logger
from providers.servarr import servarrUpdate
from providers.portainer import portainerWebhook


def updater(container, discord_webhook):
    if container['container']['isServarr']:
        if servarrUpdate(
            container['container']['url'], 
            container['container']['apiKey'], 
            container['name'],
            container['container']['apiVer'],
            discord_webhook
        ):
            stat = portainerWebhook(container['portainer']['webhook'])
            logger.log(f'portainer reponse: {stat}')
            