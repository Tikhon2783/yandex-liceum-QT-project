# Form implementation generated from reading ui file 'internal/ooi/blakejake.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 677)
        MainWindow.setStyleSheet("background-color: rgb(1, 67, 30);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dealerCard1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard1.setGeometry(QtCore.QRect(30, 40, 150, 218))
        self.dealerCard1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dealerCard1.setText("")
        self.dealerCard1.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard1.setScaledContents(True)
        self.dealerCard1.setObjectName("dealerCard1")
        self.playerCard1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard1.setGeometry(QtCore.QRect(30, 310, 150, 218))
        self.playerCard1.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.playerCard1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.playerCard1.setText("")
        self.playerCard1.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard1.setScaledContents(True)
        self.playerCard1.setObjectName("playerCard1")
        self.dlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.dlabel.setGeometry(QtCore.QRect(80, 0, 351, 21))
        self.dlabel.setStyleSheet("color: rgb(243, 198, 32);")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dlabel.setFont(font)
        self.dlabel.setText("Дилер: 0")
        self.dlabel.setObjectName("dlabel")
        self.dealerCard2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard2.setGeometry(QtCore.QRect(200, 40, 150, 218))
        self.dealerCard2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dealerCard2.setText("")
        self.dealerCard2.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard2.setScaledContents(True)
        self.dealerCard2.setObjectName("dealerCard2")
        self.dealerCard3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard3.setGeometry(QtCore.QRect(370, 40, 150, 218))
        self.dealerCard3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dealerCard3.setText("")
        self.dealerCard3.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard3.setScaledContents(True)
        self.dealerCard3.setObjectName("dealerCard3")
        self.dealerCard4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard4.setGeometry(QtCore.QRect(540, 40, 150, 218))
        self.dealerCard4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dealerCard4.setText("")
        self.dealerCard4.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard4.setScaledContents(True)
        self.dealerCard4.setObjectName("dealerCard4")
        self.dealerCard5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard5.setGeometry(QtCore.QRect(710, 40, 150, 218))
        self.dealerCard5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dealerCard5.setText("")
        self.dealerCard5.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard5.setScaledContents(True)
        self.dealerCard5.setObjectName("dealerCard5")
        self.playerCard2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard2.setGeometry(QtCore.QRect(200, 310, 150, 218))
        self.playerCard2.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.playerCard2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.playerCard2.setText("")
        self.playerCard2.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard2.setScaledContents(True)
        self.playerCard2.setObjectName("playerCard2")
        self.playerCard3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard3.setGeometry(QtCore.QRect(370, 310, 150, 218))
        self.playerCard3.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.playerCard3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.playerCard3.setText("")
        self.playerCard3.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard3.setScaledContents(True)
        self.playerCard3.setObjectName("playerCard3")
        self.playerCard4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard4.setGeometry(QtCore.QRect(540, 310, 150, 218))
        self.playerCard4.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.playerCard4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.playerCard4.setText("")
        self.playerCard4.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard4.setScaledContents(True)
        self.playerCard4.setObjectName("playerCard4")
        self.playerCard5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard5.setGeometry(QtCore.QRect(710, 310, 150, 218))
        self.playerCard5.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.playerCard5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.playerCard5.setText("")
        self.playerCard5.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard5.setScaledContents(True)
        self.playerCard5.setObjectName("playerCard5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 540, 841, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.actions = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.actions.setContentsMargins(0, 0, 0, 0)
        self.actions.setObjectName("actions")
        self.btn_restart = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_restart.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_restart.setFont(font)
        self.btn_restart.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.btn_restart.setStyleSheet("background-color: rgb(1, 38, 67);\n"
"color: rgb(243, 198, 32);")
        self.btn_restart.setObjectName("btn_restart")
        self.actions.addWidget(self.btn_restart)
        self.btn_hit = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_hit.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_hit.setFont(font)
        self.btn_hit.setStyleSheet("background-color: rgb(1, 38, 67);\n"
"color: rgb(243, 198, 32);")
        self.btn_hit.setObjectName("btn_hit")
        self.actions.addWidget(self.btn_hit)
        self.btn_stand = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_stand.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stand.setFont(font)
        self.btn_stand.setStyleSheet("background-color: rgb(1, 38, 67);\n"
"color: rgb(243, 198, 32);")
        self.btn_stand.setObjectName("btn_stand")
        self.actions.addWidget(self.btn_stand)
        self.playerCard6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard6.setGeometry(QtCore.QRect(65, 315, 150, 218))
        self.playerCard6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerCard6.setLineWidth(2)
        self.playerCard6.setText("")
        self.playerCard6.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard6.setScaledContents(True)
        self.playerCard6.setObjectName("playerCard6")
        self.playerCard7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard7.setGeometry(QtCore.QRect(235, 315, 150, 218))
        self.playerCard7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerCard7.setLineWidth(2)
        self.playerCard7.setText("")
        self.playerCard7.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard7.setScaledContents(True)
        self.playerCard7.setObjectName("playerCard7")
        self.dealerCard_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_2.setEnabled(True)
        self.dealerCard_2.setGeometry(QtCore.QRect(80, 40, 150, 218))
        self.dealerCard_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_2.setLineWidth(2)
        self.dealerCard_2.setText("")
        self.dealerCard_2.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_2.setScaledContents(True)
        self.dealerCard_2.setObjectName("dealerCard_2")
        self.dealerCard_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_3.setEnabled(True)
        self.dealerCard_3.setGeometry(QtCore.QRect(130, 40, 150, 218))
        self.dealerCard_3.setAutoFillBackground(False)
        self.dealerCard_3.setStyleSheet("")
        self.dealerCard_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_3.setLineWidth(2)
        self.dealerCard_3.setText("")
        self.dealerCard_3.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_3.setScaledContents(True)
        self.dealerCard_3.setObjectName("dealerCard_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(69, 260, 751, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.labels_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.labels_layout.setContentsMargins(0, 0, 0, 0)
        self.labels_layout.setObjectName("labels_layout")
        self.plabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.plabel.setStyleSheet("color: rgb(243, 198, 32);")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plabel.setFont(font)
        self.plabel.setText("Игрок: 0")
        self.plabel.setObjectName("plabel")
        self.labels_layout.addWidget(self.plabel)
        self.res_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.res_label.setFont(font)
        self.res_label.setStyleSheet("color: rgb(243, 198, 32);")
        self.res_label.setText("")
        self.res_label.setObjectName("res_label")
        self.labels_layout.addWidget(self.res_label)
        self.playerCard8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard8.setGeometry(QtCore.QRect(405, 315, 150, 218))
        self.playerCard8.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerCard8.setLineWidth(2)
        self.playerCard8.setText("")
        self.playerCard8.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard8.setScaledContents(True)
        self.playerCard8.setObjectName("playerCard8")
        self.playerCard9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard9.setGeometry(QtCore.QRect(575, 315, 150, 218))
        self.playerCard9.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerCard9.setLineWidth(2)
        self.playerCard9.setText("")
        self.playerCard9.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard9.setScaledContents(True)
        self.playerCard9.setObjectName("playerCard9")
        self.playerCard10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard10.setGeometry(QtCore.QRect(745, 315, 150, 218))
        self.playerCard10.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerCard10.setLineWidth(2)
        self.playerCard10.setText("")
        self.playerCard10.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard10.setScaledContents(True)
        self.playerCard10.setObjectName("playerCard10")
        self.dealerCard_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_4.setEnabled(True)
        self.dealerCard_4.setGeometry(QtCore.QRect(180, 40, 150, 218))
        self.dealerCard_4.setAutoFillBackground(False)
        self.dealerCard_4.setStyleSheet("")
        self.dealerCard_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_4.setLineWidth(2)
        self.dealerCard_4.setText("")
        self.dealerCard_4.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_4.setScaledContents(True)
        self.dealerCard_4.setObjectName("dealerCard_4")
        self.dealerCard_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_8.setEnabled(True)
        self.dealerCard_8.setGeometry(QtCore.QRect(380, 40, 150, 218))
        self.dealerCard_8.setAutoFillBackground(False)
        self.dealerCard_8.setStyleSheet("")
        self.dealerCard_8.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_8.setLineWidth(2)
        self.dealerCard_8.setText("")
        self.dealerCard_8.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_8.setScaledContents(True)
        self.dealerCard_8.setObjectName("dealerCard_8")
        self.dealerCard_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_6.setEnabled(True)
        self.dealerCard_6.setGeometry(QtCore.QRect(280, 40, 150, 218))
        self.dealerCard_6.setAutoFillBackground(False)
        self.dealerCard_6.setStyleSheet("")
        self.dealerCard_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_6.setLineWidth(2)
        self.dealerCard_6.setText("")
        self.dealerCard_6.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_6.setScaledContents(True)
        self.dealerCard_6.setObjectName("dealerCard_6")
        self.dealerCard_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_5.setEnabled(True)
        self.dealerCard_5.setGeometry(QtCore.QRect(230, 40, 150, 218))
        self.dealerCard_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_5.setLineWidth(2)
        self.dealerCard_5.setText("")
        self.dealerCard_5.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_5.setScaledContents(True)
        self.dealerCard_5.setObjectName("dealerCard_5")
        self.dealerCard_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_7.setEnabled(True)
        self.dealerCard_7.setGeometry(QtCore.QRect(330, 40, 150, 218))
        self.dealerCard_7.setAutoFillBackground(False)
        self.dealerCard_7.setStyleSheet("")
        self.dealerCard_7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_7.setLineWidth(2)
        self.dealerCard_7.setText("")
        self.dealerCard_7.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_7.setScaledContents(True)
        self.dealerCard_7.setObjectName("dealerCard_7")
        self.dealerCard_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_9.setEnabled(True)
        self.dealerCard_9.setGeometry(QtCore.QRect(430, 40, 150, 218))
        self.dealerCard_9.setAutoFillBackground(False)
        self.dealerCard_9.setStyleSheet("")
        self.dealerCard_9.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_9.setLineWidth(2)
        self.dealerCard_9.setText("")
        self.dealerCard_9.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_9.setScaledContents(True)
        self.dealerCard_9.setObjectName("dealerCard_9")
        self.dealerCard_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_10.setEnabled(True)
        self.dealerCard_10.setGeometry(QtCore.QRect(480, 40, 150, 218))
        self.dealerCard_10.setAutoFillBackground(False)
        self.dealerCard_10.setStyleSheet("")
        self.dealerCard_10.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_10.setLineWidth(2)
        self.dealerCard_10.setText("")
        self.dealerCard_10.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_10.setScaledContents(True)
        self.dealerCard_10.setObjectName("dealerCard_10")
        self.dealerCard_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_11.setEnabled(True)
        self.dealerCard_11.setGeometry(QtCore.QRect(530, 40, 150, 218))
        self.dealerCard_11.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_11.setLineWidth(2)
        self.dealerCard_11.setText("")
        self.dealerCard_11.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_11.setScaledContents(True)
        self.dealerCard_11.setObjectName("dealerCard_11")
        self.dealerCard_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dealerCard_12.setEnabled(True)
        self.dealerCard_12.setGeometry(QtCore.QRect(580, 40, 150, 218))
        self.dealerCard_12.setAutoFillBackground(False)
        self.dealerCard_12.setStyleSheet("")
        self.dealerCard_12.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dealerCard_12.setLineWidth(2)
        self.dealerCard_12.setText("")
        self.dealerCard_12.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_clubs.png"))
        self.dealerCard_12.setScaledContents(True)
        self.dealerCard_12.setObjectName("dealerCard_12")
        self.playerCard11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard11.setGeometry(QtCore.QRect(100, 320, 150, 218))
        self.playerCard11.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerCard11.setLineWidth(2)
        self.playerCard11.setText("")
        self.playerCard11.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard11.setScaledContents(True)
        self.playerCard11.setObjectName("playerCard11")
        self.playerCard12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.playerCard12.setGeometry(QtCore.QRect(270, 320, 150, 218))
        self.playerCard12.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.playerCard12.setLineWidth(2)
        self.playerCard12.setText("")
        self.playerCard12.setPixmap(QtGui.QPixmap("internal/ooi\\images/cards/2_of_diamonds.png"))
        self.playerCard12.setScaledContents(True)
        self.playerCard12.setObjectName("playerCard12")
        self.dealerCard1.raise_()
        self.playerCard1.raise_()
        self.dlabel.raise_()
        self.dealerCard2.raise_()
        self.dealerCard3.raise_()
        self.dealerCard4.raise_()
        self.dealerCard5.raise_()
        self.playerCard2.raise_()
        self.playerCard3.raise_()
        self.playerCard4.raise_()
        self.playerCard5.raise_()
        self.horizontalLayoutWidget.raise_()
        self.playerCard6.raise_()
        self.playerCard7.raise_()
        self.dealerCard_2.raise_()
        self.dealerCard_3.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.playerCard8.raise_()
        self.playerCard9.raise_()
        self.playerCard10.raise_()
        self.dealerCard_4.raise_()
        self.dealerCard_5.raise_()
        self.dealerCard_6.raise_()
        self.dealerCard_7.raise_()
        self.dealerCard_8.raise_()
        self.dealerCard_9.raise_()
        self.dealerCard_10.raise_()
        self.dealerCard_11.raise_()
        self.dealerCard_12.raise_()
        self.playerCard11.raise_()
        self.playerCard12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 26))
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
        self.dlabel.setText(_translate("MainWindow", "Дилер: 0"))
        self.btn_restart.setText(_translate("MainWindow", "Начать заново"))
        self.btn_hit.setText(_translate("MainWindow", "Взять карту"))
        self.btn_stand.setText(_translate("MainWindow", "Остановиться"))
        self.plabel.setText(_translate("MainWindow", "Игрок: 0"))
