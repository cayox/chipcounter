from PyQt6 import QtCore, QtWidgets

from chip_counter.config import CONFIG

from .view import View
from .widgets import PageTitle


class SettingsView(View):
    """View to display the user settings."""

    def _build_ui(self) -> None:
        main_lay = QtWidgets.QVBoxLayout(self)
        main_lay.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignCenter
        )

        title = PageTitle("Einstellungen")
        main_lay.addWidget(title)

        form_layout = QtWidgets.QFormLayout()
        form_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.chip_factor = QtWidgets.QDoubleSpinBox()
        self.chip_factor.setMinimum(0)
        self.chip_factor.setMaximum(100)
        self.chip_factor.setValue(CONFIG.counting.chip_factor)

        form_layout.addRow("Chip Faktor: ", self.chip_factor)

        self.motor_duration = QtWidgets.QSpinBox()
        self.motor_duration.setMinimum(1)
        self.motor_duration.setMaximum(120)
        self.motor_duration.setValue(CONFIG.counting.motor_duration)

        form_layout.addRow("Vibrationsinterval: ", self.motor_duration)

        self.reset_button = QtWidgets.QPushButton("Reset")
        form_layout.addRow("Kompletter Zähler Reset: ", self.reset_button)

        self.close_button = QtWidgets.QPushButton("Schließen")
        form_layout.addRow("Programm schließen", self.close_button)

        self.back_button = QtWidgets.QPushButton("Zurück")
        form_layout.addWidget(self.back_button)

        main_lay.addLayout(form_layout)
