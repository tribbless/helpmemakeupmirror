from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class BareFace_Capture(QWidget):

    def __init__(self):
        super(BareFace_Capture, self).__init__()

        # 얼굴
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(122, 66, 318, 424)) ## 3:4 비율!
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 텍스트
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(112, 490, 338, 70))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_manual.setFont(font)
        self.label_manual.setText("베이스 메이크업 전 촬영입니다.\n화면을 캡쳐하세요.")
        self.label_manual.setAlignment(Qt.AlignCenter)
        self.label_manual.setStyleSheet('color: #7B7B7B;')



        # 캡쳐 버튼 background image
        self.label_background_Capture = QtWidgets.QLabel(self)
        self.label_background_Capture.setGeometry(QtCore.QRect(65, 586, 230, 110))
        self.label_background_Capture.setObjectName("label_background_Capture")
        self.label_background_Capture.setStyleSheet("border-image: url(image/btn_capture.png);")

        # 캡쳐 버튼
        self.pushButton_Capture = QtWidgets.QPushButton(self)
        self.pushButton_Capture.setGeometry(QtCore.QRect(65, 586, 230, 110))
        self.pushButton_Capture.setStyleSheet('background-color: transparent;')
        self.pushButton_Capture.setObjectName("pushButton_Capture")
        self.pushButton_Capture.clicked.connect(self.captureFace)

        # 이동 버튼 background image
        self.label_background_GoPersonalColor = QtWidgets.QLabel(self)
        self.label_background_GoPersonalColor.setGeometry(QtCore.QRect(305, 586, 192, 110))
        self.label_background_GoPersonalColor.setObjectName("label_background_GoPersonalColor")
        self.label_background_GoPersonalColor.setStyleSheet("border-image: url(image/btn_check_your_type.png);")

        # 이동 버튼 (->퍼스널 컬러)
        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(305, 586, 192, 110))
        self.pushButton_GoPersonalColor.setStyleSheet('background-color: transparent;')
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")

        ## 이동 버튼 background
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(7, 5, 31, 40))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")

        # 이동 버튼 (previous)
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(10, 12, 25, 25))
        self.pushButton_GoMainMenu.setStyleSheet("border-image: url(image/btn_back.png);")
        self.pushButton_GoMainMenu.setObjectName("pushButton_GoMainMenu")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_GoMainMenu.setFont(font)
        #self.pushButton_GoMainMenu.setText("<")


        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40)) #0, 707, 536, 61
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")


    def captureFace(self):
        print("얼굴 캡쳐하기")