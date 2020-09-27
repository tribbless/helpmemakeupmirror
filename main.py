##  순서

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

3. 퍼스널 컬러 [personal_color.py] ~ 쌩얼 캡쳐

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
import sys
import requests
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
## 헬미로고는 베이스메이크업 로고 기준으로 함.!!!!!


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
        today_temp, url_icon = weatherInfo.weather()
        # 온도
        self.label_Temperature.setText(today_temp+"°")
        # 날씨 아이콘
        contents = requests.get(url_icon).content
        file = QtCore.QTemporaryFile(self.label_WeatherIcon)
        if file.open():
            file.write(contents)
            file.flush()
            self.label_WeatherIcon.setStyleSheet("""
                                          border-image: url(%s);""" % file.fileName())


    def setupUi(self):
        self.setWindowTitle("Help Me MakUp Mirror")
        #self.resize(562, 794)
        #self.setStyleSheet("background:transparent")
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setStyleSheet("background-color:transparent;")
        ## 나중에 jetson nano 화면을 회전해야함.
        ## 나중에 버튼위치 및 크기를 2배씩 곱해야함
        self.resize(1124, 1588) # 원본 미러 크기


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

        self.select_thema.pushButton_GoSubMenu.clicked.connect(self.goToSubMenu)
        self.select_face_eyebrow.pushButton_GoSubMenu.clicked.connect(self.goToSubMenu)
        self.select_face_eyeshadow.pushButton_GoEyebrowAR.clicked.connect(self.goToEyebrowAR)
        self.select_face_eyeliner.pushButton_GoEyeshadowAR.clicked.connect(self.goToEyeshadowAR)
        self.select_face_blusher.pushButton_GoEyelinerAR.clicked.connect(self.goToEyelinerAR)
        self.select_face_lip.pushButton_GoBlusherAR.clicked.connect(self.goToBlusherAR)

        self.frame_eyebrow.pushButton_GoARorThema.clicked.connect(self.goToLipARorTHEMA)
        self.frame_eyeshadow.pushButton_GoEyebrowFrame.clicked.connect(self.goToEyebrowFrame)
        self.frame_eyeliner.pushButton_GoEyeshadowFrame.clicked.connect(self.goToEyeshadowFrame)
        self.frame_blusher.pushButton_GoEyelinerFrame.clicked.connect(self.goToEyelinerFrame)
        self.frame_lip.pushButton_GoBlusherFrame.clicked.connect(self.goToBlusherFrame)

        self.Real_AR_Face_compare.pushButton_GoHome.clicked.connect(self.goToHome)
        self.Real_AR_Face_compare.pushButton_GoLipFrame.clicked.connect(self.goToLipFrame)

        '''고정값'''
        ## 상단 타이틀바 background
        self.label_background_TitleBar = QtWidgets.QLabel(self)
        self.label_background_TitleBar.setGeometry(QtCore.QRect(0, 0, 562, 50))
        self.label_background_TitleBar.setObjectName("label_background_TitleBar")
        self.label_background_TitleBar.setStyleSheet("border-image: url(image/background.png);")
        self.label_background_TitleBar.lower()
        self.label_background_TitleBar.hide()
        #self.label_background_TitleBar.setWindowOpacity(1.0)


        ## 시간/날짜
        self.label_DateTime = QtWidgets.QLabel(self)
        self.label_DateTime.setGeometry(QtCore.QRect(285, 0, 110, 50))
        self.label_DateTime.setObjectName("label_DateTime")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_DateTime.setFont(font)
        self.label_DateTime.setText("")
        self.label_DateTime.setAlignment(Qt.AlignCenter)
        self.label_DateTime.hide()

        ## 온도
        self.label_Temperature = QtWidgets.QLabel(self)
        self.label_Temperature.setGeometry(QtCore.QRect(408, 5, 40, 40))
        self.label_Temperature.setObjectName("label_Temperature")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_Temperature.setFont(font)
        self.label_Temperature.setText("")
        self.label_Temperature.setAlignment(Qt.AlignCenter)
        self.label_Temperature.hide()

        ## 날씨 아이콘
        self.label_WeatherIcon = QtWidgets.QLabel(self)
        self.label_WeatherIcon.setGeometry(QtCore.QRect(448, 5, 40, 40))
        self.label_WeatherIcon.setObjectName("label_WeatherIcon")
        self.label_WeatherIcon.hide()

        ## 날씨 버튼
        self.pushButton_Weather = QtWidgets.QPushButton(self)
        self.pushButton_Weather.setGeometry(QtCore.QRect(408, 5, 80, 40))
        self.pushButton_Weather.setObjectName("pushButton_Weather")
        self.pushButton_Weather.setStyleSheet("border-style: dashed; border-width: 1px; border-color: red;")
        self.pushButton_Weather.clicked.connect(self.goToWeather_Window)
        self.pushButton_Weather.hide()



        ## 메뉴 바로가기 버튼
        self.pushButton_MenuShortcut = QtWidgets.QPushButton(self)
        self.pushButton_MenuShortcut.setGeometry(QtCore.QRect(501, 5, 46, 40))
        self.pushButton_MenuShortcut.setObjectName("pushButton_MenuShortcut")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_MenuShortcut.setFont(font)
        self.pushButton_MenuShortcut.setText("메뉴")
        self.pushButton_MenuShortcut.setStyleSheet("background-color: blue;")
        self.pushButton_MenuShortcut.clicked.connect(self.goToMenuShortcut_Window)
        self.pushButton_MenuShortcut.hide()

    ## 서브 윈도우 화면 나타나기
    def goToWeather_Window(self):
        print("날씨 윈도우화면")
        weather = SubWindow_Weather()
        r = weather.showModal()
        if r:
            print("--이 메시지는 안나옴--")
        else:
            print("close")
    def goToMenuShortcut_Window(self):
        print("메뉴 바로가기 윈도우화면")
        menuShortcut = SubWindow_MenuShortcut()
        r = menuShortcut.showModal()
        if r:
            print("메뉴 바로가기 클릭성공")
            if(menuShortcut.btn==1):
                self.goToHome()
            elif(menuShortcut.btn==2):
                self.goToMainMenu()
            elif (menuShortcut.btn == 3):
                self.goToBaseMakeupVideo()
            elif (menuShortcut.btn == 4):
                self.goToBareFaceCapture()
            elif (menuShortcut.btn == 5):
                self.goToMakeupFaceCapture()
            elif (menuShortcut.btn == 6):
                self.goToSubMenu()
            else:
                sys.exit()

        else:
            print("close")

    ## 화면전환 NEXT & PREVIOUS
    def goToMainMenu(self):
        self.label_background_TitleBar.show()
        self.label_DateTime.show()
        self.label_Temperature.show()
        self.label_WeatherIcon.show()
        self.pushButton_Weather.show()
        self.pushButton_MenuShortcut.show()
        self.stk_w.setCurrentWidget(self.main_menu)
    def goToBareFaceCapture(self):
        self.stk_w.setCurrentWidget(self.bareFace_capture)
    def goToBaseMakeupVideo(self):
        self.main_menu.btn = "video"
        self.stk_w.setCurrentWidget(self.base_makeup_video)
    def goToMakeupFaceCapture(self):
        self.main_menu.btn = "MakeupFaceCapture"
        self.stk_w.setCurrentWidget(self.makeupFace_capture)
    def goToMakeupFaceCapture_Later(self):
        self.stk_w.setCurrentWidget(self.makeupFace_capture)
    def goToPersonalColor(self):
        self.stk_w.setCurrentWidget(self.personal_color)
    def goToMainMENUorVideo(self):
        print(self.main_menu.btn)
        if (self.main_menu.btn == "video"):
            self.stk_w.setCurrentWidget(self.base_makeup_video)
        else:
            self.stk_w.setCurrentWidget(self.main_menu)
    def goToSubMenu(self):
        self.stk_w.setCurrentWidget(self.sub_menu)
    def goToThema(self):
        self.sub_menu.btn = "select_thema" # Frame에서 back버튼 시 활용
        self.stk_w.setCurrentWidget(self.select_thema)
    def goToEyebrowAR(self):
        self.sub_menu.btn = "select_face" # Frame에서 back버튼 시 활용
        self.stk_w.setCurrentWidget(self.select_face_eyebrow)
    def goToEyeshadowAR(self):
        self.stk_w.setCurrentWidget(self.select_face_eyeshadow)
    def goToEyelinerAR(self):
        self.stk_w.setCurrentWidget(self.select_face_eyeliner)
    def goToBlusherAR(self):
        self.stk_w.setCurrentWidget(self.select_face_blusher)
    def goToLipAR(self):
        self.stk_w.setCurrentWidget(self.select_face_lip)

    def goToLipARorTHEMA(self):
        if (self.sub_menu.btn == "select_face"):
            self.stk_w.setCurrentWidget(self.select_face_lip)
        else:
            self.stk_w.setCurrentWidget(self.select_thema)

    def goToEyebrowFrame(self):
        self.stk_w.setCurrentWidget(self.frame_eyebrow)
    def goToEyeshadowFrame(self):
        self.stk_w.setCurrentWidget(self.frame_eyeshadow)
    def goToEyelinerFrame(self):
        self.stk_w.setCurrentWidget(self.frame_eyeliner)
    def goToBlusherFrame(self):
        self.stk_w.setCurrentWidget(self.frame_blusher)
    def goToLipFrame(self):
        self.stk_w.setCurrentWidget(self.frame_lip)

    def goToCompare(self):
        self.stk_w.setCurrentWidget(self.Real_AR_Face_compare)

    def goToHome(self):
        self.label_background_TitleBar.hide()
        self.label_DateTime.hide()
        self.label_Temperature.hide()
        self.label_WeatherIcon.hide()
        self.pushButton_Weather.hide()
        self.pushButton_MenuShortcut.hide()
        self.stk_w.setCurrentWidget(self.home)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MAIN_StackedWidget()
    form.show()
    exit(app.exec_())

