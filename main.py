## 순서

# 0. home
# 1. face_capture (쌩얼인 상태) : 얼굴형 분석
# 2. menu -> [select by face, select by thema, personal color]

# 3-0. select by face & select by thema 클릭 시
#      -> base makeup 동영상
#      -> face_capture(base메이크업한 상태)
# 3-1. select by face ~~ frame
#  -> eyebrow - eyeshadow - eyeliner - blusher - lip
# 3-2. select by thema
#  테마 스타일 선택 ~~ frame
# 3-3. personal color
#  색상 추천  ~~ select by thema

# 4. frame (본격적인 화장 시작)
#  -> 눈썹프레임 - 아이새됴우프레임 - 아이라이너 프레임 - 블러셔 프레임 - 립(프레임은 없음)
# 5. 가상화장한 얼굴 - 실제 화장한 얼굴 비교
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from home import Home
from face_capture import Face_Capture
from menu import Menu

from personal_color import Personal_Color
from select_thema import Select_Thema
from select_face_thema_base import Select_face_thema_Base
from select_face_thema_capture import Select_face_thema_Capture

from select_face_eyebrow import Select_face_Eyebrow
from select_face_eyeshadow import Select_face_Eyeshadow
from select_face_eyeliner import Select_face_Eyeliner
from select_face_blusher import Select_face_Blusher
from select_face_lip import Select_face_Lip


class MAIN_StackedWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.stk_w = QStackedWidget(self)
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("Help Me MakUp Mirror")
        ## 나중에 jetson nano 화면을 회전해야함.
        ## 나중에 버튼위치 및 크기를 2배씩 곱해야함
        # self.resize(1122, 1587) # 원본 미러 크기
        self.resize(561, 793.5)  # 원본 미러 크기에서 나누기 2함
        widget_laytout = QHBoxLayout()


        self.home = Home()
        self.face_capture = Face_Capture()
        self.menu = Menu()
        self.personal_color = Personal_Color()
        self.select_thema = Select_Thema()
        self.select_face_thema_base = Select_face_thema_Base()
        self.select_face_thema_capture = Select_face_thema_Capture()

        self.select_face_eyebrow = Select_face_Eyebrow()
        self.select_face_eyeshadow = Select_face_Eyeshadow()
        self.select_face_eyeliner = Select_face_Eyeliner()
        self.select_face_blusher = Select_face_Blusher()
        self.select_face_lip = Select_face_Lip()



        self.stk_w.addWidget(self.home)
        self.stk_w.addWidget(self.face_capture)
        self.stk_w.addWidget(self.menu)
        self.stk_w.addWidget(self.personal_color)
        self.stk_w.addWidget(self.select_thema)
        self.stk_w.addWidget(self.select_face_thema_base)
        self.stk_w.addWidget(self.select_face_thema_capture)

        self.stk_w.addWidget(self.select_face_eyebrow)
        self.stk_w.addWidget(self.select_face_eyeshadow)
        self.stk_w.addWidget(self.select_face_eyeliner)
        self.stk_w.addWidget(self.select_face_blusher)
        self.stk_w.addWidget(self.select_face_lip)



        widget_laytout.addWidget(self.stk_w)
        self.setLayout(widget_laytout)


        ## 화면전환 NEXT
        self.home.pushButton_GoFaceCatprue.clicked.connect(self.goToFaceCapture)
        self.face_capture.pushButton_GoMenu.clicked.connect(self.goToMenu)

        self.menu.pushButton_GoPersonalColor.clicked.connect(self.goToPersonalColor)
        self.menu.pushButton_GoSelectFace.clicked.connect(self.goToBaseMakeUp_Face)
        self.menu.pushButton_GoSelectThema.clicked.connect(self.goToBaseMakeUp_Thema)

        self.personal_color.pushButton_GoThema.clicked.connect(self.goToBaseMakeUp_Thema)
        self.select_face_thema_base.pushButton_GoSelectFaceCapture.clicked.connect(self.goToSelectFaceCapture)
        self.select_face_thema_capture.pushButton_GoThemaOrEyebrowAR.clicked.connect(self.goToThemaOrEyebrowAR)

        self.select_face_eyebrow.pushButton_GoEyeshadowAR.clicked.connect(self.goToEyshadowAR)
        self.select_face_eyeshadow.pushButton_GoEyelinerAR.clicked.connect(self.goToEyelinerAR)
        self.select_face_eyeliner.pushButton_GoBlusherAR.clicked.connect(self.goToBlusherAR)
        self.select_face_blusher.pushButton_GoLipAR.clicked.connect(self.goToLipAR)


        ## 화면전환 PREVIOUS

    def goToFaceCapture(self):
        self.stk_w.setCurrentWidget(self.face_capture)

    def goToMenu(self):
        self.stk_w.setCurrentWidget(self.menu)

    def goToPersonalColor(self):
        self.stk_w.setCurrentWidget(self.personal_color)

    def goToBaseMakeUp_Face(self):
        self.menu.btn = "select_face"
        self.stk_w.setCurrentWidget(self.select_face_thema_base)

    def goToBaseMakeUp_Thema(self):
        self.menu.btn = "select_thema"
        self.stk_w.setCurrentWidget(self.select_face_thema_base)

    def goToSelectFaceCapture(self):
        self.stk_w.setCurrentWidget(self.select_face_thema_capture)

    def goToThemaOrEyebrowAR(self):
        print(self.menu.btn)
        if(self.menu.btn=="select_face"):
            self.stk_w.setCurrentWidget(self.select_face_eyebrow)
        else:
            self.stk_w.setCurrentWidget(self.select_thema)

    def goToEyshadowAR(self):
        self.stk_w.setCurrentWidget(self.select_face_eyeshadow)

    def goToEyelinerAR(self):
        self.stk_w.setCurrentWidget(self.select_face_eyeliner)

    def goToBlusherAR(self):
        self.stk_w.setCurrentWidget(self.select_face_blusher)

    def goToLipAR(self):
        self.stk_w.setCurrentWidget(self.select_face_lip)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MAIN_StackedWidget()
    form.show()
    exit(app.exec_())

