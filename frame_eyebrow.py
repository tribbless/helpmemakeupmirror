from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Eyebrow(QWidget):

    def __init__(self):
        super(Frame_Eyebrow, self).__init__()

        self.label_frameEyebrow = QtWidgets.QLabel(self)
        self.label_frameEyebrow.setGeometry(QtCore.QRect(120, 30, 301, 61))
        self.label_frameEyebrow.setObjectName("label_frameEyebrow")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameEyebrow.setFont(font)
        self.label_frameEyebrow.setText("frame_eyebrow화면")

        self.pushButton_GoFrameEyesahdow = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameEyesahdow.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameEyesahdow.setFont(font)
        self.pushButton_GoFrameEyesahdow.setText("NEXT")
        self.pushButton_GoFrameEyesahdow.setObjectName("pushButton_GoFrameEyesahdow")

        self.pushButton_GoAROrThema = QtWidgets.QPushButton(self)
        self.pushButton_GoAROrThema.setGeometry(QtCore.QRect(10, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoAROrThema.setFont(font)
        self.pushButton_GoAROrThema.setText("BACK")
        self.pushButton_GoAROrThema.setObjectName("pushButton_GoAROrThema")
