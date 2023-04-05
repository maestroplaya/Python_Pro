import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLCDNumber


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        self.setWindowTitle("Кликер")
        plus_button = QPushButton("+1", self)
        to_null_button = QPushButton("to 0", self)
        self.lcd = QLCDNumber(self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(plus_button)
        vbox.addWidget(to_null_button)
        self.setLayout(vbox)
        plus_button.clicked.connect(self.button_was_clicked)
        to_null_button.clicked.connect(self.button_was_clicked)
        self.count = 0

    def button_was_clicked(self):
        sender = self.sender()
        if sender.text() == "+1":
            self.count += 1
        elif sender.text() == "to 0":
            self.count = 0
        self.lcd.display(self.count)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            app.closeAllWindows()
        elif event.key() == Qt.Key_1:
            self.count += 1
        elif event.key() == Qt.Key_2:
            self.count -= 1
        self.lcd.display(self.count)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
