from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget

from components.message_box import MessageBox

class BiometricsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler