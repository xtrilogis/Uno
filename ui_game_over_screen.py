# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_game_over_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MWinEnde(object):
    def setupUi(self, MWinEnde):
        MWinEnde.setObjectName("MWinEnde")
        MWinEnde.resize(1000, 650)
        self.centralwidget = QtWidgets.QWidget(MWinEnde)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_Background = QtWidgets.QFrame(self.centralwidget)
        self.frame_Background.setStyleSheet("QFrame {\n"
"    background-color: rgb(217, 198, 255);\n"
"}\n"
"")
        self.frame_Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Background.setObjectName("frame_Background")
        self.frame_gameOverMenu = QtWidgets.QFrame(self.frame_Background)
        self.frame_gameOverMenu.setGeometry(QtCore.QRect(0, 310, 981, 68))
        self.frame_gameOverMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gameOverMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gameOverMenu.setObjectName("frame_gameOverMenu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_gameOverMenu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_PlayAgain = QtWidgets.QPushButton(self.frame_gameOverMenu)
        self.pushButton_PlayAgain.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(20)
        self.pushButton_PlayAgain.setFont(font)
        self.pushButton_PlayAgain.setStyleSheet("QPushButton {\n"
"    background-color: rgb(225, 124, 200);\n"
"    border-radius: 25px\n"
"}")
        self.pushButton_PlayAgain.setObjectName("pushButton_PlayAgain")
        self.horizontalLayout.addWidget(self.pushButton_PlayAgain)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_Menu = QtWidgets.QPushButton(self.frame_gameOverMenu)
        self.pushButton_Menu.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        self.pushButton_Menu.setFont(font)
        self.pushButton_Menu.setStyleSheet("QPushButton {\n"
"    background-color: rgb(184, 101, 162);\n"
"    border-radius: 25px\n"
"}")
        self.pushButton_Menu.setObjectName("pushButton_Menu")
        self.horizontalLayout.addWidget(self.pushButton_Menu)
        spacerItem2 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_Quit = QtWidgets.QPushButton(self.frame_gameOverMenu)
        self.pushButton_Quit.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        self.pushButton_Quit.setFont(font)
        self.pushButton_Quit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(184, 101, 162);\n"
"    border-radius: 25px\n"
"}")
        self.pushButton_Quit.setObjectName("pushButton_Quit")
        self.horizontalLayout.addWidget(self.pushButton_Quit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_gameOverMessage = QtWidgets.QLabel(self.frame_Background)
        self.label_gameOverMessage.setGeometry(QtCore.QRect(0, 150, 1000, 51))
        self.label_gameOverMessage.setMinimumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(28)
        self.label_gameOverMessage.setFont(font)
        self.label_gameOverMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gameOverMessage.setObjectName("label_gameOverMessage")
        self.label_Victor = QtWidgets.QLabel(self.frame_Background)
        self.label_Victor.setGeometry(QtCore.QRect(0, 220, 1000, 50))
        self.label_Victor.setMinimumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(24)
        self.label_Victor.setFont(font)
        self.label_Victor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Victor.setObjectName("label_Victor")
        self.verticalLayout.addWidget(self.frame_Background)
        MWinEnde.setCentralWidget(self.centralwidget)

        self.retranslateUi(MWinEnde)
        QtCore.QMetaObject.connectSlotsByName(MWinEnde)

    def retranslateUi(self, MWinEnde):
        _translate = QtCore.QCoreApplication.translate
        MWinEnde.setWindowTitle(_translate("MWinEnde", "asdf"))
        self.pushButton_PlayAgain.setText(_translate("MWinEnde", "Noch Mal"))
        self.pushButton_Menu.setText(_translate("MWinEnde", "Start"))
        self.pushButton_Quit.setText(_translate("MWinEnde", "Beenden"))
        self.label_gameOverMessage.setText(_translate("MWinEnde", "Spiel beendet"))
        self.label_Victor.setText(_translate("MWinEnde", "<strong>Spieler</strong> hat gewonnen"))
