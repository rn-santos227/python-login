from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout

class QuestionBox(QDialog):
  def __init__(self, title="Question", message="Are you sure?", parent=None):
    super().__init__(parent)
    self.setWindowTitle(title)
    self.init_ui(message)

  def init_ui(self, message):
    self.layout: QVBoxLayout = QVBoxLayout()

    self.message_label: QLabel = QLabel(message)
    self.layout.addWidget(self.message_label)

    self.button_layout: QHBoxLayout = QHBoxLayout()
    self.yes_button: QPushButton = QPushButton("Yes")
    self.yes_button.clicked.connect(self.accept)
    self.button_layout.addWidget(self.yes_button)
    
    self.no_button: QPushButton = QPushButton("No")
    self.no_button.clicked.connect(self.reject)
    self.button_layout.addWidget(self.no_button)
    
    self.layout.addLayout(self.button_layout)
    self.setLayout(self.layout)