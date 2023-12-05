# 스페이스 연타 프로그램.

import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QTextBrowser
from PyQt6.QtCore import Qt, QTimer

class Machine(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Machine Repair')
        self.setFixedSize(500, 400)

        self.spacebar_counter = 0
        self.machine_repairing = False
        self.key_space = False;

        self.text_label = QLabel(self)
        self.text_label.setGeometry(50, 50, 400, 30)

        self.machine_repairing_browser = QTextBrowser(self)
        self.machine_repairing_browser.setText("기계 수리 (스페이스바 연타)")
        self.machine_repairing_browser.setGeometry(100, 100, 200, 30)

        self.spacebar_timer = QTimer(self)
        self.spacebar_timer.timeout.connect(self.check_spacebar_counter)
        self.spacebar_timer.start(100)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.key_space = True
            self.spacebar_counter += 1

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.key_space = False
            self.spacebar_counter = 0

    def start_machine_repair(self):
        self.machine_repairing = True
        self.spacebar_counter = 0
        self.machine_repairing_browser.setText(self.repair)

    def repair(self):
        if self.machine_repairing and self.spacebar_counter >= 10:
            self.machine_repairing_browser.setText("수리 성공")
            self.machine_repairing = False
            self.machine_window.hide()


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    print(traceback.format_exc())
    exit(1)

if __name__ == '__main__':
    sys.excepthook = exception_hook
    qapp = QApplication(sys.argv)
    machine_window = Machine()
    machine_window.show()
    sys.exit(qapp.exec())
