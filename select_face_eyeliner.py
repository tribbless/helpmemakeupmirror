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


class Select_face_Eyeliner(QWidget):

    def __init__(self):
        super(Select_face_Eyeliner, self).__init__()

        self.label_eyelinerAR = QtWidgets.QLabel(self)
        self.label_eyelinerAR.setGeometry(QtCore.QRect(160, 10, 241, 40))
        self.label_eyelinerAR.setObjectName("label_eyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_eyelinerAR.setFont(font)
        self.label_eyelinerAR.setText("face_eyeliner")

        # 이미지
        self.label_select = QtWidgets.QLabel(self)
        self.label_select.setObjectName("label_select")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.label_select.setPalette(palette)
        font = QtGui.QFont("Times", 15)
        self.label_select.setFont(font)
        self.label_select.setStyleSheet("border-image: url(image/selectAR.png);")
        self.label_select.setText("30%")
        self.label_select.setGeometry(QtCore.QRect(5, 490, 526, 280))


        self.pushButton_GoBlusherAR = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusherAR.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoBlusherAR.setFont(font)
        self.pushButton_GoBlusherAR.setText("NEXT")
        self.pushButton_GoBlusherAR.setObjectName("pushButton_GoBlusherAR")

        self.pushButton_GoEyeshadowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyeshadowAR.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyeshadowAR.setFont(font)
        self.pushButton_GoEyeshadowAR.setText("BACK")
        self.pushButton_GoEyeshadowAR.setObjectName("pushButton_GoEyeshadowAR")