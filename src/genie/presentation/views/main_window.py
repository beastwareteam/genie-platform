from PySide6.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget

from genie.presentation.viewmodels.main_view_model import MainViewModel


class MainWindow(QMainWindow):
    def __init__(self, view_model: MainViewModel) -> None:
        super().__init__()
        self._view_model = view_model
        self.setWindowTitle("Genie Platform")
        self.resize(860, 520)

        root = QWidget(self)
        layout = QVBoxLayout(root)

        self._title = QLabel(self._view_model.state.title)
        self._input = QLineEdit()
        self._input.setPlaceholderText("Prompt an Genie senden...")
        self._button = QPushButton("Senden")
        self._output = QLabel(self._view_model.state.last_output)

        self._button.clicked.connect(self._on_submit)

        layout.addWidget(self._title)
        layout.addWidget(self._input)
        layout.addWidget(self._button)
        layout.addWidget(self._output)

        self.setCentralWidget(root)

    def _on_submit(self) -> None:
        prompt = self._input.text().strip()
        if not prompt:
            return
        self._view_model.submit_prompt(prompt)
        self._output.setText(self._view_model.state.last_output)
        self._input.clear()
