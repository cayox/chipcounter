import configparser
import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, Qt
import pyqtgraph as pg
import pandas as pd
from chip_counter.config import CONFIG


class CountBarChartWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zählverlauf")

        # Set up the plot widget
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground(CONFIG.colors.background_color)
        self.plot_widget.setLabel("left", "Chips")
        self.plot_widget.setLabel("bottom", "Hours", units="h")

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

    def animate_on_show(self):
        self.animation_step = 0
        self.timer.start(50)  # Update every 50 milliseconds

    def update_animation(self):
        if self.animation_step < len(self.counts):
            self.bar_item.setOpts(
                height=self.counts * (self.animation_step / len(self.counts))
            )
            self.animation_step += 1
        else:
            self.timer.stop()

    def update_data(self, dataframe: pd.DataFrame):
        if isinstance(dataframe, pd.DataFrame) and dataframe.shape[0] == 24:
            self.counts = dataframe["summary"].values
            self.animate_on_show()
        else:
            raise ValueError(
                "Dataframe must have exactly 24 rows representing counts for each hour."
            )
