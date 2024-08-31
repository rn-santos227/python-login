from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from handlers.biometrics_handler import BiometricsHandler

class Biometrics(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.init_ui()

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)