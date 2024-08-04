from chip_counter.models.gpio import is_raspberry_pi

PI_BACKLIGHT_FILE = (
    "/sys/devices/platform/rpi_backlight/backlight/rpi_backlight/bl_power"
)


def toggle_backlight() -> None:
    """Method to toggle the raspberry pi screen backlight."""
    if not is_raspberry_pi():
        return

    with open(PI_BACKLIGHT_FILE, "r+") as file:
        current_status = int(file.read(1))

        bl_set = 1 if current_status == 0 else 0

        bl_update = str(bl_set)
        file.seek(0)
        file.write(bl_update)
