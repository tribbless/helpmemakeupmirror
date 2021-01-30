from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Sub_Menu(QWidget):

    def __init__(self):
        super(Sub_Menu, self).__init__()

        # 메뉴 background image
        self.label_SubMenu = QtWidgets.QLabel(self)
        self.label_SubMenu.setGeometry(QtCore.QRect(273, 378, 478, 454))
        self.label_SubMenu.setObjectName("label_SubMenu")
        self.label_SubMenu.setStyleSheet("border-image: url(image/btn_select.png);")


        # 이동 버튼 (->가상화장, 테마)
        self.pushButton_GoSelectFace = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectFace.setGeometry(QtCore.QRect(295, 398, 435, 198))
        self.pushButton_GoSelectFace.setStyleSheet('background-color: transparent;'
                                                   'border-top-left-radius :198px; border-top-right-radius:198px')
        self.pushButton_GoSelectFace.setObjectName("pushButton_GoSelectFace")

        self.pushButton_GoSelectThema = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectThema.setGeometry(QtCore.QRect(295, 615, 435, 198))
        self.pushButton_GoSelectThema.setStyleSheet('background-color: transparent;'
                                                    'border-bottom-left-radius:194px; border-bottom-right-radius:194px')
        self.pushButton_GoSelectThema.setObjectName("pushButton_GoSelectThema")

        # 이동 버튼 image
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(25, 22, 45, 45))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("border-image: url(image/btn_back.png);")

        ## 이동 버튼 (previous)
        self.pushButton_GoMakeupFaceCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoMakeupFaceCapture.setGeometry(QtCore.QRect(23, 9, 55, 72))
        self.pushButton_GoMakeupFaceCapture.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                          "border-radius: 10px;")
        self.pushButton_GoMakeupFaceCapture.setObjectName("pushButton_GoMakeupFaceCapture")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")


        ## 혹시 몰라 지우지 않았습니다.
        '''
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
        '''





