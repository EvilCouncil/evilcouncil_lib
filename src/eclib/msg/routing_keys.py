import enum


class RoutingKeys(enum.StrEnum):
    notification = "messaging.evilcouncil.notification"
    http_log_collection = "infra.log_collect.http"
    docker_log_collection = "infra.log_collect.docker"
    malware_urls = "infra.malware.urls"


class ConsumerKeys(enum.StrEnum):
    infra_all = "infra.#"
    infra_log_collect = "infra.log_collect.#"
    malare_urls = "infra.malware.urls"
