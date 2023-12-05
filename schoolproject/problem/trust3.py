import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextBrowser, QLineEdit, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from main.chap1 import Chap1Window

class TrustWindow(QWidget):
    switch_window = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('추리')
        self.setFixedSize(1000, 600)

        self.line_label1 = QLabel(self)
        self.line_label1.setText("범인 찾기")
        self.line_label1.setGeometry(40, 20, 1000, 50)

        file_path = r"../main/trust3.txt"

        try:
            with open("../main/trust3.txt", "r", encoding="utf-8") as file:
                Question_content = file.read()
        except FileNotFoundError:
            Question_content = "file not found."
        self.Question_browser = QTextBrowser(self)
        self.Question_browser.setText(Question_content)
        font = QFont("맑은고딕", 15)
        self.Question_browser.setFont(font)
        self.Question_browser.setGeometry(80, 100, 400, 400)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("거짓말 하고 있는 한명을 적으세요")
        self.input_field.setGeometry(550, 470, 300, 30)

        self.enter_button = QPushButton(self)
        self.enter_button.setText("Enter")
        self.enter_button.setGeometry(850, 465, 40, 40)
        self.enter_button.clicked.connect(self.check_answer)


        self.line_label2 = QLabel(self)
        self.line_label2.setText("=" * 200)
        self.line_label2.setGeometry(0, 500, 2000, 50)

        self.evidence_button = QPushButton(self)
        self.evidence_button.setText("증거 1")
        self.evidence_button.setGeometry(550, 200, 90, 40)
        self.evidence_button.clicked.connect(self.show_evidence)
        self.evidence_button.hide()
        self.ishide1 = True

        self.evidence_button2 = QPushButton(self)
        self.evidence_button2.setText("증거 2")
        self.evidence_button2.setGeometry(800, 200, 90, 40)
        self.evidence_button2.clicked.connect(self.show_evidence2)
        self.evidence_button2.hide()
        self.ishide2 = True

        self.answer_label = QLabel(self)
        self.incorrect_label = QLabel(self)
        self.time_end_label = QLabel(self)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(645, 120, 200, 15)

        self.start_progress_button = QPushButton(self)
        self.start_progress_button.setGeometry(645, 140, 100, 30)
        self.start_progress_button.setText("시작")
        self.start_progress_button.clicked.connect(self.start_progress)
        self.start_cnt = 1

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

    def update_progress(self):
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 1)

            if current_value == 25:
                if self.ishide1:
                    self.evidence_button.show()
                    self.ishide1 = False

            else:
                if current_value == 50 :
                    self.evidence_button2.show()

        if current_value >= 100:
            self.timer.stop()
            QTimer.singleShot(3000, self.hide_evidence_button)
            self.time_end_label.setGeometry(705, 140, 150, 30)
            self.time_end_label.setText(f"버튼 표시 남은 시간: 3 초")

    def start_progress(self):
        # Start the QTimer to simulate progress
        self.progress_bar.setValue(0)
        self.timer.start(500)  # Set the interval (milliseconds)

        if self.start_cnt == 1:
            self.start_progress_button.hide()
            self.start_cnt += 1

    def show_hide_button(self):
        self.evidence_button2.show()
        self.ishide2 = True

    def show_evidence(self):
        self.evidence_open = Evidence()
        self.evidence_open.show()

    def show_evidence2(self):
        self.another_evidence_open2 = Evidence2()
        self.another_evidence_open2.show()

    def hide_evidence_button(self):
        self.evidence_button.hide()
        self.evidence_button2.hide()

    def check_answer(self):
        user_answer = self.input_field.text().strip()
        correct_answer = "B"

        # Check for common words

        if user_answer == correct_answer:
            self.answer_label.setText("정답. 3초 후 이전 화면으로 돌아갑니다.")
            self.answer_label.setGeometry(550, 500, 300, 30)

            self.timer = QTimer(self)

            self.timer.start(3000)  # 3000 milliseconds (3 seconds)
            self.timer.timeout.connect(self.go_back_to_chap1)


        else:

            self.answer_label.setText("오답 ")
            self.answer_label.setGeometry(550, 500, 300, 30)

    def go_back_to_chap1(self):
        self.switch_window.emit()
        self.timer.timeout.disconnect(self.go_back_to_chap1)
        self.timer.stop()
        self.close()





class Evidence(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('힌트 1')
        self.setFixedSize(250, 200)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("모순을 찾는 것이 중요")
        self.line_label2.setGeometry(90, 70, 1000, 50)

class Evidence2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('힌트 2')
        self.setFixedSize(300, 200)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("두명에게 주목")
        self.line_label2.setGeometry(60, 70, 1000, 50)



def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    print(traceback.format_exc())
    exit(1)

if __name__ == '__main__':
    sys.excepthook = exception_hook
    qapp = QApplication(sys.argv)
    trust_window = TrustWindow()
    chap1_window = Chap1Window()

    trust_window.switch_window.connect(chap1_window.show)
    chap1_window.switch_window.connect(trust_window.show)

    trust_window.show()
    sys.exit(qapp.exec())