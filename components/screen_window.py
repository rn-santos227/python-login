from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt

class ScreenWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowFlags(Qt.FramelessWindowHint)
    self.showFullScreen()

    self.stacked_widget = QStackedWidget()