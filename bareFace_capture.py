from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class BareFace_Capture(QWidget):

    def __init__(self):
        super(BareFace_Capture, self).__init__()

        # 얼굴
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(122, 40, 318, 424)) ## 3:4 비율!
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 텍스트
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(112, 464, 338, 70))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_manual.setFont(font)
        self.label_manual.setText("베이스 메이크업 전 촬영입니다.\n화면을 캡쳐하세요.")
        self.label_manual.setAlignment(Qt.AlignCenter)
        self.label_manual.setStyleSheet('color: #7B7B7B;')



        # 캡쳐 버튼 background image
        self.label_background_Capture = QtWidgets.QLabel(self)
        self.label_background_Capture.setGeometry(QtCore.QRect(65, 560, 230, 110))
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
        self.label_background_GoPersonalColor = QtWidgets.QLabel(self)
        self.label_background_GoPersonalColor.setGeometry(QtCore.QRect(305, 560, 192, 110))
        self.label_background_GoPersonalColor.setObjectName("label_background_GoPersonalColor")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_background_GoPersonalColor.setFont(font)
        self.label_background_GoPersonalColor.setAlignment(Qt.AlignCenter)
        #self.label_background_GoPersonalColor.setText("CHECK\nYOUR\nTYPE")
        self.label_background_GoPersonalColor.setStyleSheet("border-image: url(image/btn_check_your_type.png);")

        # 이동 버튼 (->퍼스널 컬러)
        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(507, 560, 40, 110))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(10)
        self.pushButton_GoPersonalColor.setFont(font)
        self.pushButton_GoPersonalColor.setText("CHECK\nYOUR\nTYPE")
        self.pushButton_GoPersonalColor.setObjectName("GoPersonalColor")


        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 733, 562, 61)) #0, 707, 536, 61
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_HelpMe_Logo.setFont(font)
        self.label_HelpMe_Logo.setAlignment(Qt.AlignCenter)
        #self.label_HelpMe_Logo.setText("헬미 로고")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")



        '''
        # 캡쳐 버튼
        self.pushButton_Capture = QtWidgets.QPushButton(self)
        self.pushButton_Capture.setGeometry(QtCore.QRect(145, 500, 265, 50))
        font = QtGui.QFont("Times", 17)
        self.pushButton_Capture.setFont(font)
        self.pushButton_Capture.setText("화면을 캡쳐하세요.")
        self.pushButton_Capture.setStyleSheet('color: #7B7B7B; background-color:transparent;')
        self.pushButton_Capture.setObjectName("pushButton_Capture")
        self.pushButton_Capture.clicked.connect(self.captureFace)
        '''




    def captureFace(self):
        print("얼굴 캡쳐하기")