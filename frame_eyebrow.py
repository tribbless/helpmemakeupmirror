from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Eyebrow(QWidget):

    def __init__(self):
        super(Frame_Eyebrow, self).__init__()

        self.label_frameEyebrow = QtWidgets.QLabel(self)
        self.label_frameEyebrow.setGeometry(QtCore.QRect(160, 10, 241, 40))
        self.label_frameEyebrow.setObjectName("label_frameEyebrow")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameEyebrow.setFont(font)
        self.label_frameEyebrow.setText("frame_eyebrow")

        #이미지
        self.label_manual_background = QtWidgets.QLabel(self)
        self.label_manual_background.setGeometry(QtCore.QRect(5, 520, 526, 255))
        self.label_manual_background.setObjectName("label_manual_background")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_manual_background.setFont(font)
        self.label_manual_background.setStyleSheet('background:yellow')
        self.label_manual_background.setText("나는 이미지")

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


        self.pushButton_GoFrameEyesahdow = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameEyesahdow.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameEyesahdow.setFont(font)
        self.pushButton_GoFrameEyesahdow.setText("NEXT")
        self.pushButton_GoFrameEyesahdow.setObjectName("pushButton_GoFrameEyesahdow")

        self.pushButton_GoAROrThema = QtWidgets.QPushButton(self)
        self.pushButton_GoAROrThema.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoAROrThema.setFont(font)
        self.pushButton_GoAROrThema.setText("BACK")
        self.pushButton_GoAROrThema.setObjectName("pushButton_GoAROrThema")
