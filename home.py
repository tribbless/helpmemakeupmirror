from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
## <메모> 536 X 768 / 13 X 13
class Home(QWidget):

    def __init__(self):
        super(Home, self).__init__()


        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(97, 172, 342, 50))
        self.label_title.setObjectName("label_title")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setText("HELP ME MAKE UP MIRROR")



        ## go to main button
        self.pushButton_GoMainMenu = QtWidgets.QPushButton(self)
        self.pushButton_GoMainMenu.setGeometry(QtCore.QRect(97, 222, 342, 324))
        font = QtGui.QFont()
        font.setFamily("AlternateGothic2 BT")
        font.setPointSize(28)
        self.pushButton_GoMainMenu.setText("Face Detector \n\n CAPTURE YOUR FACE")
        self.pushButton_GoMainMenu.setFont(font)
        self.pushButton_GoMainMenu.setObjectName("pushButton_GoMainMenu")
        # ui test
        self.pushButton_GoMainMenu.setStyleSheet("/* Rectangle 16 */\n"
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



