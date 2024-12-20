import sys
from os import chdir, getcwd
from os.path import abspath
from PyQt6.QtWidgets import QApplication

import internal.logic.widgets as wdt
from internal.logic.database import Database
from internal.logic.logging import logger


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def normalize_path():
    path = abspath(getcwd())
    if '/' in path and path.split('/')[-2] == 'dist' or '\\' in path and path.split('\\')[-2] == 'dist':
        chdir('../..')


class Context():
    def __init__(self, database: Database, logger, users_last_time_table_filepath):
        self.db = database
        self.logger = logger
        self.timesfilepath = users_last_time_table_filepath
        self.username = ''

if __name__ == '__main__':
    global _
    # Ловим ошибки
    sys.excepthook = except_hook
    normalize_path()

    app = QApplication(sys.argv)
    # Объявляем экземпляры всех мспользуемых классов и передаем их друг другу через аргументы
    # Так, класс окна аутентификации (AuthWidget) будет создавать экземпляр интерфейса next,
    # где next - класс виджета главного меню (MainMenuWidget)
    filepath = 'internal/database/database.db'
    ludomania_rates_filepath = 'internal/database/ludomania.csv'
    ctx = Context(Database(filepath), logger, ludomania_rates_filepath)
    auther = wdt.AuthWidget(
        ctx,
        wdt.MainMenuWidget(ctx, wdt.ProgramInfoWidget, wdt.LeaderboardWidget, wdt.Rules, wdt.BlackJackWidget)
    )
    auther.show()

    exit_status = app.exec()
    auther.ctx.db.conn.close()
    sys.exit(exit_status)
