from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Sub_Menu(QWidget):

    def __init__(self):
        super(Sub_Menu, self).__init__()

        # 메뉴 background image
        self.label_SubMenu = QtWidgets.QLabel(self)
        self.label_SubMenu.setGeometry(QtCore.QRect(110, 222, 342, 324))
        self.label_SubMenu.setObjectName("label_SubMenu")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_SubMenu.setFont(font)
        self.label_SubMenu.setAlignment(Qt.AlignCenter)
        self.label_SubMenu.setStyleSheet("border-image: url(image/btn_select.png);")
        #self.label_SubMenu.setText("메뉴 이미지")



        # 이동 버튼 (->가상화장, 테마)
        self.pushButton_GoSelectFace = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectFace.setGeometry(QtCore.QRect(110, 600, 342, 50))
        #self.pushButton_GoSelectFace.setStyleSheet('background-color: transparent; '
        #                                           'border-top-left-radius : 125px; border-top-right-radius:125px')
        self.pushButton_GoSelectFace.setObjectName("pushButton_GoSelectFace")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoSelectFace.setFont(font)
        self.pushButton_GoSelectFace.setText("SELECT BY FACE")


        self.pushButton_GoSelectThema = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectThema.setGeometry(QtCore.QRect(110, 650, 342, 50))
        #self.pushButton_GoSelectThema.setStyleSheet('background-color: transparent; '
        #                                              'border-bottom-left-radius : 125px; border-bottom-right-radius : 125px')
        self.pushButton_GoSelectThema.setObjectName("pushButton_GoSelectThema")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoSelectThema.setFont(font)
        self.pushButton_GoSelectThema.setText("SELECT BY THEMA")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 733, 562, 61))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_HelpMe_Logo.setFont(font)
        self.label_HelpMe_Logo.setAlignment(Qt.AlignCenter)
        #self.label_HelpMe_Logo.setText("헬미 로고")
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





