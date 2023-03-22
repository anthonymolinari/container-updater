import requests as req

# return response status
def discordNotification(url: str, msg: str) -> int:
    res = req.post(url=url, json={
        "content": msg,
    })
    
    return res.status_code
