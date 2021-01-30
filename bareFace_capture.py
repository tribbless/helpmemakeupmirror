from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2

from personalColor import personal_color_start


class BareFace_Capture(QWidget):

    def __init__(self):
        super(BareFace_Capture, self).__init__()

        self.action = False # 캡쳐버튼 눌렀는지
        self.flag = False # 카메라 상태

        # 얼굴
        self.label_face = QtWidgets.QLabel(self)
        #self.label_face.setGeometry(QtCore.QRect(122, 66, 318, 424)) ## 3:4 비율!
        self.label_face.setGeometry(QtCore.QRect(162, 152, 700, 525)) # 4:3 비율!
        self.label_face.setObjectName("label_face")
        self.label_face.setStyleSheet('background-color:white;')

        # 텍스트
        self.label_manual = QtWidgets.QLabel(self)
        #self.label_manual.setGeometry(QtCore.QRect(112, 490, 338, 70))
        self.label_manual.setGeometry(QtCore.QRect(277, 719, 470, 100))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_manual.setFont(font)
        self.label_manual.setText("베이스 메이크업 전 촬영입니다.\n화면을 캡쳐하세요.")
        self.label_manual.setAlignment(Qt.AlignCenter)
        self.label_manual.setStyleSheet('color: white;')

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(145, 862, 734, 216))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 30px;")

        # 캡쳐 버튼 background image
        self.label_background_Capture = QtWidgets.QLabel(self)
        self.label_background_Capture.setGeometry(QtCore.QRect(165, 882, 368, 176))
        self.label_background_Capture.setObjectName("label_background_Capture")
        self.label_background_Capture.setStyleSheet("border-image: url(image/btn_capture.png);"
                                                    "border-radius: 20px;")

        # 캡쳐 버튼
        self.pushButton_Capture = QtWidgets.QPushButton(self)
        self.pushButton_Capture.setGeometry(QtCore.QRect(165, 882, 368, 176))
        self.pushButton_Capture.setStyleSheet('background-color: transparent; '
                                              'border-radius: 20px; border: 0px;')
        self.pushButton_Capture.setObjectName("pushButton_Capture")
        self.pushButton_Capture.clicked.connect(self.captureFace)

        # 이동 버튼 background image
        self.label_background_GoPersonalColor = QtWidgets.QLabel(self)
        self.label_background_GoPersonalColor.setGeometry(QtCore.QRect(553, 882, 306, 176))
        self.label_background_GoPersonalColor.setObjectName("label_background_GoPersonalColor")
        self.label_background_GoPersonalColor.setStyleSheet("border-image: url(image/btn_check_your_type.png);"
                                                            "border-radius: 20px;")

        # 이동 버튼 (->퍼스널 컬러)
        self.pushButton_GoPersonalColor = QtWidgets.QPushButton(self)
        self.pushButton_GoPersonalColor.setGeometry(QtCore.QRect(553, 882, 306, 176))
        self.pushButton_GoPersonalColor.setStyleSheet('background-color: transparent; '
                                                      'border-radius:20px; border: 0px;')
        self.pushButton_GoPersonalColor.setObjectName("pushButton_GoPersonalColor")

        # 이동 버튼 image
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(25, 22, 45, 45))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("border-image: url(image/btn_back.png);")

        ## 이동 버튼 (previous)
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(23, 9, 55, 72))
        self.pushButton_GoMainMenu.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                 "border-radius: 10px;")
        self.pushButton_GoMainMenu.setObjectName("pushButton_GoMainMenu")
        self.pushButton_GoMainMenu.clicked.connect(self.stop)

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")


    def stop(self):
        self.timer.stop()

    def start(self):
        self.flag = True
        print("camera start")
        self.timer = QTimer()
        self.timer = QTimer(self, interval=1000 / 24, timeout=self.nextFrameSlot) # # 타이머가 끝날때마다 nextFrameSlot실행됨.
        self.timer.start()  # 1000이 1초 : 초당 24프레임으로 영상을 전송하겠다.

    def nextFrameSlot(self):
        if self.flag == False:
            print("camera stop")
            self.stop()
        ret_val, cam = self.cpt.read()
        cam = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)  # 첨에 영상정보가 BGR이므로 RGB으로 바꿈ㅇㅇ 색상정보 위치바꾸기
        cam = cv2.flip(cam, 1)  # 0이 상하반전 / 1이 좌우반전
        self.bareFace = cam
        img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888)  # 가로 세로 ㅇㅇ
        pix = QPixmap.fromImage(img)
        self.label_face.setPixmap(QtGui.QPixmap(pix.scaled(700, 525, Qt.KeepAspectRatio)))

    def captureFace(self):
        print("얼굴 캡쳐하기")
        self.flag = False
        self.action = True
        self.bareFace = cv2.cvtColor(self.bareFace, cv2.COLOR_BGR2RGB)
        cv2.imwrite('capture.jpg', self.bareFace)

    def personal_analysis(self):
        self.label_manual.setText("퍼스널 컬러 진단 중 입니다.")

    def personalFace(self):
        print("stop")
        self.flag = False
        self.result = True

        #check =os.path.isfile('capture.jpg')
        if self.action == True:
            print("퍼스널 컬러 진단 시작")
            tone = personal_color_start.main('capture.jpg')
            print(tone)
            if tone == False:
                print("얼굴 인식 실패하셨습니다.")
                self.label_manual.setText("얼굴 인식에 실패했습니다.\n화면을 다시 캡쳐해주세요.")
                self.action = False
                self.result = False
                self.start()
                return
            self.tone = tone
            self.bareFace = cv2.cvtColor(self.bareFace, cv2.COLOR_RGB2BGR)
        else:
            print("캡쳐하지 않았습니다.")

    def reset(self):
        self.label_face.clear()
        self.action = False
        self.flag = False
        self.label_manual.setText("베이스 메이크업 전 촬영입니다.\n화면을 캡쳐하세요.")
