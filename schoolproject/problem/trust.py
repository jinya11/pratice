import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextBrowser, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer,Qt, pyqtSignal
from main.chap1 import Chap1Window


class TrustWindow(QWidget):
    switch_window = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('수평적 사고 퀴즈')
        self.setFixedSize(1000, 600)

        self.line_label1 = QLabel(self)
        self.line_label1.setText("숲속의 수영")
        self.line_label1.setGeometry(40, 20, 1000, 50)

        self.Question_browser = QTextBrowser(self)
        self.Question_browser.setText("""숲 속 깊은 곳에 한 사람이 죽어 있다. 그는 수영복과 스노클, 물안경을 끼고 있다. 가장 가까운 호수는 8마일 밖에 있으며, 바다는 100마일 이상 떨어져 있다. 그는 어떻게 죽은 것일까?\n\n죽은 사람의 근처는 불바다다""")
        font = QFont("맑은고딕", 15)
        self.Question_browser.setFont(font)
        self.Question_browser.setGeometry(80, 100, 400, 400)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Type your answer here")
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

        self.evidence_button3 = QPushButton(self)
        self.evidence_button3.setText("증거 3")
        self.evidence_button3.setGeometry(550, 300, 90, 40)
        self.evidence_button3.clicked.connect(self.show_evidence3)

        self.answer_label = QLabel(self)

    def show_evidence(self):
        self.evidence_open = Evidence()
        self.evidence_open.show()

    def show_evidence2(self):
        self.evidence_open2 = Evidence2()
        self.evidence_open2.show()

    def show_evidence3(self):
        self.evidence_open3 = Evidence3()
        self.evidence_open3.show()

    def check_answer(self):
        user_answer = self.input_field.text().strip().lower()
        correct_answer = '''숲 속에서 산불이 발생한 중에 
                          소방관이 불을 진압하기 위해 
                          호수에서 물을 가져오려다가, 
                          수영자를 집어 들었다.'''

        user_answer= user_answer.replace(',', '')
        important_words = {"소방관", "호수", "물"}



        # Check for common words
        user_words = set(user_answer.split())

        common_important_words_count = len(user_words.intersection(important_words))

        if common_important_words_count >= 2 or all(word in user_words for word in important_words):
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
        self.line_label1.setText("숲에서 무슨 일이 일어났는가?")
        self.line_label1.setGeometry(40, 30, 1000, 50)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("Yes")
        self.line_label2.setGeometry(120, 100, 1000, 50)

class Evidence2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('증거 2')
        self.setFixedSize(250, 200)

        self.line_label1 = QLabel(self)
        self.line_label1.setText("남자는 숲에서 죽었는가")
        self.line_label1.setGeometry(40, 30, 1000, 50)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("No")
        self.line_label2.setGeometry(120, 100, 1000, 50)

class Evidence3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('증거 3')
        self.setFixedSize(300, 200)

        self.line_label1 = QLabel(self)
        self.line_label1.setText(''''남자는 불을 끄는 과정에서 불행하게 죽었는가''')
        self.line_label1.setGeometry(20, 30, 1000, 50)

        self.line_label2 = QLabel(self)
        self.line_label2.setText("Yes")
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