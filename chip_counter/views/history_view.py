from PyQt6 import QtWidgets

from chip_counter.config import CONFIG

from .view import View
from .widgets import CountBarChartWidget, CountWidget, SummaryCountWidget


class HistoryView(View):
    """View displaying the history of the daily counts."""

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)

        count_widget_layout = QtWidgets.QGridLayout()

        self.plot_widget = CountBarChartWidget()
        count_widget_layout.addWidget(self.plot_widget, 0, 0, 3, 3)

        self.blue_chips_count_widget = CountWidget(style_type="accent1")
        self.blue_chips_count_widget.set_description(CONFIG.ui.text_counter1)
        count_widget_layout.addWidget(self.blue_chips_count_widget, 3, 0)

        self.red_chips_count_widget = CountWidget(
            style_type="accent2", show_total_counts=False
        )
        self.red_chips_count_widget.set_description(CONFIG.ui.text_counter2)
        count_widget_layout.addWidget(self.red_chips_count_widget, 3, 1)

        self.all_chips_count_widget = SummaryCountWidget(show_total_counts=False)
        self.all_chips_count_widget.set_description(CONFIG.ui.text_counter_global)
        count_widget_layout.addWidget(self.all_chips_count_widget, 3, 2)

        layout.addLayout(count_widget_layout)
