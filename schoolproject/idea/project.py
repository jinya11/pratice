## 초기안

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from main import chap1

class GameWindow(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle('Game Window')
        self.setFixedSize(1000, 700)
        self.game_label = QLabel(self)
        self.game_label.setText(f"Welcome, {name}! This is the Game Window")
        self.game_label.setGeometry(50,30,220,50)

        self.line_label = QLabel(self)
        self.line_label.setText("=" * 200)
        self.line_label.setGeometry(0, 40, 1000, 50)

        self.chap1button = QPushButton(self)
        self.chap1button.setText("1")
        self.chap1button.setGeometry(350, 200, 300, 300)
        self.chap1button.clicked.connect(self.chap1open)
                                    # x   #y

        self.creditbutton = QPushButton(self)
        self.creditbutton.setText("credit")
        self.creditbutton.setGeometry(900,10,50,50)
        self.creditbutton.clicked.connect(self.creditopen)

    def creditopen(self):
        self.creditopen = creditWindow()
        self.creditopen.show()

    def chap1open(self):
        self.chap1open = chap1.Chap1Window()
        self.chap1open.show()
        self.close()

class NameInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Name Input')

        self.name_label = QLabel('Enter your name:')
        self.name_input = QLineEdit()
        self.name_label2 = QLabel('이름 결정 시 Enter로 진행')

        layout = QVBoxLayout(self)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.name_label2)
        self.setLayout(layout)

        self.name_input.returnPressed.connect(self.openGameWindow)



    def openGameWindow(self):
        name = self.name_input.text()
        self.game_window = GameWindow(name)
        self.game_window.show()
        self.close()


class creditWindow(QWidget):
    def __init__(self):
        super().__init__()
        file_path = file_path = r"../main/credit.txt.txt"

        try:
            with open("../main/credit.txt.txt", "r", encoding="utf-8") as file:
                credit_content = file.read()
        except FileNotFoundError:
            credit_content = "Credit file not found."
        self.setWindowTitle('credit')
        self.setFixedSize(500,700)
        self.credit_label = QLabel(self)
        self.credit_label.setText(credit_content)
        layout = QVBoxLayout(self)
        layout.addWidget(self.credit_label)
        self.setLayout(layout)


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    print(traceback.format_exc())
    exit(1)

if __name__ == '__main__':
    sys.excepthook = exception_hook
    qapp = QApplication(sys.argv)
    input_window = NameInputWindow()
    input_window.show()
    sys.exit(qapp.exec())
