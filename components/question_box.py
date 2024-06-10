from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

class QuestionBox(QDialog):
  def __init__(self, title="Question", message="Are you sure?", parent=None):
    super().__init__(parent)
    self.setWindowTitle(title)
    self.init_ui(message)

  def init_ui(self, message):
    self.layout = QVBoxLayout()

    self.message_label = QLabel(message)
    self.layout.addWidget(self.message_label)

    self.button_layout = QHBoxLayout()
    self.yes_button = QPushButton("Yes")
    self.yes_button.clicked.connect(self.accept)
    self.button_layout.addWidget(self.yes_button)
    
    self.no_button = QPushButton("No")
    self.no_button.clicked.connect(self.reject)
    self.button_layout.addWidget(self.no_button)
    
    self.layout.addLayout(self.button_layout)
    self.setLayout(self.layout)