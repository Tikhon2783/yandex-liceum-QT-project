# Form implementation generated from reading ui file 'internal/ooi/leedeerbhoord.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_records(object):
    def setupUi(self, records):
        records.setObjectName("records")
        records.resize(619, 734)
        records.setStyleSheet("background-color: rgb(0, 77, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=records)
        self.centralwidget.setObjectName("centralwidget")
        self.table_of_widgets = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table_of_widgets.setEnabled(True)
        self.table_of_widgets.setGeometry(QtCore.QRect(120, 180, 361, 331))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Cond")
        font.setPointSize(14)
        self.table_of_widgets.setFont(font)
        self.table_of_widgets.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)")
        self.table_of_widgets.setObjectName("table_of_widgets")
        self.table_of_widgets.setColumnCount(3)
        self.table_of_widgets.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_of_widgets.setItem(1, 2, item)
        self.records_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.records_label.setGeometry(QtCore.QRect(130, 70, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Cond")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.records_label.setFont(font)
        self.records_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0)")
        self.records_label.setObjectName("records_label")
        records.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=records)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 26))
        self.menubar.setObjectName("menubar")
        records.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=records)
        self.statusbar.setObjectName("statusbar")
        records.setStatusBar(self.statusbar)

        self.retranslateUi(records)
        QtCore.QMetaObject.connectSlotsByName(records)

    def retranslateUi(self, records):
        _translate = QtCore.QCoreApplication.translate
        records.setWindowTitle(_translate("records", "MainWindow"))
        item = self.table_of_widgets.verticalHeaderItem(0)
        item.setText(_translate("records", "Игра 1"))
        item = self.table_of_widgets.verticalHeaderItem(1)
        item.setText(_translate("records", "Игра 2"))
        item = self.table_of_widgets.verticalHeaderItem(2)
        item.setText(_translate("records", "Игра 3"))
        item = self.table_of_widgets.verticalHeaderItem(3)
        item.setText(_translate("records", "Игра 4"))
        item = self.table_of_widgets.verticalHeaderItem(4)
        item.setText(_translate("records", "Игра 5"))
        item = self.table_of_widgets.verticalHeaderItem(5)
        item.setText(_translate("records", "Игра 6"))
        item = self.table_of_widgets.verticalHeaderItem(6)
        item.setText(_translate("records", "Игра7"))
        item = self.table_of_widgets.verticalHeaderItem(7)
        item.setText(_translate("records", "Игра 8"))
        item = self.table_of_widgets.verticalHeaderItem(8)
        item.setText(_translate("records", "Игра 9"))
        item = self.table_of_widgets.verticalHeaderItem(9)
        item.setText(_translate("records", "Игра 10"))
        item = self.table_of_widgets.horizontalHeaderItem(0)
        item.setText(_translate("records", "Игрок"))
        item = self.table_of_widgets.horizontalHeaderItem(1)
        item.setText(_translate("records", "Соперник"))
        item = self.table_of_widgets.horizontalHeaderItem(2)
        item.setText(_translate("records", "Выиграл"))
        __sortingEnabled = self.table_of_widgets.isSortingEnabled()
        self.table_of_widgets.setSortingEnabled(False)
        self.table_of_widgets.setSortingEnabled(__sortingEnabled)
        self.records_label.setText(_translate("records", "                 Таблица рекордов"))
