import sys
from PyQt6.QtWidgets import QApplication
import internal.logic.widgets as wdt
from internal.logic.logging import logger


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    # Ловим ошибки
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    # Объявляем экземпляры всех мспользуемых классов и передаем их друг другу через аргументы
    # Так, класс окна аутентификации (AuthWidget) будет создавать экземпляр интерфейса next,
    # где next - класс виджета главного меню (MainMenuWidget)
    auther = wdt.AuthWidget(wdt.MainMenuWidget, wdt.ProgramInfoWidget, wdt.LeaderboardWidget, wdt.BlackJackWidget)
    auther.show()
    # todo: передать логгер
    # todo: собственно логировать события

    sys.exit(app.exec())
    
