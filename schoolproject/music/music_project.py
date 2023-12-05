import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt6.QtCore import QUrl, pyqtSignal
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
import os
import re
from main.chap1 import Chap1Window

class Music(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Window')
        self.setFixedSize(1000, 600)
        icon_path = r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\music\music1.png"
        self.setWindowIcon(QIcon(icon_path))

        self.line_label = QLabel(self)
        self.line_label.setText("=" * 200)
        self.line_label.setGeometry(0, 40, 1000, 50)

        self.no_song_label = QLabel(self)

        self.image_label = QLabel(self)
        pixmap = QPixmap(r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\music\music.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(400, 100, 300, 300)

        self.player_input = QLineEdit(self)
        self.player_input.setPlaceholderText("음악 듣고 노래 맞추기")
        self.player_input.setGeometry(400, 400, 150, 20)

        self.enter_button = QPushButton(self)
        self.enter_button.setText("Enter")
        self.enter_button.setGeometry(555, 390, 40, 40)
        self.enter_button.clicked.connect(self.check_answer)

        self.end_button = QPushButton(self)
        self.end_button.setText("End")
        self.end_button.setGeometry(900, 10, 50, 50)
        self.end_button.clicked.connect(self.go_back_to_chap1)

        self.play_button = QPushButton(self)
        self.play_button.setText(">")
        self.play_button.setGeometry(480, 450, 30, 30)
        self.play_button.clicked.connect(self.play_music)

        self.next_song_button = QPushButton(self)
        self.next_song_button.setText("다음 노래")
        self.next_song_button.setGeometry(550, 450, 100, 30)
        self.next_song_button.clicked.connect(self.play_next_song)
        self.next_song_button.hide()

        self.music_directory = r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\main\musicdir"
        self.music_list = os.listdir(self.music_directory)  # 노래 목록 가져오기

        self.correct_answer_path = r"C:\Users\SAMSUNG\OneDrive\바탕 화면\schoolproject\main\musicinfo.txt"

        self.current_index = 0

        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput(self)
        self.media_player.setAudioOutput(self.audio_output)

        self.answer_label = QLabel(self)


    def check_answer(self):
        user_answer = self.player_input.text().strip()

        with open(self.correct_answer_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            correct_answers = [re.findall(r'\b([^\(\)\[\]\{\}-]+)\b', line) for line in lines]
            correct_answers = [tuple(word for word in words) for words in correct_answers]
            correct_answers = [item for item in correct_answers if item]

            # word 제거하는 부분 추가
            word = ("mv", "-", " ")
            correct_answers = [item for item in correct_answers if not any(w in word for w in item)]



        user_set = set(user_answer.split())

        for correct_line in correct_answers:
            # Convert correct_line tuple to a set after removing spaces
            correct_line_set = set(word.replace(" ", "") for word in correct_line)
            print(correct_line_set)
            # Check if user's answer is a subset of the correct answer
            if ' ' in user_answer:
                # user_answer에 문장이 없으면 오답 처리
                self.answer_label.setText("공백 오답")
                self.answer_label.setGeometry(400, 430, 300, 30)
                return

            if user_set.issubset(correct_line_set):
                self.answer_label.setText("정답")
                self.answer_label.setGeometry(400, 430, 300, 30)

                self.next_song_button.setEnabled(True)
                self.next_song_button.show()
                break  # 정답을 찾았으므로 반복 중단

        else:
            self.answer_label.setText("오답")
            self.answer_label.setGeometry(400, 430, 300, 30)
            self.next_song_button.setEnabled(False)
            self.next_song_button.hide()

    def play_media(self, index):
        if self.media_player.mediaStatus() == QMediaPlayer.MediaStatus.LoadingMedia or \
                self.media_player.mediaStatus() == QMediaPlayer.MediaStatus.BufferedMedia:
            self.media_player.stop()

        if index < len(self.music_list):
            file_name = self.music_list[index]
            file_path = os.path.join(self.music_directory, file_name)

            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.audio_output.setVolume(50)  # 볼륨 설정
            self.media_player.play()

            self.answer_label.clear()
            self.player_input.clear()

        else:
            self.no_song_label.setText("재생할 노래가 없습니다.")
            self.no_song_label.setGeometry(200, 300, 300, 30)

    def play_music(self):
        self.play_media(self.current_index)
        self.play_media(self.current_index)  # 임시조치 라이브러리 쪽 오류

    def play_next_song(self):
        if self.current_index < len(self.music_list) - 1:
            print(self.music_list)
            self.current_index += 1
            self.media_player.stop()
            self.play_media(self.current_index)

            self.answer_label.clear()
            self.next_song_button.hide()
            self.player_input.setPlaceholderText("음악 듣고 노래 맞추기")

        else:
            self.no_song_label.setText("재생할 노래가 없습니다.")
            self.no_song_label.setGeometry(200, 300, 300, 30)

    def go_back_to_chap1(self):
        self.switch_window.emit()
        self.media_player.stop()
        self.close()



def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    print(traceback.format_exc())
    exit(1)

if __name__ == '__main__':
    sys.excepthook = exception_hook
    qapp = QApplication(sys.argv)

    music_window = Music()
    chap1_window = Chap1Window()

    music_window.switch_window.connect(chap1_window.show)
    chap1_window.switch_window.connect(music_window.show)

    input_window = Music()
    input_window.show()
    sys.exit(qapp.exec())
