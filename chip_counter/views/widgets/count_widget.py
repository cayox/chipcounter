from PyQt6 import QtCore, QtWidgets, QtGui
from typing import Literal, Any
import datetime


class CountLabel(QtWidgets.QLabel):
    def __init__(self, *args, style_type: Literal["accent1", "accent2"] | None = None,
                 description_field: bool = False, **kwargs):
        super().__init__(*args, **kwargs)

        self.description = description_field

        self.setObjectName("CountLabel")
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._style_type = ""
        self.style_type = style_type

    @QtCore.pyqtProperty(str)
    def style_type(self) -> str:
        """Getter for highlighting the button via QSS stylesheet."""
        return self._style_type

    @style_type.setter
    def style_type(self, state: Literal["accent1", "accent2"] | None):
        """Setter for highlighting the button via QSS stylesheet."""
        # Register change of state
        self._style_type = state if not self.description else f"description_{state}"
        # Update displayed style
        self.style().polish(self)


class CountWidget(QtWidgets.QGroupBox):
    def __init__(
            self,
            title: str | None = None,
            initial_count: int = 0,
            style_type: Literal["accent1", "accent2"] | None = None,
    ):
        super().__init__()
        self.setObjectName("CountWidget")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        self.count_label = CountLabel(str(initial_count))
        layout.addWidget(self.count_label)

        self.description_label = CountLabel("Description", description_field=True)
        layout.addStretch()
        layout.addWidget(self.description_label)

        self.setMaximumHeight(256)

        # Initialize the timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._update_count_animated)

        self.target_count = 0
        self.current_count = 0
        self.increment = 1
        self.fixed_count_up_time = 1000 # in milliseconds

        if title is not None:
            self.setTitle(title)

        self._style_type = ""

        self.style_type = style_type

    def set_count(self, count: int):
        self.target_count = count
        counts = count - int(self.count_label.text())
        interval = self.fixed_count_up_time // counts
        self.timer.start(interval)

    def set_description(self, desc: str):
        self.description_label.setText(desc)

    def _update_count_animated(self):
        current_count = int(self.count_label.text())
        if current_count < self.target_count:
            current_count += self.increment
            self.count_label.setText(str(current_count))
        else:
            self.timer.stop()

    @QtCore.pyqtProperty(str)
    def style_type(self) -> str:
        """Getter for highlighting the button via QSS stylesheet."""
        return self._style_type

    @style_type.setter
    def style_type(self, state: Literal["accent1", "accent2"]):
        """Setter for highlighting the button via QSS stylesheet."""
        # Register change of state
        self._style_type = state
        self.count_label.style_type = state
        self.description_label.style_type = state
        # Update displayed style
        self.style().polish(self)


class SummaryCountWidget(CountWidget):
    def __init__(self, title: str | None = None, initial_count: int = 0, ):
        super().__init__(title=title, initial_count=initial_count)
        self.setObjectName("SummaryCountWidget")



