from .controller import Controller
from chip_counter.views import MainView, HomeView, HistoryView, SettingsView
import pandas as pd
import numpy as np
from chip_counter.models.count_manager import CountManager
from chip_counter.models.input_manager import ButtonSwitchManager
from PyQt6 import QtCore
from chip_counter.config import CONFIG

DATA = pd.DataFrame({"Counts": np.random.randint(0, 200, 24)})


class MainController(Controller[MainView]):
    def __init__(self):
        super().__init__(MainView)

    def connect_view(self):
        self.ctrl_home = None

        self.view_home = HomeView()
        self.view.stack.addWidget(self.view_home)

        self.view_history = HistoryView()
        self.view.stack.addWidget(self.view_history)

        self.view_settings = SettingsView()
        self.view.stack.addWidget(self.view_settings)

        self.count_manager = CountManager()
        self.count_manager.chip_detected.connect(self.increment_count)

        self.input_manager = ButtonSwitchManager(
            button1_pin=CONFIG.raspberry_pi.button_reset_pin,
            button2_pin=CONFIG.raspberry_pi.button_engine_pin,
            switch_pin1=CONFIG.raspberry_pi.mode_switch_pin1,
            switch_pin2=CONFIG.raspberry_pi.mode_switch_pin2,
        )

        self.increment_count()

    @QtCore.pyqtSlot()
    def increment_count(self):
        history = self.count_manager.count_history

        sum_blue_chips = int(history["blue_chips"].sum())
        sum_red_chips = int(history["red_chips"].sum())
        sum_all_chips = int(history["summary"].sum())

        self.view_home.red_chips_count_widget.set_count(sum_blue_chips)
        self.view_home.blue_chips_count_widget.set_count(sum_red_chips)
        self.view_home.all_chips_count_widget.set_count(sum_all_chips)

        self.view_history.red_chips_count_widget.set_count(sum_blue_chips)
        self.view_history.blue_chips_count_widget.set_count(sum_red_chips)
        self.view_history.all_chips_count_widget.set_count(sum_all_chips)

        self.view_history.plot_widget.update_data(history)
