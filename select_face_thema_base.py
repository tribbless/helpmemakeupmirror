from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Select_face_thema_Base(QWidget):

    def __init__(self):
        super(Select_face_thema_Base, self).__init__()

        self.label_base = QtWidgets.QLabel(self)
        self.label_base.setGeometry(QtCore.QRect(130, 10, 271, 40))
        self.label_base.setObjectName("label_base")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_base.setFont(font)
        self.label_base.setAlignment(Qt.AlignCenter)
        self.label_base.setText("Base MakeUp")

        self.pushButton_GoSelectFaceCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoSelectFaceCapture.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoSelectFaceCapture.setFont(font)
        self.pushButton_GoSelectFaceCapture.setText("NEXT")
        self.pushButton_GoSelectFaceCapture.setObjectName("pushButton_GoSelectFaceCapture")


        self.pushButton_GoMenuOrColor = QtWidgets.QPushButton(self)
        self.pushButton_GoMenuOrColor.setGeometry(QtCore.QRect(0, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoMenuOrColor.setFont(font)
        self.pushButton_GoMenuOrColor.setObjectName("pushButton_GoMenuOrColor")