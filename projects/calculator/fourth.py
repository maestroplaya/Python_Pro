import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        self.setWindowTitle("Кликер")
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def mousePressEvent(self, event):
        self.label.setText(f'{event.x()}, {event.y()}')

    def keyPressEvent(self, event):
        self.label.setText(event.text())
        print(event.key())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
