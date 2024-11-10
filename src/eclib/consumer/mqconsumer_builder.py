from . import mqconsumer
from . import config_constants
from . import config_loader
from . import routing_keys
import queue


def BuildMQConsumer(
    cl: config_loader.ConfigLoader, ck: routing_keys.ConsumerKeys
) -> mqconsumer.MQConsumer:
    server = cl.get_config(config_constants.ConfigConstants.rabbit_server)
    port = cl.get_config(config_constants.ConfigConstants.rabbit_port)
    exchange = cl.get_config(config_constants.ConfigConstants.rabbit_exchange)
    local_queue = queue.Queue()

    return mqconsumer.MQConsumer(server, port, exchange, ck, local_queue)
