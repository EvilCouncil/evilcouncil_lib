from . import config_loader
from . import config_constants

import requests
import yaml


class HttpYamlConfigLoader(config_loader.ConfigLoader):

    def __init__(self, config_url: str):
        response = requests.get(config_url)
        response.raise_for_status()
        self._data = yaml.safe_load(response.text)

    def get_config(self, key: config_constants.ConfigConstants):
        data = self._data
        for kp in key.split("."):
            val = data.get(kp, None)
            if val == None:
                raise ValueError

            elif type(val) == dict:
                data = val
            else:
                return val
        else:
            raise ValueError
