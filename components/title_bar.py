from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class TitleBar(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)