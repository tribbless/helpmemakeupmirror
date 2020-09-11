from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class RealFace_ARFace_Compare(QWidget):

    def __init__(self):
        super(RealFace_ARFace_Compare, self).__init__()

        # 텍스트
        self.label_AR = QtWidgets.QLabel(self)
        self.label_AR.setGeometry(QtCore.QRect(10, 80, 246, 80))
        self.label_AR.setObjectName("label_AR")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_AR.setFont(font)
        self.label_AR.setAlignment(Qt.AlignCenter)
        self.label_AR.setText("가상 메이크업")

        self.label_REAL = QtWidgets.QLabel(self)
        self.label_REAL.setGeometry(QtCore.QRect(280, 80, 246, 80))
        self.label_REAL.setObjectName("label_REAL")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_REAL.setFont(font)
        self.label_REAL.setAlignment(Qt.AlignCenter)
        self.label_REAL.setText("완성된 메이크업")

        # 메이크업 비교
        self.label_faceAR = QtWidgets.QLabel(self)
        self.label_faceAR.setGeometry(QtCore.QRect(10, 140, 246, 328))
        self.label_faceAR.setObjectName("label_faceAR")
        self.label_faceAR.setStyleSheet('background-color:white')

        self.label_faceREAL = QtWidgets.QLabel(self)
        self.label_faceREAL.setGeometry(QtCore.QRect(280, 140, 246, 328))
        self.label_faceREAL.setObjectName("label_faceREAL")
        self.label_faceREAL.setStyleSheet("background-color: transparent;" 
                                          "border-style: dashed;"
                                          "border-width: 3px;"
                                          "border-color: rgb(183,166,231);")

        # 이미지
        self.label_manual_background = QtWidgets.QLabel(self)
        self.label_manual_background.setObjectName("label_manual_background")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.label_manual_background.setPalette(palette)
        font = QtGui.QFont("Times", 15)
        self.label_manual_background.setFont(font)
        self.label_manual_background.setStyleSheet("border-image: url(image/frameBack.png);")
        #self.label_manual_background.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.")
        self.label_manual_background.setGeometry(QtCore.QRect(5, 540, 526, 235))

        '''# 이미지에 맞게 label사이즈 및 위치 조절해야함~~~   : 설명쓰는 공간~~
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(40, 540, 451, 161))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        #font.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        font.setPointSize(14)
        self.label_manual.setFont(font)
        #self.label_manual.setStyleSheet('QLabel{background-color: rgba(0, 0, 0, 0.0)}')
        self.label_manual.setStyleSheet('background-color: transparent; color: white')
        self.label_manual.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.\n어쩌구저쩌구\n룰루랄라 ^^이렇게 하면 됩니다 ^^")
        '''


        # 이동 버튼
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(5, 721, 527, 43))
        self.pushButton_GoHome.setStyleSheet('background-color: transparent;')
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")

        self.pushButton_GoFrameLip = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameLip.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameLip.setFont(font)
        self.pushButton_GoFrameLip.setText("BACK")
        self.pushButton_GoFrameLip.setObjectName("pushButton_GoFrameLip")
