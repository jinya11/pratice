import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextBrowser, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from main.chap1 import Chap1Window


class TrustWindow(QWidget):
    switch_window = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('수평적 사고 퀴즈')
        self.setFixedSize(1000, 600)

        self.line_label1 = QLabel(self)
        self.line_label1.setText("무죄의 이유")
        self.line_label1.setGeometry(40, 20, 1000, 50)

        file_path = file_path = r"../main/trust2.txt"

        try:
            with open("../main/trust2.txt", "r", encoding="utf-8") as file:
                Question_content = file.read()
        except FileNotFoundError:
            Question_content = "Credit file not found."
        self.Question_browser = QTextBrowser(self)
        self.Question_browser.setText(Question_content)
        font = QFont("맑은고딕", 15)
        self.Question_browser.setFont(font)
        self.Question_browser.setGeometry(80, 100, 400, 400)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("문장 형식으로 작성해야 합니다.(.필수)")
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

        self.evidence_button2 = QPushButton(self)
        self.evidence_button2.setText("증거 2")
        self.evidence_button2.setGeometry(800, 200, 90, 40)
        self.evidence_button2.clicked.connect(self.show_evidence2)

        self.answer_label = QLabel(self)


        self.incorrect_label = QLabel(self)




    def show_evidence(self):
        self.evidence_open = Evidence()
        self.evidence_open.show()

    def show_evidence2(self):
        self.evidence_open2 = Evidence2()
        self.evidence_open2.show()

    def check_answer(self):
        user_answer = self.input_field.text().strip().lower()
        correct_answer = ('''남자는 빌련덕 책을 다시 도서관에 반납했다. 
                            반납기일이 많이 지났기 때문에 5.4유로를 지불한 것이다.
                            도서관 사서의 행동은 위법이 아니다.''')

        important_words = {"도서관", "반납기일", "반납일", "위법", "법을 어기다", "빌린", "늦게", "돌려주다", "지났기", "때문에", "때문이다."}

        user_answer = user_answer.replace(',', '')
        if '.' not in user_answer or not user_answer.strip():
            # user_answer에 문장이 없으면 오답 처리
            self.answer_label.setText("오답: 문장이 없습니다.")
            self.answer_label.setGeometry(550, 500, 300, 30)
            return

        # Check for common words
        user_words = set(user_answer.split())

        common_important_words_count = len(user_words.intersection(important_words))

        if common_important_words_count >= 2 or common_important_words_count == len(important_words):
            self.answer_label.setText("정답 3초 후 이전 창으로 돌아갑니다.")
            self.answer_label.setGeometry(550, 500, 300, 30)

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.go_back_to_chap1)
            self.timer.start(3000)  # 3000 milliseconds (3 seconds)
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
        self.setWindowTitle('증거 1')
        self.setFixedSize(250, 200)

        self.line_label1 = QLabel(self)
        self.line_label1.setText("장소가 어디인가?")
        self.line_label1.setGeometry(40, 30, 1000, 50)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("책이 많은 공간")
        self.line_label2.setGeometry(120, 100, 1000, 50)

class Evidence2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('증거 2')
        self.setFixedSize(300, 200)

        self.line_label1 = QLabel(self)
        self.line_label1.setText("둘다 위법 행위 또한 법에 어긋난 행동을 했는가?")
        self.line_label1.setGeometry(20, 30, 1000, 50)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("No")
        self.line_label2.setGeometry(120, 100, 1000, 50)



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