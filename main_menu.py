from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main_Menu(QWidget):

    def __init__(self):
        super(Main_Menu, self).__init__()


        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(100, 112, 362, 50))
        self.label_title.setObjectName("label_title")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setText("HELP ME MAKE UP MIRROR")

        ##메뉴이미지
        self.label_background_MainMenu = QtWidgets.QLabel(self)
        self.label_background_MainMenu.setObjectName("label_menu")
        self.label_background_MainMenu.resize(300, 300)
        pixmap = QPixmap("image/menu1.png")
        pixmap = pixmap.scaledToWidth(375)
        self.label_background_MainMenu.setPixmap(QPixmap(pixmap))
        self.label_background_MainMenu.setGeometry(QtCore.QRect(93, 200, 375, 375))

        # 이동 버튼(->퍼스널 컬러, 베이스 메이크업 비디오, 컬러 메이크업)
        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(113, 216, 334, 127))
        self.pushButton_GoPersonalColor.setStyleSheet('background-color: transparent;'
                                                      'border-top-left-radius : 127px; border-top-right-radius:127px')
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")


        self.pushButton_GoBaseMakeupVideo = QtWidgets.QPushButton(self)
        self.pushButton_GoBaseMakeupVideo.setGeometry(QtCore.QRect(113, 344, 334, 90))
        self.pushButton_GoBaseMakeupVideo.setStyleSheet('background-color: transparent;')
        self.pushButton_GoBaseMakeupVideo.setObjectName("pushButton_GoBaseMakeupVideo")


        self.pushButton_GoColorMakeup = QtWidgets.QPushButton(self)
        self.pushButton_GoColorMakeup.setGeometry(QtCore.QRect(115, 435, 330, 125))
        self.pushButton_GoColorMakeup.setStyleSheet('background-color: transparent;'
                                                    'border-bottom-left-radius : 125px; border-bottom-right-radius : 125px')
        self.pushButton_GoColorMakeup.setObjectName("pushButton_GoColorMakeup")

        ## 이동 버튼 background
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(7, 5, 31, 40))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")

        # 이동 버튼 (previous)
        self.pushButton_GoHome = QtWidgets.QPushButton(self)
        self.pushButton_GoHome.setGeometry(QtCore.QRect(10, 12, 25, 25))
        self.pushButton_GoHome.setStyleSheet("border-image: url(image/btn_back.png);")
        self.pushButton_GoHome.setObjectName("pushButton_GoHome")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_GoHome.setFont(font)
        #self.pushButton_GoHome.raise_()
        #self.pushButton_GoHome.setText("<")


