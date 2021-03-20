from Theme_template import *

developer = ColorTheme()

# ##### VALUES ############################################################################### #
developer.backgroundColor = "rgb(217, 198, 255);"

# ## COLORS ## #
# Basics
developer.buttonColorBasic = "rgb(184, 101, 162)"
developer.buttonColorActive = "rgb(255, 35, 152)"
developer.buttonColorPassive = "rgb(186, 26, 111)"
developer.buttonColorFocus = "rgb(177, 90, 173)"

# First 'Screen'
developer.titleColor = "rgb(105, 163, 255)"
developer.subtitleColor = "rgb(123, 132, 255)"
developer.infoLabelColor = "rgb(152, 166, 202)"

# Second 'Screen'
developer.entryButtonColor = "rgb(162, 255, 216)"
developer.entrySpinBoxColor = "rgb(208, 255, 246)"
developer.entryLineEditColor = "rgb(182, 166, 214)"
developer.entryLabelColor = "rgb(0, 0, 0)"
developer.entryCustomPlayerColor = "rgb(225, 124, 200)"

# Third 'Screen' | Main Window
# ## Card Colors
developer.blue = "rgb(125, 177, 255)"
developer.red = "rgb(255, 165, 138)"
developer.green = "rgb(169, 255, 149)"
developer.yellow = "rgb(238, 226, 137)"
developer.black = "rgb(72, 71, 72)"

# ## Card Border Colors
developer.normalBorderColor = "rgb(255, 255, 255)"
developer.playableBorderColor = "rgb(211, 112, 218)"

# ## Card Value Picture
developer.filePath = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"

# Default colors for the Players
developer.defaultPlayerColors = ["rgb(150, 129, 212)", "rgb(61, 198, 213)",
                                 "rgb(67, 190, 40)", "rgb(59, 216, 230)",
                                 "rgb(230, 198, 30)", "rgb(230, 37, 170)"
                                 ]
developer.updateStyle()
"""class Farbschema:
    def __init__(self):
        # ##### VALUES ############################################################################### #
        self.backgroundColor = "rgb(217, 198, 255);"

        # ## COLORS ## #
        # Basics
        self.buttonColorBasic = "rgb(184, 101, 162)"
        self.buttonColorActive = "rgb(255, 35, 152)"
        self.buttonColorPassive = "rgb(186, 26, 111)"
        self.buttonColorFocus = "rgb(177, 90, 173)"

        # First 'Screen'
        self.titelColor = "rgb(105, 163, 255)"
        self.labelSubtitelColor = "rgb(123, 132, 255)"
        self.labelInfoColor = "rgb(152, 166, 202)"

        # Second 'Screen'
        self.buttonsEntryColor = "rgb(162, 255, 216)"
        self.spinBoxColor = "rgb(208, 255, 246)"
        self.lineEditColor = "rgb(182, 166, 214)"
        self.labelEntryColor = "rgb(0, 0, 0)"
        self.chooseColor = "rgb(225, 124, 200)"

        # Third 'Screen' | Main Window
        # ## Card Colors
        self.blau = "rgb(125, 177, 255)"
        self.rot = "rgb(255, 165, 138)"
        self.green = "rgb(169, 255, 149)"
        self.gelb = "rgb(238, 226, 137)"
        self.black = "rgb(72, 71, 72)"

        # ## Card Border Colors
        self.borderNormalColor = "rgb(255, 255, 255)"
        self.borderPlayColor = "rgb(211, 112, 218)"

        # ## Card Value Picture
        self.filePath = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"

        # Default colors for the Players
        self.P_COLORS = ["rgb(150, 129, 212)", "rgb(61, 198, 213)",
                         "rgb(67, 190, 40)", "rgb(59, 216, 230)",
                         "rgb(230, 198, 30)", "rgb(230, 37, 170)"
                         ]

        # ## RADIUS ## #
        self.windowRadius = "15px"

        # Second 'Screen'
        self.basicButtonRadius = "15px"
        self.startButtonRadius = "15px"
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

        # First 'Screen'
        self.titelLabel = (f"{self.frameBackground}\n"
                           f"color: {self.labelTitelColor};")
        self.descriptionLabel = (f"{self.frameBackground}\n"
                                 f"color: {self.labelSubtitelColor};")
        self.startButton = ("QPushButton {\n"
                            f"    background-color: {self.startButtonRadius};\n"
                            f"    border-radius: {self.buttonActiveColor};\n"
                            "}")
        self.infoLabel = f"color: {self.labelInfoColor};"

        # Second 'Screen'
        self.entryLabel = (f"{self.frameBackground}\n"
                           f"color: {self.labelEntryColor}")
        self.pulsMinus = ("QPushButton {\n"
                          f"    background-color: {self.buttonsEntryColor};\n"
                          f"    border-radius: {self.entryRadius};\n"
                          "}")
        self.spinBox = ("QSpinBox {\n"
                        f"    background-color: {self.spinBoxColor};\n"
                        f"    border-radius: {self.entryRadius};\n"
                        "}")

        self.nameEntry = ("QLineEdit {\n"
                          f"    border-radius: {self.lineEditColor};\n"
                          f"    background-color: {self.entryRadius};\n"
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
                              f"    border-radius: {self.startButtonRadius};\n"
                              f"    background-color: {self.buttonColorPassive};\n"
                              "}")
        # = startButton
        self.buttonActive = self.startButton
        self.theme_Reset = ("QPushButton {\n"
                            f"    border-radius: {self.basicButtonRadius};\n"
                            f"    background-color: {self.buttonColorBasic};\n"
                            "}")

        # Third 'Screen'
        self.currentPlayerName = f"color: {self.labelEntryColor}"
        self.uno_skipButton = ("QPushButton {\n"
                               f"    background-color: {self.buttonColorBasic};\n"
                               f"    border-radius: {self.entryRadius}\n"
                               "}")
        self.unoButtonclicked = ("QPushButton {\n"
                                 f"    background-color: {self.buttonColorPassive};\n"
                                 f"    border-radius: {self.entryRadius}\n"
                                 "}")
        self.highlightedDrawTalon = ("QPushButton {\n"
                                     f"    background-color: {self.black};\n"
                                     "    border-radius: 15px;\n"
                                     "    border-width: 3px; \n"
                                     "    border-style: solid;\n"
                                     f"    border-color: {self.borderPlayColor};"
                                     f"    image: url({self.filePath}default.png);\n "
                                     "}")
        self.drawTalon = ("QPushButton {\n"
                          "    background-color: rgb(72, 71, 72);\n"
                          "border-radius: 15px;\n"
                          f"image: url({self.filePath}default.png);\n "
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

        # Forth 'Screen'
        self.endMessage = self.titelLabel
        self.playButton = (("QPushButton {\n"
                            f"    background-color: {self.buttonColorFocus};\n"
                            f"    border-radius: {self.endButtonRadius}\n"
                            "}"))
        self.menuQuitButton = ("QPushButton {\n"
                               f"    background-color: {self.buttonColorBasic};\n"
                               f"    border-radius: {self.endButtonRadius}\n"
                               "}")


developer = Farbschema()"""
