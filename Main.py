from sympy import *
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

x = Symbol('x')


class Ui_Bisection(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 981, 771))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.880682, x2:1, y2:1, stop:0 rgba(195, 20, 50, 255), stop:1 rgba(36, 11, 54, 255));}")
        self.widget.setObjectName("widget")
        self.heading = QtWidgets.QLabel(self.widget)
        self.heading.setGeometry(QtCore.QRect(0, 10, 871, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.heading.setFont(font)
        self.heading.setStyleSheet("color:white\n"
"")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white\n"
"")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 110, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#ffbfcf\n"
"")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#ffbfcf\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#ffbfcf\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 521, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#ffbfcf\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white\n"
"")
        self.label_6.setObjectName("label_6")
        self.inputText = QtWidgets.QLineEdit(self.widget)
        self.inputText.setGeometry(QtCore.QRect(40, 230, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputText.setFont(font)
        self.inputText.setObjectName("inputText")
        self.outputText = QtWidgets.QTextBrowser(self.widget)
        self.outputText.setGeometry(QtCore.QRect(40, 410, 811, 341))
        self.outputText.setObjectName("outputText")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 380, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white\n"
"")
        self.label_7.setObjectName("label_7")
        self.solve_button = QtWidgets.QPushButton(self.widget, clicked=lambda: self.press_it())
        self.solve_button.setGeometry(QtCore.QRect(340, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        self.solve_button.setFont(font)
        self.solve_button.setStyleSheet("QPushButton{\n"
"color:#ffbfcf;\n"
"border-radius:20px;\n"
"border:2px solid #fff;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #fff;\n"
"  color: #000;\n"
"   cursor: pointer;\n"
"}\n"
"\n"
"")
        self.solve_button.setObjectName("solve_button")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white\n"
"")
        self.label_8.setObjectName("label_8")
        self.inputText_2 = QtWidgets.QLineEdit(self.widget)
        self.inputText_2.setGeometry(QtCore.QRect(230, 270, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.inputText_2.setFont(font)
        self.inputText_2.setObjectName("inputText_2")
        self.inputText_3 = QtWidgets.QLineEdit(self.widget)
        self.inputText_3.setGeometry(QtCore.QRect(230, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.inputText_3.setFont(font)
        self.inputText_3.setObjectName("inputText_3")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(40, 300, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white\n"
"")
        self.label_9.setObjectName("label_9")
        self.inputText_4 = QtWidgets.QLineEdit(self.widget)
        self.inputText_4.setGeometry(QtCore.QRect(580, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.inputText_4.setFont(font)
        self.inputText_4.setObjectName("inputText_4")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(380, 280, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white\n"
"")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self):
        s = ''
        self.outputText.setText(s)
        expression = sympify(self.inputText.text())

        try:
            a = float(self.inputText_2.text())
        except ValueError:
            s += 'Invalid Lower Bound'
            self.outputText.setText(s)

        try:
            b = float(self.inputText_3.text())
        except ValueError:
            s += 'Invalid Upper Bound'
            self.outputText.setText(s)
        eps = 10E-6

        try:
            maxiter = int(self.inputText_4.text())
        except ValueError:
            s += 'Invalid Max Iterations'
            self.outputText.setText(s)

        def f(z):
            return expression.subs(x, z)

        if f(a) * f(b) > 0:
            s += 'The given guesses do not bracket the root.'
            self.outputText.setText(s)
            print(s)
            return

        s += '-'*200
        s += '\n  iteration \t\t a \t\t b \t\t c \t\t f(c)        \n'
        s += '-'*200
        self.outputText.setText(s)

        for i in range(maxiter):
            # Calculate the value of the root at the ith step
            c = (a + b) / 2

            # Print some values for the table
            a = round(a, 8)
            b = round(b, 8)
            c = round(c, 8)
            temp = round(f(c), 8)
            s += '\n'
            s += str(i + 1) + f'\t\t{a}\t\t{b}\t\t{c}\t\t{temp}\t'
            # print(str(i + 1) + '\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' % (a, b, c, f(c)))

            # Check if the root has been found with acceptable error or not?
            if np.abs(f(c)) < eps:
                s += '\n'
                s += '-'*200
                s += 'Root found : ' + str(c)
                self.outputText.setText(s)
                return
            # Check whether the root lies between a and c
            if f(a) * f(c) < 0:
                # Change the upper bound
                b = c
            else:  # The root lies between c and b
                # Change the lower bound
                a = c

        s += '\n'
        s += '-' * 200
        self.outputText.setText(s)
        if i == maxiter - 1:
            s += '\n\nMax iterations reached!'
            s += '\nApproximaiton to the Root after max iterations is : ' + str(c)
            self.outputText.setText(s)
            return

        print(expression)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BisectionMethod"))
        self.heading.setText(_translate("MainWindow", "BISECTION METHOD"))
        self.label_2.setText(_translate("MainWindow", "INSTRUCTIONS:"))
        self.label.setText(_translate("MainWindow", "1. For using powers \'^\' this cannot be used for 3^4 it should be written 3**4"))
        self.label_3.setText(_translate("MainWindow", "2. For using exponential equations e^x should be written as exp(x)"))
        self.label_4.setText(_translate("MainWindow", "3. 8x should be written as 8*x"))
        self.label_5.setText(_translate("MainWindow", "4. Every equation will by default be equated to 0 "))
        self.label_6.setText(_translate("MainWindow", "Enter the equation below in terms of x only :"))
        self.label_7.setText(_translate("MainWindow", "Output :"))
        self.solve_button.setText(_translate("MainWindow", "Solve"))
        self.label_8.setText(_translate("MainWindow", "Enter Lower Bound Guess:"))
        self.label_9.setText(_translate("MainWindow", "Enter Upper Bound Guess:"))
        self.label_10.setText(_translate("MainWindow", "Max. Number of Iterations:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Bisection()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
