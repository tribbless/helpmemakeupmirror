from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class RealFace_ARFace_Compare(QWidget):

    def __init__(self):
        super(RealFace_ARFace_Compare, self).__init__()

        self.label_compare = QtWidgets.QLabel(self)
        self.label_compare.setGeometry(QtCore.QRect(115, 45, 311, 81))
        self.label_compare.setObjectName("label_compare")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_compare.setFont(font)
        self.label_compare.setText("Real face와 AR face\n비교 화면")

        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(180, 610, 201, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoHome.setFont(font)
        self.pushButton_GoHome.setText("HOME")
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")

        self.pushButton_GoFrameLip = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameLip.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameLip.setFont(font)
        self.pushButton_GoFrameLip.setText("BACK")
        self.pushButton_GoFrameLip.setObjectName("pushButton_GoFrameLip")
