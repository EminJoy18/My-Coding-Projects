import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 420, 590)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('calculator.png'))
        self.setStyleSheet("background-color:black;border-radius:35px;font-size:30px;color:white;font:Arial")

        self.text = " "

        self.input = QLabel(self)
        self.input.setGeometry(40, 10, 340, 80)
        self.input.setStyleSheet("background-color:transparent;border-radius:0px")
        self.input.setAlignment(Qt.AlignBaseline)
        self.input.setWordWrap(True)
        # self.output.setAlignment(Qt.AlignRight)

        self.output = QLabel(self)
        self.output.setGeometry(40, 90, 340, 30)
        self.output.setStyleSheet("background-color:transparent;border-radius:0px;font-size:24px")
        self.output.setAlignment(Qt.AlignRight)

        self.cl = QPushButton(self)
        self.cl.setGeometry(40, 140, 70, 70)
        self.cl.setStyleSheet("background-color:grey")
        self.cl.setText("C")
        self.cl.setShortcut(Qt.Key_C)
        self.cl.setToolTip("Clear the screen")
        self.cl.clicked.connect(self.clear)

        self.perc = QPushButton(self)
        self.perc.setGeometry(130, 140, 70, 70)
        self.perc.setStyleSheet("background-color:grey")
        self.perc.setText("%")
        self.perc.clicked.connect(self.pressed)

        self.b = QPushButton(self)
        self.b.setGeometry(220, 140, 70, 70)
        self.b.setStyleSheet("background-color:grey")
        self.b.setIcon(QIcon('backspace.png'))
        self.b.setIconSize(QSize(30, 30))
        self.b.clicked.connect(self.backspace)

        self.div = QPushButton(self)
        self.div.setGeometry(310, 140, 70, 70)
        self.div.setStyleSheet("background-color:grey")
        self.div.setIcon(QIcon('divide.png'))
        self.div.setIconSize(QSize(25, 25))
        self.div.clicked.connect(self.divide)

        self.seven = QPushButton(self)
        self.seven.setGeometry(40, 230, 70, 70)
        self.seven.setStyleSheet("background-color:#2d3138")
        self.seven.setText("7")
        self.seven.clicked.connect(self.pressed)

        self.eight = QPushButton(self)
        self.eight.setGeometry(130, 230, 70, 70)
        self.eight.setStyleSheet("background-color:#2d3138")
        self.eight.setText("8")
        self.eight.clicked.connect(self.pressed)

        self.nine = QPushButton(self)
        self.nine.setGeometry(220, 230, 70, 70)
        self.nine.setStyleSheet("background-color:#2d3138")
        self.nine.setText("9")
        self.nine.setShortcut(Qt.Key_9)
        self.nine.clicked.connect(self.pressed)

        self.mu = QPushButton(self)
        self.mu.setGeometry(310, 230, 70, 70)
        self.mu.setStyleSheet("background-color:grey")
        self.mu.setIcon(QIcon('crossed.png'))
        self.mu.setIconSize(QSize(25, 25))
        self.mu.clicked.connect(self.multiply)

        self.four = QPushButton(self)
        self.four.setGeometry(40, 320, 70, 70)
        self.four.setStyleSheet("background-color:#2d3138")
        self.four.setText("4")
        self.four.clicked.connect(self.pressed)

        self.five = QPushButton(self)
        self.five.setGeometry(130, 320, 70, 70)
        self.five.setStyleSheet("background-color:#2d3138")
        self.five.setText("5")
        self.five.clicked.connect(self.pressed)

        self.six = QPushButton(self)
        self.six.setGeometry(220, 320, 70, 70)
        self.six.setStyleSheet("background-color:#2d3138")
        self.six.setText("6")
        self.six.clicked.connect(self.pressed)

        self.sub = QPushButton(self)
        self.sub.setGeometry(310, 320, 70, 70)
        self.sub.setStyleSheet("background-color:grey")
        self.sub.setText('-')
        self.sub.clicked.connect(self.subtract)

        self.one = QPushButton(self)
        self.one.setGeometry(40, 410, 70, 70)
        self.one.setStyleSheet("background-color:#2d3138")
        self.one.setText("1")
        self.one.clicked.connect(self.pressed)

        self.two = QPushButton(self)
        self.two.setGeometry(130, 410, 70, 70)
        self.two.setStyleSheet("background-color:#2d3138")
        self.two.setText("2")
        self.two.clicked.connect(self.pressed)

        self.three = QPushButton(self)
        self.three.setGeometry(220, 410, 70, 70)
        self.three.setStyleSheet("background-color:#2d3138")
        self.three.setText("3")
        self.three.clicked.connect(self.pressed)

        self.add = QPushButton(self)
        self.add.setGeometry(310, 410, 70, 70)
        self.add.setStyleSheet("background-color:grey")
        self.add.setIcon(QIcon('plus.png'))
        self.add.setIconSize(QSize(35, 35))
        self.add.clicked.connect(self.addition)

        self.zeroz = QPushButton(self)
        self.zeroz.setGeometry(40, 500, 70, 70)
        self.zeroz.setStyleSheet("background-color:#2d3138")
        self.zeroz.setText("00")
        self.zeroz.clicked.connect(self.pressed)

        self.zero = QPushButton(self)
        self.zero.setGeometry(130, 500, 70, 70)
        self.zero.setStyleSheet("background-color:#2d3138")
        self.zero.setText("0")
        self.zero.clicked.connect(self.pressed)

        self.dec = QPushButton(self)
        self.dec.setGeometry(220, 500, 70, 70)
        self.dec.setStyleSheet("background-color:#2d3138")
        self.dec.setText(".")
        self.dec.clicked.connect(self.pressed)

        self.eq = QPushButton(self)
        self.eq.setGeometry(310, 500, 70, 70)
        self.eq.setText("=")
        self.eq.setStyleSheet("background-color:#26bcc9")
        # adding equal button a color effect
        # self.c_effect = QGraphicsColorizeEffect(self)
        # self.c_effect.setColor(Qt.red)
        # self.eq.setGraphicsEffect(self.c_effect)
        self.eq.clicked.connect(self.equal)


    def pressed(self):
        self.text = self.input.text()
        self.input.setText(self.text + (self.sender().text()))

    def divide(self):
        self.text = self.input.text()
        self.input.setText(self.text + '/')

    def multiply(self):
        self.text = self.input.text()
        self.input.setText(self.text + '*')

    def subtract(self):
        self.text = self.input.text()
        self.input.setText(self.text + '-')

    def addition(self):
        self.text = self.input.text()
        self.input.setText(self.text + '+')

    def equal(self):
        res = float(eval(self.input.text()))
        if int(res) == res:
            self.output.setText(str(int(res)))
        else:
            self.output.setText(str(res))

    def clear(self):
        self.output.clear()
        self.input.clear()

    def backspace(self):
        self.input.setText(self.input.text()[0:len(self.input.text())-1])

    # for keyboard input
    def keyPressEvent(self, e):
        # if e.key() == Qt.Key_9:
        #     self.text = self.input.text()
        #     self.input.setText(self.text + '9')

        if e.key() == Qt.Key_8:
            self.text = self.input.text()
            self.input.setText(self.text + '8')

        elif e.key() == Qt.Key_7:
            self.text = self.input.text()
            self.input.setText(self.text + '7')

        elif e.key() == Qt.Key_6:
            self.text = self.input.text()
            self.input.setText(self.text + '6')

        elif e.key() == Qt.Key_5:
            self.text = self.input.text()
            self.input.setText(self.text + '5')

        elif e.key() == Qt.Key_4:
            self.text = self.input.text()
            self.input.setText(self.text + '4')

        elif e.key() == Qt.Key_3:
            self.text = self.input.text()
            self.input.setText(self.text + '3')

        elif e.key() == Qt.Key_2:
            self.text = self.input.text()
            self.input.setText(self.text + '2')

        elif e.key() == Qt.Key_1:
            self.text = self.input.text()
            self.input.setText(self.text + '1')

        elif e.key() == Qt.Key_Plus:
            self.text = self.input.text()
            self.input.setText(self.text + '+')

        elif e.key() == Qt.Key_Minus:
            self.text = self.input.text()
            self.input.setText(self.text + '-')

        elif e.key() == Qt.Key_Backslash:
            self.text = self.input.text()
            self.input.setText(self.text + '/')

        elif e.key() == Qt.Key_multiply:
            self.text = self.input.text()
            self.input.setText(self.text + '*')

        elif e.key() == Qt.Key_Enter:
            self.equal()

        elif e.key() == Qt.Key_Backspace:
            self.backspace()

        elif e.key() == Qt.Key_F4:
            self.close()


if __name__=="__main__":
    app = QApplication([])

    window = Calculator()
    window.show()

    sys.exit(app.exec_())
