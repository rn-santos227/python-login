
from PyQt5.QtWidgets import QWidget, QVBoxLayout

class ScannerPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.students = []

  def init_ui(self):
    self.main_layout = QVBoxLayout()