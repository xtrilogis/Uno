from theme_class import ColorTheme

developer = ColorTheme()


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
