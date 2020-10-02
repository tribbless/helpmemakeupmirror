from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MakeupFace_Capture(QWidget):

    def __init__(self):
        super(MakeupFace_Capture, self).__init__()

        # 얼굴
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(122, 66, 318, 424))  ## 3:4 비율!
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
        self.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")
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
        self.pushButton_Capture.setStyleSheet('background-color:transparent;')
        self.pushButton_Capture.setObjectName("pushButton_Capture")
        self.pushButton_Capture.clicked.connect(self.captureFace)


        # 이동 버튼 background image
        self.label_background_GoSubMenu = QtWidgets.QLabel(self)
        self.label_background_GoSubMenu.setGeometry(QtCore.QRect(305, 586, 192, 110))
        self.label_background_GoSubMenu.setObjectName("label_background_GoSubMenu")
        self.label_background_GoSubMenu.setStyleSheet("border-image: url(image/btn_save2.png);")

        # 이동 버튼 (->서브메뉴)
        self.pushButton_GoSubMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoSubMenu.setGeometry(QtCore.QRect(305, 586, 192, 110))
        self.pushButton_GoSubMenu.setStyleSheet('background-color:transparent;')
        self.pushButton_GoSubMenu.setObjectName("pushButton_GoSubMenu")
        self.pushButton_GoSubMenu.clicked.connect(self.Save_captureFace)

        ## 이동 버튼 background
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(7, 5, 31, 40))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")

        # 이동 버튼 (previous)
        self.pushButton_GoMainMENUorVideo = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMENUorVideo.setGeometry(QtCore.QRect(10, 12, 25, 25))
        self.pushButton_GoMainMENUorVideo.setStyleSheet("border-image: url(image/btn_back.png);")
        self.pushButton_GoMainMENUorVideo.setObjectName("pushButton_GoMainMENUorVideo")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_GoMainMENUorVideo.setFont(font)
        #self.pushButton_GoMainMENUorVideo.setText("<")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

    def captureFace(self):
        print("얼굴 캡쳐하기")
    def Save_captureFace(self):
        print("얼굴 캡쳐본 저장하기")