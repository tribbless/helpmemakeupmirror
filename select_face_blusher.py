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

        self.pushButton_Round = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Round.setMinimumSize(172, 150)
        self.pushButton_Round.setText("round")
        self.pushButton_Round.setFont(font)
        self.pushButton_Round.setStyleSheet('background-color:white;')
        self.pushButton_Round.setObjectName("pushButton_Round")

        self.pushButton_Oblong = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Oblong.setMinimumSize(172, 150)
        self.pushButton_Oblong.setText("oblong")
        self.pushButton_Oblong.setFont(font)
        self.pushButton_Oblong.setStyleSheet('background-color:white;')
        self.pushButton_Oblong.setObjectName("pushButton_Oblong")

        self.pushButton_Square = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Square.setMinimumSize(172, 150)
        self.pushButton_Square.setText("square")
        self.pushButton_Square.setFont(font)
        self.pushButton_Square.setStyleSheet('background-color:white;')
        self.pushButton_Square.setObjectName("pushButton_Square")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetAll)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Round)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Oblong)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Square)

        self.setLayout(layout)

class Color(QWidget):
    def __init__(self):
        super().__init__()



        self.pushButton_ResetColor = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        #self.pushButton_ResetColor.setMinimumSize(172, 150)
        self.pushButton_ResetColor.setMaximumSize(172, 150)
        self.pushButton_ResetColor.setText("color reset")
        self.pushButton_ResetColor.setFont(font)
        self.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.pushButton_ResetColor.setObjectName("pushButton_ResetColor")

        self.pushButton_Pink = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        #self.pushButton_Pink.setMinimumSize(172, 150)
        self.pushButton_Pink.setMaximumSize(172, 150)
        self.pushButton_Pink.setText("pink")
        self.pushButton_Pink.setFont(font)
        self.pushButton_Pink.setStyleSheet('background-color:white;')
        self.pushButton_Pink.setObjectName("pushButton_Pink")

        self.pushButton_Orange = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        #self.pushButton_Orange.setMinimumSize(172, 150)
        self.pushButton_Orange.setMaximumSize(172, 150)
        self.pushButton_Orange.setText("orange")
        self.pushButton_Orange.setFont(font)
        self.pushButton_Orange.setStyleSheet('background-color:white;')
        self.pushButton_Orange.setObjectName("pushButton_Orange")


        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.pushButton_ResetColor)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Pink)
        layout.setSpacing(10)
        layout.addWidget(self.pushButton_Orange)


        self.setLayout(layout)


class Select_face_Blusher(QWidget):

    def __init__(self):
        super(Select_face_Blusher, self).__init__()

        # 얼굴 사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(125, 57, 312, 416)) #125, 36, 312, 416
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
        self.label_subject.setText("blusher")
        self.label_subject.setStyleSheet('color: #737373')

        # blusher option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(13, 524, 536, 230)) #13, 503, 536, 230
        self.label_background_Option.setObjectName("label_background_Option")
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);")


        # 이동 버튼 (prev/next)
        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(13, 484, 112, 30))
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("< eyeliner")
        self.pushButton_GoEyelinerAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoLipAR = QtWidgets.QPushButton(self)
        self.pushButton_GoLipAR.setGeometry(QtCore.QRect(437, 484, 112, 30)) #437, 463, 112, 30
        self.pushButton_GoLipAR.setObjectName("pushButton_GoLipAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoLipAR.setFont(font)
        self.pushButton_GoLipAR.setText("lip >")
        self.pushButton_GoLipAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))  ## 0, 733, 562, 61  ++ 21
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
        self.scrollArea.setStyleSheet('background-color: transparent; border: 0px;')

        self.stk_w2 = QStackedWidget(self)
        self.shape = Shape()
        self.color = Color()
        self.stk_w2.addWidget(self.shape)
        self.stk_w2.addWidget(self.color)

        self.scrollArea.setWidget(self.stk_w2)


        ## 모양 버튼 클릭
        self.shape.pushButton_ResetAll.clicked.connect(self.Apply_ResetAll)
        self.shape.pushButton_Round.clicked.connect(self.Apply_Round)
        self.shape.pushButton_Oblong.clicked.connect(self.Apply_Oblong)
        self.shape.pushButton_Square.clicked.connect(self.Apply_Square)

        ## 색상 버튼 클릭
        self.color.pushButton_ResetColor.clicked.connect(self.Apply_ResetColor)
        self.color.pushButton_Pink.clicked.connect(self.Apply_Pink)
        self.color.pushButton_Orange.clicked.connect(self.Apply_Orange)

    def Apply_ResetAll(self):
        print("all reset clicked")
        self.shape.pushButton_ResetAll.setStyleSheet('background-color:black;color:white;')
        self.shape.pushButton_Round.setStyleSheet('background-color:white;')
        self.shape.pushButton_Oblong.setStyleSheet('background-color:white;')
        self.shape.pushButton_Square.setStyleSheet('background-color:white;')
        #print(self.shape.height())
        #print(self.shape.width())
        #print(self.color.height())
        #print(self.color.width())
        #print(self.stk_w2.height()) #150
        #print(self.stk_w2.width()) #718
        #print(self.shape.pushButton_ResetAll.height())
        #print(self.shape.pushButton_ResetAll.width())

    def Apply_Round(self):
        print("round clicked")
        self.pushButton_GoBack.show()
        self.shape.pushButton_Round.setStyleSheet('background-color:black;color:white;')
        self.shape.pushButton_ResetAll.setStyleSheet('background-color:white;')
        self.shape.pushButton_Oblong.setStyleSheet('background-color:white;')
        self.shape.pushButton_Square.setStyleSheet('background-color:white;')
        self.goToColor()

    def Apply_Oblong(self):
        print("oblong clicked")
        self.pushButton_GoBack.show()
        self.shape.pushButton_Oblong.setStyleSheet('background-color:black;color:white;')
        self.shape.pushButton_ResetAll.setStyleSheet('background-color:white;')
        self.shape.pushButton_Round.setStyleSheet('background-color:white;')
        self.shape.pushButton_Square.setStyleSheet('background-color:white;')
        self.goToColor()

    def Apply_Square(self):
        print("oblong clicked")
        self.pushButton_GoBack.show()
        self.shape.pushButton_Square.setStyleSheet('background-color:black;color:white;')
        self.shape.pushButton_ResetAll.setStyleSheet('background-color:white;')
        self.shape.pushButton_Round.setStyleSheet('background-color:white;')
        self.shape.pushButton_Oblong.setStyleSheet('background-color:white;')
        self.goToColor()

    def Apply_ResetColor(self):
        print("color reset clicked")
        #print(self.color.pushButton_ResetColor.height())
        #print(self.color.pushButton_ResetColor.width())
        self.color.pushButton_ResetColor.setStyleSheet('background-color:black;color:white;')
        self.color.pushButton_Pink.setStyleSheet('background-color:white;')
        self.color.pushButton_Orange.setStyleSheet('background-color:white;')
        self.slider.hide()
        self.label_slider.hide()

    def Apply_Pink(self):
        print("pink clicked")
        self.color.pushButton_Pink.setStyleSheet('background-color:black;color:white;')
        self.color.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.color.pushButton_Orange.setStyleSheet('background-color:white;')
        self.slider.setValue(50)  # 투명도 바 초기값으로 셋팅
        self.slider.show()
        self.label_slider.show()

    def Apply_Orange(self):
        print("Orange clicked")
        self.color.pushButton_Orange.setStyleSheet('background-color:black;color:white;')
        self.color.pushButton_ResetColor.setStyleSheet('background-color:white;')
        self.color.pushButton_Pink.setStyleSheet('background-color:white;')
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
        self.stk_w2.setMaximumWidth(718)
        self.stk_w2.setCurrentWidget(self.shape)

    def goToColor(self):
        self.stk_w2.setMaximumWidth(536)
        self.stk_w2.setCurrentWidget(self.color)





