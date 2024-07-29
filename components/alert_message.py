from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class AlertMessage(QWidget):
  def __init__(self, message="", alert_type="info", parent=None):
    super().__init__(parent)
    self.init_ui(message, alert_type)

  def init_ui(self, message, alert_type):
    self.layout: QVBoxLayout = QVBoxLayout()
    self.setLayout(self.layout)

    self.label: QLabel = QLabel(message)
    self.label.setAlignment(Qt.AlignCenter)

    self.layout.addWidget(self.label)
    self.set_alert_type(alert_type)

  def set_alert_type(self, alert_type):
    if alert_type == "success":
      self.label.setStyleSheet("color: white; background-color: green; padding: 10px; border-radius: 5px;")

    elif alert_type == "warning":
      self.label.setStyleSheet("color: black; background-color: yellow; padding: 10px; border-radius: 5px;")

    elif alert_type == "error":
      self.label.setStyleSheet("color: white; background-color: red; padding: 10px; border-radius: 5px;")

    else:
      self.label.setStyleSheet("color: black; background-color: lightgrey; padding: 10px; border-radius: 5px;")

  def set_message(self, message):
    self.label.setText(message)