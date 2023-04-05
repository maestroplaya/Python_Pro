import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QToolBar


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(800, 400)
        self.centralWidget = QLabel("彡彡◦༄◦°˚°◦.¸¸◦°´ *•.¸♥")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createMenuBar()
        self._createToolBars()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("File", self)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("Edit")
        helpMenu = menuBar.addMenu("Help")

    def _createToolBars(self):
        fileToolBar = self.addToolBar("File")
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())