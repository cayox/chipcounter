from .controller import Controller
from chip_counter.views import MainView, HomeView, HistoryView


class MainController(Controller[MainView]):
    def __init__(self):
        super().__init__(MainView)

    def connect_view(self):
        self.ctrl_home = None
        self.view_home = HistoryView()
        self.view.stack.addWidget(self.view_home)

        self.view_home.red_chips_count_widget.set_count(200)
        self.view_home.plot_widget.update_data(200)
