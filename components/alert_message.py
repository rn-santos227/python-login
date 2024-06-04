from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class AlertMessage(QWidget):
  def __init__(self, message="", alert_type="info", parent=None):
    super().__init__(parent)