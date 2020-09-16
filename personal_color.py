from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Personal_Color(QWidget):

    def __init__(self):
        super(Personal_Color, self).__init__()

        # 쌩얼 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(100, 30, 336, 448)) ## 3:4 비율!
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("BARE FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 퍼스널 컬러 정보 background image
        self.label_background_manual = QtWidgets.QLabel(self)
        self.label_background_manual.setGeometry(QtCore.QRect(11, 497, 514, 210))
        self.label_background_manual.setObjectName("label_background_manual")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_manual.setFont(font)
        self.label_background_manual.setAlignment(Qt.AlignCenter)
        self.label_background_manual.setText("SPRING WARM..")
        self.label_background_manual.setStyleSheet('background-color:#B5A4E7')

        # 이동 버튼(->메인 메뉴)
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(450, 350, 77, 112))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoMainMenu.setFont(font)
        self.pushButton_GoMainMenu.setText("SAVE")
        self.pushButton_GoMainMenu.setObjectName("GoMainMenu")

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

