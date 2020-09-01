from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Lip(QWidget):

    def __init__(self):
        super(Frame_Lip, self).__init__()

        self.label_frameLip = QtWidgets.QLabel(self)
        self.label_frameLip.setGeometry(QtCore.QRect(115, 30, 311, 61))
        self.label_frameLip.setObjectName("label_frameLip")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameLip.setFont(font)
        self.label_frameLip.setText("frame_lip화면")

        self.pushButton_GoCompare = QtWidgets.QPushButton(self)
        self.pushButton_GoCompare.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoCompare.setFont(font)
        self.pushButton_GoCompare.setText("RESULT")
        self.pushButton_GoCompare.setObjectName("pushButton_GoCompare")

        self.pushButton_GoBlusher = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusher.setGeometry(QtCore.QRect(10, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoBlusher.setFont(font)
        self.pushButton_GoBlusher.setText("BACK")
        self.pushButton_GoBlusher.setObjectName("pushButton_GoBlusher")
