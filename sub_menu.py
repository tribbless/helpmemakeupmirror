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
        self.label_SubMenu.setStyleSheet("border-image: url(image/btn_select.png);")


        # 이동 버튼 (->가상화장, 테마)
        self.pushButton_GoSelectFace = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectFace.setGeometry(QtCore.QRect(126, 236, 311, 142))
        #self.pushButton_GoSelectFace.setStyleSheet("border-style: dashed; border-width: 1px; border-color: red;")
        self.pushButton_GoSelectFace.setStyleSheet('background-color: transparent;'
                                                   'border-top-left-radius :142px; border-top-right-radius:142px')
        self.pushButton_GoSelectFace.setObjectName("pushButton_GoSelectFace")



        self.pushButton_GoSelectThema = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectThema.setGeometry(QtCore.QRect(126, 390, 311, 142))
        self.pushButton_GoSelectThema.setStyleSheet('background-color: transparent;'
                                                    'border-bottom-left-radius:142px; border-bottom-right-radius:142px')
        self.pushButton_GoSelectThema.setObjectName("pushButton_GoSelectThema")

        # 이동 버튼 (previous)
        self.pushButton_GoMakeupFaceCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoMakeupFaceCapture.setGeometry(QtCore.QRect(15, 12, 25, 25))
        self.pushButton_GoMakeupFaceCapture.setStyleSheet("border-image: url(image/btn_back.png);")
        self.pushButton_GoMakeupFaceCapture.setObjectName("pushButton_GoMakeupFaceCapture")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_GoMakeupFaceCapture.setFont(font)
        self.pushButton_GoMakeupFaceCapture.setText("<")
        self.pushButton_GoMakeupFaceCapture.setStyleSheet('background-color:blue;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
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





