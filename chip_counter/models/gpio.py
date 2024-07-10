from chip_counter.config import CONFIG
import logging
import io

log = logging.getLogger(__name__)

# Mocking GPIO for non-RPi environment
class MockGPIO:
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
        pass

    def setup(self, pin: int, mode: str, pull_up_down: str | None = None) -> None:
        self.pin_state[pin] = MockGPIO.LOW

    def input(self, pin: int) -> int:
        return self.pin_state.get(pin, MockGPIO.LOW)

    def output(self, pin: int, state: int) -> None:
        self.pin_state[pin] = state

    def cleanup(self) -> None:
        self.pin_state = {}

    def add_event_detect(self, *args, **kwargs):
        pass


def is_raspberry_pi() -> bool:
    try:
        with io.open("/sys/firmware/devicetree/base/model", "r") as m:
            if "raspberry pi" in m.read().lower():
                return True
    except Exception as exc:
        log.exception("Error when defining system platform", exc_info=exc)
    return False


def setup_GPIO():
    if not is_raspberry_pi():
        log.debug("Initiating mock GPIO")
        return MockGPIO()

    import RPi.GPIO as GPIO
    log.debug("Initiating real GPIO on Raspberry Pi")

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CONFIG.raspberry_pi.sensor_pin1, GPIO.IN)
    GPIO.setup(CONFIG.raspberry_pi.sensor_pin2, GPIO.IN)
    GPIO.setup(CONFIG.raspberry_pi.motor_pin, GPIO.OUT)
    return GPIO


GPIO = setup_GPIO()
