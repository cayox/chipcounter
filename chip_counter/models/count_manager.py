import datetime
import logging
import os
from copy import deepcopy

import numpy as np
import pandas as pd
from PyQt6 import QtCore

from chip_counter.config import APP_CONFIG_ROOT, CONFIG
from chip_counter.models.gpio import GPIO
from threading import Timer

log = logging.getLogger(__name__)


class CountHistory(pd.DataFrame):
    """Class behaving like a dataframe to store and manage the history data."""

    def __init__(self, save_path: str, factor: int | None = None):
        super().__init__(
            columns=["hour", "blue_chips", "red_chips", "summary", "chip_factor"]
        )

        self.save_path = save_path
        self._factor = factor
        self.full_reset()
        self.load()

    @property
    def factor(self) -> int:
        # to refresh the factor without gui restart. Factor is changed directly in the config object
        return CONFIG.counting.chip_factor if self._factor is None else self._factor

    def full_reset(self) -> None:
        """Reset data to default."""
        self.loc[:, "hour"] = np.arange(1, 25)
        self.loc[:, "blue_chips"] = 0
        self.loc[:, "red_chips"] = 0
        self.loc[:, "summary"] = 0
        self.loc[:, "chip_factor"] = self.factor

    def recalculate_data(self) -> None:
        """Recalculate the data and save it afterwards."""
        self["summary"] = self["red_chips"] + (self["blue_chips"] // self.factor)
        self.save()

    def load(self) -> None:
        """Load the data from a file."""
        if not os.path.isfile(self.save_path):
            return
        df = pd.read_csv(self.save_path)
        df.save_path = self.save_path
        df._factor = None
        self.__dict__ = deepcopy(df.__dict__)

    def save(self) -> None:
        """Save the data to a file."""
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)

        self.to_csv(self.save_path)


class CountManager(QtCore.QObject):
    """Class to manage the counting of chips and the vibration of the motors."""

    red_chip_detected = QtCore.pyqtSignal()
    blue_chip_detected = QtCore.pyqtSignal()
    chip_detected = QtCore.pyqtSignal()

    COUNT_SAVE_FILE = os.path.join(APP_CONFIG_ROOT, "saves", "count_history.csv")
    DAILY_COUNT_SAVE_FILE = os.path.join(
        APP_CONFIG_ROOT, "saves", "daily_count_history.csv"
    )

    def __init__(self):
        super().__init__()

        self.daily_count_history = CountHistory(save_path=self.DAILY_COUNT_SAVE_FILE)
        self.count_history = CountHistory(save_path=self.COUNT_SAVE_FILE, factor=1)

        self._motor1_active = False
        self._motor2_active = False

        GPIO.add_event_detect(
            CONFIG.raspberry_pi.count_sensor1_pin,
            GPIO.FALLING,
            callback=self._red_chip_detected,
            bouncetime=CONFIG.raspberry_pi.sensor_bounce_time,
        )
        GPIO.add_event_detect(
            CONFIG.raspberry_pi.count_sensor2_pin,
            GPIO.FALLING,
            callback=self._blue_chip_detected,
            bouncetime=CONFIG.raspberry_pi.sensor_bounce_time,
        )
        GPIO.add_event_detect(
            CONFIG.raspberry_pi.motor1_trigger_sensor,
            GPIO.FALLING,
            callback=self.activate_motor1_vibration,
            bouncetime=CONFIG.raspberry_pi.sensor_bounce_time,
        )
        GPIO.add_event_detect(
            CONFIG.raspberry_pi.motor2_trigger_sensor,
            GPIO.FALLING,
            callback=self.activate_motor2_vibration,
            bouncetime=CONFIG.raspberry_pi.sensor_bounce_time,
        )

        timer = QtCore.QTimer()
        timer.timeout.connect(self.save)
        timer.setInterval(CONFIG.ui.save_interval * 60000)

        # timers because they cannot be created outside of a QThread
        # (GPIO Thread of event handler is not such a environment)
        self.motor1_deactivate_timer = None

        self.motor2_deactivate_timer = None

        self.timers = []

    def reset(self) -> None:
        """Method to reset the current history."""
        self.count_history.full_reset()

    def full_reset(self) -> None:
        """Method to reset all histories."""
        self.count_history.full_reset()
        self.daily_count_history.full_reset()

    @QtCore.pyqtSlot()
    def deactivate_motor1_vibration(self) -> None:
        """Method to deactivate the vibration of the first motor."""
        log.debug("Deactivating motor 1")
        GPIO.output(CONFIG.raspberry_pi.motor1_pin, GPIO.LOW)
        self._motor1_active = False

    @QtCore.pyqtSlot()
    def activate_motor1_vibration(self, *_) -> None:
        """Method to activate the vibration of the first motor."""
        if self._motor1_active:
            return

        log.debug("Activating motor 1")
        self._motor1_active = True
        GPIO.output(CONFIG.raspberry_pi.motor1_pin, GPIO.HIGH)
        self.motor1_deactivate_timer = Timer(CONFIG.counting.motor_duration, self.deactivate_motor1_vibration)
        self.motor1_deactivate_timer.start()
        if not CONFIG.counting.seperate_motors:
            self.activate_motor2_vibration()

    @QtCore.pyqtSlot()
    def deactivate_motor2_vibration(self) -> None:
        """Method to deactivate the vibration of the second motor."""
        log.debug("Deactivating motor 2")
        GPIO.output(CONFIG.raspberry_pi.motor2_pin, GPIO.LOW)
        self._motor2_active = False

    @QtCore.pyqtSlot()
    def activate_motor2_vibration(self, *_) -> None:
        """Method to activate the vibration of the second motor."""
        if self._motor2_active:
            return

        log.debug("Activating motor 2")
        self._motor2_active = True
        GPIO.output(CONFIG.raspberry_pi.motor2_pin, GPIO.HIGH)
        self.motor2_deactivate_timer = Timer(CONFIG.counting.motor_duration, self.deactivate_motor2_vibration)
        self.motor2_deactivate_timer.start()
        if not CONFIG.counting.seperate_motors:
            self.activate_motor1_vibration()

    def activate_full_vibration(self) -> None:
        """Method to activate the vibration of all motors."""
        self.activate_motor1_vibration()
        self.activate_motor2_vibration()

    def _red_chip_detected(self, *_) -> None:
        self._chip_detected("red_chips")
        log.debug("Red Chip detected")

    def _blue_chip_detected(self, *_) -> None:
        self._chip_detected("blue_chips")
        log.debug("Blue Chip detected")

    def _chip_detected(self, chip_type: str) -> None:
        now = datetime.datetime.now()
        hour = now.hour

        self.count_history.loc[self.count_history["hour"] == hour, chip_type] += 1
        self.daily_count_history.loc[self.count_history["hour"] == hour, chip_type] += 1

        self.count_history.recalculate_data()
        self.daily_count_history.recalculate_data()

        self.chip_detected.emit()

    def save(self) -> None:
        """Method to save the histories to their respective save files."""
        log.info("Saving counting logs")
        self.count_history.save()
        self.daily_count_history.save()

    def load(self) -> None:
        """Method to load the histories from their respective save files."""
        log.info("Loading counting logs")
        self.count_history = CountHistory(save_path=self.COUNT_SAVE_FILE, factor=1)
        self.daily_count_history = CountHistory(save_path=self.DAILY_COUNT_SAVE_FILE)
