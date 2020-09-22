from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Select_face_Lip(QWidget):

    def __init__(self):
        super(Select_face_Lip, self).__init__()

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(125, 57, 312, 416))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(125, 484, 312, 30))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("lip")
        self.label_subject.setStyleSheet('color: #737373')

        # lip option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(13, 524, 536, 230))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);")


        # 이동 버튼 (prev/next)
        self.pushButton_GoBlusherAR = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusherAR.setGeometry(QtCore.QRect(13, 484, 112, 30))
        self.pushButton_GoBlusherAR.setObjectName("pushButton_GoBlusherAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoBlusherAR.setFont(font)
        self.pushButton_GoBlusherAR.setText("< blusher")
        self.pushButton_GoBlusherAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoEyebrowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowFrame.setGeometry(QtCore.QRect(437, 484, 112, 30))
        self.pushButton_GoEyebrowFrame.setObjectName("pushButton_GoEyebrowFrame")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyebrowFrame.setFont(font)
        self.pushButton_GoEyebrowFrame.setText("frame >")
        self.pushButton_GoEyebrowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")

        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        ## 선택화면 안 요소..


        ##
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(13, 580, 536, 174)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet('background-color: transparent; border: 0px;')


        ## 색상 버튼
        self.pushButton_ResetColor = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ResetColor.setMinimumSize(172, 150)
        self.pushButton_ResetColor.setText("color reset")
        self.pushButton_ResetColor.setFont(font)
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ResetColor.setObjectName("pushButton_ResetColor")
        self.pushButton_ResetColor.clicked.connect(self.Apply_ResetColor)

        self.pushButton_Red = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Red.setMinimumSize(172, 150)
        self.pushButton_Red.setText("red")
        self.pushButton_Red.setFont(font)
        self.pushButton_Red.setStyleSheet('background-color:white;')
        self.pushButton_Red.setObjectName("pushButton_Red")
        self.pushButton_Red.clicked.connect(self.Apply_Red)

        self.pushButton_Pink = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Pink.setMinimumSize(172, 150)
        self.pushButton_Pink.setText("pink")
        self.pushButton_Pink.setFont(font)
        self.pushButton_Pink.setStyleSheet('background-color:white;')
        self.pushButton_Pink.setObjectName("pushButton_Pink")
        self.pushButton_Pink.clicked.connect(self.Apply_Pink)

        self.pushButton_Orange = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Orange.setMinimumSize(172, 150)
        self.pushButton_Orange.setText("orange")
        self.pushButton_Orange.setFont(font)
        self.pushButton_Orange.setStyleSheet('background-color:white;')
        self.pushButton_Orange.setObjectName("pushButton_Orange")
        self.pushButton_Orange.clicked.connect(self.Apply_Orange)


        ## 레이아웃
        widget = QWidget(self.scrollArea)
        scrollLayout = QHBoxLayout(widget)
        scrollLayout.setContentsMargins(0,0,0,0)
        scrollLayout.addWidget(self.pushButton_ResetColor)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_Red)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_Pink)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_Orange)
        widget.setLayout(scrollLayout)
        self.scrollArea.setWidget(widget)

    def Apply_ResetColor(self):
        print("color reset clicked")
        self.pushButton_ResetColor.setStyleSheet('background-color:black;color:white;')
        self.pushButton_Red.setStyleSheet('background-color:white;')
        self.pushButton_Pink.setStyleSheet('background-color:white;')
        self.pushButton_Orange.setStyleSheet('background-color:white;')

    def Apply_Red(self):
        print("red clicked")
        self.pushButton_Red.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_Pink.setStyleSheet('background-color:white;')
        self.pushButton_Orange.setStyleSheet('background-color:white;')

    def Apply_Pink(self):
        print("pink clicked")
        self.pushButton_Pink.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_Red.setStyleSheet('background-color:white;')
        self.pushButton_Orange.setStyleSheet('background-color:white;')

    def Apply_Orange(self):
        print("orange clicked")
        self.pushButton_Orange.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_Red.setStyleSheet('background-color:white;')
        self.pushButton_Pink.setStyleSheet('background-color:white;')


