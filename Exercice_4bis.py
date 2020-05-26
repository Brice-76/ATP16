from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox, QSlider, QProgressBar,QGridLayout

class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.layout=QGridLayout()
        self.__Button0=QPushButton('0')
        self.__Button1=QPushButton('1')
        self.__Button2=QPushButton('2')

        self.__Button3=QPushButton('3')
        self.__Button4=QPushButton('4')
        self.__Button5=QPushButton('5')
        self.__Button6=QPushButton('6')
        self.__Button7=QPushButton('7')
        self.__Button8=QPushButton('8')
        self.__Button9=QPushButton('9')
        self.__plus=QPushButton('+')
        self.__moins=QPushButton('-')
        self.__egal=QPushButton('=')
        self.__div=QPushButton('/')
        self.__fois=QPushButton('*')
        self.__pt=QPushButton('.')
        self.__c=QPushButton('C')
        self.__ce=QPushButton('CE')
        self.__label=QLabel('bvn')

        self.layout.addWidget(self.__label,0,0,1,4)
        self.layout.addWidget(self.__ce,1,0,1,2)
        self.layout.addWidget(self.__c,1,2,1,2)
        self.layout.addWidget(self.__Button1,2,0)
        self.layout.addWidget(self.__Button2,2,1)
        self.layout.addWidget(self.__Button3,2,2)
        self.layout.addWidget(self.__div,2,3)
        self.layout.addWidget(self.__Button4,3,0)
        self.layout.addWidget(self.__Button5,3,1)
        self.layout.addWidget(self.__Button6,3,2)
        self.layout.addWidget(self.__fois,3,3)
        self.layout.addWidget(self.__Button7,4,0)
        self.layout.addWidget(self.__Button8,4,1)
        self.layout.addWidget(self.__Button9,4,2)
        self.layout.addWidget(self.__moins,4,3)
        self.layout.addWidget(self.__Button0,5,0)
        self.layout.addWidget(self.__pt,5,1)
        self.layout.addWidget(self.__egal,5,2)
        self.layout.addWidget(self.__plus,5,3)



        self.setLayout(self.layout)
        self.show()







if __name__ == '__main__' :
    app=QApplication([])
    window=Window()
    window.show()
    app.exec_()
