'''
0. 홈 [home.py]
1. 메인메뉴 [main_menu.py]
 -> personal color
 -> base makeup video
 -> color makeup

2.
 2-1)쌩얼 캡쳐 [bareFace_capture.py] ~ 퍼스널 컬러
 2-2)베이스 메이크업 [base_makeup_video.py] ~ 메이크업 캡쳐
 2-3)메이크업 캡쳐 [makeupFace_capture.py] ~ 서브메뉴

3. 퍼스널 컬러 [personalColor.py] ~ 쌩얼 캡쳐

4. 서브 메뉴
 -> SELECT BY FACE
 -> SELECT BY THEMA

5.
 5-1) SELECT BY FACE [select_face_*.py]~ 프레임
 눈썹, 아이새도우, 아이라이너, 블러셔, 립 총 5가지 화면
 5-2)SELECT BY THEMA [select_thema.py] ~ 프레임

6. FRAME [frame_*.py] ~ 비교화면
  눈썹, 아이새됴우, 아이라이너, 블러셔, 립 총 5가지 화면.

7. 비교화면 [RealFace_ARFace_compare.py] ~ 홈
홈버튼(홈버튼)과 공유버튼이 있다.
'''
import sys, os

import cv2

from weather import weatherInfo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from home import Home
from main_menu import Main_Menu

from bareFace_capture import BareFace_Capture
from base_makeup_video import Base_Makeup_Video
from makeupFace_capture import MakeupFace_Capture
from personal_color import Personal_Color

from sub_menu import Sub_Menu

from select_thema import Select_Thema
from select_face_eyebrow import Select_face_Eyebrow
from select_face_eyeshadow import Select_face_Eyeshadow
from select_face_eyeliner import Select_face_Eyeliner
from select_face_blusher import Select_face_Blusher
from select_face_lip import Select_face_Lip


from frame_eyebrow import Frame_Eyebrow
from frame_eyeshadow import Frame_Eyeshadow
from frame_eyeliner import Frame_Eyeliner
from frame_blusher import Frame_Blusher
from frame_lip import Frame_Lip

from RealFace_ARFace_compare import RealFace_ARFace_Compare
from subwindow_menuShortcut import SubWindow_MenuShortcut
from subwindow_weather import SubWindow_Weather

##### python -m PyQt5.uic.pyuic -x ex_02.ui -o ex_02.py
##### "border-style: dashed; border-width: 3px; border-color: red;

class MAIN_StackedWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.stk_w = QStackedWidget(self)
        self.setupUi()
        timer1 = QtCore.QTimer(self, interval=1000, timeout=self.showDateTime) ## 1000이 1초 / 60000 1분
        timer1.start()
        self.showDateTime()
        timer2 = QtCore.QTimer(self, interval=300000, timeout=self.showWeather) ## 5분
        timer2.start()
        self.showWeather()
        self.menuShortcut = SubWindow_MenuShortcut()
        self.weather = SubWindow_Weather()

    def showDateTime(self):
        date = QtCore.QDate.currentDate()
        time = QtCore.QTime.currentTime()
        textDate = date.toString(Qt.ISODate)
        textTime = time.toString("HH:mm")
        text2 = time.toString("AP")

        if text2=="오전":
            textTime=textTime+" AM"
        else:
            textTime=textTime+" PM"
        self.label_DateTime.setText(textDate+"\n"+textTime)

    def showWeather(self):
        today_temp, icon_url = weatherInfo.weather()
        # 온도/날씨
        self.label_Temperature.setText(today_temp + "℃")  # °
        self.label_WeatherIcon.setStyleSheet("border-image: url(" + icon_url[0] + ")")


    def setupUi(self):
        self.setWindowTitle("Help Me MakeUp Mirror")
        #self.resize(562, 794)
        #self.move(0, -200)
        self.resize(1024, 1256)
        #self.center()
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setStyleSheet("background-color:transparent;")
        ## 나중에 jetson nano 화면을 회전해야함.


        widget_laytout = QHBoxLayout()

        self.home = Home()
        self.main_menu = Main_Menu()
        self.bareFace_capture = BareFace_Capture()
        self.base_makeup_video = Base_Makeup_Video()
        self.makeupFace_capture = MakeupFace_Capture()
        self.personal_color = Personal_Color()

        self.sub_menu = Sub_Menu()

        self.select_thema = Select_Thema()

        self.select_face_eyebrow = Select_face_Eyebrow()
        self.select_face_eyeshadow = Select_face_Eyeshadow()
        self.select_face_eyeliner = Select_face_Eyeliner()
        self.select_face_blusher = Select_face_Blusher()
        self.select_face_lip = Select_face_Lip()

        self.frame_eyebrow = Frame_Eyebrow()
        self.frame_eyeshadow = Frame_Eyeshadow()
        self.frame_eyeliner = Frame_Eyeliner()
        self.frame_blusher = Frame_Blusher()
        self.frame_lip = Frame_Lip()

        self.Real_AR_Face_compare = RealFace_ARFace_Compare()


        self.stk_w.addWidget(self.home)
        self.stk_w.addWidget(self.main_menu)
        self.stk_w.addWidget(self.bareFace_capture)
        self.stk_w.addWidget(self.base_makeup_video)
        self.stk_w.addWidget(self.makeupFace_capture)
        self.stk_w.addWidget(self.personal_color)

        self.stk_w.addWidget(self.sub_menu)

        self.stk_w.addWidget(self.select_thema)

        self.stk_w.addWidget(self.select_face_eyebrow)
        self.stk_w.addWidget(self.select_face_eyeshadow)
        self.stk_w.addWidget(self.select_face_eyeliner)
        self.stk_w.addWidget(self.select_face_blusher)
        self.stk_w.addWidget(self.select_face_lip)

        self.stk_w.addWidget(self.frame_eyebrow)
        self.stk_w.addWidget(self.frame_eyeshadow)
        self.stk_w.addWidget(self.frame_eyeliner)
        self.stk_w.addWidget(self.frame_blusher)
        self.stk_w.addWidget(self.frame_lip)

        self.stk_w.addWidget(self.Real_AR_Face_compare)

        widget_laytout.addWidget(self.stk_w)
        widget_laytout.setContentsMargins(0,0,0,0)


        self.setLayout(widget_laytout)


        ## 화면전환 NEXT

        self.home.pushButton_GoMainMenu.clicked.connect(self.goToMainMenu)
        self.main_menu.pushButton_GoPersonalColor.clicked.connect(self.goToBareFaceCapture)
        self.main_menu.pushButton_GoBaseMakeupVideo.clicked.connect(self.goToBaseMakeupVideo)
        self.main_menu.pushButton_GoColorMakeup.clicked.connect(self.goToMakeupFaceCapture)

        self.bareFace_capture.pushButton_GoPersonalColor.clicked.connect(self.goToPersonalColor)
        self.personal_color.pushButton_GoMainMenu.clicked.connect(self.goToMainMenu)
        self.base_makeup_video.pushButton_GoColorMakeup.clicked.connect(self.goToMakeupFaceCapture_Later)
        self.makeupFace_capture.pushButton_GoSubMenu.clicked.connect(self.goToSubMenu)
        self.sub_menu.pushButton_GoSelectThema.clicked.connect(self.goToThema)
        self.select_thema.pushButton_GoEyebrowFrame.clicked.connect(self.goToEyebrowFrame)

        self.sub_menu.pushButton_GoSelectFace.clicked.connect(self.goToEyebrowAR)
        self.select_face_eyebrow.pushButton_GoEyeshadowAR.clicked.connect(self.goToEyeshadowAR)
        self.select_face_eyeshadow.pushButton_GoEyelinerAR.clicked.connect(self.goToEyelinerAR)
        self.select_face_eyeliner.pushButton_GoBlusherAR.clicked.connect(self.goToBlusherAR)
        self.select_face_blusher.pushButton_GoLipAR.clicked.connect(self.goToLipAR)
        self.select_face_lip.pushButton_GoEyebrowFrame.clicked.connect(self.goToEyebrowFrame)

        self.frame_eyebrow.pushButton_GoEyesahdowFrame.clicked.connect(self.goToEyeshadowFrame)
        self.frame_eyeshadow.pushButton_GoEyelinerFrame.clicked.connect(self.goToEyelinerFrame)
        self.frame_eyeliner.pushButton_GoBlusherFrame.clicked.connect(self.goToBlusherFrame)
        self.frame_blusher.pushButton_GoLipFrame.clicked.connect(self.goToLipFrame)
        self.frame_lip.pushButton_GoCompare.clicked.connect(self.goToCompare)

        ## 화면전환 PREVIOUS
        self.main_menu.pushButton_GoHome.clicked.connect(self.goToHome)
        self.bareFace_capture.pushButton_GoMainMenu.clicked.connect(self.goToMainMenu)
        self.personal_color.pushButton_GoBareFaceCapture.clicked.connect(self.goToBareFaceCapture)
        self.base_makeup_video.pushButton_GoMainMenu.clicked.connect(self.goToMainMenu)
        self.makeupFace_capture.pushButton_GoMainMENUorVideo.clicked.connect(self.goToMainMENUorVideo)
        self.sub_menu.pushButton_GoMakeupFaceCapture.clicked.connect(self.goToMakeupFaceCapture_Later)

        self.select_thema.pushButton_GoSubMenu.clicked.connect(self.goToSubMenu_Later)
        self.select_face_eyebrow.pushButton_GoSubMenu.clicked.connect(self.goToSubMenu_Later)
        self.select_face_eyeshadow.pushButton_GoEyebrowAR.clicked.connect(self.goToEyebrowARLater)
        self.select_face_eyeliner.pushButton_GoEyeshadowAR.clicked.connect(self.goToEyeshadowARLater)
        self.select_face_blusher.pushButton_GoEyelinerAR.clicked.connect(self.goToEyelinerARLater)
        self.select_face_lip.pushButton_GoBlusherAR.clicked.connect(self.goToBlusherARLater)

        self.frame_eyebrow.pushButton_GoARorThema.clicked.connect(self.goToLipARorTHEMA)
        self.frame_eyeshadow.pushButton_GoEyebrowFrame.clicked.connect(self.goToEyebrowFrame)
        self.frame_eyeliner.pushButton_GoEyeshadowFrame.clicked.connect(self.goToEyeshadowFrame)
        self.frame_blusher.pushButton_GoEyelinerFrame.clicked.connect(self.goToEyelinerFrame)
        self.frame_lip.pushButton_GoBlusherFrame.clicked.connect(self.goToBlusherFrame)

        self.Real_AR_Face_compare.pushButton_GoHome.clicked.connect(self.goToHome)
        self.Real_AR_Face_compare.pushButton_GoLipFrame.clicked.connect(self.goToLipFrame)


        '''고정값'''
        ## 나는 뒷배경~~
        self.label_back_background = QtWidgets.QLabel(self)
        self.label_back_background.setGeometry(QtCore.QRect(0, 90, 1024, 1094))
        self.label_back_background.setStyleSheet("background-color: black;")
        self.label_back_background.lower()
        self.label_back_background.hide()

        ## 상단 타이틀바 background
        self.label_background_TitleBar = QtWidgets.QLabel(self)
        self.label_background_TitleBar.setGeometry(QtCore.QRect(0, 0, 1024, 92))
        self.label_background_TitleBar.setObjectName("label_background_TitleBar")
        self.label_background_TitleBar.setStyleSheet("border-image: url(image/background.png);")
        self.label_background_TitleBar.lower()
        self.label_background_TitleBar.hide()


        ## 시간/날짜
        self.label_DateTime = QtWidgets.QLabel(self)
        self.label_DateTime.setGeometry(QtCore.QRect(513, 0, 198, 92))
        self.label_DateTime.setObjectName("label_DateTime")
        font = QtGui.QFont()
        font.setPointSize(20) # 11
        self.label_DateTime.setFont(font)
        self.label_DateTime.setText("")
        self.label_DateTime.setAlignment(Qt.AlignCenter)
        self.label_DateTime.hide()

        ## 온도
        self.label_Temperature = QtWidgets.QLabel(self)
        self.label_Temperature.setGeometry(QtCore.QRect(819, 36, 63, 45))
        self.label_Temperature.setObjectName("label_Temperature")
        font = QtGui.QFont()
        font.setPointSize(21) #10
        self.label_Temperature.setFont(font)
        self.label_Temperature.setText("")
        self.label_Temperature.setAlignment(Qt.AlignCenter)
        self.label_Temperature.hide()

        ## 날씨 아이콘
        self.label_WeatherIcon = QtWidgets.QLabel(self)
        self.label_WeatherIcon.setGeometry(QtCore.QRect(734, 0, 90, 90))
        self.label_WeatherIcon.setObjectName("label_WeatherIcon")
        self.label_WeatherIcon.hide()

        ## 날씨 버튼
        self.pushButton_Weather = QtWidgets.QPushButton(self)
        self.pushButton_Weather.setGeometry(QtCore.QRect(734, 9, 153, 72))
        self.pushButton_Weather.setObjectName("pushButton_Weather")
        self.pushButton_Weather.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                              "border-radius: 10px;")
        self.pushButton_Weather.clicked.connect(self.goToWeather_Window)
        self.pushButton_Weather.hide()

        ## 메뉴 바로가기 버튼 background
        self.label_background_MenuShortcut = QtWidgets.QLabel(self)
        self.label_background_MenuShortcut.setGeometry(QtCore.QRect(938, 22, 45, 45))
        self.label_background_MenuShortcut.setObjectName("label_background_MenuShortcut")
        self.label_background_MenuShortcut.setStyleSheet("border-image: url(image/btn_menu.png);")
        self.label_background_MenuShortcut.hide()

        ## 메뉴 바로가기 버튼
        self.pushButton_MenuShortcut = QtWidgets.QPushButton(self)
        self.pushButton_MenuShortcut.setGeometry(QtCore.QRect(920, 9, 81, 72))
        self.pushButton_MenuShortcut.setObjectName("pushButton_MenuShortcut")
        self.pushButton_MenuShortcut.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                   "border-radius: 10px;")
        self.pushButton_MenuShortcut.clicked.connect(self.goToMenuShortcut_Window)
        self.pushButton_MenuShortcut.hide()

        ## Shutdown 버튼
        self.Real_AR_Face_compare.pushButton_Shutdown.clicked.connect(self.ShutDown)

        ##
        self.Real_AR_Face_compare.pushButton_Share.clicked.connect(self.goToSubMenu_Later)

        ## 카메라 오픈
        #self.cpt = cv2.VideoCapture(0) ## in window
        self.cpt = cv2.VideoCapture("/dev/video0") ## in jetson nano

    ## 서브 윈도우 화면 나타나기
    def goToWeather_Window(self):
        print("[main.py] 날씨 윈도우화면")
        r = self.weather.showModal()
        if r:
            print("[main.py] --이 메시지는 안나옴--")
        else:
            print("[main.py] close")
    def goToMenuShortcut_Window(self):
        print("[main.py] 메뉴 바로가기 윈도우화면")
        r = self.menuShortcut.showModal()
        if r:
            print("[main.py] 메뉴 바로가기 클릭성공")
            # camera stop
            if self.menuShortcut.btn != 4:
                self.bareFace_capture.flag = False
            if self.menuShortcut.btn != 5:
                self.makeupFace_capture.flag = False
            self.frame_eyebrow.flag = False
            self.frame_eyeshadow.flag = False
            self.frame_eyeliner.flag = False
            self.frame_blusher.flag = False
            self.frame_lip.flag = False
            if(self.menuShortcut.btn==1):
                self.goToHome()
            elif(self.menuShortcut.btn==2):
                self.goToMainMenu()
            elif (self.menuShortcut.btn == 3):
                self.goToBaseMakeupVideo()
            elif (self.menuShortcut.btn == 4):
                self.goToBareFaceCapture()
            elif (self.menuShortcut.btn == 5):
                self.goToMakeupFaceCapture()
            elif (self.menuShortcut.btn == 6):
                self.goToSubMenu()
            else:
                self.ShutDown()
        else:
            print("[main.py] close")

    ## 화면전환 NEXT & PREVIOUS
    def goToMainMenu(self):
        self.label_back_background.show()
        self.label_background_TitleBar.show()
        self.label_DateTime.show()
        self.label_Temperature.show()
        self.label_WeatherIcon.show()
        self.pushButton_Weather.show()
        self.label_background_MenuShortcut.show()
        self.pushButton_MenuShortcut.show()
        self.stk_w.setCurrentWidget(self.main_menu)
    def goToBareFaceCapture(self):
        #print(self.width())
        #print(self.height())
        self.bareFace_capture.action = False
        self.bareFace_capture.label_manual.setText("베이스 메이크업 전 촬영입니다.\n화면을 캡쳐하세요.")
        self.bareFace_capture.cpt = self.cpt
        self.bareFace_capture.start()
        self.stk_w.setCurrentWidget(self.bareFace_capture)
    def goToBaseMakeupVideo(self):
        self.main_menu.btn = "video"
        self.stk_w.setCurrentWidget(self.base_makeup_video)
    def goToMakeupFaceCapture(self):
        self.main_menu.btn = "MakeupFaceCapture"
        self.makeupFace_capture.action = False
        self.makeupFace_capture.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")
        self.makeupFace_capture.cpt = self.cpt
        self.makeupFace_capture.start()
        self.stk_w.setCurrentWidget(self.makeupFace_capture)
    def goToMakeupFaceCapture_Later(self):
        self.makeupFace_capture.action = False
        self.makeupFace_capture.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")
        self.makeupFace_capture.cpt = self.cpt
        self.makeupFace_capture.start()
        self.stk_w.setCurrentWidget(self.makeupFace_capture)

    def goToPersonalColor(self):
        self.bareFace_capture.personal_analysis()
        self.showPersonalColor()
    def showPersonalColor(self):
        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.realPersonalColor)
        self.timer3.setSingleShot(True)
        self.timer3.start(100)  # 0.1초후 실행됨.
    def realPersonalColor(self):
        self.bareFace_capture.personalFace()
        check = self.bareFace_capture.action
        check2 = self.bareFace_capture.result
        print(f"[main.py] check? {check}, check2? {check2}")
        if check == True:
            tone = self.bareFace_capture.tone
            print(tone)
            self.personal_color.label_tone.setText("< " + tone + " >")
            result = self.changePixmap(self.bareFace_capture.bareFace)
            self.personal_color.label_face.setPixmap(QtGui.QPixmap(result).scaled(664, 498, Qt.KeepAspectRatio))
            self.personal_color.big_color_show(tone)
            self.personal_color.small_color_show(tone)
        if check2 == True:
            self.stk_w.setCurrentWidget(self.personal_color)

    def goToMainMENUorVideo(self):
        print(f"[main.py] {self.main_menu.btn}")
        if (self.main_menu.btn == "video"):
            self.stk_w.setCurrentWidget(self.base_makeup_video)
        else:
            self.stk_w.setCurrentWidget(self.main_menu)

    def goToSubMenu(self):
        self.makeupFace_capture.landmark_make()
        self.showSubMenu()

    def showSubMenu(self):
        self.timer4 = QTimer()
        self.timer4.timeout.connect(self.realSubMenu)
        self.timer4.setSingleShot(True)
        self.timer4.start(100)  # 0.1초후 실행됨.

    def realSubMenu(self):
        self.makeupFace_capture.Save_captureFace()
        if self.makeupFace_capture.result == True:
            self.stk_w.setCurrentWidget(self.sub_menu)
        self.makeupFace_capture.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")


    def goToSubMenu_Later(self):
        self.makeupFace_capture.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")
        self.stk_w.setCurrentWidget(self.sub_menu)

    def goToThema(self):
        self.sub_menu.btn = "select_thema" # Frame에서 back버튼 시 활용
        check = self.makeupFace_capture.action
        check2 = self.bareFace_capture.action
        if check == True:
            self.select_thema.makeupFace = self.makeupFace_capture.makeupFace
            self.select_thema.resultFace = self.select_thema.makeupFace
            self.select_thema.landmark = self.makeupFace_capture.landmark
            result = self.changePixmap(self.select_thema.makeupFace)
            self.select_thema.label_face.setPixmap(QtGui.QPixmap(result).scaled(672, 504, Qt.KeepAspectRatio))
            self.select_thema.action = True
        if check2 == True:
            print(f"[main.py] 퍼스널 컬러 진단 결과 : {self.bareFace_capture.tone}")
            self.select_thema.tone = self.bareFace_capture.tone
        self.stk_w.setCurrentWidget(self.select_thema)

    def goToEyebrowAR(self):
        self.sub_menu.btn = "select_face" # Frame에서 back버튼 시 활용
        check = self.makeupFace_capture.action
        if check == True:
            self.select_face_eyebrow.makeupFace = self.makeupFace_capture.makeupFace
            self.select_face_eyebrow.resultFace = self.select_face_eyebrow.makeupFace
            self.select_face_eyebrow.landmark = self.makeupFace_capture.landmark
            result = self.changePixmap(self.select_face_eyebrow.makeupFace)
            self.select_face_eyebrow.label_face.setPixmap(QtGui.QPixmap(result).scaled(672, 504, Qt.KeepAspectRatio))
            self.select_face_eyebrow.action = True
        self.stk_w.setCurrentWidget(self.select_face_eyebrow)
    def goToEyeshadowAR(self):
        check = self.makeupFace_capture.action
        if check == True:
            self.select_face_eyeshadow.makeupFace = self.select_face_eyebrow.resultFace
            self.select_face_eyeshadow.resultFace = self.select_face_eyeshadow.makeupFace
            result = self.changePixmap(self.select_face_eyebrow.resultFace)
            self.select_face_eyeshadow.label_face.setPixmap(QtGui.QPixmap(result).scaled(672, 504, Qt.KeepAspectRatio))
            self.select_face_eyeshadow.action = True
        self.stk_w.setCurrentWidget(self.select_face_eyeshadow)
    def goToEyelinerAR(self):
        check = self.makeupFace_capture.action
        if check == True:
            self.select_face_eyeliner.makeupFace = self.select_face_eyeshadow.resultFace
            self.select_face_eyeliner.resultFace = self.select_face_eyeliner.makeupFace
            self.select_face_eyeliner.landmark = self.makeupFace_capture.landmark
            result = self.changePixmap(self.select_face_eyeshadow.resultFace)
            self.select_face_eyeliner.label_face.setPixmap(QtGui.QPixmap(result).scaled(672, 504, Qt.KeepAspectRatio))
            self.select_face_eyeliner.action = True
        self.stk_w.setCurrentWidget(self.select_face_eyeliner)
    def goToBlusherAR(self):
        check = self.makeupFace_capture.action
        if check == True:
            self.select_face_blusher.makeupFace = self.select_face_eyeliner.resultFace
            self.select_face_blusher.resultFace = self.select_face_blusher.makeupFace
            result = self.changePixmap(self.select_face_eyeliner.resultFace)
            self.select_face_blusher.label_face.setPixmap(QtGui.QPixmap(result).scaled(672, 504, Qt.KeepAspectRatio))
            self.select_face_blusher.action = True
        self.stk_w.setCurrentWidget(self.select_face_blusher)
    def goToLipAR(self):
        check = self.makeupFace_capture.action
        if check == True:
            self.select_face_lip.makeupFace = self.select_face_blusher.resultFace
            self.select_face_lip.resultFace = self.select_face_lip.makeupFace
            result = self.changePixmap(self.select_face_blusher.resultFace)
            self.select_face_lip.label_face.setPixmap(QtGui.QPixmap(result).scaled(672, 504, Qt.KeepAspectRatio))
            self.select_face_lip.action = True
        self.stk_w.setCurrentWidget(self.select_face_lip)

    def goToEyebrowARLater(self):
        self.stk_w.setCurrentWidget(self.select_face_eyebrow)
    def goToEyeshadowARLater(self):
        self.stk_w.setCurrentWidget(self.select_face_eyeshadow)
    def goToEyelinerARLater(self):
        self.stk_w.setCurrentWidget(self.select_face_eyeliner)
    def goToBlusherARLater(self):
        self.stk_w.setCurrentWidget(self.select_face_blusher)

    def goToLipARorTHEMA(self):
        if (self.sub_menu.btn == "select_face"):
            self.stk_w.setCurrentWidget(self.select_face_lip)
        else:
            self.stk_w.setCurrentWidget(self.select_thema)

    def goToEyebrowFrame(self):
        check = self.makeupFace_capture.action
        if (self.sub_menu.btn == "select_face"):
            if check == True:
                result = self.changePixmap(self.select_face_lip.resultFace)
                self.frame_eyebrow.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isKind = self.select_face_eyebrow.isKind
                isColor = self.select_face_eyebrow.isColor
                if isKind & isColor == True:
                    kind = self.select_face_eyebrow.kind
                    print(f"[main.py] 아이브로우 종류 : {kind}")
                    self.frame_eyebrow.isDetect = False
                    self.frame_eyebrow.face_kind = "0"
                    self.frame_eyebrow.kind = kind
                    self.frame_eyebrow.cpt = self.cpt
                    self.frame_eyebrow.start()
                else:
                    self.frame_eyebrow.label_background_Manual.setText("you didn't choice")
                    self.frame_eyebrow.resetPix()

        else:
            if check == True:
                result = self.changePixmap(self.select_thema.resultFace)
                self.frame_eyebrow.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isChoice = self.select_thema.isChoice
                isDetect = self.select_thema.isDetect
                print("[main.py] 한마디로 맞춤형 버튼 눌렀니? "+str(isDetect))
                if isChoice == True:
                    if isDetect == True:
                        print("[main.py] 맞춤형 버튼 눌렀단다.")
                        self.frame_eyebrow.isDetect = True
                        self.frame_eyebrow.face_kind = self.select_thema.kindBlusher
                    else:
                        print("[main.py] 안눌렀단다.")
                        self.frame_eyebrow.isDetect = False
                        self.frame_eyebrow.face_kind = "0"
                    kind = self.select_thema.kindBrow
                    print(f"[main.py] 아이브로우 종류 : {kind}")
                    self.frame_eyebrow.kind = kind
                    self.frame_eyebrow.cpt = self.cpt
                    self.frame_eyebrow.start()
                else:
                    self.frame_eyebrow.label_background_Manual.setText("you didn't choice")
                    self.frame_eyebrow.resetPix()
        self.stk_w.setCurrentWidget(self.frame_eyebrow)
    def goToEyeshadowFrame(self):
        check = self.makeupFace_capture.action
        if (self.sub_menu.btn == "select_face"):
            if check == True:
                result = self.changePixmap(self.select_face_lip.resultFace)
                self.frame_eyeshadow.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isKind = self.select_face_eyeshadow.isKind
                isColor = self.select_face_eyeshadow.isColor
                if isKind & isColor == True:
                    kind = self.select_face_eyeshadow.kind
                    print(f"[main.py] 아이쉐도우 종류 : {kind}")
                    self.frame_eyeshadow.kind = kind
                    self.frame_eyeshadow.cpt = self.cpt
                    self.frame_eyeshadow.start()
                else:
                    self.frame_eyeshadow.label_background_Manual.setText("you didn't choice")
                    self.frame_eyeshadow.resetPix()
        else:
            if check == True:
                result = self.changePixmap(self.select_thema.resultFace)
                self.frame_eyeshadow.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isChoice = self.select_thema.isChoice
                if isChoice == True:
                    kind = self.select_thema.kindShadow
                    print(f"[main.py] 아이쉐도우 종류 : {kind}")
                    self.frame_eyeshadow.kind = kind
                    self.frame_eyeshadow.cpt = self.cpt
                    self.frame_eyeshadow.start()
                else:
                    self.frame_eyeshadow.label_background_Manual.setText("you didn't choice")
                    self.frame_eyeshadow.resetPix()
        self.stk_w.setCurrentWidget(self.frame_eyeshadow)
    def goToEyelinerFrame(self):
        check = self.makeupFace_capture.action
        if (self.sub_menu.btn == "select_face"):
            if check == True:
                result = self.changePixmap(self.select_face_lip.resultFace)
                self.frame_eyeliner.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isKind = self.select_face_eyeliner.isKind
                isColor = self.select_face_eyeliner.isColor
                if isKind & isColor == True:
                    kind = self.select_face_eyeliner.kind
                    print(f"[main.py] 아이라이너 종류 : {kind}")
                    self.frame_eyeliner.kind = kind
                    self.frame_eyeliner.cpt = self.cpt
                    self.frame_eyeliner.start()
                else:
                    self.frame_eyeliner.label_background_Manual.setText("you didn't choice")
                    self.frame_eyeliner.resetPix()
        else:
            if check == True:
                result = self.changePixmap(self.select_thema.resultFace)
                self.frame_eyeliner.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isChoice = self.select_thema.isChoice
                if isChoice == True:
                    kind = self.select_thema.kindLiner
                    print(f"[main.py] 아이라이너 종류 : {kind}")
                    self.frame_eyeliner.kind = kind
                    self.frame_eyeliner.cpt = self.cpt
                    self.frame_eyeliner.start()
                else:
                    self.frame_eyeliner.label_background_Manual.setText("you didn't choice")
                    self.frame_eyeliner.resetPix()
        self.stk_w.setCurrentWidget(self.frame_eyeliner)
    def goToBlusherFrame(self):
        check = self.makeupFace_capture.action
        if (self.sub_menu.btn == "select_face"):
            if check == True:
                result = self.changePixmap(self.select_face_lip.resultFace)
                self.frame_blusher.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isKind = self.select_face_blusher.isKind
                isColor = self.select_face_blusher.isColor
                if isKind & isColor == True:
                    kind = self.select_face_blusher.kind
                    print(f"[main.py] 블러셔 종류 : {kind}")
                    self.frame_blusher.kind = kind
                    self.frame_blusher.cpt = self.cpt
                    self.frame_blusher.start()
                else:
                    self.frame_blusher.label_background_Manual.setText("you didn't choice")
                    self.frame_blusher.resetPix()
        else:
            if check == True:
                result = self.changePixmap(self.select_thema.resultFace)
                self.frame_blusher.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isChoice = self.select_thema.isChoice
                if isChoice == True:
                    kind = self.select_thema.kindBlusher
                    print(f"[main.py] 블러셔 종류 : {kind}")
                    self.frame_blusher.kind = kind
                    self.frame_blusher.cpt = self.cpt
                    self.frame_blusher.start()
                else:
                    self.frame_blusher.label_background_Manual.setText("you didn't choice")
                    self.frame_blusher.resetPix()
        self.stk_w.setCurrentWidget(self.frame_blusher)
    def goToLipFrame(self):
        self.frame_lip.cpt = self.cpt
        self.frame_lip.start()
        check = self.makeupFace_capture.action
        if (self.sub_menu.btn == "select_face"):
            if check == True:
                result = self.changePixmap(self.select_face_lip.resultFace)
                self.frame_lip.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isColor = self.select_face_lip.isColor
                if isColor == True:
                    self.frame_lip.label_background_Manual.setText("AR사진에 lip color로 립을 칠해주세요.")
                else:
                    self.frame_lip.label_background_Manual.setText("you didn't choice")
        else:
            if check == True:
                result = self.changePixmap(self.select_thema.resultFace)
                self.frame_lip.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(324, 243, Qt.KeepAspectRatio))
                isChoice = self.select_thema.isChoice
                if isChoice == True:
                    self.frame_lip.label_background_Manual.setText("AR사진에 lip color로 립을 칠해주세요.")
                else:
                    self.frame_blusher.label_background_Manual.setText("you didn't choice")
        self.stk_w.setCurrentWidget(self.frame_lip)

    def goToCompare(self):
        check = self.makeupFace_capture.action
        if (self.sub_menu.btn == "select_face"):
            if check == True:
                result = self.changePixmap(self.select_face_lip.resultFace)
                self.Real_AR_Face_compare.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(448, 336, Qt.KeepAspectRatio))
        else:
            if check == True:
                result = self.changePixmap(self.select_thema.resultFace)
                self.Real_AR_Face_compare.label_faceAR.setPixmap(QtGui.QPixmap(result).scaled(448, 336, Qt.KeepAspectRatio))
        self.stk_w.setCurrentWidget(self.Real_AR_Face_compare)

    def goToHome(self):
        self.resetALL()
        self.label_back_background.hide()
        self.label_background_TitleBar.hide()
        self.label_DateTime.hide()
        self.label_Temperature.hide()
        self.label_WeatherIcon.hide()
        self.pushButton_Weather.hide()
        self.label_background_MenuShortcut.hide()
        self.pushButton_MenuShortcut.hide()
        self.stk_w.setCurrentWidget(self.home)

    def changePixmap(self, result):
        result = QtGui.QImage(result, result.shape[1], result.shape[0], result.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        result2 = QtGui.QPixmap(result)
        return result2

    def closeEvent(self, event):
        print("[main.py] 헬미를 종료합니다.")
        check = os.path.isfile('capture.jpg')
        check2 = os.path.isfile('capture2.jpg')
        if check == True:
            os.remove('capture.jpg')
        if check2 == True:
            os.remove('capture2.jpg')
        self.cpt.release()

    def ShutDown(self):
        print("[main.py] 헬미를 종료합니다.")
        check = os.path.isfile('capture.jpg')
        check2 = os.path.isfile('capture2.jpg')
        if check == True:
            os.remove('capture.jpg')
        if check2 == True:
            os.remove('capture2.jpg')
        self.cpt.release()
        sys.exit()

    def resetALL(self):
        self.bareFace_capture.reset()
        self.makeupFace_capture.reset()
        self.personal_color.reset()
        self.select_thema.reset()
        self.select_face_eyebrow.reset()
        self.select_face_eyeshadow.reset()
        self.select_face_eyeliner.reset()
        self.select_face_blusher.reset()
        self.select_face_lip.reset()
        self.frame_eyebrow.reset()
        self.frame_eyeshadow.reset()
        self.frame_eyeliner.reset()
        self.frame_blusher.reset()
        self.frame_lip.reset()
        self.Real_AR_Face_compare.reset()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MAIN_StackedWidget()
    form.show()
    exit(app.exec_())
