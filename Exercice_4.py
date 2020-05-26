from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox, QSlider, QProgressBar

class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.txt=QLabel('4+3')
        self.ligne_1=ligne_2_boutons()
        self.ligne_1.button1.clicked.connect(self.C)
        self.ligne_1.button2.clicked.connect(self.CE)
        self.ligne_2=ligne_4_boutons('1','2','3','/')
        self.ligne_3=ligne_4_boutons('4','5','6','*')
        self.ligne_4=ligne_4_boutons('7','8','9','-')
        self.ligne_5=ligne_4_boutons('0','.','=','+')
        self.init_button(self.ligne_2)
        self.init_button(self.ligne_3)
        self.init_button(self.ligne_4)
        self.init_button(self.ligne_5)
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.txt)
        self.layout.addWidget(self.ligne_1)
        self.layout.addWidget(self.ligne_2)
        self.layout.addWidget(self.ligne_3)
        self.layout.addWidget(self.ligne_4)
        self.layout.addWidget(self.ligne_5)
        self.setLayout(self.layout)

    def init_button(self,obj):
        obj.button1.clicked.connect(self.push)
        obj.button2.clicked.connect(self.push)
        obj.button3.clicked.connect(self.push)
        obj.button4.clicked.connect(self.push)

    def push(self):
        a=self.sender()
        if a.text() == '=' :
            a=self.txt.text()
            a=eval(a)
            self.txt.setText(str(a))


        else :
            a=a.text()
            self.txt.setText(self.txt.text() + a)

        self.hide()
        self.show()
    def C(self):
        self.txt.setText('')
        self.hide()
        self.show()
    def CE(self):
        self.txt.setText(self.txt.text()[:-1])
        self.hide()
        self.show()









class ligne_2_boutons(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.button1=QPushButton('C')
        self.button2=QPushButton('CE')
        self.__layout=QHBoxLayout()
        self.__layout.addWidget(self.button1)
        self.__layout.addWidget(self.button2)
        self.setLayout(self.__layout)



class ligne_4_boutons(QWidget) :
    def __init__(self,A,B,C,D):
        QWidget.__init__(self)
        self.__a=A
        self.__b=B
        self.__c=C
        self.__d=D
        self.button1=QPushButton((A))
        self.button2=QPushButton((B))
        self.button3=QPushButton((C))
        self.button4=QPushButton(D)
        self.__layout=QHBoxLayout()
        self.__layout.addWidget(self.button1)
        self.__layout.addWidget(self.button2)
        self.__layout.addWidget(self.button3)
        self.__layout.addWidget(self.button4)
        self.setLayout(self.__layout)



    def Push1(self) :
        return self.__a
    def Push2(self):
        return self.__b
    def Push3(self):
        return self.__c
    def Push4(self):
        return self.__d


if __name__ == '__main__' :
    app=QApplication([])
    window=Window()
    window.show()
    app.exec_()
