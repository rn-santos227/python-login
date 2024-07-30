from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt

from config.config import app_name

class TitleBar(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.init_ui()

  def init_ui(self):
    self.setFixedHeight(30) 

    layout: QHBoxLayout = QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    self.title: QLabel = QLabel(app_name)
    self.title.setAlignment(Qt.AlignCenter)

    self.close_button: QPushButton = QPushButton("X")
    self.close_button.setFixedSize(30, 30)
    self.close_button.setStyleSheet("QPushButton { font-size: 20px; padding: 0; margin: 0; }")
    self.close_button.clicked.connect(self.close_window)

    layout.addWidget(self.title)
    layout.addWidget(self.close_button)

    self.setLayout(layout)

  def close_window(self):
    self.window().close()