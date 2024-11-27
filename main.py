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
    # Создаем экземпляры всех нужных классов и передаем их друг другу через аргументы
    # Так, например, класс окна аутентификации (AuthWidget) будет вызывать метод next.do() аргумента next,
    # где next - экземпляр класса виджета главного меню (MainMenuWidget)
    auther = wdt.AuthWidget(wdt.MainMenuWidget, wdt.ProgramInfoWidget, wdt.LeaderboardWidget, wdt.BlackJackWidget)
    auther.show()

    sys.exit(app.exec())
    