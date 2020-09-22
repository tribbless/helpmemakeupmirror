from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Shape(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButton_ResetAll = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ResetAll.setMinimumSize(164, 150)
        self.pushButton_ResetAll.setText("all reset")
        self.pushButton_ResetAll.setFont(font)
        self.pushButton_ResetAll.setStyleSheet('background-color:white;')
        self.pushButton_ResetAll.setObjectName("pushButton_ResetALl")

        self.pushButton_Arch = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Arch.setMinimumSize(164, 150)
        self.pushButton_Arch.setText("arch")
        self.pushButton_Arch.setFont(font)
        self.pushButton_Arch.setStyleSheet('background-color:white;')
        self.pushButton_Arch.setObjectName("pushButton_Arch")

        self.pushButton_Straight = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Straight.setMinimumSize(164, 150)
        self.pushButton_Straight.setText("straight")
        self.pushButton_Straight.setFont(font)
        self.pushButton_Straight.setStyleSheet('background-color:white;')
        self.pushButton_Straight.setObjectName("pushButton_Straight")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetAll)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Arch)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Straight)

        self.setLayout(layout)

class Color(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButton_ResetColor = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ResetColor.setMinimumSize(164, 150)
        self.pushButton_ResetColor.setText("color reset")
        self.pushButton_ResetColor.setFont(font)
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ResetColor.setObjectName("pushButton_ResetColor")

        self.pushButton_Black = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Black.setMinimumSize(164, 150)
        self.pushButton_Black.setText("black")
        self.pushButton_Black.setFont(font)
        self.pushButton_Black.setStyleSheet('background-color:white;')
        self.pushButton_Black.setObjectName("pushButton_Black")

        self.pushButton_Brown = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Brown.setMinimumSize(164, 150)
        self.pushButton_Brown.setText("brown")
        self.pushButton_Brown.setFont(font)
        self.pushButton_Brown.setStyleSheet('background-color:white;')
        self.pushButton_Brown.setObjectName("pushButton_Brown")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetColor)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Black)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Brown)

        self.setLayout(layout)

class Select_face_Eyeshadow(QWidget):

    def __init__(self):
        super(Select_face_Eyeshadow, self).__init__()

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(125, 57, 312, 416))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(125, 484, 312, 30))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("eye shadow")
        self.label_subject.setStyleSheet('color: #737373')

        # eyeshadow option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(13, 524, 536, 230))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);")

        # 이동 버튼 (prev/next)
        self.pushButton_GoEyebrowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowAR.setGeometry(QtCore.QRect(13, 484, 112, 30))
        self.pushButton_GoEyebrowAR.setObjectName("pushButton_GoEyebrowAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyebrowAR.setFont(font)
        self.pushButton_GoEyebrowAR.setText("< eyebrow")
        self.pushButton_GoEyebrowAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(437, 484, 112, 30))
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("eyeliner >")
        self.pushButton_GoEyelinerAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")
