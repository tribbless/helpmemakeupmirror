from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Shape(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButton_ResetAll = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ResetAll.setMinimumSize(172, 150)
        self.pushButton_ResetAll.setText("all reset")
        self.pushButton_ResetAll.setFont(font)
        self.pushButton_ResetAll.setStyleSheet('background-color:white;')
        self.pushButton_ResetAll.setObjectName("pushButton_ResetALl")

        self.pushButton_Middle = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Middle.setMinimumSize(172, 150)
        self.pushButton_Middle.setText("middle")
        self.pushButton_Middle.setFont(font)
        self.pushButton_Middle.setStyleSheet('background-color:white;')
        self.pushButton_Middle.setObjectName("pushButton_Middle")

        self.pushButton_Up = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Up.setMinimumSize(172, 150)
        self.pushButton_Up.setText("up")
        self.pushButton_Up.setFont(font)
        self.pushButton_Up.setStyleSheet('background-color:white;')
        self.pushButton_Up.setObjectName("pushButton_Up")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetAll)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Middle)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Up)

        self.setLayout(layout)

class Color(QWidget):
    def __init__(self):
        super().__init__()

        self.pushButton_ResetColor = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ResetColor.setMinimumSize(172, 150)
        self.pushButton_ResetColor.setText("color reset")
        self.pushButton_ResetColor.setFont(font)
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ResetColor.setObjectName("pushButton_ResetColor")

        self.pushButton_Black = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Black.setMinimumSize(172, 150)
        self.pushButton_Black.setText("black")
        self.pushButton_Black.setFont(font)
        self.pushButton_Black.setStyleSheet('background-color:white;')
        self.pushButton_Black.setObjectName("pushButton_Black")

        self.pushButton_Brown = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Brown.setMinimumSize(172, 150)
        self.pushButton_Brown.setText("brown")
        self.pushButton_Brown.setFont(font)
        self.pushButton_Brown.setStyleSheet('background-color:white;')
        self.pushButton_Brown.setObjectName("pushButton_Brown")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetColor)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Black)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Brown)

        self.setLayout(layout)

class Select_face_Eyeliner(QWidget):

    def __init__(self):
        super(Select_face_Eyeliner, self).__init__()

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(125, 57, 312, 416))
        self.label_face.setObjectName("label_face")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_face.setFont(font)
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # subject
        self.label_subject = QtWidgets.QLabel(self)
        self.label_subject.setGeometry(QtCore.QRect(125, 484, 312, 30))
        self.label_subject.setObjectName("label_subject")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_subject.setFont(font)
        self.label_subject.setAlignment(Qt.AlignCenter)
        self.label_subject.setText("eye liner")
        self.label_subject.setStyleSheet('color: #737373')

        # eyeliner option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(13, 524, 536, 230))
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);")


        # 이동 버튼 (prev/next)
        self.pushButton_GoEyeshadowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyeshadowAR.setGeometry(QtCore.QRect(13, 484, 112, 30))
        self.pushButton_GoEyeshadowAR.setObjectName("pushButton_GoEyeshadowAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyeshadowAR.setFont(font)
        self.pushButton_GoEyeshadowAR.setText("< shadow")
        self.pushButton_GoEyeshadowAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoBlusherAR = QtWidgets.QPushButton(self)
        self.pushButton_GoBlusherAR.setGeometry(QtCore.QRect(437, 484, 112, 30))
        self.pushButton_GoBlusherAR.setObjectName("pushButton_GoBlusherAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoBlusherAR.setFont(font)
        self.pushButton_GoBlusherAR.setText("blusher >")
        self.pushButton_GoBlusherAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")

        ## 선택화면 안 요소..
        # 모양화면으로 back 버튼
        self.pushButton_GoBack = QtWidgets.QPushButton(self)
        self.pushButton_GoBack.setGeometry(QtCore.QRect(44, 537, 30, 30))
        self.pushButton_GoBack.setObjectName("pushButton_GoBack")
        self.pushButton_GoBack.setStyleSheet("border-image: url(image/btn_triangle.png);")
        self.pushButton_GoBack.clicked.connect(self.backClicked)
        self.pushButton_GoBack.hide()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(QtCore.QRect(105, 537, 352, 30))  # 73, 537, 332, 30
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changeValue)
        self.slider.setStyleSheet(
            'QSlider::groove:horizontal { border-radius: 1px; height: 5px;margin: 0px;background-color: rgb(52, 59, 72);}'
            'QSlider::groove:horizontal:hover {background-color: rgb(55, 62, 76);}'
            'QSlider::handle:horizontal {background-color: white;border: none;height: 16px;width: 16px;margin: -8px 0;border-radius: 8px;padding: -8px 0px;}'
            # 'QSlider::handle:horizontal:hover {background-color: rgb(188,170,231);}'
            'QSlider::handle:horizontal:pressed {background-color: white;}'
            'QSlider::add-page:qlineargradient {background: rgb(227,218,243);border-top-right-radius: 9px;border-bottom-right-radius: 9px;border-top-left-radius: 0px;border-bottom-left-radius: 0px;}'
            'QSlider::sub-page:qlineargradient {background: white;border-top-right-radius: 0px;border-bottom-right-radius: 0px;'
            'border-top-left-radius: 9px;border-bottom-left-radius: 9px;}')
        self.slider.hide()

        self.label_slider = QtWidgets.QLabel(self)
        self.label_slider.setGeometry(QtCore.QRect(467, 537, 72, 30))  # 415, 532, 60, 30
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(15)
        self.label_slider.setFont(font)
        self.label_slider.setAlignment(Qt.AlignCenter)
        self.label_slider.setText("0%")
        self.label_slider.setStyleSheet('color:white;')
        self.label_slider.hide()

        ##
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(13, 580, 536, 174)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet('background-color: transparent; border: 0px;')  # 테두리없앳당!!!!!! #background-color: transparent;

        self.stk_w2 = QStackedWidget(self)
        self.shape = Shape()
        self.color = Color()
        self.stk_w2.addWidget(self.shape)
        self.stk_w2.addWidget(self.color)
        self.scrollArea.setWidget(self.stk_w2)

        ## 모양 버튼 클릭
        self.shape.pushButton_ResetAll.clicked.connect(self.Apply_ResetAll)
        self.shape.pushButton_Middle.clicked.connect(self.Apply_Middle)
        self.shape.pushButton_Up.clicked.connect(self.Apply_Up)

        ## 색상 버튼 클릭
        self.color.pushButton_ResetColor.clicked.connect(self.Apply_ResetColor)
        self.color.pushButton_Black.clicked.connect(self.Apply_Black)
        self.color.pushButton_Brown.clicked.connect(self.Apply_Brown)

    def Apply_ResetAll(self):
        print("all reset clicked")
        self.shape.pushButton_ResetAll.setStyleSheet('background-color:black;color:white;')
        self.shape.pushButton_Middle.setStyleSheet('background-color:white;')
        self.shape.pushButton_Up.setStyleSheet('background-color:white;')

    def Apply_Middle(self):
        print("middle clicked")
        self.pushButton_GoBack.show()
        self.shape.pushButton_Middle.setStyleSheet('background-color:black;color:white;')
        self.shape.pushButton_ResetAll.setStyleSheet('background-color:white;')
        self.shape.pushButton_Up.setStyleSheet('background-color:white;')
        self.stk_w2.setCurrentWidget(self.color)

    def Apply_Up(self):
        print("up clicked")
        self.pushButton_GoBack.show()
        self.shape.pushButton_Up.setStyleSheet('background-color:black;color:white;')
        self.shape.pushButton_ResetAll.setStyleSheet('background-color:white;')
        self.shape.pushButton_Middle.setStyleSheet('background-color:white;')
        self.stk_w2.setCurrentWidget(self.color)

    def Apply_ResetColor(self):
        print("color reset clicked")
        self.color.pushButton_ResetColor.setStyleSheet('background-color:black;color:white;')
        self.color.pushButton_Black.setStyleSheet('background-color:white;')
        self.color.pushButton_Brown.setStyleSheet('background-color:white;')
        self.slider.hide()
        self.label_slider.hide()

    def Apply_Black(self):
        print("black clicked")
        self.color.pushButton_Black.setStyleSheet('background-color:black;color:white;')
        self.color.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.color.pushButton_Brown.setStyleSheet('background-color:white;')
        self.slider.setValue(50)  # 투명도 바 초기값으로 셋팅
        self.slider.show()
        self.label_slider.show()

    def Apply_Brown(self):
        print("brown clicked")
        self.color.pushButton_Brown.setStyleSheet('background-color:black;color:white;')
        self.color.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.color.pushButton_Black.setStyleSheet('background-color:white;')
        self.slider.setValue(50)  # 투명도 바 초기값으로 셋팅
        self.slider.show()
        self.label_slider.show()

    def changeValue(self):
        size = str(self.slider.value())
        self.label_slider.setText(size + "%")

    def backClicked(self):
        print("back clicked")
        self.slider.hide()
        self.label_slider.hide()
        self.pushButton_GoBack.hide()
        self.stk_w2.setCurrentWidget(self.shape)


