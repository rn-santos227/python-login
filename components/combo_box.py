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

    self.setLayout(self.layout)

    if items:
      self.set_items(items)

  def get_selected_value(self):
    return self.combo_box.currentData()
  
  def get_selected_text(self):
    return self.combo_box.currentText()
  
  def set_label_text(self, text):
    self.label.setText(text)

  def set_items(self, items):
    self.combo_box.clear()
    for text, value in items:
      self.combo_box.addItem(text, value)

  def clear_selection(self):
    self.combo_box.setCurrentIndex(-1)