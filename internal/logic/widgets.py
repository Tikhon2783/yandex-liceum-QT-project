from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QErrorMessage, QLabel, QTableWidgetItem
# from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QPen, QImage, QPixmap
from PyQt6.QtCore import Qt, QTimer

from csv import DictReader
import datetime as dt
from math import pi, sin, cos

import internal.ooi.aooth as auth_ooi
import internal.ooi.meenyoo as menu_ooi
import internal.ooi.blakejake as bj_ooi
import internal.ooi.eenfoo as info_ooi
import internal.ooi.leedeerbhoord as lb_ui
import internal.ooi.eenfoo as rules_ui
from internal.logic.games import Blackjack
from main import Context

# Виджет ошибки
class AlertWidget(QErrorMessage):
    def __init__(self, err):
        super().__init__()
        self.showMessage(err)
        # self.setGeometry(300, 300, 200, 200)
        # self.setWindowTitle("Ошибка")
        # self.lbl = QLabel(self)
        # self.lbl.setText(err)
        # self.show()
        # self.activateWindow()


# Виджет окна входа в аккаунт
class AuthWidget(QMainWindow, auth_ooi.Ui_MainWindow):
    def __init__(self, ctx: Context, next: QWidget, *next_args):
        super().__init__()
        self.setupUi(self)

        self.ctx = ctx
        self.next = next
        self.next_args = next_args

        self.btn_login.clicked.connect(self.authenticate)
        self.btn_signup.clicked.connect(self.register)
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
    def authenticate(self):
        global _
        self.ctx.logger.debug('Пользователь хочет войти в аккаунт.')
        username = self.lbl_username.text()
        password = self.lbl_psw.text()
        try:
          if not self.ctx.db.check_user(username, password):
                self.ctx.logger.debug('Пароли не совпадают.')
                _ = AlertWidget('Неверный пароль!')
                return
        except IndexError:
            self.ctx.logger.debug('Пользователя с таким юзернеймом не существует.')
            _ = AlertWidget('Лудомана с таким именем не существует!')
            return
        
        # Пользователь прошел проверку аутентификации
        self.ctx.logger.debug('Пользователь прошел проверку аутентификации.')
        self.ctx.username = username
        self.grant_access(hash(username))
    # Метод на регистрацию пользователя
    def register(self):
        global _
        self.ctx.logger.debug('Пользователь хочет создать в аккаунт.')
        username = self.lbl_username.text()
        password = self.lbl_psw.text()
        try:
            self.ctx.db.check_user(username, password)
            self.ctx.logger.debug('Имя уже занято.')
            _ = AlertWidget('Лудоман с таким именем уже существет!')
            return
        except IndexError:
            self.ctx.db.register_user(username, password)
        
        # Пользователь успешно зарегистрирован
        self.ctx.logger.debug('Пользователь успешно зарегистрирован.')
        self.ctx.username = username
        self.grant_access(hash(username))
    
    
    # Метод успешного входа в аккаунт
    def grant_access(self, username_hash):
        global _
        now = dt.datetime.now()
        with open(self.ctx.timesfilepath, encoding='utf8') as f:
            for row in DictReader(f, ['username_hash', 'time'], delimiter=';'):
                if row['username_hash'] == username_hash:
                    absense_time = dt.datetime.strptime('%f', row['time']) - now
                    break
        _ = DrawStar()
        QTimer.singleShot(1500, self.proceed)
        # self.proceed()

        self.ctx.logger.debug('Вошли в аккаунт, показываем экран загрузки.')
    
    # Открываем следующий виджет и закрываем текущий
    def proceed(self):
        global _
        _ = self.next.show()
        self.destroy()


# Виджет главного меню
class MainMenuWidget(QMainWindow, menu_ooi.Ui_Blackjack):
    def __init__(self, ctx, info_widget, leaderboard_widget, rules_widget, *games_widgets):
        super().__init__()
        self.setupUi(self)

        self.bj_widget = games_widgets[0](ctx, Blackjack([], []))
        self.info_widget = info_widget(ctx)
        self.lb_widget = leaderboard_widget(ctx)
        self.rules_widget = rules_widget

        self.Begin_game.clicked.connect(self.StartBlackJack)
        self.Settings.clicked.connect(self.about)
        self.pushButton.clicked.connect(self.about)
        self.Records.clicked.connect(self.leaderboard)
    
    def StartBlackJack(self):
        # self.hide()
        self.bj_widget.show()
    
    def about(self):
        self.info_widget.show()
    
    def rules(self):
        self.rules_widget.show()
    
    def leaderboard(self):
        self.lb_widget.show()



# Виджет окна "О программе"
class Rules(QMainWindow, rules_ui.Ui_MainWindow):
    def __init__(self, ctx):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн

# Виджет окна "О программе"
class ProgramInfoWidget(QMainWindow, info_ooi.Ui_MainWindow):
    def __init__(self, ctx):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн


# Виджет окна с результатами и достижениями
class LeaderboardWidget(QMainWindow, lb_ui.Ui_records):
    def __init__(self, ctx):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.ctx = ctx
    
    def update_result(self):
        # Получили результат запроса, который ввели в текстовое поле
        result = self.ctx.db.getlb()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


# Виджет окна с игрой blackjack (двадцать одно)
class BlackJackWidget(QMainWindow, bj_ooi.Ui_MainWindow):
    def __init__(self, ctx, game):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн

        self.ctx = ctx
        self.btn_restart.clicked.connect(self.restart)

        self.player_slots = [self.playerCard1, self.playerCard2, self.playerCard3,
                      self.playerCard4, self.playerCard5, self.playerCard6,
                      self.playerCard7]
        self.dealer_slots = [self.dealerCard1, self.dealerCard2, self.dealerCard3,
                      self.dealerCard4, self.dealerCard5, self.dealerCard6,
                      self.dealerCard7]
        
        self.prepare_game(game)
    
    def restart(self):
        self.btn_hit.clicked.disconnect()
        self.btn_stand.clicked.disconnect()
        self.prepare_game(Blackjack([], []))
    
    def prepare_game(self, game):
        self.dealerCard6.hide()
        self.dealerCard7.hide()
        self.playerCard6.hide()
        self.playerCard7.hide()
        self.btn_hit.clicked.connect(self.hit_player)
        self.btn_stand.clicked.connect(self.stand_player)
        self.res_label.setText('')

        self.game = game
        self.player_cards_n = 0
        self.dealer_cards_n = 0

        pixmap = QPixmap('images/cards/rubashka_of_card')
        for i in range(1, 6):
            exec(f'self.playerCard{i}.setPixmap(pixmap)')
            exec(f'self.dealerCard{i}.setPixmap(pixmap)')
        
        dealer_cards, dealer_sum = self.game.start()
        for card in dealer_cards:
            suit = {'H': 'hearts', 'S': 'spades', 'C': 'clubs', 'D': 'diamonds'}[card[-1]]
            card_filepath = f"images/cards/{suit}/{str({'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(card[:-1], card[:-1]))}_of_{suit}"
            self.ctx.logger.debug('Берем карту из пути: ' + card_filepath)
            pixmap = QPixmap(card_filepath)

            self.dealer_slots[self.dealer_cards_n].setPixmap(pixmap)
            self.dealer_cards_n += 1
        self.dlabel.setText(f'Крупье: {dealer_sum}')


    def hit_player(self):
        self.ctx.logger.debug('Игрок берет карту')
        card, player_sum, dealer_sum = self.game.hit()
        print(player_sum)
        suit = {'H': 'hearts', 'S': 'spades', 'C': 'clubs', 'D': 'diamonds'}[card[-1]]
        card_filepath = f"images/cards/{suit}/{str({'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(card[:-1], card[:-1]))}_of_{suit}"
        self.ctx.logger.debug('Берем карту из пути: ' + card_filepath)
        pixmap = QPixmap(card_filepath)

        self.player_slots[self.player_cards_n].setPixmap(pixmap)
        self.player_cards_n += 1
        self.plabel.setText(f'Игрок: {player_sum}')
        if player_sum > 21:
            self.btn_hit.clicked.disconnect()
            self.btn_stand.clicked.disconnect()
            self.btn_hit.clicked.connect(self.laugh)
            self.btn_stand.clicked.connect(self.laugh)
            self.res_label.setText('ВЫ ПРОИГРАЛИ')
        elif player_sum == 21:
            self.stand_player()
        self.player_sum = player_sum
    
    def stand_player(self):
        self.ctx.logger.debug('Очередь крупье')
        dealer_cards, dealer_sum = self.game.stand()
        for card in dealer_cards:
            suit = {'H': 'hearts', 'S': 'spades', 'C': 'clubs', 'D': 'diamonds'}[card[-1]]
            card_filepath = f"images/cards/{suit}/{str({'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(card[:-1], card[:-1]))}_of_{suit}"
            self.ctx.logger.debug('Берем карту из пути: ' + card_filepath)
            pixmap = QPixmap(card_filepath)

            self.dealer_slots[self.dealer_cards_n].setPixmap(pixmap)
            self.dealer_cards_n += 1
        self.dlabel.setText(f'Крупье: {dealer_sum}')
        if dealer_sum > 21:
            self.btn_hit.clicked.disconnect()
            self.btn_stand.clicked.disconnect()
            self.btn_hit.clicked.connect(self.laugh)
            self.btn_stand.clicked.connect(self.laugh)
            self.res_label.setText('ВЫ ПОБЕДИЛИ')
        elif dealer_sum == self.player_sum:
            self.btn_hit.clicked.disconnect()
            self.btn_stand.clicked.disconnect()
            self.btn_hit.clicked.connect(self.laugh)
            self.btn_stand.clicked.connect(self.laugh)
            self.res_label.setText('НИЧЬЯ')

    

    def laugh(self):
        global _
        _ = AlertWidget('Игра закончена, руки прочь с карт :D')
        

class DrawStar(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setModal(True)
        self.prepare_star()
        self.show()

    def initUI(self):
        self.setGeometry(300, 200, *[500, 500])
        self.field = QImage()

    def paintEvent(self, event):
        self.myqp = QPainter()
        self.myqp.begin(self)
        # Изменяем цвет линии
        pen = QPen(Qt.GlobalColor.red, 2)
        self.myqp.setPen(pen)

        # Рисуем
        if self.i == -3:
            self.i += 1
            self.myqp.end()
            return
        if self.i == len(self.nodes2) - 2:
            self.timer.stop()
            self.flag = True
            self.myqp
            # QTimer.singleShot(200, lambda: self.destroy)
            self.myqp.end()
            self.hide()
            return
        # Отрисовываем то, что уже рисовали
        for i in range(-2, self.i):
            self.myqp.drawLine(*self.nodes2[i], *self.nodes2[i + 2])
        # Отрисовываем новую линию
        self.myqp.drawLine(*self.nodes2[self.i], *self.nodes2[self.i + 2])

        self.i += 1
        self.myqp.end()

    def xs(self, x):
        return x + [500, 500][0] // 2

    def ys(self, y):
        return [500, 500][1] // 2 - y

    def prepare_star(self):
        # Считаем координаты и переводим их в экранные
        self.nodes = [(200 * cos(i * 2 * pi / 5),
                        200 * sin(i * 2 * pi / 5))
                        for i in range(5)]
        self.nodes2 = [(int(self.xs(node[0])), int(self.ys(node[1]))) for node in self.nodes]

        self.i = -3
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(300)
    
    def test(self):
        print('tick')