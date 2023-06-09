import sys
import PyQt5
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 250)
        self.setWindowTitle("Distance Converter")
        self.setStyleSheet("background-color:black;border-radius:20px")
        self.setWindowIcon(QIcon('repost.png'))

        self.inp = QLineEdit(self)
        self.button = QPushButton(self)
        self.mile = QLabel(self)

        self.button1 = QPushButton(self)
        self.button1.setGeometry(0, 0, 400, 80)
        self.button1.setText("Km -> mile")
        self.button1.setStyleSheet("QPushButton"
                                   "{"
            "border:5px solid orange;color:white;font:Helvetica;font-size:24px;"
                                   "}"
                                   "QPushButton:pressed"
                                   "{"
                                   "background-color:orange"
                                   "}")

        self.button2 = QPushButton(self)
        self.button2.setGeometry(400, 0, 400, 80)
        self.button2.setText("Mile -> Km")
        self.button2.setStyleSheet("QPushButton"
                                   "{"
                                   "border:5px solid orange;color:white;font:Helvetica;font-size:24px;"
                                   "}"
                                   "QPushButton:pressed"
                                   "{"
                                   "background-color:orange"
                                   "}")

        self.bg = QButtonGroup(self)
        self.bg.addButton(self.button1)
        self.bg.addButton(self.button2)

        self.button1.clicked.connect(self.btn1func)
        self.button2.clicked.connect(self.btn2func)

    def btn1func(self):
        self.inp.clear()
        self.inp.setGeometry(80, 100, 500, 50)
        self.inp.setStyleSheet("background-color:white;\n"
                               "border-radius:10px;\n"
                               "font-size:24px;\n"
                               "font:Helvetica")
        self.inp.setPlaceholderText("Enter the kilometers")

        self.button.setText("Convert")
        self.button.setGeometry(600, 100, 150, 50)
        self.button.setStyleSheet("background-color:orange;\n"
                                  "color:white;\n"
                                  "font-size:24px;\n"
                                  "font-weight:bold;\n"
                                  "border-radius:10px")
        self.button.clicked.connect(self.convertkm)

        self.mile.setGeometry(300, 170, 150, 70)
        self.mile.setStyleSheet("background-color:white;\n"
                                  "color:black;\n"
                                  "font-size:24px;\n"
                                  "font-weight:bold;\n"
                                  "border-radius:10px")
        self.mile.setAlignment(Qt.AlignCenter)

    def btn2func(self):
        self.inp.clear()
        self.inp.setGeometry(80, 100, 500, 50)
        self.inp.setStyleSheet("background-color:white;\n"
                               "border-radius:10px;\n"
                               "font-size:24px;\n"
                               "font:Helvetica")
        self.inp.setPlaceholderText("Enter the miles")

        self.button.setText("Convert")
        self.button.setGeometry(600, 100, 150, 50)
        self.button.setStyleSheet("background-color:orange;\n"
                                  "color:white;\n"
                                  "font-size:24px;\n"
                                  "font-weight:bold;\n"
                                  "border-radius:10px")
        self.button.clicked.connect(self.convertmk)

        self.mile.setGeometry(300, 170, 150, 70)
        self.mile.setStyleSheet("background-color:white;\n"
                                  "color:black;\n"
                                  "font-size:24px;\n"
                                  "font-weight:bold;\n"
                                  "border-radius:10px")
        self.mile.setAlignment(Qt.AlignCenter)

    def convertkm(self):
        n = float(self.inp.text())
        m = (n/1.609).__round__(3)
        self.mile.setText(str(m))

    def convertmk(self):
        n = float(self.inp.text())
        m = (n*1.609).__round__(3)
        self.mile.setText(str(m))


# convapp = QApplication([])
# convapp.setApplicationName('Utility Apps')
#
# window = ConverterApp()
# window.show()
#
# sys.exit(convapp.exec_())
