import logging
import os
import sys

from PyQt6 import QtGui, QtWidgets

from chip_counter.config import APP_CONFIG_ROOT, ASSETS, CONFIG
from chip_counter.log import setup_basic_logger
from chip_counter.controllers import MainController

STYLESHEET = os.path.join(ASSETS, "styles", "stylesheet.qss")
FONTS = os.path.join(ASSETS, "fonts")

log_file = os.path.join(
    APP_CONFIG_ROOT,
    CONFIG.general.log_directory,
    "disco_express.log",
)
os.makedirs(os.path.dirname(log_file), exist_ok=True)
setup_basic_logger(log_file)


def load_fonts():
    """Load all available fonts in the assets/fonts directory into the QFontDatabase."""
    for file in os.listdir(FONTS):
        font = os.path.join(FONTS, file)
        QtGui.QFontDatabase.addApplicationFont(font)


def main():  # noqa: D103
    app = QtWidgets.QApplication(sys.argv)

    load_fonts()

    with open(STYLESHEET) as f:
        style = f.read()

    for color_name, color in CONFIG.colors.dict().items():
        style = style.replace(f"%{color_name}%", color)

    app.setStyleSheet(style)

    ctrl = MainController()
    ctrl.view.showFullScreen()
    try:
        app.exec()
    except BaseException as exc:
        logging.exception("Base Exception ocurred", exc_info=exc)
        logging.log("Shutting down")


if __name__ == "__main__":
    main()
