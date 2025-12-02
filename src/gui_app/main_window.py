from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('SQL trainer')

        button = QPushButton('Press me')
        button.clicked.connect(self.the_button_was_clicked)

        self.setFixedSize(QSize(800, 600))

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print('Clicked')
