from PySide6.QtWidgets import QApplication

from genie.app.container import ApplicationContainer
from genie.presentation.views.main_window import MainWindow


class ApplicationController:
    def __init__(self, container: ApplicationContainer) -> None:
        self._container = container

    def run(self) -> None:
        app = QApplication([])
        window = MainWindow(view_model=self._container.main_view_model)
        window.show()
        app.exec()
