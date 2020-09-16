from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class RealFace_ARFace_Compare(QWidget):

    def __init__(self):
        super(RealFace_ARFace_Compare, self).__init__()

        # 텍스트
        self.label_AR = QtWidgets.QLabel(self)
        self.label_AR.setGeometry(QtCore.QRect(0, 96, 261, 50))
        self.label_AR.setObjectName("label_AR")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_AR.setFont(font)
        self.label_AR.setAlignment(Qt.AlignCenter)
        self.label_AR.setText("가상 메이크업")

        self.label_REAL = QtWidgets.QLabel(self)
        self.label_REAL.setGeometry(QtCore.QRect(275, 96, 261, 50))
        self.label_REAL.setObjectName("label_REAL")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_REAL.setFont(font)
        self.label_REAL.setAlignment(Qt.AlignCenter)
        self.label_REAL.setText("완성된 메이크업")

        # 메이크업 비교
        self.label_faceAR = QtWidgets.QLabel(self)
        self.label_faceAR.setGeometry(QtCore.QRect(0, 146, 261, 352))
        self.label_faceAR.setObjectName("label_faceAR")
        self.label_faceAR.setStyleSheet('background-color:white')

        self.label_faceREAL = QtWidgets.QLabel(self)
        self.label_faceREAL.setGeometry(QtCore.QRect(275, 146, 261, 352))
        self.label_faceREAL.setObjectName("label_faceREAL")
        self.label_faceREAL.setStyleSheet("background-color: transparent;" 
                                          "border-style: dashed;"
                                          "border-width: 3px;"
                                          "border-color: rgb(183,166,231);")

        # 홈 버튼 background image
        self.label_background_Home = QtWidgets.QLabel(self)
        self.label_background_Home.setGeometry(QtCore.QRect(52, 548, 230, 110))
        self.label_background_Home.setObjectName("label_background_Home")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Home.setFont(font)
        self.label_background_Home.setAlignment(Qt.AlignCenter)
        self.label_background_Home.setText("HOME")
        self.label_background_Home.setStyleSheet('background-color:#B5A4E7')

        # 홈 버튼
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(0, 548, 50, 110))
        self.pushButton_GoHome.setObjectName("GoHome")
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(15)
        self.pushButton_GoHome.setFont(font)
        self.pushButton_GoHome.setText("HOME")

        # 공유 버튼 background image
        self.label_background_Share = QtWidgets.QLabel(self)
        self.label_background_Share.setGeometry(QtCore.QRect(292, 548, 192, 110))
        self.label_background_Share.setObjectName("label_background_Share")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Share.setFont(font)
        self.label_background_Share.setAlignment(Qt.AlignCenter)
        self.label_background_Share.setText("SHARE")
        self.label_background_Share.setStyleSheet('background-color:#B5A4E7')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 707, 536, 61))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_HelpMe_Logo.setFont(font)
        self.label_HelpMe_Logo.setAlignment(Qt.AlignCenter)
        self.label_HelpMe_Logo.setText("헬미 로고")
        self.label_HelpMe_Logo.setStyleSheet('color:white; background-color:black')




