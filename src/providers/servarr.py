import requests as req
from utils import logger
from providers.discord import discordNotification

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
