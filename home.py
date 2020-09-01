from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Home(QWidget):

    def __init__(self):
        super(Home, self).__init__()

        ## 어떤화면인지 알리기 위한 label (나중에 삭제)
        self.label_home = QtWidgets.QLabel(self)
        self.label_home.setGeometry(QtCore.QRect(10, 10, 171, 61))
        self.label_home.setObjectName("label_home")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_home.setFont(font)
        self.label_home.setText("home화면")

        ## go to main button
        self.pushButton_GoFaceCatprue = QtWidgets.QPushButton(self)
        self.pushButton_GoFaceCatprue.setGeometry(QtCore.QRect(140, 230, 271, 261))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(28)
        self.pushButton_GoFaceCatprue.setText("Face Capture")
        self.pushButton_GoFaceCatprue.setFont(font)
        self.pushButton_GoFaceCatprue.setObjectName("pushButton_GoFaceCatprue")
