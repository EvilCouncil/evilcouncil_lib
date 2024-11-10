from . import mqpublisher
from . import config_constants
from . import config_loader
from . import routing_keys


def BuildMQPublisher(
    cl: config_loader.ConfigLoader, rk: routing_keys.RoutingKeys
) -> mqpublisher.MQPublisher:
    server = cl.get_config(config_constants.ConfigConstants.rabbit_server)
    port = cl.get_config(config_constants.ConfigConstants.rabbit_port)
    exchange = cl.get_config(config_constants.ConfigConstants.rabbit_exchange)

    return mqpublisher.MQPublisher(host=server, port=port, exchange=exchange)
