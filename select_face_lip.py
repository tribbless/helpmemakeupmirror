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
        self.scrollArea.setStyleSheet(
            """
            QScrollArea {
                background: transparent;
                border: 0px;
            } 
            QScrollBar:horizontal {
                border: 0px solid grey;
                background: #FFFFFF;
                height: 15px;
                margin: 0px 20px 0 20px;
            }
            QScrollBar::handle:horizontal {
                background: #B5A4E7;
                min-width: 20px;
            }
            QScrollBar::add-line:horizontal {
                border: 0px solid grey;
                background: #B5A4E7;
                width: 20px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:horizontal {
                border: 0px solid grey;
                background: #B5A4E7;
                width: 20px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }
            """
        )

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

        self.pushButton_ColorOne = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ColorOne.setMinimumSize(172, 150)
        self.pushButton_ColorOne.setText("ColorOne")
        self.pushButton_ColorOne.setFont(font)
        self.pushButton_ColorOne.setStyleSheet('background-color:white;')
        self.pushButton_ColorOne.setObjectName("pushButton_ColorOne")
        self.pushButton_ColorOne.clicked.connect(self.Apply_ColorOne)

        self.pushButton_ColorTwo = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ColorTwo.setMinimumSize(172, 150)
        self.pushButton_ColorTwo.setText("ColorTwo")
        self.pushButton_ColorTwo.setFont(font)
        self.pushButton_ColorTwo.setStyleSheet('background-color:white;')
        self.pushButton_ColorTwo.setObjectName("pushButton_ColorTwo")
        self.pushButton_ColorTwo.clicked.connect(self.Apply_ColorTwo)

        self.pushButton_ColorThree = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ColorThree.setMinimumSize(172, 150)
        self.pushButton_ColorThree.setText("ColorThree")
        self.pushButton_ColorThree.setFont(font)
        self.pushButton_ColorThree.setStyleSheet('background-color:white;')
        self.pushButton_ColorThree.setObjectName("pushButton_ColorThree")
        self.pushButton_ColorThree.clicked.connect(self.Apply_ColorThree)

        self.pushButton_ColorFour = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ColorFour.setMinimumSize(172, 150)
        self.pushButton_ColorFour.setText("ColorFour")
        self.pushButton_ColorFour.setFont(font)
        self.pushButton_ColorFour.setStyleSheet('background-color:white;')
        self.pushButton_ColorFour.setObjectName("pushButton_ColorFour")
        self.pushButton_ColorFour.clicked.connect(self.Apply_ColorFour)

        self.pushButton_ColorFive = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ColorFive.setMinimumSize(172, 150)
        self.pushButton_ColorFive.setText("ColorFive")
        self.pushButton_ColorFive.setFont(font)
        self.pushButton_ColorFive.setStyleSheet('background-color:white;')
        self.pushButton_ColorFive.setObjectName("pushButton_ColorFive")
        self.pushButton_ColorFive.clicked.connect(self.Apply_ColorFive)

        self.pushButton_ColorSix = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ColorSix.setMinimumSize(172, 150)
        self.pushButton_ColorSix.setText("ColorSix")
        self.pushButton_ColorSix.setFont(font)
        self.pushButton_ColorSix.setStyleSheet('background-color:white;')
        self.pushButton_ColorSix.setObjectName("pushButton_ColorSix")
        self.pushButton_ColorSix.clicked.connect(self.Apply_ColorSix)

        ## 레이아웃
        widget = QWidget(self.scrollArea)
        widget.setStyleSheet("background-color: transparent; border: 0px")
        scrollLayout = QHBoxLayout(widget)
        scrollLayout.setContentsMargins(0, 0, 0, 0)
        scrollLayout.addWidget(self.pushButton_ResetColor)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_ColorOne)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_ColorTwo)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_ColorThree)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_ColorFour)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_ColorFive)
        scrollLayout.setSpacing(10)
        scrollLayout.addWidget(self.pushButton_ColorSix)
        widget.setLayout(scrollLayout)
        self.scrollArea.setWidget(widget)

    def Apply_ResetColor(self):
        print("color reset clicked")
        self.pushButton_ResetColor.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ColorOne.setStyleSheet('background-color:white;')
        self.pushButton_ColorTwo.setStyleSheet('background-color:white;')
        self.pushButton_ColorThree.setStyleSheet('background-color:white;')
        self.pushButton_ColorFour.setStyleSheet('background-color:white;')
        self.pushButton_ColorFive.setStyleSheet('background-color:white;')
        self.pushButton_ColorSix.setStyleSheet('background-color:white;')

    def Apply_ColorOne(self):
        print("ColorOne clicked")
        self.pushButton_ColorOne.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ColorTwo.setStyleSheet('background-color:white;')
        self.pushButton_ColorThree.setStyleSheet('background-color:white;')
        self.pushButton_ColorFour.setStyleSheet('background-color:white;')
        self.pushButton_ColorFive.setStyleSheet('background-color:white;')
        self.pushButton_ColorSix.setStyleSheet('background-color:white;')

    def Apply_ColorTwo(self):
        print("ColorTwo clicked")
        self.pushButton_ColorTwo.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ColorOne.setStyleSheet('background-color:white;')
        self.pushButton_ColorThree.setStyleSheet('background-color:white;')
        self.pushButton_ColorFour.setStyleSheet('background-color:white;')
        self.pushButton_ColorFive.setStyleSheet('background-color:white;')
        self.pushButton_ColorSix.setStyleSheet('background-color:white;')

    def Apply_ColorThree(self):
        print("ColorThree clicked")
        self.pushButton_ColorThree.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ColorOne.setStyleSheet('background-color:white;')
        self.pushButton_ColorTwo.setStyleSheet('background-color:white;')
        self.pushButton_ColorFour.setStyleSheet('background-color:white;')
        self.pushButton_ColorFive.setStyleSheet('background-color:white;')
        self.pushButton_ColorSix.setStyleSheet('background-color:white;')

    def Apply_ColorFour(self):
        print("ColorFour clicked")
        self.pushButton_ColorFour.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ColorOne.setStyleSheet('background-color:white;')
        self.pushButton_ColorTwo.setStyleSheet('background-color:white;')
        self.pushButton_ColorThree.setStyleSheet('background-color:white;')
        self.pushButton_ColorFive.setStyleSheet('background-color:white;')
        self.pushButton_ColorSix.setStyleSheet('background-color:white;')

    def Apply_ColorFive(self):
        print("ColorFive clicked")
        self.pushButton_ColorFive.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ColorOne.setStyleSheet('background-color:white;')
        self.pushButton_ColorTwo.setStyleSheet('background-color:white;')
        self.pushButton_ColorThree.setStyleSheet('background-color:white;')
        self.pushButton_ColorFour.setStyleSheet('background-color:white;')
        self.pushButton_ColorSix.setStyleSheet('background-color:white;')

    def Apply_ColorSix(self):
        print("ColorSix clicked")
        self.pushButton_ColorSix.setStyleSheet('background-color:black;color:white;')
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ColorOne.setStyleSheet('background-color:white;')
        self.pushButton_ColorTwo.setStyleSheet('background-color:white;')
        self.pushButton_ColorThree.setStyleSheet('background-color:white;')
        self.pushButton_ColorFour.setStyleSheet('background-color:white;')
        self.pushButton_ColorFive.setStyleSheet('background-color:white;')