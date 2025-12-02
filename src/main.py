from PyQt6.QtWidgets import QApplication

from di import resolve
from gui_app.main_window import MainWindow

if __name__ == '__main__':
    app = resolve(QApplication)
    window = MainWindow()
    window.show()
    app.exec()
