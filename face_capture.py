from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Face_Capture(QWidget):

    def __init__(self):
        super(Face_Capture, self).__init__()

        # 얼굴
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(120, 70, 315, 420))
        self.label_face.setObjectName("label_face")
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 이미지
        self.label_manual_background = QtWidgets.QLabel(self)
        self.label_manual_background.setObjectName("label_manual_background")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.label_manual_background.setPalette(palette)
        font = QtGui.QFont("Times", 15)
        self.label_manual_background.setFont(font)
        self.label_manual_background.setStyleSheet("border-image: url(image/frameBack.png);")
        #self.label_manual_background.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.")
        self.label_manual_background.setGeometry(QtCore.QRect(5, 560, 526, 215))

        # 글씨
        self.label_text = QtWidgets.QLabel(self)
        self.label_text.setGeometry(QtCore.QRect(2, 340, 110, 70))
        self.label_text.setObjectName("label_text")
        font = QtGui.QFont("Times", 13)
        self.label_text.setFont(font)
        self.label_text.setText("영상\n나오는 중")
        self.label_text.setAlignment(Qt.AlignCenter)

        # 캡쳐버튼
        self.pushButton_Capture = QtWidgets.QPushButton(self)
        self.pushButton_Capture.setGeometry(QtCore.QRect(145, 500, 265, 50))
        font = QtGui.QFont("Times", 17)
        self.pushButton_Capture.setFont(font)
        self.pushButton_Capture.setText("화면을 캡쳐하세요.")
        self.pushButton_Capture.setStyleSheet('color: #7B7B7B; background-color:transparent;')
        self.pushButton_Capture.setObjectName("pushButton_Capture")
        self.pushButton_Capture.clicked.connect(self.captureFace)


        # 이동버튼
        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(5, 724, 527, 40))
        self.pushButton_GoMenu.setStyleSheet('background-color: transparent;')
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")

        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoHome.setText("HOME")
        self.pushButton_GoHome.setFont(font)
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")

    def captureFace(self):
        print("얼굴 캡쳐하기")