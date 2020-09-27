import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class SubWindow_MenuShortcut(QDialog): #QDialog
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #self.setWindowTitle('MENU')
        self.resize(340,280)
        self.setStyleSheet('background-color:white;')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        ## 상단 타이틀 바
        self.label_titlebar = QtWidgets.QLabel(self)
        self.label_titlebar.setObjectName("label_titlebar")
        self.label_titlebar.setMinimumHeight(50)
        self.label_titlebar.setStyleSheet('background-color:#B5A4E7')


        self.pushButton_Close = QtWidgets.QPushButton(self)
        self.pushButton_Close.setGeometry(QtCore.QRect(290, 0, 50, 50))
        self.pushButton_Close.setObjectName("pushButton_Close")
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setText("×")
        self.pushButton_Close.setStyleSheet('background-color:#B5A4E7; color:white;')
        self.pushButton_Close.clicked.connect(self.CloseClieked)

        ## 메뉴모음
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")
        self.pushButton_GoHome.setMinimumHeight(120)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_GoHome.setFont(font)
        self.pushButton_GoHome.setText("HOME")
        self.pushButton_GoHome.clicked.connect(self.HomeClieked)

        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")
        self.pushButton_GoMenu.setMinimumHeight(120)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_GoMenu.setFont(font)
        self.pushButton_GoMenu.setText("MENU")
        self.pushButton_GoMenu.clicked.connect(self.MenuClieked)

        self.pushButton_GoBaseMakeup = QtWidgets.QPushButton(self)
        self.pushButton_GoBaseMakeup.setObjectName("pushButton_GoBaseMakeup")
        self.pushButton_GoBaseMakeup.setMinimumHeight(120)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_GoBaseMakeup.setFont(font)
        self.pushButton_GoBaseMakeup.setText("BASE\nMAKEUP")
        self.pushButton_GoBaseMakeup.clicked.connect(self.BaseMakeupClieked)


        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")
        self.pushButton_GoPersonalColor.setMinimumHeight(120)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_GoPersonalColor.setFont(font)
        self.pushButton_GoPersonalColor.setText("PERSONAL\nCOLOR")
        self.pushButton_GoPersonalColor.clicked.connect(self.PersonalColorClieked)

        self.pushButton_GoCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoCapture.setObjectName("pushButton_GoCapture")
        self.pushButton_GoCapture.setMinimumHeight(120)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_GoCapture.setFont(font)
        self.pushButton_GoCapture.setText("CAPTURE")
        self.pushButton_GoCapture.clicked.connect(self.CaptureClieked)

        self.pushButton_GoSelect = QtWidgets.QPushButton(self)
        self.pushButton_GoSelect.setObjectName("pushButton_GoSelect")
        self.pushButton_GoSelect.setMinimumHeight(120)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_GoSelect.setFont(font)
        self.pushButton_GoSelect.setText("SELECT")
        self.pushButton_GoSelect.clicked.connect(self.SelectClieked)


        self.pushButton_GoExit = QtWidgets.QPushButton(self)
        self.pushButton_GoExit.setObjectName("pushButton_GoExit")
        self.pushButton_GoExit.setMinimumHeight(40)
        self.pushButton_GoExit.setMaximumWidth(40)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_GoExit.setFont(font)
        self.pushButton_GoExit.setText("EXIT")
        self.pushButton_GoExit.clicked.connect(self.ExitClieked)


        ## 레이아웃 배치
        titlebar = QHBoxLayout()
        titlebar.setContentsMargins(0,0,0,0)
        titlebar.addWidget(self.label_titlebar)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.pushButton_GoHome)
        hbox1.addWidget(self.pushButton_GoMenu)
        hbox1.addWidget(self.pushButton_GoBaseMakeup)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.pushButton_GoPersonalColor)
        hbox2.addWidget(self.pushButton_GoCapture)
        hbox2.addWidget(self.pushButton_GoSelect)

        layout.addLayout(titlebar)
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
        layout.addWidget(self.pushButton_GoExit,alignment=Qt.AlignRight)

        self.setLayout(layout)


    def showModal(self): #새 Modal 창이 열렸을 경우 기존에 있던 창을 사용하지 못하는 방식입니다.
        return super().exec_()

    def CloseClieked(self):
        self.reject()

    def HomeClieked(self):
        print("home clicked")
        self.btn = 1
        self.accept()
    def MenuClieked(self):
        print("main menu clicked")
        self.btn = 2
        self.accept()
    def BaseMakeupClieked(self):
        print("base makeup video clicked")
        self.btn = 3
        self.accept()

    def PersonalColorClieked(self):
        print("personal color clicked")
        self.btn = 4
        self.accept()
    def CaptureClieked(self):
        print("color makeup clicked")
        self.btn = 5
        self.accept()
    def SelectClieked(self):
        print("sub menu clicked")
        self.btn = 6
        self.accept()
    def ExitClieked(self):
        print("exit clicked")
        self.btn = 0
        self.accept()