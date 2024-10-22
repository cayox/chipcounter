import logging
import time

from PyQt6 import QtCore

from chip_counter.config import CONFIG
from chip_counter.models.gpio import GPIO
from chip_counter.models.utils import toggle_backlight

try:
    # import lgpio on py if possible to catch errors with gpio
    import lgpio.error
except ImportError:
    pass

log = logging.getLogger(__name__)


class ButtonSwitchManager(QtCore.QObject):
    """Class to manage the buttons and switches states of this project."""

    button1_pressed = QtCore.pyqtSignal()
    button2_pressed = QtCore.pyqtSignal()
    switch_changed = QtCore.pyqtSignal(int)

    def __init__(
        self,
        button1_pin: int,
        button2_pin: int,
        switch_pin1: int,
        switch_pin2: int,
        power_button_pin: int,
    ):
        super().__init__()
        self.button1_pin = button1_pin
        self.button2_pin = button2_pin
        self.switch_pins = [switch_pin1, switch_pin2]
        self.power_button_pin = power_button_pin

        self.switch_state = -1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.power_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(
            self.power_button_pin,
            GPIO.FALLING,
            callback=toggle_backlight,
            bouncetime=CONFIG.raspberry_pi.sensor_bounce_time,
        )
        for pin in self.switch_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.thread = QtCore.QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.monitor_inputs)
        self.thread.start()

    @QtCore.pyqtSlot()
    def monitor_inputs(self) -> None:
        """Method to check the inputs of the buttons and switches in an endless loop."""
        try:
            while True:
                if not GPIO.input(self.button1_pin):
                    self.button1_pressed.emit()
                    log.info("Button1 pressed")
                    time.sleep(0.2)
                if not GPIO.input(self.button2_pin):
                    self.button2_pressed.emit()
                    log.info("Button2 pressed")
                    time.sleep(0.2)
                new_switch_state = self.get_switch_state()
                if new_switch_state != self.switch_state:
                    log.info("New Switch state %s", new_switch_state)
                    self.switch_state = new_switch_state
                    self.switch_changed.emit(self.switch_state)
                time.sleep(0.1)
        except lgpio.error:
            return

    def get_switch_state(self) -> int:
        """Method to find out the current state of the switch. Returns -1 if no state was detected."""
        for index, pin in enumerate(self.switch_pins):
            if not GPIO.input(pin):
                return index
        return -1
