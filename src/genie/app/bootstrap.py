from genie.app.container import ApplicationContainer
from genie.app.lifecycle import ApplicationController


def bootstrap_application() -> ApplicationController:
    container = ApplicationContainer.build_default()
    return ApplicationController(container=container)
