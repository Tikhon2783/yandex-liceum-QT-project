from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QMainWindow, QWidget

# Виджет окна входа в аккаунт
class AuthWidget(QMainWindow):
    def __init__(self, next, *next_args):
        super().__init__()
        uic.loadUi('internal/ooi/aooth.ui', self)  # Загружаем дизайн

        self.next_widget = next
        self.next_args = next_args

        self.lbl_username.textChanged.connect(self.check_labels)
        self.lbl_psw.textChanged.connect(self.check_labels)
    
    # Проверка на заполнение полей перед активацией кнопок входа
    def check_labels(self):
        if self.lbl_username.text() and self.lbl_psw.text():
            self.btn_login.setEnabled(True)
            self.btn_signup.setEnabled(True)
        else:
            self.btn_login.setEnabled(False)
            self.btn_signup.setEnabled(False)
    
    # Метод проверки пароля
    def authenticate(self, username, password):
        # todo: Query DB
        todo_verified = (password == username + '1')
        if not todo_verified:
            # todo: show error widget
            return
        
        # Пользователь прошел проверку аутентификации
        self.grant_access()
    
    # Метод на регистрацию пользователя
    def register(self, username, password):
        # todo: Query DB
        todo_username_taken = True
        if todo_username_taken:
            # todo: show error widget
            return
        
        # Пользователь успешно зарегистрирован
        self.grant_access()
    
    # Метод успешного входа в аккаунт
    def grant_access(self):
        # todo: simple loading screen widget
        # todo: welcome back message with csv

        # Открываем следующий виджет и закрываем текущий
        self.next(*self.next_args)
        self.destroy()


# Виджет главного меню
class MainMenuWidget(QWidget):
    def __init__(self, info_widget, leaderboard_widget, *games_widgets):
        super().__init__()
        raise "UI FILE DOES NOT EXISTS YET!"
        uic.loadUi('internal/ooi/meenyoo.ui', self)  # Загружаем дизайн

        self.nextWidget = next
               
        self.lbl_username.textChanged.connect(self.check_labels)
        self.lbl_psw.textChanged.connect(self.check_labels)


# Виджет окна "О программе"
class ProgramInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        raise "UI FILE DOES NOT EXISTS YET!"
        uic.loadUi('internal/ooi/eenfoo.ui', self)  # Загружаем дизайн


# Виджет окна с результатами и достижениями
class LeaderboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        raise "UI FILE DOES NOT EXISTS YET!"
        uic.loadUi('internal/ooi/leedeerbhoord.ui', self)  # Загружаем дизайн


# Виджет окна с игрой blackjack (двадцать одно)
class BlackJackWidget(QWidget):
    def __init__(self):
        super().__init__()
        raise "UI FILE DOES NOT EXISTS YET!"
        uic.loadUi('internal/ooi/blakejake.ui', self)  # Загружаем дизайн
