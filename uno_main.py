import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QColorDialog, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

from ui_prepare_screen import *
from ui_main_game_window import *
from ui_game_over_screen import *

from theme_development import developer
from theme_dark_blue import dark_blue
from theme_class import default, size

"Handkartenframe wird nicht angezeigt"
"Pfad als Relation vom Projekt ordner"
# ### GLOBALS ### #
COLORS = ["Blue", "Green", "Yellow", "Red"]
VALUES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DRAW_TALON = []
PLAY_TALON = []
PLAYERS = []
VICTOR = None

# Basic Start Theme
THEME = default


# ##### Front-End Methods (GUI) ##### #
# ##### Back-End Methods (None-GUI/No direct relation) ##### #
# ##### Button calls ##### #

# ### First + Second 'Screen' ### #
class UiStartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MWinPrepare()
        self.ui.setupUi(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.player_counter = len(PLAYERS) + 1

        # ### SETUP UI ### #
        self.set_theme()
        self.setup_start_screen()

        self.prepare_game()

        # ### BUTTON CONNECT ### #
        self.ui.pushButton_Start.clicked.connect(self.startPushed)
        self.ui.pushButton_Close.clicked.connect(self.close)

        self.ui.pushButton_SelectColor.clicked.connect(self.show_color_dialog)
        self.ui.pushButton_ReturnEntry.clicked.connect(self.process_name_entry)
        self.ui.pushButton_Next.clicked.connect(self.next_clicked)

        self.ui.pushButton_Reset.clicked.connect(self.reset_entries)
        self.ui.pushButton_Theme.clicked.connect(self.change_theme)

    # ##### Front-End Methods (GUI) ##### #
    def set_theme(self):
        """adjust all GUI parts to the currently selected Theme"""
        self.ui.frame_Background.setStyleSheet(THEME.windowBackground_Style)
        self.ui.frame_Close.setStyleSheet(THEME.transparentBackground)

        self.ui.frame_NextScreen.setStyleSheet(THEME.transparentBackground)
        self.ui.pushButton_Start.setStyleSheet(THEME.mainButton_Style)
        self.ui.pushButton_Next.setStyleSheet(THEME.passiveButton_Style)

        self.ui.label_Title.setStyleSheet(THEME.titelLabel_Style)
        self.ui.label_Subtitle.setStyleSheet(THEME.subtitleLabel_Style)
        self.ui.label_Info.setStyleSheet(THEME.infoLabel_Style)

        self.ui.frame_PlayerQuantity.setStyleSheet(THEME.transparentBackground)
        self.ui.label_Quantity.setStyleSheet(THEME.entryLabels_Style)
        self.ui.pushButton_QuantityPlus.setStyleSheet(THEME.pulsMinusButton_Style)
        self.ui.pushButton_QuantityMinus.setStyleSheet(THEME.pulsMinusButton_Style)
        self.ui.spinBox_Quantity.setStyleSheet(THEME.spinBox_Style)

        self.ui.frame_PlayerEntry.setStyleSheet(THEME.transparentBackground)
        self.ui.label_Entry.setStyleSheet(THEME.entryLabels_Style)
        self.ui.lineEdit_EnterName.setStyleSheet(THEME.playerNameEntry_Style)
        self.ui.pushButton_SelectColor.setStyleSheet(THEME.colorButton_Style)
        self.ui.pushButton_ReturnEntry.setStyleSheet(THEME.okButton_Style)
        self.ui.label_Result.setStyleSheet(THEME.entryLabels_Style)

        self.ui.frame_ResetThemeInfo.setStyleSheet(THEME.transparentBackground)
        self.ui.pushButton_Reset.setStyleSheet(THEME.theme_ResetButton_Style)
        self.ui.pushButton_Theme.setStyleSheet(THEME.theme_ResetButton_Style)

    def setup_start_screen(self):
        """sets Settings for the first screen to appear when Programm executed"""
        self.hide_prepare_screen()
        self.set_drop_shadow()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # removes window control bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # transparent background behind frame

    def set_drop_shadow(self):
        """adds a drop shadow to the background-frame as well as the start pushButton"""
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame_Background.setGraphicsEffect(self.shadow)
        self.ui.pushButton_Start.setGraphicsEffect(self.shadow)

    def show_start_screen(self):
        """shows everything related to the start_screen

        shows Title, Subtitle, Start-Button"""
        self.ui.pushButton_Start.show()
        self.ui.label_Title.show()
        self.ui.label_Subtitle.show()

    def hide_start_screen(self):
        """hides everything related to the start_screen

        hides Title, Subtitle, Start-Button"""
        self.ui.pushButton_Start.hide()
        self.ui.label_Title.hide()
        self.ui.label_Subtitle.hide()

    def show_prepare_screen(self):
        """shows everything related to the prepare-screen

        shows Player-Quantity-frame, Player-Entry-frame, Reset-, Next- and Theme-Button"""
        self.ui.frame_PlayerQuantity.show()
        self.ui.frame_PlayerEntry.show()
        self.ui.pushButton_Reset.show()
        self.ui.pushButton_Next.show()
        self.ui.pushButton_Theme.show()

    def hide_prepare_screen(self):
        """hides all GUI Parts related to the prepare-screen

        hides Player-Quantity-frame, Player-Entry-frame, Reset-, Next- and Theme-Button"""
        self.ui.frame_PlayerQuantity.hide()
        self.ui.frame_PlayerEntry.hide()
        self.ui.pushButton_Reset.hide()
        self.ui.pushButton_Next.hide()
        self.ui.pushButton_Theme.hide()
        self.ui.label_Result.hide()

    # ##### Back-End Methods (None-GUI/No direct relation) ##### #
    def prepare_game(self):
        """sets the minimum of Players to 2 and sets the entry_Label vor the first Entry"""
        self.ui.spinBox_Quantity.setMinimum(2)
        self.ui.label_Entry.setText(f"Spieler {self.player_counter}:")

    def create_player(self):
        """creates an object of class Players

        creates the player with the entered Name, an empty list for the hand and
            sets the Player color by using the first element of the Player-colors list
        removes the used color to the end of the color list
        clears the lineEdit"""
        PLAYERS.append(Player(name=self.ui.lineEdit_EnterName.text(),
                              hand_cards=[],
                              player_color=THEME.defaultPlayerColors[0]))
        THEME.defaultPlayerColors.append(THEME.defaultPlayerColors.pop(0))
        self.ui.lineEdit_EnterName.clear()

    def start_game(self):
        """opens a new Window, initializing the game"""
        self.game_window = UiMainGameWindow()
        self.game_window.show()

        self.close()

    def display_missing_players(self):
        """displays a Massage saying how many names were entert and how many need to be added"""
        self.ui.frame_PlayerQuantity.show()
        self.ui.frame_PlayerEntry.show()
        self.ui.label_Result.show()

        self.ui.label_Entry.setText(f"Spieler {self.player_counter}:")
        given_entries = self.ui.spinBox_Quantity.value() - len(PLAYERS)
        if len(PLAYERS) == 0:
            self.ui.label_Result.setText(f"Zu wenig Spieler! Noch kein Spielername eingegeben. \n"
                                         f"Es fehlen noch: {given_entries} Namen")
        else:
            self.ui.label_Result.setText(f"Zu wenig Spieler! Nur {len(PLAYERS)} Spielername(n) eingegeben.\n"
                                         f"Es fehlen noch: {given_entries} Namen")

    # ##### Button calls ##### #
    def startPushed(self):
        """switches from start-screen to prepare_screen"""
        self.hide_start_screen()
        self.show_prepare_screen()

    def show_color_dialog(self):
        """shows a pop-up Color Dialog and inserts the chosen color to the Player-color list"""
        selected_color = QColorDialog.getColor()
        if selected_color.isValid():
            THEME.defaultPlayerColors.insert(0, f"rgb{selected_color.getRgb()}")

    def process_name_entry(self):
        """ creates the player and adjusts the GUI

        if not all players are created: change Label
        if all created: hide entry-fields, set 'Next' Button to active"""
        global PLAYERS
        self.create_player()

        if len(PLAYERS) < self.ui.spinBox_Quantity.value():
            self.player_counter = len(PLAYERS) + 1
            self.ui.label_Entry.setText(f"Spieler {self.player_counter}:")
        else:
            self.ui.frame_PlayerEntry.hide()
            self.ui.frame_PlayerQuantity.hide()

            self.ui.label_Result.show()
            self.ui.label_Result.setText(f"{len(PLAYERS)} Spieler")
            self.ui.pushButton_Next.setStyleSheet(THEME.mainButton_Style)

    def next_clicked(self):
        """checks if all players are created, opens Game-Window or displays an Error-message

        if all players created: open Game-Window
        if not: display how many Players are created, show Entry-fields"""
        if len(PLAYERS) == self.ui.spinBox_Quantity.value():
            self.start_game()
        else:
            self.display_missing_players()

    def change_theme(self):
        """changes the Theme when Button is clicked"""
        global THEME
        if THEME == dark_blue:
            THEME = developer
        elif THEME == developer:
            THEME = default
        else:
            THEME = dark_blue
        self.set_theme()

        # Next-Button is by default deactivated following activates it
        if len(PLAYERS) == self.ui.spinBox_Quantity.value():
            self.ui.pushButton_Next.setStyleSheet(THEME.mainButton_Style)

    def reset_entries(self):
        """Resets all entries"""
        global PLAYERS
        PLAYERS = []
        self.ui.frame_PlayerEntry.show()
        self.ui.frame_PlayerQuantity.show()
        self.ui.pushButton_Next.setStyleSheet(THEME.passiveButton_Style)
        self.ui.label_Result.hide()

        self.ui.spinBox_Quantity.setValue(2)
        self.ui.lineEdit_EnterName.clear()
        self.player_counter = len(PLAYERS) + 1
        self.prepare_game()


# ### Third 'Screen' ### #
class UiMainGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.titel = "UNO - The Game"
        self.icon = f'{THEME.filePath}icon.png'

        self.player = PLAYERS[0]
        self.number_of_shown_card_set = 1
        self.called_uno = False
        self.can_choose_a_card = True   # Only changes if color for wild card needs to be chosen

        self.pre_start()
        self.start_turn()

        # ## BUTTON AKTIONEN ## #
        self.ui.pushButton_Draw_Talon.clicked.connect(self.draw_card_from_Draw_Talon)
        self.ui.pushButton_skip.clicked.connect(self.player_skips)
        self.ui.pushButton_uno.clicked.connect(self.uno_button_clicked)

        self.ui.pushButton_next_card_set.clicked.connect(self.move_to_rest_of_hand)
        self.ui.pushButton_last_card_set.clicked.connect(self.move_back_to_last_of_hand)

        self.ui.pushButton_wild_blue.clicked.connect(self.selected_blue)
        self.ui.pushButton_wild_green.clicked.connect(self.selected_green)
        self.ui.pushButton_wild_yellow.clicked.connect(self.selected_yellow)
        self.ui.pushButton_wild_red.clicked.connect(self.selected_red)

    # ##### GUI ##### #
    # ##### Front-End Methods (GUI) ##### #
    def ui_preset(self):
        """sets the default Game GUI"""
        self.set_theme()
        self.setWindowTitle(self.titel)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.hide_unnecessary()

    def setup_player_ui(self, hand_cards):
        self.ui.label_current_player.setText(self.player.name)
        self.adjust_color_to_player_color()
        self.adjust_frame_player_hand(quantity=len(hand_cards))
        self.position_and_update_cards(hand_cards[:12])

    # ### Methods that hide and show stuff ### #
    def hide_unnecessary(self):
        """hides all elements only needed in special cases, e.g. uno-Button"""
        self.ui.frame_skip.hide()
        self.ui.frame_wild_color_choice.hide()
        self.ui.pushButton_uno.hide()
        self.ui.pushButton_next_card_set.hide()
        self.ui.pushButton_last_card_set.hide()

    def show_necessary(self):
        """shows Buttons, that depend on specific settings when they are needed"""
        length = len(self.player.hand)

        # hide show uno
        if length == 2:
            self.ui.pushButton_uno.show()
        else:
            self.ui.pushButton_uno.hide()

        # hide show next_card_set
        if length > 12 and self.number_of_shown_card_set == 1:
            self.ui.pushButton_next_card_set.show()
        elif length > 24 and self.number_of_shown_card_set == (1 or 2):
            self.ui.pushButton_next_card_set.show()
        else:
            self.ui.pushButton_next_card_set.hide()

        # hide show last_card_set
        if self.number_of_shown_card_set > 1:
            self.ui.pushButton_last_card_set.show()
        else:
            self.ui.pushButton_last_card_set.hide()

        """if length > 12:                         # show next Set button if needed
            if self.number_of_shown_card_set == 2 and length <= 24:
                self.ui.pushButton_next_card_set.hide()
            elif self.number_of_shown_card_set == 3:
                self.ui.pushButton_next_card_set.hide()
            else:
                self.ui.pushButton_next_card_set.show()
        else:
            self.ui.pushButton_next_card_set.hide()"""

    def hide_player_cards(self):
        for card in self.player.hand:
            card.pushButtonKarte.hide()

    # ### Methods that adjust or set properties ### #
    def set_theme(self):
        """adjust all GUI parts to the currently selected Theme"""
        self.ui.frame_background.setStyleSheet(THEME.gameWindowBackground_Style)
        self.ui.frame_talons.setStyleSheet(THEME.transparentBackground)
        self.ui.frame_player_hand.setStyleSheet(THEME.transparentBackground)

        self.ui.frame_uno_name.setStyleSheet(THEME.transparentBackground)
        self.ui.pushButton_uno.setStyleSheet(THEME.uno_SkipButton_Style)

        self.ui.frame_skip.setStyleSheet(THEME.transparentBackground)
        self.ui.pushButton_skip.setStyleSheet(THEME.uno_SkipButton_Style)

        self.ui.frame_wild_color_choice.setStyleSheet(THEME.transparentBackground)
        self.ui.pushButton_wild_blue.setStyleSheet(THEME.blueChoice_Style)
        self.ui.pushButton_wild_green.setStyleSheet(THEME.greenChoice_Style)
        self.ui.pushButton_wild_yellow.setStyleSheet(THEME.yellowChoice_Style)
        self.ui.pushButton_wild_red.setStyleSheet(THEME.redChoice_Style)

        self.ui.frame_left_last.setStyleSheet(THEME.transparentBackground)
        self.ui.frame_right_next.setStyleSheet(THEME.transparentBackground)

    def set_play_talon_style(self):
        """Adjusts the GUI of pushButton Play-Talon to current upcard"""
        self.ui.pushButton_Play_Talon.setStyleSheet(PLAY_TALON[0].pushButtonKarte.styleSheet())

    def set_draw_talon_style(self):
        """Adjust Draw-Button Style to highlight it, if the player has to draw a card

        if none of the hand-card is playable the player has to draw"""
        if not self.player.validate_all_cards(PLAY_TALON[0]):
            self.ui.pushButton_Draw_Talon.setStyleSheet(THEME.highlightedDrawTalon_Style)
            self.ui.label_current_player.setText(f"{self.player.name}, du musst ziehen.")
        else:
            self.ui.pushButton_Draw_Talon.setStyleSheet(THEME.normalDrawTalon_Style)

    def adjust_color_to_player_color(self):
        """set the frame and name-label color to the players color"""
        color = self.player.color
        self.ui.frame_player_hand.setStyleSheet("QFrame {\n"
                                                "background-color: rgba(255, 255, 255, 0);\n"
                                                f"    border: 7px solid  {color};\n"
                                                "}")
        self.ui.label_current_player.setStyleSheet(f"color: {color}")

    def adjust_frame_player_hand(self, quantity):
        """adjust the frame size depending on the number of cards

        up to 6 Card in one row, max. to rows"""
        rand = 2 * size.rand

        if quantity <= 6:
            width = rand + quantity * size.card_width + (quantity - 1) * size.space
            height = rand + size.card_height
        else:
            width = rand + 6 * size.card_width + 5 * size.space
            height = rand + 2 * size.card_height + 1 * size.space

        self.ui.frame_player_hand.setMinimumSize(int(width), height)

    def position_and_update_cards(self, cards):
        """gives every card it's GUI Position as well as updating index and playable"""
        x = size.rand
        y = size.rand

        for index, card in enumerate(cards):
            card.index = index
            card.validate_card(PLAY_TALON[0])

            card.change_border()
            card.change_geometry(x, y)
            card.pushButtonKarte.show()

            x += size.card_w_and_space
            if index == 5:
                y += size.card_h_and_space
                x = size.rand

    # ##### Back-End Methods (None-GUI/No direct relation) ##### #
    # ##### TURN ##### #
    # ### Methods preparing the game ### #
    def pre_start(self):
        """prepares the Game

        generates cards, distributes them, sets upcard and sets default GUI settings"""
        self.generate_cards()
        for spieler, _ in enumerate(PLAYERS):  # distributing cards
            PLAYERS[spieler].draw_card(7)

        self.turn_over_upcard()
        self.ui_preset()

    def turn_over_upcard(self):
        """defines first upcard

        takes first card of Draw-Talon and appends it to Play-Talon
        takes second card if first card is a wild cards
        adjust the style of Button Play-Talon"""
        if "Black" in DRAW_TALON[0].color:
            PLAY_TALON.append(DRAW_TALON.pop(1))
        else:
            PLAY_TALON.append(DRAW_TALON.pop(0))
        self.set_play_talon_style()

    # ### Methods controlling a players turn ### #
    def start_turn(self):
        self.player = PLAYERS[0]
        current_hand = self.player.hand
        self.number_of_shown_card_set = 1
        self.show_necessary()

        self.setup_player_ui(hand_cards=current_hand)
        self.set_draw_talon_style()

        print("~ Setup completed ~")
        print(f"Karten von {PLAYERS[0].name} | {len(current_hand)}")

    def discard_chosen_card(self, index: int):
        """hides players cards, moves chosen card from player.hand to new upcard

        can_choose_a_card is only False if wild-card color-choice needs to be done"""
        if self.can_choose_a_card:
            self.hide_player_cards()

            PLAY_TALON.insert(0, self.player.hand.pop(index))

            PLAY_TALON[0].playable = False
            PLAY_TALON[0].change_border()

            self.process_chosen_card()

    def process_chosen_card(self):
        """checks consequences of the chosen card

        checks whether the player has won
        check if chosen card is a special or wild-card
            calls a function to execute the cards action"""
        global VICTOR
        self.set_draw_talon_style()
        self.set_play_talon_style()

        if self.player.player_finished():
            VICTOR = self.player.name  # ### maybe in spiel ende
            self.game_over()
        else:
            if PLAY_TALON[0].color == "Black":
                self.wild_card_action(card=PLAY_TALON[0])
            else:
                self.check_uno()

                if PLAY_TALON[0].value not in VALUES:
                    self.special_card_action(card=PLAY_TALON[0])
                else:
                    self.play_order()

                self.end_turn()

    def draw_card_from_Draw_Talon(self):
        if self.can_choose_a_card:
            self.hide_player_cards()
            self.player.draw_card(1)

            self.show_necessary()

            if self.number_of_shown_card_set == 2:
                cards = self.player.hand[12:]
            else:
                cards = self.player.hand[:12]

            self.setup_player_ui(hand_cards=cards)
            self.ui.frame_skip.show()

    def end_turn(self):
        """check for refill, resets ui, start_turn for the next player"""
        global VICTOR
        if not self.ein_spieler_fertig():
            self.refill()
            self.ui.pushButton_uno.setStyleSheet(THEME.uno_SkipButton_Style)
            self.hide_unnecessary()
            self.start_turn()
        else:
            VICTOR = "Jemand hat gewonnen."
            self.game_over()

    def game_over(self):
        """opens the Game-Over Window"""
        self.ende = UiGameOverWindow()
        self.ende.show()

        self.close()

    # ### Methods call in a turn ### #
    def check_uno(self):
        """checks if player has called uno

        player only needs to call uno before he discards his
        second last card"""
        if len(self.player.hand) == 1:
            if self.called_uno:
                self.ui.label_current_player.setText("Spieler hat UNO")
                # self.called_uno = False
            else:
                self.player.draw_card(2)
            self.called_uno = False

    def play_order(self):
        """configures player-order by moving the first player to the end"""
        PLAYERS.append(PLAYERS.pop(0))

    def refill(self):
        """refills Draw_Talon if only 4 or less cards in it"""
        if len(DRAW_TALON) <= 4:
            self.generate_cards()

    def ein_spieler_fertig(self):
        """Checks whether on player has won

        check by checking every player and appending the result to a list
        if Ture in that list one player has won"""
        ende = []
        for spieler, _ in enumerate(PLAYERS):
            ende.append(PLAYERS[spieler].player_finished)
        return True in ende

    # ##### CARDS ##### #
    # ### Methods generating cards ### #
    def generate_cards(self):
        """generates the hole deck and shuffles it"""
        global DRAW_TALON
        DRAW_TALON.extend(self.normal_cards())
        DRAW_TALON.extend(self.special_cards())
        DRAW_TALON.extend(self.wild_cards())
        random.shuffle(DRAW_TALON)

    def normal_cards(self) -> list:
        """generates cards on basis of @COLORS und @VALUES, every card exists 4 times"""
        global COLORS, VALUES
        normal_cards = []
        for rate in range(4):
            for color in COLORS:
                for value in VALUES:
                    normal_cards.append(UiCard(color, value, display=self.ui.frame_player_hand))
        return normal_cards

    def special_cards(self) -> list:
        """generates special cards with global @COLORS and list special"""
        global COLORS
        special = ["+2", "Skip", "Change_Direction"]
        special_cards = []
        for rate in range(4):
            for color in COLORS:
                for value in special:
                    special_cards.append(UiCard(color, value, display=self.ui.frame_player_hand))
        return special_cards

    def wild_cards(self) -> list:
        """creates +4 and 'Choice' as wild cards"""
        wild_cards = []
        for rate in range(4):
            wild_cards.append(UiCard("Black", "+4",
                                     display=self.ui.frame_player_hand,
                                     playable=True))
            wild_cards.append(UiCard("Black", "Choice",
                                     display=self.ui.frame_player_hand,
                                     playable=True))
        return wild_cards

    # ### Card actions ### #
    def special_card_action(self, card):
        """executes actions based on the special card played

        if +2: next player in line draws two
        if skip: next player in line gets moved to the end of player order as well
        if change_direction: player order gets reversed"""
        global PLAYERS
        if card.value == "+2":  # später noch "möchtest" du zwei Karten ziehen oder eine +2 oder +4 ablegen
            PLAYERS[1].draw_card(2)
            self.play_order()
        elif card.value == "Skip":
            self.play_order()
            self.play_order()
        else:
            if len(PLAYERS) == 2:
                self.play_order()
                self.play_order()
            else:
                PLAYERS = PLAYERS[::-1]  # Slicing

    def wild_card_action(self, card):
        """shows the players cards and buttons to choose a color"""
        global PLAYERS
        if card.value == "+4":
            PLAYERS[1].draw_card(4)

        self.ui.frame_wild_color_choice.show()
        self.called_uno = False

        self.setup_player_ui(hand_cards=self.player.hand)

    def selected_blue(self):
        """tells end_wild_card_action that color "Blue" has been chosen"""
        self.end_wild_card_action(color="Blue")

    def selected_green(self):
        """tells end_wild_card_action that color "Green" has been chosen"""
        self.end_wild_card_action(color="Green")

    def selected_yellow(self):
        """tells end_wild_card_action that color "Yellow" has been chosen"""
        self.end_wild_card_action(color="Yellow")

    def selected_red(self):
        """tells end_wild_card_action that color "Red" has been chosen"""
        self.end_wild_card_action(color="Red")

    def end_wild_card_action(self, color):
        PLAY_TALON[0].color = color
        PLAY_TALON[0].wild_card_chosen_color_style()
        self.set_play_talon_style()

        self.hide_player_cards()
        # self.ui.frame_wild_color_choice.hide()  # ## necessary
        self.can_choose_a_card = True

        self.check_uno()
        self.play_order()
        self.end_turn()

    # ##### Button calls ##### #
    def player_skips(self):
        """ hides player cards and finishes the turn

        player choose not to play a card nor to draw again"""
        self.hide_player_cards()
        self.play_order()
        self.end_turn()

    def uno_button_clicked(self):
        """saves if player clicked the uno-Button and changes the stylesheet"""
        self.called_uno = True
        self.ui.pushButton_uno.setStyleSheet(THEME.unoButtonClicked_Style)
        print("Spieler hat UNO gedrückt")

    def move_to_rest_of_hand(self):
        """shows cards whit index over 11 as 12 cards is maximum of shown cards

        if the player has more than 12 Cards new cards are set in a "new" frame
        which can be seen by clicking the Button"""
        self.hide_player_cards()

        if self.number_of_shown_card_set == 1:
            self.number_of_shown_card_set = 2
            spare_cards = self.player.hand[12:24]  # ## test [12:24]
            self.show_necessary()
        else:
            self.number_of_shown_card_set = 3
            spare_cards = self.player.hand[24:]
            self.show_necessary()

        self.adjust_frame_player_hand(quantity=len(spare_cards))
        self.position_and_update_cards(cards=spare_cards)

        self.ui.pushButton_last_card_set.show()

    def move_back_to_last_of_hand(self):
        """shows cards whit index smaller as currently shown

        if the player has more than 12 Cards new cards are set in a "new" frame
        clicking the last_set Button shows the previous cards"""
        self.hide_player_cards()

        if self.number_of_shown_card_set == 2:
            self.number_of_shown_card_set = 1
            spare_cards = self.player.hand[:12]  # ## test [12:24]
            self.show_necessary()
        else:  # self.number... = 3
            self.number_of_shown_card_set = 3
            spare_cards = self.player.hand[12:24]
            self.show_necessary()

        self.adjust_frame_player_hand(quantity=len(spare_cards))
        self.position_and_update_cards(cards=spare_cards)


class UiCard(QtWidgets.QWidget):
    """creates a custom Widget to display the cards"""
    def __init__(self, color, value, display, playable=False, index=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display = display
        self.pushButtonKarte = QtWidgets.QPushButton(display)

        # ### Card Information ### #
        self.color = color
        self.value = value
        self.playable = playable
        self.index = index

        # ### Default GUI Settings ### #
        self.background_color = THEME.black
        self.border_color = THEME.normalBorderColor
        # self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/default.png"
        self.image = f"{THEME.filePath}default.png"
        self.x_koordinate = size.rand
        self.y_koordinate = size.rand

        self.setup_card_ui()

        # ### BUTTON CONNECT ### #
        self.pushButtonKarte.clicked.connect(self.card_chosen)

    # ##### Front-End Methods (GUI-related) ##### #
    def setup_card_ui(self):
        """adjusts the card Values related to the UI and sets up the Button widget"""
        self.change_background()
        self.change_image()

        self.pushButtonKarte.setGeometry(QtCore.QRect(self.x_koordinate, self.y_koordinate, 141, 233))
        self.set_card_style()
        self.pushButtonKarte.setObjectName("pushButtonKarte")

        self.pushButtonKarte.hide()

    def change_background(self):
        """changes the default background color, which represents the card color, according to the theme"""
        if self.color == "Blue":
            self.background_color = THEME.blue
        elif self.color == "Green":
            self.background_color = THEME.green
        elif self.color == "Yellow":
            self.background_color = THEME.yellow
        elif self.color == "Red":
            self.background_color = THEME.red
        else:
            self.background_color = THEME.black

    def change_image(self):
        """changes the image representing the card Value to the relative picture"""
        # ##pfad = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"
        self.image = f"{THEME.filePath}{self.value}.png"

    def change_border(self):
        """changes the card border to highlight playable cards"""
        if self.playable:
            self.border_color = THEME.playableBorderColor
        else:
            self.border_color = THEME.normalBorderColor
        self.set_card_style()

    def set_card_style(self):
        """Adjust the Button Stylesheets based on the values background-color, border_color and image"""
        self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                           f"    background-color: {self.background_color};\n"
                                           "    border-radius: 15px;\n"
                                           "    border-width: 3px;\n"
                                           "    border-style: solid;\n"
                                           f"    border-color: {self.border_color};\n"
                                           f"    image: url({self.image});\n"
                                           "}")

    def wild_card_chosen_color_style(self):
        """Adjusts the Card Stylesheet so the chosen color is displayed"""
        self.change_background()
        self.border_color = THEME.normalBorderColor
        self.set_card_style()

    def change_geometry(self, x: int, y: int):
        """Changes the absolute Geometry based on the given parameters

        :parameter x -> int
        :parameter y -> int"""
        self.x_koordinate = x
        self.y_koordinate = y
        self.pushButtonKarte.setGeometry(QtCore.QRect(self.x_koordinate, self.y_koordinate, 141, 233))

    # ##### Back-End Methods (None-GUI/No direct relation) ##### #
    def validate_card(self, comparing_card):
        """compares card with a given and changes playable accordingly

        a card is playable when: the card is a wild card(color="Black")
         the colors  oder values match
        if current upcard = wild card only the color needs to be checked"""
        skip_value = bool(comparing_card.value == "+4" or comparing_card.value == "Choice")

        if self.color == "Black":
            self.playable = True
        elif self.color == comparing_card.color:
            self.playable = True
        elif not skip_value:
            if self.value == comparing_card.value:
                self.playable = True
            else:
                self.playable = False
        else:
            self.playable = False

    # ##### Button calls ##### #
    def card_chosen(self):
        """tells the Game which card has been chosen"""
        print(f" Kartenindex: {self.index}")  # Test:
        if self.playable:
            window.game_window.discard_chosen_card(self.index)


class Player:
    def __init__(self, name, hand_cards, player_color):
        self.name = name
        self.hand = hand_cards
        self.color = player_color

    def draw_card(self, quantity=7):
        """draws as many cars as given from global @DRAW_TALON

        :parameter quantity -> int
        pops the first element of Draw_Talon and adds it to hand_cards"""
        global DRAW_TALON
        drawn = []
        for draw in range(quantity):
            drawn.append(DRAW_TALON.pop(0))
        self.hand.extend(drawn)

    def validate_all_cards(self, upcard: UiCard):
        """checks if the player has any card which is playable

        :parameter upcard -> object of Cards
        :return -> bool"""
        for card in self.hand:
            card.validate_card(upcard)
            if card.playable:
                return True
        return False

    def player_finished(self):
        """check whether the player has won (has no cards)

        :return ->bool"""
        return bool(len(self.hand) == 0)

    def pop(self, index: int):
        card = self.hand.pop(index)
        return card


# ### Forth 'Screen' ### #
class UiGameOverWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MWinEnde()
        self.ui.setupUi(self)

        self.titel = "UNO - The Game"
        self.icon = f'{THEME.filePath}icon.png'

        self.setup_GUI()

        # ##### BUTTON CONNECT ##### #
        self.ui.pushButton_PlayAgain.clicked.connect(self.play_again)
        self.ui.pushButton_Menu.clicked.connect(self.new_game)
        self.ui.pushButton_Quit.clicked.connect(self.close)

    # ##### Front-End Methods (GUI) ##### #
    def setup_GUI(self):
        """sets all parts of the GUI"""
        self.set_theme()
        self.setWindowTitle(self.titel)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.ui.label_Victor.setText(f"<strong>{VICTOR}</strong> hat gewonnen")

    def set_theme(self):
        """adjust all GUI parts to the currently selected Theme"""
        self.ui.frame_Background.setStyleSheet(THEME.gameWindowBackground_Style)
        self.ui.label_gameOverMessage.setStyleSheet(THEME.gameOverMassage_Style)
        self.ui.label_Victor.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                           f"color: {PLAYERS[0].color};")

        self.ui.frame_gameOverMenu.setStyleSheet(THEME.transparentBackground)
        self.ui.pushButton_PlayAgain.setStyleSheet(THEME.playAgainButton_Style)
        self.ui.pushButton_Menu.setStyleSheet(THEME.menu_QuitButton_Style)
        self.ui.pushButton_Quit.setStyleSheet(THEME.menu_QuitButton_Style)

    # ##### Button calls ##### #
    def play_again(self):
        """lunches an new Game with existing players"""
        global PLAYERS, DRAW_TALON, PLAY_TALON
        for player in PLAYERS:
            player.hand = []
        DRAW_TALON = []
        PLAY_TALON = []
        window.start_game()

        self.close()

    def new_game(self):
        """opens the entry menu to start a game with new players"""
        global DRAW_TALON, PLAY_TALON, PLAYERS
        window.reset_entries()
        DRAW_TALON = []
        PLAY_TALON = []
        window.show()

        self.close()

    def quit(self):
        """ends the Application"""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UiStartWindow()
    window.show()
    sys.exit(app.exec_())
