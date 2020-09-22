from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Select_face_Blusher(QWidget):

    def __init__(self):
        super(Select_face_Blusher, self).__init__()

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(125, 57, 312, 416)) #125, 36, 312, 416
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
        self.label_subject.setText("blusher")
        self.label_subject.setStyleSheet('color: #737373')

        # blusher option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(13, 524, 536, 230)) #13, 503, 536, 230
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);")


        # 이동 버튼 (prev/next)
        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(13, 484, 112, 30))
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("< eyeliner")
        self.pushButton_GoEyelinerAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoLipAR = QtWidgets.QPushButton(self)
        self.pushButton_GoLipAR.setGeometry(QtCore.QRect(437, 484, 112, 30)) #437, 463, 112, 30
        self.pushButton_GoLipAR.setObjectName("pushButton_GoLipAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoLipAR.setFont(font)
        self.pushButton_GoLipAR.setText("lip >")
        self.pushButton_GoLipAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))  ## 0, 733, 562, 61  ++ 21
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

