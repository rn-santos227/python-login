from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QFont

class ComboBox(QWidget):
  def __init__(self, label_text="Combo Box", items=None, parent=None):
    super().__init__(parent)
    self.init_ui(label_text, items)

  def init_ui(self, label_text, items):
    self.layout = QVBoxLayout()

    self.label = QLabel(label_text)
    self.combo_box = QComboBox()

    label_font = QFont()
    label_font.setPointSize(14)
    self.label.setFont(label_font)

    combo_box_font = QFont()
    combo_box_font.setPointSize(12)
    self.combo_box.setFont(combo_box_font)

    self.layout.addWidget(self.label)
    self.layout.addWidget(self.combo_box)