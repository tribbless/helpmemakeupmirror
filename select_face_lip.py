from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from virtual_makeup import lipVM


class Select_face_Lip(QWidget):

    def __init__(self):
        super(Select_face_Lip, self).__init__()

        self.action = False # 앞에 화면에서 캡쳐했는지 check
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
        self.label_subject.setText("Lip")
        self.label_subject.setStyleSheet('color: white;')

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(50, 755, 924, 410))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 20px;")
        self.label_background_white.lower()

        # lip option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(60, 765, 904, 370))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);"
                                                   "border-radius: 20px;")


        # 이동 버튼 (prev/next)
        self.pushButton_GoBlusherAR = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusherAR.setGeometry(QtCore.QRect(60, 680, 168, 45))
        self.pushButton_GoBlusherAR.setObjectName("pushButton_GoBlusherAR")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoBlusherAR.setFont(font)
        self.pushButton_GoBlusherAR.setText("< Blusher")
        self.pushButton_GoBlusherAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoEyebrowFrame = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowFrame.setGeometry(QtCore.QRect(796, 680, 168, 45))
        self.pushButton_GoEyebrowFrame.setObjectName("pushButton_GoEyebrowFrame")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoEyebrowFrame.setFont(font)
        self.pushButton_GoEyebrowFrame.setText("Frame >")
        self.pushButton_GoEyebrowFrame.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 1184, 1024, 72))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        ## 선택화면 안 요소..
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
        self.setStyleSheet(
            """
            QPushButton#pushButton_ResetColor{
                border-image: url(image/ar_shape/all_reset.png);
                background-color: white; }
            QPushButton#pushButton_ColorOne{
                border-image: url(image/ar_color/lip1.png);
                background-color: white; }
            QPushButton#pushButton_ColorTwo{
                border-image: url(image/ar_color/lip2.png);
                background-color: white; }
            QPushButton#pushButton_ColorThree{
                border-image: url(image/ar_color/lip3.png);
                background-color: white; }
            QPushButton#pushButton_ColorFour{
                border-image: url(image/ar_color/lip4.png);
                background-color: white; }
            QPushButton#pushButton_ColorFive{
                border-image: url(image/ar_color/lip5.png);
                background-color: white; }
            QPushButton#pushButton_ColorSix{
                border-image: url(image/ar_color/lip6.png);
                background-color: white; }
            """
        )

        ## 색상 버튼
        self.pushButton_ResetColor = QtWidgets.QPushButton(self)
        self.pushButton_ResetColor.setMinimumSize(270, 250)
        self.pushButton_ResetColor.setObjectName("pushButton_ResetColor")
        self.pushButton_ResetColor.clicked.connect(self.Apply_ResetColor)

        self.pushButton_ColorOne = QtWidgets.QPushButton(self)
        self.pushButton_ColorOne.setMinimumSize(270, 250)
        self.pushButton_ColorOne.setObjectName("pushButton_ColorOne")
        self.pushButton_ColorOne.clicked.connect(self.Apply_ColorOne)

        self.pushButton_ColorTwo = QtWidgets.QPushButton(self)
        self.pushButton_ColorTwo.setMinimumSize(270, 250)
        self.pushButton_ColorTwo.setObjectName("pushButton_ColorTwo")
        self.pushButton_ColorTwo.clicked.connect(self.Apply_ColorTwo)

        self.pushButton_ColorThree = QtWidgets.QPushButton(self)
        self.pushButton_ColorThree.setMinimumSize(270, 250)
        self.pushButton_ColorThree.setObjectName("pushButton_ColorThree")
        self.pushButton_ColorThree.clicked.connect(self.Apply_ColorThree)

        self.pushButton_ColorFour = QtWidgets.QPushButton(self)
        self.pushButton_ColorFour.setMinimumSize(270, 250)
        self.pushButton_ColorFour.setObjectName("pushButton_ColorFour")
        self.pushButton_ColorFour.clicked.connect(self.Apply_ColorFour)

        self.pushButton_ColorFive = QtWidgets.QPushButton(self)
        self.pushButton_ColorFive.setMinimumSize(270, 250)
        self.pushButton_ColorFive.setObjectName("pushButton_ColorFive")
        self.pushButton_ColorFive.clicked.connect(self.Apply_ColorFive)

        self.pushButton_ColorSix = QtWidgets.QPushButton(self)
        self.pushButton_ColorSix.setMinimumSize(270, 250)
        self.pushButton_ColorSix.setObjectName("pushButton_ColorSix")
        self.pushButton_ColorSix.clicked.connect(self.Apply_ColorSix)

        ## 레이아웃
        widget = QWidget(self.scrollArea)
        widget.setStyleSheet("background-color: transparent; border: 0px")
        scrollLayout = QHBoxLayout(widget)
        scrollLayout.setContentsMargins(0, 0, 0, 0)
        scrollLayout.addWidget(self.pushButton_ResetColor)
        scrollLayout.setSpacing(47)
        scrollLayout.addWidget(self.pushButton_ColorOne)
        scrollLayout.setSpacing(47)
        scrollLayout.addWidget(self.pushButton_ColorTwo)
        scrollLayout.setSpacing(47)
        scrollLayout.addWidget(self.pushButton_ColorThree)
        scrollLayout.setSpacing(47)
        scrollLayout.addWidget(self.pushButton_ColorFour)
        scrollLayout.setSpacing(47)
        scrollLayout.addWidget(self.pushButton_ColorFive)
        scrollLayout.setSpacing(47)
        scrollLayout.addWidget(self.pushButton_ColorSix)
        widget.setLayout(scrollLayout)
        self.scrollArea.setWidget(widget)

        self.BTN_Select(-1)

    def BTN_Select(self, lip_color):
        # print(lip_color)
        set = ["white", "white", "white", "white", "white", "white", "white"]
        if lip_color == 1:
            set[1] = "black"
        elif lip_color == 2:
            set[2] = "black"
        elif lip_color == 3:
            set[3] = "black"
        elif lip_color == 4:
            set[4] = "black"
        elif lip_color == 5:
            set[5] = "black"
        elif lip_color == 6:
            set[6] = "black"
        elif lip_color == 0:
            set[0] = "black"
        # print(set)
        self.pushButton_ResetColor.setStyleSheet("background-color:" + set[0] + ";")
        self.pushButton_ColorOne.setStyleSheet("background-color:" + set[1] + ";")
        self.pushButton_ColorTwo.setStyleSheet("background-color:" + set[2] + ";")
        self.pushButton_ColorThree.setStyleSheet("background-color:" + set[3] + ";")
        self.pushButton_ColorFour.setStyleSheet("background-color:" + set[4] + ";")
        self.pushButton_ColorFive.setStyleSheet("background-color:" + set[5] + ";")
        self.pushButton_ColorSix.setStyleSheet("background-color:" + set[6] + ";")

    def Apply_ResetColor(self):
        print("color reset clicked")
        if self.action == True:
            self.isColor = False
            self.changePixmap(self.makeupFace)
            self.resultFace = self.makeupFace
        self.BTN_Select(0)
        self.slider.hide()
        self.label_slider.hide()

    def Apply_ColorOne(self):
        self.change = "False"
        print("ColorOne clicked")
        self.R = 200
        self.G = 6
        self.B = 6
        self.BTN_Select(1)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorTwo(self):
        self.change = "False"
        print("ColorTwo clicked")
        self.R = 227
        self.G = 67
        self.B = 62
        self.BTN_Select(2)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorThree(self):
        self.change = "False"
        print("ColorThree clicked")
        self.R = 249
        self.G = 107
        self.B = 125
        self.BTN_Select(3)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorFour(self):
        self.change = "False"
        print("ColorFour clicked")
        self.R = 167
        self.G = 57
        self.B = 46
        self.BTN_Select(4)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorFive(self):
        self.change = "False"
        print("ColorFive clicked")
        self.R = 125
        self.G = 19
        self.B = 15
        self.BTN_Select(5)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorSix(self):
        self.change = "False"
        print("ColorSix clicked")
        self.R = 94
        self.G = 1
        self.B = 2
        self.BTN_Select(6)
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
            file_path = 'frame/lipsArray.txt'
            l = lipVM.lipstick_class(self.B, self.G, self.R, self.makeupFace, file_path)
            l.lipstick_makeup()
            # 투명도 조절
            alpha = self.slider.value()/10
            l.makeupFace_lip_blending(alpha)
            self.resultFace = l.lip_makeup_finally()
            self.changePixmap(self.resultFace)
        self.change = "True"

    def changePixmap(self, result):
        result = QtGui.QImage(result, result.shape[1], result.shape[0], result.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        result2 = QtGui.QPixmap(result)
        self.label_face.setPixmap(QtGui.QPixmap(result2).scaled(672, 504, Qt.KeepAspectRatio))

    def reset(self):
        print("lip resetALL")
        self.label_face.clear()
        self.label_face.setText("you didn't capture")
        self.action = False # 앞에 화면에서 캡쳐했는지 check
        self.isColor = False # 컬러 선택했는지 check
        self.slider.hide()
        self.label_slider.hide()
        self.BTN_Select(-1)
        self.scrollArea.horizontalScrollBar().setValue(0)
