from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Frame_Eyeshadow(QWidget):

    def __init__(self):
        super(Frame_Eyeshadow, self).__init__()

        self.label_frameEyeshadow = QtWidgets.QLabel(self)
        self.label_frameEyeshadow.setGeometry(QtCore.QRect(130, 10, 271, 40))
        self.label_frameEyeshadow.setObjectName("label_frameEyeshadow")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_frameEyeshadow.setFont(font)
        self.label_frameEyeshadow.setAlignment(Qt.AlignCenter)
        self.label_frameEyeshadow.setText("frame_eyeshadow")

        #얼굴사진
        self.label_face = QtWidgets.QLabel(self)
        self.label_face.setGeometry(QtCore.QRect(105, 70, 330, 440))
        self.label_face.setObjectName("label_face")
        self.label_face.setText("FACE IMAGE")
        self.label_face.setAlignment(Qt.AlignCenter)
        self.label_face.setStyleSheet('background-color:white;')

        # 이미지
        self.label_manual_background = QtWidgets.QLabel(self)
        self.label_manual_background.setObjectName("label_manual_background")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.label_manual_background.setPalette(palette)
        font = QtGui.QFont("Times", 15)
        self.label_manual_background.setFont(font)
        self.label_manual_background.setStyleSheet("border-image: url(image/frameBack.png);")
        self.label_manual_background.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.")
        self.label_manual_background.setGeometry(QtCore.QRect(5, 540, 526, 235))

        '''  이미지에 맞게 label사이즈 및 위치 조절해야함~~~   : 설명쓰는 공간~~
        self.label_manual = QtWidgets.QLabel(self)
        self.label_manual.setGeometry(QtCore.QRect(40, 540, 451, 161))
        self.label_manual.setObjectName("label_manual")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_manual.setFont(font)
        self.label_manual.setStyleSheet('background-color: transparent')
        self.label_manual.setText("긴 얼굴형에는 가로로 어쩌꾸 저쩌구를 한다.\n어쩌구저쩌구\n룰루랄라 ^^이렇게 하면 됩니다 ^^")
        '''

        ## 이동 버튼
        self.pushButton_GoMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMenu.setGeometry(QtCore.QRect(5, 721, 527, 43))
        self.pushButton_GoMenu.setStyleSheet('background-color: transparent;')
        self.pushButton_GoMenu.setObjectName("pushButton_GoMenu")

        self.pushButton_GoFrameEyeliner = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameEyeliner.setGeometry(QtCore.QRect(401, 10, 130, 40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameEyeliner.setFont(font)
        self.pushButton_GoFrameEyeliner.setText("eye liner")
        self.pushButton_GoFrameEyeliner.setObjectName("pushButton_GoFrameEyeliner")
        self.pushButton_GoFrameEyeliner.setStyleSheet("background:rgb(144,144,144);");

        self.pushButton_GoFrameEyebrow = QtWidgets.QPushButton(self)
        self.pushButton_GoFrameEyebrow.setGeometry(QtCore.QRect(0, 10, 130,40))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(20)
        self.pushButton_GoFrameEyebrow.setFont(font)
        self.pushButton_GoFrameEyebrow.setText("eyebrow")
        self.pushButton_GoFrameEyebrow.setObjectName("pushButton_GoFrameEyebrow")
        self.pushButton_GoFrameEyebrow.setStyleSheet("background:rgb(144,144,144);");