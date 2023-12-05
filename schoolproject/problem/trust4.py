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

        file_path = r"../main/trust4.txt"

        try:
            with open("../main/trust4.txt", "r", encoding="utf-8") as file:
                Question_content = file.read()
        except FileNotFoundError:
            Question_content = "Credit file not found."
        self.Question_browser = QTextBrowser(self)
        self.Question_browser.setText(Question_content)
        font = QFont("맑은고딕", 15)
        self.Question_browser.setFont(font)
        self.Question_browser.setGeometry(80, 100, 400, 400)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("3번의 답변 기회")
        self.input_field.setGeometry(550, 470, 300, 30)
        self.answer_cnt = 3

        self.count_label = QLabel(self)
        self.count_label.setText(f"답변 기회 {self.answer_cnt}번")
        self.count_label.setGeometry(800,415,100,60)

        self.enter_button = QPushButton(self)
        self.enter_button.setText("Enter")
        self.enter_button.setGeometry(850, 465, 40, 40)
        self.enter_button.clicked.connect(self.check_answer)


        self.line_label2 = QLabel(self)
        self.line_label2.setText("=" * 200)
        self.line_label2.setGeometry(0, 500, 2000, 50)

        self.answer_label = QLabel(self)



    def check_answer(self):
        if self.answer_cnt <=1:
            self.input_field.setPlaceholderText("3회 실패")
            self.enter_button.hide()
            timer = QTimer(self)
            timer.timeout.connect(self.go_back_to_chap1)
            timer.start(3000)


        user_answer = self.input_field.text().strip().lower()
        correct_answer = "59초"

        if user_answer == correct_answer:
            self.answer_label.setText("정답 3초 후 이전 화면으로 돌아갑니다.")
            self.answer_label.setGeometry(550, 500, 300, 30)

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.go_back_to_chap1)
            self.timer.start(3000)  # 3000 milliseconds (3 seconds)

        else:
            self.answer_label.setText("오답")
            self.answer_label.setGeometry(550, 500, 300, 30)
            self.answer_cnt -=1
            self.count_label.setText(f"답변 기회 {self.answer_cnt}번")


    def go_back_to_chap1(self):
        self.switch_window.emit()
        self.timer.timeout.disconnect(self.go_back_to_chap1)
        self.timer.stop()
        self.close()



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