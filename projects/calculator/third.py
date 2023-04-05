import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        self.setWindowTitle("Кликер")
        button_1 = QPushButton("Нажми меня 1", self)
        button_2 = QPushButton("Нажми меня 2", self)
        vbox = QVBoxLayout()
        vbox.addWidget(button_1)
        vbox.addWidget(button_2)
        self.setLayout(vbox)
        button_1.clicked.connect(self.button_was_clicked)
        button_2.clicked.connect(self.button_was_clicked)

    def button_was_clicked(self):
        sender = self.sender()
        print(sender.text())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
