from PyQt6 import QtCore, QtWidgets

from .view import View
from .widgets import TimeWidget, TitleLabel


class MainWindow(QtWidgets.QMainWindow):
    """The main Window handling all window operations."""

    def __init__(self):
        super().__init__()

        self.setCentralWidget(MainView())


class MainView(View):
    """The Main View storing all content."""

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        header_layout = QtWidgets.QHBoxLayout()
        header_layout.setContentsMargins(16, 16, 16, 16)
        header_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.time_widget = TimeWidget()
        header_layout.addWidget(self.time_widget)

        self.title = TitleLabel("Chip Counter")
        header_layout.addStretch()
        header_layout.addWidget(self.title)

        self.date_widget = TimeWidget(time_format="%d.%m.%Y")
        header_layout.addStretch()
        header_layout.addWidget(self.date_widget)

        self.settings_button = QtWidgets.QPushButton("Settings")
        self.settings_button.setObjectName("SettingsButton")
        self.settings_button.setVisible(False)
        header_layout.addWidget(self.settings_button)

        layout.addLayout(header_layout)

        self.stack = QtWidgets.QStackedWidget()
        layout.addWidget(self.stack)
