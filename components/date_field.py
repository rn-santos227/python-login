from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateEdit
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

    self.layout.addWidget(self.label)
    self.layout.addWidget(self.date_field)
    self.setLayout(self.layout)