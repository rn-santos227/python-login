from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QFont

class Label(QWidget):
  def __init__(self, label_text="Text Field", parent=None):
    super().__init__(parent)
    self.init_ui(label_text)

  def init_ui(self, label_text):
    self.label: QLabel = QLabel(label_text)

    label_font: QFont = QFont()
    label_font.setPointSize(14)
    self.label.setFont(label_font)
    self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

  def set_text(self, text):
    self.label.setText(text)