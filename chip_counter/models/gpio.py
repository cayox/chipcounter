import logging

from chip_counter.config import CONFIG

log = logging.getLogger(__name__)


# Mocking GPIO for non-RPi environment
class MockGPIO:
    """Class for ocking the GPIO of the raspberry pi so that the script doesnt throw errors when tested on a pc."""

    BCM = "BCM"
    IN = "IN"
    OUT = "OUT"
    LOW = 0
    HIGH = 1
    PUD_UP = "PUD_UP"
    FALLING = 1
    RISING = 2
    BOTH = 3

    def __init__(self):
        self.pin_state = {}

    def setmode(self, mode: str) -> None:
        """Emulate the setmode method."""

    def setup(self, pin: int, mode: str, pull_up_down: str | None = None) -> None:  # noqa: ARG002
        """Emulate the setup method."""
        self.pin_state[pin] = MockGPIO.LOW if not pull_up_down else MockGPIO.HIGH

    def input(self, pin: int) -> int:  # noqa: ARG002
        """Emulate the input method."""
        return -1

    def output(self, pin: int, state: int) -> None:
        """Emulate the output method."""
        self.pin_state[pin] = state

    def cleanup(self) -> None:
        """Emulate the cleanup method."""
        self.pin_state = {}

    def add_event_detect(self, *args, **kwargs) -> None:
        """Emulate the add_event_detect method."""


def is_raspberry_pi() -> bool:
    """Method to check if script runs on a raspberry pi."""
    try:
        with open("/sys/firmware/devicetree/base/model") as m:
            if "raspberry pi" in m.read().lower():
                return True
    except Exception as exc:
        log.exception("Error when defining system platform", exc_info=exc)
    return False


def setup_gpio() -> "GPIO":
    """Method to setup the GPIO.

    If this file runs not on a raspberry pi, the GPIO of the raspberry pi is emulated.
    """
    if not is_raspberry_pi():
        log.debug("Initiating mock GPIO")
        return MockGPIO()

    from RPi import GPIO

    log.debug("Initiating real GPIO on Raspberry Pi")

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CONFIG.raspberry_pi.count_sensor1_pin, GPIO.IN)
    GPIO.setup(CONFIG.raspberry_pi.count_sensor2_pin, GPIO.IN)
    GPIO.setup(CONFIG.raspberry_pi.motor1_trigger_sensor, GPIO.IN)
    GPIO.setup(CONFIG.raspberry_pi.motor2_trigger_sensor, GPIO.IN)
    GPIO.setup(CONFIG.raspberry_pi.motor1_pin, GPIO.OUT)
    GPIO.setup(CONFIG.raspberry_pi.motor2_pin, GPIO.OUT)
    return GPIO


GPIO = setup_gpio()
