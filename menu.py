from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Menu(QWidget):

    def __init__(self):
        super(Menu, self).__init__()

        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(50, 140, 461, 61))
        self.label_title.setObjectName("label_title")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setText("HELP ME MAKE UP MIRROR")
        self.label_title.setStyleSheet("/* Rectangle 16 */\n"
                                                    "/* HELP ME MAKEUP MIRROR   */\n"
                                                    "position: absolute;\n"
                                                    "width: 516px;\n"
                                                    "height: 45px;\n"
                                                    "\n"
                                                    "font-family: Monaco;\n"
                                                    "font-style: normal;\n"
                                                    "font-weight: 300;\n"
                                                    "font-size: 25px;\n"
                                                    "line-height: 25px;\n"
                                                    "\n"
                                                    "color: #B7B7B7;\n")


        ##메뉴이미지
        self.label_menu = QtWidgets.QLabel(self)
        self.label_menu.setObjectName("label_menu")
        self.label_menu.resize(300, 300)
        pixmap = QPixmap("image/menu1.png")
        pixmap = pixmap.scaledToWidth(375)
        self.label_menu.setPixmap(QPixmap(pixmap))
        self.label_menu.setGeometry(QtCore.QRect(80, 200, 375, 375))


        self.pushButton_GoSelectFace = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectFace.setGeometry(QtCore.QRect(10, 590, 231, 41))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(22)
        self.pushButton_GoSelectFace.setFont(font)
        self.pushButton_GoSelectFace.setText("SELECT BY FACE")
        self.pushButton_GoSelectFace.setObjectName("pushButton_GoSelectFace")


        self.pushButton_GoSelectThema = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectThema.setGeometry(QtCore.QRect(10, 629, 231, 51))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(22)
        self.pushButton_GoSelectThema.setFont(font)
        self.pushButton_GoSelectThema.setText("SELECT BY THEMA")
        self.pushButton_GoSelectThema.setObjectName("pushButton_GoSelectThema")

        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(10, 680, 231, 51))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(22)
        self.pushButton_GoPersonalColor.setFont(font)
        self.pushButton_GoPersonalColor.setText("PERSONAL COLOR")
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")

        self.pushButton_GoFaceCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoFaceCapture.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFaceCapture.setFont(font)
        self.pushButton_GoFaceCapture.setText("BACK")
        self.pushButton_GoFaceCapture.setObjectName("pushButton_GoFaceCapture")

