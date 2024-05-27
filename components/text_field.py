from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel

class TextField(QWidget):
  def __init__(self, label_text="Text Field", placeholder_text="Enter text...", parent=None):
    super().__init__(parent)
    self.init_ui(label_text, placeholder_text)

  def init_ui(self, label_text, placeholder_text):
    self.layout = QVBoxLayout()

    self.label = QLabel(label_text)
    self.text_field = QLineEdit()