from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Select_Thema(QWidget):

    def __init__(self):
        super(Select_Thema, self).__init__()

        self.label_thema = QtWidgets.QLabel(self)
        self.label_thema.setGeometry(QtCore.QRect(10, 20, 271, 61))
        self.label_thema.setObjectName("label_thema")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_thema.setFont(font)
        self.label_thema.setText("select_thema화면")

        self.pushButton_GoFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoFrame.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrame.setFont(font)
        self.pushButton_GoFrame.setText("FRAME")
        self.pushButton_GoFrame.setObjectName("pushButton_GoFrame")