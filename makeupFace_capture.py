from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MakeupFace_Capture(QWidget):

    def __init__(self):
        super(MakeupFace_Capture, self).__init__()

        # 얼굴
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(109, 40, 318, 424))  ## 3:4 비율!
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 텍스트
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(99, 464, 338, 70))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_manual.setFont(font)
        self.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")
        self.label_manual.setAlignment(Qt.AlignCenter)
        self.label_manual.setStyleSheet('color: #7B7B7B;')

        # 캡쳐 버튼 background image
        self.label_background_Capture = QtWidgets.QLabel(self)
        self.label_background_Capture.setGeometry(QtCore.QRect(52, 560, 230, 110))
        self.label_background_Capture.setObjectName("label_background_Capture")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Capture.setFont(font)
        self.label_background_Capture.setAlignment(Qt.AlignCenter)
        #self.label_background_Capture.setText("CAPTURE")
        self.label_background_Capture.setStyleSheet("border-image: url(image/btn_capture.png);")

        # 캡쳐 버튼
        '''pushButton'''


        # 이동 버튼 background image
        self.label_background_GoSubMenu = QtWidgets.QLabel(self)
        self.label_background_GoSubMenu.setGeometry(QtCore.QRect(292, 560, 192, 110))
        self.label_background_GoSubMenu.setObjectName("label_background_GoSubMenu")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_GoSubMenu.setFont(font)
        self.label_background_GoSubMenu.setAlignment(Qt.AlignCenter)
        #self.label_background_GoSubMenu.setText("SAVE")
        self.label_background_GoSubMenu.setStyleSheet("border-image: url(image/btn_save2.png);")

        # 이동 버튼 (->서브메뉴)
        self.pushButton_GoSubMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoSubMenu.setGeometry(QtCore.QRect(494, 560, 40, 110))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(13)
        self.pushButton_GoSubMenu.setFont(font)
        self.pushButton_GoSubMenu.setText("SAVE")
        self.pushButton_GoSubMenu.setObjectName("GoSubMenu")

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

