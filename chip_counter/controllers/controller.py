import logging
from typing import Generic, TypeVar

from PyQt6 import QtCore, QtWidgets


V = TypeVar("V")


class Controller(QtCore.QObject, Generic[V]):
    """Base class for a controller."""

    def __init__(self, view_class: type[V]):
        super().__init__()

        self._view = view_class()

        self.connect_view()

    @property
    def view(self) -> V:
        """Method to retrieve the managed view."""
        return self._view

    def show_error(self, text: str):
        """Method to show `text` in an error messagebox."""
        logging.error("Displaying error: %s", text)
        QtWidgets.QMessageBox.critical(self.view, "Error", text)

    def connect_view(self):
        """Method that is called upon initialization to connect the controller to its view."""
        raise NotImplementedError
