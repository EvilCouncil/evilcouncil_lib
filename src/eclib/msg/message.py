import abc
import dataclasses
import json

from . import routing_keys


class Message(abc.ABC):
    def get_message(self) -> str:
        """Gets JSON string of message"""

    def get_routing_key(self) -> routing_keys.RoutingKeys:
        """Gets routing key for message"""


@dataclasses.dataclass
class Notification(Message):
    msg: str

    def get_message(self) -> str:
        return json.dumps({"message": self.msg})

    def get_routing_key(self) -> routing_keys.RoutingKeys:
        return routing_keys.RoutingKeys.notification
