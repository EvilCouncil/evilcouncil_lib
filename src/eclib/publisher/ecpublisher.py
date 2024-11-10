import abc
from . import message


class ECPublisher(abc.ABC):
    """Base class for EC publishers."""

    def send_message(self, msg: message.Message):
        """Sends message to appropirate destination."""
