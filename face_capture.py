from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Face_Capture(QWidget):

    def __init__(self):
        super(Face_Capture, self).__init__()

        self.label_faceCapture = QtWidgets.QLabel(self)
        self.label_faceCapture.setGeometry(QtCore.QRect(10, 10, 281, 61))
        self.label_faceCapture.setObjectName("label_faceCapture")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_faceCapture.setFont(font)
        self.label_faceCapture.setText("face_capture화면")

        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(430, 620, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoMenu.setText("Capture")
        self.pushButton_GoMenu.setFont(font)
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")

        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(10, 620, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoHome.setText("HOME")
        self.pushButton_GoHome.setFont(font)
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")