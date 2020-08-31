from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Select_face_Eyebrow(QWidget):

    def __init__(self):
        super(Select_face_Eyebrow, self).__init__()

        self.label_eyebrowAR = QtWidgets.QLabel(self)
        self.label_eyebrowAR.setGeometry(QtCore.QRect(10, 10, 381, 61))
        self.label_eyebrowAR.setObjectName("label_eyebrowAR")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_eyebrowAR.setFont(font)
        self.label_eyebrowAR.setText("selcect_face_eyebrow화면")


        self.pushButton_GoEyeshadowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyeshadowAR.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyeshadowAR.setFont(font)
        self.pushButton_GoEyeshadowAR.setText("NEXT")
        self.pushButton_GoEyeshadowAR.setObjectName("pushButton_GoEyeshadowAR")