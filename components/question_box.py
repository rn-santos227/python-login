from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

class DynamicQuestionBox(QDialog):
  def __init__(self, title="Question", message="Are you sure?", parent=None):
    super().__init__(parent)
    self.setWindowTitle(title)

  def init_ui(self, message):
    self.layout = QVBoxLayout()

    self.message_label = QLabel(message)
    self.layout.addWidget(self.message_label)

    self.button_layout = QHBoxLayout()