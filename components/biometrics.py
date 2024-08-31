from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from handlers.biometrics_handler import BiometricsHandler

class Biometrics(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.biometrics_handler: BiometricsHandler = BiometricsHandler()
    self.init_ui()

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)
    self.label = QLabel(self)
    self.layout.addWidget(self.label)