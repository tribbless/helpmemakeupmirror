from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from virtual_makeup import eyebrowVM

class Shape(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
            QPushButton#pushButton_ResetALl{ border-image: url(image/ar_shape/all_reset.png); background-color: white; }
            QPushButton#pushButton_Arch{ border-image: url(image/ar_shape/eyebrow_arch_black.png); background-color: white; }
            QPushButton#pushButton_Straight{ border-image: url(image/ar_shape/eyebrow_illza_black.png); background-color: white; }
            """
        )

        self.pushButton_ResetAll = QtWidgets.QPushButton(self)
        self.pushButton_ResetAll.setMinimumSize(270, 250)
        self.pushButton_ResetAll.setObjectName("pushButton_ResetALl")

        self.pushButton_Arch = QtWidgets.QPushButton(self)
        self.pushButton_Arch.setMinimumSize(270, 250)
        self.pushButton_Arch.setObjectName("pushButton_Arch")

        self.pushButton_Straight = QtWidgets.QPushButton(self)
        self.pushButton_Straight.setMinimumSize(270, 250)
        self.pushButton_Straight.setObjectName("pushButton_Straight")


        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.pushButton_ResetAll)
        layout.setSpacing(47) #10
        layout.addWidget(self.pushButton_Arch)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Straight)

        self.setLayout(layout)

    def BTN_Select(self, brow_shape):
        # print(brow_shape)
        set = ["white", "white", "white"]
        if brow_shape == 1:
            set[1] = "black"
        elif brow_shape == 2:
            set[2] = "black"
        elif brow_shape == 0:
            set[0] = "black"
        # print(set)
        self.pushButton_ResetAll.setStyleSheet("background-color:" + set[0] + ";")
        self.pushButton_Arch.setStyleSheet("background-color:" + set[1] + ";")
        self.pushButton_Straight.setStyleSheet("background-color:" + set[2] + ";")

class Color(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
            QPushButton#pushButton_ResetColor{ border-image: url(image/ar_shape/all_reset.png); background-color: white; }
            QPushButton#pushButton_Black{ border-image: url(image/ar_color/eyebrow1.png); background-color: white; }
            QPushButton#pushButton_Brown{ border-image: url(image/ar_color/eyebrow2.png); background-color: white; }
            """
        )

        self.pushButton_ResetColor = QtWidgets.QPushButton(self)
        self.pushButton_ResetColor.setMinimumSize(270, 250)
        self.pushButton_ResetColor.setObjectName("pushButton_ResetColor")

        self.pushButton_Black = QtWidgets.QPushButton(self)
        self.pushButton_Black.setMinimumSize(270, 250)
        self.pushButton_Black.setObjectName("pushButton_Black")

        self.pushButton_Brown = QtWidgets.QPushButton(self)
        self.pushButton_Brown.setMinimumSize(270, 250)
        self.pushButton_Brown.setObjectName("pushButton_Brown")


        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.pushButton_ResetColor)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Black)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Brown)

        self.setLayout(layout)

    def BTN_Select(self, brow_color):
        # print(brow_color)
        set = ["white", "white", "white"]
        if brow_color == 1:
            set[1] = "black"
        elif brow_color == 2:
            set[2] = "black"
        elif brow_color == 0:
            set[0] = "black"
        # print(set)
        self.pushButton_ResetColor.setStyleSheet("background-color:" + set[0] + ";")
        self.pushButton_Black.setStyleSheet("background-color:" + set[1] + ";")
        self.pushButton_Brown.setStyleSheet("background-color:" + set[2] + ";")

class Select_face_Eyebrow(QWidget):

    def __init__(self):
        super(Select_face_Eyebrow, self).__init__()

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
        self.label_subject.setText("Eye brow")
        self.label_subject.setStyleSheet('color: white;')

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(50, 755, 924, 410))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 20px;")
        self.label_background_white.lower()

        # eyebrow option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(60, 765, 904, 390))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);"
                                                   "border-radius: 20px")

        # 이동 버튼 (prev/next)
        self.pushButton_GoSubMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoSubMenu.setGeometry(QtCore.QRect(60, 680, 168, 45))
        self.pushButton_GoSubMenu.setObjectName("pushButton_GoSubMenu")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoSubMenu.setFont(font)
        self.pushButton_GoSubMenu.setText("< Menu")
        self.pushButton_GoSubMenu.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        self.pushButton_GoEyeshadowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyeshadowAR.setGeometry(QtCore.QRect(796, 680, 168, 45))
        self.pushButton_GoEyeshadowAR.setObjectName("pushButton_GoEyeshadowAR")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoEyeshadowAR.setFont(font)
        self.pushButton_GoEyeshadowAR.setText("Shadow >")
        self.pushButton_GoEyeshadowAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

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
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
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

        ## 모양 버튼 클릭
        self.shape.pushButton_ResetAll.clicked.connect(self.Apply_ResetAll)
        self.shape.pushButton_Arch.clicked.connect(self.Apply_Arch)
        self.shape.pushButton_Straight.clicked.connect(self.Apply_Straight)

        ## 색상 버튼 클릭
        self.color.pushButton_ResetColor.clicked.connect(self.Apply_ResetColor)
        self.color.pushButton_Black.clicked.connect(self.Apply_Black)
        self.color.pushButton_Brown.clicked.connect(self.Apply_Brown)

    def Apply_ResetAll(self):
        print("all reset clicked")
        if self.action == True:
            self.isKind = False
            self.changePixmap(self.makeupFace)
            self.resultFace = self.makeupFace
        self.shape.BTN_Select(0)

    def Apply_Arch(self):
        if self.action == True:
            self.isKind = True
            self.kind = "arch"
        print("arch clicked")
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(1)
        self.goToColor()

    def Apply_Straight(self):
        if self.action == True:
            self.isKind = True
            self.kind = "straight"
        print("straight clicked")
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(2)
        self.goToColor()

    def Apply_ResetColor(self):
        if self.action == True:
            self.isColor = False
        print("color reset clicked")
        self.color.BTN_Select(0)
        self.slider.hide()
        self.label_slider.hide()

    def Apply_Black(self):
        self.change = "False"
        print("balck clicked")

        if self.action == True:
            self.isColor = True
            face = self.makeupFace.copy()
            brow = eyebrowVM.Eyebrow(self.kind, "black")
            self.image = brow.eyebrow_Apply(self.landmark, face)
        self.color.BTN_Select(1)
        self.slider.setValue(4)# 투명도 바 초기값으로 셋팅
        #print(self.change)
        if(self.change=="False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()



    def Apply_Brown(self):
        self.change = "False"
        print("brown clicked")
        if self.action == True:
            self.isColor = True
            face = self.makeupFace.copy()
            brow = eyebrowVM.Eyebrow(self.kind, "brown")
            self.image = brow.eyebrow_Apply(self.landmark, face)
        self.color.BTN_Select(2)
        self.slider.setValue(4)  # 투명도 바 초기값으로 셋팅
        if(self.change=="False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def changeValue(self):
        size = str((self.slider.value())*10)
        self.label_slider.setText(size+"%")
        if self.action == True:
            alpha = self.slider.value()/10
            # 투명도 조절할 때
            self.resultFace = eyebrowVM.makeupFace_face_blending(self.makeupFace, self.image, alpha)
            self.changePixmap(self.resultFace)
        self.change = "True"

    def backClicked(self):
        print("back clicked")
        self.slider.hide()
        self.label_slider.hide()
        self.pushButton_GoBack.hide()
        self.stk_w2.setCurrentWidget(self.shape)

    def goToColor(self):
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


'''
        self.label_slider.hide() # 투명도 바 숨기기
        self.slider.setValue(50) # 투명도 바 초기값으로 셋팅
        self.slider.show()  # 투명도 바 나타내기
'''



