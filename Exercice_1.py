from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox
from random import *

class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500,300)
        self.__layout=QVBoxLayout()
        self.__button=QPushButton('changer le cycle')
        self.__label=QLabel()
        self.lst= ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        self.__button.clicked.connect(self.Push)
        self.__layout.addWidget(self.__label)
        self.__layout.addWidget(self.__button)
        self.setLayout(self.__layout)

    def Push(self):
        print('push')
        self.__label.setText(choice(self.lst))
        self.hide()
        self.show()




if __name__ == '__main__' :
    app=QApplication([])
    window=Window()
    window.show()
    app.exec_()
