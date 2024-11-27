from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import sys
import random


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("blackjack.ui", self)
        self.setWindowTitle("BlackJack!")

        # Define our widgets
        self.dealerCard1 = self.findChild(QLabel, "dealerCard1")
        self.dealerCard2 = self.findChild(QLabel, "dealerCard2")
        self.dealerCard3 = self.findChild(QLabel, "dealerCard3")
        self.dealerCard4 = self.findChild(QLabel, "dealerCard4")
        self.dealerCard5 = self.findChild(QLabel, "dealerCard5")

        self.playerCard1 = self.findChild(QLabel, "playerCard1")
        self.playerCard2 = self.findChild(QLabel, "playerCard2")
        self.playerCard3 = self.findChild(QLabel, "playerCard3")
        self.playerCard4 = self.findChild(QLabel, "playerCard4")
        self.playerCard5 = self.findChild(QLabel, "playerCard5")

        self.dealerHeaderLabel = self.findChild(QLabel, "dlabel")
        self.playerHeaderLabel = self.findChild(QLabel, "plabel")

        self.shuffleButton = self.findChild(QPushButton, "spushButton")
        self.hitMeButton = self.findChild(QPushButton, "hitMeButton")
        self.standButton = self.findChild(QPushButton, "standButton")

        # Shuffle Cards
        self.shuffle()

        # Click Buttons
        self.shuffleButton.clicked.connect(self.shuffle)
        self.hitMeButton.clicked.connect(self.playerTakesCard)
        self.standButton.clicked.connect(self.stand)

        # Show The App
        self.show()

    # Stand
    def stand(self):
       pass

    # Check For Blackjack
    def blackjack(self, player):
        pass

    def shuffle(self):
       pass

    def dealCards(self):
        pass

    def dealerTakesCard(self):
        pass

    def playerTakesCard(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec())
