import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from components.text_field import TextField

class LoginPage(QWidget):
  def __init__(self, main_window):
    super().__init__()
    self.main_window = main_window
