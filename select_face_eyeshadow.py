from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#모양버튼
#색깔버튼
#합쳐서 4가지 버튼해야하나..흠.. 아니면 모양선택-> 색깔선택 후 완료버튼을 누르는겨..
#둘다 선택안햇으면 메시지박스로 선택하라고 안내메시지 주는겨..

#모양과 색깔을 선택하면 그 정보+얼굴 사진을 눈썹.py에 있는 class(?)에게 주는겨
#class는 return 이미지 주는겨~~~~~


class Select_face_Eyeshadow(QWidget):

    def __init__(self):
        super(Select_face_Eyeshadow, self).__init__()

        self.label_eyeshadowAR = QtWidgets.QLabel(self)
        self.label_eyeshadowAR.setGeometry(QtCore.QRect(140, 10, 261, 40))
        self.label_eyeshadowAR.setObjectName("label_eyeshadowAR")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_eyeshadowAR.setFont(font)
        self.label_eyeshadowAR.setAlignment(Qt.AlignCenter)
        self.label_eyeshadowAR.setText("face_eyeshadow")

        #얼굴사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(120, 70, 300, 400))
        self.label_face.setObjectName("label_eyebrowAR")
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 이미지
        self.label_select = QtWidgets.QLabel(self)
        self.label_select.setObjectName("label_select")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.label_select.setPalette(palette)
        font = QtGui.QFont("Times", 15)
        self.label_select.setFont(font)
        self.label_select.setStyleSheet("border-image: url(image/selectAR.png);")
        #self.label_select.setText("30%")
        self.label_select.setGeometry(QtCore.QRect(5, 490, 526, 280))

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


        self.pushButton_GoEyelinerAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyelinerAR.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyelinerAR.setFont(font)
        self.pushButton_GoEyelinerAR.setText("NEXT")
        self.pushButton_GoEyelinerAR.setObjectName("pushButton_GoEyelinerAR")

        self.pushButton_GoEyebrowAR = QtWidgets.QPushButton(self)
        self.pushButton_GoEyebrowAR.setGeometry(QtCore.QRect(10, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoEyebrowAR.setFont(font)
        self.pushButton_GoEyebrowAR.setText("BACK")
        self.pushButton_GoEyebrowAR.setObjectName("pushButton_GoEyebrowAR")

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