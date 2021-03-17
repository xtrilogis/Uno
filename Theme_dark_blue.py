class Farbschema:
    def __init__(self):
        # ##### VALUES ############################################################################### #
        self.backgroundColor = "qlineargradient(spread:pad, x1:0.0797727, y1:0.914, x2:0.914773, y2:0.08, " \
                               "stop:0.0568182 rgba(28, 40, 54, 255), stop:0.960227 rgba(63, 88, 119, 255)) "

        # ## COLORS ## #
        # Basics
        self.buttonColorBasic = "rgb(217, 91, 19)"
        self.buttonColorActive = "rgb(247, 94, 0)"
        self.buttonColorPassive = "rgb(158, 89, 48)"
        self.buttonColorFocus = "rgb(245, 125, 5)"

        # First 'Screen'
        self.labelTitel = "rgb(99, 140, 186)"
        self.labelSubtitel = "rgb(74, 105, 138);"
        self.labelInfo = "rgb(152, 166, 202)"

        # Second 'Screen'
        self.buttonsEntry = "rgb(135, 230, 195)"
        self.spinBox = "rgb(208, 255, 246)"
        self.lineEdit = "rgb(158, 176, 218)"
        self.labelEntry = "rgb(192, 209, 255)"
        self.chooseColor = "rgb(135, 186, 167)"

        # Third 'Screen' | Main Window
        # Card Colors
        self.blau = "rgb(96, 130, 226)"
        self.rot = "rgb(202, 77, 77)"
        self.green = "rgb(43, 191, 43)"
        self.gelb = "rgb(217, 191, 62)"
        self.black = "rgb(72, 71, 72)"

        # Card Border Colors
        self.borderNormal = "rgb(172, 187, 191)"
        self.borderPlay = "rgb(150, 255, 215)"

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
        self.WindowBackground = ("QFrame {\n"
                                 f"    background-color: {self.backgroundColor};\n"
                                 f"    border-radius: {self.windowRadius};\n"
                                 "}")
        self.WindowBackgroundGame = ("QFrame {\n"
                                     f"    background-color: {self.backgroundColor};\n"
                                     "}")
        # ### First 'Screen'
        self.TitelLabel = (f"{self.frameBackground}\n"
                           f"color: {self.labelTitel};")
        self.DescriptionLabel = (f"{self.frameBackground}\n"
                                 f"color: {self.labelSubtitel};")
        self.StartButton = ("QPushButton {\n"
                            f"    background-color: {self.buttonColorActive};\n"
                            f"    border-radius: {self.startButtonRadius};\n"
                            "}")
        self.infoLabel = f"color: {self.labelInfo};"

        # Prepare
        self.EntryLabels = (f"{self.frameBackground}\n"
                            f"color: {self.labelEntry}")

        self.PulsMinus = ("QPushButton {\n"
                          f"    background-color: {self.buttonsEntry};\n"
                          f"    border-radius: {self.entryRadius};\n"
                          "}")
        self.spinBox = ("QSpinBox {\n"
                        f"    background-color: {self.spinBox};\n"
                        f"    border-radius: {self.entryRadius};\n"
                        "}\n")

        self.NameEntry = ("QLineEdit {\n"
                          f"    background-color: {self.lineEdit};\n"
                          f"    border-radius: {self.entryRadius};\n"
                          "}")
        self.colorButton = ("QPushButton {\n"
                            f"    background-color: {self.chooseColor};\n"
                            f"    border-radius: {self.entryRadius};\n"
                            "}")
        self.okButton = ("QPushButton {\n"
                         f"    background-color: {self.buttonsEntry};\n"
                         "    border-width: 1px;\n"
                         "    border-style: solid;\n"
                         "    border-color:  rgb(98, 98, 98);\n"
                         "}\n")

        self.ButtonPassive = ("QPushButton {\n"
                              f"    background-color: {self.buttonColorPassive};\n"
                              f"    border-radius: {self.startButtonRadius};\n"
                              "}")
        # = startButton
        self.ButtonActive = self.StartButton
        self.theme_Reset = ("QPushButton {\n"
                            f"    background-color: {self.buttonColorBasic};\n"
                            f"    border-radius: {self.basicButtonRadius};\n"
                            "}")

        # Spiel
        self.currentPlayerName = f"color: {self.labelEntry}"
        self.UNO_SkipButton = ("QPushButton {\n"
                               f"    background-color: {self.buttonColorFocus};\n"
                               f"    border-radius: {self.entryRadius}\n"
                               "}")
        self.UNOButtonClicked = ("QPushButton {\n"
                                 f"    background-color: {self.buttonColorPassive};\n"
                                 f"    border-radius: {self.entryRadius}\n"
                                 "}")
        self.highlightedDrawTalon = ("QPushButton {\n"
                                     f"    background-color: {self.black};\n"
                                     "    border-radius: 15px;\n"
                                     "    border-width: 3px; \n"
                                     "    border-style: solid;\n"
                                     f"    border-color: {self.borderPlay};"
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
        self.EndMessage = self.TitelLabel
        self.PlayButton = ("QPushButton {\n"
                           f"    background-color: {self.buttonColorFocus};\n"
                           f"    border-radius: {self.endButtonRadius}\n"
                           "}")
        self.menu_QuitButton = ("QPushButton {\n"
                                f"    background-color: {self.buttonColorBasic};\n"
                                f"    border-radius: {self.endButtonRadius}\n"
                                "}")


dark_blue = Farbschema()
