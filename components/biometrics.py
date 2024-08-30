from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class Biometrics(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)