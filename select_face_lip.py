from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Select_face_Lip(QWidget):

    def __init__(self):
        super(Select_face_Lip, self).__init__()

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(125, 10, 312, 416))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(125, 437, 312, 30))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("lip")
        self.label_subject.setStyleSheet('color: #737373')

        # lip option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(13, 477, 536, 230))
        self.label_background_Option.setObjectName("label_background_Option")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Option.setFont(font)
        self.label_background_Option.setAlignment(Qt.AlignCenter)
        self.label_background_Option.setText("lip option background image")
        #self.label_background_Option.setStyleSheet('background-color: #B5A4E7;')
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);")


        # 이동 버튼 (prev/next)
        self.pushButton_GoBlusherAR = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusherAR.setGeometry(QtCore.QRect(13, 437, 112, 30))
        self.pushButton_GoBlusherAR.setObjectName("pushButton_GoBlusherAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoBlusherAR.setFont(font)
        self.pushButton_GoBlusherAR.setText("< blusher")
        self.pushButton_GoBlusherAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoEyebrowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowFrame.setGeometry(QtCore.QRect(437, 437, 112, 30))
        self.pushButton_GoEyebrowFrame.setObjectName("pushButton_GoEyebrowFrame")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyebrowFrame.setFont(font)
        self.pushButton_GoEyebrowFrame.setText("frame >")
        self.pushButton_GoEyebrowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 733, 562, 61))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_HelpMe_Logo.setFont(font)
        self.label_HelpMe_Logo.setAlignment(Qt.AlignCenter)
        #self.label_HelpMe_Logo.setText("헬미 로고")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        ''' 

        ## 선택 버튼
        self.pushButton_FirstOption = QtWidgets.QPushButton(self)
        self.pushButton_FirstOption.setGeometry(QtCore.QRect(5, 552, 168, 156))
        self.pushButton_FirstOption.setStyleSheet('background-color: transparent;')
        self.pushButton_FirstOption.setObjectName("pushButton_FirstOption")
        self.pushButton_FirstOption.clicked.connect(self.Apply_FirstOption)

        self.pushButton_TwoOption = QtWidgets.QPushButton(self)
        self.pushButton_TwoOption.setGeometry(QtCore.QRect(185, 552, 168, 156))
        self.pushButton_TwoOption.setStyleSheet('background-color: transparent;')
        self.pushButton_TwoOption.setObjectName("pushButton_TwoOption")
        self.pushButton_TwoOption.clicked.connect(self.Apply_TwoOption)

        self.pushButton_ThirdOption = QtWidgets.QPushButton(self)
        self.pushButton_ThirdOption.setGeometry(QtCore.QRect(363, 552, 168, 156))
        self.pushButton_ThirdOption.setStyleSheet('background-color: transparent;')
        self.pushButton_ThirdOption.setObjectName("pushButton_ThirdOption")
        self.pushButton_ThirdOption.clicked.connect(self.Apply_ThirdOption)

        ## 이동 버튼
        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(5, 725, 527, 56))
        self.pushButton_GoMenu.setStyleSheet('background-color: transparent;')
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")
        '''


    def Apply_FirstOption(self):
        print("first option clicked")
    def Apply_TwoOption(self):
        print("two option clicked")
    def Apply_ThirdOption(self):
        print("third option clicked")


