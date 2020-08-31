from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Menu(QWidget):

    def __init__(self):
        super(Menu, self).__init__()

        self.label_menu = QtWidgets.QLabel(self)
        self.label_menu.setGeometry(QtCore.QRect(10, 10, 181, 61))
        self.label_menu.setObjectName("label_menu")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_menu.setFont(font)
        self.label_menu.setText("menu화면")



        self.pushButton_GoSelectFace = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectFace.setGeometry(QtCore.QRect(130, 210, 300, 100))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(22)
        self.pushButton_GoSelectFace.setFont(font)
        self.pushButton_GoSelectFace.setText("SELECT BY FACE")
        self.pushButton_GoSelectFace.setObjectName("pushButton_GoSelectFace")


        self.pushButton_GoSelectThema = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectThema.setGeometry(QtCore.QRect(130, 310, 300, 100))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(22)
        self.pushButton_GoSelectThema.setFont(font)
        self.pushButton_GoSelectThema.setText("SELECT BY THEMA")
        self.pushButton_GoSelectThema.setObjectName("pushButton_GoSelectThema")

        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(130, 410, 300, 100))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(22)
        self.pushButton_GoPersonalColor.setFont(font)
        self.pushButton_GoPersonalColor.setText("PERSONAL COLOR")
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")
