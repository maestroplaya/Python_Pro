import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLCDNumber, QHBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.lcd = QLCDNumber(self)
        self.button_0 = QPushButton("0", self)
        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)
        self.button_9 = QPushButton("9", self)
        self.button_plus = QPushButton("+", self)
        self.button_minus = QPushButton("-", self)
        self.button_mul = QPushButton("*", self)
        self.button_div = QPushButton("/", self)
        self.button_equal = QPushButton("=", self)

        self.button_0.clicked.connect(self.number_click)
        self.button_1.clicked.connect(self.number_click)
        self.button_2.clicked.connect(self.number_click)
        self.button_3.clicked.connect(self.number_click)
        self.button_4.clicked.connect(self.number_click)
        self.button_5.clicked.connect(self.number_click)
        self.button_6.clicked.connect(self.number_click)
        self.button_7.clicked.connect(self.number_click)
        self.button_8.clicked.connect(self.number_click)
        self.button_9.clicked.connect(self.number_click)

        self.button_plus.clicked.connect(self.operation_click)
        self.button_minus.clicked.connect(self.operation_click)
        self.button_mul.clicked.connect(self.operation_click)
        self.button_div.clicked.connect(self.operation_click)
        self.button_equal.clicked.connect(self.operation_click)

        self.expression = ''  # строка с арифметическим выражением
        self.number = ''  # строка с числом для вывода в QLCDNumber
        self.prev_number = ''
        self.init_ui()

    def init_ui(self):
        self.resize(250, 500)
        self.setWindowTitle("Калькулятор")
        self.lcd.setMaximumHeight(200)
        self.label.setMaximumHeight(30)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.lcd, 5)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_0)
        hbox.addWidget(self.button_1)
        hbox.addWidget(self.button_2)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_3)
        hbox.addWidget(self.button_4)
        hbox.addWidget(self.button_5)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_6)
        hbox.addWidget(self.button_7)
        hbox.addWidget(self.button_8)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_plus)
        hbox.addWidget(self.button_9)
        hbox.addWidget(self.button_minus)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_mul)
        hbox.addWidget(self.button_div)
        hbox.addWidget(self.button_equal)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def number_click(self):
        """
        Функция для обработки сигналов нажатия на кнопки с цифрами.
        """
        sender_name = self.sender().text()
        self.number += sender_name
        self.lcd.display(self.number)

    def operation_click(self):
        """
        Функция для обработки сигналов нажатия на кнопки с действиями.
        """
        sender_name = self.sender().text()
        if sender_name != '=':
            self.expression += sender_name
            self.prev_number += self.number
            self.number = ''
            self.lcd.display(self.expression)
        else:
            result = 0
            if self.expression == '+':
                result = int(self.prev_number) + int(self.number)
            elif self.expression == '-':
                result = int(self.prev_number) - int(self.number)

    def keyPressEvent(self, event):
        """
        Функция обработчик нажатия клавиши.
        """
        if event.key() == Qt.Key_Escape:
            app.closeAllWindows()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
