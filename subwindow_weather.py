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
        date_str, rain_str, icon_url, temp_str = weatherInfo.weather_rain()

        '''
        ### 임의로 날씨 데이터 입력 start
        date_str = ["00", "01", "02", "03", "04", "05", "06", "07"]
        rain_str = ["70", "70", "80", "90", "80", "70", "60", "60"]
        icon_url = ["image/ic_small/ic_weather_rain.png", "image/ic_small/ic_weather_rain.png", "image/ic_small/ic_weather_rain.png", "image/ic_small/ic_weather_rain.png",
                    "image/ic_small/ic_weather_rain.png", "image/ic_small/ic_weather_rain.png", "image/ic_small/ic_weather_rain.png", "image/ic_small/ic_weather_rain.png"]
        temp_str = ["25", "25", "24", "24", "25", "24", "25", "26"]
        self.label_TimeOne.setText(date_str[0])
        self.label_TimeTwo.setText(date_str[1])
        self.label_TimeThree.setText(date_str[2])
        self.label_TimeFour.setText(date_str[3])
        self.label_TimeFive.setText(date_str[4])
        self.label_TimeSix.setText(date_str[5])
        self.label_TimeSeven.setText(date_str[6])
        self.label_TimeEight.setText(date_str[7])
        ### 임의로 날씨 데이터 입력 end
        '''

        # 시간
        self.label_TimeOne.setText(date_str[0][-2:])
        self.label_TimeTwo.setText(date_str[1][-2:])
        self.label_TimeThree.setText(date_str[2][-2:])
        self.label_TimeFour.setText(date_str[3][-2:])
        self.label_TimeFive.setText(date_str[4][-2:])
        self.label_TimeSix.setText(date_str[5][-2:])
        self.label_TimeSeven.setText(date_str[6][-2:])
        self.label_TimeEight.setText(date_str[7][-2:])

        # 강수 확률
        self.label_RainOne.setText(rain_str[0] + "%")
        self.label_RainTwo.setText(rain_str[1] + "%")
        self.label_RainThree.setText(rain_str[2] + "%")
        self.label_RainFour.setText(rain_str[3] + "%")
        self.label_RainFive.setText(rain_str[4] + "%")
        self.label_RainSix.setText(rain_str[5] + "%")
        self.label_RainSeven.setText(rain_str[6] + "%")
        self.label_RainEight.setText(rain_str[7] + "%")
        # 온도
        self.label_TempOne.setText(temp_str[0] + "℃")
        self.label_TempTwo.setText(temp_str[1] + "℃")
        self.label_TempThree.setText(temp_str[2] + "℃")
        self.label_TempFour.setText(temp_str[3] + "℃")
        self.label_TempFive.setText(temp_str[4] + "℃")
        self.label_TempSix.setText(temp_str[5] + "℃")
        self.label_TempSeven.setText(temp_str[6] + "℃")
        self.label_TempEight.setText(temp_str[7] + "℃")
        # 날씨
        self.label_WeatherIconOne.setStyleSheet("border-image: url(" + icon_url[0] + "); background-color: #EEEEEE;")
        self.label_WeatherIconTwo.setStyleSheet("border-image: url(" + icon_url[1] + "); background-color: #EEEEEE")
        self.label_WeatherIconThree.setStyleSheet("border-image: url(" + icon_url[2] + "); background-color: #EEEEEE")
        self.label_WeatherIconFour.setStyleSheet("border-image: url(" + icon_url[3] + "); background-color: #EEEEEE")
        self.label_WeatherIconFive.setStyleSheet("border-image: url(" + icon_url[4] + "); background-color: #EEEEEE")
        self.label_WeatherIconSix.setStyleSheet("border-image: url(" + icon_url[5] + "); background-color: #EEEEEE")
        self.label_WeatherIconSeven.setStyleSheet("border-image: url(" + icon_url[6] + "); background-color: #EEEEEE")
        self.label_WeatherIconEight.setStyleSheet("border-image: url(" + icon_url[7] + "); background-color: #EEEEEE")

    def initUI(self):
        # self.setWindowTitle('WEATHER')
        self.resize(760, 350)
        self.setStyleSheet('background-color:white;')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        ## 상단 타이틀 바
        self.label_titlebar = QtWidgets.QLabel(self)
        self.label_titlebar.setObjectName("label_titlebar")
        self.label_titlebar.setMaximumHeight(90)
        self.label_titlebar.setMinimumHeight(90)
        self.label_titlebar.setStyleSheet('background-color:#B5A4E7')

        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(40, 0, 180, 90))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setText("WEATHER")
        self.label_title.setStyleSheet('background-color:transparent; color:white;')

        self.label_subtitle = QtWidgets.QLabel(self)
        self.label_subtitle.setGeometry(QtCore.QRect(220, 10, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_subtitle.setFont(font)
        self.label_subtitle.setText("온도 - 날씨 - 시간 - 강수확률 순")
        self.label_subtitle.setStyleSheet('background-color:transparent; color:white;')

        self.pushButton_Close = QtWidgets.QPushButton(self)
        self.pushButton_Close.setGeometry(QtCore.QRect(670, 0, 90, 90))
        self.pushButton_Close.setObjectName("pushButton_Close")
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setText("×")
        self.pushButton_Close.setStyleSheet('background-color:#B5A4E7; color:white;')
        self.pushButton_Close.clicked.connect(self.CloseClieked)

        # 온도(Temperature)
        font_T = QtGui.QFont()
        font_T.setPointSize(18)
        font_T.setFamily("Segoe MDL2 Assets")

        self.label_TempOne = QtWidgets.QLabel(self)
        self.label_TempOne.setFont(font_T)
        self.label_TempOne.setAlignment(Qt.AlignCenter)


        self.label_TempTwo = QtWidgets.QLabel(self)
        self.label_TempTwo.setFont(font_T)
        self.label_TempTwo.setAlignment(Qt.AlignCenter)

        self.label_TempThree = QtWidgets.QLabel(self)
        self.label_TempThree.setFont(font_T)
        self.label_TempThree.setAlignment(Qt.AlignCenter)

        self.label_TempFour = QtWidgets.QLabel(self)
        self.label_TempFour.setFont(font_T)
        self.label_TempFour.setAlignment(Qt.AlignCenter)

        self.label_TempFive = QtWidgets.QLabel(self)
        self.label_TempFive.setFont(font_T)
        self.label_TempFive.setAlignment(Qt.AlignCenter)

        self.label_TempSix = QtWidgets.QLabel(self)
        self.label_TempSix.setFont(font_T)
        self.label_TempSix.setAlignment(Qt.AlignCenter)

        self.label_TempSeven = QtWidgets.QLabel(self)
        self.label_TempSeven.setFont(font_T)
        self.label_TempSeven.setAlignment(Qt.AlignCenter)

        self.label_TempEight = QtWidgets.QLabel(self)
        self.label_TempEight.setFont(font_T)
        self.label_TempEight.setAlignment(Qt.AlignCenter)

        # 날씨 아이콘
        self.label_WeatherIconOne = QtWidgets.QLabel(self)
        self.label_WeatherIconOne.setMinimumSize(80, 80)
        self.label_WeatherIconOne.setStyleSheet('background-color:#EEEEEE')

        self.label_WeatherIconTwo = QtWidgets.QLabel(self)
        self.label_WeatherIconTwo.setMinimumSize(80, 80)
        self.label_WeatherIconTwo.setStyleSheet('background-color:#EEEEEE')

        self.label_WeatherIconThree = QtWidgets.QLabel(self)
        self.label_WeatherIconThree.setMinimumSize(80, 80)
        self.label_WeatherIconThree.setStyleSheet('background-color:#EEEEEE')

        self.label_WeatherIconFour = QtWidgets.QLabel(self)
        self.label_WeatherIconFour.setMinimumSize(80, 80)
        self.label_WeatherIconFour.setStyleSheet('background-color:#EEEEEE')

        self.label_WeatherIconFive = QtWidgets.QLabel(self)
        self.label_WeatherIconFive.setMinimumSize(80, 80)
        self.label_WeatherIconFive.setStyleSheet('background-color:#EEEEEE')

        self.label_WeatherIconSix = QtWidgets.QLabel(self)
        self.label_WeatherIconSix.setMinimumSize(80, 80)
        self.label_WeatherIconSix.setStyleSheet('background-color:#EEEEEE')

        self.label_WeatherIconSeven = QtWidgets.QLabel(self)
        self.label_WeatherIconSeven.setMinimumSize(80, 80)
        self.label_WeatherIconSeven.setStyleSheet('background-color:#EEEEEE')

        self.label_WeatherIconEight = QtWidgets.QLabel(self)
        self.label_WeatherIconEight.setMinimumSize(80, 80)
        self.label_WeatherIconEight.setStyleSheet('background-color:#EEEEEE')

        # 시간
        font_T2 = QtGui.QFont()
        font_T2.setPointSize(20)
        font_T2.setBold(True)
        font_T2.setFamily("Segoe MDL2 Assets")

        self.label_TimeOne = QtWidgets.QLabel(self)
        self.label_TimeOne.setFont(font_T2)
        self.label_TimeOne.setAlignment(Qt.AlignCenter)
        self.label_TimeOne.setMinimumSize(70, 45)
        # self.label_TimeOne.setMaximumSize(70, 45)
        self.label_TimeOne.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        self.label_TimeTwo = QtWidgets.QLabel(self)
        self.label_TimeTwo.setFont(font_T2)
        self.label_TimeTwo.setAlignment(Qt.AlignCenter)
        self.label_TimeTwo.setMinimumSize(70, 45)
        self.label_TimeTwo.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        self.label_TimeThree = QtWidgets.QLabel(self)
        self.label_TimeThree.setFont(font_T2)
        self.label_TimeThree.setAlignment(Qt.AlignCenter)
        self.label_TimeThree.setMinimumSize(70, 45)
        self.label_TimeThree.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        self.label_TimeFour = QtWidgets.QLabel(self)
        self.label_TimeFour.setFont(font_T2)
        self.label_TimeFour.setAlignment(Qt.AlignCenter)
        self.label_TimeFour.setMinimumSize(70, 45)
        self.label_TimeFour.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        self.label_TimeFive = QtWidgets.QLabel(self)
        self.label_TimeFive.setFont(font_T2)
        self.label_TimeFive.setAlignment(Qt.AlignCenter)
        self.label_TimeFive.setMinimumSize(70, 45)
        self.label_TimeFive.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        self.label_TimeSix = QtWidgets.QLabel(self)
        self.label_TimeSix.setFont(font_T2)
        self.label_TimeSix.setAlignment(Qt.AlignCenter)
        self.label_TimeSix.setMinimumSize(70, 45)
        self.label_TimeSix.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        self.label_TimeSeven = QtWidgets.QLabel(self)
        self.label_TimeSeven.setFont(font_T2)
        self.label_TimeSeven.setAlignment(Qt.AlignCenter)
        self.label_TimeSeven.setMinimumSize(70, 45)
        self.label_TimeSeven.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        self.label_TimeEight = QtWidgets.QLabel(self)
        self.label_TimeEight.setFont(font_T2)
        self.label_TimeEight.setAlignment(Qt.AlignCenter)
        self.label_TimeEight.setMinimumSize(70, 45)
        self.label_TimeEight.setStyleSheet('background-color:black; color:white; border-radius:20px;')

        # 강수 확률
        font_R = QtGui.QFont()
        font_R.setPointSize(14)
        font_R.setFamily("Segoe MDL2 Assets")

        self.label_RainOne = QtWidgets.QLabel(self)
        self.label_RainOne.setFont(font_R)
        self.label_RainOne.setAlignment(Qt.AlignCenter)

        self.label_RainTwo = QtWidgets.QLabel(self)
        self.label_RainTwo.setFont(font_R)
        self.label_RainTwo.setAlignment(Qt.AlignCenter)

        self.label_RainThree = QtWidgets.QLabel(self)
        self.label_RainThree.setFont(font_R)
        self.label_RainThree.setAlignment(Qt.AlignCenter)

        self.label_RainFour = QtWidgets.QLabel(self)
        self.label_RainFour.setFont(font_R)
        self.label_RainFour.setAlignment(Qt.AlignCenter)

        self.label_RainFive = QtWidgets.QLabel(self)
        self.label_RainFive.setFont(font_R)
        self.label_RainFive.setAlignment(Qt.AlignCenter)

        self.label_RainSix = QtWidgets.QLabel(self)
        self.label_RainSix.setFont(font_R)
        self.label_RainSix.setAlignment(Qt.AlignCenter)

        self.label_RainSeven = QtWidgets.QLabel(self)
        self.label_RainSeven.setFont(font_R)
        self.label_RainSeven.setAlignment(Qt.AlignCenter)

        self.label_RainEight = QtWidgets.QLabel(self)
        self.label_RainEight.setFont(font_R)
        self.label_RainEight.setAlignment(Qt.AlignCenter)

        ## 레이아웃 배치
        titlebar = QHBoxLayout()
        titlebar.setContentsMargins(0, 0, 0, 0)
        titlebar.addWidget(self.label_titlebar)

        gbox = QGridLayout()
        gbox.setContentsMargins(30, 10, 30, 15)
        gbox.addWidget(self.label_TempOne, 0, 0)
        gbox.addWidget(self.label_TempTwo, 0, 1)
        gbox.addWidget(self.label_TempThree, 0, 2)
        gbox.addWidget(self.label_TempFour, 0, 3)
        gbox.addWidget(self.label_TempFive, 0, 4)
        gbox.addWidget(self.label_TempSix, 0, 5)
        gbox.addWidget(self.label_TempSeven, 0, 6)
        gbox.addWidget(self.label_TempEight, 0, 7)

        gbox.addWidget(self.label_WeatherIconOne, 1, 0)
        gbox.addWidget(self.label_WeatherIconTwo, 1, 1)
        gbox.addWidget(self.label_WeatherIconThree, 1, 2)
        gbox.addWidget(self.label_WeatherIconFour, 1, 3)
        gbox.addWidget(self.label_WeatherIconFive, 1, 4)
        gbox.addWidget(self.label_WeatherIconSix, 1, 5)
        gbox.addWidget(self.label_WeatherIconSeven, 1, 6)
        gbox.addWidget(self.label_WeatherIconEight, 1, 7)

        gbox.addWidget(self.label_TimeOne, 2, 0, Qt.AlignCenter)
        gbox.addWidget(self.label_TimeTwo, 2, 1, Qt.AlignCenter)
        gbox.addWidget(self.label_TimeThree, 2, 2, Qt.AlignCenter)
        gbox.addWidget(self.label_TimeFour, 2, 3, Qt.AlignCenter)
        gbox.addWidget(self.label_TimeFive, 2, 4, Qt.AlignCenter)
        gbox.addWidget(self.label_TimeSix, 2, 5, Qt.AlignCenter)
        gbox.addWidget(self.label_TimeSeven, 2, 6, Qt.AlignCenter)
        gbox.addWidget(self.label_TimeEight, 2, 7, Qt.AlignCenter)

        gbox.addWidget(self.label_RainOne, 3, 0)
        gbox.addWidget(self.label_RainTwo, 3, 1)
        gbox.addWidget(self.label_RainThree, 3, 2)
        gbox.addWidget(self.label_RainFour, 3, 3)
        gbox.addWidget(self.label_RainFive, 3, 4)
        gbox.addWidget(self.label_RainSix, 3, 5)
        gbox.addWidget(self.label_RainSeven, 3, 6)
        gbox.addWidget(self.label_RainEight, 3, 7)

        layout.addLayout(titlebar)
        layout.addLayout(gbox)

        self.setLayout(layout)

    def showModal(self):  # 새 Modal 창이 열렸을 경우 기존에 있던 창을 사용하지 못하는 방식입니다.
        return super().exec_()

    def CloseClieked(self):
        self.reject()