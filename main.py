from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(110, 110, 500, 500)
    win.setWindowTitle('sheded')

    label = QtWidgets.QLabel(win)
    label.setText('label')
    label.move(50, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText('click me')


    win.show()
    sys.exit(app.exec_())

window()