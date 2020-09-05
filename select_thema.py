from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Select_Thema(QWidget):

    def __init__(self):
        super(Select_Thema, self).__init__()

        self.label_thema = QtWidgets.QLabel(self)
        self.label_thema.setGeometry(QtCore.QRect(160, 10, 241, 40))
        self.label_thema.setObjectName("label_thema")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_thema.setFont(font)
        self.label_thema.setText("select_thema")

        #이미지
        self.label_select = QtWidgets.QLabel(self)
        self.label_select.setGeometry(QtCore.QRect(5, 510, 526, 260))
        self.label_select.setObjectName("label_select")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_select.setFont(font)
        self.label_select.setStyleSheet('background:yellow')
        self.label_select.setText("나는 이미지")

        self.pushButton_GoFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoFrame.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrame.setFont(font)
        self.pushButton_GoFrame.setText("FRAME")
        self.pushButton_GoFrame.setObjectName("pushButton_GoFrame")

        self.pushButton_GoSelectCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectCapture.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoSelectCapture.setFont(font)
        self.pushButton_GoSelectCapture.setText("BACK")
        self.pushButton_GoSelectCapture.setObjectName("pushButton_GoSelectCapture")