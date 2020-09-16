from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QBrush
class Frame_Eyebrow(QWidget):

    def __init__(self):
        super(Frame_Eyebrow, self).__init__()

        # 프레임 씌어진 얼굴 모습
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(91, 38, 354, 472))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("Framed FACE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(112, 520, 312, 30))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("eye brow")
        self.label_subject.setStyleSheet('color: #737373')

        # eyebrow manual background image
        self.label_background_Manual = QtWidgets.QLabel(self)
        self.label_background_Manual.setGeometry(QtCore.QRect(0, 560, 536, 147))
        self.label_background_Manual.setObjectName("label_background_Manual")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Manual.setFont(font)
        self.label_background_Manual.setAlignment(Qt.AlignCenter)
        self.label_background_Manual.setText("eyebrow manual background image")
        self.label_background_Manual.setStyleSheet('background-color: #B5A4E7;')
        #self.label_background_Manual.setStyleSheet("border-image: url(image/frameBack.png);")


        # 이동 버튼 (prev/next)
        self.pushButton_GoARorThema = QtWidgets.QPushButton(self)
        self.pushButton_GoARorThema.setGeometry(QtCore.QRect(0, 520, 112, 30))
        self.pushButton_GoARorThema.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoARorThema.setFont(font)
        self.pushButton_GoARorThema.setText("< prev")
        self.pushButton_GoARorThema.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        self.pushButton_GoEyesahdowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyesahdowFrame.setGeometry(QtCore.QRect(424, 520, 112, 30))
        self.pushButton_GoEyesahdowFrame.setObjectName("pushButton_GoEyesahdowFrame")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyesahdowFrame.setFont(font)
        self.pushButton_GoEyesahdowFrame.setText("shadow >")
        self.pushButton_GoEyesahdowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 707, 536, 61))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_HelpMe_Logo.setFont(font)
        self.label_HelpMe_Logo.setAlignment(Qt.AlignCenter)
        self.label_HelpMe_Logo.setText("헬미 로고")
        self.label_HelpMe_Logo.setStyleSheet('color:white; background-color:black')





        '''# 이미지에 맞게 label사이즈 및 위치 조절해야함~~~   : 설명쓰는 공간~~
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(40, 540, 451, 161))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        #font.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        font.setPointSize(14)
        self.label_manual.setFont(font)
        #self.label_manual.setStyleSheet('QLabel{background-color: rgba(0, 0, 0, 0.0)}')
        self.label_manual.setStyleSheet('background-color: transparent; color: white')
        self.label_manual.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.\n어쩌구저쩌구\n룰루랄라 ^^이렇게 하면 됩니다 ^^")
        

        ## 이동 버튼
        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(5, 721, 527, 43))
        self.pushButton_GoMenu.setStyleSheet('background-color: transparent;')
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")
        '''

