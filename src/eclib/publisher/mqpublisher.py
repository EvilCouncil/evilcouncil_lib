import pika

from . import message
from . import ecpublisher


class MQPublisher(ecpublisher.ECPublisher):
    def __init__(self, host: str, port: int, exchange: str):
        self._conn_param = pika.ConnectionParameters(host=host, port=port)
        self._exchange = exchange

    def send_message(self, msg: message.Message):
        with pika.BlockingConnection(self._conn_param) as conn:
            channel = conn.channel()

            channel.basic_publish(
                exchange=self._exchange,
                routing_key=msg.get_routing_key(),
                body=msg.get_message(),
            )
