
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from components.button import Button
from components.message_box import MessageBox

class ScannerPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.students = []

  def init_ui(self):
    self.main_layout = QVBoxLayout()

    self.setLayout(self.main_layout)