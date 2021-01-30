from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class RealFace_ARFace_Compare(QWidget):

    def __init__(self):
        super(RealFace_ARFace_Compare, self).__init__()

        # 텍스트
        self.label_AR = QtWidgets.QLabel(self)
        self.label_AR.setGeometry(QtCore.QRect(46, 250, 448, 70))
        self.label_AR.setObjectName("label_AR")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_AR.setFont(font)
        self.label_AR.setAlignment(Qt.AlignCenter)
        self.label_AR.setText("가상 메이크업")
        self.label_AR.setStyleSheet("color: white;")

        self.label_REAL = QtWidgets.QLabel(self)
        self.label_REAL.setGeometry(QtCore.QRect(530, 250, 448, 70))
        self.label_REAL.setObjectName("label_REAL")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_REAL.setFont(font)
        self.label_REAL.setAlignment(Qt.AlignCenter)
        self.label_REAL.setText("완성된 메이크업")
        self.label_REAL.setStyleSheet("color: white;")

        # 메이크업 비교
        self.label_faceAR = QtWidgets.QLabel(self)
        self.label_faceAR.setGeometry(QtCore.QRect(46, 333, 448, 336))
        self.label_faceAR.setObjectName("label_faceAR")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_faceAR.setFont(font)
        self.label_faceAR.setAlignment(Qt.AlignCenter)
        self.label_faceAR.setText("you didn't capture")
        self.label_faceAR.setStyleSheet('background-color:white')

        self.label_faceREAL = QtWidgets.QLabel(self)
        self.label_faceREAL.setGeometry(QtCore.QRect(530, 333, 448, 336))
        self.label_faceREAL.setObjectName("label_faceREAL")
        self.label_faceREAL.setStyleSheet("background-color: black;")


        # 공유 버튼 background image
        self.label_background_Share = QtWidgets.QLabel(self)
        self.label_background_Share.setGeometry(QtCore.QRect(150, 812, 152, 140))
        self.label_background_Share.setObjectName("label_background_Share")
        self.label_background_Share.setStyleSheet("border-image: url(image/compare_btn_share4.png);")

        # 공유 버튼
        self.pushButton_Share = QtWidgets.QPushButton(self)
        self.pushButton_Share.setGeometry(QtCore.QRect(150, 812, 152, 140))
        self.pushButton_Share.setStyleSheet("background-color: transparent; border: 0px;")
        self.pushButton_Share.setObjectName("pushButton_Share")
        self.pushButton_Share.clicked.connect(self.ShareImage)

        # 홈 버튼 background image
        self.label_background_Home = QtWidgets.QLabel(self)
        self.label_background_Home.setGeometry(QtCore.QRect(436, 812, 152, 140))
        self.label_background_Home.setObjectName("label_background_Home")
        self.label_background_Home.setStyleSheet("border-image: url(image/compare_btn_home3.png);")

        # 홈 버튼
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(436, 812, 152, 140))
        self.pushButton_GoHome.setStyleSheet("background-color: transparent; border: 0px;")
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")

        # shutdwon 버튼 background image
        self.label_background_Shutdown = QtWidgets.QLabel(self)
        self.label_background_Shutdown.setGeometry(QtCore.QRect(722, 812, 152, 140))
        self.label_background_Shutdown.setObjectName("label_background_Shutdown")
        self.label_background_Shutdown.setStyleSheet("border-image: url(image/compare_btn_shutdown3.png);")

        # shutdown 버튼
        self.pushButton_Shutdown = QtWidgets.QPushButton(self)
        self.pushButton_Shutdown.setGeometry(QtCore.QRect(722, 812, 152, 140))
        self.pushButton_Shutdown.setStyleSheet("background-color: transparent; border: 0px;")
        self.pushButton_Shutdown.setObjectName("pushButton_Shutdown")

        # 이동 버튼 image
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(25, 22, 45, 45))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("border-image: url(image/btn_back.png);")

        ## 이동 버튼 (previous)
        self.pushButton_GoLipFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoLipFrame.setGeometry(QtCore.QRect(23, 9, 55, 72))
        self.pushButton_GoLipFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")
        self.pushButton_GoLipFrame.setObjectName("pushButton_GoLipFrame")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

    def ShareImage(self):
        print("이미지 공유하기")

    def reset(self):
        print("compare resetALL")
        self.label_faceAR.clear()
        self.label_faceAR.setText("you didn't capture")
