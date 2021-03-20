from Theme_template import ColorTheme

dark_blue = ColorTheme()
dark_blue.backgroundColor = "qlineargradient(spread:pad, x1:0.0797727, y1:0.914, x2:0.914773, y2:0.08, " \
                            "stop:0.0568182 rgba(28, 40, 54, 255), stop:0.960227 rgba(63, 88, 119, 255)) "

# ## COLORS ## #
# Basics
dark_blue.buttonColorBasic = "rgb(217, 91, 19)"
dark_blue.buttonColorActive = "rgb(247, 94, 0)"
dark_blue.buttonColorPassive = "rgb(158, 89, 48)"
dark_blue.buttonColorFocus = "rgb(245, 125, 5)"

# First 'Screen'
dark_blue.titelColor = "rgb(99, 140, 186)"
dark_blue.subtitelColor = "rgb(74, 105, 138);"
dark_blue.infoLabelColor = "rgb(152, 166, 202)"

# Second 'Screen'
dark_blue.entryButtonColor = "rgb(135, 230, 195)"
dark_blue.entrySpinBoxColor = "rgb(208, 255, 246)"
dark_blue.entryLineEditColor = "rgb(158, 176, 218)"
dark_blue.entryLabelColor = "rgb(192, 209, 255)"
dark_blue.entryCustomPlayerColor = "rgb(135, 186, 167)"

# Third 'Screen' | Main Window
# Card Colors
dark_blue.blue = "rgb(96, 130, 226)"
dark_blue.red = "rgb(202, 77, 77)"
dark_blue.green = "rgb(43, 191, 43)"
dark_blue.yellow = "rgb(217, 191, 62)"
dark_blue.black = "rgb(72, 71, 72)"

# Card Border Colors
dark_blue.normalBorderColor = "rgb(172, 187, 191)"
dark_blue.playableBorderColor = "rgb(150, 255, 215)"

# Card Value Picture
dark_blue.filePath = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"

# Default colors for the Players
dark_blue.defaultPlayerColors = ["rgb(150, 129, 212)", "rgb(61, 198, 213)",
                                 "rgb(67, 190, 40)", "rgb(59, 216, 230)",
                                 "rgb(230, 198, 30)", "rgb(230, 37, 170)"
                                 ]
dark_blue.updateStyle()
"""class Farbschema:
    def __init__(self):
        # ##### VALUES ############################################################################### #
        self.backgroundColor = "qlineargradient(spread:pad, x1:0.0797727, y1:0.914, x2:0.914773, y2:0.08, " \
                               "stop:0.0568182 rgba(28, 40, 54, 255), stop:0.960227 rgba(63, 88, 119, 255)) "

        # ## COLORS ## #
        # Basics
        self.buttonBasicColor = "rgb(217, 91, 19)"
        self.buttonActiveColor = "rgb(247, 94, 0)"
        self.buttonPassiveColor = "rgb(158, 89, 48)"
        self.buttonFocusColor = "rgb(245, 125, 5)"

        # First 'Screen'
        self.labelTitelColor = "rgb(99, 140, 186)"
        self.labelSubtitelColor = "rgb(74, 105, 138);"
        self.labelInfoColor = "rgb(152, 166, 202)"

        # Second 'Screen'
        self.buttonsEntryColor = "rgb(135, 230, 195)"
        self.spinBoxColorColor = "rgb(208, 255, 246)"
        self.lineEditColor = "rgb(158, 176, 218)"
        self.labelEntryColor = "rgb(192, 209, 255)"
        self.chooseColor = "rgb(135, 186, 167)"

        # Third 'Screen' | Main Window
        # Card Colors
        self.blau = "rgb(96, 130, 226)"
        self.rot = "rgb(202, 77, 77)"
        self.green = "rgb(43, 191, 43)"
        self.gelb = "rgb(217, 191, 62)"
        self.black = "rgb(72, 71, 72)"

        # Card Border Colors
        self.borderNormalColor = "rgb(172, 187, 191)"
        self.borderPlayColor = "rgb(150, 255, 215)"

        # Card Value Picture
        self.filePath = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"

        # Default colors for the Players
        self.P_COLORS = ["rgb(150, 129, 212)", "rgb(61, 198, 213)",
                         "rgb(67, 190, 40)", "rgb(59, 216, 230)",
                         "rgb(230, 198, 30)", "rgb(230, 37, 170)"
                         ]

        # ## RADIUS ## #
        self.windowRadius = "15px"

        # Second 'Screen'
        self.basicButtonRadius = "17px"
        self.startButtonRadius = "20px"
        self.entryRadius = "10px"

        # Third 'Screen'
        self.colorChoiceRadius = ("    border-top-left-radius : 5px;\n"
                                  "    border-top-right-radius : 0px; \n"
                                  "    border-bottom-left-radius : 0px; \n"
                                  "    border-bottom-right-radius : 5px\n")

        # Forth 'Screen'
        self.endButtonRadius = "25px"

        # STYLESHEETS ############################################################################### #

        self.frameBackground = "background-color: rgba(255, 255, 255, 0);"
        self.windowBackground = ("QFrame {\n"
                                 f"    background-color: {self.backgroundColor};\n"
                                 f"    border-radius: {self.windowRadius};\n"
                                 "}")
        self.windowBackgroundGame = ("QFrame {\n"
                                     f"    background-color: {self.backgroundColor};\n"
                                     "}")
        # ### First 'Screen'
        self.titelLabel = (f"{self.frameBackground}\n"
                           f"color: {self.labelTitelColor};")
        self.descriptionLabel = (f"{self.frameBackground}\n"
                                 f"color: {self.labelSubtitelColor};")
        self.startButton = ("QPushButton {\n"
                            f"    background-color: {self.buttonActiveColor};\n"
                            f"    border-radius: {self.startButtonRadius};\n"
                            "}")
        self.infoLabel = f"color: {self.labelInfoColor};"

        # Prepare
        self.entryLabels = (f"{self.frameBackground}\n"
                            f"color: {self.labelEntryColor}")

        self.pulsMinus = ("QPushButton {\n"
                          f"    background-color: {self.buttonsEntryColor};\n"
                          f"    border-radius: {self.entryRadius};\n"
                          "}")
        self.spinBox = ("QSpinBox {\n"
                        f"    background-color: {self.spinBoxColorColor};\n"
                        f"    border-radius: {self.entryRadius};\n"
                        "}\n")

        self.NameEntry = ("QLineEdit {\n"
                          f"    background-color: {self.lineEditColor};\n"
                          f"    border-radius: {self.entryRadius};\n"
                          "}")
        self.colorButton = ("QPushButton {\n"
                            f"    background-color: {self.chooseColor};\n"
                            f"    border-radius: {self.entryRadius};\n"
                            "}")
        self.okButton = ("QPushButton {\n"
                         f"    background-color: {self.buttonsEntryColor};\n"
                         "    border-width: 1px;\n"
                         "    border-style: solid;\n"
                         "    border-color:  rgb(98, 98, 98);\n"
                         "}\n")

        self.buttonPassive = ("QPushButton {\n"
                              f"    background-color: {self.buttonPassiveColor};\n"
                              f"    border-radius: {self.startButtonRadius};\n"
                              "}")
        # = startButton
        self.buttonActive = self.startButton
        self.theme_Reset = ("QPushButton {\n"
                            f"    background-color: {self.buttonBasicColor};\n"
                            f"    border-radius: {self.basicButtonRadius};\n"
                            "}")

        # Spiel
        self.currentPlayerName = f"color: {self.labelEntryColor}"
        self.uno_SkipButton = ("QPushButton {\n"
                               f"    background-color: {self.buttonFocusColor};\n"
                               f"    border-radius: {self.entryRadius}\n"
                               "}")
        self.unoButtonClicked = ("QPushButton {\n"
                                 f"    background-color: {self.buttonPassiveColor};\n"
                                 f"    border-radius: {self.entryRadius}\n"
                                 "}")
        self.highlightedDrawTalon = ("QPushButton {\n"
                                     f"    background-color: {self.black};\n"
                                     "    border-radius: 15px;\n"
                                     "    border-width: 3px; \n"
                                     "    border-style: solid;\n"
                                     f"    border-color: {self.borderPlayColor};"
                                     f"     image: url({self.filePath}default.png);\n "
                                     "}")
        self.normalDrawTalon = ("QPushButton {\n"
                                "    background-color: {self.};\n"
                                "    border-radius: 15px;\n"
                                f"   image: url({self.filePath}default.png);\n "
                                "}")

        self.blueChoice = ("QPushButton {\n"
                           f"    background-color: {self.blau};\n"
                           f"    {self.colorChoiceRadius}"
                           "}")
        self.greenChoice = ("QPushButton {\n"
                            f"    background-color: {self.green};\n"
                            f"    {self.colorChoiceRadius}"
                            "}")
        self.gelbChoice = ("QPushButton {\n"
                           f"    background-color: {self.gelb};\n"
                           f"    {self.colorChoiceRadius}"
                           "}")
        self.rotChoice = ("QPushButton {\n"
                          f"    background-color: {self.rot};\n"
                          f"    {self.colorChoiceRadius}"
                          "}")

        # Ende
        self.endMessage = self.titelLabel
        self.playButton = ("QPushButton {\n"
                           f"    background-color: {self.buttonFocusColor};\n"
                           f"    border-radius: {self.endButtonRadius}\n"
                           "}")
        self.menu_QuitButton = ("QPushButton {\n"
                                f"    background-color: {self.buttonBasicColor};\n"
                                f"    border-radius: {self.endButtonRadius}\n"
                                "}")


dark_blue = Farbschema()"""
