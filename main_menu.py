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
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(97, 600, 342, 50))
        #self.pushButton_GoPersonalColor.setStyleSheet('background-color: #B5A4E7; '
        #                                           'border-top-left-radius : 50px; border-top-right-radius:50px')
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoPersonalColor.setFont(font)
        self.pushButton_GoPersonalColor.setText("PERSONAL COLOR")


        self.pushButton_GoBaseMakeupVideo = QtWidgets.QPushButton(self)
        self.pushButton_GoBaseMakeupVideo.setGeometry(QtCore.QRect(97, 650, 342, 50))
        #self.pushButton_GoBaseMakeupVideo.setStyleSheet('background-color: #B5A4E7;')
        self.pushButton_GoBaseMakeupVideo.setObjectName("pushButton_GoBaseMakeupVideo")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoBaseMakeupVideo.setFont(font)
        self.pushButton_GoBaseMakeupVideo.setText("BASE MAKEUP VIDEO")


        self.pushButton_GoColorMakeup = QtWidgets.QPushButton(self)
        self.pushButton_GoColorMakeup.setGeometry(QtCore.QRect(97, 700, 342, 50))
        #self.pushButton_GoColorMakeup.setStyleSheet('background-color: #B5A4E7; '
        #                                              'border-bottom-left-radius : 50px; border-bottom-right-radius : 50px')
        self.pushButton_GoColorMakeup.setObjectName("pushButton_GoColorMakeup")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoColorMakeup.setFont(font)
        self.pushButton_GoColorMakeup.setText("COLOR MAKEUP")



        ## 메모 : 125px / 높이 차례대로 130 88 130

