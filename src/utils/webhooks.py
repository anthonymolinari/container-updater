import requests as req

from utils import logger

def servarrUpdate(base_url: str, apiKey: str, name: str, apiVer, discord_url: str) -> bool:
    url = f'{base_url}/api/{apiVer}/update?apiKey={apiKey}'
    res = req.get(url)
    if res.status_code != 200:
        logger.error(f'{name} response code: {res.status_code}')
        return False
    
    # check top version in response
    release = (res.json())[0]
    if not release['latest'] or not release['installable'] or release['installed']:
        return False
    
    logger.log(f'new update available for {name}: { release["version"] }')
    discordNotification(discord_url, f'new update available for {name}: ver { release["version"] }')
    return True


def portainerWebhook(webhook_url: str) -> int:
    logger.log('requesting container update: ')
    res = req.post(webhook_url)
    if res.status_code != 200 or res.status_code != 204:
        # log error to console
        logger.error(f'invalid webhook url: {webhook_url}')
        return res.status_code

    # todo - wait and check if container succesfully restarts

    return res.status_code

# return response status
def discordNotification(url: str, msg: str) -> int:
    res = req.post(url=url, json={
        "content": msg,
    })
    
    return res.status_code