from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog,QDialogButtonBox, QSlider, QProgressBar


class Window(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500,300)
        self.__layout=QHBoxLayout()
        self.__progress_bar=QProgressBar()
        self.__slider=QSlider()
        self.__layout.addWidget(self.__progress_bar)
        self.__layout.addWidget(self.__slider)
        self.__slider.valueChanged.connect(self.Signal)
        self.setLayout(self.__layout)

    def Signal(self):
        self.Slot(self.__slider.value())
        self.hide()
        self.show()
    def Slot(self,value):
        self.__progress_bar.setValue(self.__slider.value())




if __name__ == '__main__' :
    app=QApplication([])
    window=Window()
    window.show()
    app.exec_()
