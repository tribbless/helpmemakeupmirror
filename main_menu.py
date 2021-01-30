from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main_Menu(QWidget):

    def __init__(self):
        super(Main_Menu, self).__init__()

        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(259, 230, 506, 70))
        self.label_title.setObjectName("label_title")
        font = QtGui.QFont()
        font.setPointSize(30) #15
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setText("HELP ME MAKE UP MIRROR")
        self.label_title.setStyleSheet("color: white;")

        ##메뉴이미지
        self.label_background_MainMenu = QtWidgets.QLabel(self)
        self.label_background_MainMenu.setObjectName("label_menu")
        self.label_background_MainMenu.resize(500, 500)
        pixmap = QPixmap("image/menu11.png")
        pixmap = pixmap.scaledToWidth(525)
        self.label_background_MainMenu.setPixmap(QPixmap(pixmap))
        self.label_background_MainMenu.setGeometry(QtCore.QRect(250, 342, 525, 525))

        # 이동 버튼(->퍼스널 컬러, 베이스 메이크업 비디오, 컬러 메이크업)
        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(288, 374, 447, 167))
        self.pushButton_GoPersonalColor.setStyleSheet('background-color: transparent;'
                                                      'border-top-left-radius : 167px; border-top-right-radius:167px')
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")


        self.pushButton_GoBaseMakeupVideo = QtWidgets.QPushButton(self)
        self.pushButton_GoBaseMakeupVideo.setGeometry(QtCore.QRect(288, 542, 447, 126))
        self.pushButton_GoBaseMakeupVideo.setStyleSheet('background-color: transparent; border:0px;')
        self.pushButton_GoBaseMakeupVideo.setObjectName("pushButton_GoBaseMakeupVideo")


        self.pushButton_GoColorMakeup = QtWidgets.QPushButton(self)
        self.pushButton_GoColorMakeup.setGeometry(QtCore.QRect(288, 669, 447, 160))
        self.pushButton_GoColorMakeup.setStyleSheet('background-color: transparent;'
                                                    'border-bottom-left-radius : 160px; border-bottom-right-radius : 160px')
        self.pushButton_GoColorMakeup.setObjectName("pushButton_GoColorMakeup")


        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        # 이동 버튼 image
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(25, 22, 45, 45))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("border-image: url(image/btn_back.png);")

        ## 이동 버튼 (previous)
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(23, 9, 55, 72))
        self.pushButton_GoHome.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                             "border-radius: 10px;")
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")
