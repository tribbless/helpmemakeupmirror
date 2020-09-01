from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#모양버튼
#색깔버튼
#합쳐서 4가지 버튼해야하나..흠.. 아니면 모양선택-> 색깔선택 후 완료버튼을 누르는겨..
#둘다 선택안햇으면 메시지박스로 선택하라고 안내메시지 주는겨..

#모양과 색깔을 선택하면 그 정보+얼굴 사진을 눈썹.py에 있는 class(?)에게 주는겨
#class는 return 이미지 주는겨~~~~~


class Select_face_Eyeshadow(QWidget):

    def __init__(self):
        super(Select_face_Eyeshadow, self).__init__()

        self.label_eyeshadowAR = QtWidgets.QLabel(self)
        self.label_eyeshadowAR.setGeometry(QtCore.QRect(140, 10, 421, 61))
        self.label_eyeshadowAR.setObjectName("label_eyeshadowAR")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_eyeshadowAR.setFont(font)
        self.label_eyeshadowAR.setText("selcect_face\neyeshadow화면")


        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("NEXT")
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")

        self.pushButton_GoEyebrowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowAR.setGeometry(QtCore.QRect(10, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyebrowAR.setFont(font)
        self.pushButton_GoEyebrowAR.setText("BACK")
        self.pushButton_GoEyebrowAR.setObjectName("pushButton_GoEyebrowAR")