from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QLineEdit

class PromptDialog(QDialog):
  def __init__(self, title="Input Prompt", message="Please enter something:", parent=None):
    super().__init__(parent)
    self.setWindowTitle(title)
    self.parent = parent
    self.user_input = None

  def init_ui(self, message):
    self.layout = QVBoxLayout()