from PyQt6 import QtCore, QtWidgets

from chip_counter.views.view import View
from chip_counter.views.widgets import TitleLabel


class PasswordButton(QtWidgets.QPushButton):
    """Button with custom style to enter the password."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName("PasswordButton")


class PasswordView(View):
    """View to display the password page."""

    def _build_ui(self) -> None:
        layout = QtWidgets.QGridLayout(self)
        layout.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        max_cols = 3

        title = TitleLabel("Enter Password")
        layout.addWidget(title, 0, 0, 1, max_cols)

        password_hbox = QtWidgets.QHBoxLayout()

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setReadOnly(True)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        password_hbox.addWidget(self.password_input)

        self.button_reset_input = PasswordButton("Delete")
        self.button_reset_input.clicked.connect(
            lambda *_: self.password_input.setText("")
        )
        password_hbox.addWidget(self.button_reset_input)

        layout.addLayout(password_hbox, 1, 0, 1, max_cols)

        self.buttons = []
        for i in range(1, 10):
            btn = PasswordButton(str(i))
            btn.clicked.connect(self._add_password_char)
            self.buttons.append(btn)
            layout.addWidget(btn, ((i - 1) // 3) + 2, (i - 1) % 3)

        btn = PasswordButton("0")
        btn.clicked.connect(self._add_password_char)
        layout.addWidget(btn, 5, 0, 1, 3)

    @QtCore.pyqtSlot()
    def _add_password_char(self) -> None:
        sender: PasswordButton = self.sender()
        self.password_input.setText(self.password_input.text() + sender.text())
