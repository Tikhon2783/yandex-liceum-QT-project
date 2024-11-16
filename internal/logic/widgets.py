from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class AuthWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('internal/ooi/aooth.ui', self)  # Загружаем дизайн

        self.lbl_username.textChanged.connect(self.check_labels)
        self.lbl_psw.textChanged.connect(self.check_labels)
    
    def check_labels(self):
        if self.lbl_username.text() and self.lbl_psw.text():
            self.btn_login.setEnabled(True)
            self.btn_signup.setEnabled(True)
        else:
            self.btn_login.setEnabled(False)
            self.btn_signup.setEnabled(False)
