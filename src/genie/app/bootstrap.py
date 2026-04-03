from genie.app.container import ApplicationContainer
from genie.infrastructure.server import LocalHttpServer, LocalServerEdge


def bootstrap_application() -> "ApplicationController":
    from genie.app.lifecycle import ApplicationController

    container = ApplicationContainer.build_default()
    return ApplicationController(container=container)


def bootstrap_server_edge() -> LocalServerEdge:
    container = ApplicationContainer.build_default()
    return container.edge.server_edge


def bootstrap_http_server(host: str = "127.0.0.1", port: int = 8765) -> LocalHttpServer:
    edge = bootstrap_server_edge()
    return LocalHttpServer(edge=edge, host=host, port=port)
