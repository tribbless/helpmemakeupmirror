from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Base_Makeup_Video(QWidget):

    def __init__(self):
        super(Base_Makeup_Video, self).__init__()

        # 베이스 메이크업 동영상
        self.label_video = QtWidgets.QLabel(self)
        self.label_video.setGeometry(QtCore.QRect(90, 177, 382, 370))
        self.label_video.setObjectName("label_video")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_video.setFont(font)
        self.label_video.setAlignment(Qt.AlignCenter)
        self.label_video.setStyleSheet("color:white; background-color:#4B4B4B;")
        self.label_video.setText("Video")


        # 이동 버튼 background image
        self.label_background_GoColorMakeup = QtWidgets.QLabel(self)
        self.label_background_GoColorMakeup.setGeometry(QtCore.QRect(161, 599, 240, 65))
        self.label_background_GoColorMakeup.setObjectName("label_background_GoColorMakeup")
        font = QtGui.QFont()
        font.setPointSize(18)
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
                                      "font-size: 20px;\n"
                                      "line-height: 22px;\n"
                                      "\n"
                                      "color: #FFFFFF;\n"
                                      "border: 1px solid #FFFFFF;")


        # 이동 버튼(->캡쳐화면으로)
        self.pushButton_GoColorMakeup = QtWidgets.QPushButton(self)
        self.pushButton_GoColorMakeup.setGeometry(QtCore.QRect(13, 599, 130, 65))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(15)
        self.pushButton_GoColorMakeup.setFont(font)
        self.pushButton_GoColorMakeup.setText("COLOR MAKE UP")
        self.pushButton_GoColorMakeup.setObjectName("GoColorMakeup")

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


