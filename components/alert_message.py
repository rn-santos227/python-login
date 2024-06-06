from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class AlertMessage(QWidget):
  def __init__(self, message="", alert_type="info", parent=None):
    super().__init__(parent)
    self.init_ui(message, alert_type)

  def init_ui(self, message, alert_type):
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    self.label = QLabel(message)
    self.label.setAlignment(Qt.AlignCenter)

    self.layout.addWidget(self.label)

  def set_alert_type(self, alert_type):
    if alert_type == "success":
      self.label.setStyleSheet("color: white; background-color: green; padding: 10px; border-radius: 5px;")

    elif alert_type == "warning":
      self.label.setStyleSheet("color: black; background-color: yellow; padding: 10px; border-radius: 5px;")