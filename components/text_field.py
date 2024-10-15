from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont

class TextField(QWidget):
  def __init__(self, label_text="Text Field", placeholder_text="Enter text...", parent=None):
    super().__init__(parent)
    self.init_ui(label_text, placeholder_text)

  def init_ui(self, label_text, placeholder_text):
    self.layout: QVBoxLayout = QVBoxLayout()

    self.label: QLabel = QLabel(label_text)
    self.text_field: QLineEdit = QLineEdit()
    self.text_field.setPlaceholderText(placeholder_text)

    label_font: QFont = QFont()
    label_font.setPointSize(14)
    self.label.setFont(label_font)
    self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    text_field_font: QFont = QFont()
    text_field_font.setPointSize(12)
    self.text_field.setFont(text_field_font)

    self.layout.addWidget(self.label)
    self.layout.addWidget(self.text_field)

    self.setLayout(self.layout)

  def get_text(self):
    return self.text_field.text()
  
  def set_text(self, text):
    self.text_field.setText(text)
  
  def set_label_text(self, text):
    self.label.setText(text)

  def set_placeholder_text(self, text):
    self.text_field.setPlaceholderText(text)

  def set_enabled(self, condition: bool = True):
    self.text_field.setEnabled(condition)

  def set_read_only(self, condition: bool = False):
    self.text_field.setReadOnly(condition)

  def set_width(value: int):
    pass

  def clear_text(self):
    self.text_field.clear()