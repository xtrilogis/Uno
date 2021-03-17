import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from ui_Preparescreen import *
from ui_Basic_Spielscreen import *
from ui_Endscreen import *
from Theme_development import *
from Theme_dark_blue import *

""" to do: Stylesheet änderungen flexibler"""
# ### GLOBALS ### #
FARBEN = ["Blau", "Rot", "Grün", "Gelb"]
WERTE = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DRAW_TALON = []
PLAY_TALON = []
PLAYERS = []
# P_COLORS = ["rgb(150, 129, 212)", "rgb(61, 198, 213)", "rgb(67, 190, 40)", "rgb(59, 216, 230)", "rgb(230, 198, 30)",
# "rgb(230, 37, 170)"]
Gewinner = None
# THEME = default
THEME = dark_blue


class UiStartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MWinPrepare()
        self.ui.setupUi(self)

        self.counter = 1

        self.setTheme()

        # ### SETUP UI START-SCREEN ### #
        self.hidePre()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frameBackground.setGraphicsEffect(self.shadow)
        self.ui.pushButtonStart.setGraphicsEffect(self.shadow)

        # entfernt alles außer dem Frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ### Needed ### #

        self.prepare_game()

        # ### BUTTON CONNECT ### #
        self.ui.pushButtonStart.clicked.connect(self.startPushed)
        self.ui.pushButtonClose.clicked.connect(self.close)

        self.ui.pushButtonWeiter.clicked.connect(self.weiterPushed)
        self.ui.pushButtonReset.clicked.connect(self.reset_entry)
        self.ui.pushButtonSetColor.clicked.connect(self.showColorDialog)
        self.ui.pushButton_SpielerEnter.clicked.connect(self.spielernamen)
        self.ui.pushButtonColorTheme.clicked.connect(self.changeTheme)

    def hidePre(self):
        self.ui.frameSpieleranzahl.hide()
        self.ui.frameSpieler1.hide()
        self.ui.pushButtonReset.hide()
        self.ui.pushButtonWeiter.hide()
        self.ui.pushButtonColorTheme.hide()
        self.ui.labelErgebnis.hide()

    def show_start(self):
        self.ui.pushButtonStart.show()
        self.ui.labelUNO.show()
        self.ui.labelDescription.show()

    def setTheme(self):
        self.ui.frameBackground.setStyleSheet(THEME.backgroundstyle)
        self.ui.frameClose.setStyleSheet(THEME.frameBackground)
        self.ui.frameSpieleranzahl.setStyleSheet(THEME.frameBackground)
        self.ui.frameSpieler1.setStyleSheet(THEME.frameBackground)
        self.ui.frameReset.setStyleSheet(THEME.frameBackground)
        self.ui.frameWeiter.setStyleSheet(THEME.frameBackground)

        self.ui.labelUNO.setStyleSheet(THEME.UNOLabel)
        self.ui.labelDescription.setStyleSheet(THEME.DescriptionLabel)
        self.ui.pushButtonStart.setStyleSheet(THEME.StartButton)
        self.ui.labelinfo.setStyleSheet(THEME.infoLabel)

        self.ui.labelAnzahl.setStyleSheet(THEME.AnzahlLabel)
        self.ui.pushButton_plus.setStyleSheet(THEME.PulsMinus)
        self.ui.pushButton_minus.setStyleSheet(THEME.PulsMinus)
        self.ui.spinBoxNumber.setStyleSheet(THEME.spinBox)
        self.ui.labelSpieler1.setStyleSheet(THEME.NameLabel)
        self.ui.lineEditSpieler1.setStyleSheet(THEME.NameEingabe)
        self.ui.pushButtonSetColor.setStyleSheet(THEME.colorButton)
        self.ui.pushButton_SpielerEnter.setStyleSheet(THEME.okButton)
        self.ui.labelErgebnis.setStyleSheet(THEME.AnzahlLabel)
        self.ui.pushButtonWeiter.setStyleSheet(THEME.weiterBPassiv)
        self.ui.pushButtonColorTheme.setStyleSheet(THEME.theme_Reset)
        self.ui.pushButtonReset.setStyleSheet(THEME.theme_Reset)

    def changeTheme(self):
        global THEME
        if THEME == dark_blue:
            THEME = default
        else:
            THEME = dark_blue
        self.setTheme()

        if len(PLAYERS) == self.ui.spinBoxNumber.value():
            self.ui.pushButtonWeiter.setStyleSheet(THEME.weiterBAktiv)

    def prepare_game(self):
        """ setzt SpinBox Minimum auf 2 & Label: Spieler 1"""
        self.ui.spinBoxNumber.setMinimum(2)
        self.ui.labelSpieler1.setText(f"Spieler {self.counter}:")

    # ### BUTTON AUFRUFE ### #
    def startPushed(self):
        """versteckt den Start-Screen, lässt Spieler-Eingaben erscheinen"""
        self.ui.pushButtonStart.hide()
        self.ui.labelUNO.hide()
        self.ui.labelDescription.hide()

        self.ui.frameSpieleranzahl.show()
        self.ui.frameSpieler1.show()
        self.ui.pushButtonReset.show()
        self.ui.pushButtonWeiter.show()
        self.ui.pushButtonColorTheme.show()

    def spielernamen(self):
        """fügt die eingegebenen Namen der liste hinzu.

        Eingegebener Text in liste, LineEdit wird geleert,
        wenn counter < als Spielerzahl: counter wird erhöht und Label entsprechend geändert
        wenn counter = Spielerzahl: Button&LineEdit verschwinden, Label zeigt die Liste der Spieler
            der weiter Button bekommt eine neu Farbe "wird aktiviert" """
        global PLAYERS
        self.ui.labelErgebnis.hide()
        PLAYERS.append(Spieler(name=self.ui.lineEditSpieler1.text(), handkarten=[], farbe=THEME.P_COLORS[0]))
        THEME.P_COLORS.append(THEME.P_COLORS.pop(0))
        self.ui.lineEditSpieler1.clear()

        if len(PLAYERS) < self.ui.spinBoxNumber.value():
            self.counter += 1
            self.ui.labelSpieler1.setText(f"Spieler {self.counter}:")
        else:
            self.ui.pushButton_SpielerEnter.hide()
            self.ui.pushButtonSetColor.hide()
            self.ui.lineEditSpieler1.hide()

            self.ui.labelSpieler1.setText(f"{len(PLAYERS)} Spieler")
            self.ui.pushButtonWeiter.setStyleSheet(THEME.weiterBAktiv)

    def showColorDialog(self):
        selected_color = QColorDialog.getColor()
        if selected_color.isValid():
            THEME.P_COLORS.insert(0, f"rgb{selected_color.getRgb()}")

    def weiterPushed(self):
        """Wenn jeder Spieler (len(Players)==SpinBox) einen Namen eingegeben hat, wird das Spielfenster geöffnet

        sonst wird um Eingabe gebeten."""
        if len(PLAYERS) == self.ui.spinBoxNumber.value():
            self.spielFenster = UiSpielFenster()
            self.spielFenster.show()

            self.close()
        else:
            self.ui.labelSpieler1.setText(f"Spieler {self.counter}:")
            self.ui.lineEditSpieler1.show()
            self.ui.pushButtonSetColor.show()
            self.ui.pushButton_SpielerEnter.show()
            if len(PLAYERS) == 0:
                text = f"Zu wenig Spieler! Noch kein Spielername eingegeben."
            else:
                text = f"Zu wenig Spieler! Nur {len(PLAYERS)} Spielername(n) eingegeben."
            self.ui.labelErgebnis.show()
            self.ui.labelErgebnis.setText(str(text))

    def reset_entry(self):
        """Setzt alle Eingabefelder zurück"""
        global PLAYERS
        PLAYERS = []
        self.ui.spinBoxNumber.setValue(2)
        self.ui.pushButton_SpielerEnter.show()
        self.ui.lineEditSpieler1.show()
        self.ui.pushButtonSetColor.show()
        self.ui.pushButtonWeiter.setStyleSheet(THEME.weiterBPassiv)
        self.counter = 1
        self.prepare_game()


class UiSpielFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setTheme()
        # später im Preparescreen
        # spieler_preset()

        # Variablen
        self.titel = "UNO - The Game"
        self.icon = 'D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/icon.png'

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

        self.ui.pushButtonBlau.clicked.connect(self.farbeBlau)
        self.ui.pushButtonGruen.clicked.connect(self.farbeGreen)
        self.ui.pushButtonGelb.clicked.connect(self.farbeGelb)
        self.ui.pushButtoRot.clicked.connect(self.farbeRot)

        # Funktionsaufrufe
        self.preStart()
        self.setUpUi()

    def setTheme(self):
        # Frames
        self.ui.frameHintergrund.setStyleSheet(THEME.backgroundstyleSpiel)
        self.ui.frame_Stapel.setStyleSheet(THEME.frameBackground)
        self.ui.frame_Handkarten.setStyleSheet(THEME.frameBackground)
        self.ui.framePassen.setStyleSheet(THEME.frameBackground)
        self.ui.frameFarbwahl.setStyleSheet(THEME.frameBackground)
        self.ui.frameLeftLast.setStyleSheet(THEME.frameBackground)
        self.ui.frameRightNext.setStyleSheet(THEME.frameBackground)
        self.ui.frameTop.setStyleSheet(THEME.frameBackground)

        self.ui.pushButtonWeiter.setStyleSheet(THEME.UNOButton)
        self.ui.pushButtonUNO.setStyleSheet(THEME.UNOButton)
        self.ui.pushButtonBlau.setStyleSheet(THEME.blueChoice)
        self.ui.pushButtonGruen.setStyleSheet(THEME.greenChoice)
        self.ui.pushButtonGelb.setStyleSheet(THEME.gelbChoice)
        self.ui.pushButtoRot.setStyleSheet(THEME.rotChoice)

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
        if "Schwarz" in DRAW_TALON[0].farbe:
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
            self.ui.pushButtonDraw_T.setStyleSheet(THEME.hasToDraw)
            self.ui.LabelSpielername.setText(f"{self.player.name}, du musst ziehen.")
        else:
            self.ui.pushButtonDraw_T.setStyleSheet(THEME.drawTalon)

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
        global Gewinner
        # ist Spieler fertig
        self.ui.pushButtonDraw_T.setStyleSheet(THEME.drawTalon)
        if self.player.spieler_fertig():
            Gewinner = self.player.name
            self.spielEnde()

        if "Schwarz" == PLAY_TALON[0].farbe:
            self.joker_action(PLAY_TALON[0])
        else:
            # UNO gesagt?
            self.UNO()

            if PLAY_TALON[0].wert not in WERTE:
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
        global Gewinner
        if not ein_spieler_fertig():
            self.refill()
            self.ui.pushButtonUNO.setStyleSheet(THEME.UNOButton)
            self.hideUnnecessary()
            self.setUpUi()
        else:
            Gewinner = self.player.name
            self.spielEnde()

    # ##
    # Button funktionen

    def passen(self):
        self.karten_hide(self.handkarten)
        self.play_order()
        self.endTurn()

    def UNOClicked(self):
        self.uno_gesagt = True
        self.ui.pushButtonUNO.setStyleSheet(THEME.UNOButtonclicked)
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

    def farbeBlau(self):
        self.farbe = "Blau"
        self.endJoker()

    def farbeGreen(self):
        self.farbe = "Grün"
        self.endJoker()

    def farbeGelb(self):
        self.farbe = "Gelb"
        self.endJoker()

    def farbeRot(self):
        self.farbe = "Rot"
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
        """generiert die normalen Karten als Klasse aus global @FARBEN und @WERTE, jede Karte gibt es viermal"""
        global FARBEN, WERTE
        karten = []
        for i in range(1):
            for farbe in FARBEN:
                for wert in WERTE:
                    karten.append(UiKarten(farbe, wert, spielbar=False, fenster=self.ui.frame_Handkarten, index=None))
        return karten

    def special_cards(self) -> list:
        """erstellt Sonder-Karten +2, Aussetzen, Richtungswechsel, benutzt global constant @FARBEN"""
        global FARBEN
        sonder_werte = ["+2", "Aussetzen", "Richtungswechsel"]
        karten = []
        for i in range(4):
            for farbe in FARBEN:
                for wert in sonder_werte:
                    karten.append(UiKarten(farbe, wert, spielbar=False, fenster=self.ui.frame_Handkarten, index=None))
        return karten

    def joker_cards(self) -> list:
        """ erstellt Joker_Karten +4 und 'Wunsch', jede Karte gibt es vier mal"""
        karten = []
        for i in range(4):
            karten.append(UiKarten("Schwarz", "+4", spielbar=True, fenster=self.ui.frame_Handkarten, index=None))
            karten.append(UiKarten("Schwarz", "Wunsch", spielbar=True, fenster=self.ui.frame_Handkarten, index=None))
        return karten


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
        # ## Basic Farben
        self.background_color = "rgb(200, 50, 192)"
        self.border_color = "rgb(255, 255, 255)"
        self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/default.png"
        self.xKoordinate = 7
        self.yKoordinate = 7

        # ## Funktionsaufrufe
        self.changeBackground()
        self.changeImage()

        self.pushButtonKarte.setGeometry(QtCore.QRect(self.xKoordinate, self.yKoordinate, 141, 233))
        self.pushButtonKarte.setMinimumSize(QtCore.QSize(141, 233))
        self.pushButtonKarte.setMaximumSize(QtCore.QSize(141, 233))  # ??
        self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                           f"    background-color: {self.background_color};\n"
                                           "    border-radius: 15px;\n"
                                           "    border-width: 3px;\n"
                                           "    border-style: solid;\n"
                                           f"    border-color: {self.border_color};\n"
                                           f"    image: url({self.image});\n"
                                           "}")
        self.pushButtonKarte.setObjectName("pushButtonKarte")
        # self.layout.addWidget(self.pushButtonKarte, 0, 0)

        # BUTTON AKTION
        self.pushButtonKarte.clicked.connect(self.buttonClicked)

        self.pushButtonKarte.hide()

    def buttonClicked(self):
        print(f" Kartenindex: {self.index}")  # Test:
        if self.spielbar:
            # window.playCard(self.index)
            window.spielFenster.playCard(self.index)

    def changeBackground(self):
        if self.farbe == "Blau":
            self.background_color = THEME.blau
        elif self.farbe == "Grün":
            self.background_color = THEME.green
        elif self.farbe == "Gelb":
            self.background_color = THEME.gelb
        elif self.farbe == "Rot":
            self.background_color = THEME.rot
        else:
            self.background_color = THEME.black

    def changeImage(self):
        pfad = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/"
        self.image = f"{pfad}{self.wert}.png"
        """"if self.wert == "0":
            self.image = f"{pfad}0.png"
        elif self.wert == "1":
            self.image = f"{pfad}1.png"
        elif self.wert == "2":
            self.image = f"{pfad}2.png"
        elif self.wert == "3":
            self.image = f"{pfad}3.png"
        elif self.wert == "4":
            self.image = f"{pfad}4.png"
        elif self.wert == "5":
            self.image = f"{pfad}5.png"
        elif self.wert == "6":
            self.image = f"{pfad}6.png"
        elif self.wert == "7":
            self.image = f"{pfad}7.png"
        elif self.wert == "8":
            self.image = f"{pfad}8.png"
        elif self.wert == "9":
            self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/9.png"
        elif self.wert == "+2":
            self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/+2.png"
        elif self.wert == "Aussetzen":
            self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/Aussetzen.png"
        elif self.wert == "Richtungswechsel":
            self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/Richtungswechsel.png"
        elif self.wert == "+4":
            self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/+4.png"
        else:
            self.image = "D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/Wunsch.png"""""

    def changeBorder(self):
        if self.spielbar:
            self.border_color = THEME.borderPlay
            self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                               f"    background-color: {self.background_color};\n"
                                               "    border-radius: 15px;\n"
                                               "    border-width: 6px;\n"
                                               "    border-style: solid;\n"
                                               f"    border-color: {self.border_color};\n"
                                               f"    image: url({self.image});\n"
                                               "}")
        else:
            self.border_color = THEME.borderNormal
            self.pushButtonKarte.setStyleSheet("QPushButton {\n"
                                               f"    background-color: {self.background_color};\n"
                                               "    border-radius: 15px;\n"
                                               "    border-width: 4px;\n"
                                               "    border-style: solid;\n"
                                               f"    border-color: {self.border_color};\n"
                                               f"    image: url({self.image});\n"
                                               "}")

    def changeGeometry(self, x, y):
        self.xKoordinate = x
        self.yKoordinate = y
        self.pushButtonKarte.setGeometry(QtCore.QRect(self.xKoordinate, self.yKoordinate, 141, 233))

    def validate_card(self, vergleichs_karte):
        if vergleichs_karte.wert == "+4" or vergleichs_karte.wert == "Wunsch":
            if self.farbe == vergleichs_karte.farbe:
                self.spielbar = True
            elif self.farbe == "Schwarz":  # braucht man?
                self.spielbar = True
            else:
                self.spielbar = False
        elif self.farbe == "Schwarz":  # braucht man?
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
                                           f"    border-color: rgb(255, 255, 255);\n"
                                           f"    image: url({self.image});\n"
                                           "}")


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
        self.icon = 'D:/Users/Wisdom/Documents/Weiteres/Projekte/UNO/Karten/icon.png'

        self.setWindowTitle(self.titel)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.ui.labelGewinner.setText(f"<strong>{Gewinner}</strong> hat gewonnen")

        self.ui.pushButtonPlayAgain.clicked.connect(self.play_again)
        self.ui.pushButtonMenu.clicked.connect(self.menu)
        self.ui.pushButtonQuit.clicked.connect(self.close)

    def setTheme(self):
        self.ui.frame.setStyleSheet(THEME.backgroundstyleSpiel)
        self.ui.labelSpielende.setStyleSheet(THEME.gewinnerLabel)
        self.ui.labelGewinner.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                         f"color: {PLAYERS[0].farbe};")
        self.ui.pushButtonMenu.setStyleSheet(THEME.menuQuitButton)
        self.ui.pushButtonQuit.setStyleSheet(THEME.menuQuitButton)
        self.ui.pushButtonPlayAgain.setStyleSheet(THEME.PlayButton)
        self.ui.frame_2.setStyleSheet(THEME.frameBackground)

    def play_again(self):
        global PLAYERS, DRAW_TALON, PLAY_TALON
        for player in PLAYERS:
            player.handkarten = []
        DRAW_TALON = []
        PLAY_TALON = []
        #self.neuesSpiel = UiSpielFenster()
        #self.neuesSpiel.show()
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
