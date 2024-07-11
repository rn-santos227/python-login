from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateEdit
from PyQt5.QtCore import QDate

class DateField(QWidget):
  def __init__(self, label_text="Select Date", parent=None):
    super().__init__(parent)