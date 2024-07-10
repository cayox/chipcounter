from PyQt6 import QtCore, QtWidgets


class PageTitle(QtWidgets.QWidget):
    def __init__(self, title: str):
        super().__init__()

        layout = QtWidgets.QHBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        title = QtWidgets.QLabel(title)
        title.setObjectName("PageTitle")
        layout.addWidget(title)
