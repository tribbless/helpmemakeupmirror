from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from virtual_makeup import blusherVM

class Shape(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
            QPushButton#pushButton_ResetALl{ border-image: url(image/ar_shape/all_reset.png); background-color: white; }
            QPushButton#pushButton_Round{ background-color: white; color:black;}
            QPushButton#pushButton_Oblong{ background-color: white; color:black;}
            QPushButton#pushButton_Square{ background-color: white; color:black;}
            """
        )

        self.pushButton_ResetAll = QtWidgets.QPushButton(self)
        self.pushButton_ResetAll.setMinimumSize(270, 250)
        self.pushButton_ResetAll.setObjectName("pushButton_ResetALl")

        self.pushButton_Round = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_Round.setMinimumSize(270, 250)
        self.pushButton_Round.setText("Round")
        self.pushButton_Round.setFont(font)
        self.pushButton_Round.setObjectName("pushButton_Round")

        self.pushButton_Oblong = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_Oblong.setMinimumSize(270, 250)
        self.pushButton_Oblong.setText("Oblong")
        self.pushButton_Oblong.setFont(font)
        self.pushButton_Oblong.setObjectName("pushButton_Oblong")

        self.pushButton_Square = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_Square.setMinimumSize(270, 250)
        self.pushButton_Square.setText("Square")
        self.pushButton_Square.setFont(font)
        self.pushButton_Square.setObjectName("pushButton_Square")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetAll)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Round)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Oblong)
        layout.setSpacing(47)
        layout.addWidget(self.pushButton_Square)

        self.setLayout(layout)

    def BTN_Select(self, blusher_shape):
        # print(blusher_shape)
        set = ["white", "white", "white", "white"]
        set2 = ["black", "black", "black"]  # 글씨 색
        if blusher_shape == 1:
            set[1] = "black"
            set2[0] = "white"
        elif blusher_shape == 2:
            set[2] = "black"
            set2[1] = "white"
        elif blusher_shape == 3:
            set[3] = "black"
            set2[2] = "white"
        elif blusher_shape == 0:
            set[0] = "black"
        # print(set)
        # print(set2)
        self.pushButton_ResetAll.setStyleSheet("background-color:" + set[0] + ";")
        self.pushButton_Round.setStyleSheet("background-color:" + set[1] + "; color:" + set2[0] + ";")
        self.pushButton_Oblong.setStyleSheet("background-color:" + set[2] + "; color:" + set2[1] + ";")
        self.pushButton_Square.setStyleSheet("background-color:" + set[3] + "; color:" + set2[2] + ";")


class Color(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
            QPushButton#pushButton_ResetColor{ border-image: url(image/ar_shape/all_reset.png); background-color: white; }
            QPushButton#pushButton_ColorOne{ border-image: url(image/ar_color/blusher1.png); background-color: white; }
            QPushButton#pushButton_ColorTwo{ border-image: url(image/ar_color/blusher2.png); background-color: white; }
            QPushButton#pushButton_ColorThree{ border-image: url(image/ar_color/blusher3.png); background-color: white; }
            QPushButton#pushButton_ColorFour{ border-image: url(image/ar_color/blusher4.png); background-color: white; }
            QPushButton#pushButton_ColorFive{ border-image: url(image/ar_color/blusher5.png); background-color: white; }
            QPushButton#pushButton_ColorSix{ border-image: url(image/ar_color/blusher6.png); background-color: white; }
            QPushButton#pushButton_ColorSeven{ border-image: url(image/ar_color/blusher7.png); background-color: white; }
            QPushButton#pushButton_ColorEight{ border-image: url(image/ar_color/blusher8.png); background-color: white; } 
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

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
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


        self.setLayout(layout)

    def BTN_Select(self, blusher_color):
        # print(blusher_color)
        set = ["white", "white", "white", "white", "white", "white", "white", "white", "white"]
        if blusher_color == 1:
            set[1] = "black"
        elif blusher_color == 2:
            set[2] = "black"
        elif blusher_color == 3:
            set[3] = "black"
        elif blusher_color == 4:
            set[4] = "black"
        elif blusher_color == 5:
            set[5] = "black"
        elif blusher_color == 6:
            set[6] = "black"
        elif blusher_color == 7:
            set[7] = "black"
        elif blusher_color == 8:
            set[8] = "black"
        elif blusher_color == 0:
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


class Select_face_Blusher(QWidget):

    def __init__(self):
        super(Select_face_Blusher, self).__init__()

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
        self.label_subject.setText("Blusher")
        self.label_subject.setStyleSheet('color: white')

        self.label_background_white = QtWidgets.QLabel(self)
        self.label_background_white.setGeometry(QtCore.QRect(50, 755, 924, 410))
        self.label_background_white.setObjectName("label_background_white")
        self.label_background_white.setStyleSheet("background-color: white;"
                                                  "border-radius: 20px;")
        self.label_background_white.lower()

        # blusher option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(60, 765, 904, 390))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);"
                                                   "border-radius: 20px;")


        # 이동 버튼 (prev/next)
        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(60, 680, 168, 45))
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("< Eyeliner")
        self.pushButton_GoEyelinerAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoLipAR = QtWidgets.QPushButton(self)
        self.pushButton_GoLipAR.setGeometry(QtCore.QRect(796, 680, 168, 45))
        self.pushButton_GoLipAR.setObjectName("pushButton_GoLipAR")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_GoLipAR.setFont(font)
        self.pushButton_GoLipAR.setText("Lip >")
        self.pushButton_GoLipAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

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

        self.label_slider = QtWidgets.QLabel(self)
        self.label_slider.setGeometry(QtCore.QRect(800, 785, 164, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(25)
        self.label_slider.setFont(font)
        self.label_slider.setAlignment(Qt.AlignCenter)
        self.label_slider.setText("0%")
        self.label_slider.setStyleSheet('color: white;')
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
        self.stk_w2.setMaximumWidth(1221)

        ## 모양 버튼 클릭
        self.shape.pushButton_ResetAll.clicked.connect(self.Apply_ResetAll)
        self.shape.pushButton_Round.clicked.connect(self.Apply_Round)
        self.shape.pushButton_Oblong.clicked.connect(self.Apply_Oblong)
        self.shape.pushButton_Square.clicked.connect(self.Apply_Square)

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

    def Apply_ResetAll(self):
        print("all reset clicked")
        if self.action == True:
            self.isKind = False
            self.changePixmap(self.makeupFace)
            self.resultFace = self.makeupFace
        self.shape.BTN_Select(0)


    def Apply_Round(self):
        print("round clicked")
        if self.action == True:
            self.isKind = True
            self.kind = "round"
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(1)
        self.goToColor()

    def Apply_Oblong(self):
        print("oblong clicked")
        if self.action == True:
            self.isKind = True
            self.kind = "oblong"
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(2)
        self.goToColor()

    def Apply_Square(self):
        print("square clicked")
        if self.action == True:
            self.isKind = True
            self.kind = "square"
        self.pushButton_GoBack.show()
        self.shape.BTN_Select(3)
        self.goToColor()

    def Apply_ResetColor(self):
        print("color reset clicked")
        if self.action == True:
            self.isColor = False
        # print(self.color.pushButton_ResetColor.height())
        # print(self.color.pushButton_ResetColor.width())
        self.color.BTN_Select(0)
        self.slider.hide()
        self.label_slider.hide()

    def Apply_ColorOne(self):
        self.change = "False"
        print("ColorOne clicked")
        self.colorName = "179, 181, 251"
        self.color.BTN_Select(1)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorTwo(self):
        self.change = "False"
        print("ColorTwo clicked")
        self.colorName = "155, 174, 249"
        self.color.BTN_Select(2)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorThree(self):
        self.change = "False"
        print("ColorThree clicked")
        self.colorName = "164, 172, 229"
        self.color.BTN_Select(3)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorFour(self):
        self.change = "False"
        print("ColorFour clicked")
        self.colorName = "122, 157, 243"
        self.color.BTN_Select(4)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorFive(self):
        self.change = "False"
        print("ColorFive clicked")
        self.colorName = "93, 109, 232"
        self.color.BTN_Select(5)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorSix(self):
        self.change = "False"
        print("ColorSix clicked")
        self.colorName = "64, 104, 246"
        self.color.BTN_Select(6)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorSeven(self):
        self.change = "False"
        print("ColorSeven clicked")
        self.colorName = "105, 89, 240"
        self.color.BTN_Select(7)
        self.slider.setValue(3)  # 투명도 바 초기값으로 셋팅
        if (self.change == "False"):
            self.changeValue()
        self.slider.show()
        self.label_slider.show()

    def Apply_ColorEight(self):
        self.change = "False"
        print("ColorEight clicked")
        self.colorName = "87, 64, 225"
        self.color.BTN_Select(8)
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
            file_path = "frame/"+self.kind+"Blusher2.txt"
            m = blusherVM.makeup(self.makeupFace, file_path)
            alpha = self.slider.value() / 10
            self.resultFace = m.apply_makeup_all(self.colorName, alpha)
            self.changePixmap(self.resultFace)
        self.change = "True"

    def backClicked(self):
        print("back clicked")
        self.slider.hide()
        self.label_slider.hide()
        self.pushButton_GoBack.hide()
        self.stk_w2.setMaximumWidth(1221)
        self.stk_w2.setCurrentWidget(self.shape)

    def goToColor(self):
        self.stk_w2.setMaximumWidth(2806)
        self.color.BTN_Select(-1)
        self.stk_w2.setCurrentWidget(self.color)

    def changePixmap(self, result):
        result = QtGui.QImage(result, result.shape[1], result.shape[0], result.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        result2 = QtGui.QPixmap(result)
        self.label_face.setPixmap(QtGui.QPixmap(result2).scaled(672, 504, Qt.KeepAspectRatio))

    def reset(self):
        print("blusher resetALL")
        self.label_face.clear()
        self.label_face.setText("you didn't capture")
        self.action = False # 앞에 화면에서 캡쳐했는지 check
        self.isKind = False # 종류(모양) 선택했는지 check
        self.isColor = False # 컬러 선택했는지 check
        self.backClicked()
        self.shape.BTN_Select(-1)
        self.scrollArea.horizontalScrollBar().setValue(0)