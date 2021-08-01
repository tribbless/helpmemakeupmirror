from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from virtual_makeup import eyeshadowVM

class Shape(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
            QPushButton#pushButton_ResetALl{ border-image: url(image/ar_shape/all_reset.png); background-color: white; }
            QPushButton#pushButton_Middle{ background-color: white; color: black;}
            QPushButton#pushButton_Large{ background-color: white; color: black;}
            QPushButton#pushButton_Small{ background-color: white; color: black;}
            """
        )

        self.pushButton_ResetAll = QtWidgets.QPushButton(self)
        self.pushButton_ResetAll.setMinimumSize(270, 250)
        self.pushButton_ResetAll.setObjectName("pushButton_ResetALl")

        self.pushButton_Middle = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_Middle.setMinimumSize(270, 250)
        self.pushButton_Middle.setText("Middle")
        self.pushButton_Middle.setFont(font)
        self.pushButton_Middle.setObjectName("pushButton_Middle")

        self.pushButton_Large = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_Large.setMinimumSize(270, 250)
        self.pushButton_Large.setText("Large")
        self.pushButton_Large.setFont(font)
        self.pushButton_Large.setObjectName("pushButton_Large")

        self.pushButton_Small = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_Small.setMinimumSize(270, 250)
        self.pushButton_Small.setText("Small")
        self.pushButton_Small.setFont(font)
        self.pushButton_Small.setObjectName("pushButton_Small")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetAll)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Small)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Middle)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Large)


        self.setLayout(layout)

    def BTN_Select(self, shadow_shape):
        # print(shadow_shape)
        set = ["white", "white", "white", "white"]
        set2 = ["black", "black", "black"]  # 글씨 색
        if shadow_shape == 1:
            set[1] = "black"
            set2[0] = "white"
        elif shadow_shape == 2:
            set[2] = "black"
            set2[1] = "white"
        elif shadow_shape == 3:
            set[3] = "black"
            set2[2] = "white"
        elif shadow_shape == 0:
            set[0] = "black"
        # print(set)
        # print(set2)
        self.pushButton_ResetAll.setStyleSheet("background-color:" + set[0] + ";")
        self.pushButton_Small.setStyleSheet("background-color:" + set[1] + "; color:" + set2[0] + ";")
        self.pushButton_Middle.setStyleSheet("background-color:" + set[2] + "; color:" + set2[1] + ";")
        self.pushButton_Large.setStyleSheet("background-color:" + set[3] + "; color:" + set2[2] + ";")

class Color(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
            QPushButton#pushButton_ResetColor{ border-image: url(image/ar_shape/all_reset.png); background-color: white;}
            QPushButton#pushButton_ColorOne{ border-image: url(image/ar_color/eyeshadow1.png); background-color: white;}
            QPushButton#pushButton_ColorTwo{ border-image: url(image/ar_color/eyeshadow2.png); background-color: white;}
            QPushButton#pushButton_ColorThree{ border-image: url(image/ar_color/eyeshadow3.png); background-color: white;}
            QPushButton#pushButton_ColorFour{ border-image: url(image/ar_color/eyeshadow4.png); background-color: white;}
            QPushButton#pushButton_ColorFive{ border-image: url(image/ar_color/eyeshadow5.png); background-color: white;}
            QPushButton#pushButton_ColorSix{ border-image: url(image/ar_color/eyeshadow6.png); background-color: white;}
            QPushButton#pushButton_ColorSeven{ border-image: url(image/ar_color/eyeshadow7.png); background-color: white;}
            QPushButton#pushButton_ColorEight{ border-image: url(image/ar_color/eyeshadow8.png); background-color: white;}
            QPushButton#pushButton_ColorNine{ border-image: url(image/ar_color/eyeshadow9.png); background-color: white;}  
            """
        )

        self.pushButton_ResetColor = QtWidgets.QPushButton(self)
        self.pushButton_ResetColor.setMinimumSize(270, 250)
        self.pushButton_ResetColor.setObjectName("pushButton_ResetColor")

        self.pushButton_ColorOne = QtWidgets.QPushButton(self)
        self.pushButton_ColorOne.setMinimumSize(270, 250)
        self.pushButton_ColorOne.setObjectName("pushButton_ColorOne")

        self.pushButton_ColorTwo = QtWidgets.QPushButton(self)
        self.pushButton_ColorTwo.setMinimumSize(270, 250)
        self.pushButton_ColorTwo.setObjectName("pushButton_ColorTwo")

        self.pushButton_ColorThree = QtWidgets.QPushButton(self)
        self.pushButton_ColorThree.setMinimumSize(270, 250)
        self.pushButton_ColorThree.setObjectName("pushButton_ColorThree")

        self.pushButton_ColorFour = QtWidgets.QPushButton(self)
        self.pushButton_ColorFour.setMinimumSize(270, 250)
        self.pushButton_ColorFour.setObjectName("pushButton_ColorFour")

        self.pushButton_ColorFive = QtWidgets.QPushButton(self)
        self.pushButton_ColorFive.setMinimumSize(270, 250)
        self.pushButton_ColorFive.setObjectName("pushButton_ColorFive")

        self.pushButton_ColorSix = QtWidgets.QPushButton(self)
        self.pushButton_ColorSix.setMinimumSize(270, 250)
        self.pushButton_ColorSix.setObjectName("pushButton_ColorSix")

        self.pushButton_ColorSeven = QtWidgets.QPushButton(self)
        self.pushButton_ColorSeven.setMinimumSize(270, 250)
        self.pushButton_ColorSeven.setObjectName("pushButton_ColorSeven")

        self.pushButton_ColorEight = QtWidgets.QPushButton(self)
        self.pushButton_ColorEight.setMinimumSize(270, 250)
        self.pushButton_ColorEight.setObjectName("pushButton_ColorEight")

        self.pushButton_ColorNine = QtWidgets.QPushButton(self)
        self.pushButton_ColorNine.setMinimumSize(270, 250)
        self.pushButton_ColorNine.setObjectName("pushButton_ColorNine")

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.pushButton_ResetColor)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorOne)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorTwo)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorThree)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorFour)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorFive)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorSix)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorSeven)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorEight)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_ColorNine)

        self.setLayout(layout)

    def BTN_Select(self, shadow_color):
        # print(shadow_color)
        set = ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white"]
        if shadow_color == 1:
            set[1] = "black"
        elif shadow_color == 2:
            set[2] = "black"
        elif shadow_color == 3:
            set[3] = "black"
        elif shadow_color == 4:
            set[4] = "black"
        elif shadow_color == 5:
            set[5] = "black"
        elif shadow_color == 6:
            set[6] = "black"
        elif shadow_color == 7:
            set[7] = "black"
        elif shadow_color == 8:
            set[8] = "black"
        elif shadow_color == 9:
            set[9] = "black"
        elif shadow_color == 0:
            set[0] = "black"
        # print(set)
        self.pushButton_ResetColor.setStyleSheet("background-color:" + set[0] + ";")
        self.pushButton_ColorOne.setStyleSheet("background-color:" + set[1] + ";")
        self.pushButton_ColorTwo.setStyleSheet("background-color:" + set[2] + ";")
        self.pushButton_ColorThree.setStyleSheet("background-color:" + set[3] + ";")
        self.pushButton_ColorFour.setStyleSheet("background-color:" + set[4] + ";")
        self.pushButton_ColorFive.setStyleSheet("background-color:" + set[5] + ";")
        self.pushButton_ColorSix.setStyleSheet("background-color:" + set[6] + ";")
        self.pushButton_ColorSeven.setStyleSheet("background-color:" + set[7] + ";")
        self.pushButton_ColorEight.setStyleSheet("background-color:" + set[8] + ";")
        self.pushButton_ColorNine.setStyleSheet("background-color:" + set[9] + ";")

class Select_face_Eyeshadow(QWidget):

    def __init__(self):
        super(Select_face_Eyeshadow, self).__init__()

        self.action = False # 앞에 화면에서 캡쳐했는지 check
        self.isKind = False # 종류(모양) 선택했는지 check
        self.isColor = False # 컬러 선택했는지 check

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

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(228, 680, 568, 45))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("Eye shadow")
        self.label_subject.setStyleSheet('color: white;')

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(50, 755, 924, 410))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 20px;")
        self.label_background_white.lower()

        # eyeshadow option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(60, 765, 904, 390))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);"
                                                   "border-radius: 20px;")

        # 이동 버튼 (prev/next)
        self.pushButton_GoEyebrowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowAR.setGeometry(QtCore.QRect(60, 680, 168, 45))
        self.pushButton_GoEyebrowAR.setObjectName("pushButton_GoEyebrowAR")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoEyebrowAR.setFont(font)
        self.pushButton_GoEyebrowAR.setText("< Eyebrow")
        self.pushButton_GoEyebrowAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(796, 680, 168, 45))
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("Eyeliner >")
        self.pushButton_GoEyelinerAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        ## 선택화면 안 요소..
        # 모양화면으로 back 버튼
        self.pushButton_GoBack = QtWidgets.QPushButton(self)
        self.pushButton_GoBack.setGeometry(QtCore.QRect(107, 785, 45, 50))
        self.pushButton_GoBack.setObjectName("pushButton_GoBack")
        self.pushButton_GoBack.setStyleSheet("border-image: url(image/btn_triangle2.png);")
        self.pushButton_GoBack.clicked.connect(self.backClicked)
        self.pushButton_GoBack.hide()


        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(QtCore.QRect(200, 785, 600, 50))
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.valueChanged.connect(self.changeValue)
        self.slider.setStyleSheet(
            """
            QSlider::groove:horizontal{
                border-radius: 1px;
                height: 10px;
                margin: 0px;
                background-color: rgb(52, 59, 72);
            }
            QSlider::groove:horizontal:hover {
                background-color: rgb(55, 62, 76);
            }
            QSlider::handle:horizontal {
                background-color: white;
                border: none;
                height: 25px;
                width: 30px;
                margin: -10px 0;
                border-radius: 15px;
                padding: -10px 0px;
            }
            QSlider::handle:horizontal:pressed {
                background-color: white;
            }
            QSlider::add-page:qlineargradient {
                background: rgb(227,218,243);
                border-top-right-radius: 9px;
                border-bottom-right-radius: 9px;
                border-top-left-radius: 0px;
                border-bottom-left-radius: 0px;
            }
            QSlider::sub-page:qlineargradient {
                background: white;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
                border-top-left-radius: 9px;
                border-bottom-left-radius: 9px;
            }
            """
        )
        self.slider.hide()


        self.label_slider =QtWidgets.QLabel(self)
        self.label_slider.setGeometry(QtCore.QRect(800, 785, 164, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(25)
        self.label_slider.setFont(font)
        self.label_slider.setAlignment(Qt.AlignCenter)
        self.label_slider.setText("0%")
        self.label_slider.setStyleSheet('color:white;')
        self.label_slider.hide()

        ##
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(60, 855, 904, 300)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # #FFFFFF;
        self.scrollArea.setStyleSheet(
            """
            QScrollArea {
                background: transparent;
                border: 0px;
            } 
            QScrollBar:horizontal {
                border: 3px solid #A3A3A3;
                border-radius: 7px;
                background: #F3C5D8;
                height: 50px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background: #A3A3A3;
                min-width: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:horizontal {
                width: 0px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:horizontal {
                width: 0px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }
            """
        )
        self.stk_w2 = QStackedWidget(self)
        self.stk_w2.setStyleSheet("background-color: transparent; border: 0px;")
        self.shape = Shape()
        self.color = Color()
        self.stk_w2.addWidget(self.shape)
        self.stk_w2.addWidget(self.color)
        self.scrollArea.setWidget(self.stk_w2)
        self.stk_w2.setMaximumWidth(1221)

        ## 모양 버튼 클릭
        self.shape.pushButton_ResetAll.clicked.connect(self.Apply_ResetAll)
        self.shape.pushButton_Middle.clicked.connect(self.Apply_Middle)
        self.shape.pushButton_Large.clicked.connect(self.Apply_Large)
        self.shape.pushButton_Small.clicked.connect(self.Apply_Small)

        ## 색상 버튼 클릭
        self.color.pushButton_ResetColor.clicked.connect(self.Apply_ResetColor)
        self.color.pushButton_ColorOne.clicked.connect(self.Apply_ColorOne)
        self.color.pushButton_ColorTwo.clicked.connect(self.Apply_ColorTwo)
        self.color.pushButton_ColorThree.clicked.connect(self.Apply_ColorThree)
        self.color.pushButton_ColorFour.clicked.connect(self.Apply_ColorFour)
        self.color.pushButton_ColorFive.clicked.connect(self.Apply_ColorFive)
        self.color.pushButton_ColorSix.clicked.connect(self.Apply_ColorSix)
        self.color.pushButton_ColorSeven.clicked.connect(self.Apply_ColorSeven)
        self.color.pushButton_ColorEight.clicked.connect(self.Apply_ColorEight)
        self.color.pushButton_ColorNine.clicked.connect(self.Apply_ColorNine)

    def Apply_ResetAll(self):
        print("[select_face_eyeshadow.py] all reset clicked")
        if self.action == True:
            self.isKind = False
            self.changePixmap(self.makeupFace)
            self.resultFace = self.makeupFace
        self.shape.BTN_Select(0)
        # print(self.shape.pushButton_ResetAll.height())
        # print(self.shape.pushButton_ResetAll.width())

    def Apply_Small(self):
        print("[select_face_eyeshadow.py] small clicked")
        if self.action == True:
            self.isKind = True
            self.kind = "small_shadow"
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(1)
        self.goToColor()

    def Apply_Middle(self):
        print("[select_face_eyeshadow.py] middle clicked")
        if self.action == True:
            self.isKind = True
            self.kind = "middle_shadow"
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(2)
        self.goToColor()

    def Apply_Large(self):
        print("[select_face_eyeshadow.py] large clicked")
        if self.action == True:
            self.isKind = True
            self.kind = "large_shadow"
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(3)
        self.goToColor()


    def Apply_ResetColor(self):
        if self.action == True:
            self.isColor = False
        print("[select_face_eyeshadow.py] color reset clicked")
        # print(self.color.pushButton_ResetColor.height())
        # print(self.color.pushButton_ResetColor.width())
        self.color.BTN_Select(0)
        self.slider.hide()
        self.label_slider.hide()

    def Apply_ColorOne(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorOne clicked")
        self.R = 247
        self.G = 157
        self.B = 155
        self.color.BTN_Select(1)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorTwo(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorTwo clicked")
        self.R = 225
        self.G = 157
        self.B = 167
        self.color.BTN_Select(2)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorThree(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorThree clicked")
        self.R = 198
        self.G = 113
        self.B = 120
        self.color.BTN_Select(3)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorFour(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorFour clicked")
        self.R = 220
        self.G = 118
        self.B = 113
        self.color.BTN_Select(4)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorFive(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorFive clicked")
        self.R = 187
        self.G = 90
        self.B = 88
        self.color.BTN_Select(5)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorSix(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorSix clicked")
        self.R = 203
        self.G = 154
        self.B = 122
        self.color.BTN_Select(6)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorSeven(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorSeven clicked")
        self.R = 182
        self.G = 134
        self.B = 88
        self.color.BTN_Select(7)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorEight(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorEight clicked")
        #print(self.stk_w2.width())
        self.R = 148
        self.G = 97
        self.B = 52
        self.color.BTN_Select(8)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorNine(self):
        self.change = "False"
        print("[select_face_eyeshadow.py] ColorNine clicked")
        #print(self.stk_w2.width())
        self.R = 104
        self.G = 61
        self.B = 27
        self.color.BTN_Select(9)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def changeValue(self):
        size = str((self.slider.value()) * 10)
        self.label_slider.setText(size + "%")
        if self.action == True:
            self.isColor = True
            path = 'frame/shadowArray2.txt'
            e = eyeshadowVM.eyeshadow_class(self.B, self.G, self.R, self.kind, self.makeupFace, path)
            e.eyeshadow_makeup()
            # 투명도 조절
            alpha = self.slider.value() / 10
            e.makeupFace_shadow_blending(alpha)
            self.resultFace = e.shadow_makeup_finally()
            self.changePixmap(self.resultFace)
        self.change = "True"

    def backClicked(self):
        print("[select_face_eyeshadow.py] back clicked")
        self.slider.hide()
        self.label_slider.hide()
        self.pushButton_GoBack.hide()
        self.stk_w2.setMaximumWidth(1221)
        self.stk_w2.setCurrentWidget(self.shape)

    def goToColor(self):
        self.stk_w2.setMaximumWidth(3123)
        self.color.BTN_Select(-1)
        self.stk_w2.setCurrentWidget(self.color)

    def changePixmap(self, result):
        result = QtGui.QImage(result, result.shape[1], result.shape[0], result.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        result2 = QtGui.QPixmap(result)
        self.label_face.setPixmap(QtGui.QPixmap(result2).scaled(672, 504, Qt.KeepAspectRatio))

    def reset(self):
        self.label_face.clear()
        self.label_face.setText("you didn't capture")
        self.action = False # 앞에 화면에서 캡쳐했는지 check
        self.isKind = False # 종류(모양) 선택했는지 check
        self.isColor = False # 컬러 선택했는지 check
        self.backClicked()
        self.shape.BTN_Select(-1)
        self.scrollArea.horizontalScrollBar().setValue(0)