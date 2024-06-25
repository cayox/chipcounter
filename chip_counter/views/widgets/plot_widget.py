import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, Qt
import pyqtgraph as pg

class CountBarChartWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zählverlauf")

        # Set up the plot widget
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.setLabel('left', 'Counts')
        self.plot_widget.setLabel('bottom', 'Hours', units='h')

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        # Initialize data for the bar chart
        self.hours = np.arange(24)
        self.counts = np.zeros(24)

        # Create the bar chart item
        self.bar_item = pg.BarGraphItem(x=self.hours, height=self.counts, width=0.8, brush='b')
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
            self.bar_item.setOpts(height=self.counts * (self.animation_step / len(self.counts)))
            self.animation_step += 1
        else:
            self.timer.stop()

    def update_data(self, new_counts):
        self.counts = new_counts
        self.animate_on_show()