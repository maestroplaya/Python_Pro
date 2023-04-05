import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        self.setWindowTitle("Ввод текста")
        label = QLabel()
        line_edit = QLineEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(line_edit)
        self.setLayout(vbox)
        line_edit.textChanged.connect(label.setText)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
