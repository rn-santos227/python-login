import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

class FullScreenWindow(QMainWindow):
  def __init__(self):
    super().__init__()