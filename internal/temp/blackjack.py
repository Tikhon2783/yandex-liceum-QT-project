# Form implementation generated from reading ui file 'blackjack.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setStyleSheet("background-color: rgb(0, 77, 0);;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.spushButton.setGeometry(QtCore.QRect(30, 570, 150, 40))
        self.spushButton.setStyleSheet("background-color: white;")
        self.spushButton.setObjectName("spushButton")
        self.hitMeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.hitMeButton.setGeometry(QtCore.QRect(200, 570, 150, 40))
        self.hitMeButton.setStyleSheet("background-color: white;")
        self.hitMeButton.setObjectName("hitMeButton")
        self.dealerCard1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard1.setGeometry(QtCore.QRect(30, 40, 150, 218))
        self.dealerCard1.setText("")
        self.dealerCard1.setPixmap(QtGui.QPixmap("images/cards/2_of_clubs.png"))
        self.dealerCard1.setScaledContents(True)
        self.dealerCard1.setObjectName("dealerCard1")
        self.playerCard1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard1.setGeometry(QtCore.QRect(30, 310, 150, 218))
        self.playerCard1.setText("")
        self.playerCard1.setPixmap(QtGui.QPixmap("images/cards/2_of_diamonds.png"))
        self.playerCard1.setScaledContents(True)
        self.playerCard1.setObjectName("playerCard1")
        self.dlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.dlabel.setGeometry(QtCore.QRect(30, 10, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dlabel.setFont(font)
        self.dlabel.setObjectName("dlabel")
        self.plabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.plabel.setGeometry(QtCore.QRect(34, 280, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plabel.setFont(font)
        self.plabel.setObjectName("plabel")
        self.standButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.standButton.setGeometry(QtCore.QRect(370, 570, 150, 40))
        self.standButton.setStyleSheet("background-color: light gray;")
        self.standButton.setObjectName("standButton")
        self.dealerCard2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard2.setGeometry(QtCore.QRect(200, 40, 150, 218))
        self.dealerCard2.setText("")
        self.dealerCard2.setPixmap(QtGui.QPixmap("images/cards/2_of_clubs.png"))
        self.dealerCard2.setScaledContents(True)
        self.dealerCard2.setObjectName("dealerCard2")
        self.dealerCard3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard3.setGeometry(QtCore.QRect(370, 40, 150, 218))
        self.dealerCard3.setText("")
        self.dealerCard3.setPixmap(QtGui.QPixmap("images/cards/2_of_clubs.png"))
        self.dealerCard3.setScaledContents(True)
        self.dealerCard3.setObjectName("dealerCard3")
        self.dealerCard4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard4.setGeometry(QtCore.QRect(540, 40, 150, 218))
        self.dealerCard4.setText("")
        self.dealerCard4.setPixmap(QtGui.QPixmap("images/cards/2_of_clubs.png"))
        self.dealerCard4.setScaledContents(True)
        self.dealerCard4.setObjectName("dealerCard4")
        self.dealerCard5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard5.setGeometry(QtCore.QRect(710, 40, 150, 218))
        self.dealerCard5.setText("")
        self.dealerCard5.setPixmap(QtGui.QPixmap("images/cards/2_of_clubs.png"))
        self.dealerCard5.setScaledContents(True)
        self.dealerCard5.setObjectName("dealerCard5")
        self.playerCard2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard2.setGeometry(QtCore.QRect(200, 310, 150, 218))
        self.playerCard2.setText("")
        self.playerCard2.setPixmap(QtGui.QPixmap("images/cards/2_of_diamonds.png"))
        self.playerCard2.setScaledContents(True)
        self.playerCard2.setObjectName("playerCard2")
        self.playerCard3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard3.setGeometry(QtCore.QRect(370, 310, 150, 218))
        self.playerCard3.setText("")
        self.playerCard3.setPixmap(QtGui.QPixmap("images/cards/2_of_diamonds.png"))
        self.playerCard3.setScaledContents(True)
        self.playerCard3.setObjectName("playerCard3")
        self.playerCard4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard4.setGeometry(QtCore.QRect(540, 310, 150, 218))
        self.playerCard4.setText("")
        self.playerCard4.setPixmap(QtGui.QPixmap("images/cards/2_of_diamonds.png"))
        self.playerCard4.setScaledContents(True)
        self.playerCard4.setObjectName("playerCard4")
        self.playerCard5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard5.setGeometry(QtCore.QRect(710, 310, 150, 218))
        self.playerCard5.setText("")
        self.playerCard5.setPixmap(QtGui.QPixmap("images/cards/2_of_diamonds.png"))
        self.playerCard5.setScaledContents(True)
        self.playerCard5.setObjectName("playerCard5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spushButton.setText(_translate("MainWindow", "Начать заново"))
        self.hitMeButton.setText(_translate("MainWindow", "Взять карту"))
        self.dlabel.setText(_translate("MainWindow", "Соперник"))
        self.plabel.setText(_translate("MainWindow", "Игрок"))
        self.standButton.setText(_translate("MainWindow", "Закончить"))
        
