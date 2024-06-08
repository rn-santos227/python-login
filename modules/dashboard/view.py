from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt

class DashboardPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    layout = QHBoxLayout(self)