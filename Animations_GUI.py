import sys
import PyQt5
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(400, 400)

        self.label = QPushButton(self)
        self.label.setGeometry(10, 10, 50, 50)
        self.label.setStyleSheet("background-color:red;border-radius:10px")
        self.label.clicked.connect(self.change)

    def change(self):
        # self.setStyleSheet("background-color:red")
        self.label.move(0, 0)
        self.anim = QPropertyAnimation(self.label, b"size")
        self.anim.setEndValue(QSize(400, 400))
        # self.anim.setDuration(500)
        self.anim.start()


app = QApplication([])

w = MainWindow()
w.show()

sys.exit(app.exec_())