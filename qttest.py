import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Awooga", "Bazinga", "Poggers", "Cringe"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("UwU", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())