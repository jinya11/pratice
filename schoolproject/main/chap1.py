
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import os
from pytube import YouTube
from PyQt6.QtCore import pyqtSignal


class Chap1Window(QWidget):
    switch_window = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Game Window')
        self.setFixedSize(1000, 700)
        self.game_label = QLabel(self)
        self.game_label.setText(f"Welcome, This is the Game Window")
        self.game_label.setGeometry(50,30,220,50)

        self.line_label = QLabel(self)
        self.line_label.setText("=" * 200)
        self.line_label.setGeometry(0, 40, 1000, 50)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("=" * 200)
        self.line_label2.setGeometry(0, 600, 1000, 50)

        self.trust1_button = QPushButton(self)
        self.trust1_button.setText("숲속의 수영")
        self.trust1_button.setGeometry(600, 400, 70, 40)
        self.trust1_button.clicked.connect(lambda: self.trust1open())

        self.trust2_button = QPushButton(self)
        self.trust2_button.setText("무죄의 원인")
        self.trust2_button.setGeometry(500, 400, 70, 40)
        self.trust2_button.clicked.connect(lambda: self.trust2open())

        self.trust3_button = QPushButton(self)
        self.trust3_button.setText("거짓말쟁이")
        self.trust3_button.setGeometry(400, 400, 70, 40)
        self.trust3_button.clicked.connect(lambda: self.trust3open())

        self.trust4_button = QPushButton(self)
        self.trust4_button.setText("일수 추리")
        self.trust4_button.setGeometry(300, 400, 70, 40)
        self.trust4_button.clicked.connect(lambda: self.trust4open())

        self.music_button = QPushButton(self)
        self.music_button.setText("음악 맞추기 게임")
        self.music_button.setGeometry(450, 300, 100, 40)
        self.music_button.clicked.connect(lambda : self.musicopen())

        self.creditbutton = QPushButton(self)
        self.creditbutton.setText("credit")
        self.creditbutton.setGeometry(900,10,50,50)
        self.creditbutton.clicked.connect(self.creditopen)

        self.music_add_button = QPushButton(self)
        self.music_add_button.setText("music add")
        self.music_add_button.setGeometry(877, 70, 100, 50)
        self.music_add_button.clicked.connect(self.musicaddopen)

        self.bugbutton = QPushButton(self)
        self.bugbutton.setText("bug report")
        self.bugbutton.setGeometry(877, 120, 80, 50)
        self.bugbutton.clicked.connect(self.bug_report_open)

        self.open_button = QPushButton(self)
        self.open_button.setText("open")
        self.open_button.setGeometry(900, 170, 50, 50)
        self.open_button.clicked.connect(self.open_music_txt)

        self.trust_open = None
        self.music_game_open = None


    def creditopen(self):
        self.creditopen = creditWindow()
        self.creditopen.show()

    def bug_report_open(self):
        self.bug_report_open = BugreportWindow()
        self.bug_report_open.show()


    def musicaddopen(self):
        self.musicaddopen = Musicadd()
        self.musicaddopen.show()

    def trust1open(self):
        if not self.trust_open:
            from problem.trust import TrustWindow
            self.trust_open1 = TrustWindow()
            self.trust_open1.switch_window.connect(self.show_main_menu)
        self.trust_open1.show()
        self.close()

    def trust2open(self):
        if not self.trust_open:
            from problem.trust2 import TrustWindow
            self.trust_open2 = TrustWindow()
            self.trust_open2.switch_window.connect(self.show_main_menu)
        self.trust_open2.show()
        self.close()

    def trust3open(self):
        if not self.trust_open:
            from problem.trust3 import TrustWindow
            self.trust_open3 = TrustWindow()
            self.trust_open3.switch_window.connect(self.show_main_menu)
        self.trust_open3.show()
        self.close()

    def trust4open(self):
        if not self.trust_open:
            from problem.trust4 import TrustWindow
            self.trust_open4 = TrustWindow()
            self.trust_open4.switch_window.connect(self.show_main_menu)
        self.trust_open4.show()
        self.close()

    def musicopen(self):
        if not self.music_game_open:
            from music.music_project import Music
            self.music_game_open = Music()
            self.music_game_open.switch_window.connect(self.show_main_menu)
        self.music_game_open.show()
        self.close()

    def show_main_menu(self):
        self.show()

    def open_music_txt(self):
        self.open_txt = Music_credit()
        self.open_txt.show()

class Musicadd(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Music Add Window')
        self.setFixedSize(400, 200)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter the YouTube URL")

        self.download_button = QPushButton("Download and Add")
        self.download_button.clicked.connect(self.download_and_add)

        layout = QVBoxLayout(self)
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)
        self.setLayout(layout)

    def download_and_add(self):
        url = self.url_input.text()

        if not url:
            return

        yt = YouTube(url)
        download_path = r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\main\musicdir"
        filePath = yt.streams.filter(only_audio=True).first().download(download_path)
        mp3FilePath = filePath.replace('mp4', 'mp3')
        os.rename(filePath, mp3FilePath)

        song_title = yt.title

        txt_file_path = f"C:\\Users\\SAMSUNG\\OneDrive\\바탕 화면\\schoolproject\\main\\musicinfo.txt"
        with open(txt_file_path, 'a', encoding='utf-8') as txt_file:
            txt_file.write(f"{song_title}\n")

        # Check if the file exists, and create it if not
        if not os.path.exists(mp3FilePath):
            with open(mp3FilePath, 'w'):  # Create an empty file
                pass

class Music_credit(QWidget):
    def __init__(self):
        super().__init__()

        try:
            with open(r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\main\musicinfo.txt", "r", encoding="utf-8") as file:
                credit_content = file.read()
        except FileNotFoundError:
            credit_content = "file not found."
        self.setWindowTitle('Music Credit')
        self.setFixedSize(500, 700)
        self.credit_label = QLabel(self)
        self.credit_label.setText(credit_content)
        layout = QVBoxLayout(self)
        layout.addWidget(self.credit_label)
        self.setLayout(layout)

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

class BugreportWindow(QWidget):
    def __init__(self):
        super().__init__()
        file_path = file_path = r"../main/버그 정리표.txt"

        try:
            with open("../main/버그 정리표.txt", "r", encoding="utf-8") as file:
                credit_content = file.read()
        except FileNotFoundError:
            credit_content = "file not found."
        self.setWindowTitle('bug report')
        self.setFixedSize(700,700)
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

    chap1_window = Chap1Window()
    chap1_window.show()
    sys.exit(qapp.exec())
