from PyQt6 import QtCore, QtWidgets, QtGui
from typing import Literal, Any
import datetime

class HeaderLabel(QtWidgets.QLabel):
    """Label that is styled as a header in QSS stylesheet.

    Has glow effect.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.setObjectName("HeaderLabel")


class TitleLabel(QtWidgets.QLabel):
    """Label that is styled as a title in QSS stylesheet.

    Has glow effect.
    """

    def __init__(self, text: str):
        super().__init__(f"{text}")
        self.setObjectName("Title")


class TimeWidget(HeaderLabel):
    """Widget representing a time or date, which updates automatically.

    Args:
        timer_interval: the intervall the time should be updated.
        time_format: the format in which the time should be represented.
            See datetime library for format options. Defaults to "%H:%M".
    """

    def __init__(
            self,
            timer_interval: int = 60_000,
            time_format: str | None = None,
            *args: Any,
            **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)

        if time_format is None:
            time_format = "%H:%M"

        self.setObjectName("TimeWidget")

        self.timer_interval = timer_interval
        self.time_format = time_format

        self.update_time()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.timer_interval)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    @QtCore.pyqtSlot()
    def update_time(self):
        time = datetime.datetime.now()
        self.setText(time.strftime(self.time_format))