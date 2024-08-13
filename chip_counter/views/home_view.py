from PyQt6 import QtWidgets

from chip_counter.config import CONFIG

from .view import View
from .widgets import CountWidget, SummaryCountWidget


class HomeView(View):
    """View displaying the first page of the app."""

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        count_widget_layout = QtWidgets.QGridLayout()

        self.blue_chips_count_widget = CountWidget(
            style_type="accent1", show_total_counts=False
        )
        self.blue_chips_count_widget.set_description(CONFIG.ui.text_counter1)
        count_widget_layout.addWidget(self.blue_chips_count_widget, 0, 0, 1, 2)

        self.red_chips_count_widget = CountWidget(
            style_type="accent2", show_total_counts=False
        )
        self.red_chips_count_widget.set_description(CONFIG.ui.text_counter2)
        count_widget_layout.addWidget(self.red_chips_count_widget, 0, 2, 1, 2)

        self.all_chips_count_widget = SummaryCountWidget(show_total_counts=False)
        self.all_chips_count_widget.set_description(CONFIG.ui.text_counter_global)
        count_widget_layout.addWidget(self.all_chips_count_widget, 1, 1, 1, 2)

        layout.addLayout(count_widget_layout)
