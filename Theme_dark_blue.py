class Farbschema:
    def __init__(self):
        # bei allen
        self.backgroundcolor = "qlineargradient(spread:pad, x1:0.0797727, y1:0.914, x2:0.914773, y2:0.08, stop:0.0568182 rgba(28, 40, 54, 255), stop:0.960227 rgba(63, 88, 119, 255))"

        self.frameBackground = "background-color: rgba(255, 255, 255, 0);"

        # self.defaultStyle

        # Button styles Color
        self.buttonAktiv = "rgb(247, 94, 0)"
        self.buttonPassiv = "rgb(158, 89, 48)"
        self.buttonNormal = "rgb(217, 91, 19)"
        self.buttonFokus = "rgb(245, 125, 5)"

        #
        # prepare screen
        self.preRadiusButton = "17px"
        self.preRadiusStart = "20px"
        self.preRadiusEingabe = "10px"

        self.spinBoxColor = "rgb(208, 255, 246)"
        self.eingabeColor = "rgb(135, 230, 195)"
        self.lineEdit = "rgb(158, 176, 218)"
        self.labelColor = "rgb(192, 209, 255)"
        self.chooseColor = "rgb(135, 186, 167)"

        # ###
        self.subtitel = "rgb(74, 105, 138);"
        self.titel = "rgb(99, 140, 186)"
        self.info = "rgb(152, 166, 202)"

        # Spiel
        self.blau = "rgb(96, 130, 226)"
        self.rot = "rgb(202, 77, 77)"
        self.green = " rgb(43, 191, 43)"
        self.gelb = "rgb(217, 191, 62)"
        self.black = "rgb(72, 71, 72)"

        self.P_COLORS = ["rgb(150, 129, 212)", "rgb(61, 198, 213)", "rgb(67, 190, 40)", "rgb(59, 216, 230)",
                         "rgb(230, 198, 30)",
                         "rgb(230, 37, 170)"]

        # Border
        self.borderNormal = "rgb(172, 187, 191)"
        self.borderPlay = "rgb(150, 255, 215)"
        # Ende
        self.endRadius = "25px"

        # ##########################################
        # Stylesheets
        self.backgroundstyle = ("QFrame {\n"
                                f"    background-color: {self.backgroundcolor};\n"
                                "    border-radius: 15px;\n"
                                "}")

        self.backgroundstyleSpiel = ("QFrame {\n"
                                     f"    background-color: {self.backgroundcolor};\n"
                                     
                                     "}")

        # Start
        # ###
        self.UNOLabel = ("background-color: rgba(255, 255, 255, 0);\n"
                         f"color: {self.titel};")
        self.DescriptionLabel = ("background-color: rgba(255, 255, 255, 0);\n"
                                 f"color: {self.subtitel};")
        self.StartButton = ("QPushButton {\n"
                            f"    border-radius: {self.preRadiusStart};\n"
                            f"    background-color: {self.buttonAktiv};\n"
                            "}")
        self.infoLabel = (f"color: {self.info};")

        # Prepare
        self.AnzahlLabel = (f"    background-color: rgba(255, 255, 255, 0);\n"
                            f"color: {self.labelColor}")
        self.PulsMinus = ("QPushButton {\n"
                          f"    border-radius: {self.preRadiusEingabe};\n"
                          f"    background-color: {self.eingabeColor};\n"
                          "}")
        self.spinBox = ("QSpinBox {\n"
                        f"    border-radius: {self.preRadiusEingabe};\n"
                        f"    background-color: {self.spinBoxColor};\n"
                        "}\n")

        self.NameLabel = (f"color: {self.labelColor}")
        self.NameEingabe = ("QLineEdit {\n"
                            f"    border-radius: {self.preRadiusEingabe};\n"
                            f"    background-color: {self.lineEdit};\n"
                            "}")
        self.colorButton = ("QPushButton {\n"
                            f"    background-color: {self.chooseColor};\n"
                            f"    border-radius: {self.preRadiusEingabe};\n"
                            "}")
        self.okButton = ("QPushButton {\n"
                         f"    background-color: {self.eingabeColor};\n"
                         "    border-width: 1px;\n"
                         "    border-style: solid;\n"
                         "    border-color:  rgb(98, 98, 98);\n"
                         "}\n")

        self.weiterBPassiv = ("QPushButton {\n"
                              f"    border-radius: {self.preRadiusStart};\n"
                              f"    background-color: {self.buttonPassiv};\n"
                              "}")
        # = startButton
        self.weiterBAktiv = ("QPushButton {\n"
                             f"    border-radius: {self.preRadiusStart};\n"
                             f"    background-color: {self.buttonAktiv};\n"
                             "}")
        self.theme_Reset = ("QPushButton {\n"
                            f"    border-radius: {self.preRadiusButton};\n"
                            f"    background-color: {self.buttonNormal};\n"
                            "}")

        # Spiel
        self.aktuellerSp = (f"color: {self.labelColor}")
        self.UNOButton = ("QPushButton {\n"
                          f"    background-color: {self.buttonFokus};\n"
                          f"    border-radius: {self.preRadiusEingabe}\n"
                          "}")
        self.UNOButtonclicked = ("QPushButton {\n"
                                 f"    background-color: {self.buttonPassiv};\n"
                                 f"    border-radius: {self.preRadiusEingabe}\n"
                                 "}")
        # self.passen = self.UNOButton
        self.hasToDraw = ("QPushButton {\n"
                          f"    background-color: {self.black};\n"
                          "    border-radius: 15px;\n"
                          "    border-width: 3px; \n"
                          "    border-style: solid;\n"
                          f"    border-color: {self.borderPlay};"
                          "image: url(D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten"
                          "/default.png);\\n\n "
                          "}")
        self.drawTalon = ("QPushButton {\n"
                          "    background-color: rgb(72, 71, 72);\n"
                          "border-radius: 15px;\n"
                          "image: url(D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/default.png);\\n\n "
                          "}")

        self.blueChoice = ("QPushButton {\n"
                           f"    background-color: {self.blau};\n"
                           "    border-top-left-radius : 5px;\n"
                           "    border-top-right-radius : 0px; \n"
                           "    border-bottom-left-radius : 0px; \n"
                           "    border-bottom-right-radius : 5px\n"
                           "}\n")
        self.greenChoice = ("QPushButton {\n"
                            f"    background-color: {self.green};\n"
                            "    border-top-left-radius : 5px;\n"
                            "    border-top-right-radius : 0px; \n"
                            "    border-bottom-left-radius : 0px; \n"
                            "    border-bottom-right-radius : 5px\n"
                            "}\n")
        self.gelbChoice = ("QPushButton {\n"
                           f"    background-color: {self.gelb};\n"
                           "    border-top-left-radius : 5px;\n"
                           "    border-top-right-radius : 0px; \n"
                           "    border-bottom-left-radius : 0px; \n"
                           "    border-bottom-right-radius : 5px\n"
                           "}\n")
        self.rotChoice = ("QPushButton {\n"
                          f"    background-color: {self.rot};\n"
                          "    border-top-left-radius : 5px;\n"
                          "    border-top-right-radius : 0px; \n"
                          "    border-bottom-left-radius : 0px; \n"
                          "    border-bottom-right-radius : 5px\n"
                          "}\n")

        # Karten

        # Ende
        self.gewinnerLabel = self.UNOLabel
        self.PlayButton = ("QPushButton {\n"
                           f"    background-color: {self.buttonFokus};\n"
                           f"    border-radius: {self.endRadius}\n"
                           "}")
        self.menuQuitButton = ("QPushButton {\n"
                               f"    background-color: {self.buttonNormal};\n"
                               f"    border-radius: {self.endRadius}\n"
                               "}")


dark_blue = Farbschema()
