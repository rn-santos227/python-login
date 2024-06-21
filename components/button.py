from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont

class Button(QWidget):
  def __init__(self, button_text="Button", parent=None):
    super().__init__(parent)
    self.init_ui(button_text)

  def init_ui(self, button_text):
    self.layout = QVBoxLayout()
    self.button = QPushButton(button_text)
    self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    button_font = QFont()
    button_font.setPointSize(12)
    self.button.setFont(button_font)

    self.layout.addWidget(self.button)
    self.setLayout(self.layout)

  def set_button_text(self, text):
    self.button.setText(text)

  def connect_signal(self, slot):
    self.button.clicked.connect(slot)

  def set_fixed_width(self, width):
    self.button.setFixedWidth(width)

  def set_font_size(self, size):
    button_font = self.button.font()
    button_font.setPointSize(size)
    self.button.setFont(button_font)

  def set_bg_color(self, color="white"):
    self.button.setStyleSheet(f"background-color: {color};")

  def set_font_color(self, color="black"):
    self.button.setStyleSheet(f"color: {color};")
