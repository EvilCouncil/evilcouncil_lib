import enum


class ConfigConstants(enum.StrEnum):
    rabbit_server = "rabbit.server"
    rabbit_port = "rabbit.port"
    rabbit_exchange = "rabbit.exchange"
    rabbit_queue = "rabbit.queue"
    mysql_server = "mysql.server"
    mysql_port = "mysql.port"
    mysql_user = "mysql.user"
    mysql_password = "mysql.password"
