import numpy as np
import pandas as pd
import pyqtgraph as pg
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from chip_counter.config import CONFIG

HOURS_IN_DAY = 24


class CountBarChartWidget(QWidget):
    """Widget to display daily counts in a bar chart hourly."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zählverlauf")

        # Set up the plot widget
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground(CONFIG.colors.background_color)
        self.plot_widget.setLabel("left", "Chips")
        self.plot_widget.setLabel("bottom", "Stunden", units="h")

        # Disable interactivity
        self.plot_widget.setMouseEnabled(x=False, y=False)
        self.plot_widget.hideButtons()

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        # Initialize data for the bar chart
        self.hours = np.arange(24)
        self.counts = np.zeros(24)

        # Create the bar chart item
        self.bar_item = pg.BarGraphItem(
            x=self.hours, height=self.counts, width=0.8, brush=CONFIG.colors.accent1
        )
        self.plot_widget.addItem(self.bar_item)

        # Set up the timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.animation_step = 0

    def animate_on_show(self) -> None:
        """Start the animation when showing the plot widget."""
        self.animation_step = 0
        self.timer.start(50)  # Update every 50 milliseconds

    def update_animation(self) -> None:
        """Method to update the counting animation."""
        if not self.counts.any():
            self.timer.stop()
            return

        if self.animation_step < len(self.counts):
            self.bar_item.setOpts(
                height=self.counts * (self.animation_step / len(self.counts))
            )
            self.animation_step += 1
        else:
            self.timer.stop()

    def update_data(self, dataframe: pd.DataFrame) -> None:
        """Method to set new data for the plot to display.

        Args:
            dataframe: the new data to display
        """
        if isinstance(dataframe, pd.DataFrame) and dataframe.shape[0] == HOURS_IN_DAY:
            self.counts = dataframe["summary"].values
            self.animate_on_show()
        else:
            raise ValueError(
                "Dataframe must have exactly 24 rows representing counts for each hour."
            )
