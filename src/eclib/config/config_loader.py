import abc
from . import config_constants


class ConfigLoader(abc.ABC):
    """Load configs"""

    def get_config(self, key: config_constants.ConfigConstants):
        """get vaalue"""
