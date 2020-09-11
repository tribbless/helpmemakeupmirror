from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Personal_Color(QWidget):

    def __init__(self):
        super(Personal_Color, self).__init__()

        self.label_personalColor = QtWidgets.QLabel(self)
        self.label_personalColor.setGeometry(QtCore.QRect(130, 10, 271, 40))
        self.label_personalColor.setObjectName("label_personalColor")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_personalColor.setFont(font)
        self.label_personalColor.setAlignment(Qt.AlignCenter)
        self.label_personalColor.setText("personal color")

        # 얼굴사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(120, 70, 315, 420))
        self.label_face.setObjectName("label_face")
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        #이미지
        self.label_manual_background = QtWidgets.QLabel(self)
        self.label_manual_background.setObjectName("label_manual_background")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.label_manual_background.setPalette(palette)
        font = QtGui.QFont("Times", 15)
        self.label_manual_background.setFont(font)
        self.label_manual_background.setStyleSheet("border-image: url(image/frameBack.png);")
        self.label_manual_background.setText("SPRING WARM")
        self.label_manual_background.setGeometry(QtCore.QRect(5, 520, 526, 255))

        # 이동 버튼
        self.pushButton_GoThema = QtWidgets.QPushButton(self)
        self.pushButton_GoThema.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoThema.setFont(font)
        self.pushButton_GoThema.setText("THEMA")
        self.pushButton_GoThema.setObjectName("pushButton_GoThema")

        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(0, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoMenu.setFont(font)
        self.pushButton_GoMenu.setText("MENU")
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")