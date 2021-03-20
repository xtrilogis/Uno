class ColorTheme:
    """Contains als Variables and Stylesheets needed for The GUI

    VALUES contain all Values(Colors and Radius) which are changed for a new Theme
    STYLESHEETS contains the Stylesheets based on the Values
    UpdateStyle is needed for any new Theme to update the Stylesheets with the new Values"""

    def __init__(self):
        # ##### VALUES ######################################## #
        self.backgroundColor = "rgb(240, 240, 240)"

        # ## COLORS ## #
        # Basics
        self.buttonColorBasic = "rgb(195, 195, 195)"
        self.buttonColorActive = "rgb(195, 195, 195)"
        self.buttonColorPassive = "rgb(195, 195, 195)"
        self.buttonColorFocus = "rgb(195, 195, 195)"

        # First 'Screen'
        self.titleColor = "rgb(108, 108, 108)"
        self.subtitleColor = "rgb(108, 108, 108)"
        self.infoLabelColor = "rgb(108, 108, 108)"

        # Second 'Screen'
        self.entryButtonColor = "rgb(155, 182, 193)"
        self.entrySpinBoxColor = "rgb(108, 108, 108)"
        self.entryLineEditColor = "rgb(108, 108, 108)"
        self.entryLabelColor = "rgb(108, 108, 108)"
        self.entryCustomPlayerColor = "rgb(108, 108, 108)"

        # Third 'Screen' | Main Window
        # ## Card Colors
        self.blue = "rgb(31, 11, 255)"
        self.red = "rgb(255, 2, 2)"
        self.green = "rgb(73, 255, 7)"
        self.yellow = "rgb(255, 255, 8)"
        self.black = "rgb(141, 137, 156)"

        # ## Card Border Colors
        self.normalBorderColor = "rgb(155, 182, 193)"
        self.playableBorderColor = "rgb(108, 108, 108)"

        # ## Directory for Card-Value Pictures
        self.filePath = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"

        self.defaultPlayerColors = ["rgb(255, 85, 255)", "rgb(0, 170, 127)",
                                    "rgb(0, 85, 255)"]  # A list of rgb colors as strings

        # ## RADIUS ## #
        self.windowRadius = "15px"

        # Second 'Screen'
        self.buttonRadiusBasic = "17px"
        self.buttonRadiusMain = "20px"
        self.entryRadius = "10px"

        # Third 'Screen'
        self.buttonRadiusWildcard_ColorWish = ("    border-top-left-radius : 5px;\n"
                                               "    border-top-right-radius : 0px; \n"
                                               "    border-bottom-left-radius : 0px; \n"
                                               "    border-bottom-right-radius : 5px\n")

        # Forth 'Screen'
        self.buttonRadiusGameOverMenu = "25px"

        # STYLESHEETS ######################################## #
        self.transparentBackground = "background-color: rgba(255, 255, 255, 0);"
        self.windowBackground_Style = ("QFrame {\n"
                                       f"    background-color: {self.backgroundColor};\n"
                                       f"    border-radius: {self.windowRadius};\n"
                                       "}")
        self.gameWindowBackground_Style = ("QFrame {\n"
                                           f"    background-color: {self.backgroundColor};\n"
                                           "}")

        # ### First 'Screen'
        self.titelLabel_Style = (f"{self.transparentBackground}\n"
                                 f"color: {self.titleColor};")
        self.subtitleLabel_Style = (f"{self.transparentBackground}\n"
                                    f"color: {self.subtitleColor};")
        self.mainButton_Style = ("QPushButton {\n"
                                 f"    background-color: {self.buttonColorActive};\n"
                                 f"    border-radius: {self.buttonRadiusMain};\n"
                                 "}")  # StartButton
        self.infoLabel_Style = f"color: {self.infoLabelColor};"  # infoLabel

        # Second 'Screen'
        self.entryLabels_Style = (f"{self.transparentBackground}\n"
                                  f"color: {self.entryLabelColor}")  # AnzahlLabel | NameLabel
        self.pulsMinusButton_Style = ("QPushButton {\n"
                                      f"    background-color: {self.entryButtonColor};\n"
                                      f"    border-radius: {self.entryRadius};\n"
                                      "}")
        self.spinBox_Style = ("QSpinBox {\n"
                              f"    background-color: {self.entrySpinBoxColor};\n"
                              f"    border-radius: {self.entryRadius};\n"
                              "}\n")

        self.playerNameEntry_Style = ("QLineEdit {\n"
                                      f"    background-color: {self.entryLineEditColor};\n"
                                      f"    border-radius: {self.entryRadius};\n"
                                      "}")  # NameEingabe
        self.colorButton_Style = ("QPushButton {\n"
                                  f"    background-color: {self.entryCustomPlayerColor};\n"
                                  f"    border-radius: {self.entryRadius};\n"
                                  "}")
        self.okButton_Style = ("QPushButton {\n"
                               f"    background-color: {self.entryButtonColor};\n"
                               "    border-width: 1px;\n"
                               "    border-style: solid;\n"
                               "    border-color:  rgb(98, 98, 98);\n"
                               "}\n")

        self.passiveButton_Style = ("QPushButton {\n"
                                    f"    background-color: {self.buttonColorPassive};\n"
                                    f"    border-radius: {self.buttonRadiusMain};\n"
                                    "}")

        self.theme_ResetButton_Style = ("QPushButton {\n"
                                        f"    background-color: {self.buttonColorBasic};\n"
                                        f"    border-radius: {self.buttonRadiusBasic};\n"
                                        "}")

        # Third 'Screen'
        # self.currentPlayerName_Style = f"color: {self.entryLabelColor}"
        self.uno_SkipButton_Style = ("QPushButton {\n"
                                     f"    background-color: {self.buttonColorFocus};\n"
                                     f"    border-radius: {self.entryRadius}\n"
                                     "}")
        self.unoButtonClicked_Style = ("QPushButton {\n"
                                       f"    background-color: {self.buttonColorPassive};\n"
                                       f"    border-radius: {self.entryRadius}\n"
                                       "}")
        self.highlightedDrawTalon_Style = ("QPushButton {\n"
                                           f"    background-color: {self.black};\n"
                                           "    border-radius: 15px;\n"
                                           "    border-width: 3px; \n"
                                           "    border-style: solid;\n"
                                           f"    border-color: {self.playableBorderColor};"
                                           f"     image: url({self.filePath}default.png);\n "
                                           "}")
        self.normalDrawTalon_Style = ("QPushButton {\n"
                                      f"    background-color: {self.black};\n"
                                      "    border-radius: 15px;\n"
                                      "    border-width: 3px; \n"
                                      "    border-style: solid;\n"
                                      f"    border-color: {self.black};"
                                      f"     image: url({self.filePath}default.png);\n "
                                      "}")
        """"QPushButton {\n"
                                      f"    background-color: {self.bl};\n"
                                      "    border-radius: 15px;\n"
                                      f"   image: url({self.filePath}default.png);\n "
                                      "}")"""

        self.blueChoice_Style = ("QPushButton {\n"
                                 f"    background-color: {self.blue};\n"
                                 f"    {self.buttonRadiusWildcard_ColorWish}"
                                 "}")
        self.greenChoice_Style = ("QPushButton {\n"
                                  f"    background-color: {self.green};\n"
                                  f"    {self.buttonRadiusWildcard_ColorWish}"
                                  "}")
        self.yellowChoice_Style = ("QPushButton {\n"
                                   f"    background-color: {self.yellow};\n"
                                   f"    {self.buttonRadiusWildcard_ColorWish}"
                                   "}")
        self.redChoice_Style = ("QPushButton {\n"
                                f"    background-color: {self.red};\n"
                                f"    {self.buttonRadiusWildcard_ColorWish}"
                                "}")

        # Forth 'Screen'
        self.gameOverMassage_Style = self.titelLabel_Style
        self.playAgainButton_Style = ("QPushButton {\n"
                                      f"    background-color: {self.buttonColorFocus};\n"
                                      f"    border-radius: {self.buttonRadiusGameOverMenu}\n"
                                      "}")
        self.menu_QuitButton_Style = ("QPushButton {\n"
                                      f"    background-color: {self.buttonColorBasic};\n"
                                      f"    border-radius: {self.buttonRadiusGameOverMenu}\n"
                                      "}")

    def updateStyle(self):
        """Updates the Stylesheets, needed whenever attributes are other than the default"""
        self.transparentBackground = "background-color: rgba(255, 255, 255, 0);"
        self.windowBackground_Style = ("QFrame {\n"
                                       f"    background-color: {self.backgroundColor};\n"
                                       f"    border-radius: {self.windowRadius};\n"
                                       "}")
        self.gameWindowBackground_Style = ("QFrame {\n"
                                           f"    background-color: {self.backgroundColor};\n"
                                           "}")

        # ### First 'Screen'
        self.titelLabel_Style = (f"{self.transparentBackground}\n"
                                 f"color: {self.titleColor};")
        self.subtitleLabel_Style = (f"{self.transparentBackground}\n"
                                    f"color: {self.subtitleColor};")
        self.mainButton_Style = ("QPushButton {\n"
                                 f"    background-color: {self.buttonColorActive};\n"
                                 f"    border-radius: {self.buttonRadiusMain};\n"
                                 "}")  # StartButton
        self.infoLabel_Style = f"color: {self.infoLabelColor};"  # infoLabel

        # Second 'Screen'
        self.entryLabels_Style = (f"{self.transparentBackground}\n"
                                  f"color: {self.entryLabelColor}")  # AnzahlLabel | NameLabel
        self.pulsMinusButton_Style = ("QPushButton {\n"
                                      f"    background-color: {self.entryButtonColor};\n"
                                      f"    border-radius: {self.entryRadius};\n"
                                      "}")
        self.spinBox_Style = ("QSpinBox {\n"
                              f"    background-color: {self.entrySpinBoxColor};\n"
                              f"    border-radius: {self.entryRadius};\n"
                              "}\n")

        self.playerNameEntry_Style = ("QLineEdit {\n"
                                      f"    background-color: {self.entryLineEditColor};\n"
                                      f"    border-radius: {self.entryRadius};\n"
                                      "}")  # NameEingabe
        self.colorButton_Style = ("QPushButton {\n"
                                  f"    background-color: {self.entryCustomPlayerColor};\n"
                                  f"    border-radius: {self.entryRadius};\n"
                                  "}")
        self.okButton_Style = ("QPushButton {\n"
                               f"    background-color: {self.entryButtonColor};\n"
                               "    border-width: 1px;\n"
                               "    border-style: solid;\n"
                               "    border-color:  rgb(98, 98, 98);\n"
                               "}\n")

        self.passiveButton_Style = ("QPushButton {\n"
                                    f"    background-color: {self.buttonColorPassive};\n"
                                    f"    border-radius: {self.buttonRadiusMain};\n"
                                    "}")

        self.theme_ResetButton_Style = ("QPushButton {\n"
                                        f"    background-color: {self.buttonColorBasic};\n"
                                        f"    border-radius: {self.buttonRadiusBasic};\n"
                                        "}")

        # Third 'Screen'
        # self.currentPlayerName_Style = f"color: {self.entryLabelColor}"
        self.uno_SkipButton_Style = ("QPushButton {\n"
                                     f"    background-color: {self.buttonColorFocus};\n"
                                     f"    border-radius: {self.entryRadius}\n"
                                     "}")
        self.unoButtonClicked_Style = ("QPushButton {\n"
                                       f"    background-color: {self.buttonColorPassive};\n"
                                       f"    border-radius: {self.entryRadius}\n"
                                       "}")
        self.highlightedDrawTalon_Style = ("QPushButton {\n"
                                           f"    background-color: {self.black};\n"
                                           "    border-radius: 15px;\n"
                                           "    border-width: 3px; \n"
                                           "    border-style: solid;\n"
                                           f"    border-color: {self.playableBorderColor};"
                                           f"     image: url({self.filePath}default.png);\n "
                                           "}")
        self.normalDrawTalon_Style = ("QPushButton {\n"
                                      f"    background-color: {self.black};\n"
                                      "    border-radius: 15px;\n"
                                      "    border-width: 3px; \n"
                                      "    border-style: solid;\n"
                                      f"    border-color: {self.black};"
                                      f"     image: url({self.filePath}default.png);\n "
                                      "}")

        self.blueChoice_Style = ("QPushButton {\n"
                                 f"    background-color: {self.blue};\n"
                                 f"    {self.buttonRadiusWildcard_ColorWish}"
                                 "}")
        self.greenChoice_Style = ("QPushButton {\n"
                                  f"    background-color: {self.green};\n"
                                  f"    {self.buttonRadiusWildcard_ColorWish}"
                                  "}")
        self.yellowChoice_Style = ("QPushButton {\n"
                                   f"    background-color: {self.yellow};\n"
                                   f"    {self.buttonRadiusWildcard_ColorWish}"
                                   "}")
        self.redChoice_Style = ("QPushButton {\n"
                                f"    background-color: {self.red};\n"
                                f"    {self.buttonRadiusWildcard_ColorWish}"
                                "}")

        # Forth 'Screen'
        self.gameOverMassage_Style = self.titelLabel_Style
        self.playAgainButton_Style = ("QPushButton {\n"
                                      f"    background-color: {self.buttonColorFocus};\n"
                                      f"    border-radius: {self.buttonRadiusGameOverMenu}\n"
                                      "}")
        self.menu_QuitButton_Style = ("QPushButton {\n"
                                      f"    background-color: {self.buttonColorBasic};\n"
                                      f"    border-radius: {self.buttonRadiusGameOverMenu}\n"
                                      "}")


default = ColorTheme()
