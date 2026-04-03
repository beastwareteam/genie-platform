from genie.app.container import ApplicationContainer
from genie.app.lifecycle import ApplicationController
from genie.infrastructure.server import LocalServerEdge


def bootstrap_application() -> ApplicationController:
    container = ApplicationContainer.build_default()
    return ApplicationController(container=container)


def bootstrap_server_edge() -> LocalServerEdge:
    container = ApplicationContainer.build_default()
    return container.edge.server_edge
