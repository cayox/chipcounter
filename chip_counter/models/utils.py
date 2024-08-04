import subprocess

from chip_counter.models.gpio import is_raspberry_pi


def set_display_brightness(brightness: float) -> bool:
    """Set the brightness level of the specified display."""
    if brightness < 0.0 or brightness > 1.0:
        raise ValueError("Brightness must be between 0.0 and 1.0")

    try:
        # Calculate the desired brightness level as a percentage
        brightness_percentage = int(brightness * 100)

        # Set the brightness using brightnessctl
        subprocess.run(  # noqa: S603
            ["brightnessctl", "set", f"{brightness_percentage}%"],  # noqa: S607
            check=True,
        )

    except subprocess.CalledProcessError:
        return False
    else:
        return True


_toggle = True


def toggle_backlight(*_) -> None:
    """Method to toggle the raspberry pi screen backlight."""
    if not is_raspberry_pi():
        return

    global _toggle  # noqa: PLW0603
    _toggle = not _toggle
    set_display_brightness(brightness=1 * int(_toggle))
