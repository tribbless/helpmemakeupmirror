from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Personal_Color(QWidget):

    def __init__(self):
        super(Personal_Color, self).__init__()

        self.label_personalColor = QtWidgets.QLabel(self)
        self.label_personalColor.setGeometry(QtCore.QRect(140, 20, 281, 61))
        self.label_personalColor.setObjectName("label_personalColor")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_personalColor.setFont(font)
        self.label_personalColor.setText("personal color화면")

        self.pushButton_GoThema = QtWidgets.QPushButton(self)
        self.pushButton_GoThema.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoThema.setFont(font)
        self.pushButton_GoThema.setText("THEMA")
        self.pushButton_GoThema.setObjectName("pushButton_GoThema")

        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoMenu.setFont(font)
        self.pushButton_GoMenu.setText("MENU")
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")