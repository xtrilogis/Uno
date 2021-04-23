class Size:
    """Contains basic sizes for the GUI"""
    def __init__(self):
        self.rand = 10
        self.space = 3
        self.card_width = 141
        self.card_height = 233

        self.card_w_and_space = self.card_width + self.space
        self.card_h_and_space = self.card_height + self.space


size = Size()


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
        self.buttonColorBasic = "rgb(181, 181, 181)"
        self.buttonColorActive = "rgb(108, 108, 108)"
        self.buttonColorPassive = "rgb(206, 206, 206)"
        self.buttonColorFocus = "rgb(117, 117, 117)"

        # First 'Screen'
        self.titleColor = "rgb(138, 138, 138)"
        self.subtitleColor = "rgb(177, 177, 177)"
        self.infoLabelColor = "rgb(148, 148, 148)"

        # Second 'Screen'
        self.entryButtonColor = "rgb(155, 182, 193)"
        self.entrySpinBoxColor = "rgb(131, 147, 177)"
        self.entryLineEditColor = "rgb(131, 147, 177)"
        self.entryLabelColor = "rgb(108, 108, 108)"
        self.entryCustomPlayerColor = "rgb(122, 144, 152)"

        # Third 'Screen' | Main Window
        # ## Card Colors
        self.blue = "rgb(125, 177, 255)"
        self.red = "rgb(255, 165, 138)"
        self.green = "rgb(148, 222, 130)"
        self.yellow = "rgb(225, 214, 7)"
        self.black = "rgb(141, 137, 156)"

        # ## Card Border Colors
        self.normalBorderColor = "rgb(255, 255, 255)"
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

        """        # ###
        self.transparentBackground = ""
        self.windowBackground_Style = ()
        self.gameWindowBackground_Style = ()
        # ### First 'Screen'
        self.titelLabel_Style = ()
        self.subtitleLabel_Style = ()
        self.mainButton_Style = ()
        self.infoLabel_Style = f""
        # Second 'Screen'
        self.entryLabels_Style = ()
        self.pulsMinusButton_Style = ()
        self.spinBox_Style = ()
        self.playerNameEntry_Style = ()
        self.colorButton_Style = ()
        self.okButton_Style = ()
        self.passiveButton_Style = ()
        self.theme_ResetButton_Style = ()
        # Third 'Screen'

        self.uno_SkipButton_Style = ()
        self.unoButtonClicked_Style = ()
        self.highlightedDrawTalon_Style = ()
        self.normalDrawTalon_Style = ()
        self.blueChoice_Style = ()
        self.greenChoice_Style = ()
        self.yellowChoice_Style = ()
        self.redChoice_Style = ()
        # Forth 'Screen'
        self.gameOverMassage_Style = self.titelLabel_Style
        self.playAgainButton_Style = ()
        self.menu_QuitButton_Style = ()
        
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
                                      "}")"""
        self.updateStyle()

    def updateStyle(self):
        """"Updates the Stylesheets, needed whenever attributes are other than the default"""
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
                                 "}")
        self.infoLabel_Style = f"color: {self.infoLabelColor};"

        # Second 'Screen'
        self.entryLabels_Style = (f"{self.transparentBackground}\n"
                                  f"color: {self.entryLabelColor}")
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
                                      "}")
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
