# 실험 상에서 사용하였던 코드


#self.right_button = QPushButton(self)
 #       self.right_button.setText(">")
  ##     self.right_button.clicked.connect(self.onRightButtonClick)

    #    self.left_button = QPushButton(self)
     #   self.left_button.setText("<")
      #  self.left_button.setGeometry(300, 400, 50, 50)
       # self.left_button.clicked.connect(self.onLeftButtonClick)

#self.text_browser = QTextBrowser(self)
#self.text_browser.setPlainText("도구")
#self.text_browser.setGeometry(40, 100, 300, 400)

#self.text_browser.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
# eventFilter 등록
#self.text_browser.installEventFilter(self)

#self.texts = ["도구", "두 번째 텍스트", "세 번째 텍스트"]
 #       self.current_text_index = 0


#def onRightButtonClick(self):
 #   if self.current_text_index < len(self.texts) - 1:
  #      self.current_text_index += 1
   #     self.text_browser.setPlainText(self.texts[self.current_text_index])


#def onLeftButtonClick(self):
 #   if self.current_text_index > 0:
  #      self.current_text_index -= 1
   #     self.text_browser.setPlainText(self.texts[self.current_text_index])


#def eventFilter(self, obj, event):
 #   if obj == self.text_browser and event.type() == QEvent.Type.KeyPress:
  #      if event.key() == Qt.Key.Key_Z:
   #         self.show_tool_item()
    #        return True
     #   return False
    #return super().eventFilter(obj, event)

#def show_tool_item(self):
 #   self.tool_list_dialog = ToolListDialog(self.inventory)
  #  self.tool_list_dialog.exec()


#def use_tool_item(self):
 #   if "도구" in self.inventory:
  #      self.inventory.remove("도구")
   #     self.line_label1 = QLabel(self)
     #   self.line_label1.setText("탈출 성공")
    #    self.line_label1.setGeometry(40, 20, 1000, 50)
      #  sys.exit()
    #else:
     #   self.line_label1 = QLabel(self)
      #  self.line_label1.setText("도구가 없습니다.")
       # self.line_label1.setGeometry(400, 20, 1000, 50)

# class NameInputWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Name Input')
#
#         self.name_label = QLabel('Enter your name:')
#         self.name_input = QLineEdit()
#         self.name_label2 = QLabel('이름 결정 시 Enter로 진행')
#
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.name_label)
#         layout.addWidget(self.name_input)
#         layout.addWidget(self.name_label2)
#         self.setLayout(layout)
#
#         self.name_input.returnPressed.connect(self.openGameWindow)


# chap1_window = next((widget for widget in QApplication.topLevelWidgets() if isinstance(widget, Chap1Window)),
#                             None)
#         if chap1_window is None:
#             chap1_window = Chap1Window()