import yaml
from utils import logger

def load_config(path: str) -> any:
    logger.log("loading config")
    try:
        with open(path, 'r') as config_file:
            config = yaml.safe_load(config_file)
    except:
        logger.log("failed to open configuration file, you may need to create one.")
        logger.log("terminating...")
        exit(1)

    return config


def validate_config(config: any) -> bool:
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
