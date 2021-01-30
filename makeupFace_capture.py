from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from frame import frame as fr
import cv2

class MakeupFace_Capture(QWidget):

    def __init__(self):
        super(MakeupFace_Capture, self).__init__()

        self.action = False  # 캡쳐버튼 눌렀는지
        self.flag = False  # 카메라 상태

        # 얼굴
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(162, 152, 700, 525))
        self.label_face.setObjectName("label_face")
        self.label_face.setStyleSheet('background-color:white;')

        # 텍스트
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(277, 719, 470, 100))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_manual.setFont(font)
        self.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")
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
        self.pushButton_Capture.setStyleSheet('background-color:transparent; '
                                              'border-radius: 20px; border: 0px;')
        self.pushButton_Capture.setObjectName("pushButton_Capture")
        self.pushButton_Capture.clicked.connect(self.captureFace)


        # 이동 버튼 background image
        self.label_background_GoSubMenu = QtWidgets.QLabel(self)
        self.label_background_GoSubMenu.setGeometry(QtCore.QRect(553, 882, 306, 176))
        self.label_background_GoSubMenu.setObjectName("label_background_GoSubMenu")
        self.label_background_GoSubMenu.setStyleSheet("border-image: url(image/btn_save2.png);"
                                                      "border-radius: 20px;")

        # 이동 버튼 (->서브메뉴)
        self.pushButton_GoSubMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoSubMenu.setGeometry(QtCore.QRect(553, 882, 306, 176))
        self.pushButton_GoSubMenu.setStyleSheet('background-color:transparent; '
                                                'border-radius: 20px; border: 0px;')
        self.pushButton_GoSubMenu.setObjectName("pushButton_GoSubMenu")
        #self.pushButton_GoSubMenu.clicked.connect(self.Save_captureFace)


        # 이동 버튼 image
        self.label_background_prev = QtWidgets.QLabel(self)
        self.label_background_prev.setGeometry(QtCore.QRect(25, 22, 45, 45))
        self.label_background_prev.setObjectName("label_background_prev")
        self.label_background_prev.setStyleSheet("border-image: url(image/btn_back.png);")

        ## 이동 버튼 (previous)
        self.pushButton_GoMainMENUorVideo = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMENUorVideo.setGeometry(QtCore.QRect(23, 9, 55, 72))
        self.pushButton_GoMainMENUorVideo.setStyleSheet("background-color: rgba(255, 255, 255, 0.24);"
                                                        "border-radius: 10px;")
        self.pushButton_GoMainMENUorVideo.setObjectName("pushButton_GoMainMENUorVideo")
        self.pushButton_GoMainMENUorVideo.clicked.connect(self.stop)

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
        self.timer = QTimer(self, interval=1000 / 24, timeout=self.nextFrameSlot)  # # 타이머가 끝날때마다 nextFrameSlot실행됨.
        self.timer.start()  # 1000이 1초 : 초당 24프레임으로 영상을 전송하겠다.

    def nextFrameSlot(self):
        if self.flag == False:
            print("makeupFace Capture camera stop")
            self.stop()
        ret_val, cam = self.cpt.read()
        cam = cv2.flip(cam, 1)  # 0이 상하반전 / 1이 좌우반전
        self.makeupFace = cam
        cam = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)  # 첨에 영상정보가 BGR이므로 RGB으로 바꿈ㅇㅇ 색상정보 위치바꾸기
        img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888)  # 가로 세로 ㅇㅇ
        pix = QPixmap.fromImage(img)
        self.label_face.setPixmap(QtGui.QPixmap(pix.scaled(700, 525, Qt.KeepAspectRatio)))

    def captureFace(self):
        print("얼굴 캡쳐하기")
        self.flag = False
        self.action = True
        cv2.imwrite('capture2.jpg', self.makeupFace)

    def landmark_make(self):
        self.label_manual.setText("잠시만 기다려주세요.")

    def Save_captureFace(self):
        self.result = True
        self.flag = False
        if self.action == True:
            face = self.makeupFace.copy()
            print("--txt파일 생성 및 landmark(shape) make--")
            print("shape start")
            self.shape, self.result = fr.image_to_shape(face) # landmark
            print(self.result)
            if self.result == False:
                print("얼굴인식 실패")
                self.label_manual.setText("얼굴 인식에 실패했습니다.\n화면을 다시 캡쳐해주세요.")
                self.action = False
                self.start()
                return
            print("shape end")
            self.landmark = self.shape
            print("eyeshadow start")
            result = fr.EyeBrow("Arch").frame(face, self.shape, True, flag=1) # eyeshadow
            fr.shadowCheck()
            print("eyeshadow end")
            print("lip start")
            fr.make_lips_txt(self.shape) # lip
            print("lip end")
            print("blusher start")
            result = fr.Blusher("Round").frame(face, self.shape, flag=1) # blusher
            result = fr.Blusher("Oblong").frame(face, self.shape, flag=1)
            result = fr.Blusher("Square").frame(face, self.shape, flag=1)
            print("--blusher end--")

        else:
            print("캡쳐하지 않았습니다.")

    def reset(self):
        self.label_face.clear()
        self.action = False
        self.flag = False
        self.label_manual.setText("베이스 메이크업 후 촬영입니다.\n화면을 캡쳐하세요.")