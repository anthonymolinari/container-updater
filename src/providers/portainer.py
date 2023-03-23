import requests as req

from utils import logger


def portainerWebhook(webhook_url: str) -> int:
    logger.log('requesting container update: ')
    res = req.post(webhook_url)
    if res.status_code != 200 or res.status_code != 204:
        # log error to console
        logger.error(f'invalid webhook url: {webhook_url}')
        return res.status_code

    # todo - wait and check if container succesfully restarts

    return res.status_code
