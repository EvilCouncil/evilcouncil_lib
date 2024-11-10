"""Read from rabbitmq, dump data onto a queue"""

# rabbitmq
import pika

# standard
import json
import time
import logging
import sys
import threading
import time
import queue

from . import routing_keys


class MQConsumer(threading.Thread):
    """Object to wrap around RabbitMQ and send gelf data"""

    def __init__(
        self,
        host: str,
        port: int,
        exchange: str,
        routes: routing_keys.ConsumerKeys,
        local_queue: queue.Queue,
    ):
        super().__init__()
        self._exchange = exchange
        self._routing_key = routes
        self._host = host
        self._port = port
        self._running = True
        self._queue_name = None
        self._rabbitqueue = None
        self._queue = local_queue

    def _connect(self):
        # why did i turn heartbeat off
        # self.conection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port, heartbeat=0))
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self._host, port=self._port)
        )
        self._channel = self._connection.channel()
        self._channel.exchange_declare(
            exchange=self._exchange, exchange_type="topic", durable=True
        )

        self._rabbitqueue = self._channel.queue_declare(
            "", auto_delete=True, exclusive=True
        )
        self._queue_name = self._rabbitqueue.method.queue
        self._channel.queue_bind(
            exchange=self._exchange,
            queue=self._queue_name,
            routing_key=self._routing_key,
        )

    def run(self):
        self._connect()
        self._channel.basic_consume(self._queue_name, self.handle_message)

        while self._running:
            time.sleep(1)
            self._connection.process_data_events()

            #     self.conection.process_data_events()

        self._connection.close()

    def stop(self):
        self._running = False

    def handle_message(self, channel, method_frame, header_frame, body):
        # print(method_frame.delivery_tag)
        self._queue.put_nowait(json.loads(body))
        # channel.basic_ack(delivery_tag=header_frame.delivery_tag)

    @property
    def queue(self) -> queue.Queue:
        return self._queue
