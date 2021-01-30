from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Base_Makeup_Video(QWidget):

    def __init__(self):
        super(Base_Makeup_Video, self).__init__()

        # 베이스 메이크업 동영상
        self.label_video = QtWidgets.QLabel(self)
        self.label_video.setGeometry(QtCore.QRect(112, 295, 800, 450))
        self.label_video.setObjectName("label_video")
        self.label_video.setStyleSheet("border-image: url(image/youtube_video.png);")

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(340, 820, 344, 140))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 30px;")
        self.label_background_white.lower()

        # 이동 버튼 background image
        self.label_background_GoColorMakeup = QtWidgets.QLabel(self)
        self.label_background_GoColorMakeup.setGeometry(QtCore.QRect(350, 830, 324, 120))
        self.label_background_GoColorMakeup.setObjectName("label_background_GoColorMakeup")
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_background_GoColorMakeup.setFont(font)
        self.label_background_GoColorMakeup.setAlignment(Qt.AlignCenter)
        self.label_background_GoColorMakeup.setText("COLOR MAKE UP")
        self.label_background_GoColorMakeup.setStyleSheet("/* Rectangle 16 */\n"
                                      "position: absolute;\n"
                                      "width: 240px;\n"
                                      "height: 65px;\n"
                                      "\n"
                                      "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "  stop: 0 #B5A4E7, \n"
                                      "  stop: 1.0 #F3C3D6);\n"
                                      "\n"
                                      "/* CAPTURE YOUR FACE */\n"
                                      "position: absolute;\n"
                                      "width: 396px;\n"
                                      "height: 80px;\n"
                                      "\n"
                                      "font-family: Segoe MDL2 Assets;\n"
                                      "font-style: normal;\n"
                                      "font-weight: 700;\n"
                                      "font-size: 30px;\n"
                                      "line-height: 22px;\n"
                                      "\n"
                                      "color: #FFFFFF;\n"
                                      "border-radius: 20px;")


        # 이동 버튼(->캡쳐화면으로)
        self.pushButton_GoColorMakeup = QtWidgets.QPushButton(self)
        self.pushButton_GoColorMakeup.setGeometry(QtCore.QRect(260, 830, 504, 169))
        self.pushButton_GoColorMakeup.setStyleSheet('background-color:transparent; border: 0px;')
        self.pushButton_GoColorMakeup.setObjectName("pushButton_GoColorMakeup")

        # 이동 버튼 image
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(25, 22, 45, 45))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("border-image: url(image/btn_back.png);")

        ## 이동 버튼 (previous)
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(23, 9, 55, 72))
        self.pushButton_GoMainMenu.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")
        self.pushButton_GoMainMenu.setObjectName("pushButton_GoMainMenu")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")


