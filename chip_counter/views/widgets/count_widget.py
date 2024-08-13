import logging
from typing import Literal

from PyQt6 import QtCore, QtWidgets

log = logging.getLogger(__name__)


class CountLabel(QtWidgets.QLabel):
    """Label to display a count in a specific style.

    Args:
        *args:
        style_type: the style to display the label in
        description_field: the description of the displayed count
        **kwargs:
    """

    def __init__(
        self,
        *args,
        style_type: Literal["accent1", "accent2"] | None = None,
        description_field: bool = False,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self.description = description_field

        self.setObjectName(self.__class__.__name__)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._style_type = ""
        self.style_type = style_type

    @QtCore.pyqtProperty(str)
    def style_type(self) -> str:
        """Getter for highlighting the button via QSS stylesheet."""
        return self._style_type

    @style_type.setter
    def style_type(self, state: Literal["accent1", "accent2"] | None) -> None:
        """Setter for highlighting the button via QSS stylesheet."""
        # Register change of state
        self._style_type = state if not self.description else f"description_{state}"
        # Update displayed style
        self.style().polish(self)


class SubCountLabel(CountLabel):
    """Countlabel with custom style."""


class CountWidget(QtWidgets.QGroupBox):
    """Widget to display a count animated in different style types.

    Args:
        title: the title of the widget
        initial_count: the initial count to display.
        style_type: the style the widget should have
        show_total_counts: whether a field should be displayed with a count including the factor.
    """

    def __init__(
        self,
        title: str | None = None,
        initial_count: int = 0,
        style_type: Literal["accent1", "accent2"] | None = None,
        show_total_counts: bool = True,
    ):
        super().__init__()
        self.setObjectName("CountWidget")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        self.count_label = CountLabel(str(initial_count), style_type=style_type)
        layout.addWidget(self.count_label)

        self.total_counts_label = SubCountLabel("[0]", style_type=style_type)
        layout.addWidget(self.total_counts_label)
        self.total_counts_label.setVisible(show_total_counts)
        layout.addStretch()

        self.description_label = CountLabel("Description", description_field=True)
        layout.addWidget(self.description_label)

        self.setMaximumHeight(256)

        # Initialize the timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._update_count_animated)

        self.target_count = 0
        self.current_count = 0
        self.increment = 1
        self.fixed_count_up_time = 1000  # in milliseconds

        if title is not None:
            self.setTitle(title)

        self._style_type = ""

        self.style_type = style_type

    def set_count(self, count: int) -> None:
        """Method to set the count value of the widget animated."""
        log.debug("Setting counts to %s", count)
        self.target_count = int(count)
        counts = count - int(self.count_label.text())

        if not counts:
            return

        interval = int(self.fixed_count_up_time // counts)

        self.timer.start(abs(interval))

    def set_description(self, desc: str) -> None:
        """Method to set the description text."""
        self.description_label.setText(desc)

    def _update_count_animated(self) -> None:
        current_count = int(self.count_label.text())
        if current_count < self.target_count:
            current_count += self.increment
            self.count_label.setText(str(current_count))
        elif current_count > self.target_count:
            current_count -= self.increment
            self.count_label.setText(str(current_count))
        else:
            self.timer.stop()

    def set_total_counts(self, counts: int) -> None:
        """Method to set the total counts amount."""
        self.total_counts_label.setText(f"[{int(counts)}]")

    @QtCore.pyqtProperty(str)
    def style_type(self) -> str:
        """Getter for highlighting the button via QSS stylesheet."""
        return self._style_type

    @style_type.setter
    def style_type(self, state: Literal["accent1", "accent2"]) -> None:
        """Setter for highlighting the button via QSS stylesheet."""
        # Register change of state
        self._style_type = state
        self.count_label.style_type = state
        self.description_label.style_type = state
        # Update displayed style
        self.style().polish(self)


class SummaryCountWidget(CountWidget):
    """Method to display the summary counts in a widget."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName("SummaryCountWidget")
