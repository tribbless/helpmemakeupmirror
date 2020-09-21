from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Eyeliner(QWidget):

    def __init__(self):
        super(Frame_Eyeliner, self).__init__()

        # 프레임 씌어진 얼굴 모습
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(104, 85, 354, 472))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("Framed FACE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(125, 567, 312, 30))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("eye liner")
        self.label_subject.setStyleSheet('color: #737373')

        # eyeliner manual background image
        self.label_background_Manual = QtWidgets.QLabel(self)
        self.label_background_Manual.setGeometry(QtCore.QRect(13, 607, 536, 147))
        self.label_background_Manual.setObjectName("label_background_Manual")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Manual.setFont(font)
        self.label_background_Manual.setAlignment(Qt.AlignCenter)
        self.label_background_Manual.setText("eyeliner manual background image")
        self.label_background_Manual.setStyleSheet("border-image: url(image/background.png); color: white;")


        # 이동 버튼 (prev/next)
        self.pushButton_GoEyeshadowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyeshadowFrame.setGeometry(QtCore.QRect(13, 567, 112, 30))
        self.pushButton_GoEyeshadowFrame.setObjectName("pushButton_GoEyeshadowFrame")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyeshadowFrame.setFont(font)
        self.pushButton_GoEyeshadowFrame.setText("< shadow")
        self.pushButton_GoEyeshadowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        self.pushButton_GoBlusherFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusherFrame.setGeometry(QtCore.QRect(437, 567, 112, 30))
        self.pushButton_GoBlusherFrame.setObjectName("pushButton_GoBlusherFrame")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoBlusherFrame.setFont(font)
        self.pushButton_GoBlusherFrame.setText("blusher >")
        self.pushButton_GoBlusherFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

