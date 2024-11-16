import sys
from PyQt6.QtWidgets import QApplication
from internal.logic.widgets import AuthWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AuthWidget()
    ex.show()
    sys.exit(app.exec())
