from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Eyeliner(QWidget):

    def __init__(self):
        super(Frame_Eyeliner, self).__init__()

        self.label_frameEyeliner = QtWidgets.QLabel(self)
        self.label_frameEyeliner.setGeometry(QtCore.QRect(115, 30, 311, 61))
        self.label_frameEyeliner.setObjectName("label_frameEyeliner")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameEyeliner.setFont(font)
        self.label_frameEyeliner.setText("frame_eyeliner화면")

        self.pushButton_GoBlusher = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusher.setGeometry(QtCore.QRect(430, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoBlusher.setFont(font)
        self.pushButton_GoBlusher.setText("NEXT")
        self.pushButton_GoBlusher.setObjectName("pushButton_GoBlusher")

        self.pushButton_GoEyesahdow = QtWidgets.QPushButton(self)
        self.pushButton_GoEyesahdow.setGeometry(QtCore.QRect(10, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyesahdow.setFont(font)
        self.pushButton_GoEyesahdow.setText("BACK")
        self.pushButton_GoEyesahdow.setObjectName("pushButton_GoEyesahdow")
