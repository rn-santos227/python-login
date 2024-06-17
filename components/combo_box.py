from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QFont

class ComboBox(QWidget):
  def __init__(self, label_text="Combo Box", items=None, parent=None):
    super().__init__(parent)

  def init_ui(self, label_text, items):
    self.layout = QVBoxLayout()