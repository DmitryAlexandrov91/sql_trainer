from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('SQL trainer')

        button = QPushButton('Press me')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled) 

        self.setFixedSize(QSize(800, 600))

        self.setCentralWidget(button)

    def the_button_was_clicked(self) -> None:
        print('Clicked')

    def the_button_was_toggled(self, checked) -> None:
        self.button_is_checked = checked
        print(self.button_is_checked)
