import cv2
import dlib
import imutils
from imutils import face_utils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from frame import make_frame as fr


class Frame_Eyebrow(QWidget):

    def __init__(self):
        super(Frame_Eyebrow, self).__init__()

        self.real_shape = 0
        self.shape_flag = False
        self.isDetect = False
        self.face_kind = "0"

        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("face_detector/shape_predictor_68_face_landmarks.dat")
        self.flag = False  # 카메라 상태

        # 프레임 씌어진 얼굴 모습
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(379, 246, 616, 462))
        self.label_face.setObjectName("label_face")
        self.label_face.setStyleSheet("background-color: transparent;" 
                                      "border-style: dashed;"
                                      "border-width: 3px;"
                                      "border-color: rgb(183,166,231);")

        # AR 사진
        self.label_faceAR = QtWidgets.QLabel(self)
        self.label_faceAR.setGeometry(QtCore.QRect(26, 155, 324, 243))
        self.label_faceAR.setObjectName("label_faceAR")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_faceAR.setFont(font)
        self.label_faceAR.setAlignment(Qt.AlignCenter)
        self.label_faceAR.setText("you didn't capture")
        self.label_faceAR.setStyleSheet("background-color: white;")

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(245, 805, 534, 45))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("Eye Brow")
        self.label_subject.setStyleSheet('color: white;')

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(48, 890, 928, 250))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 30px;")
        self.label_background_white.lower()

        # eyebrow manual background image
        self.label_background_Manual = QtWidgets.QLabel(self)
        self.label_background_Manual.setGeometry(QtCore.QRect(60, 900, 904, 230))
        self.label_background_Manual.setObjectName("label_background_Manual")
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_background_Manual.setFont(font)
        self.label_background_Manual.setAlignment(Qt.AlignCenter)
        self.label_background_Manual.setText("you didn't capture")
        self.label_background_Manual.setStyleSheet("border-image: url(image/background.png); "
                                                   "border-radius: 20px; color: white;")


        # 이동 버튼 (prev/next)
        self.pushButton_GoARorThema = QtWidgets.QPushButton(self)
        self.pushButton_GoARorThema.setGeometry(QtCore.QRect(60, 805, 168, 50))
        self.pushButton_GoARorThema.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoARorThema.setFont(font)
        self.pushButton_GoARorThema.setText("< Prev")
        self.pushButton_GoARorThema.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')
        self.pushButton_GoARorThema.clicked.connect(self.shifting)

        self.pushButton_GoEyesahdowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyesahdowFrame.setGeometry(QtCore.QRect(796, 805, 168, 50))
        self.pushButton_GoEyesahdowFrame.setObjectName("pushButton_GoEyesahdowFrame")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoEyesahdowFrame.setFont(font)
        self.pushButton_GoEyesahdowFrame.setText("Shadow >")
        self.pushButton_GoEyesahdowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')
        self.pushButton_GoEyesahdowFrame.clicked.connect(self.shifting)

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

    def shifting(self):
        self.flag = False

    def stop(self):
        self.timer.stop()

    def start(self):
        self.flag = True
        print("camera start")
        if self.kind =="arch":
            self.kindName = "Eyebrow_Arch"
            self.label_background_Manual.setText("아치형으로 눈썹을 그려주세요.")
        elif self.kind =="straight":
            self.kindName = "Eyebrow_Straight"
            self.label_background_Manual.setText("일자로 눈썹을 그려주세요.")
        print(self.face_kind)
        if self.face_kind!= "0":
            print("얼굴형에 맞춘 눈썹입니다. : ", self.face_kind) ## 무슨 멘트써야하지..흐음.....
        print(self.kindName)
        print(self.isDetect)
        self.timer = QTimer()
        self.timer = QTimer(self, interval=1000 / 24, timeout=self.nextFrameSlot)  # # 타이머가 끝날때마다 nextFrameSlot실행됨.
        self.timer.start()  # 1000이 1초 : 초당 24프레임으로 영상을 전송하겠다.

    def nextFrameSlot(self):
        if self.flag == False:
            print("camera stop")
            self.stop()
        ret_val, image = self.cpt.read()
        #image = imutils.resize(image, width=708)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale frame
        rects = self.detector(gray, 0)
        output = image

        if rects:  # 얼굴인식 성공시 TRUE
            shape = self.predictor(gray, rects[0])
            shape = face_utils.shape_to_np(shape)
            self.real_shape = shape
            self.shape_flag = True
        if self.shape_flag:
            if self.isDetect == True:
                output = fr.customize_eyebrow_frame(image, self.real_shape, self.face_kind)
            else:
                output = fr.image_frame_insert(image, self.real_shape, self.kindName)

        #output = imutils.resize(output, width=354)
        cam = output
        cam = cv2.flip(cam, 1)  # 0이 상하반전 / 1이 좌우반전
        cam = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)  # 첨에 영상정보가 BGR이므로 RGB으로 바꿈ㅇㅇ 색상정보 위치바꾸기
        img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888)  # 가로 세로 ㅇㅇ
        pix = QPixmap.fromImage(img)
        self.label_face.setPixmap(QtGui.QPixmap(pix.scaled(616, 462, Qt.KeepAspectRatio)))

    def resetPix(self):
        self.label_face.clear()

    def reset(self):
        print("frame brow resetALL")
        self.isDetect = False
        self.shape_flag = False
        self.face_kind = "0"
        self.resetPix()
        self.label_faceAR.clear()
        self.label_faceAR.setText("you didn't capture")
        self.label_background_Manual.setText("you didn't capture")

