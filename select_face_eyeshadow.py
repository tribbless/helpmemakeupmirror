from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Select_face_Eyeshadow(QWidget):

    def __init__(self):
        super(Select_face_Eyeshadow, self).__init__()

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
        self.label_subject.setText("eye shadow")
        self.label_subject.setStyleSheet('color: #737373')

        # eyeshadow option background image
        self.label_background_Option = QtWidgets.QLabel(self)
        self.label_background_Option.setGeometry(QtCore.QRect(13, 524, 536, 230))
        self.label_background_Option.setObjectName("label_background_Option")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_background_Option.setFont(font)
        self.label_background_Option.setAlignment(Qt.AlignCenter)
        self.label_background_Option.setText("eyeshadow option background image")
        #self.label_background_Option.setStyleSheet('background-color: #B5A4E7;')
        self.label_background_Option.setStyleSheet("border-image: url(image/background.png);")

        # 이동 버튼 (prev/next)
        self.pushButton_GoEyebrowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowAR.setGeometry(QtCore.QRect(13, 484, 112, 30))
        self.pushButton_GoEyebrowAR.setObjectName("pushButton_GoEyebrowAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyebrowAR.setFont(font)
        self.pushButton_GoEyebrowAR.setText("< eyebrow")
        self.pushButton_GoEyebrowAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')


        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(437, 484, 112, 30))
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("eyeliner >")
        self.pushButton_GoEyelinerAR.setStyleSheet('color: white; background-color:#B1B1B1; border:0px;')

        # 하단 로고
        self.label_HelpMe_Logo = QtWidgets.QLabel(self)
        self.label_HelpMe_Logo.setGeometry(QtCore.QRect(0, 754, 562, 40))
        self.label_HelpMe_Logo.setObjectName("label_HelpMe_Logo")
        self.label_HelpMe_Logo.setStyleSheet("border-image: url(image/logo_text.png);")





        '''

        ## eyebrow 선택 버튼
        self.pushButton_FirstOption = QtWidgets.QPushButton(self)
        self.pushButton_FirstOption.setGeometry(QtCore.QRect(5, 552, 168, 156))
        self.pushButton_FirstOption.setStyleSheet('background-color: transparent;')
        self.pushButton_FirstOption.setObjectName("pushButton_FirstOption")
        self.pushButton_FirstOption.clicked.connect(self.Apply_FirstOption)

        self.pushButton_TwoOption = QtWidgets.QPushButton(self)
        self.pushButton_TwoOption.setGeometry(QtCore.QRect(185, 552, 168, 156))
        self.pushButton_TwoOption.setStyleSheet('background-color: transparent;')
        self.pushButton_TwoOption.setObjectName("pushButton_TwoOption")
        self.pushButton_TwoOption.clicked.connect(self.Apply_TwoOption)

        self.pushButton_ThirdOption = QtWidgets.QPushButton(self)
        self.pushButton_ThirdOption.setGeometry(QtCore.QRect(363, 552, 168, 156))
        self.pushButton_ThirdOption.setStyleSheet('background-color: transparent;')
        self.pushButton_ThirdOption.setObjectName("pushButton_ThirdOption")
        self.pushButton_ThirdOption.clicked.connect(self.Apply_ThirdOption)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(QtCore.QRect(73, 507, 332, 30))
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changeValue)
        self.slider.setStyleSheet('QSlider::groove:horizontal { border-radius: 1px; height: 5px;margin: 0px;background-color: rgb(52, 59, 72);}'
                                  'QSlider::groove:horizontal:hover {background-color: rgb(55, 62, 76);}'
                                  'QSlider::handle:horizontal {background-color: white;border: none;height: 16px;width: 16px;margin: -8px 0;border-radius: 8px;padding: -8px 0px;}' 
                                  #'QSlider::handle:horizontal:hover {background-color: rgb(188,170,231);}'
                                  'QSlider::handle:horizontal:pressed {background-color: white;}'
                                  'QSlider::add-page:qlineargradient {background: rgb(227,218,243);border-top-right-radius: 9px;border-bottom-right-radius: 9px;border-top-left-radius: 0px;border-bottom-left-radius: 0px;}'
                                  'QSlider::sub-page:qlineargradient {background: white;border-top-right-radius: 0px;border-bottom-right-radius: 0px;'
                                  'border-top-left-radius: 9px;border-bottom-left-radius: 9px;}')

        self.label_slider =QtWidgets.QLabel(self)
        self.label_slider.setGeometry(QtCore.QRect(425, 502, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(15)
        self.label_slider.setFont(font)
        self.label_slider.setAlignment(Qt.AlignCenter)
        self.label_slider.setText("0%")
        self.label_slider.setStyleSheet('color:white;')

        ## 이동 버튼
        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(5, 725, 527, 56))
        self.pushButton_GoMenu.setStyleSheet('background-color: transparent;')
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")

        '''

    def Apply_FirstOption(self): ## 원상복구버튼
        self.slider.hide()
        self.label_slider.hide() # 투명도 바 숨기기
        print("first option clicked")
    def Apply_TwoOption(self):
        self.slider.setValue(0) # 투명도 바 초기값으로 셋팅
        self.slider.show()  # 투명도 바 나타내기
        self.label_slider.show()
        print("two option clicked")
    def Apply_ThirdOption(self):
        self.slider.setValue(0) # 투명도 바 초기값으로 셋팅
        self.slider.show()  # 투명도 바 나타내기
        self.label_slider.show()
        print("third option clicked")

    def changeValue(self):
        size = str(self.slider.value())
        self.label_slider.setText(size+"%")