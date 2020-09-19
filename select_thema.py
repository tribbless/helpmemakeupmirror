from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Select_Thema(QWidget):

    def __init__(self):
        super(Select_Thema, self).__init__()

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(112, 20, 312, 416))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # TEHMA option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(0, 507, 536, 200))
        self.label_background_Option.setObjectName("label_background_Option")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Option.setFont(font)
        self.label_background_Option.setAlignment(Qt.AlignCenter)
        #self.label_background_Option.setText("thema option background image")
        self.label_background_Option.setStyleSheet("border-image: url(image/btn_thema.png);")
        #pixmap = QPixmap("image/thema1.png")
        #pixmap = pixmap.scaledToWidth(530)
        #self.label_background_Option.setPixmap(QPixmap(pixmap))
        #self.label_background_Option.setStyleSheet("border-image: url(image/selectAR.png);")

        # 이동 버튼 (prev/next)
        self.pushButton_GoSubMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoSubMenu.setGeometry(QtCore.QRect(0, 457, 92, 30))
        self.pushButton_GoSubMenu.setObjectName("pushButton_GoSubMenu")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoSubMenu.setFont(font)
        self.pushButton_GoSubMenu.setText("< prev")
        self.pushButton_GoSubMenu.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        self.pushButton_GoEyebrowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowFrame.setGeometry(QtCore.QRect(444, 457, 92, 30))
        self.pushButton_GoEyebrowFrame.setObjectName("pushButton_GoEyebrowFrame")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyebrowFrame.setFont(font)
        self.pushButton_GoEyebrowFrame.setText("next >")
        self.pushButton_GoEyebrowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 707, 536, 61))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_HelpMe_Logo.setFont(font)
        self.label_HelpMe_Logo.setAlignment(Qt.AlignCenter)
        #self.label_HelpMe_Logo.setText("헬미 로고")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        ''''
        ## 테마 선택 버튼
        self.pushButton_UserThema = QtWidgets.QPushButton(self)
        self.pushButton_UserThema.setGeometry(QtCore.QRect(23, 551, 160, 146))
        self.pushButton_UserThema.setStyleSheet('background-color: transparent;')
        self.pushButton_UserThema.setObjectName("pushButton_UserThema")
        self.pushButton_UserThema.clicked.connect(self.Apply_UserThema)

        self.pushButton_SpringThema = QtWidgets.QPushButton(self)
        self.pushButton_SpringThema.setGeometry(QtCore.QRect(189, 551, 78, 70))
        self.pushButton_SpringThema.setStyleSheet('background-color: transparent;')
        self.pushButton_SpringThema.setObjectName("pushButton_SpringThema")
        self.pushButton_SpringThema.clicked.connect(self.Apply_SpringThema)

        self.pushButton_SummerThema = QtWidgets.QPushButton(self)
        self.pushButton_SummerThema.setGeometry(QtCore.QRect(274, 551, 78, 70))
        self.pushButton_SummerThema.setStyleSheet('background-color: transparent;')
        self.pushButton_SummerThema.setObjectName("pushButton_SummerThema")
        self.pushButton_SummerThema.clicked.connect(self.Apply_SummerThema)

        self.pushButton_FallThema = QtWidgets.QPushButton(self)
        self.pushButton_FallThema.setGeometry(QtCore.QRect(189, 630, 78, 70))
        self.pushButton_FallThema.setStyleSheet('background-color: transparent;')
        self.pushButton_FallThema.setObjectName("pushButton_FallThema")
        self.pushButton_FallThema.clicked.connect(self.Apply_FallThema)

        self.pushButton_WinterThema = QtWidgets.QPushButton(self)
        self.pushButton_WinterThema.setGeometry(QtCore.QRect(274, 630, 78, 70))
        self.pushButton_WinterThema.setStyleSheet('background-color: transparent;')
        self.pushButton_WinterThema.setObjectName("pushButton_WinterThema")
        self.pushButton_WinterThema.clicked.connect(self.Apply_WinterThema)

        self.pushButton_PartyThema = QtWidgets.QPushButton(self)
        self.pushButton_PartyThema.setGeometry(QtCore.QRect(359, 551, 160, 45))
        self.pushButton_PartyThema.setStyleSheet('background-color: transparent;')
        self.pushButton_PartyThema.setObjectName("pushButton_PartyThema")
        self.pushButton_PartyThema.clicked.connect(self.Apply_PartyThema)

        self.pushButton_DateThema = QtWidgets.QPushButton(self)
        self.pushButton_DateThema.setGeometry(QtCore.QRect(359, 601, 160, 45))
        self.pushButton_DateThema.setStyleSheet('background-color: transparent;')
        self.pushButton_DateThema.setObjectName("pushButton_DateThema")
        self.pushButton_DateThema.clicked.connect(self.Apply_DateThema)

        self.pushButton_OfficeThema = QtWidgets.QPushButton(self)
        self.pushButton_OfficeThema.setGeometry(QtCore.QRect(359, 651, 160, 45))
        self.pushButton_OfficeThema.setStyleSheet('background-color: transparent;')
        self.pushButton_OfficeThema.setObjectName("pushButton_OfficeThema")
        self.pushButton_OfficeThema.clicked.connect(self.Apply_OfficeThema)

        ## 이동 버튼
        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(5, 711, 527, 52))
        self.pushButton_GoMenu.setStyleSheet('background-color: transparent;')
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")
        '''





    def Apply_UserThema(self):
        print("user click")
    def Apply_SpringThema(self):
        print("spring click")
    def Apply_SummerThema(self):
        print("summer click")
    def Apply_FallThema(self):
        print("fall click")
    def Apply_WinterThema(self):
        print("winter click")
    def Apply_PartyThema(self):
        print("party click")
    def Apply_DateThema(self):
        print("date click")
    def Apply_OfficeThema(self):
        print("office click")




