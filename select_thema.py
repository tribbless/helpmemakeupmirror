from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from virtual_makeup import eyebrowVM, eyeshadowVM, eyelinerVM, blusherVM, lipVM
from face_shape import face_shape_detect
import time
from face_shape import client_test

class Select_Thema(QWidget):

    def __init__(self):
        super(Select_Thema, self).__init__()
        self.action = False
        self.isChoice = False
        self.isDetect = False # 얼굴진단여부
        self.tone = "False"

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(176, 143, 672, 504))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("you didn't capture")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 텍스트
        self.label_text = QtWidgets.QLabel(self)
        self.label_text.setGeometry(QtCore.QRect(262, 682, 500, 50))
        self.label_text.setObjectName("label_text")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_text.setFont(font)
        self.label_text.setText("")
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_text.setStyleSheet("color: white;")

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(50, 760, 924, 370))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 30px;")
        self.label_background_white.lower()

        # TEHMA option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(60, 770, 904, 350))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/btn_thema.png);"
                                                   "border-radius: 20px;")

        # 이동 버튼 (prev/next)
        self.pushButton_GoSubMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoSubMenu.setGeometry(QtCore.QRect(60, 682, 168, 50))
        self.pushButton_GoSubMenu.setObjectName("pushButton_GoSubMenu")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoSubMenu.setFont(font)
        self.pushButton_GoSubMenu.setText("< Menu")
        self.pushButton_GoSubMenu.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        self.pushButton_GoEyebrowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowFrame.setGeometry(QtCore.QRect(796, 682, 168, 50))
        self.pushButton_GoEyebrowFrame.setObjectName("pushButton_GoEyebrowFrame")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_GoEyebrowFrame.setFont(font)
        self.pushButton_GoEyebrowFrame.setText("Frame >")
        self.pushButton_GoEyebrowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        ## 테마 선택 버튼

        self.pushButton_UserThema = QtWidgets.QPushButton(self)
        self.pushButton_UserThema.setGeometry(QtCore.QRect(90, 840, 275, 260))
        self.pushButton_UserThema.setStyleSheet('background-color: transparent; border: 0px;')
        self.pushButton_UserThema.setObjectName("pushButton_UserThema")
        self.pushButton_UserThema.clicked.connect(self.Apply_UserThema)
        # self.pushButton_UserThema.setStyleSheet("border-style: dashed;"
        #                                        "border-width: 3px;"
        #                                        "border-color: rgb(183,166,231);")

        self.pushButton_SpringThema = QtWidgets.QPushButton(self)
        self.pushButton_SpringThema.setGeometry(QtCore.QRect(375, 840, 135, 125))
        self.pushButton_SpringThema.setStyleSheet('background-color: transparent; border: 0px;')

        self.pushButton_SpringThema.setObjectName("pushButton_SpringThema")
        self.pushButton_SpringThema.clicked.connect(lambda: self.Apply_SpringThema())

        self.pushButton_SummerThema = QtWidgets.QPushButton(self)
        self.pushButton_SummerThema.setGeometry(QtCore.QRect(520, 840, 135, 125))
        self.pushButton_SummerThema.setStyleSheet('background-color: transparent; border: 0px;')
        self.pushButton_SummerThema.setObjectName("pushButton_SummerThema")
        self.pushButton_SummerThema.clicked.connect(lambda: self.Apply_SummerThema())

        self.pushButton_FallThema = QtWidgets.QPushButton(self)
        self.pushButton_FallThema.setGeometry(QtCore.QRect(375, 975, 135, 125))
        self.pushButton_FallThema.setStyleSheet('background-color: transparent; border: 0px;')
        self.pushButton_FallThema.setObjectName("pushButton_FallThema")
        self.pushButton_FallThema.clicked.connect(lambda: self.Apply_FallThema())

        self.pushButton_WinterThema = QtWidgets.QPushButton(self)
        self.pushButton_WinterThema.setGeometry(QtCore.QRect(520, 975, 135, 125))
        self.pushButton_WinterThema.setStyleSheet('background-color: transparent; border: 0px;')
        self.pushButton_WinterThema.setObjectName("pushButton_WinterThema")
        self.pushButton_WinterThema.clicked.connect(lambda: self.Apply_WinterThema())

        self.pushButton_PartyThema = QtWidgets.QPushButton(self)
        self.pushButton_PartyThema.setGeometry(QtCore.QRect(663, 840, 275, 80))
        self.pushButton_PartyThema.setStyleSheet('background-color: transparent; border: 0px;')
        self.pushButton_PartyThema.setObjectName("pushButton_PartyThema")
        self.pushButton_PartyThema.clicked.connect(lambda: self.Apply_PartyThema())

        self.pushButton_DateThema = QtWidgets.QPushButton(self)
        self.pushButton_DateThema.setGeometry(QtCore.QRect(663, 932, 275, 80))
        self.pushButton_DateThema.setStyleSheet('background-color: transparent; border: 0px;')
        self.pushButton_DateThema.setObjectName("pushButton_DateThema")
        self.pushButton_DateThema.clicked.connect(lambda: self.Apply_DateThema())

        self.pushButton_OfficeThema = QtWidgets.QPushButton(self)
        self.pushButton_OfficeThema.setGeometry(QtCore.QRect(663, 1022, 275, 80))
        self.pushButton_OfficeThema.setStyleSheet('background-color: transparent; border: 0px;')
        self.pushButton_OfficeThema.setObjectName("pushButton_OfficeThema")
        self.pushButton_OfficeThema.clicked.connect(lambda: self.Apply_OfficeThema())

    def showTime(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.face_shape_detect)
        self.timer.setSingleShot(True)
        self.timer.start(500)  # 0.5초후 실행됨.

    def face_shape_detect(self):
        isDetect = True
        print("얼굴형 진단 시작")
        start_time = time.time()
        #face_shape = face_shape_detect.main('capture2.jpg')
        face_shape = client_test.client_main('capture2.jpg')
        end_time = time.time()
        print("Working Time: {} sec".format(end_time-start_time))
        print("얼굴형은? " + face_shape)
        face_shape2 = face_shape.capitalize()
        #face_shape = "oblong"
        #face_shape2 = "Oblong"
        print(self.tone)
        ## 얼굴형에 따른 눈썹 모양
        if face_shape == "oblong":
            brow_shape = "straight"
        else:
            brow_shape = "arch"
        print(brow_shape)
        '''
        봄웜톤(spring) : SPRING WARM
        가을웜톤(fall) : FALL WARM
        여름쿨톤(summer) : SUMMER COOL
        겨울쿨톤(winter) : WINTER COOL
        '''
        if self.tone != "False":
            print()
            if self.tone == "SPRING WARM":
                self.Apply_SpringThema(face_shape, brow_shape, isDetect)
            elif self.tone == "SUMMER COOL":
                self.Apply_SummerThema(face_shape, brow_shape, isDetect)
            elif self.tone == "FALL WARM":
                self.Apply_FallThema(face_shape, brow_shape, isDetect)
            elif self.tone == "WINTER COOL":
                self.Apply_WinterThema(face_shape, brow_shape, isDetect)
        else:
            self.Apply_OfficeThema(face_shape, brow_shape, isDetect)
        self.label_text.setText("얼굴형은 " + face_shape2 + "입니다.")

    def Apply_UserThema(self):
        print("user click")
        if self.action == True:
            self.label_text.setText("얼굴형 분석 중 입니다.")
            self.showTime()
        else:
            print("you didn't capture.")

    def Apply_SpringThema(self, blusher_shape="round", brow_shape="arch", isDetect=False):
        self.label_text.setText("SPRING")
        print("spring click")
        #print(blusher_shape)
        if self.action == True:
            self.isChoice = True

            print(blusher_shape)
            brow = self.Start_eyebrowVM(brow_shape, "brown", 0.3)
            shadow = self.Start_eyeshadowVM("small_shadow", 104, 61, 27, 0.3, brow)
            liner = self.Start_eyelinerVM("Middle", (49, 62, 106), 0.6, shadow)
            blusher = self.Start_blusherVM(blusher_shape, "105, 89, 240", 0.2, liner)
            lip = self.Start_lipVM(227, 67, 62, 0.3, blusher)
            self.resultFace = lip
            self.changePixmap(self.resultFace)
            self.sendKind("arch", "small_shadow", "Middle", blusher_shape, isDetect)
        else:
            print("you didn't capture.")

    def Apply_SummerThema(self, blusher_shape="round", brow_shape="straight", isDetect=False):
        self.label_text.setText("SUMMER")
        print("summer click")
        if self.action == True:
            self.isChoice = True

            brow = self.Start_eyebrowVM(brow_shape, "black", 0.3)
            shadow = self.Start_eyeshadowVM("small_shadow", 242, 168, 198, 0.3, brow)
            liner = self.Start_eyelinerVM("Middle", (0, 0, 0), 0.6, shadow)
            blusher = self.Start_blusherVM(blusher_shape, "50, 19, 152", 0.2, liner)
            lip = self.Start_lipVM(237, 70, 150, 0.3, blusher)
            self.resultFace = lip
            self.changePixmap(self.resultFace)
            self.sendKind("straight", "small_shadow", "Middle", blusher_shape, isDetect)
        else:
            print("you didn't capture.")

    def Apply_FallThema(self, blusher_shape="round", brow_shape="arch", isDetect=False):
        self.label_text.setText("FALL")
        print("fall click")
        if self.action == True:
            self.isChoice = True

            brow = self.Start_eyebrowVM(brow_shape, "brown", 0.3)
            shadow = self.Start_eyeshadowVM("small_shadow", 246, 166, 139, 0.3, brow)
            liner = self.Start_eyelinerVM("Middle", (49, 62, 106), 0.6, shadow)
            blusher = self.Start_blusherVM(blusher_shape, "61, 57, 186", 0.2, liner)
            lip = self.Start_lipVM(186, 57, 61, 0.3, blusher)
            self.resultFace = lip
            self.changePixmap(self.resultFace)
            self.sendKind("arch", "small_shadow", "Middle", blusher_shape, isDetect)
        else:
            print("you didn't capture.")

    def Apply_WinterThema(self, blusher_shape="round", brow_shape="straight", isDetect=False):
        self.label_text.setText("WINTER")
        print("winter click")
        if self.action == True:
            self.isChoice = True

            brow = self.Start_eyebrowVM(brow_shape, "black", 0.3)
            shadow = self.Start_eyeshadowVM("small_shadow", 82, 28, 44, 0.3, brow)
            liner = self.Start_eyelinerVM("Middle", (0, 0, 0), 0.6, shadow)
            blusher = self.Start_blusherVM(blusher_shape, "129, 36, 198", 0.2, liner)
            lip = self.Start_lipVM(198, 36, 129, 0.3, blusher)
            self.resultFace = lip
            self.changePixmap(self.resultFace)
            self.sendKind("straight", "small_shadow", "Middle", blusher_shape, isDetect)
        else:
            print("you didn't capture.")

    def Apply_PartyThema(self, isDetect=False):
        self.label_text.setText("PARTY")
        print("party click")
        if self.action == True:
            self.isChoice = True

            brow = self.Start_eyebrowVM("straight", "black", 0.3)
            shadow = self.Start_eyeshadowVM("small_shadow", 203, 154, 122, 0.3, brow)
            liner = self.Start_eyelinerVM("Up", (0, 0, 0), 0.6, shadow)
            blusher = self.Start_blusherVM("round", "120, 120, 240", 0.2, liner)
            lip = self.Start_lipVM(210, 6, 6, 0.4, blusher)
            self.resultFace = lip
            self.changePixmap(self.resultFace)
            self.sendKind("straight", "small_shadow", "Up", "round", isDetect)
        else:
            print("you didn't capture.")

    def Apply_DateThema(self, isDetect=False):
        self.label_text.setText("DATE")
        print("date click")
        if self.action == True:
            self.isChoice = True

            brow = self.Start_eyebrowVM("arch", "brown", 0.3)
            shadow = self.Start_eyeshadowVM("small_shadow", 249, 127, 146, 0.3, brow)
            liner = self.Start_eyelinerVM("Middle", (12, 55, 84), 0.6, shadow)
            blusher = self.Start_blusherVM("round", "146, 127, 249", 0.3, liner)
            lip = self.Start_lipVM(246, 80, 61, 0.3, blusher)
            self.resultFace = lip
            self.changePixmap(self.resultFace)
            self.sendKind("arch", "small_shadow", "Middle", "round", isDetect)
        else:
            print("you didn't capture.")

    def Apply_OfficeThema(self, blusher_shape="round", brow_shape="arch", isDetect=False):
        self.label_text.setText("OFFICE")
        print("office click")
        if self.action == True:
            self.isChoice = True

            brow = self.Start_eyebrowVM(brow_shape, "brown", 0.3)
            shadow = self.Start_eyeshadowVM("small_shadow", 237, 190, 162, 0.3, brow)
            liner = self.Start_eyelinerVM("Middle", (34, 42, 70), 0.6, shadow)
            blusher = self.Start_blusherVM(blusher_shape, "120, 137, 241", 0.2, liner)
            lip = self.Start_lipVM(235, 86, 95, 0.3, blusher)
            self.resultFace = lip
            self.changePixmap(self.resultFace)
            self.sendKind("arch", "small_shadow", "Middle", blusher_shape, isDetect)
        else:
            print("you didn't capture.")

    ## 가상 화장 (rgb: 새도우 그대로/아이라이너 반대/블러셔반대/립그대로
    def Start_eyebrowVM(self, kind, color, alpha):
        print("start eyebrowVM")
        face = self.makeupFace.copy()
        brow = eyebrowVM.Eyebrow(kind, color)
        image = brow.eyebrow_Apply(self.landmark, face)
        result = eyebrowVM.makeupFace_face_blending(self.makeupFace, image, alpha)
        return result

    def Start_eyeshadowVM(self, kind, R, G, B, alpha, face):
        print("start eyeshadowVM")
        path = 'frame/shadowArray2.txt'
        e = eyeshadowVM.eyeshadow_class(B, G, R, kind, face, path)
        e.eyeshadow_makeup()
        e.makeupFace_shadow_blending(alpha)
        result = e.shadow_makeup_finally()
        return result

    def Start_eyelinerVM(self, kind, color, alpha, face):
        print("start eyelinerVM")
        shadow = face.copy()
        liner = eyelinerVM.Eyeliner(kind, color, shadow)
        image = liner.eyeliner_Apply(self.landmark)
        result = eyelinerVM.makeupFace_face_blending(face, image, alpha)
        return result

    def Start_blusherVM(self, kind, color, alpha, face):
        print("start blusherVM")
        file_path = "frame/" + kind + "Blusher2.txt"
        m = blusherVM.makeup(face, file_path)
        result = m.apply_makeup_all(color, alpha)
        return result

    def Start_lipVM(self, R, G, B, alpha, face):
        print("start lipVM")
        file_path = 'frame/lipsArray.txt'
        l = lipVM.lipstick_class(B, G, R, face, file_path)
        l.lipstick_makeup()
        l.makeupFace_lip_blending(alpha)
        result = l.lip_makeup_finally()
        return result

    def changePixmap(self, result):
        result = QtGui.QImage(result, result.shape[1], result.shape[0], result.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        result2 = QtGui.QPixmap(result)
        self.label_face.setPixmap(QtGui.QPixmap(result2).scaled(672, 504, Qt.KeepAspectRatio))

    def sendKind(self, brow, shadow, liner, blusher, isDetect):
        self.kindBrow = brow
        self.kindShadow = shadow
        self.kindLiner = liner
        self.kindBlusher = blusher
        self.isDetect = isDetect
        print(isDetect)

    def reset(self):
        self.label_face.clear()
        self.label_face.setText("you didn't capture")
        self.label_text.setText("")
        self.action = False
        self.isChoice = False
        self.isDetect = False
        self.tone = "False"

