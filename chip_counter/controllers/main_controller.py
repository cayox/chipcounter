import logging
import sys

from PyQt6 import QtCore

from chip_counter.config import CONFIG, CONFIG_PATH
from chip_counter.controllers.ctrl_password import PasswordController
from chip_counter.models.count_manager import CountManager
from chip_counter.models.gpio import GPIO
from chip_counter.models.input_manager import ButtonSwitchManager
from chip_counter.views import HistoryView, HomeView, MainView, SettingsView

from .controller import Controller

log = logging.getLogger(__name__)

SETTINGS_BUTTON_PAGE_INDEX = 2


class MainController(Controller[MainView]):
    """Controller managing the main components of the app."""

    def __init__(self):
        super().__init__(MainView)

    def connect_view(self) -> None:  # noqa: D102 inherited
        self.view.settings_button.clicked.connect(lambda *_: self._on_switch_change(3))

        self.ctrl_home = None

        self.view_home = HomeView()
        self.view.stack.addWidget(self.view_home)

        self.ctrl_password = PasswordController()
        self.ctrl_password.password_correct.connect(
            lambda *_: self._on_switch_change(2)
        )
        self.view.stack.addWidget(self.ctrl_password.view)

        self.view_history = HistoryView()
        self.view.stack.addWidget(self.view_history)

        self.view_settings = SettingsView()
        self.view_settings.back_button.clicked.connect(
            lambda *_: self._on_switch_change(2)
        )
        self.view_settings.chip_factor.valueChanged.connect(self._on_chip_factor_change)
        self.view_settings.motor_duration.valueChanged.connect(
            self._on_motor_duration_change
        )
        self.view_settings.reset_button.clicked.connect(self._on_full_reset_press)
        self.view_settings.close_button.clicked.connect(self.close)
        self.view.stack.addWidget(self.view_settings)

        self.count_manager = CountManager()
        self.count_manager.load()
        self.count_manager.chip_detected.connect(self.display_counts)

        self.input_manager = ButtonSwitchManager(
            button1_pin=CONFIG.raspberry_pi.button_reset_pin,
            button2_pin=CONFIG.raspberry_pi.button_engine_pin,
            switch_pin1=CONFIG.raspberry_pi.mode_switch_pin1,
            switch_pin2=CONFIG.raspberry_pi.mode_switch_pin2,
            power_button_pin=CONFIG.raspberry_pi.power_button_pin,
        )

        self.display_counts()

        self.input_manager.switch_changed.connect(self._on_switch_change)
        self.input_manager.button1_pressed.connect(self._on_reset_press)
        self.input_manager.button2_pressed.connect(
            self.count_manager.activate_full_vibration
        )

    @QtCore.pyqtSlot()
    def close(self) -> None:
        """Method to call when closing the application. Cleans up data, GPIO and saves the counts."""
        self.count_manager.save()
        CONFIG.save(CONFIG_PATH)
        GPIO.cleanup()
        sys.exit(0)

    @QtCore.pyqtSlot()
    def display_counts(self) -> None:
        """Method to update and display the counts of all count widgets."""
        log.debug("Displaying new Counts")
        history = self.count_manager.count_history

        sum_blue_chips = int(history["blue_chips"].sum())
        sum_red_chips = int(history["red_chips"].sum())
        sum_all_chips = int(history["summary"].sum())

        log.debug(
            "Chip Sums: [Red: %s] [Blue: %s] [All: %s]",
            sum_red_chips,
            sum_blue_chips,
            sum_all_chips,
        )
        factor = history.loc[0, "factor"]

        self.view_home.red_chips_count_widget.set_count(sum_red_chips)
        self.view_home.red_chips_count_widget.set_total_counts(sum_red_chips)
        self.view_home.blue_chips_count_widget.set_count(sum_blue_chips)
        self.view_home.blue_chips_count_widget.set_total_counts(sum_blue_chips * factor)
        self.view_home.all_chips_count_widget.set_count(sum_all_chips)
        self.view_home.all_chips_count_widget.set_total_counts(
            sum_blue_chips * factor + sum_red_chips
        )

        history = self.count_manager.daily_count_history
        factor = history.loc[0, "factor"]

        sum_blue_chips = int(history["blue_chips"].sum())
        sum_red_chips = int(history["red_chips"].sum())
        sum_all_chips = int(history["summary"].sum())

        log.debug(
            "DAILY Chip Sums: [Red: %s] [Blue: %s] [All: %s]",
            sum_red_chips,
            sum_blue_chips,
            sum_all_chips,
        )

        self.view_history.red_chips_count_widget.set_count(sum_red_chips)
        self.view_history.blue_chips_count_widget.set_count(sum_blue_chips)
        self.view_history.all_chips_count_widget.set_count(sum_all_chips)

        self.view_history.red_chips_count_widget.set_total_counts(sum_red_chips)
        self.view_history.blue_chips_count_widget.set_total_counts(
            sum_blue_chips * factor
        )
        self.view_history.all_chips_count_widget.set_total_counts(
            sum_blue_chips * factor + sum_red_chips
        )

        self.view_history.plot_widget.update_data(history)

    @QtCore.pyqtSlot(int)
    def _on_switch_change(self, state: int) -> None:
        self.view.stack.setCurrentIndex(state)
        self.view.settings_button.setVisible(state == SETTINGS_BUTTON_PAGE_INDEX)

    @QtCore.pyqtSlot()
    def _on_reset_press(self) -> None:
        log.info("Resetting Counts")
        self.count_manager.reset()
        self.display_counts()

    @QtCore.pyqtSlot()
    def _on_full_reset_press(self) -> None:
        log.info("Fully Resetting Counts")
        self.count_manager.full_reset()
        self.display_counts()

    @QtCore.pyqtSlot()
    def _on_chip_factor_change(self) -> None:
        CONFIG.counting.chip_factor = self.view_settings.chip_factor.value()
        self.count_manager.count_history.recalculate_data()
        self.count_manager.daily_count_history.recalculate_data()
        self.display_counts()

    @QtCore.pyqtSlot()
    def _on_motor_duration_change(self) -> None:
        CONFIG.counting.motor_duration = self.view_settings.motor_duration.value()
