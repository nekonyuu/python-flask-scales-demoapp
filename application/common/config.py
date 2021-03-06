import os
import glob

import yaml

from . import Map

# DEFAULTS
# --------
DEFAULT_ENVIRONMENT = 'development'
DEFAULT_CONFIG = {
    "environment": DEFAULT_ENVIRONMENT,
    "listen_port": 8090,
    "debug": True,
    "graphite": {
        "enable": False,
        "host": "127.0.0.1",
        "port": 2003
    }
}


def load_configuration():
    """
    Load configuration using ENV environment variable
    :return: a Map object containing the configuration
    :rtype: Map
    """
    # load available environment configs
    env_list = dict()
    env_configs = glob.glob("config/*.yml")
    config = DEFAULT_CONFIG.copy()

    for cp in env_configs:
        env_name = os.path.basename(cp).split(".")[0]
        env_list.update({env_name: cp})

    # loading configuration based on environment, fallback :
    #   - on development if passed one does not exist ;
    #   - on default config if development does not exist.
    if "ENV" in os.environ and os.environ["ENV"] in env_list:
        environment = os.environ["ENV"]
        config_path = env_list[environment]
    elif DEFAULT_ENVIRONMENT in env_list:
        environment = DEFAULT_ENVIRONMENT
        config_path = env_list[environment]
    else:
        environment = DEFAULT_ENVIRONMENT
        config_path = None

    if config_path is None:
        config = DEFAULT_CONFIG
    else:
        config_file = open(config_path)
        config.update(yaml.load(config_file))
        config.update({"environment": environment})

    return Map(config)
