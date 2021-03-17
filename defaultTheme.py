""" Sortieren werte komplette Stylesheets
hier fertige Stylesheets

flexible werte oben
styhlesheets, die von werten abhängen unten"""


class Farbschema:
    def __init__(self):
        # bei allen
        self.backgroundcolor = "rgb(217, 198, 255);"

        self.frameBackground = ("background-color: rgba(255, 255, 255, 0);")

        # self.defaultStyle

        # Button styles Color
        self.buttonAktiv = "rgb(255, 35, 152)"
        self.buttonPassiv = "rgb(186, 26, 111)"
        self.buttonNormal = "rgb(184, 101, 162)"
        self.buttonFokus = "rgb(177, 90, 173)"

        #
        # prepare screen
        self.preRadiusButton = "15px"
        self.preRadiusEingabe = "10px"
        self.spinBoxColor = "rgb(208, 255, 246)"
        self.eingabeColor = "rgb(162, 255, 216)"
        self.lineEdit = "rgb(182, 166, 214)"
        self.labelColor = "color: rgb(0, 0, 0);"
        self.chooseColor = "rgb(225, 124, 200)"

        # self.subtitel = ("color: rgb(123, 132, 255);")
        # self.titelschriftfarbe = ("color: rgb(105, 163, 255);")

        # Spiel
        self.blau = "rgb(125, 177, 255)"
        self.rot = "rgb(255, 165, 138)"
        self.green = "rgb(169, 255, 149)"
        self.gelb = "rgb(238, 226, 137)"
        self.black = "rgb(72, 71, 72)"

        self.P_COLORS = ["rgb(150, 129, 212)", "rgb(61, 198, 213)", "rgb(67, 190, 40)", "rgb(59, 216, 230)",
                         "rgb(230, 198, 30)",
                         "rgb(230, 37, 170)"]

        # Border
        self.borderNormal = "rgb(255, 255, 255)"
        self.borderPlay = "rgb(211, 112, 218)"
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
        self.UNOLabel = ("color: rgb(105, 163, 255);")
        self.DescriptionLabel = ("color: rgb(123, 132, 255);")
        self.StartButton = ("QPushButton {\n"
                            f"    border-radius: {self.preRadiusButton};\n"
                            f"    background-color: {self.buttonAktiv};\n"
                            "}")
        self.infoLabel = ("color: rgb(152, 166, 202);")

        # Prepare
        self.AnzahlLabel = (f"color: {self.labelColor}")
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
                              f"    border-radius: {self.preRadiusButton};\n"
                              f"    background-color: {self.buttonPassiv};\n"
                              "}")
        # = startButton
        self.weiterBAktiv = ("QPushButton {\n"
                             f"    border-radius: {self.preRadiusButton};\n"
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
                          f"    border-radius: {self.endRadius}\n"
                          "}")
        self.UNOButtonclicked = ("QPushButton {\n"
                                 f"    background-color: {self.buttonPassiv};\n"
                                 f"    border-radius: {self.endRadius}\n"
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
        self.PlayButton = (("QPushButton {\n"
                            f"    background-color: {self.buttonFokus};\n"
                            f"    border-radius: {self.endRadius}\n"
                            "}"))
        self.menuQuitButton = ("QPushButton {\n"
                               f"    background-color: {self.buttonNormal};\n"
                               f"    border-radius: {self.endRadius}\n"
                               "}")


default = Farbschema()


