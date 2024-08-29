from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget

from components.message_box import MessageBox

from modules.biometrics.model import Biometric

class BiometricsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.message_box: MessageBox = MessageBox(self)
    self.pages_handler = pages_handler