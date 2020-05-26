from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox, QSlider, QProgressBar

class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500,300)
        self.__button=QPushButton('Changer mon texte ...')
        self.__text_edit=QTextEdit()
        self.__layout=QVBoxLayout()
        self.__button.clicked.connect(self.Push)
        self.__nbre=0
        self.__layout.addWidget(self.__button)
        self.__layout.addWidget(self.__text_edit)
        self.setLayout(self.__layout)


    def Push(self):
        self.__nbre+=1
        self.__button.setText('Clic '+str(self.__nbre))
        self.__text_edit.setText('Clic '+str(self.__nbre))
        self.hide()
        self.show()


if __name__ == '__main__' :
    app=QApplication([])
    window=Window()
    window.show()
    app.exec_()
pyinstaller --name="MyApplication2" --windowed --onefile Exercice_1.py
pyinstaller --name="MyApplication" --windowed Exercice_1.py
