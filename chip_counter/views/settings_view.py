import datetime

from .view import View
from PyQt6 import QtWidgets, QtCore, QtGui
from .widgets import CountWidget, SummaryCountWidget, CountBarChartWidget, PageTitle
from chip_counter.config import CONFIG


class SettingsView(View):
    def _build_ui(self):
        main_lay = QtWidgets.QVBoxLayout(self)
        main_lay.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

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
        form_layout.addWidget(self.reset_button)

        main_lay.addLayout(form_layout)
