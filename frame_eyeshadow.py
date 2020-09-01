from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Eyeshadow(QWidget):

    def __init__(self):
        super(Frame_Eyeshadow, self).__init__()

        self.label_frameEyeshadow = QtWidgets.QLabel(self)
        self.label_frameEyeshadow.setGeometry(QtCore.QRect(115, 30, 311, 61))
        self.label_frameEyeshadow.setObjectName("label_frameEyeshadow")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameEyeshadow.setFont(font)
        self.label_frameEyeshadow.setText("frame_eyeshadow화면")

        self.pushButton_GoFrameEyeliner = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameEyeliner.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameEyeliner.setFont(font)
        self.pushButton_GoFrameEyeliner.setText("NEXT")
        self.pushButton_GoFrameEyeliner.setObjectName("pushButton_GoFrameEyeliner")

        self.pushButton_GoFrameEyebrow = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameEyebrow.setGeometry(QtCore.QRect(10, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameEyebrow.setFont(font)
        self.pushButton_GoFrameEyebrow.setText("BACK")
        self.pushButton_GoFrameEyebrow.setObjectName("pushButton_GoFrameEyebrow")
