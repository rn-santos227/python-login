from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont

class Button(QWidget):
  def __init__(self, button_text="Button", parent=None):
    super().__init__(parent)
    self.init_ui(button_text)

  def init_ui(self, button_text):
    self.layout = QVBoxLayout()
    self.button = QPushButton(button_text)
    self.button.setFixedWidth(250) 

    button_font = QFont()
    button_font.setPointSize(12)
    self.button.setFont(button_font)

    self.layout.addWidget(self.button)
    self.setLayout(self.layout)

  def set_button_text(self, text):
    self.button.setText(text)