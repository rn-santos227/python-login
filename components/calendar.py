from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class Calendar(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)