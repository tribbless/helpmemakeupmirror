from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Personal_Color(QWidget):

    def __init__(self):
        super(Personal_Color, self).__init__()


        # 쌩얼 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(180, 130, 664, 498))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_face.setFont(font)
        self.label_face.setText("you didn't capture")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # tone info text
        self.label_tone = QtWidgets.QLabel(self)
        self.label_tone.setGeometry(QtCore.QRect(297, 648, 430, 100))
        self.label_tone.setObjectName("label_tone")
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_tone.setFont(font)
        self.label_tone.setAlignment(Qt.AlignCenter)
        self.label_tone.setText("Unknown TONE")
        self.label_tone.setStyleSheet("color: white;;")

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(92, 768, 840, 371))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 30px;")
        self.label_background_white.lower()

        # 퍼스널 컬러 정보 background image
        self.label_background_manual = QtWidgets.QLabel(self)
        self.label_background_manual.setGeometry(QtCore.QRect(102, 778, 820, 351))
        self.label_background_manual.setObjectName("label_background_manual")
        self.label_background_manual.setStyleSheet("border-radius: 20px;"
                                                   "border-image: url(image/personal_background_btn.png);")
        # 컬러 추천 text
        self.label_rec = QtWidgets.QLabel(self)
        self.label_rec.setGeometry(QtCore.QRect(142, 804, 370, 50))
        self.label_rec.setObjectName("label_rec")
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label_rec.setFont(font)
        self.label_rec.setText("★ MAKEUP COLOR 추천")

        # 다구 색상표표
        self.label_bigColor = QtWidgets.QLabel(self)
        self.label_bigColor.setGeometry(QtCore.QRect(413, 880, 300, 220))
        self.label_bigColor.setObjectName("label_bigColor")
        self.label_bigColor.setStyleSheet("background-color:white;")


        ## 4구 색상표

        # background
        self.label_smallColor = QtWidgets.QLabel(self)
        self.label_smallColor.setGeometry(QtCore.QRect(142, 880, 240, 220))
        self.label_smallColor.setObjectName("label_smallColor")
        self.label_smallColor.setStyleSheet("background-color: white;")

        smallFont = QtGui.QFont()
        smallFont.setPointSize(30)
        # 첫번째 색상
        self.label_smallColor_One = QtWidgets.QLabel(self)
        self.label_smallColor_One.setGeometry(QtCore.QRect(158, 896, 100, 90))
        self.label_smallColor_One.setObjectName("label_smallColor_One")
        self.label_smallColor_One.setFont(smallFont)
        self.label_smallColor_One.setText("1")
        self.label_smallColor_One.setAlignment(Qt.AlignCenter)
        #self.label_smallColor_One.setStyleSheet("background-color: #EE572A; color: white;")
        self.label_smallColor_One.hide()

        # 두번째 색상
        self.label_smallColor_Two = QtWidgets.QLabel(self)
        self.label_smallColor_Two.setGeometry(QtCore.QRect(266, 896, 100, 90))
        self.label_smallColor_Two.setObjectName("label_smallColor_Two")
        self.label_smallColor_Two.setFont(smallFont)
        self.label_smallColor_Two.setText("2")
        self.label_smallColor_Two.setAlignment(Qt.AlignCenter)
        self.label_smallColor_Two.setStyleSheet("background-color: #B96407; color: white;")
        self.label_smallColor_Two.hide()

        # 세번째 색상
        self.label_smallColor_Three = QtWidgets.QLabel(self)
        self.label_smallColor_Three.setGeometry(QtCore.QRect(158, 994, 100, 90))
        self.label_smallColor_Three.setObjectName("label_smallColor_Three")
        self.label_smallColor_Three.setFont(smallFont)
        self.label_smallColor_Three.setText("3")
        self.label_smallColor_Three.setAlignment(Qt.AlignCenter)
        self.label_smallColor_Three.setStyleSheet("background-color: #F06050; color: white;")
        self.label_smallColor_Three.hide()

        # 네번째 색상
        self.label_smallColor_Four = QtWidgets.QLabel(self)
        self.label_smallColor_Four.setGeometry(QtCore.QRect(266, 994, 100, 90))
        self.label_smallColor_Four.setObjectName("label_smallColor_Four")
        self.label_smallColor_Four.setFont(smallFont)
        self.label_smallColor_Four.setText("4")
        self.label_smallColor_Four.setAlignment(Qt.AlignCenter)
        self.label_smallColor_Four.setStyleSheet("background-color: #F2824B; color: white;")
        self.label_smallColor_Four.hide()

        # 메인 메뉴로 가는 버튼
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(745, 882, 144, 192))
        self.pushButton_GoMainMenu.setStyleSheet('background-color:transparent; border: 0px;')
        self.pushButton_GoMainMenu.setObjectName("pushButton_GoMainMenu")
        #self.pushButton_GoMainMenu.setStyleSheet("border-style: dashed;"
        #                                         "border-width: 3px;"
        #                                         "border-color: red;")

        # 이동 버튼 image
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(25, 22, 45, 45))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("border-image: url(image/btn_back.png);")

        ## 이동 버튼 (previous)
        self.pushButton_GoBareFaceCapture = QtWidgets.QPushButton(self)
        self.pushButton_GoBareFaceCapture.setGeometry(QtCore.QRect(23, 9, 55, 72))
        self.pushButton_GoBareFaceCapture.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                        "border-radius: 10px;")
        self.pushButton_GoBareFaceCapture.setObjectName("pushButton_GoBareFaceCapture")

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        '''
            봄웜톤(spring) : SPRING WARM
            가을웜톤(fall) : FALL WARM
            여름쿨톤(summer) : SUMMER COOL
            겨울쿨톤(winter) : WINTER COOL
        '''

    def big_color_show(self, tone):
        if tone == "SPRING WARM":
            self.label_bigColor.setStyleSheet("border-image: url(image/personal_palette_spring.png);")
        elif tone == "SUMMER COOL":
            self.label_bigColor.setStyleSheet("border-image: url(image/personal_palette_summer.png);")
        elif tone == "FALL WARM":
            self.label_bigColor.setStyleSheet("border-image: url(image/personal_palette_fall.png);")
        elif tone == "WINTER COOL":
            self.label_bigColor.setStyleSheet("border-image: url(image/personal_palette_winter.png);")

    def small_color_show(self, tone):
        if tone == "SPRING WARM":
            one = "EE572A"
            two = "B96407"
            three = "F06050"
            four = "F2824B"
        elif tone == "SUMMER COOL":
            one = "CB93BB"
            two = "F2A8C6"
            three = "981332"
            four = "ED4696"
        elif tone == "FALL WARM":
            one = "C36665"
            two = "BA393D"
            three = "F6A68B"
            four = "A0542D"
        elif tone == "WINTER COOL":
            one = "E589D1"
            two = "C62481"
            three = "941452"
            four = "521C2C"
        self.label_smallColor_One.setStyleSheet("background-color: #"+one+"; color: white;")
        self.label_smallColor_Two.setStyleSheet("background-color: #"+two+"; color: white;")
        self.label_smallColor_Three.setStyleSheet("background-color: #"+three+"; color: white;")
        self.label_smallColor_Four.setStyleSheet("background-color: #"+four+"; color: white;")
        self.label_smallColor_One.show()
        self.label_smallColor_Two.show()
        self.label_smallColor_Three.show()
        self.label_smallColor_Four.show()

    def reset(self):
        self.label_face.clear()
        self.label_face.setText("you didn't capture")
        self.label_tone.setText("Unknown TONE")
        self.label_bigColor.setStyleSheet("background-color:white;")
        self.label_smallColor_One.hide()
        self.label_smallColor_Two.hide()
        self.label_smallColor_Three.hide()
        self.label_smallColor_Four.hide()





