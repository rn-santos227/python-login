from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel

class TextField(QWidget):
  def __init__(self, label_text="Text Field", placeholder_text="Enter text...", parent=None):
    super().__init__(parent)
    self.init_ui(label_text, placeholder_text)

  def init_ui(self, label_text, placeholder_text):
    self.layout = QVBoxLayout()

    self.label = QLabel(label_text)
    self.text_field = QLineEdit()
    self.text_field.setPlaceholderText(placeholder_text)
    self.text_field.setFixedWidth(500)

    self.layout.addWidget(self.label)
    self.layout.addWidget(self.text_field)

    self.setLayout(self.layout)

  def get_text(self):
    return self.text_field.text()
  
  def set_label_text(self, text):
    self.label.setText(text)

  def set_placeholder_text(self, text):
    self.text_field.setPlaceholderText(text)

  def clear_text(self):
    self.text_field.clear()