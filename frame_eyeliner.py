from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Eyeliner(QWidget):

    def __init__(self):
        super(Frame_Eyeliner, self).__init__()

        self.label_frameEyeliner = QtWidgets.QLabel(self)
        self.label_frameEyeliner.setGeometry(QtCore.QRect(160, 10, 241, 40))
        self.label_frameEyeliner.setObjectName("label_frameEyeliner")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameEyeliner.setFont(font)
        self.label_frameEyeliner.setText("frame_eyeliner")

        #이미지
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

        self.pushButton_GoBlusher = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusher.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoBlusher.setFont(font)
        self.pushButton_GoBlusher.setText("blusher")
        self.pushButton_GoBlusher.setObjectName("pushButton_GoBlusher")
        self.pushButton_GoBlusher.setStyleSheet("background:rgb(144,144,144);");

        self.pushButton_GoEyesahdow = QtWidgets.QPushButton(self)
        self.pushButton_GoEyesahdow.setGeometry(QtCore.QRect(10, 10, 130,40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyesahdow.setFont(font)
        self.pushButton_GoEyesahdow.setText("eye shadow")
        self.pushButton_GoEyesahdow.setObjectName("pushButton_GoEyesahdow")
        self.pushButton_GoEyesahdow.setStyleSheet("background:rgb(144,144,144);");