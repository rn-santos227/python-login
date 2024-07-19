from PyQt5.QtWidgets import QDateEdit, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate

class DateField(QWidget):
  def __init__(self, label_text="Select Date", parent=None):
    super().__init__(parent)
    self.init_ui(label_text)

  def init_ui(self, label_text):
    self.layout = QVBoxLayout()

    self.label = QLabel(label_text)
    self.date_field = QDateEdit()
    self.date_field.setCalendarPopup(True)
    self.date_field.setDate(QDate.currentDate())

    label_font = QFont()
    label_font.setPointSize(14)
    self.label.setFont(label_font)
    self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    label_font = QFont()
    label_font.setPointSize(12)
    self.date_field.setFont(label_font)

    self.layout.addWidget(self.label)
    self.layout.addWidget(self.date_field)
    self.setLayout(self.layout)

  def get_date(self):
    return self.date_field.date().toString("yyyy-MM-dd")
  
  def set_date(self, date_str):
      self.date_edit.setDate(QDate.fromString(date_str, "yyyy-MM-dd"))