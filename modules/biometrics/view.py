from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QWidget

from components.message_box import MessageBox

from modules.biometrics.model import Biometric

class BiometricsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box: MessageBox = MessageBox(self)
    self.students: list[Biometric] = []

  def init_ui(self):
    content_frame: QFrame = QFrame(self)