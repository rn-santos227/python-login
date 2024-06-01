from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont

class Button(QWidget):
  def __init__(self, button_text="Button", parent=None):
    super().__init__(parent)
    self.init_ui(button_text)