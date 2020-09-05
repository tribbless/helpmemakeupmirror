from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Select_face_thema_Capture(QWidget): ## Before label

    def __init__(self):
        super(Select_face_thema_Capture, self).__init__()

        self.label_selectCapture = QtWidgets.QLabel(self)
        self.label_selectCapture.setGeometry(QtCore.QRect(140, 20, 431, 61))
        self.label_selectCapture.setObjectName("label_selectCapture")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_selectCapture.setFont(font)
        self.label_selectCapture.setText("select_face&thema\nFace Capture 화면")

        ## 이 버튼은 Thema or Eyebrow AR 로 갑니다.
        self.pushButton_GoThemaOrEyebrowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoThemaOrEyebrowAR.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoThemaOrEyebrowAR.setFont(font)
        self.pushButton_GoThemaOrEyebrowAR.setText("NEXT")
        self.pushButton_GoThemaOrEyebrowAR.setObjectName("pushButton_GoThemaOrEyebrowAR")

        self.pushButton_GoSelectBase = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectBase.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoSelectBase.setFont(font)
        self.pushButton_GoSelectBase.setText("BACK")
        self.pushButton_GoSelectBase.setObjectName("pushButton_GoSelectBase")