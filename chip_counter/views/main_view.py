from PyQt6 import QtCore, QtWidgets
from .view import View
from .widgets import TimeWidget, TitleLabel
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(MainView())


class MainView(View):
    def _build_ui(self):

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        header_layout = QtWidgets.QHBoxLayout()
        header_layout.setContentsMargins(16, 16, 16, 16)

        self.time_widget = TimeWidget()
        header_layout.addWidget(self.time_widget)

        self.title = TitleLabel("Chip Counter")
        header_layout.addStretch()
        header_layout.addWidget(self.title)

        self.date_widget = TimeWidget(time_format="%d.%m.%Y")
        header_layout.addStretch()
        header_layout.addWidget(self.date_widget)

        self.close_button = QtWidgets.QPushButton("X")
        self.close_button.clicked.connect(lambda: sys.exit(0))
        header_layout.addWidget(self.close_button)

        layout.addLayout(header_layout)

        self.stack = QtWidgets.QStackedWidget()
        layout.addWidget(self.stack)
