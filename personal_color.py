from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Personal_Color(QWidget):

    def __init__(self):
        super(Personal_Color, self).__init__()

        # 쌩얼 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(113, 77, 336, 448)) ## 3:4 비율!
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("BARE FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 퍼스널 컬러 정보 background image
        self.label_background_manual = QtWidgets.QLabel(self)
        self.label_background_manual.setGeometry(QtCore.QRect(24, 544, 514, 210))
        self.label_background_manual.setObjectName("label_background_manual")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_manual.setFont(font)
        self.label_background_manual.setAlignment(Qt.AlignCenter)
        self.label_background_manual.setText("SPRING WARM..")
        self.label_background_manual.setStyleSheet("border-image: url(image/personal_background_btn_.png);")

        # 이동 버튼(->메인 메뉴)
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(424, 593, 78, 108))
        self.pushButton_GoMainMenu.setStyleSheet('background-color:transparent;')
        self.pushButton_GoMainMenu.setObjectName("pushButton_GoMainMenu")

        ## 이동 버튼 background
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(7, 5, 31, 40))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")

        # 이동 버튼 (previous)
        self.pushButton_GoBareFaceCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoBareFaceCapture.setGeometry(QtCore.QRect(10, 12, 25, 25))
        self.pushButton_GoBareFaceCapture.setStyleSheet("border-image: url(image/btn_back.png);")
        self.pushButton_GoBareFaceCapture.setObjectName("pushButton_GoBareFaceCapture")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_GoBareFaceCapture.setFont(font)
        #self.pushButton_GoBareFaceCapture.setText("<")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

