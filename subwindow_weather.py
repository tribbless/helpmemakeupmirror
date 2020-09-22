import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class SubWindow_Weather(QDialog): #QDialog
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('WEHATER')
        self.resize(400,400)
        self.setStyleSheet('background-color:white;')

        layout = QHBoxLayout()

        self.label_Info = QtWidgets.QLabel(self)
        self.label_Info.setObjectName("label_Info")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_Info.setFont(font)
        self.label_Info.setText("내일도 일교차 10°이상 ~~")
        self.label_Info.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label_Info)
        self.setLayout(layout)

    def showModal(self): #새 Modal 창이 열렸을 경우 기존에 있던 창을 사용하지 못하는 방식입니다.
        return super().exec_()