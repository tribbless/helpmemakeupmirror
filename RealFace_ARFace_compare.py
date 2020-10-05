from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class RealFace_ARFace_Compare(QWidget):

    def __init__(self):
        super(RealFace_ARFace_Compare, self).__init__()

        # 텍스트
        self.label_AR = QtWidgets.QLabel(self)
        self.label_AR.setGeometry(QtCore.QRect(13, 96, 261, 50))
        self.label_AR.setObjectName("label_AR")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_AR.setFont(font)
        self.label_AR.setAlignment(Qt.AlignCenter)
        self.label_AR.setText("가상 메이크업")

        self.label_REAL = QtWidgets.QLabel(self)
        self.label_REAL.setGeometry(QtCore.QRect(288, 96, 261, 50))
        self.label_REAL.setObjectName("label_REAL")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_REAL.setFont(font)
        self.label_REAL.setAlignment(Qt.AlignCenter)
        self.label_REAL.setText("완성된 메이크업")

        # 메이크업 비교
        self.label_faceAR = QtWidgets.QLabel(self)
        self.label_faceAR.setGeometry(QtCore.QRect(13, 146, 261, 352))
        self.label_faceAR.setObjectName("label_faceAR")
        self.label_faceAR.setStyleSheet('background-color:white')

        self.label_faceREAL = QtWidgets.QLabel(self)
        self.label_faceREAL.setGeometry(QtCore.QRect(288, 146, 261, 352))
        self.label_faceREAL.setObjectName("label_faceREAL")
        self.label_faceREAL.setStyleSheet("background-color: transparent;" 
                                          "border-style: dashed;"
                                          "border-width: 3px;"
                                          "border-color: rgb(183,166,231);")

        # 홈 버튼 background image
        self.label_background_Home = QtWidgets.QLabel(self)
        self.label_background_Home.setGeometry(QtCore.QRect(65, 548, 230, 110))
        self.label_background_Home.setObjectName("label_background_Home")
        self.label_background_Home.setStyleSheet("border-image: url(image/btn_home.png);")

        # 홈 버튼
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(65, 548, 230, 110))
        self.pushButton_GoHome.setStyleSheet("background-color: transparent;")
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")


        # 공유 버튼 background image
        self.label_background_Share = QtWidgets.QLabel(self)
        self.label_background_Share.setGeometry(QtCore.QRect(305, 548, 192, 110))
        self.label_background_Share.setObjectName("label_background_Share")
        self.label_background_Share.setStyleSheet("border-image: url(image/btn_share.png);")

        # 공유 버튼
        self.pushButton_Share = QtWidgets.QPushButton(self)
        self.pushButton_Share.setGeometry(QtCore.QRect(305, 548, 192, 110))
        self.pushButton_Share.setStyleSheet("background-color: transparent;")
        self.pushButton_Share.setObjectName("pushButton_Share")
        self.pushButton_Share.clicked.connect(self.ShareImage)

        ## 이동 버튼 background
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(7, 5, 31, 40))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")

        # 이동 버튼 (previous)
        self.pushButton_GoLipFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoLipFrame.setGeometry(QtCore.QRect(10, 12, 25, 25))
        self.pushButton_GoLipFrame.setStyleSheet("border-image: url(image/btn_back.png);")
        self.pushButton_GoLipFrame.setObjectName("pushButton_GoLipFrame")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

    def ShareImage(self):
        print("이미지 공유하기")

