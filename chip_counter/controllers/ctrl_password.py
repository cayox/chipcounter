from PyQt6 import QtCore

from chip_counter.config import CONFIG
from chip_counter.controllers.controller import Controller
from chip_counter.views import PasswordView


class PasswordController(Controller[PasswordView]):
    """Controller managing the entry and safety of the password view."""

    password_correct = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__(PasswordView)

    def connect_view(self) -> None:  # noqa: D102, inherited
        self.view.password_input.textChanged.connect(self._on_password_update)

    @QtCore.pyqtSlot(str)
    def _on_password_update(self, text: str) -> None:
        if len(text) != len(CONFIG.ui.admin_password):
            return

        if text != CONFIG.ui.admin_password:
            self.show_error("Incorrect Password")
            self.view.password_input.setText("")
            return

        self.password_correct.emit()
        self.view.password_input.setText("")
