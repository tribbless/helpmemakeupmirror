from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import dlib
import imutils
from imutils import face_utils
from frame import make_frame as fr


class Frame_Blusher(QWidget):

    def __init__(self):
        super(Frame_Blusher, self).__init__()

        self.real_shape = 0
        self.shape_flag = False

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
        self.label_subject.setText("Blusher")
        self.label_subject.setStyleSheet('color: white;')

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(48, 890, 928, 250))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 30px;")
        self.label_background_white.lower()

        # blusher manual background image
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
        self.pushButton_GoEyelinerFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerFrame.setGeometry(QtCore.QRect(60, 805, 168, 50))
        self.pushButton_GoEyelinerFrame.setObjectName("pushButton_GoEyelinerFrame")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoEyelinerFrame.setFont(font)
        self.pushButton_GoEyelinerFrame.setText("< Eyeliner")
        self.pushButton_GoEyelinerFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')
        self.pushButton_GoEyelinerFrame.clicked.connect(self.shifting)

        self.pushButton_GoLipFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoLipFrame.setGeometry(QtCore.QRect(796, 805, 168, 50))
        self.pushButton_GoLipFrame.setObjectName("pushButton_GoLipFrame")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoLipFrame.setFont(font)
        self.pushButton_GoLipFrame.setText("Lip >")
        self.pushButton_GoLipFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')
        self.pushButton_GoLipFrame.clicked.connect(self.shifting)

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
        print("[frame_blusher.py] camera start")
        if self.kind == "round":
            self.kindName = "Blusher_Round"
            self.label_background_Manual.setText("프레임 영역에 맞춰 볼 중앙 바깥부터 관자놀이까지\n사선 모양으로 블러셔를 발라주세요.")
        elif self.kind == "oblong":
            self.kindName = "Blusher_Oblong"
            self.label_background_Manual.setText("프레임 영역에 맞춰 블러셔를 가로로 발라주세요.")
        elif self.kind == "square":
            self.kindName = "Blusher_Square"
            self.label_background_Manual.setText("프레임 영역에 맞춰 볼 앞쪽부터 귀 쪽까지\n사선 반대 방향으로 블러셔를 넓게 펴서 발라주세요.")
        print(f"[frame_blusher.py] 블러셔 종류 : {self.kindName}")
        self.timer = QTimer()
        self.timer = QTimer(self, interval=1000 / 24, timeout=self.nextFrameSlot)  # # 타이머가 끝날때마다 nextFrameSlot실행됨.
        self.timer.start()  # 1000이 1초 : 초당 24프레임으로 영상을 전송하겠다.

    def nextFrameSlot(self):
        if self.flag == False:
            print("[frame_blusher.py] camera stop")
            self.stop()
        ret_val, image = self.cpt.read()
        # image = imutils.resize(image, width=708)

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
            output = fr.image_frame_insert(image, self.real_shape, self.kindName)

        # output = imutils.resize(output, width=354)
        cam = output

        cam = cv2.flip(cam, 1)  # 0이 상하반전 / 1이 좌우반전
        cam = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)  # 첨에 영상정보가 BGR이므로 RGB으로 바꿈ㅇㅇ 색상정보 위치바꾸기
        img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888)  # 가로 세로 ㅇㅇ
        pix = QPixmap.fromImage(img)
        self.label_face.setPixmap(QtGui.QPixmap(pix.scaled(616, 462, Qt.KeepAspectRatio)))

    def resetPix(self):
        self.label_face.clear()

    def reset(self):
        print("[frame_blusher.py] frame blusher resetALL")
        self.shape_flag = False
        self.resetPix()
        self.label_faceAR.clear()
        self.label_faceAR.setText("you didn't capture")
        self.label_background_Manual.setText("you didn't capture")

