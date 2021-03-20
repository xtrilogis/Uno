import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QColorDialog, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

from ui_prepare_screen import *
from ui_main_game_window import *
from ui_game_over_screen import *

from theme_development import developer
from theme_dark_blue import dark_blue
from theme_class import default

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


# ### First + Second 'Screen' ### #
class UiStartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MWinPrepare()
        self.ui.setupUi(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.player_counter = len(PLAYERS) + 1

        # ### SETUP UI ### #
        self.setTheme()
        self.setUp_start_screen()

        self.prepare_game()

        # ### BUTTON CONNECT ### #
        self.ui.pushButton_Start.clicked.connect(self.startPushed)
        self.ui.pushButton_Close.clicked.connect(self.close)

        self.ui.pushButton_SelectColor.clicked.connect(self.showColorDialog)
        self.ui.pushButton_ReturnEntry.clicked.connect(self.process_name_entry)
        self.ui.pushButton_Next.clicked.connect(self.next_clicked)

        self.ui.pushButton_Reset.clicked.connect(self.reset_entries)
        self.ui.pushButton_Theme.clicked.connect(self.change_theme)

    # ##### Front-End Methods (GUI) ##### #
    def setTheme(self):
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

    def setUp_start_screen(self):
        """sets Settings for the first screen to appear when Programm executed"""
        self.hide_prepare_screen()
        self.setDropShadow()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)       # removes window control bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   # transparent background behind frame

    def setDropShadow(self):
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
        PLAYERS.append(Spieler(name=self.ui.lineEdit_EnterName.text(),
                               handkarten=[],
                               farbe=THEME.defaultPlayerColors[0]))
        THEME.defaultPlayerColors.append(THEME.defaultPlayerColors.pop(0))
        self.ui.lineEdit_EnterName.clear()

    # ##### Button calls ##### #
    def startPushed(self):
        """switches from start-screen to prepare_screen"""
        self.hide_start_screen()
        self.show_prepare_screen()

    def showColorDialog(self):
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
            self.game_window = UiMainGameWindow()
            self.game_window.show()

            self.close()
        else:
            self.ui.frame_PlayerQuantity.show()
            self.ui.frame_PlayerEntry.show()
            self.ui.label_Result.show()

            self.ui.label_Entry.setText(f"Spieler {self.player_counter}:")
            if len(PLAYERS) == 0:
                self.ui.label_Result.setText(f"Zu wenig Spieler! Noch kein Spielername eingegeben.")
            else:
                self.ui.label_Result.setText(f"Zu wenig Spieler! Nur {len(PLAYERS)} Spielername(n) eingegeben.")

    def change_theme(self):
        """changes the Theme when Button is clicked"""
        global THEME
        if THEME == dark_blue:
            THEME = developer
        if THEME == developer:
            THEME = default
        if THEME == default:
            THEME = dark_blue
        self.setTheme()

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

        self.ui.spinBox_Quantity.setValue(2)
        self.player_counter = len(PLAYERS) + 1
        self.prepare_game()


# ### Third 'Screen' ### #
class UiMainGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setTheme()
        # später im Prepare-screen
        # spieler_preset()

        self.pfad = THEME.filePath  # ## to-do

        # Variablen
        self.titel = "UNO - The Game"
        self.icon = f'{self.pfad}icon.png'

        # ?? self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.rand = 10
        self.zwischen = 3
        self.karten_w = 141
        self.karten_h = 233

        self.aktiviert = True
        self.uno_gesagt = False
        self.farbe = None
        self.hFrame = 1

        self.player = PLAYERS[0]
        # Basic Ui Änderungen
        # set
        self.setWindowTitle(self.titel)
        self.setWindowIcon(QtGui.QIcon(self.icon))

        # hide
        self.hideUnnecessary()

        # ## BUTTON AKTIONEN ## #
        self.ui.pushButtonDraw_T.clicked.connect(self.nachziehen)
        self.ui.pushButtonWeiter.clicked.connect(self.passen)
        self.ui.pushButtonUNO.clicked.connect(self.UNOClicked)

        self.ui.pushButtonNextCardSet.clicked.connect(self.move2terFrame)
        self.ui.pushButtonLastCardSet.clicked.connect(self.moveBack1terFrame)

        self.ui.pushButtonBlau.clicked.connect(self.colorBlue)
        self.ui.pushButtonGruen.clicked.connect(self.colorGreen)
        self.ui.pushButtonGelb.clicked.connect(self.colorYellow)
        self.ui.pushButtoRot.clicked.connect(self.colorRed)

        # Funktionsaufrufe
        self.preStart()
        self.setUpUi()

        #self.show()

    def setTheme(self):
        # Frames
        self.ui.frameHintergrund.setStyleSheet(THEME.gameWindowBackground_Style)
        self.ui.frame_Stapel.setStyleSheet(THEME.transparentBackground)
        self.ui.frame_Handkarten.setStyleSheet(THEME.transparentBackground)
        self.ui.framePassen.setStyleSheet(THEME.transparentBackground)
        self.ui.frameFarbwahl.setStyleSheet(THEME.transparentBackground)
        self.ui.frameLeftLast.setStyleSheet(THEME.transparentBackground)
        self.ui.frameRightNext.setStyleSheet(THEME.transparentBackground)
        self.ui.frameTop.setStyleSheet(THEME.transparentBackground)

        # weiter zu Skip
        self.ui.pushButtonWeiter.setStyleSheet(THEME.uno_SkipButton_Style)
        self.ui.pushButtonUNO.setStyleSheet(THEME.uno_SkipButton_Style)
        self.ui.pushButtonBlau.setStyleSheet(THEME.blueChoice_Style)
        self.ui.pushButtonGruen.setStyleSheet(THEME.greenChoice_Style)
        self.ui.pushButtonGelb.setStyleSheet(THEME.yellowChoice_Style)
        self.ui.pushButtoRot.setStyleSheet(THEME.redChoice_Style)

        # self.ui.LabelSpielername.setStyleSheet(THEME.aktuellerSp)

    def preStart(self):
        self.generate_cards()

        # handkarten verteilen
        for spieler in range(len(PLAYERS)):
            PLAYERS[spieler].draw_card(7)

    def setUpUi(self):
        self.player = PLAYERS[0]
        self.handkarten = self.player.handkarten
        self.kartenanzahl = len(self.handkarten)
        self.frame_farbe = self.player.farbe

        self.hFrame = 1

        self.ui.LabelSpielername.setText(self.player.name)

        # Startkarte aufdecken
        self.setPlayTalon()

        # Wenn UNO möglich --> UNO Button erscheint
        if self.kartenanzahl == 2:
            self.ui.pushButtonUNO.show()

        self.setUpHandkarten()
        print("~ Setup completed ~")
        print(f"Karten von {PLAYERS[0].name} | {self.kartenanzahl}")

        # Prüft 'muss ziehen'
        self.setDrawTalon()

    # ### UI SETUP - STAPEL + HANDKARTENKARTEN UI ### #
    def setPlayTalon(self):
        """deckt die erste Spielkarte auf

        fügt die erste Karte vom Zugstapel dem Spielstapel hinzu
        falls die erste Karte ein Joker ist, wird die nächste Karte als oberste Karte genommen
        setzt das StyleSheet vom PLY_TALON - Button auf das der obersten Karte
        """
        if "Black" in DRAW_TALON[0].farbe:
            PLAY_TALON.append(DRAW_TALON.pop(1))
            self.ui.pushButton_Play_T.setStyleSheet(PLAY_TALON[0].pushButtonKarte.styleSheet())
        else:
            PLAY_TALON.append(DRAW_TALON.pop(0))
            self.ui.pushButton_Play_T.setStyleSheet(PLAY_TALON[0].pushButtonKarte.styleSheet())

    def setUpHandkarten(self):
        # SetUp Handkarten - Frame
        self.setFrameSize(self.kartenanzahl)
        self.setFrameBorder()

        # Switch Button
        if self.kartenanzahl > 12:
            self.ui.pushButtonNextCardSet.show()

        # SetUp Handkarten - Karten
        self.setUpCards(self.handkarten[0:12])

    def setFrameSize(self, kartenanzahl):
        """Setzt die Größe des Handkarten Frame entsprechend der Kartenanzahl

        bis 6 Karten eine Reihe a max. 6 Karten
        bis 12 Karten zwei Reihen a max. 6 Karten"""
        rand = 2 * self.rand

        if kartenanzahl <= 6:
            width = rand + kartenanzahl * self.karten_w + (kartenanzahl - 1) * self.zwischen
            height = rand + self.karten_h
        else:
            width = rand + 6 * self.karten_w + 5 * self.zwischen
            height = rand + 2 * self.karten_h + 1 * self.zwischen

        self.ui.frame_Handkarten.setMinimumSize(int(width), height)

    def setFrameBorder(self):
        self.ui.frame_Handkarten.setStyleSheet("QFrame {\n"
                                               "background-color: rgba(255, 255, 255, 0);\n"
                                               f"    border: 7px solid  {self.frame_farbe};\n"
                                               "}")
        self.ui.LabelSpielername.setStyleSheet(f"color: {self.frame_farbe}")

    def setUpCards(self, karten):
        """vergibt an jede Karte ihre Position

        jede Karte bekommt einen Index zugeteilt
        erste Karte ist (7 | 7), nächste (7 + Kartenbreite + Abstand zwischen karten | 7), usw.
        wenn die maximal Zahl für eine Reihe voll ist wird der Y wert um eine Kartenhöhe mit Abstand erweitert
        und X auf 7 zurückgesetzt"""
        x = self.rand
        y = self.rand
        counter = 0
        kartenanzahl = len(karten)

        if kartenanzahl == 1:
            self.setCardValues(self.handkarten[0], counter, self.rand, self.rand)
            self.handkarten[0].pushButtonKarte.show()
        else:
            for karte in karten:
                karte.index = counter
                self.setCardValues(karte, counter, x, y)

                x += self.karten_w + self.zwischen
                if counter == 5:
                    y += self.karten_h + self.zwischen
                    x = self.rand
                counter += 1

                # Karten anzeigen
                # print(karte.farbe, karte.wert, karte.index)
                karte.pushButtonKarte.show()

        print("\n Karten positioniert")
        print(f"Counter: {counter}")

    def setCardValues(self, karte, counter: int, x, y):
        karte.index = counter
        karte.validate_card(PLAY_TALON[0])
        karte.changeBorder()
        karte.changeGeometry(x, y)

    def setDrawTalon(self):
        """Passt UI an fall Spieler ziehen muss

        Wenn der Spieler keine Karte spielen kann wir das Label geändert und DRAW_Talon bekommt einen Rahmen"""
        if not self.player.validate_all_cards(PLAY_TALON[0]):
            self.ui.pushButtonDraw_T.setStyleSheet(THEME.highlightedDrawTalon_Style)
            self.ui.LabelSpielername.setText(f"{self.player.name}, du musst ziehen.")
        else:
            self.ui.pushButtonDraw_T.setStyleSheet(THEME.normalDrawTalon_Style)

    # # Zug ##############
    def playCard(self, index: int):
        """ wird aufgerufen, wenn eine Karte ausgewählt wurde

        aktiviert normalerweise Ture esseiden es muss eine Farbe für den Joker gewählt werden
        setzt das Stylesheet von pushButton auf das von PushButtonKarte"""
        if self.aktiviert:
            # Spielerkarten verstecken
            self.karten_hide(self.player.handkarten)

            # Karte ablegen: von handkarten auf PLAY_TALON
            PLAY_TALON.insert(0, self.player.handkarten.pop(index))

            # Values für die UI
            PLAY_TALON[0].spielbar = False
            PLAY_TALON[0].changeBorder()

            self.cardAction()

    def cardAction(self):
        global VICTOR
        # ist Spieler fertig
        self.ui.pushButtonDraw_T.setStyleSheet(THEME.normalDrawTalon_Style)
        if self.player.spieler_fertig():
            VICTOR = self.player.name
            self.spielEnde()

        if "Black" == PLAY_TALON[0].farbe:
            self.joker_action(PLAY_TALON[0])
        else:
            # UNO gesagt?
            self.UNO()

            if PLAY_TALON[0].wert not in VALUES:
                self.sonder_action(PLAY_TALON[0])
            else:
                self.play_order()

            self.endTurn()

    def nachziehen(self):
        """ ähnlich wie playCard"""
        if self.aktiviert:
            print("Spieler zieht")
            # Spielerkarten verstecken
            self.karten_hide(self.handkarten)

            # 1 Karte ziehen
            self.player.draw_card(1)

            if len(self.handkarten) == 2:
                self.ui.pushButtonUNO.show()
            else:
                self.ui.pushButtonUNO.hide()

            if len(self.handkarten) > 12:
                self.ui.pushButtonNextCardSet.show()

            if self.hFrame == 2:
                self.ui.pushButtonNextCardSet.hide()
                self.ui.pushButtonLastCardSet.show()
                kartenanzahl = len(self.handkarten[12:])
                handkarten = self.handkarten[12:]
            else:
                kartenanzahl = len(self.handkarten)
                handkarten = self.handkarten
            # Frame neu anpassen
            self.setFrameSize(kartenanzahl)
            # neue Handkarten anzeigen
            self.setUpCards(handkarten[:12])

            # Button zug beenden, falls, Karte nicht gespielt werden will kann
            self.ui.framePassen.show()

    def endTurn(self):
        global VICTOR
        if not ein_spieler_fertig():
            self.refill()
            self.ui.pushButtonUNO.setStyleSheet(THEME.uno_SkipButton_Style)
            self.hideUnnecessary()
            self.setUpUi()
        else:
            VICTOR = self.player.name
            self.spielEnde()

    # ##
    # Button funktionen

    def passen(self):
        self.karten_hide(self.handkarten)
        self.play_order()
        self.endTurn()

    def UNOClicked(self):
        self.uno_gesagt = True
        self.ui.pushButtonUNO.setStyleSheet(THEME.unoButtonClicked_Style)
        print("Spieler hat UNO gedrückt")

    def move2terFrame(self):
        self.hideAllCards()
        kartenzahl = len(self.handkarten[12:])
        self.hFrame = 2

        self.setFrameSize(kartenzahl)
        self.setUpCards(self.handkarten[12:])

        if len(self.handkarten) <= 24:
            self.ui.pushButtonNextCardSet.hide()
        self.ui.pushButtonLastCardSet.show()

    def moveBack1terFrame(self):
        self.hideAllCards()
        kartenzahl = len(self.handkarten[0:12])
        self.hFrame = 2

        self.setFrameSize(kartenzahl)
        self.setUpCards(self.handkarten[0:12])

        self.ui.pushButtonLastCardSet.hide()
        self.ui.pushButtonNextCardSet.show()

    def colorBlue(self, text):
        print(text)
        self.farbe = "Blue"
        self.endJoker()

    def colorGreen(self):
        self.farbe = "Green"
        self.endJoker()

    def colorYellow(self):
        self.farbe = "Yellow"
        self.endJoker()

    def colorRed(self):
        self.farbe = "Red"
        self.endJoker()

    # ### *Kategoriename* ### # ? Prepetetive?
    def karten_show(self, karten):
        for karte in karten:
            karte.pushButtonKarte.show()

    def karten_hide(self, karten):
        for card in karten:
            card.pushButtonKarte.hide()

    def hideKarte(self, karte):
        karte.pushButtonKarte.hide()

    def hideAllCards(self):
        for player in PLAYERS:
            self.karten_hide(player.handkarten)

    def hideUnnecessary(self):
        self.ui.frameFarbwahl.hide()
        self.ui.pushButtonUNO.hide()
        self.ui.pushButtonNextCardSet.hide()
        self.ui.pushButtonLastCardSet.hide()
        self.ui.framePassen.hide()

    def UNO(self):
        if len(PLAYERS[0].handkarten) == 1:
            if self.uno_gesagt:
                self.ui.LabelSpielername.setText("Spieler hat UNO.")
                self.uno_gesagt = False
            else:
                self.player.draw_card(2)
                self.uno_gesagt = False
            # ## print(f"geprüft")

    def play_order(self):
        """fügt den aktuellen Spieler hinten an die Spielerreihenfolge an"""
        PLAYERS.append(PLAYERS.pop(0))
        return

    def refill(self):
        """füllt den Zieh-Stapel neu auf"""
        if len(DRAW_TALON) <= 4:
            self.generate_cards()
        return

    def spielEnde(self):
        self.ende = UiEndWindow()
        self.ende.show()

        self.close()

    # ## Aktionen ## #
    def sonder_action(self, karte):
        global PLAYERS
        if karte.wert == "+2":  # später noch "möchtest" du zwei Karten ziehen oder eine +2 oder +4 ablegen
            PLAYERS[1].draw_card(2)
            self.play_order()
        elif karte.wert == "Aussetzen":
            self.play_order()
            # print(f'Spieler {PLAYERS[0].name} muss aussetzen.')
            self.play_order()
        else:  # wert == "Richtungswechsel"
            if len(PLAYERS) == 2:
                self.play_order()
                self.play_order()
            else:
                PLAYERS = PLAYERS[::-1]  # Slicing
            # print("Richtung gewechselt")
        return

    def joker_action(self, karte):
        global PLAYERS
        if karte.wert == "+4":
            # print(f"{PLAYERS[1].name} muss 4 Karten ziehen \n--------")
            PLAYERS[1].draw_card(4)

        self.ui.frameFarbwahl.show()
        self.aktiviert = False
        self.ui.pushButton_Play_T.setStyleSheet(PLAY_TALON[0].pushButtonKarte.styleSheet())

        self.setFrameSize(len(self.handkarten))
        self.setUpCards(self.handkarten)

    def endJoker(self):
        PLAY_TALON[0].farbe = self.farbe
        PLAY_TALON[0].jokerStyle()
        self.ui.pushButton_Play_T.setStyleSheet(PLAY_TALON[0].pushButtonKarte.styleSheet())

        self.karten_hide(self.handkarten)
        self.ui.frameFarbwahl.hide()
        self.aktiviert = True

        # Zugbeenden
        self.UNO()
        self.play_order()
        self.endTurn()

    # # Funktionen sortiert unf "fertig" ##
    # ### KARTEN ERSTELLEN ### #

    def generate_cards(self):
        global DRAW_TALON
        DRAW_TALON.extend(self.normal_cards())
        DRAW_TALON.extend(self.special_cards())
        DRAW_TALON.extend(self.joker_cards())
        random.shuffle(DRAW_TALON)

    def normal_cards(self) -> list:
        """generiert die normalen Karten als Klasse aus global @COLORS und @VALUES, jede Karte gibt es viermal"""
        global COLORS, VALUES
        karten = []
        for i in range(4):
            for color in COLORS:
                for value in VALUES:
                    karten.append(UiKarten(color, value, spielbar=False, fenster=self.ui.frame_Handkarten, index=None))
        return karten

    def special_cards(self) -> list:
        """erstellt Sonder-Karten +2, Aussetzen, Richtungswechsel, benutzt global constant @COLORS"""
        global COLORS
        special = ["+2", "Aussetzen", "Richtungswechsel"]
        karten = []
        for i in range(4):
            for color in COLORS:
                for value in special:
                    karten.append(UiKarten(color, value, spielbar=False, fenster=self.ui.frame_Handkarten, index=None))
        return karten

    def joker_cards(self) -> list:
        """ erstellt Joker_Karten +4 und 'Wunsch', jede Karte gibt es vier mal"""
        karten = []
        for i in range(4):
            karten.append(UiKarten("Black", "+4", spielbar=True, fenster=self.ui.frame_Handkarten, index=None))
            karten.append(UiKarten("Black", "Wunsch", spielbar=True, fenster=self.ui.frame_Handkarten, index=None))
        return karten


# ### Forth 'Screen' ### #
class UiKarten(QtWidgets.QWidget):

    def __init__(self, farbe, wert, spielbar, fenster, index, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fenster = fenster
        self.pushButtonKarte = QtWidgets.QPushButton(fenster)

        # Informationen
        self.farbe = farbe
        self.wert = wert
        self.spielbar = spielbar
        self.index = index

        # Style
        # ## Basic Colors
        self.background_color = "rgb(200, 50, 192)"
        self.border_color = THEME.normalBorderColor

        # ### Theme.filepath
        # self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/default.png"
        self.image = f"{THEME.filePath}default.png"
        self.xKoordinate = 7
        self.yKoordinate = 7

        # ## Funktionsaufrufe
        self.changeBackground()
        self.changeImage()

        self.pushButtonKarte.setGeometry(QtCore.QRect(self.xKoordinate, self.yKoordinate, 141, 233))
        # self.pushButtonKarte.setMinimumSize(QtCore.QSize(141, 233))
        # self.pushButtonKarte.setMaximumSize(QtCore.QSize(141, 233))  # ??
        self.setCardStyle()
        self.pushButtonKarte.setObjectName("pushButtonKarte")
        # self.layout.addWidget(self.pushButtonKarte, 0, 0)

        # BUTTON AKTION
        self.pushButtonKarte.clicked.connect(self.buttonClicked)

        self.pushButtonKarte.hide()

    def setCardStyle(self):
        self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                           f"    background-color: {self.background_color};\n"
                                           "    border-radius: 15px;\n"
                                           "    border-width: 3px;\n"
                                           "    border-style: solid;\n"
                                           f"    border-color: {self.border_color};\n"
                                           f"    image: url({self.image});\n"
                                           "}")

    def buttonClicked(self):
        print(f" Kartenindex: {self.index}")  # Test:
        if self.spielbar:
            # window.playCard(self.index)
            window.game_window.playCard(self.index)

    def changeBackground(self):
        if self.farbe == "Blue":
            self.background_color = THEME.blue
        elif self.farbe == "Green":
            self.background_color = THEME.green
        elif self.farbe == "Yellow":
            self.background_color = THEME.yellow
        elif self.farbe == "Red":
            self.background_color = THEME.red
        else:
            self.background_color = THEME.black

    def changeImage(self):
        # ##pfad = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"
        self.image = f"{THEME.filePath}{self.wert}.png"

    def changeBorder(self):
        if self.spielbar:
            self.border_color = THEME.playableBorderColor
            """self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                               f"    background-color: {self.background_color};\n"
                                               "    border-radius: 15px;\n"
                                               "    border-width: 6px;\n"
                                               "    border-style: solid;\n"
                                               f"    border-color: {self.border_color};\n"
                                               f"    image: url({self.image});\n"
                                               "}")"""
            self.setCardStyle()
        else:
            self.border_color = THEME.normalBorderColor
            """self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                               f"    background-color: {self.background_color};\n"
                                               "    border-radius: 15px;\n"
                                               "    border-width: 4px;\n"
                                               "    border-style: solid;\n"
                                               f"    border-color: {self.border_color};\n"
                                               f"    image: url({self.image});\n"
                                               "}")"""
            self.setCardStyle()

    def changeGeometry(self, x, y):
        self.xKoordinate = x
        self.yKoordinate = y
        self.pushButtonKarte.setGeometry(QtCore.QRect(self.xKoordinate, self.yKoordinate, 141, 233))

    def validate_card(self, vergleichs_karte):
        if vergleichs_karte.wert == "+4" or vergleichs_karte.wert == "Wunsch":
            if self.farbe == vergleichs_karte.farbe:
                self.spielbar = True
            elif self.farbe == "Black":  # braucht man?
                self.spielbar = True
            else:
                self.spielbar = False
        elif self.farbe == "Black":  # braucht man?
            self.spielbar = True
        elif self.farbe == vergleichs_karte.farbe:
            self.spielbar = True
        elif self.wert == vergleichs_karte.wert:
            self.spielbar = True
        else:
            self.spielbar = False

    def jokerStyle(self):
        self.changeBackground()
        self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                           f"    background-color: {self.background_color};\n"
                                           "    border-radius: 15px;\n"
                                           "    border-width: 3px;\n"
                                           "    border-style: solid;\n"
                                           f"    border-color: rgb(255, 255, 255);\n"  # ###
                                           f"    image: url({self.image});\n"
                                           "}")
        # self.setCardStyle(


class Spieler:
    def __init__(self, name, handkarten, farbe):
        self.name = name
        self.handkarten = handkarten
        self.farbe = farbe

    def draw_card(self, anzahl=7):
        """Zieht so viele Karten von DRAW_TALON wie übergeben werden.

        :parameter anzahl -> int
        'ziehen': erste Karte von DRAW_TALON wird in 'ausgeteilt' verschoben(.append(.pop(0)))
        gezogene Karten werden direkt den "handkarten" angehängt"""
        global DRAW_TALON
        ausgeteilt = []
        for zug in range(anzahl):
            ausgeteilt.append(DRAW_TALON.pop(0))
        self.handkarten.extend(ausgeteilt)
        return

    def validate_all_cards(self, oberste_karte):
        x = False
        for karte in self.handkarten:
            karte.validate_card(oberste_karte)
            if karte.spielbar:
                x = True
        return x

    def spieler_fertig(self):
        if len(self.handkarten) == 0:
            return True

    def pop(self, index):
        karte = self.handkarten.pop(index)
        return karte


def ein_spieler_fertig():
    """Prüft, ob einer der Spieler fertig ist

    falls ein ein Spieler fertig ist gibt .spieler_fertig Ture zurück, falls also True in ende -> ist ein spieler fertig
    sonst wird False zurückgegeben"""
    ende = []
    for spieler in range(len(PLAYERS)):
        ende.append(PLAYERS[spieler].spieler_fertig())
    if True in ende:
        return True
    else:
        return False


class UiEndWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MWinEnde()
        self.ui.setupUi(self)

        self.setTheme()

        self.titel = "UNO - The Game"
        self.icon = f'{THEME.filePath}icon.png'

        self.setWindowTitle(self.titel)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.ui.labelGewinner.setText(f"<strong>{VICTOR}</strong> hat gewonnen")

        self.ui.pushButtonPlayAgain.clicked.connect(self.play_again)
        self.ui.pushButtonMenu.clicked.connect(self.menu)
        self.ui.pushButtonQuit.clicked.connect(self.close)

    def setTheme(self):
        self.ui.frame.setStyleSheet(THEME.windowBackground_Style)
        self.ui.labelSpielende.setStyleSheet(THEME.gameOverMassage_Style)
        self.ui.labelGewinner.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            f"color: {PLAYERS[0].farbe};")
        self.ui.pushButtonMenu.setStyleSheet(THEME.menu_QuitButton_Style)
        self.ui.pushButtonQuit.setStyleSheet(THEME.menu_QuitButton_Style)
        self.ui.pushButtonPlayAgain.setStyleSheet(THEME.playAgainButton_Style)
        self.ui.frame_2.setStyleSheet(THEME.transparentBackground)

    def play_again(self):
        global PLAYERS, DRAW_TALON, PLAY_TALON
        for player in PLAYERS:
            player.handkarten = []
        DRAW_TALON = []
        PLAY_TALON = []
        # ##self.neuesSpiel = UiSpielFenster()
        # ##self.neuesSpiel.show()
        window.weiterPushed()

        self.close()

    def menu(self):
        global DRAW_TALON, PLAY_TALON, PLAYERS
        window.reset_entry()
        DRAW_TALON = []
        PLAY_TALON = []

        window.show()

        self.close()

    def quit(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UiStartWindow()
    window.show()
    sys.exit(app.exec_())
