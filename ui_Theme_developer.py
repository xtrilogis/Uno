
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        """
        self.frameBackground.setStyleSheet("QFrame {\n"
"    background-color: rgb(17, 198, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.labelDescription.setStyleSheet("color: rgb(123, 132, 255);")

        self.labelUNO.setStyleSheet("\n"
"color: rgb(105, 163, 255);")

        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(162, 255, 216);\n"
"}")

        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(162, 255, 216);\n"
"}")
                self.spinBoxNumber.setStyleSheet("QSpinBox {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(208, 255, 246);\n"
"}\n"
"")
"""

    def setupUi(self, MainWindow):

        self.pushButtonColorTheme.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(184, 101, 162);\n"
"}")

        self.pushButtonReset.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(184, 101, 162);\n"
"}")





        self.lineEditSpieler1.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(182, 166, 214);\n"
"}")

        self.pushButtonSetColor.setStyleSheet("QPushButton {\n"
"    background-color: rgb(225, 124, 200);\n"
"    border-radius: 10px;\n"
"}")

        self.pushButton_SpielerEnter.setStyleSheet("QPushButton {\n"
"    background-color: rgb(225, 124, 200);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:  rgb(98, 98, 98);\n"
"}\n"
"")


        self.pushButtonClose.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-radius: 1px;\n"
"    image: url(D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/x.png);\n"
"}\n"
"")


        self.pushButtonStart.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 35, 152);\n"
"}")

        self.pushButtonWeiter.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(186, 26, 111);\n"
"}")

        self.pushButtonUNO.setStyleSheet("QPushButton {\n"
"    background-color:rgb(177, 90, 173);\n"
"    border-radius: 10px;\n"
"}")


        self.LabelSpielername.setStyleSheet("")

        self.frame_Stapel.setStyleSheet("")


        #self.pushButtonDraw_T.setStyleSheet("QPushButton {\n"
#"    background-color: rgb(72, 71, 72);\n"
#"    border-radius: 15px;\n"
#"    image: url(D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/default.png);\\n\n"
#"}")

        # self.pushButton_Play_T.setStyleSheet("QPushButton {\n"
#"    background-color: rgb(195, 190, 195);\n"
#"    border-radius: 15px;\n"
#"}")


        self.frame_Handkarten.setStyleSheet("QFrame {\n"
"    border: 5px solid  rgb(150, 129, 212);\n"
"}")

        self.pushButton_Play_T_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(125, 177, 255);\n"
"    border-radius: 15px;\n"
"    border-width: 4px;\n"
"    border-style: solid;\n"
"    border-color: rgb(211, 112, 218);\n"
"}\n"
"")

        self.pushButton_Play_T_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(169, 255, 149);\n"
"    border-radius: 15px;\n"
"    border-width: 4px;\n"
"    border-style: solid;\n"
"    border-color: rgb(211, 112, 218);\n"
"}")

        self.pushButton_Play_T_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 226, 137);\n"
"    border-radius: 15px;\n"
"    border-width: 4px;\n"
"    border-style: solid;\n"
"    border-color: rgb(211, 112, 218); \n"
"}")

        self.pushButton_Play_T_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 138);\n"
"    border-radius: 15px;\n"
"    border-width: 4px;\n"
"    border-style: solid;\n"
"    border-color: rgb(211, 112, 218);\n"
"}")


        self.pushButton_Play_T_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(125, 177, 255);\n"
"    border-radius: 15px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.pushButton_Play_T_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(169, 255, 149);\n"
"    border-radius: 15px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")

        self.pushButton_Play_T_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 226, 137);\n"
"    border-radius: 15px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")

        self.pushButton_Play_T_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 138);\n"
"    border-radius: 15px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")


        self.pushButtonWeiter_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(177, 90, 173);\n"
"    border-radius: 5px;\n"
"}")


        self.pushButtonBlau.setStyleSheet("QPushButton {\n"
"    background-color: rgb(125, 177, 255);\n"
"    border-top-left-radius : 5px;\n"
"    border-top-right-radius : 0px; \n"
"    border-bottom-left-radius : 0px; \n"
"    border-bottom-right-radius : 5px\n"
"}")

        self.pushButtonGruen.setStyleSheet("QPushButton {\n"
"    background-color: rgb(169, 255, 149);\n"
"    border-top-left-radius : 5px;\n"
"    border-top-right-radius : 0px; \n"
"    border-bottom-left-radius : 0px; \n"
"    border-bottom-right-radius : 5px\n"
"}\n"
"")

        self.pushButtonGelb.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 226, 137);\n"
"    border-top-left-radius : 5px;\n"
"    border-top-right-radius : 0px; \n"
"    border-bottom-left-radius : 0px; \n"
"    border-bottom-right-radius : 5px\n"
"}\n"
"")

        self.pushButtoRot.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 165, 138);\n"
"    border-top-left-radius : 5px;\n"
"    border-top-right-radius : 0px; \n"
"    border-bottom-left-radius : 0px; \n"
"    border-bottom-right-radius : 5px\n"
"}\n"
"")


        self.pushButtonPlayAgain.setStyleSheet("QPushButton {\n"
"    background-color: rgb(225, 124, 200);\n"
"    border-radius: 25px\n"
"}")

        self.pushButtonMenu.setStyleSheet("QPushButton {\n"
"    background-color: rgb(184, 101, 162);\n"
"    border-radius: 25px\n"
"}")

        self.pushButtonQuit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(184, 101, 162);\n"
"    border-radius: 25px\n"
"}")
