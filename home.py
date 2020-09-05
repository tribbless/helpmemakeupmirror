from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Home(QWidget):

    def __init__(self):
        super(Home, self).__init__()

        ## 어떤화면인지 알리기 위한 label (나중에 삭제)
        self.label_home = QtWidgets.QLabel(self)
        self.label_home.setGeometry(QtCore.QRect(10, 10, 171, 61))
        self.label_home.setObjectName("label_home")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_home.setFont(font)
        self.label_home.setText("home화면")

        ## go to main button
        self.pushButton_GoFaceCatprue = QtWidgets.QPushButton(self)
        self.pushButton_GoFaceCatprue.setGeometry(QtCore.QRect(140, 230, 271, 261))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(28)
        self.pushButton_GoFaceCatprue.setText("Face Detector \n\n CAPTURE YOUR FACE")
        self.pushButton_GoFaceCatprue.setFont(font)
        self.pushButton_GoFaceCatprue.setObjectName("pushButton_GoFaceCatprue")
        # ui test
        self.pushButton_GoFaceCatprue.setStyleSheet("/* Rectangle 16 */\n"
                                                    "position: absolute;\n"
                                                    "width: 665.67px;\n"
                                                    "height: 632.68px;\n"
                                                    "\n"
                                                    "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                    "  stop: 0 #B5A4E7, \n"
                                                    "  stop: 1.0 #F3C3D6);\n"
                                                    "\n"
                                                    "/* CAPTURE YOUR FACE */\n"
                                                    "position: absolute;\n"
                                                    "top:50%;\n"
                                                    "left:50%;\n"
                                                    "width: 396px;\n"
                                                    "height: 80px;\n"
                                                    "\n"
                                                    "font-family: Consolas;\n"
                                                    "font-style: normal;\n"
                                                    "font-weight: 700;\n"
                                                    "font-size: 20px;\n"
                                                    "line-height: 22px;\n"
                                                    "\n"
                                                    "color: #FFFFFF;\n"
                                                    "border: 1px solid #FFFFFF;")

        '''
                hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label_2)
        hbox.addStretch(1)
        hbox.addWidget(self.pushButton_4)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        
        self.label_2.setMaximumSize(301,81)
        
        self.pushButton_4.setStyleSheet('QPushButton{background-color: rgba(0, 0, 0, 0.0)}')
        
        
        
        '''
