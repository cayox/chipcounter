import datetime
import os
import sys
import io

import pandas as pd
import numpy as np
from PyQt6 import QtCore, QtWidgets
import time
from chip_counter.config import CONFIG
from chip_counter.models.gpio import GPIO
import logging


log = logging.getLogger(__name__)


class SensorThread(QtCore.QThread):
    chip_detected = QtCore.pyqtSignal()

    def __init__(self, sensor_pin: int):
        super().__init__()

        self.sensor_pin = sensor_pin
        self.previous_state = GPIO.input(self.sensor_pin)
        log.info("Initiated Sensor Thread for pin %s", self.sensor_pin)
        self.running = True

    def run(self):
        while self.running:
            current_state = GPIO.input(self.sensor_pin)
            log.debug("Current GPIO state (PIN %s): %s", self.sensor_pin, current_state)
            if current_state != self.previous_state:
                if current_state == GPIO.LOW:  # Assuming IR sensor is active low
                    self.chip_detected.emit()
                self.previous_state = current_state

    def stop(self):
        self.running = False
        self.wait()


class CountManager(QtCore.QObject):
    red_chip_detected = QtCore.pyqtSignal()
    blue_chip_detected = QtCore.pyqtSignal()
    chip_detected = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.count_history = pd.DataFrame(
            columns=["hour", "blue_chips", "red_chips", "summary"]
        ).astype(
            {
                "hour": "uint16",
                "blue_chips": "uint16",
                "red_chips": "uint16",
                "summary": "uint16",
            }
        )
        self.count_history.loc[:, "hour"] = np.arange(1, 25)

        # self.sensor1_thread = SensorThread(CONFIG.raspberry_pi.sensor_pin1)
        # self.sensor1_thread.chip_detected.connect(
        #     lambda: self.blue_chip_detected.emit()
        # )
        # self.sensor1_thread.start()

        # self.sensor2_thread = SensorThread(CONFIG.raspberry_pi.sensor_pin2)
        # self.sensor2_thread.chip_detected.connect(lambda: self.red_chip_detected.emit())
        # self.sensor2_thread.start()

        GPIO.add_event_detect(CONFIG.raspberry_pi.sensor_pin1, GPIO.FALLING, callback=lambda: self.red_chip_detected.emit())
        GPIO.add_event_detect(CONFIG.raspberry_pi.sensor_pin2, GPIO.FALLING, callback=lambda: self.blue_chip_detected.emit())



    def activate_vibration(self):
        GPIO.output(CONFIG.raspberry_pi.motor_pin, GPIO.HIGH)
        QtCore.QTimer.singleShot(
            CONFIG.counting.motor_duration * 1000,
            lambda: GPIO.output(CONFIG.raspberry_pi.motor_pin, GPIO.LOW),
        )

    def activate_ctrl_led(self, chip_type: str):
        if chip_type == "red_chips":
            pin = CONFIG.raspberry_pi.ctrl_sensor_pin1
        else:
            pin = CONFIG.raspberry_pi.ctrl_sensor_pin2

        GPIO.output(pin, GPIO.HIGH)
        QtCore.QTimer.singleShot(
            100,
            lambda: GPIO.output(pin, GPIO.LOW),
        )

    def cleanup(self):
        self.sensor1_thread.stop()
        self.sensor2_thread.stop()
        GPIO.cleanup()

    @QtCore.pyqtSlot()
    def _blue_chip_detected(self):
        self._chip_detected("blue_chips")
        log.debug("Blue Chip detected")

    @QtCore.pyqtSlot()
    def _red_chip_detected(self):
        self._chip_detected("red_chips")
        log.debug("Red Chip detected")

    def _chip_detected(self, chip_type: str):
        self.activate_ctrl_led(chip_type)

        hour = datetime.datetime.now().hour
        self.count_history.loc[self.count_history["hour"] == hour, chip_type] += 1

        self.count_history["summary"] = (
            self.count_history["red_chips"]
            + self.count_history["blue_chips"] // CONFIG.counting.chip_factor
        )
