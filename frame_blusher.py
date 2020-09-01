from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Blusher(QWidget):

    def __init__(self):
        super(Frame_Blusher, self).__init__()

        self.label_frameBlusher = QtWidgets.QLabel(self)
        self.label_frameBlusher.setGeometry(QtCore.QRect(115, 30, 311, 61))
        self.label_frameBlusher.setObjectName("label_frameBlusher")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameBlusher.setFont(font)
        self.label_frameBlusher.setText("frame_blusher화면")

        self.pushButton_GoLip = QtWidgets.QPushButton(self)
        self.pushButton_GoLip.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoLip.setFont(font)
        self.pushButton_GoLip.setText("NEXT")
        self.pushButton_GoLip.setObjectName("pushButton_GoLip")

        self.pushButton_GoEyeliner = QtWidgets.QPushButton(self)
        self.pushButton_GoEyeliner.setGeometry(QtCore.QRect(10, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyeliner.setFont(font)
        self.pushButton_GoEyeliner.setText("BACK")
        self.pushButton_GoEyeliner.setObjectName("pushButton_GoEyeliner")
