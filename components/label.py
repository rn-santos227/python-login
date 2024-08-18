from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QFont

class Label(QWidget):
  def __init__(self, label_text="Text Field", parent=None):
    super().__init__(parent)
    self.init_ui(label_text)

  def init_ui(self, label_text):
    self.label: QLabel = QLabel(label_text)