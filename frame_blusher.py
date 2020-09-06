from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Blusher(QWidget):

    def __init__(self):
        super(Frame_Blusher, self).__init__()

        self.label_frameBlusher = QtWidgets.QLabel(self)
        self.label_frameBlusher.setGeometry(QtCore.QRect(160, 10, 241, 40))
        self.label_frameBlusher.setObjectName("label_frameBlusher")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameBlusher.setFont(font)
        self.label_frameBlusher.setText("frame_blusher화")

        # 이미지
        self.label_manual_background = QtWidgets.QLabel(self)
        self.label_manual_background.setObjectName("label_manual_background")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.label_manual_background.setPalette(palette)
        font = QtGui.QFont("Times", 15)
        self.label_manual_background.setFont(font)
        self.label_manual_background.setStyleSheet("border-image: url(image/frameBack.png);")
        self.label_manual_background.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.")
        self.label_manual_background.setGeometry(QtCore.QRect(5, 520, 526, 255))

        '''  이미지에 맞게 label사이즈 및 위치 조절해야함~~~   : 설명쓰는 공간~~
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(40, 540, 451, 161))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_manual.setFont(font)
        self.label_manual.setStyleSheet('background-color: transparent')
        self.label_manual.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.\n어쩌구저쩌구\n룰루랄라 ^^이렇게 하면 됩니다 ^^")
        '''

        ## 이동 버튼
        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(5, 716, 527, 48))
        self.pushButton_GoMenu.setStyleSheet('background-color: transparent;')
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")

        self.pushButton_GoLip = QtWidgets.QPushButton(self)
        self.pushButton_GoLip.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoLip.setFont(font)
        self.pushButton_GoLip.setText("lip")
        self.pushButton_GoLip.setObjectName("pushButton_GoLip")
        self.pushButton_GoLip.setStyleSheet("background:rgb(144,144,144);");

        self.pushButton_GoEyeliner = QtWidgets.QPushButton(self)
        self.pushButton_GoEyeliner.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyeliner.setFont(font)
        self.pushButton_GoEyeliner.setText("eyeliner")
        self.pushButton_GoEyeliner.setObjectName("pushButton_GoEyeliner")
        self.pushButton_GoEyeliner.setStyleSheet("background:rgb(144,144,144);");