import sys
from weather import weatherInfo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class SubWindow_Weather(QDialog): #QDialog
    def __init__(self):
        super().__init__()
        self.initUI()
        timer2 = QtCore.QTimer(self, interval=1800000, timeout=self.showWeather)  ## 30분
        timer2.start()
        self.showWeather()

    def showWeather(self):
        date_str, rain_str = weatherInfo.weather_rain()
        text=[]
        for i in range(0,8):
            text.append(date_str[i][-2:] + "시 : " + rain_str[i] + "%")
        textWeather = text[0]+"\n"+text[1]+"\n"+text[2]+"\n"+text[3]+"\n"+text[4]+"\n"+text[5]+"\n"+text[6]+"\n"+text[7]
        self.label_Info.setText(textWeather)

    def initUI(self):
        #self.setWindowTitle('WEATHER')
        self.resize(400,400)
        self.setStyleSheet('background-color:white;')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        ## 상단 타이틀 바
        self.label_titlebar = QtWidgets.QLabel(self)
        self.label_titlebar.setObjectName("label_titlebar")
        self.label_titlebar.setMaximumHeight(35)
        self.label_titlebar.setStyleSheet('background-color:#B5A4E7')

        self.pushButton_Close = QtWidgets.QPushButton(self)
        self.pushButton_Close.setGeometry(QtCore.QRect(365, 0, 35, 35))
        self.pushButton_Close.setObjectName("pushButton_Close")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setText("X")
        self.pushButton_Close.setStyleSheet('background-color:#B5A4E7; color:white;')
        self.pushButton_Close.clicked.connect(self.CloseClieked)

        self.label_Info = QtWidgets.QLabel(self)
        self.label_Info.setObjectName("label_Info")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Info.setFont(font)
        self.label_Info.setText("")
        self.label_Info.setAlignment(Qt.AlignCenter)

        ## 레이아웃 배치
        titlebar = QHBoxLayout()
        titlebar.setContentsMargins(0, 0, 0, 0)
        titlebar.addWidget(self.label_titlebar)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label_Info)

        layout.addLayout(titlebar)
        layout.addLayout(hbox)

        self.setLayout(layout)

    def showModal(self): #새 Modal 창이 열렸을 경우 기존에 있던 창을 사용하지 못하는 방식입니다.
        return super().exec_()

    def CloseClieked(self):
        self.reject()