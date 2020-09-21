from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
## <메모> 536 X 768 / 13 X 13
class Home(QWidget):

    def __init__(self):
        super(Home, self).__init__()


        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(110, 102, 342, 50))
        self.label_title.setObjectName("label_title")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setText("HELP ME MAKE UP MIRROR")



        ## go to main button
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(0, 150 , 562, 550))
        self.pushButton_GoMainMenu.setObjectName("pushButton_GoMainMenu")
        # ui test
        self.pushButton_GoMainMenu.setStyleSheet("border-image: url(image/logo_image.png);")


